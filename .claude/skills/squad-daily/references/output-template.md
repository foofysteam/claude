# Output Template — SQUAD DAILY Markdown

Use this exact structure when appending to the SQUAD DAILY Notion page.
Substitute the `{{placeholders}}` with computed values. Keep the
formatting tight; don't add extra blank lines.

---

## SQUAD DAILY — {{date_DD_MMM_YYYY}} ({{day_name}})

### Scoreboard

| Squad | Projects | Open Pipeline | Balance Pending | Open Line Items | Stagnant 4d+ |
|---|---|---|---|---|---|
| Squad 1 — The Legends | {{count}} | {{pipeline_inr}} | {{balance_inr}} | {{line_items}} | {{stagnant_count}} |
| Squad 2 — Cosmic Studio | {{count}} | {{pipeline_inr}} | {{balance_inr}} | {{line_items}} | {{stagnant_count}} |
| Squad 3 — Glitch Squad | {{count}} | {{pipeline_inr}} | {{balance_inr}} | {{line_items}} | {{stagnant_count}} |
| **TOTAL** | **{{total_count}}** | **{{total_pipeline}}** | **{{total_balance}}** | **{{total_line_items}}** | **{{total_stagnant}}** |

_(Note: Former Phantom projects are aggregated into Squad 1 — The Legends. If Unassigned has projects, add a row for it before TOTAL.)_

---

### 🏛️ Squad 1 — The Legends

**Team**: Dharshan (Sales Lead) · Jaisheelan + Arun (Design) · Naga Raj (Prod) · Satya + EXTERNAL (Install) · Srinivas (Site)

**Pipeline**: {{pipeline_inr}} across {{count}} projects · **Balance pending**: {{balance_inr}} · **Open line items**: {{line_items}}

**Stagnant matrix**:
- 🟢 1d: {{list_of_projects_or_em_dash}}
- 🟡 2d: {{list}}
- 🟠 3d: {{list}}
- 🔴 **4d+**: {{list}}
- ⚫ **10d+**: {{list}}

**Today's focus**:
- **Dharshan (Sales Lead)** → {{action_1}} · {{action_2}} · {{action_3}}
- **Jaisheelan (Design)** → {{action_1}} · {{action_2}}
- **Arun (Design)** → {{action_1}} · {{action_2}}
- **Naga Raj (Production)** → {{action_1}} · {{action_2}}
- **Satya (Installation)** → {{action_1}}
- **Srinivas (Site)** → {{action_1}}

---

### 🌌 Squad 2 — Cosmic Studio

**Team**: Ashika (Design) · Sudeep (Sales) · Sharik (Prod) · Ravi Nayak (Sr Prod) · Nawaz (Install) · Naveen (Site)

**Pipeline**: {{pipeline_inr}} across {{count}} projects · **Balance pending**: {{balance_inr}} · **Open line items**: {{line_items}}

**Stagnant matrix**:
- 🟢 1d: {{list}}
- 🟡 2d: {{list}}
- 🟠 3d: {{list}}
- 🔴 **4d+**: {{list}}
- ⚫ **10d+**: {{list}}

**Today's focus**:
- **Sudeep (Sales)** → {{actions}}
- **Ashika (Design)** → {{actions}}
- **Sharik (Production)** → {{actions}}
- **Ravi Nayak (Sr Prod)** → {{actions}}
- **Nawaz (Installation)** → {{actions}}
- **Naveen (Site)** → {{actions}}

---

### 🎮 Squad 3 — Glitch Squad

**Team**: Krupa (Design) · Zain (Sales) · Keerthana (Prod) · Junaid (Sr Prod) · EXTERNAL (Install) · Hawaldar (Site)

**Pipeline**: {{pipeline_inr}} across {{count}} projects · **Balance pending**: {{balance_inr}} · **Open line items**: {{line_items}}

**Stagnant matrix**:
- 🟢 1d: {{list}}
- 🟡 2d: {{list}}
- 🟠 3d: {{list}}
- 🔴 **4d+**: {{list}}
- ⚫ **10d+**: {{list}}

**Today's focus**:
- **Zain (Sales)** → {{actions}}
- **Krupa (Design)** → {{actions}}
- **Keerthana (Production)** → {{actions}}
- **Junaid (Sr Prod)** → {{actions}}
- **Install (EXTERNAL — via Zain)** → {{actions}}
- **Hawaldar (Site)** → {{actions}}

---

### ⚠️ Unassigned (route these)

_(Only show this block if there are open projects with no squad assigned.)_

- {{project_name}} — status: {{status}} — TOV: {{tov}} — last edit: {{date}}
- ...

---

### 🔍 Praveen (All-Squad Oversight)

_(Always show this block. Praveen oversees all 3 squads — flag cross-squad issues here.)_

- **Stagnant 4d+ company-wide**: {{list of projects with owner and days}}
- **Blocked pipelines**: {{any squad where payment/advance/proposal is stuck}}
- **Collections at risk**: {{projects with high balance pending and no recent movement}}
- If nothing flagged: → nothing flagged today

---

### 🚨 Red flags

- **Top stale**: list the 5 oldest stagnant projects (10d+ first, then 4d+ by descending TOV). Name them. Name the sales owner.
- **Highest balance pending**: the 3 projects with the largest balance pending across all squads.
- **Squad with most stagnant 4d+**: name and count.
- **Projects with TOV > ₹5L still in Lead/Targeted**: name and count.

---

## Inline-chat confirmation (NOT written to Notion — only post in chat)

```
SQUAD DAILY — {{date}}
✅ Written to SQUAD DAILY page

Scoreboard:
S1 Legends:    {{pipeline}} · bal {{balance}} · {{items}} items · {{stagnant}} stagnant
S2 Cosmic:     ...
S3 Glitch:     ...
TOTAL:         ...

Top 3 red flags:
1. {{Project}} — {{days}}d stagnant — {{owner}} — ₹{{tov}}
2. ...
3. ...

Page: https://www.notion.so/SQUAD-DAILY-3622dee8423c8011829cde7362273080
Scanned: {{N}} open projects, {{N}} line items.
```

---

## INR formatting rules

- < ₹1,000 → `₹{n}` (e.g. ₹600)
- ₹1,000 – ₹99,999 → `₹{n}K` with 1 decimal (e.g. ₹4.5K, ₹85K)
- ₹1,00,000 – ₹99,99,999 → `₹{n}L` with 1 decimal (e.g. ₹2.3L, ₹85L)
- ≥ ₹1,00,00,000 → `₹{n}Cr` with 2 decimals (e.g. ₹1.25Cr)
- 0 or null → `—`
