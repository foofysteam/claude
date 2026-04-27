<?php

final class Http
{
    /**
     * @param array<string,string>     $headers  Header name => value pairs.
     * @param string|array<string,mixed>|null $body  Raw string, or array (JSON-encoded), or null.
     * @return array{status:int, body:string, json: ?array}
     */
    public static function request(
        string $method,
        string $url,
        array $headers = [],
        string|array|null $body = null,
        int $timeout = 120
    ): array {
        $ch = curl_init();
        $curlHeaders = [];
        foreach ($headers as $name => $value) {
            $curlHeaders[] = "{$name}: {$value}";
        }

        if (is_array($body)) {
            $body = json_encode($body, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
            $hasContentType = false;
            foreach ($curlHeaders as $h) {
                if (stripos($h, 'content-type:') === 0) {
                    $hasContentType = true;
                    break;
                }
            }
            if (!$hasContentType) {
                $curlHeaders[] = 'Content-Type: application/json';
            }
        }

        curl_setopt_array($ch, [
            CURLOPT_URL => $url,
            CURLOPT_CUSTOMREQUEST => $method,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $curlHeaders,
            CURLOPT_TIMEOUT => $timeout,
            CURLOPT_CONNECTTIMEOUT => 30,
            CURLOPT_SSL_VERIFYPEER => true,
            CURLOPT_SSL_VERIFYHOST => 2,
        ]);

        if ($body !== null) {
            curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
        }

        $response = curl_exec($ch);
        $status = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $err = curl_error($ch);
        curl_close($ch);

        if ($response === false) {
            throw new RuntimeException("HTTP request failed: {$err}");
        }

        $json = json_decode((string) $response, true);
        return [
            'status' => $status,
            'body' => (string) $response,
            'json' => is_array($json) ? $json : null,
        ];
    }
}
