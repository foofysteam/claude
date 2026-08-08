# Database Schemas Reference

## 1. Project Pipeline

**Data Source ID:** `collection://1a52dee8-423c-808d-b09f-000bfa700359`
**Database URL:** `https://www.notion.so/1a52dee8423c8039a133fabfd3370fd8`

### Key Financial Fields

| Field Name (exact) | Type | Notes |
|---|---|---|
| `Project Name` | title | Project identifier |
| `Customer name ` | text | Has trailing space |
| `Project status` | select | Options: Targeted, Lead, Installation, In Discussion (sales+ Design), Design - production design, Production, On Hold, Repair, PAYMENT PENDING, Won, Lost |
| `💰 Total Order Value- ( No gst)` | number (rupee) | The base value for budget calculations |
| `Transport Cost` | number (rupee) | Manually entered transport cost |
| `Labour Cost` | number (rupee) | Manually entered labour cost |
| `Material Cost (from Finance)` | rollup (sum) | Auto-calculated from linked Expenses |
| `Budget: Salary (40%)` | number (rupee) | 40% of order value |
| `Budget: Material (30%)` | number (rupee) | 30% of order value |
| `Budget: Growth (5%)` | number (rupee) | 5% of order value |
| `Budget: Saving (5%)` | number (rupee) | 5% of order value |
| `Budget: Petty Cash (10%)` | number (rupee) | 10% of order value |
| `Budget: Tax (10%)` | number (rupee) | 10% of order value |
| `Advance Amount ` | number | Has trailing space |
| `To collect` | number | Pending payment amount |
| `expenses` | number | Legacy expense field |
| `Expenses ` | relation | Links to Company Finance DB |
| `material movement ` | relation | Links to Materials Movement |

### Budget Allocation Formula
```
Total Order Value * percentage = Budget for that bucket
Example: Rs 500,000 order value
- Salary: 500,000 * 0.40 = Rs 200,000
- Material: 500,000 * 0.30 = Rs 150,000
- Growth: 500,000 * 0.05 = Rs 25,000
- Saving: 500,000 * 0.05 = Rs 25,000
- Petty Cash: 500,000 * 0.10 = Rs 50,000
- Tax: 500,000 * 0.10 = Rs 50,000
```

## 2. Materials Movement Log

**Data Source ID:** `collection://2cc2dee8-423c-81a6-91bc-000b9d1fd890`
**Database URL:** `https://www.notion.so/2cc2dee8423c81d3b522dc0c426a8638`

### Key Fields

| Field Name | Type | Notes |
|---|---|---|
| `Log Entry` | title | Entry description |
| `Material` | relation | Links to material inventory |
| `Movement Type` | select | Return, Incoming, Outgoing |
| `Quantity` | number | Amount of material |
| `unit price` | number (rupee) | Per-unit cost |
| `Total Value` | formula | Calculated total |
| `Project` | relation | Links to Project Pipeline |
| `Date` | date | Movement date |
| `Supplier` | relation | Material supplier |

### Movement Types
- **Outgoing**: Material sent to a project site (cost to project)
- **Incoming**: Material received into inventory
- **Return**: Material returned from project

## 3. Company Finance

**Data Source ID:** `collection://2762dee8-423c-8144-a923-000bc48594b8`
**Database URL:** `https://www.notion.so/2762dee8423c817b97f5c09d1b5dea2b`

### Key Fields

| Field Name | Type | Notes |
|---|---|---|
| `Reason` | title | Description of transaction |
| `Amount` | number (rupee) | Transaction amount |
| `Bucket` | select | Category: Office Expense, Petty Cash, Material Purchase, Transportation, Food, Others (for customer), vendor, Housekeeping |
| `Type` | select | Add or Deduct |
| `Project Name ` | relation | Links to Project Pipeline (trailing space!) |
| `Date` | date | Transaction date |
| `Provided by` | select | Akshay, Company, Rakesh, Praveen |
| `Mode of payment` | select | UPI, Cheque, Cash Voucher, Card, Bank Transfer, Other |
| `Verified` | checkbox | Whether entry has been verified |
| `Proof` | file | Receipt/proof upload |

### Bucket-to-Budget Mapping
| Company Finance Bucket | Maps to Budget Category |
|---|---|
| Material Purchase | Budget: Material (30%) |
| Transportation | Transport Cost |
| Petty Cash | Budget: Petty Cash (10%) |
| Office Expense | Budget: Petty Cash (10%) |
| Food | Budget: Petty Cash (10%) |
| vendor | Budget: Material (30%) |

## 4. Slack Channel

**Channel:** #all-spacecrafter
**Channel ID:** C08R5UF71L0

## 5. Notion Parent Page

**SpaceCrafter Home Page ID:** `2602dee8423c80039dbac01a1c7789c2`

## 6. Active Project Statuses (for filtering)

Include these statuses when scanning for active projects:
- Production
- Installation
- In Discussion (sales+ Design)
- Design - production design
- PAYMENT PENDING

Exclude:
- Won (completed)
- Lost
- On Hold
- Targeted (too early)
- Lead (too early)
- Repair (special case)
