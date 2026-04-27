<?php

final class Config
{
    private static ?array $values = null;

    public static function load(): array
    {
        if (self::$values !== null) {
            return self::$values;
        }

        $path = __DIR__ . '/../config.php';
        if (!is_file($path)) {
            throw new RuntimeException(
                'config.php not found. Copy config.example.php to config.php '
                . 'and fill in your Anthropic + Notion credentials.'
            );
        }

        $values = require $path;
        if (!is_array($values)) {
            throw new RuntimeException('config.php must return an array.');
        }

        foreach (['anthropic_api_key', 'notion_token', 'claude_model'] as $required) {
            if (empty($values[$required])) {
                throw new RuntimeException("Missing required config key: {$required}");
            }
        }

        self::$values = $values;
        return $values;
    }

    public static function get(string $key, mixed $default = null): mixed
    {
        $values = self::load();
        return $values[$key] ?? $default;
    }
}
