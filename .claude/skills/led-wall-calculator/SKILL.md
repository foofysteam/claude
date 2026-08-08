---
name: led-wall-calculator
description: >
  Calculate LED panel/wall pricing for indoor and outdoor installations. Computes total cost including
  panels, controllers, processors, power supplies, receiver cards, MS frame support, and generates
  a quotation with user-defined margin. Always use this skill when the user mentions: LED wall,
  LED panel, LED screen, digital screen, P1.2, P1.8, P2.5, P4, pixel pitch, LED display quote,
  LED wall cost, LED panel pricing, video wall, indoor LED, outdoor LED, LED screen quotation,
  digital display costing, LED wall calculator, conference room screen, auditorium LED, retail LED display,
  stage LED screen, or any request involving LED panel/screen sizing, pricing, or quotation.
  Also trigger when the user provides dimensions and asks about LED screen costs, even if they
  don't say "LED wall" explicitly. This is a dedicated calculator — not the general signage-quote skill.
---

# LED Wall / Panel Calculator

Calculate complete LED wall installation costs — from panel pricing through controllers, processors, MS framing, and final client quotation with margin control.

## Reference Files
1. `references/pricing-master.md` — All standard rates for panels, controllers, processors, frames, and accessories by use case
2. `references/calculation-guide.md` — Formulas for area, controller counts, power supply sizing, and frame costing

Read both reference files before generating any quote.

---

## Step 1: Gather Requirements

Before any calculation, collect these inputs from the user. Ask for anything missing — don't assume.

### Required Inputs

| Input | Why It Matters |
|-------|---------------|
| **Use case** — Indoor or Outdoor | Determines panel type, pixel pitch options, and pricing tier |
| **Dimensions** — Width × Height (in feet) | Drives total area, panel count, and frame cost |
| **Pixel pitch** — P1.2, P1.8, P2.5 (indoor) or P4 (outdoor) | Sets the per-sqft panel rate |

### Optional Inputs (use defaults if not specified)

| Input | Default |
|-------|---------|
| Novastar processor needed? | Yes for indoor screens ≥100 sqft, not standard for outdoor |
| MS frame support needed? | Yes (always required) |
| Installation location / city | Hyderabad |
| Client name | — |

### Classification Logic

Based on the inputs, classify the project:

```
OUTDOOR:
  └── P4 Digital Screen
      ├── Small Scale: area ≤ 50 sqft (e.g., 4×6, 8×4, 5×10 ft)
      │     → 1 controller, flat MS frame cost
      └── Large Scale: area > 50 sqft (e.g., 20×10, 30×10 ft)
            → 2-3 controllers, MS frame per sqft

INDOOR:
  ├── Standard Indoor: area ≤ 200 sqft
  │     → TB40 controller, standard setup
  └── Large Indoor: area > 200 sqft (e.g., 60×12 ft = 720 sqft)
        → Novastar processor + control card, heavy-duty MS frame
```

Present the classification back to the user for confirmation before calculating.

---

## Step 2: Calculate Costs

Read `references/calculation-guide.md` for the exact formulas. Here's the high-level flow:

### 2a. Panel Cost
```
Total Area (sqft) = Width (ft) × Height (ft)
Panel Cost = Total Area × Rate per sqft (from pricing-master.md)
```

### 2b. Controller / Processor Cost
Based on classification (see calculation-guide.md for thresholds):
- Outdoor small: 1 controller
- Outdoor large: 2-3 controllers based on area
- Indoor standard: TB40 controller
- Indoor large: Novastar processor + control card

### 2c. MS Frame Support
```
MS Frame Cost = Total Area × ₹250/sqft
```
This is the standard rate for structural MS frame support behind the LED panels. For outdoor large-scale, this may go up to ₹185-250/sqft depending on height and wind exposure.

### 2d. Power Supply
Rong brand power supplies, 1-year warranty. Count based on total panel wattage (see calculation-guide.md).

### 2e. Receiver Cards
DH712 Novastar receiver cards. Count based on total panel area (see calculation-guide.md).

### 2f. Accessories & Wiring
Standard electrical kit, junction boxes, cabling. Calculated as a percentage of panel cost.

---

## Step 3: Build the Cost Summary

After calculating all components, present a clear cost breakdown:

```
LED Wall Cost Breakdown
═══════════════════════
Project: [Client Name / Description]
Type: [Indoor / Outdoor]
Pixel Pitch: [P-value]
Dimensions: [W] ft × [H] ft = [Area] sqft

┌─────────────────────────────────┬──────────────┐
│ Component                       │ Cost (₹)     │
├─────────────────────────────────┼──────────────┤
│ LED Panels ([Area] sqft × ₹XX) │ X,XX,XXX     │
│ Controller(s)                   │ XX,XXX       │
│ Novastar Processor (if applicable)│ X,XX,XXX   │
│ Receiver Cards (X nos)          │ XX,XXX       │
│ Power Supplies (X nos)          │ XX,XXX       │
│ MS Frame Support ([Area] sqft)  │ X,XX,XXX     │
│ Wiring & Accessories            │ XX,XXX       │
├─────────────────────────────────┼──────────────┤
│ TOTAL BASE COST                 │ XX,XX,XXX    │
└─────────────────────────────────┴──────────────┘

Warranty: [2 years on panels & tiles / 1 year on power supply]
```

Use Indian number formatting (₹ X,XX,XXX) throughout.

---

## Step 4: Margin & Client Pricing

This is key — the user sets their own margin. Present a margin tier table so they can pick the right price point:

```
Margin Analysis
═══════════════
Base Production Cost: ₹XX,XX,XXX

┌──────────┬───────────────┬──────────────┬───────────────┬──────────────┐
│ Margin % │ Client Price  │ GST 18%      │ Grand Total   │ Your Profit  │
├──────────┼───────────────┼──────────────┼───────────────┼──────────────┤
│ 10%      │ Base ÷ 0.90   │ 18% of CP    │ CP + GST      │ CP - Base    │
│ 15%      │ Base ÷ 0.85   │              │               │              │
│ 20%      │ Base ÷ 0.80   │              │               │              │
│ 25%      │ Base ÷ 0.75   │              │               │              │
│ 30%      │ Base ÷ 0.70   │              │               │              │  ← Competitive
│ 35%      │ Base ÷ 0.65   │              │               │              │  ← Standard
│ 40%      │ Base ÷ 0.60   │              │               │              │  ← Sweet spot
│ 45%      │ Base ÷ 0.55   │              │               │              │
│ 50%      │ Base ÷ 0.50   │              │               │              │  ← Premium
└──────────┴───────────────┴──────────────┴───────────────┴──────────────┘
```

**Margin formula:** `Client Price = Base Cost ÷ (1 - Margin%)`

After showing the table, ask the user which margin they want for the client-facing quote.

---

## Step 5: Generate Excel Quotation (Optional)

If the user wants a formal quote, read the xlsx SKILL.md and generate a workbook with:

### Sheet 1 — Internal Cost Breakdown
All components with quantities, unit rates, and line totals. This is for the user's eyes only.

### Sheet 2 — Margin Analysis
The tier table from Step 4, with formulas so the user can adjust.

### Sheet 3 — Client Quotation
Clean, professional quote with:
- Company header: SPACE CRAFTER STUDIO / Kingar Signs Private Limited
- Brand purple #6A0DAD accent
- Line items (panels, installation, controller setup — no internal cost details)
- Subtotal → GST 18% → Grand Total
- Terms:
  - Payment: 50% advance | 40% pre-dispatch | 10% post-installation
  - Warranty: 2 years on LED panels/tiles, 1 year on power supply
  - Delivery: [X] working days
  - Quote validity: 15 days

File naming: `[ClientName]_LED_Wall_Quote_[Date].xlsx`

---

## Important Rules

1. **Always ask for use case first** — Indoor vs Outdoor changes everything: panel type, pricing, controller logic, and frame calculations.

2. **Always ask for dimensions** — Never guess. The entire calculation flows from Width × Height.

3. **MS frame is always required** — ₹250/sqft standard. This covers the structural steel support behind the LED panels.

4. **Show margin tiers, don't pick one** — Let the user choose their margin. Highlight the 30-40% range as the sweet spot.

5. **Indian number format** — Always use ₹ X,XX,XXX (lakhs/crores notation).

6. **Component specs matter** — Always mention: Qangali tiles, Rong power supply, DH712 Novastar receiver, Novastar TB40 controller. These are the standard components — the user's clients need to know exact brands.

7. **Warranty clarity** — 2 years on panels/tiles (Qangali), 1 year on power supply (Rong). Always state this.

8. **GST is separate** — All base costs and margin calculations are pre-GST. GST 18% is added on top of the client price.
