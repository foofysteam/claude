---
name: kingar-offer-letter
description: Generate professional offer letters for Kingar Signs Pvt Ltd (brand SpaceCrafter Studio). Use when the user says "create offer letter", "generate offer letter", "new offer letter for [name]", "offer letter for [name]", "make offer letter", or any request to produce an employment offer letter for Kingar Signs / SpaceCrafter Studio. Collects candidate details, generates a PDF using the standard company template, previews it, then on approval uploads to Google Drive under "Offer Letters / [Year]".
---

# Kingar Offer Letter Generator

## Purpose
Generate offer letters for Kingar Signs Pvt Ltd (brand: SpaceCrafter Studio) that exactly match the standard company template — letterhead, formatting, clauses, signatory block.

## Company Details (Hardcoded — do not ask the user)
- Legal Name: Kingar Signs Private Limited
- Brand Name: SpaceCrafter Studio
- Address: 423, PWD Road, Kalkere Main Road, Horamavu Post, Bengaluru, Karnataka 560043
- Email: billing@aarkaysigns.com
- GSTIN: 29AAFCK9909G1Z3
- PAN: AAFCK9909G
- Signatory: Praveen Kumar K, Director

## Standard Defaults (Hardcoded — do not ask unless user wants to override)
- Working Days: Monday to Saturday
- Working Hours: 9:00 AM to 5:30 PM
- Leave Policy: As per company policy (12 public holidays; earned leave applicable post probation)
- Probation Clause: If employment is discontinued during the probation period, 50% of the agreed salary will be payable
- Probation Period: 3 months
- Notice Period (during probation): 15 days
- Notice Period (post confirmation): 15 days
- EPF: Provided after completion of probation

## Workflow

### Step 1: Collect Candidate Info (use AskUserQuestion or direct prompts)
**Required fields:**
1. Full Name (e.g., Mary Nancy Leena)
2. Address
3. Phone Number
4. Email ID
5. Position / Designation (e.g., HR Manager)
6. Department (auto-suggest based on position, confirm with user)
7. Reporting Manager (default: Akshay Kingar / Praveen Kumar — confirm)
8. Date of Joining
9. Annual CTC or Monthly Salary — accept either, convert and show both
10. Work Location (default: 423, PWD Road, Kalkere Main Road, Horamavu Post, Bangalore – 560043)
11. Probation Period (default: 3 months)
12. Notice Period (default: 15 days probation / 15 days confirmed)
13. Acceptance Deadline (default: 2 days from today)
14. Letter Date (default: today)

**Auto-generate based on position:**
15. Key Responsibilities — Claude should write 8-11 role-specific responsibilities based on the position. Use the Leena template style (action-oriented, bold key phrases). Show these to user for approval before generating.

### Step 2: Show summary
Display all collected info in a clean summary. Ask for confirmation before generating.

### Step 3: Generate PDF
Run the generator script:
```bash
python3 /Users/Kingar/Library/Application Support/Claude/local-agent-mode-sessions/724c065a-56ad-407b-8521-7b221e1d8c60/946b24ac-ee0b-40b8-9bc9-d12ffcb8a4f0/local_1be07556-b6a4-4139-9f74-c240bc40d6eb/outputs/kingar-offer-letter/scripts/generate.py \
  --data /path/to/data.json \
  --output /path/to/output.pdf
```

The script takes a JSON file with all the fields and outputs a PDF that matches the standard template exactly.

### Step 4: Preview to user
Share the generated PDF via computer:// link. Ask:
- "Approve and upload to Google Drive?"
- "Make changes?" (then re-collect and re-generate)

### Step 5: Upload to Google Drive (on approval)
Use the Google Drive MCP tools (mcp__0835f53c-4bfe-4158-aa8f-6e18e93e69ee__*) to:
1. Check if folder "Offer Letters" exists at Drive root. If not, create it.
2. Check if year subfolder (e.g., "2026") exists. If not, create it.
3. Upload the PDF as `[Candidate Name] - Offer Letter - [DOJ].pdf`
4. Return the Drive link to the user.

## File Naming Convention
- PDF filename: `{Candidate_Name}_Offer_Letter_{YYYYMMDD}.pdf`
- Example: `Mary_Nancy_Leena_Offer_Letter_20260121.pdf`
- Drive path: `My Drive / Offer Letters / 2026 / [filename].pdf`

## Key Responsibilities Generator Guide
Based on position, generate 8-11 responsibilities matching this style:
- Action verb + scope + outcome
- Bold key phrases using `**phrase**`
- Cover: core duties, compliance/quality, team coordination, reporting, strategic input, confidentiality
- Reference position-specific tasks (e.g., for HR Manager: ESI/EPF compliance, payroll; for Designer: design output, client coordination; for Production Manager: shop floor, vendor management)

## Template Structure (DO NOT modify the order or sections)
1. Letterhead (Kingar Signs Pvt Ltd + address)
2. Brand tag: "(SpaceCrafter Studio)"
3. Date
4. Greeting: "Dear [Name],"
5. Opening paragraph (offer + one-line value statement based on position)
6. **POSITION DETAILS** section
7. **COMPENSATION STRUCTURE** section (Fixed Salary + Performance Review)
8. **EMPLOYMENT TERMS** section (6 standard points)
9. **KEY RESPONSIBILITIES** section (8-11 role-specific points)
10. **TERMS & CONDITIONS** section (5 standard points)
11. **ACCEPTANCE** section (deadline + closing)
12. Signatory block (Praveen Kumar K, Director)
13. **ACCEPTANCE** signature block for candidate

## Important Notes
- Currency: All amounts in INR (₹). Spell out in words: "(Rupees Fifty Thousand only)"
- If user gives annual CTC, divide by 12 for monthly. Show monthly in the letter (per template).
- Date format: "DD/MM/YYYY" for letter date, "Month DDth, YYYY" for joining date
- Never change the signatory unless user explicitly asks
- Always use "SpaceCrafter Studio" with that exact capitalization
- Always preserve the brand tag `( SpaceCrafter Studio )` exactly as shown in the template
