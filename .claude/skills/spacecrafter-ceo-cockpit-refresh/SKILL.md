---
name: spacecrafter-ceo-cockpit-refresh
description: Daily morning refresh of Akshay's CEO Cockpit — updates the Notion backup page and the in-app artifact
---

Refresh Akshay's SpaceCrafter CEO Cockpit. Two outputs to update — keep them consistent.

**Step 1 — Pull fresh data from Notion:**

> 🚨 **ALL financial figures (order value, advance, balance pending, project expense, etc.) MUST be pulled live from the canonical Finance // Projects page — NEVER estimated, NEVER carried forward from a previous snapshot.** ADP CX was historically wrong (set to ₹1.65L when actual is ₹28K) — this is the kind of drift that happens when figures are estimated. If a value is missing in Notion, write `null` / "—" and flag it; do NOT fabricate.

**🤑 CANONICAL FINANCE SOURCE — Finance // Projects page**
- Page: https://www.notion.so/Finance-Projects-3522dee8423c80919168c1012e233316 (id `3522dee8-423c-8091-9168-c1012e233316`)
- Inline database id: `3522dee8423c80faac33c7708819b64b` — multi-source over Project Pipeline + Company Finance
- **Three views** (use these to mirror what Akshay sees in Notion):
  1. **`project money`** view (`view://3522dee8-423c-8002-85fb-000c6cbe254b`) — Project Pipeline filtered to Project status ∈ {Installation, Production, On Hold, Repair, PAYMENT PENDING}. Pull every project with these fields:
     - `Project Name`
     - `Project status`
     - `💰 Total Order Value- ( No gst)` ← **THIS IS THE CANONICAL ORDER VALUE — never estimate**
     - `Advance Amount ` ← **canonical advance**
     - `Advance collected date `
     - `balance pending ` (formula — read-only)
     - `Total Project Expense` (formula — read-only)
     - `Project expense ` (relation to expense rows)
     - `Purchase order`, `DC`, `Invoice `, `Phone`, `Billing name`
  2. **`to collect now`** view (`view://3522dee8-423c-807b-ae64-000c291560e1`) — same source, filtered to PAYMENT PENDING + Installation + Repair, grouped by Project status. Use for the "Cash Collection — Top of Mind" section.
  3. **`Money Spent`** view (`view://3522dee8-423c-80fd-8352-000c37079055`) — Company Finance ledger. Use for daily / weekly / monthly spend totals + top buckets.

**Other sources (non-finance):**
1. Project Pipeline (collection://1a52dee8-423c-808d-b09f-000bfa700359) — top 12 most recently edited active projects. For each, capture: title, status, sales owner(s), next step, last conversation, days since unchanged, payment status flags. **For all monetary fields (order value, advance, balance) on this DB, ALWAYS go through the `project money` view above so the canonical figure is what gets quoted — never estimate.**
2. Production Line Items (collection://4b8e8797-50de-42a8-9575-b157f89d9d9a) — items with Production Start within ±2 days OR Status not "Done". Capture: name, project, status, priority, install date, departments involved, days to install (if overdue, note it).
3. Project Expenses (collection://25b2dee8-423c-801c-805a-000b72a569c0) — last 30 days, summed by project (Design / Production / Installation / Sales / Admin teams). Pull each project's running total. Cross-check against `Total Project Expense` on the project's pipeline row — they should match.
4. Company Finance (collection://2762dee8-423c-8144-a923-000bc48594b8) — today's transactions, this week's total, this month's total, top 3 buckets. Equivalent to the `Money Spent` view above.
5. Running Task Owners (page 26d2dee8-423c-80ffbb6df7403e3bc99a) — count tasks per designer: Ashika, Krupa, Arun Kumar K, Arun R, Jaisheelan; flag urgent / overdue / no-due-date / unassigned items.

**How to fetch finance values for a single project (example: ADP CX):**
1. `notion-fetch` with the project page ID (e.g. `3442dee8-423c-8096-81a7-d52259f04e1c` for ADP CX).
2. Read these fields **verbatim** from the `<properties>` block:
   - `💰 Total Order Value- ( No gst)` → `orderValue` (number, INR, no gst)
   - `Advance Amount ` → `advance`
   - `Advance payment (sales)` checkbox (`__YES__` / `__NO__`) — if NO, treat advance as ₹0 even if `Advance Amount` has a number on it (it's the asked-for amount, not the collected amount).
   - `Project status` → `projectStatus`
   - `next step`, `Payment remarks. `, `Days since Unchanged` → context for the action note
3. Compute `balanceDue = orderValue - advance` only when `Advance payment (sales) = __YES__`; otherwise `balanceDue = orderValue` and flag as "no advance collected".
4. Set `estimate: false` on the snapshot row to mark it canonical. Only set `estimate: true` when a project is missing finance fields entirely and a placeholder is unavoidable.

**Step 2 — Update the Notion backup page:**

Page: Running SPC - operator (id 34d2dee8-423c-8050-a1f7-ec324b466d03).
Use update_content (or replace_content if structure changed) to replace the contents of the "🛰️ CEO Cockpit Backup — Akshay's view" section. Keep the structure:
- Source databases deep links block — **must include the Finance // Projects page link** as the canonical money source
- Cash Collection / Hot Deals — top 6 by urgency (overdue installs, payments pending, stagnant >7d, hot follow-ups). Quote canonical INR figures only — pull from `project money` / `to collect now` views.
- **📞 Sales Team — Next Actions (NEW — required)** — dedicated per-owner action list for the sales team. Group by sales owner: Sandeep (Invoicing), Praveen (Conversion), Zain (Shadow), Akshay (CEO Direct/Takeover), and a Pipeline Hygiene block. For each owner pull from Project Pipeline `Sales ` person field + `next step` + `Days since Unchanged` + `Project status` + `Payment remarks. ` and produce 3–6 rows per owner. Each row: `priority` (🔴 today / 🟡 this week / 🟢 nurture), `deal` (linked to project page), `action` (one sentence, imperative, with INR if money-related — pulled canonical from Finance // Projects), `deadline` (e.g. "9 AM today", "Today EOD", "Mon 4 May"). Pull the same data into the artifact's `SNAPSHOT.salesActions` array (shape: `[{owner, role, urgent, items: [{deal, url, priority, action, deadline}]}]`). Urgent count per owner = items with `priority: "today"`. The artifact renders this via `renderSalesActions()` between Hot Deals and Project Spend.
- Design Workload — counts per designer with status colour
- Production lanes table — Cutting/Welding/Painting/Printing/Assembly/Installation with active count, urgent count, status
- Money pulse — today / week / month spend totals + top 3 buckets, sourced from `Money Spent` view
- Ali Cover Mode WhatsApp messages — refresh each dept-head message (Naga Raj, Ravi Naik, Nawaz, Jayanth, Satya, Samsong, Ashika) with that day's specific tasks. Rotate the inspirational quote daily from this set:
  • "Pride in the cut. Pride in the bend. Pride in the finish."
  • "Tools work because hands work. Hands work because hearts work."
  • "Aaj ka kaam aaj — kal ke liye mat chodo."
  • "The strong man stands so the weak may walk."
  • "Har naap, har cut, har joint — yahin se SpaceCrafter banta hai."
  • "Quality is what stays after the dust settles."
  • "Measure twice. Cut once. Finish like it's your home."
  • "Small details done right. Every single time."
  • "Sweat today, smile tomorrow."
  • "The work you do quietly speaks the loudest."

Always sign Ali's messages: "— Ali (on behalf of Akshay) 🙏"

**Step 3 — Update the in-app artifact:**

Use update_artifact (id: spacecrafter-ceo-cockpit) to replace the SNAPSHOT object in the HTML with the same data set, keeping field shapes identical. Keep all rendering JS unchanged. Set `estimate: false` on every cash row that came from the canonical Finance // Projects views.

**Step 4 — Notify Akshay:**

Reply to Akshay in chat with:
- Today's date
- 3-line summary: most urgent thing, biggest finance hit yesterday, single biggest deal action needed
- Confirmation that Notion + artifact are refreshed
- Link to the Notion page: https://www.notion.so/Running-SPC-operator-34d2dee8423c8050a1f7ec324b466d03

Keep the chat reply under 80 words. Bullet format.
