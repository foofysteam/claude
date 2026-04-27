<?php
/**
 * Work Order Web App — configuration.
 *
 * Copy this file to config.php on the server and fill in your credentials.
 * config.php is gitignored and protected by .htaccess from web access.
 */

return [
    // Anthropic API key — get one at https://console.anthropic.com/
    'anthropic_api_key' => 'sk-ant-...',

    // Notion internal integration token — create one at
    // https://www.notion.so/profile/integrations and share the target
    // database with the integration.
    'notion_token' => 'ntn_...',

    // Claude model used for shop-design vision analysis.
    'claude_model' => 'claude-opus-4-7',

    // Effort level: low | medium | high | xhigh | max
    // medium balances quality and token spend; high gives more thorough output.
    'claude_effort' => 'medium',

    // Maximum image upload size in bytes (default 10 MB). The Anthropic vision
    // endpoint accepts up to ~5 MB base64-encoded.
    'max_upload_bytes' => 10 * 1024 * 1024,
];
