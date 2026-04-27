<?php
session_start();

$flash = $_SESSION['flash'] ?? null;
unset($_SESSION['flash']);

$lastUrl = $_SESSION['last_notion_url'] ?? '';
$lastNotes = $_SESSION['last_notes'] ?? '';
unset($_SESSION['last_notion_url'], $_SESSION['last_notes']);
?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Shop Design → Notion Work Order</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<main class="card">
    <h1>Create Work Order</h1>
    <p class="subtitle">
        Upload a shop design image and a Notion database URL. Claude reads the
        drawing and adds a fully-populated work order row to your database.
    </p>

    <?php if ($flash): ?>
        <?php $kind = htmlspecialchars($flash['kind'], ENT_QUOTES); ?>
        <div class="flash flash-<?= $kind ?>">
            <strong>
                <?= $flash['kind'] === 'success' ? 'Work order created.' : 'Something went wrong.' ?>
            </strong>
            <p><?= nl2br(htmlspecialchars($flash['message'], ENT_QUOTES)) ?></p>
            <?php if (!empty($flash['page_url'])): ?>
                <p>
                    <a class="primary-link" href="<?= htmlspecialchars($flash['page_url'], ENT_QUOTES) ?>" target="_blank" rel="noopener">
                        Open the new work order in Notion →
                    </a>
                </p>
            <?php endif; ?>
        </div>
    <?php endif; ?>

    <form method="post" action="submit.php" enctype="multipart/form-data" class="wo-form">
        <label for="notion_url">Notion database URL</label>
        <input
            type="url"
            id="notion_url"
            name="notion_url"
            required
            placeholder="https://www.notion.so/your-workspace/your-database-..."
            value="<?= htmlspecialchars($lastUrl, ENT_QUOTES) ?>">
        <small>
            Share the database with your Notion integration first
            (Share → Connections → add your integration).
        </small>

        <label for="shop_design">Shop design image</label>
        <input type="file" id="shop_design" name="shop_design" accept="image/png,image/jpeg" required>
        <small>PNG or JPG, up to 10&nbsp;MB.</small>

        <label for="notes">Additional notes (optional)</label>
        <textarea id="notes" name="notes" rows="3" placeholder="Anything that isn't on the drawing — due date, customer, finish notes, etc."><?= htmlspecialchars($lastNotes, ENT_QUOTES) ?></textarea>

        <button type="submit">Generate work order</button>
    </form>

    <details class="help">
        <summary>How this works</summary>
        <ol>
            <li>The shop design is sent to Claude (Anthropic API) with vision enabled.</li>
            <li>Claude returns a structured work order: title, description, materials, dimensions.</li>
            <li>The image is uploaded to Notion via the file upload API.</li>
            <li>A new row is created in your Notion database with the work order details.</li>
        </ol>
    </details>
</main>
</body>
</html>
