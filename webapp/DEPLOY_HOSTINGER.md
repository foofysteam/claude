# Deploying to Hostinger (shared hosting)

The app is plain PHP 8.1+ with cURL — no Composer, no build step. You can
upload it through Hostinger's File Manager (hPanel) in about five minutes.

## 1. Prerequisites

- A Hostinger Premium / Business shared hosting plan (any plan that supports
  PHP 8.1 or newer — most do by default).
- A domain or subdomain pointed at that hosting account.
- An Anthropic API key — https://console.anthropic.com/.
- A Notion internal integration token + a database shared with that
  integration — https://www.notion.so/profile/integrations.

## 2. Verify the PHP version in hPanel

1. Log in to hPanel → **Hosting** → your domain → **Advanced** → **PHP Configuration**.
2. Set PHP version to **8.1** or newer.
3. In **PHP Options**, confirm:
   - `allow_url_fopen = On`
   - `upload_max_filesize >= 12M`
   - `post_max_size >= 12M`
   - `max_execution_time >= 240`
   - `memory_limit >= 128M`

## 3. Upload the app

Pick one of:

### A. File Manager (easiest)

1. Zip the `webapp/` directory locally:
   ```bash
   cd /path/to/repo
   zip -r webapp.zip webapp -x 'webapp/uploads/*' 'webapp/config.php'
   ```
2. hPanel → **Files** → **File Manager** → open `public_html/`.
3. Click **Upload Files** → upload `webapp.zip`.
4. Right-click the zip → **Extract**. Optionally move the contents of
   `public_html/webapp/` up into `public_html/` if you want the app served
   at the root of the domain instead of `/webapp/`.

### B. SFTP

1. hPanel → **Files** → **FTP Accounts** → grab credentials.
2. Use FileZilla / Cyberduck to upload `webapp/` into `public_html/`.

## 4. Configure credentials

1. In File Manager, open `public_html/webapp/` (or wherever you uploaded).
2. Right-click `config.example.php` → **Copy** → rename copy to `config.php`.
3. Right-click `config.php` → **Edit**. Fill in:
   - `anthropic_api_key`
   - `notion_token`
4. Save.

> `config.php` is denied to the web by `.htaccess` — make sure you keep that
> file in place.

## 5. Set folder permissions

The `uploads/` directory is only used to satisfy PHP's temporary upload path
on some shared hosts and is web-blocked. Confirm permissions in File Manager:

- `uploads/` → **0755**
- `config.php` → **0640** (or 0644 if 0640 is rejected)
- `lib/`, `assets/` → **0755**

## 6. Share the Notion database with your integration

This is the single most-missed step. From Notion:

1. Open the target database as a full page.
2. Top-right **•••** menu → **Connections** (or **Add connections**).
3. Search for your integration name → click to add.
4. Confirm by re-opening the menu — you should see the integration listed.

Without this, the app returns
`Notion API error fetching database (404): Could not find database…`.

## 7. Try it

1. Visit `https://yourdomain.com/webapp/` (or `/` if you moved files up).
2. Paste the Notion database URL.
3. Upload a PNG/JPG of a shop design.
4. (Optional) Add notes.
5. Click **Generate work order**.

The first request takes ~15-40 s while Claude analyzes the image. On success
you'll see a link to the new Notion page; on failure you'll see the error
message inline.

## 8. Watching errors

If something goes wrong and you don't see a useful flash message:

1. hPanel → **Files** → **File Manager** → `public_html/webapp/`.
2. Look for an `error_log` file in the same directory or in `public_html/`.
3. Or in hPanel: **Advanced** → **PHP Configuration** → enable
   `log_errors` and check the path it writes to.

## Updating the app

Re-upload the changed PHP files via File Manager or SFTP. Settings live in
`config.php` and are not overwritten as long as you don't upload a new
`config.php`.

## Tearing it down

Delete the `webapp/` directory in `public_html/`. The app stores nothing
permanent on the server beyond the config file you created.
