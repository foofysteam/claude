---
name: sales-owner-analyzer
description: |
  Exhaustive analysis of ALL projects in Project Pipeline by status. Generates personalized daily action notes for each sales owner.
  Triggers: "run sales analyzer", "generate sales report", "daily sales actions", "what should sales team do", "sales owner analysis", "analyze pipeline"
---

# Sales Owner Analyzer - Exhaustive Status Analysis

Analyzes **ALL projects** in the Pipeline database (excluding Won/Lost/Completed) and generates comprehensive, personalized action items for each sales owner organized by project status.

## Data Source Configuration

```yaml
database_id: 1a52dee8-423c-8039-a133-fabfd3370fd8
data_source_url: collection://1a52dee8-423c-808d-b09f-000bfa700359
target_page: 2b12dee8-423c-80be-9959-e86cbf3d00d4
```

## Workflow

1. **Get Users**: Call `Notion:notion-get-users` to map user IDs to names
2. **Search All Projects**: Use `Notion:notion-search` with `data_source_url: collection://1a52dee8-423c-808d-b09f-000bfa700359` - search multiple times with different queries to get comprehensive results
3. **Fetch Each Project**: Use `Notion:notion-fetch` to get full properties for each unique project found
4. **Filter**: Exclude projects with status = "Won", "Lost", "Completed", "Closed"
5. **Group by Owner**: Organize by the "Sales " property (people field with trailing space)
6. **Analyze by Status**: Apply exhaustive status-specific rules (see below)
7. **Write Report**: Update Sales Daily Running page with `Notion:notion-update-page`

---

## 📊 PROJECT STATUSES & REQUIRED ACTIONS

### 🔴 LEAD
New opportunities requiring qualification and follow-up.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| Stale Lead | Last edited > 7 days | "⚠️ Stale lead - follow up immediately" |
| No Next Step | `next step` is empty | "📝 Define next step for lead" |
| Missing Contact | Phone AND Email empty | "📞 Add contact details" |
| No Site Visit | `Site visit (sales)` = NO | "🚗 Schedule site visit" |
| High Priority Idle | Priority = High, no update > 3 days | "🔥 URGENT: High priority lead needs action" |
| No Proposal | `proposal Sent (sales)` = NO, lead > 14 days old | "📄 Send proposal to move lead forward" |
| Customer Ready but still Lead | `CUSTOMER IS READY` = YES | "🎯 Customer ready - convert to order!" |

---

### 🟡 QUOTATION SENT / Proposal Sent
Proposals shared, awaiting customer response.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| No Follow-up | Last edited > 5 days | "📞 Follow up on quotation" |
| Customer Ready | `CUSTOMER IS READY` = YES | "🎯 Customer ready - push for order confirmation!" |
| Stale Proposal | Last edited > 14 days | "⚠️ URGENT: Proposal going cold, re-engage" |
| No Expected Date | `Expected Payment date` empty | "📅 Set expected decision date" |
| No WhatsApp Group | `Whatsapp Group (sales)` = NO | "💬 Create WhatsApp group for faster communication" |
| No Sample Sent | `Sample / mock up (sales)` = NO, Sample required = YES | "📦 Send sample/mockup as requested" |

---

### 🟢 CUSTOMER IS READY / Customer Ready
Customer confirmed, awaiting order/advance.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| No Order Confirmed | `❤️ order confirmed` = NO | "📝 Get order confirmation in writing" |
| No Advance | `Advance payment (sales)` = NO | "💰 Collect advance payment" |
| No WhatsApp Group | `Whatsapp Group (sales)` = NO | "💬 Create project WhatsApp group" |
| Missing Billing | `Billing name` empty | "🧾 Get billing details for invoice" |
| Stale | Last edited > 5 days | "⚠️ Customer ready but stalled - CLOSE NOW" |
| No Customer Name | `Customer name` empty | "👤 Add customer contact name" |
| No Phone | `Phone` empty | "📞 Add customer phone number" |

---

### 🔵 ORDER CONFIRMED
Order received, project in execution phase.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| No Kickoff | `Project Kickoff` = NO | "🚀 Schedule project kickoff" |
| No Production Date | `Production Dates` empty | "📅 Set production schedule" |
| No Deadline | `Expected Deadline` empty | "⏰ Set project deadline" |
| Missing Billing | `Billing name` empty | "🧾 URGENT: Get billing details" |
| No Advance Collected | `Advance payment (sales)` = NO | "💰 Collect advance before production" |
| No Advance Date | `Advance collected date` empty but advance marked YES | "📅 Record advance collection date" |

---

### 🟣 DESIGN - Production Design / Design Phase
Design phase projects.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| Stale Design | Last edited > 7 days | "⚠️ Design phase stalled - check with design team" |
| No Site Survey | `Site visit (sales)` = NO | "🚗 Complete site survey for design" |
| No Designer Assigned | `designer` property empty | "👨‍🎨 Assign designer to project" |
| Missing Client Page | `CLIENT FACING PAGE` empty | "📄 Create client-facing page" |
| No Expected Deadline | `Expected Deadline` empty | "⏰ Set design completion deadline" |

---

### 🟠 PRODUCTION / In Production
Manufacturing phase.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| Production Not Done | `production done` = NO, production dates passed | "🏭 Check production status - overdue" |
| No Installation Date | `installation Date` empty | "📅 Schedule installation" |
| Missing Material Movement | `material movement` empty | "📦 Track material movement" |
| Production Dates Empty | `Production Dates` empty | "📅 Set production schedule" |
| Stale | Last edited > 7 days | "⚠️ Production stalled - follow up" |

---

### 🔧 INSTALLATION
Installation phase.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| Not Complete | `Installation done` = NO | "🔧 Complete installation" |
| No Invoice After Install | `Invoice shared` = NO, `Installation done` = YES | "🧾 URGENT: Share invoice immediately" |
| Missing Documentation | No content/images in project | "📸 Document completed work with photos" |
| Installation Date Passed | Date passed but not marked done | "⚠️ Installation overdue - update status" |
| No Payment Status Set | `Status set Date (Payment)` empty after install | "💰 Set payment pending status" |

---

### 💰 PAYMENT PENDING
Work complete, awaiting payment.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| Days Pending | Check `Days from payment pending` or calculate | "💰 Payment overdue X days - follow up" |
| No Invoice | `Invoice shared` = NO | "🧾 URGENT: Share invoice immediately" |
| No Expected Date | `Expected Payment date` empty | "📅 Set payment follow-up date" |
| No Payment Remarks | `Payment remarks` empty | "📝 Add payment conversation notes" |
| High Value Overdue | TOV > 2L, pending > 14 days | "🔴 CRITICAL: Large payment overdue - escalate" |
| Very Old | Pending > 30 days | "🚨 ESCALATE: Payment severely overdue" |
| Medium Overdue | Pending 14-30 days | "⚠️ Payment overdue - increase follow-up frequency" |
| Recent | Pending < 7 days | "📞 Regular payment follow-up" |

---

### ⏸️ ON HOLD
Paused projects requiring reactivation.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| Customer Ready | `CUSTOMER IS READY` = YES | "🎯 Customer ready but on hold - REACTIVATE!" |
| Long Hold | On hold > 14 days | "📋 Review if project should be closed or reactivated" |
| No Reason | `risk / dependency` empty | "📝 Document hold reason" |
| No Next Step | `next step` empty | "📝 Define what's needed to resume" |
| High Value | TOV > 1L | "💰 High value on hold - prioritize resolution" |

---

### ❓ OTHER STATUS (Catch-all)
Any status not covered above.

| Check | Condition | Action Required |
|-------|-----------|-----------------|
| Stale | Last edited > 10 days | "⚠️ Project needs attention" |
| Missing Status | Status empty or unclear | "📋 Set proper project status" |
| No Next Step | `next step` empty | "📝 Define next action" |

---

## 📋 Property Reference

| Property | Type | Notes |
|----------|------|-------|
| `Sales ` | People | Has trailing space - contains user mentions |
| `Project Name` | Title | Main project identifier |
| `Project status` | Select | Main status field |
| `CUSTOMER IS READY ` | Checkbox | Has trailing space |
| `❤️ order confirmed ( sales)` | Checkbox | Order confirmation |
| `Advance payment (sales)` | Checkbox | Advance collected |
| `Invoice shared` | Checkbox | Invoice sent |
| `Installation done ` | Checkbox | Has trailing space |
| `production done ` | Checkbox | Has trailing space |
| `Project Kickoff ` | Checkbox | Has trailing space |
| `Site visit (sales)` | Checkbox | Site visit completed |
| `Whatsapp Group (sales)` | Checkbox | WA group created |
| `proposal Sent (sales)` | Checkbox | Proposal sent |
| `Sample / mock up (sales)` | Checkbox | Sample sent |
| `💰 Total Order Value- ( No gst)` | Number | Deal value |
| `Advance Amount ` | Number | Advance amount |
| `Billing name` | Text | Billing details |
| `Customer name ` | Text | Has trailing space |
| `Phone` | Phone | Contact number |
| `Email` | Email | Contact email |
| `next step` | Text | Next action |
| `Last conversation` | Text | Latest notes |
| `Payment remarks. ` | Text | Has trailing space |
| `PROJECT NOTES ` | Text | Has trailing space |
| `risk / dependency ` | Text | Hold reasons |
| `Last edited time` | Date | Auto-updated |
| `Created time` | Date | Project creation |
| `date:Status set Date (Payment):start` | Date | When payment status set |
| `date:Expected Payment date :start` | Date | Expected payment |
| `date:installation Date :start` | Date | Installation date |
| `date:Production Dates:start` | Date | Production start |
| `date:Expected Deadline (t-1):start` | Date | Project deadline |
| `date:Advance collected date :start` | Date | Advance collection |
| `Priority` | Select | High/Medium/Low |
| `Industry` | Multi-select | Industry type |
| `Type of customer` | Multi-select | Customer category |

---

## 👥 User ID to Name Mapping

Query `Notion:notion-get-users` at start. Key sales team:

| User ID | Name |
|---------|------|
| `1abd872b-594c-8140-95db-0002d61c2816` | Saqlain Fazal |
| `35829c9e-bf18-4a51-931e-0424c9dc7554` | Praveen Kumar |
| `29ad872b-594c-815f-9120-0002cb07e135` | Syed Ahmed |
| `4f220fb9-6fc0-49f1-852c-332d5055202c` | Akshay |
| `264d872b-594c-81a8-973b-00026d008f38` | Nithin Kumar V |
| `3aefff2a-f6b6-48d5-8b6f-c736db625a25` | Shalin Jacob |

---

## 📝 Output Format

```markdown
## 📅 {DATE} - Daily Sales Action Plan

# DAILY SALES ACTION REPORT
*Exhaustive analysis of ALL active projects in Pipeline*

---

## 🎯 {OWNER NAME}

### 🔴 LEADS ({count})
{Owner}, follow up on these leads:
- **{Project}** - {Specific Issue}
  - {Additional context: days stale, priority, next step}
  - [View Project](url)

### 🟡 QUOTATIONS PENDING ({count})
{Owner}, follow up on these proposals:
- **{Project}** (₹{value}) - {Issue}
  - [View Project](url)

### 🟢 READY TO CLOSE ({count})
{Owner}, these customers are READY - close them TODAY:
- **{Project}** (₹{value}) - {What's missing}
  - [View Project](url)

### 🔵 IN EXECUTION ({count})
{Owner}, monitor these active projects:
- **{Project}** - {Current phase, what's needed}
  - [View Project](url)

### 💰 PAYMENT PENDING ({count})
{Owner}, collect payment from:
- **{Project}** (₹{value}) - ⏰ Pending {days} days
  - Payment remarks: {remarks}
  - [View Project](url)

### ⏸️ ON HOLD ({count})
{Owner}, review these stalled projects:
- **{Project}** - {Reason/What's needed}
  - [View Project](url)

### ⚠️ MISSING DATA
{Owner}, fill in missing info:
- **{Project}** - Missing: {field1}, {field2}

### 📊 Score: {X}/10
{Personalized performance summary}

---
```

## 🔄 Execution Steps

1. **Initialize**: Get user list with `Notion:notion-get-users`

2. **Comprehensive Search**: Run multiple searches to get all projects:
   ```
   Notion:notion-search with data_source_url: collection://1a52dee8-423c-808d-b09f-000bfa700359
   Queries: "project", "lead", "payment", "quotation", "production", "design", "installation"
   ```

3. **Deduplicate**: Collect unique project IDs from all search results

4. **Fetch Details**: For each unique project ID:
   ```
   Notion:notion-fetch with id: {project_id}
   ```

5. **Parse & Filter**:
   - Extract properties from each project
   - Skip if status in ["Won", "Lost", "Completed", "Closed"]
   - Extract owner from "Sales " property (parse user mention URL)

6. **Group by Owner**: Create dictionary of owner → projects

7. **Analyze Each Project**: For each project:
   - Identify status category
   - Apply ALL rules for that status (see tables above)
   - Generate specific action items with context
   - Include project URL for quick access

8. **Calculate Scores**: For each owner:
   - Count total issues found
   - Weight by severity (payment > stale > missing data)
   - Score = 10 - (weighted_issues / active_projects * factor)

9. **Format Report**: Generate markdown following output format

10. **Write to Notion**:
    ```
    Notion:notion-update-page
    page_id: 2b12dee8-423c-80be-9959-e86cbf3d00d4
    command: replace_content
    new_str: {generated_report}
    ```

---

## ⚠️ Important Notes

1. **Data Source URL**: Use `collection://1a52dee8-423c-808d-b09f-000bfa700359` NOT the database ID for search
2. **Property Spacing**: Many properties have trailing spaces (e.g., "Sales ", "Customer name ")
3. **User Mentions**: Sales owners are stored as `<mention-user url="{{user://UUID}}">` - parse the UUID
4. **Checkbox Values**: Stored as `__YES__` or `__NO__` in properties
5. **Date Properties**: Prefixed with `date:` and have `:start`, `:end`, `:is_datetime` suffixes
6. **Formula Results**: Properties starting with `formulaResult://` need to be fetched separately or calculated
