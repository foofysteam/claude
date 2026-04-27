<?php

require_once __DIR__ . '/Http.php';

final class ClaudeClient
{
    private const API_URL = 'https://api.anthropic.com/v1/messages';
    private const API_VERSION = '2023-06-01';

    public function __construct(
        private readonly string $apiKey,
        private readonly string $model,
        private readonly string $effort = 'medium'
    ) {
    }

    /**
     * Analyze a shop-design image and return a structured work order.
     *
     * @param string $imageBytes  Raw image bytes.
     * @param string $imageMime   e.g. image/png, image/jpeg.
     * @param string $userNotes   Optional free-text notes from the requester.
     * @return array{title:string, description:string, materials:array<int,array{item:string,quantity:string}>, dimensions:array<int,string>, raw:array}
     */
    public function generateWorkOrder(string $imageBytes, string $imageMime, string $userNotes = ''): array
    {
        $b64 = base64_encode($imageBytes);

        $systemPrompt = <<<'TXT'
You are a senior shop foreman generating a fabrication work order from a shop design drawing.

Analyze the image carefully. Identify the part / sign / assembly being fabricated, the materials specified, the dimensions and tolerances called out, and any finishing or assembly notes.

Output a single JSON object that matches the requested schema. If a field cannot be determined from the drawing, return a sensible best-effort value rather than failing — for example, an empty list for materials when none are visible. Keep the title under 80 characters and write the description in clear, imperative shop-floor language.
TXT;

        $userContent = [
            [
                'type' => 'image',
                'source' => [
                    'type' => 'base64',
                    'media_type' => $imageMime,
                    'data' => $b64,
                ],
            ],
            [
                'type' => 'text',
                'text' => trim(
                    "Generate a complete work order for the attached shop design.\n\n"
                    . ($userNotes !== '' ? "Additional notes from requester:\n{$userNotes}" : '')
                ),
            ],
        ];

        $payload = [
            'model' => $this->model,
            'max_tokens' => 4096,
            'thinking' => ['type' => 'adaptive'],
            'system' => $systemPrompt,
            'messages' => [
                ['role' => 'user', 'content' => $userContent],
            ],
            'output_config' => [
                'effort' => $this->effort,
                'format' => [
                    'type' => 'json_schema',
                    'schema' => $this->schema(),
                ],
            ],
        ];

        $response = Http::request('POST', self::API_URL, [
            'x-api-key' => $this->apiKey,
            'anthropic-version' => self::API_VERSION,
        ], $payload, 180);

        if ($response['status'] !== 200 || $response['json'] === null) {
            $detail = $response['json']['error']['message'] ?? substr($response['body'], 0, 500);
            throw new RuntimeException("Anthropic API error ({$response['status']}): {$detail}");
        }

        $text = '';
        foreach ($response['json']['content'] ?? [] as $block) {
            if (($block['type'] ?? '') === 'text') {
                $text .= $block['text'];
            }
        }

        $decoded = json_decode($text, true);
        if (!is_array($decoded)) {
            throw new RuntimeException('Claude response did not contain valid JSON: ' . substr($text, 0, 300));
        }

        return [
            'title' => (string) ($decoded['title'] ?? 'Untitled work order'),
            'description' => (string) ($decoded['description'] ?? ''),
            'materials' => array_values(array_map(
                static fn($m) => [
                    'item' => (string) ($m['item'] ?? ''),
                    'quantity' => (string) ($m['quantity'] ?? ''),
                ],
                $decoded['materials'] ?? []
            )),
            'dimensions' => array_values(array_map('strval', $decoded['dimensions'] ?? [])),
            'raw' => $decoded,
        ];
    }

    private function schema(): array
    {
        return [
            'type' => 'object',
            'properties' => [
                'title' => [
                    'type' => 'string',
                    'description' => 'Short, descriptive title for the work order (≤80 chars).',
                ],
                'description' => [
                    'type' => 'string',
                    'description' => 'Detailed shop-floor instructions describing what to fabricate.',
                ],
                'materials' => [
                    'type' => 'array',
                    'description' => 'Materials and components called out in the drawing.',
                    'items' => [
                        'type' => 'object',
                        'properties' => [
                            'item' => ['type' => 'string'],
                            'quantity' => ['type' => 'string'],
                        ],
                        'required' => ['item', 'quantity'],
                        'additionalProperties' => false,
                    ],
                ],
                'dimensions' => [
                    'type' => 'array',
                    'description' => 'Key dimensions / specs visible in the drawing.',
                    'items' => ['type' => 'string'],
                ],
            ],
            'required' => ['title', 'description', 'materials', 'dimensions'],
            'additionalProperties' => false,
        ];
    }
}
