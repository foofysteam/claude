<?php

require_once __DIR__ . '/Http.php';

final class NotionClient
{
    private const API_BASE = 'https://api.notion.com/v1';
    private const NOTION_VERSION = '2022-06-28';

    public function __construct(private readonly string $token)
    {
    }

    /**
     * Pull the 32-character object ID out of a Notion URL.
     *
     * Notion URLs look like:
     *   https://www.notion.so/workspace/Title-abcdef0123456789abcdef0123456789?v=...
     *   https://www.notion.so/abcdef01-2345-6789-abcd-ef0123456789
     */
    public static function extractIdFromUrl(string $url): string
    {
        // Database ID lives in the path (e.g. ".../Title-<id>"); the ?v=<view-id>
        // querystring carries an unrelated view ID and must be ignored.
        $path = parse_url($url, PHP_URL_PATH) ?? $url;

        if (preg_match('/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/', $path, $m)) {
            $hex = str_replace('-', '', $m[0]);
        } elseif (preg_match_all('/[0-9a-fA-F]{32}/', $path, $m)) {
            // Take the LAST 32-hex run in the path — Notion appends the ID at
            // the end of the slug (e.g. "/My-Database-<id>").
            $hex = end($m[0]);
        } else {
            throw new InvalidArgumentException(
                'Could not find a Notion ID in the URL. Make sure you copied the full URL of a Notion database.'
            );
        }

        return sprintf(
            '%s-%s-%s-%s-%s',
            substr($hex, 0, 8),
            substr($hex, 8, 4),
            substr($hex, 12, 4),
            substr($hex, 16, 4),
            substr($hex, 20, 12),
        );
    }

    public function getDatabase(string $databaseId): array
    {
        $response = Http::request('GET', self::API_BASE . "/databases/{$databaseId}", $this->headers());
        if ($response['status'] !== 200 || $response['json'] === null) {
            $detail = $response['json']['message'] ?? substr($response['body'], 0, 500);
            throw new RuntimeException("Notion API error fetching database ({$response['status']}): {$detail}");
        }
        return $response['json'];
    }

    /**
     * Create a page in a database. $properties must already match the DB schema.
     * $children is an optional array of block objects appended to the page body.
     */
    public function createPageInDatabase(string $databaseId, array $properties, array $children = []): array
    {
        $payload = [
            'parent' => ['database_id' => $databaseId],
            'properties' => $properties,
        ];
        if (!empty($children)) {
            $payload['children'] = $children;
        }
        $response = Http::request('POST', self::API_BASE . '/pages', $this->headers(), $payload);
        if ($response['status'] !== 200 || $response['json'] === null) {
            $detail = $response['json']['message'] ?? substr($response['body'], 0, 800);
            throw new RuntimeException("Notion API error creating page ({$response['status']}): {$detail}");
        }
        return $response['json'];
    }

    /**
     * Upload a file to Notion using the File Upload API and return the file_upload id
     * that can be referenced from image / file blocks and properties.
     */
    public function uploadFile(string $filename, string $mime, string $bytes): string
    {
        $createResp = Http::request('POST', self::API_BASE . '/file_uploads', $this->headers(), [
            'mode' => 'single_part',
            'filename' => $filename,
            'content_type' => $mime,
        ]);
        if ($createResp['status'] !== 200 || $createResp['json'] === null) {
            $detail = $createResp['json']['message'] ?? substr($createResp['body'], 0, 500);
            throw new RuntimeException("Notion file upload create failed ({$createResp['status']}): {$detail}");
        }
        $uploadId = $createResp['json']['id'] ?? null;
        $uploadUrl = $createResp['json']['upload_url'] ?? null;
        if (!$uploadId || !$uploadUrl) {
            throw new RuntimeException('Notion file upload response missing id or upload_url.');
        }

        $boundary = '----WebKitFormBoundary' . bin2hex(random_bytes(8));
        $body = "--{$boundary}\r\n"
            . "Content-Disposition: form-data; name=\"file\"; filename=\""
            . str_replace('"', '', $filename) . "\"\r\n"
            . "Content-Type: {$mime}\r\n\r\n"
            . $bytes . "\r\n"
            . "--{$boundary}--\r\n";

        $sendResp = Http::request('POST', $uploadUrl, [
            'Authorization' => 'Bearer ' . $this->token,
            'Notion-Version' => self::NOTION_VERSION,
            'Content-Type' => "multipart/form-data; boundary={$boundary}",
        ], $body, 180);

        if ($sendResp['status'] !== 200 || $sendResp['json'] === null) {
            $detail = $sendResp['json']['message'] ?? substr($sendResp['body'], 0, 500);
            throw new RuntimeException("Notion file upload send failed ({$sendResp['status']}): {$detail}");
        }

        return $uploadId;
    }

    /**
     * Map a generated work order onto a Notion database's actual property schema.
     * Picks the title property automatically and fills any matching rich_text /
     * select / multi_select / files property by name (case-insensitive).
     *
     * Returns ['properties' => [...], 'unmapped' => [...]] so the caller can
     * surface anything that didn't fit into the schema as page content instead.
     */
    public function buildPropertiesFromWorkOrder(array $databaseSchema, array $workOrder, ?string $imageUploadId = null): array
    {
        $schemaProps = $databaseSchema['properties'] ?? [];
        $properties = [];
        $unmapped = ['materials' => $workOrder['materials'], 'dimensions' => $workOrder['dimensions']];

        $titlePropName = null;
        foreach ($schemaProps as $name => $def) {
            if (($def['type'] ?? null) === 'title') {
                $titlePropName = $name;
                break;
            }
        }
        if ($titlePropName === null) {
            throw new RuntimeException('Notion database has no title property — cannot create row.');
        }
        $properties[$titlePropName] = [
            'title' => [['type' => 'text', 'text' => ['content' => $workOrder['title']]]],
        ];

        $fillRichText = function (string $name, string $value) use (&$properties, $schemaProps): bool {
            foreach ($schemaProps as $propName => $def) {
                if (strcasecmp($propName, $name) !== 0) {
                    continue;
                }
                if (($def['type'] ?? null) === 'rich_text') {
                    $properties[$propName] = [
                        'rich_text' => [['type' => 'text', 'text' => ['content' => $value]]],
                    ];
                    return true;
                }
            }
            return false;
        };

        $descriptionFilled = $fillRichText('Description', $workOrder['description'])
            || $fillRichText('Notes', $workOrder['description'])
            || $fillRichText('Details', $workOrder['description']);

        if ($workOrder['materials']) {
            $matText = implode("\n", array_map(
                static fn($m) => "- {$m['item']} ({$m['quantity']})",
                $workOrder['materials']
            ));
            if ($fillRichText('Materials', $matText) || $fillRichText('Bill of Materials', $matText)) {
                unset($unmapped['materials']);
            }
        }

        if ($workOrder['dimensions']) {
            $dimText = implode("\n", $workOrder['dimensions']);
            if ($fillRichText('Dimensions', $dimText) || $fillRichText('Specs', $dimText)) {
                unset($unmapped['dimensions']);
            }
        }

        if ($imageUploadId !== null) {
            foreach ($schemaProps as $propName => $def) {
                if (($def['type'] ?? null) === 'files') {
                    $properties[$propName] = [
                        'files' => [[
                            'name' => 'shop-design',
                            'type' => 'file_upload',
                            'file_upload' => ['id' => $imageUploadId],
                        ]],
                    ];
                    break;
                }
            }
        }

        return [
            'properties' => $properties,
            'unmapped' => $unmapped,
            'description_in_property' => $descriptionFilled,
        ];
    }

    /**
     * Build a list of Notion block objects to append as the page body so any
     * data that didn't fit the schema is still readable inside the page.
     */
    public function buildPageContentBlocks(array $workOrder, array $unmapped, ?string $imageUploadId, bool $descriptionInProperty): array
    {
        $blocks = [];

        if ($imageUploadId !== null) {
            $blocks[] = [
                'object' => 'block',
                'type' => 'image',
                'image' => [
                    'type' => 'file_upload',
                    'file_upload' => ['id' => $imageUploadId],
                ],
            ];
        }

        if (!$descriptionInProperty && $workOrder['description'] !== '') {
            $blocks[] = $this->headingBlock('Description');
            foreach ($this->splitParagraphs($workOrder['description']) as $para) {
                $blocks[] = $this->paragraphBlock($para);
            }
        }

        if (!empty($unmapped['materials'])) {
            $blocks[] = $this->headingBlock('Materials');
            foreach ($workOrder['materials'] as $m) {
                $blocks[] = $this->bulletBlock("{$m['item']} — {$m['quantity']}");
            }
        }

        if (!empty($unmapped['dimensions'])) {
            $blocks[] = $this->headingBlock('Dimensions / Specs');
            foreach ($workOrder['dimensions'] as $d) {
                $blocks[] = $this->bulletBlock($d);
            }
        }

        return $blocks;
    }

    private function headingBlock(string $text): array
    {
        return [
            'object' => 'block',
            'type' => 'heading_2',
            'heading_2' => [
                'rich_text' => [['type' => 'text', 'text' => ['content' => $text]]],
            ],
        ];
    }

    private function paragraphBlock(string $text): array
    {
        return [
            'object' => 'block',
            'type' => 'paragraph',
            'paragraph' => [
                'rich_text' => [['type' => 'text', 'text' => ['content' => $text]]],
            ],
        ];
    }

    private function bulletBlock(string $text): array
    {
        return [
            'object' => 'block',
            'type' => 'bulleted_list_item',
            'bulleted_list_item' => [
                'rich_text' => [['type' => 'text', 'text' => ['content' => $text]]],
            ],
        ];
    }

    private function splitParagraphs(string $text): array
    {
        $parts = preg_split("/\n\s*\n/", trim($text)) ?: [trim($text)];
        return array_values(array_filter(array_map('trim', $parts), static fn($p) => $p !== ''));
    }

    private function headers(): array
    {
        return [
            'Authorization' => 'Bearer ' . $this->token,
            'Notion-Version' => self::NOTION_VERSION,
        ];
    }
}
