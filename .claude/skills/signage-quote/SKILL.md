---
name: signage-quote
description: >
  Generate professional signage quotations from design images or specs. Analyzes uploaded signage designs to identify materials,
  dimensions, LED types, and fabrication methods, then produces a full Excel quote package with internal BOQ, client quotation,
  and margin analysis. Always use this skill when the user mentions: signage quote, BOQ, signage pricing, channel letter costing,
  signage estimate, quotation for signage, fabrication costing, create quote, cost estimate, develop quote, price this, or
  uploads a signage design image and asks for pricing. Also trigger when the user references any signage project needing a
  cost breakdown. This skill pulls live pricing from the Notion Master Unit Pricing database to ensure accuracy — never
  hardcode prices.
---

# Signage Quote Generator

Generate a complete signage quotation package from a design image or specs: a multi-sheet Excel workbook showing actual material costs, procurement overhead, and margin tiers from 10% to 50% so the user can pick the right price point for each client.

## Workflow Overview

```
Image/Specs Upload → Analyze & List Materials → User Confirms → Pull Notion Prices → Calculate BOQ → Generate Excel (with margin tiers)
```

### Reference Files (Read these before generating any quote)
1. `references/material-reference.md` — Raw material sheet sizes, LED selection rules by letter size, channel depth/rising specs, printing material widths, wiring specs, and quantity calculation formulas
2. `references/pricing-guide.md` — Full material catalog, LED grading system, calculation formulas, margin guidelines, and fallback pricing
3. `references/signage-types.md` — Visual identification guide for analyzing uploaded images

---

## Step 1: Analyze the Input

### If an image is uploaded:
1. Examine the image carefully for:
   - **Signage type**: front-lit, back-lit, halo-lit, side-lit, light box, pylon, totem, ACP cladding, etc.
   - **Materials visible**: acrylic faces, aluminium channels, ACP backdrop, fluted pipes backdrop, stainless steel, MS structure, vinyl
   - **LED type**: Apply the **1ft rule** from `references/material-reference.md`:
     - Letter height ≤ 1ft → LED Strips (6mm, side-lit)
     - Letter height > 1ft → LED Modules (10mm small or 15mm large based on letter depth)
   - **Estimated dimensions**: width × height in inches or feet (use reference objects in image if available)
   - **Letter count and style**: individual channel letters, flat-cut, built-up, router-cut
   - **Mounting method**: wall-mounted, projection, pylon, hanging
   - **Finish**: painted, powder-coated, brushed, polished, vinyl-wrapped
   - **Any digital print or vinyl graphics**

2. Present findings as a clear list to the user:
   ```
   Here's what I can see in the design:

   - Sign Type: [e.g., Front-lit channel letters on ACP backdrop]
   - Estimated Dimensions: [e.g., 12ft × 3ft]
   - Letters/Content: [e.g., "BRAND NAME" — 9 letters, English]
   - Letter Material: [e.g., Aluminium channel 40mm depth, acrylic face]
   - Channel Rising: [e.g., 1" / 40mm — per material-reference.md rising chart]
   - Backdrop: [e.g., 4mm ACP with matt black finish, 4'×8' sheet / Fluted Pipes 8"×9ft panels]
   - LED Type: [e.g., Cool white modules (letters >1ft) or strips (letters ≤1ft)]
   - LED Module Size: [e.g., Small 10mm for 1" depth, or Large 15mm for 3" depth]
   - Structure: [e.g., Wall-mounted, MS cleat frame]
   - Finish: [e.g., Automotive paint on channels]

   Please confirm or correct these details so I can generate an accurate quote.
   ```

3. Wait for user confirmation before proceeding. The user may correct dimensions, specify exact materials, change LED grade, or add items.

### If specs are provided as text:
Gather these inputs (ask for anything missing):

| Input | Example | Required? |
|-------|---------|-----------|
| Sign dimensions (W × H) | 344" × 48" or 12ft × 3ft | Yes |
| Content / text | "BRAND NAME" English + logo | Yes |
| Letter type | Front-lit channel letters, 40mm depth | Yes |
| Material specs | Aluminium channels, 4mm opal acrylic, ACP backdrop | Yes |
| LED type + grade | Cool white modules Grade A | Yes |
| Client name | Client ABC | Yes |
| Location / city | Hyderabad | Preferred |
| Mounting type | Wall / projection / pylon | Preferred |

---

## Step 2: Pull Pricing from Notion

This is critical — always fetch live pricing from the Master Unit Pricing database first. The Notion database is the source of truth for current rates.

### Notion Database Details
- **Database**: Master Unit Pricing
- **Database URL**: https://www.notion.so/26ef3ca89bac447e808f49c0e04e93e4
- **Data Source ID**: `collection://6ff2badb-adc6-489b-a1af-dc6bc32a2d20`

### How to fetch prices:
Use the Notion search tool to query the data source for each material needed:
```
Search data_source_url: collection://6ff2badb-adc6-489b-a1af-dc6bc32a2d20
Query: [material name]
```

Then fetch each result page to get the exact Unit Price, Unit, and Specs.

### LED Pricing — Grade System

LED modules and strips have a quality grading system. The grade system below is the ground truth for LED pricing:

**LED Modules (3 LEDs per module, 1.2W):**
| Grade | Price/Module | Use Case |
|-------|-------------|----------|
| Grade C (Economy) | ₹6 | Budget projects, short-term signage |
| Grade B (Standard) | ₹12 | Regular commercial signage |
| Grade A (Premium) | ₹16 | Premium retail, hospitality, long warranty |

**LED Strips:**
| Type | Base Price | Unit |
|------|-----------|------|
| Standard Strip | ₹70 | per meter |

If the Notion database shows different LED prices than the grade system above, flag this to the user. The grade system (₹6/₹12/₹16 for modules) is the definitive pricing for modules.

### Materials to fetch (typical signage project):
Read `references/pricing-guide.md` for the full material catalog and calculation formulas. If a material isn't found in Notion, use the fallback prices in pricing-guide.md and clearly mark them as estimates.

---

## Step 3: Calculate the BOQ

After confirming specs and pulling prices, calculate quantities for every material.

### Key calculation principles:

**Read `references/material-reference.md` first for sheet sizes, LED rules, and rising specs.**

1. **Acrylic/Face area** = total letter face area in sq ft
   - For channel letters, calculate each letter's actual face area based on its dimensions (height × average width)
   - Convert to **full sheets**: 4'×8' (32 sq ft) or 7'×10' (70 sq ft) — choose the size that minimizes waste
   - Apply 10-15% wastage for irregular letter shapes

2. **Aluminium channel** = total perimeter of all letters in running feet
   - Each letter's perimeter ≈ 2×(height + average width) + internal features
   - For complex letters (R, B, S, G, etc.) with interior cutouts, add ~30% to the basic perimeter
   - Select rising based on letter size: 1" = 40mm, 2" = 60mm, 3"+ = 80mm

3. **ACP / Fluted Pipes backdrop** = W × H of backdrop in sq ft
   - ACP: Convert to **full sheets**: 4'×8' (32 sq ft) or 5'×10' (50 sq ft) — minimize joins
   - Fluted Pipes: Sold as narrow **panels (8" wide × 9 ft long)**. Multiple panels are joined side-by-side to cover the backdrop width.
     - Panels needed = ceiling(backdrop_width_in_inches ÷ 8) × ceiling(backdrop_height_in_ft ÷ 9)
     - Waste comes from trimming the last panel's width and any height excess under 9ft
     - Pricing: ₹800/panel (internal/vendor cost), ₹1,600/panel (external/client-facing cost)
   - For backdrops wider than 8ft, account for multiple ACP sheets and joining strips

4. **LED Modules** — Apply the **1-foot rule** (letters > 1ft height):
   - Calculate the face area of each letter in square inches
   - Module density depends on letter depth and desired brightness:
     - Shallow letters (1" / 40mm depth): ~1 module per 3-4 sq inches (tighter spacing needed for even illumination)
     - Medium letters (2" / 60mm depth): ~1 module per 5-6 sq inches
     - Deep letters (3"+ / 80mm+ depth): ~1 module per 7-8 sq inches (light has more room to spread)
   - Total modules = sum of (each letter's face area ÷ spacing factor)
   - Add 10% spare for dead modules and replacements

5. **LED Strips** (letters ≤ 1ft height):
   - Total strip length = sum of internal perimeter of each letter in meters
   - Add 15% wastage for cuts, connections, and corners

6. **SMPS (Power Supply) Sizing**:
   - Total LED wattage = (total modules × 1.2W per module) + (total strip meters × wattage per meter)
   - Apply 1.25× safety factor (never run SMPS at full load — degrades lifespan)
   - SMPS count = ceiling(Total wattage × 1.25 ÷ SMPS rated wattage)
   - Common SMPS sizes: 200W (for small signs), 350W (standard), 600W (large installations)
   - Use the smallest SMPS size that keeps load at 70-80% capacity for best efficiency

7. **Wiring**:
   - 1.5mm single core (90m rolls): ~1.5m per letter for internal LED connections
   - 2.5mm 2-core: for main power feed from mains to SMPS, and SMPS to sign (distance-dependent)
   - Add 20% extra for routing and connections

8. **Print materials**: use standard roll widths from material-reference.md
   - Calculate sq ft needed, divide by roll width to get running length
   - Add 10% for bleed, overlap, and wastage

9. **Paint** = total painted surface area in sq ft (channel sides + returns + any structural elements)

10. **Structure / MS frame** = based on sign size and mounting type

11. **Wastage factor**: apply the appropriate % from Notion for each material (default 10% for regular shapes, 15% for irregular/complex)

---

## Step 4: Generate the Excel Quote Package

Read the xlsx SKILL.md before generating the Excel file — follow its formatting best practices.

Create a workbook with the following sheets:

### Sheet 1 — Material Cost Breakdown (Internal)

This is the core pricing sheet. For every material line item:

| Column | Description |
|--------|-------------|
| S.No | Serial number |
| Item | Material name |
| Specification | Size, grade, type details |
| Category | Lettering / Illumination / Backdrop / Electrical / Structure / Finishing |
| Qty | Calculated quantity |
| Unit | sq ft / rft / pcs / meter / sheet / roll / lot |
| Actual Unit Rate (₹) | The real cost from Notion (or fallback) |
| Actual Cost (₹) | Qty × Actual Unit Rate |
| Overhead (₹) | 10% of Actual Cost — covers procurement, logistics, and material handling |
| Base Cost (₹) | Actual Cost + Overhead |

Group rows by production phase: Lettering → Illumination → Backdrop → Electrical → Structure → Finishing

At the bottom: **Total Base Cost** = sum of all Base Cost values

### Sheet 2 — Labour & Machine Cost

| Column | Description |
|--------|-------------|
| S.No | Serial number |
| Activity | CNC cutting, welding, painting, assembly, installation, etc. |
| Specification | Material type, method details |
| Qty | Amount of work |
| Unit | rft / sq ft / per sign / lot |
| Rate (₹) | Per-unit rate |
| Amount (₹) | Qty × Rate |

Categories: CNC/Router → Bending → Welding → Painting → Assembly → Installation → Transport

At the bottom: **Total Labour Cost**

### Sheet 3 — Margin Analysis & Client Pricing

This is the key sheet for decision-making. It shows the total production cost and then presents client pricing at different margin levels so the user can pick the right price point.

**Summary section at top:**
| Item | Amount (₹) |
|------|-----------|
| Total Material Base Cost (from Sheet 1) | [value] |
| Total Labour Cost (from Sheet 2) | [value] |
| **Total Production Cost** | [sum] |

**Margin Tiers Table:**
| Margin % | Client Price (₹) | GST 18% (₹) | Grand Total (₹) | Profit (₹) |
|----------|-----------------|-------------|-----------------|------------|
| 10% | Production Cost ÷ 0.90 | 18% of client price | Client + GST | Client Price - Production Cost |
| 15% | Production Cost ÷ 0.85 | ... | ... | ... |
| 20% | Production Cost ÷ 0.80 | ... | ... | ... |
| 25% | Production Cost ÷ 0.75 | ... | ... | ... |
| 30% | Production Cost ÷ 0.70 | ... | ... | ... |
| 35% | Production Cost ÷ 0.65 | ... | ... | ... |
| 40% | Production Cost ÷ 0.60 | ... | ... | ... |
| 45% | Production Cost ÷ 0.55 | ... | ... | ... |
| 50% | Production Cost ÷ 0.50 | ... | ... | ... |

The margin formula: **Client Price = Production Cost ÷ (1 - Margin%)**

Highlight the 30-40% range as the typical sweet spot (use a light green background on those rows).

### Sheet 4 — Client Quotation (Client-Facing)

This is the clean, professional sheet to share with the client. No internal costs, overhead, or margin details visible here.

- Company header: "SPACE CRAFTER STUDIO" / Kingar Signs Private Limited, Hyderabad
- Use brand purple #6A0DAD as accent color
- Line items grouped logically:
  - A. Channel Letters / Signage Elements
  - B. Backdrop / Panels
  - C. Illumination (LED)
  - D. Electrical (SMPS, wiring)
  - E. Structure & Mounting
  - F. Installation
- Each line: S.No, Description, Qty, Unit, Rate, Amount
- The rates here come from the margin tier the user selects (default to 40% if not specified — but ask the user which margin tier to use for the client sheet)
- Subtotal → GST @ 18% → Grand Total
- Terms block at bottom:
  - Payment: 50% advance | 40% pre-dispatch | 10% post-installation
  - Delivery: [X] working days from advance receipt
  - Warranty: [X] year on LED, 1 year on fabrication
  - Quote validity: 15 days

### Formatting Standards:
- Currency format: ₹ #,##0 (Indian Rupees, no decimals)
- Headers: Bold white text on purple (#6A0DAD) background
- Category sub-headers: Purple text on light purple (#F0E6FF) background
- Alternating row shading for readability
- The margin tier rows at 30-40% should have a light green (#E8F5E9) background to highlight the typical range
- Print-ready: A4 landscape, fit to page width
- Freeze panes on header rows

---

## Step 5: Generate Interactive Configurator (Optional)

Only if the user asks for it or the project is complex enough. Create a React (.jsx) artifact that lets the client explore options:

- Toggle LED grade (Economy/Standard/Premium)
- Select backdrop material (ACP / Fluted Pipes) and finish (Matt/Glossy/Brushed)
- Choose delivery speed (Standard/Express)
- Margin slider or tier selector
- Real-time price updates
- Professional layout with Space Crafter Studio branding

---

## Important Notes

1. **Always pull from Notion first.** The Master Unit Pricing database is the source of truth. If a material isn't in Notion, use fallback prices from `references/pricing-guide.md` and clearly mark them as estimates.

2. **LED module grades override Notion.** The ₹6/₹12/₹16 per module grading is the definitive pricing. If Notion shows different numbers, flag the discrepancy to the user.

3. **Ask before assuming.** When analyzing images, list what you see and let the user confirm before generating the quote.

4. **10% overhead per material line item.** Overhead is calculated as 10% of the Actual Cost for each material row. It covers sourcing, logistics, quality checking, and material handling.

5. **Show margin tiers, not a single price.** The Excel output should always include the margin analysis sheet with tiers from 10-50%, so the user can decide the right price point for each client situation.

6. **Ask which margin tier for the client sheet.** Before generating Sheet 4 (Client Quotation), ask the user which margin % to apply. Default to 40% if they don't specify.

7. **Update the Notion page** for the project if the user asks. Search for the project in Notion's Project Pipeline and update the quote amount.

8. **File naming**: `[ClientName]_Signage_Quote_[Date].xlsx`
