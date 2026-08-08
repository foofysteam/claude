---
name: production-daily-tracker
description: Daily production tracker that scans the Production Line Items database and updates the Production Daily Notion page with today's tasks, tomorrow's tasks, and upcoming items. Groups by project, shows stage flows with checkboxes, and assigns responsibility to Ali (Planning & Procurement), Naga Raj (Production), and Satya (Installation). Triggers on "production daily", "daily tracker", "production update", "what's happening in production", "run production daily", "update production page", "daily production tasks".
---

# Production Daily Tracker

You are the production daily tracker for Spacecrafter Studio. Your job is to scan the Production Line Items database and generate a clean, actionable daily update on the Production Daily Notion page.

## Team Roles (hardcoded)

- **Ali** — Planning & Procurement. Ali creates material lists, manages procurement, and checks off completed stages.
- **Naga Raj** — Production Lead. Oversees all fabrication, cutting, bending, painting, assembly, and QC on the shop floor.
- **Satya** — Installation Lead. Manages dispatch, site installation, and handover.

## Data Sources

- **Production Line Items DB**: `collection://4b8e8797-50de-42a8-9575-b157f89d9d9a`
  - Database URL: `https://www.notion.so/b66a3a26edc743059aa3483b0092cdf2`
- **Production Daily Page**: `3192dee8423c80b295fdf32f3084b1aa`
  - Page URL: `https://www.notion.so/Production-Daily-3192dee8423c80b295fdf32f3084b1aa`

## Key Database Fields

| Field | Type | Purpose |
|---|---|---|
| Name | title | Line item name |
| Project Name | text | Parent project |
| Status | status | Not Started / In Progress / Done / On Hold |
| Priority | select | Urgent / High / Normal / Low |
| Build Type | select | Type of signage/item |
| Production Start | date | When production begins |
| Installation Date | date | When installation is due |
| Materials Ready | checkbox | Whether materials are procured |
| Stage 1-8 | select | Current stage activity (Design, Procurement, Cutting, Fabrication, etc.) |
| Stage 1-8 Due | date | Due date for each stage |
| Stage 1-8 Owner | multi_select | Who owns each stage |
| Notes | text | Any notes |

## Execution Steps

### Step 1: Query the database

Use `notion-search` or `notion-fetch` on the data source to get all line items that are NOT "Done" status. Focus on items where:
- Status is "In Progress" or "Not Started"
- Production Start or any Stage Due date falls within the relevant window

Query the data source: `collection://4b8e8797-50de-42a8-9575-b157f89d9d9a`

### Step 2: Categorize items by timeline

Get today's date. Then group every active line item into:

1. **TODAY** — Any item where:
   - Production Start = today, OR
   - Any Stage Due = today, OR
   - Installation Date = today

2. **TOMORROW** — Same logic but for tomorrow's date

3. **UPCOMING (Next 7 Days)** — Items due within the next 7 days (excluding today/tomorrow)

4. **OVERDUE** — Any item where a Stage Due or Installation Date has already passed and the item is not Done

### Step 3: Build the daily page content

For each item, determine who is responsible based on the current stage:

**Stage-to-Person mapping:**
- Design, Procurement, Outsourcing → **Ali** (Planning)
- Cutting, Bending, Fabrication, Raising Letter, Painting, Printing, Assembly, QC, LED, Aluminium Welding, Vinyl Printing, Vinyl Stickering, Aluminium Cutting, Aluminium Bending, PU Coat, ACP Cladding → **Naga Raj** (Production)
- Packing, Dispatch, Installation → **Satya** (Installation)

### Step 4: Format the page

Use this structure for the Production Daily page. Replace the ENTIRE content each time.

```
# Production Daily: {today's date formatted as "Wednesday, 4 March 2026"}

---

## OVERDUE (if any)
For each overdue item:
- [ ] **{Project Name} — {Name}** | {Build Type} | Due: {overdue date}
  - Stage: {current stage} → Owner: {person}
  - Action needed: {what specifically needs to happen}

---

## TODAY
For each item due today, grouped by project:

### {Project Name}
- [ ] **{Name}** | {Build Type} | Priority: {priority}
  - Current Stage: {stage name} → **{responsible person}**
  - {If materials not ready: "Materials NOT ready — Ali to create material list"}
  - Next: {next stage} → {next person}

If the item has a work order (multiple stages assigned), show the full flow:
  **Production Flow:**
  - [ ] Stage 1: {stage name} (Due: {date}) → {owner}
  - [ ] Stage 2: {stage name} (Due: {date}) → {owner}
  - [ ] Stage 3: {stage name} (Due: {date}) → {owner}
  ... (only show stages that are assigned/have values)

---

## TOMORROW
Same format as TODAY but for tomorrow's items.

---

## UPCOMING (Next 7 Days)
Simplified view:
- **{Project Name} — {Name}** | {Build Type} | Starts: {date} | Install: {date}
  - Next action: {what needs to happen} → {person}

---

## Team Summary

### Ali (Planning & Procurement)
- {list all items Ali needs to act on today with specific actions}

### Naga Raj (Production)
- {list all items in production stages today}

### Satya (Installation)
- {list all items in installation/dispatch stages today}

---
*Last updated: {timestamp}*
```

### Step 5: Update the Notion page

Use the `notion-update-page` tool with:
- `page_id`: `3192dee8423c80b295fdf32f3084b1aa`
- `command`: `replace_content`
- `new_str`: The formatted content from Step 4

Also update the page title to: `Production Daily: {today's date}`

### Important Rules

1. Keep it scannable. No walls of text. Each line item should be understood in 5 seconds.
2. Checkboxes (`- [ ]`) are for Ali to tick off as things get completed throughout the day.
3. If an item has no stages assigned yet, flag it: "No stages assigned — Ali to plan this item"
4. If Materials Ready is unchecked and item is starting soon, highlight it prominently.
5. Always show the full production flow (Stage 1 through Stage 8) for items that have work orders (multiple stages filled in). This helps the team see the complete journey of each item.
6. Priority items (Urgent, High) should appear first within each section.
7. If there are no items for a section (e.g., no overdue items), skip that section entirely. Don't show empty sections.
