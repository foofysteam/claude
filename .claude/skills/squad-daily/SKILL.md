---
name: squad-daily
description: "SpaceCrafter Studio daily squad scorecard and focus planner. Use this skill whenever Akshay says 'run squad daily', 'squad daily', 'squad update', 'squad report', 'squad scorecard', 'squad standup', 'how are the squads', 'daily squad briefing', 'what's happening in squads', 'how are the three squads doing', 'squad health', or 'plan my day' for SpaceCrafter. Also trigger on bare 'squads', 'squad check', or any request for a per-squad pipeline + balance pending + stagnant-projects + line-items + per-person focus breakdown. Always use this skill before producing any Squad-level daily summary."
---

# SQUAD DAILY — Akshay's per-squad daily scorecard

You are running Akshay's morning pulse on the three squads. Your job is to
scan the Project Pipeline, group everything by squad, surface the numbers
that matter, flag stagnant projects in red, and tell each person on each
squad exactly what to do today. Then append the full report to the SQUAD
DAILY Notion page.

Keep the output **dense, bullet-formatted, scannable**. Akshay has limited
attention — no fluff, no preamble, no nice-to-meet-you. Numbers first,
names second, actions third.

## Critical constants

- **Project Pipeline data source**: `collection://1a52dee8-423c-808d-b09f-000bfa700359`
- **SQUAD DAILY page (append target)**: `https://www.notion.so/SQUAD-DAILY-3622dee8423c8011829cde7362273080` — page id `3622dee8-423c-8011-829c-de7362273080`
- **Closed statuses to EXCLUDE**: `Won`, `Lost` only
- **Open statuses to INCLUDE**: Targeted, Lead, In Discussion (sales+ Design), Design - production design, Production, Installation, Repair, PAYMENT PENDING, On Hold
- **Squad property values in Notion**: `Squad 1 — The Legends`, `Squad 2 — Cosmic Studio`, `Squad 3 — Glitch Squad`, `Squad 4 — Phantom`, `Unassigned`
- **IMPORTANT**: `Squad 4 — Phantom` no longer exists as a separate squad. Treat any project tagged "Squad 4 — Phantom" as belonging to **Squad 1 — The Legends**. Aggregate their numbers into S1.

## Before you start

1. Read `references/squad-roster.md` for the squad-to-people mapping. The roster defines 3 squads + Praveen as all-squad overseer. Use it when writing the "today's focus by person" block.
2. Read `references/output-template.md` for the exact markdown template to append. Match it block-for-block.

## Execution flow

### Step 1 — Fetch the data source schema (sanity check only)

Run `Notion:notion-fetch` on the Project Pipeline data source URL once.
You're checking that the `Squad` property still exists and that the
`Project status` options haven't changed. If they have, STOP and tell
Akshay before continuing — the report will be wrong if statuses drifted.

### Step 2 — Pull all open projects from the data source

Notion MCP doesn't expose a `query_data_sources` SQL endpoint, so use
`Notion:notion-search` with `data_source_url` set to the Project Pipeline
collection. Paginate with `page_size: 25` and rotate the `query` parameter
through these strings to surface different slices of the data (semantic
search is not exhaustive on a single query):

- `"open project"`
- `"client signage"`
- `"installation hospital school office"`
- `"production design discussion"`
- `"payment pending order"`

Deduplicate by page id. You should end up with ~50–75 unique pages.

**If you suspect you missed projects** (e.g., known projects from the
SQUAD DAILY page aren't in your list), also run a search with
`"squad"` and `"branding"` as fallback queries.

### Step 3 — Fetch each project's properties

For every unique project id, call `Notion:notion-fetch` on the page.
This is the expensive step (~50–75 calls). Extract:

- `Project Name` → title
- `Project status` → string. **Skip the project if status is Won or Lost.**
- `Squad` → one of the five Notion property values, may be missing → treat as `Unassigned`
- `💰 Total Order Value- ( No gst)` → number, may be null → treat as 0
- `Received  Amount ` → number (note the **double space** in the property name), may be null → treat as 0
- `Production Line Items` → JSON array of URLs. Count = `len(array)`. May be empty → 0.
- `Last edited time` → ISO timestamp
- `Sales` → person field (user IDs)
- `next step` → text. May be empty.
- `Customer name ` → text. May be empty.
- `❤️ order confirmed ( sales)` → "__YES__" / "__NO__" / null
- `Site visit (sales)` → checkbox
- `proposal Sent (sales)` → checkbox
- `Advance payment (sales)` → checkbox
- `CUSTOMER IS READY ` → checkbox
- `date:installation Date :start` → ISO date, may be null
- `Priority` → "High" / "Medium" / "Low" / "very high" / null

**Compute per project:**
- `balance_pending = max(0, total_order_value − received_amount)`
- `stagnant_days = floor((today − last_edited_time) / 1 day)`
- `stagnant_bucket` from `stagnant_days`:
  - `0–1` → 🟢 1d
  - `2` → 🟡 2d
  - `3` → 🟠 3d
  - `4–9` → 🔴 4d+ (RED)
  - `10+` → ⚫ 10d+ (RED)

### Step 4 — Aggregate per squad

Squad mapping:
- `Squad 1 — The Legends` → S1
- `Squad 4 — Phantom` → S1 (merged — treat as Legends)
- `Squad 2 — Cosmic Studio` → S2
- `Squad 3 — Glitch Squad` → S3
- Missing/`Unassigned` → Unassigned

For each of [S1, S2, S3, Unassigned], compute:

- `open_pipeline_inr` = Σ total_order_value across open projects in this squad
- `balance_pending_inr` = Σ balance_pending across open projects in this squad
- `open_line_items` = Σ production line items count across open projects in this squad
- `project_count` = count of open projects in this squad
- `stagnant_buckets` = dict of {1d: [proj…], 2d: [proj…], 3d: [proj…], 4d+: [proj…], 10d+: [proj…]}

### Step 5 — Build "today's focus by person" per squad

For each squad, look at all of its open projects and generate **2–3 concrete
actions** for each role on the squad (from `references/squad-roster.md`).
Use these signals to drive the actions:

| Role | Look for | Action verb |
|------|----------|-------------|
| Sales | Site visit (sales)=NO, proposal Sent=NO, Advance=NO, CUSTOMER IS READY=NO, balance_pending > 0 with status=PAYMENT PENDING | "site-visit X", "send proposal Y", "chase advance on Z", "collect ₹X balance on W" |
| Designer | status = "In Discussion (sales+ Design)" or "Design - production design" | "finalize design for X", "share v2 of Y" |
| Production Owner / Sr. Production | status = "Production" with no recent Last edit, or line items not started | "start cutting on X", "QC pending on Y" |
| Installation | status = "Installation" or installation Date within 3 days | "install scheduled X on date", "site-ready check for Y" |
| Site Engineer | Site visit=NO and value > ₹1L, or installation Date approaching | "survey X tomorrow", "measurement pending at Y" |

If you can't find anything for a role on a given day, write `→ nothing flagged today`. Don't invent work.

For the **Unassigned** squad (if any open projects), just list them and flag for assignment — no per-person actions.

**Praveen (All-Squad Oversight)**: After all squad blocks, add a "🔍 Praveen (All-Squad Oversight)" block. Surface:
- All stagnant 4d+ projects company-wide (name, squad, owner, days)
- Any squad where payment/advance/proposal is stuck
- Projects with high balance pending and no recent movement
If nothing flagged: → nothing flagged today.

### Step 6 — Compose the markdown report

Use the exact template in `references/output-template.md`. The structure:

1. `## SQUAD DAILY — <Today's date in IST, format: DD MMM YYYY (DDD)>`
2. Scoreboard table (3 squads — no Phantom row — + Unassigned row if non-zero)
3. Per-squad blocks: S1 Legends, S2 Cosmic, S3 Glitch
4. Praveen All-Squad Oversight block
5. Red flags section at the bottom

All ₹ figures formatted as Indian numbers with lakhs/crores. Example:
- 230000 → ₹2.3L
- 8500000 → ₹85L
- 12000000 → ₹1.2Cr
- 6500 → ₹6.5K
- 0 → —

### Step 7 — Append to the SQUAD DAILY Notion page

Use `Notion:notion-update-page` (or whatever update tool is exposed; if
not present, search for one with `tool_search`) with the `append_content`
operation on page id `3622dee8-423c-8011-829c-de7362273080`. Add a
horizontal rule `---` BEFORE the new section so each day is visually
separated from the previous one.

**Never overwrite or delete prior content** on the SQUAD DAILY page. Only
append.

### Step 8 — Confirm and surface

After writing to Notion, post back in the chat:

- 3 short lines, one per squad, showing the scoreboard row
- Top 3 red-flag projects across all squads (the 10d+ ones, or 4d+ ones
  with high TOV)
- Link to the SQUAD DAILY page
- Number of total open projects scanned, number of line items, total
  open pipeline ₹, total balance pending ₹ across the whole company

Skip pleasantries. Numbers first.

## Important notes

- **Today's date**: use IST. India is UTC+5:30. Compute `today` accordingly
  before doing the stagnant-days math.
- **Don't include closed projects** (Won, Lost) anywhere — not in
  scoreboard, not in per-squad blocks, not in red flags.
- **Phantom → Legends**: Always map Squad 4 projects to S1. Never show a Phantom row in the scoreboard.
- **Unassigned squad**: if it has projects, list them in a slim block at
  the bottom so Akshay can route them. Don't generate per-person actions.
- **Skip Sundays**: if today is Sunday, write "No squad briefing on Sunday.
  Enjoy the break." and exit without writing to Notion.
- **Pagination caveat**: Notion semantic search is not exhaustive. If you
  end with fewer than 40 open projects, run one more search with the
  query `"customer signage"` to fill gaps. Log the final count.
- **Formula and rollup limits**: `balance pending` (formula), `Days since
  Unchanged` (formula), `TOV - with gst` (formula), and all rollup fields
  return placeholders, not values. ALWAYS compute balance pending
  manually as `total_order_value − received_amount`. ALWAYS compute
  stagnant days from `Last edited time`.
- **Property name quirks**: many property names have trailing spaces or
  double spaces. Always match the exact string from the schema. Notable:
  - `Received  Amount ` (DOUBLE space before "Amount", trailing space)
  - `Customer name ` (trailing space)
  - `Sales ` (trailing space)
  - `next step` (no trailing space — careful)
  - `❤️ order confirmed ( sales)` (emoji + spaces around `( sales)`)
- **Be opinionated in red flags**: name people. "Dharshan has 3 stagnant
  projects > 4 days." Not "some projects are stagnant."
- **Praveen is the safety net**: if you see stagnant projects that no one
  seems to be moving, flag them to Praveen explicitly — his job is to
  unblock them.
- **No targets yet**: skip the monthly-target column. (Akshay will add
  them later. When he does, edit the scoreboard template.)
