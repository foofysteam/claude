# Shop Design → Notion Work Order

A small PHP web app for Hostinger shared hosting. Upload a shop design image
and a Notion database URL — the app reads the drawing with Claude vision and
adds a fully-populated work order row to the database.

## Architecture

```
 Browser ──▶ index.php (form)
              │
              ▼
           submit.php
              │  1. Validate + read upload
              │  2. ClaudeClient::generateWorkOrder()  → Anthropic Messages API (vision + JSON schema)
              │  3. NotionClient::uploadFile()          → Notion file upload API
              │  4. NotionClient::createPageInDatabase()→ Notion pages API
              ▼
        Redirect back to index.php with success / error flash
```

No database, no composer dependencies, no Node — just PHP 8.1+ and cURL,
which Hostinger shared hosting includes by default.

## Files

| Path                  | Purpose |
|-----------------------|---------|
| `index.php`           | Upload form |
| `submit.php`          | Handles the submission and orchestrates Claude + Notion |
| `lib/ClaudeClient.php`| Calls Anthropic Messages API (Opus 4.7, vision, structured outputs) |
| `lib/NotionClient.php`| Notion REST client: DB lookup, file upload, page creation |
| `lib/Http.php`        | Tiny cURL wrapper used by both clients |
| `lib/Config.php`      | Loads `config.php` |
| `config.example.php`  | Template — copy to `config.php` and fill in credentials |
| `assets/style.css`    | Form styling |
| `.htaccess`           | Blocks direct access to `lib/`, `uploads/`, `config.php` |

## Deploying to Hostinger (shared hosting)

See `DEPLOY_HOSTINGER.md` for the full step-by-step guide.

## Local sanity check

```bash
cp config.example.php config.php
# edit config.php with real credentials
php -S 127.0.0.1:8080
# open http://127.0.0.1:8080
```

## Credentials you need

1. **Anthropic API key** — https://console.anthropic.com/ → API Keys.
2. **Notion internal integration token** — https://www.notion.so/profile/integrations
   → New integration → copy the "Internal Integration Secret".
3. **Share the target Notion database with the integration** — open the
   database in Notion → ••• menu → "Connections" → add your integration.
   Without this step, Notion returns 404 on the database lookup.

## Notion database schema

The app maps the work order onto whatever properties your database has:

- **Title property** (always present) ← Claude-generated title
- A `rich_text` property named `Description` / `Notes` / `Details` (optional) ← description
- A `rich_text` property named `Materials` / `Bill of Materials` (optional) ← bill of materials
- A `rich_text` property named `Dimensions` / `Specs` (optional) ← dimensions
- A `files` property (any name; first one wins, optional) ← shop design image

Anything that doesn't fit a property is appended to the page body as
headings + bullets, so no information is lost.
