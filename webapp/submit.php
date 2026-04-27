<?php
session_start();

require_once __DIR__ . '/lib/Config.php';
require_once __DIR__ . '/lib/ClaudeClient.php';
require_once __DIR__ . '/lib/NotionClient.php';

set_time_limit(240);

function flashAndRedirect(string $kind, string $message, ?string $pageUrl = null): never
{
    $_SESSION['flash'] = [
        'kind' => $kind,
        'message' => $message,
        'page_url' => $pageUrl,
    ];
    header('Location: index.php');
    exit;
}

try {
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        flashAndRedirect('error', 'Form must be submitted via POST.');
    }

    $config = Config::load();

    $notionUrl = trim($_POST['notion_url'] ?? '');
    $notes = trim($_POST['notes'] ?? '');
    $_SESSION['last_notion_url'] = $notionUrl;
    $_SESSION['last_notes'] = $notes;

    if ($notionUrl === '') {
        flashAndRedirect('error', 'Notion URL is required.');
    }

    if (!isset($_FILES['shop_design']) || $_FILES['shop_design']['error'] !== UPLOAD_ERR_OK) {
        $err = $_FILES['shop_design']['error'] ?? 'no file';
        flashAndRedirect('error', "Shop design upload failed (error code: {$err}).");
    }

    $maxBytes = (int) ($config['max_upload_bytes'] ?? 10 * 1024 * 1024);
    if ($_FILES['shop_design']['size'] > $maxBytes) {
        $maxMb = round($maxBytes / (1024 * 1024), 1);
        flashAndRedirect('error', "Image is larger than the {$maxMb} MB limit.");
    }

    $tmpPath = $_FILES['shop_design']['tmp_name'];
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mime = $finfo->file($tmpPath) ?: 'application/octet-stream';
    if (!in_array($mime, ['image/png', 'image/jpeg'], true)) {
        flashAndRedirect('error', "Unsupported image type: {$mime}. Please upload a PNG or JPG.");
    }
    $bytes = file_get_contents($tmpPath);
    if ($bytes === false) {
        flashAndRedirect('error', 'Could not read the uploaded file.');
    }

    $databaseId = NotionClient::extractIdFromUrl($notionUrl);

    $claude = new ClaudeClient(
        $config['anthropic_api_key'],
        $config['claude_model'],
        $config['claude_effort'] ?? 'medium'
    );
    $notion = new NotionClient($config['notion_token']);

    $database = $notion->getDatabase($databaseId);
    if (($database['object'] ?? null) !== 'database') {
        flashAndRedirect('error', 'The Notion URL does not point to a database. Paste a database URL, not a page URL.');
    }

    $workOrder = $claude->generateWorkOrder($bytes, $mime, $notes);

    $originalName = $_FILES['shop_design']['name'] ?: 'shop-design';
    $safeName = preg_replace('/[^A-Za-z0-9._-]/', '_', $originalName);
    $imageUploadId = $notion->uploadFile($safeName, $mime, $bytes);

    $mapping = $notion->buildPropertiesFromWorkOrder($database, $workOrder, $imageUploadId);
    $children = $notion->buildPageContentBlocks(
        $workOrder,
        $mapping['unmapped'],
        $imageUploadId,
        $mapping['description_in_property']
    );

    $page = $notion->createPageInDatabase($databaseId, $mapping['properties'], $children);

    unset($_SESSION['last_notion_url'], $_SESSION['last_notes']);

    $message = "Title: {$workOrder['title']}";
    flashAndRedirect('success', $message, $page['url'] ?? null);
} catch (Throwable $e) {
    flashAndRedirect('error', $e->getMessage());
}
