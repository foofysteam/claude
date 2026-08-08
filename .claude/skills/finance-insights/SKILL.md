---
name: finance-insights
description: >
  SpaceCrafter Studio financial health checker and project expense insights generator.
  Use this skill when the user says "finance check", "expense report", "budget check",
  "run finance insights", "project expenses", "financial health", "budget vs actual",
  "expense tracker update", "empty fields check", "finance update", "money check",
  "how are project budgets", "expense insights", "run finance", "financial summary",
  "check budgets", "project profitability", or any request about project-level
  expense tracking, budget allocation analysis, or financial health of SpaceCrafter Studio.
  Also triggers on "finance", "expenses", "budgets", "profitability", or "cost tracking".
---

# SpaceCrafter Studio Finance Insights

You are the financial analyst for SpaceCrafter Studio, a signage fabrication company.
Your job is to scan every active project's expense data, check for missing fields,
calculate budget vs actual spend, and deliver a clear financial health report to both
Notion and Slack.

Think like a CFO doing a weekly review: check every project's costs against its budget
allocation, flag overspends, identify projects with missing expense data, and highlight
the overall financial picture.

## Before you start

Read `references/database-schemas.md` in this skill's directory to understand the exact
database schemas, field names, budget allocation rules, and Slack channel details.

## Budget Allocation Rules

Every project's Total Order Value (no GST) gets split into these buckets:

| Bucket | % | Purpose |
|--------|---|---------|
| Salary | 40% | Labour and team salaries |
| Material | 30% | Raw materials and fabrication supplies |
| Growth | 5% | Business development and reinvestment |
| Saving | 5% | Company reserves |
| Petty Cash | 10% | Day-to-day operational expenses |
| Tax | 10% | Tax provisions |

## Execution Flow

### Step 1: Pull data from Notion

Query these data sources using the Notion MCP tools:

1. **Project Pipeline** -- data source: `collection://1a52dee8-423c-808d-b09f-000bfa700359`
   - Filter: Project status IN ("Production", "Installation", "In Discussion (sales+ Design)", "Design - production design", "PAYMENT PENDING", "Won")
   - Fields needed: Project Name, Customer name, Project status, Total Order Value (no gst), Transport Cost, Labour Cost, Material Cost (from Finance), Budget columns, Advance Amount, To collect, expenses

2. **Materials Movement Log** -- data source: `collection://2cc2dee8-423c-81a6-91bc-000b9d1fd890`
   - Pull all entries grouped by Project
   - Fields needed: Project, Total Value, Material, Quantity, unit price, Movement Type

3. **Company Finance** -- data source: `collection://2762dee8-423c-8144-a923-000bc48594b8`
   - Filter by Project Name (relation) is not empty
   - Fields needed: Reason, Amount, Bucket, Project Name, Date, Type

### Step 2: Analyze each project

For each active project, compute:

#### A. Expense Summary
- **Material Cost**: Sum of all "Material Purchase" bucket entries in Company Finance linked to this project + material movement outgoing values
- **Transport Cost**: From the "Transport Cost" field (manually entered) + sum of "Transportation" bucket entries in Company Finance
- **Labour Cost**: From the "Labour Cost" field (manually entered)
- **Total Actual Expense**: Material + Transport + Labour + any other Company Finance entries linked to this project

#### B. Budget vs Actual
Using the Total Order Value and the allocation percentages:
- Budget for Material (30%) vs Actual Material Cost --> flag if over
- Budget for Salary (40%) vs Actual Labour Cost --> flag if over
- Budget for Petty Cash (10%) vs Actual petty cash entries --> flag if over
- Overall margin = Total Order Value - Total Actual Expense

#### C. Empty Fields Check
Flag projects missing any of these critical fields:
- Total Order Value (no gst) is empty or 0
- Transport Cost is empty
- Labour Cost is empty
- No Company Finance entries linked
- No Materials Movement entries linked
- Advance Amount is empty
- Payment dates missing

### Step 3: Generate insights

Produce these insight categories:

1. **Projects at Risk** (actual spend > 80% of budget in any category)
2. **Data Gaps** (projects with empty expense fields that need manual entry)
3. **Top 5 Most Expensive Projects** (by total actual spend)
4. **Payment Collection Status** (projects with pending amounts to collect)
5. **Budget Utilization Summary** (% of budget used across all active projects)

### Step 4: Create Notion page

Create a new Notion page titled "Finance Insights - [today's date]" as a child of the
SpaceCrafter home page (page ID: `2602dee8423c80039dbac01a1c7789c2`).

Structure the page with these sections:
- Executive Summary (2-3 line overview)
- Projects at Risk (table)
- Data Gaps / Empty Fields (checklist per project)
- Project-wise Expense Breakdown (table: Project | Order Value | Material | Transport | Labour | Total | Margin)
- Payment Collection Pipeline
- Budget Utilization Charts description
- Action Items (what needs immediate attention)

### Step 5: Post to Slack

Send a summary message to **#all-spacecrafter** (channel ID: `C08R5UF71L0`) with:

```
:moneybag: *Finance Insights - [date]*

*Quick Summary:*
- X active projects tracked
- Total order value: Rs X
- Total expenses recorded: Rs X
- Overall margin: X%

*:warning: Projects at Risk:*
[List projects where spend > 80% of budget]

*:clipboard: Missing Data (needs manual entry):*
[List projects with empty Transport/Labour cost fields]

*:chart_with_upwards_trend: Top Action Items:*
1. [Most urgent financial action]
2. [Second priority]
3. [Third priority]

Full report: [link to Notion page]
```

## Important Notes

- All currency values are in Indian Rupees (Rs / INR)
- The "Total Order Value- ( No gst)" field has a leading emoji and trailing spaces -- match exactly: `💰 Total Order Value- ( No gst)`
- The budget columns are: "Budget: Salary (40%)", "Budget: Material (30%)", "Budget: Growth (5%)", "Budget: Saving (5%)", "Budget: Petty Cash (10%)", "Budget: Tax (10%)"
- Transport Cost and Labour Cost are manual entry fields on each project
- Material Cost (from Finance) is a rollup that auto-sums from linked Company Finance entries
- When calculating margins, negative means the project is over budget
- Always round currency values to nearest whole number for display
