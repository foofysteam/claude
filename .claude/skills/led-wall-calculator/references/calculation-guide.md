# LED Wall Calculation Guide

Step-by-step formulas for calculating a complete LED wall installation cost.

---

## Step 1: Total Area

```
Total Area (sqft) = Width (ft) × Height (ft)
```

Always work in feet. If the user gives dimensions in meters, convert: 1 meter = 3.281 feet.

---

## Step 2: Panel Cost

### Indoor (Qangali tiles)

```
Panel Cost = Total Area × Rate per sqft

Where rate depends on pixel pitch:
  P1.2 → ₹16,500/sqft
  P1.8 → ₹7,700/sqft
  P2.5 → ₹5,650/sqft
```

### Outdoor

```
Panel Cost = Total Area × ₹4,600/sqft (P4)
```

### Large Internal (P2.5 premium config, area > 200 sqft)

```
Panel Cost = Total Area × ₹6,500/sqft (+ GST noted separately)
```
Plus control card: ₹82,000 flat.

---

## Step 3: Controller / Processor

### Decision tree:

```
Is it OUTDOOR?
  ├── Area ≤ 50 sqft  →  1 × Novastar TB40 = ₹18,000
  ├── Area 50-150 sqft  →  2 × Novastar TB40 = ₹36,000
  └── Area > 150 sqft  →  3 × Novastar TB40 = ₹54,000

Is it INDOOR?
  ├── Area ≤ 200 sqft  →  1 × Novastar TB40 = ₹18,000
  └── Area > 200 sqft  →  Novastar Processor = ₹4,50,000 + Control Card = ₹82,000
                           Total = ₹5,32,000
```

---

## Step 4: Receiver Cards (DH712 Novastar)

Each receiver card drives a portion of the LED panel. Higher pixel density (smaller P value) means more data per sqft, so more cards needed.

```
Receiver card count = ceiling(Total Area ÷ Coverage per card)

Coverage per card:
  P1.2 → 20 sqft/card
  P1.8 → 25 sqft/card
  P2.5 → 30 sqft/card
  P4   → 35 sqft/card

Receiver Card Cost = Count × ₹3,500
```

**Always round UP** — you can't use a partial card.

---

## Step 5: Power Supplies (Rong, 1yr warranty)

Each PSU powers a section of panels. Higher density panels draw more power.

```
PSU count = ceiling(Total Area ÷ Coverage per PSU)

Coverage per PSU:
  P1.2 → 12 sqft/PSU
  P1.8 → 15 sqft/PSU
  P2.5 → 18 sqft/PSU
  P4   → 20 sqft/PSU

PSU Cost = Count × ₹2,500
```

**Always round UP.**

---

## Step 6: MS Frame Support

The structural steel frame that holds the LED panels. Always required.

### Standard calculation:
```
MS Frame Cost = Total Area × ₹250/sqft
```

### Exceptions:

**Outdoor small (≤50 sqft):**
Use the flat rate of ₹20,000 instead of per-sqft, since a simple frame is sufficient.

**Outdoor large with significant height (>15ft high):**
May increase to ₹250-300/sqft due to wind load reinforcement. Use ₹250 as default unless the user specifies challenging conditions.

**Large internal (>200 sqft):**
For very large indoor screens (like the 60×12ft reference), the MS frame fabrication is a significant cost. The reference project at 720 sqft had an MS frame cost of ₹1,55,000 — which works out to ~₹215/sqft. For estimation, continue using ₹250/sqft as the standard rate, which builds in a small buffer.

---

## Step 7: Accessories & Wiring

Quick estimation:

```
Small (≤50 sqft):       ₹15,000 flat
Medium (50-200 sqft):   ₹25,000 flat
Large (>200 sqft):      ₹40,000 + ₹50 × (Area - 200)
```

This covers: electrical wiring, data cables, junction boxes, connectors, surge protection.

---

## Step 8: Total Base Cost

```
Total Base Cost = Panel Cost
                + Controller/Processor Cost
                + Receiver Card Cost
                + PSU Cost
                + MS Frame Cost
                + Accessories & Wiring
```

For large internal screens, add the Control Card (₹82,000) if Novastar Processor is included.

---

## Step 9: Margin Calculation

```
Client Price = Total Base Cost ÷ (1 - Margin%)

Examples at different margins:
  10% margin: Base ÷ 0.90
  20% margin: Base ÷ 0.80
  30% margin: Base ÷ 0.70
  35% margin: Base ÷ 0.65
  40% margin: Base ÷ 0.60  ← Sweet spot
  50% margin: Base ÷ 0.50
```

---

## Step 10: GST

```
GST = Client Price × 0.18
Grand Total = Client Price + GST
```

---

## Worked Example: Indoor P2.5, 20ft × 10ft

```
Area = 20 × 10 = 200 sqft
Classification: Indoor standard (≤200 sqft)

Panel Cost:        200 × ₹5,650  = ₹11,30,000
Controller:        1 × TB40      = ₹18,000
Receiver Cards:    ceil(200/30)   = 7 cards × ₹3,500 = ₹24,500
Power Supplies:    ceil(200/18)   = 12 PSUs × ₹2,500 = ₹30,000
MS Frame:          200 × ₹250    = ₹50,000
Accessories:       Medium         = ₹25,000
                                    ─────────
Total Base Cost:                  = ₹12,77,500

At 40% margin:
  Client Price = ₹12,77,500 ÷ 0.60 = ₹21,29,167
  GST 18%      = ₹3,83,250
  Grand Total  = ₹25,12,417
  Your Profit  = ₹8,51,667
```

---

## Worked Example: Outdoor P4, 8ft × 4ft (Small)

```
Area = 8 × 4 = 32 sqft
Classification: Outdoor small (≤50 sqft)

Panel Cost:        32 × ₹4,600   = ₹1,47,200
Controller:        1 × TB40      = ₹18,000
Receiver Cards:    ceil(32/35)    = 1 card × ₹3,500 = ₹3,500
Power Supplies:    ceil(32/20)    = 2 PSUs × ₹2,500 = ₹5,000
MS Frame:          Flat rate      = ₹20,000
Accessories:       Small          = ₹15,000
                                    ─────────
Total Base Cost:                  = ₹2,08,700

At 35% margin:
  Client Price = ₹2,08,700 ÷ 0.65 = ₹3,21,077
  GST 18%      = ₹57,794
  Grand Total  = ₹3,78,871
  Your Profit  = ₹1,12,377
```

---

## Worked Example: Large Indoor P2.5, 60ft × 12ft

```
Area = 60 × 12 = 720 sqft
Classification: Indoor large (>200 sqft) — premium config

Panel Cost:        720 × ₹6,500  = ₹46,80,000 (+ GST)
Processor:         Novastar       = ₹4,50,000
Control Card:                     = ₹82,000
Receiver Cards:    ceil(720/30)   = 24 cards × ₹3,500 = ₹84,000
Power Supplies:    ceil(720/18)   = 40 PSUs × ₹2,500 = ₹1,00,000
MS Frame:          720 × ₹250    = ₹1,80,000
Accessories:       Large          = ₹40,000 + ₹50×520 = ₹66,000
                                    ─────────
Total Base Cost:                  = ₹55,42,000

At 40% margin:
  Client Price = ₹55,42,000 ÷ 0.60 = ₹92,36,667
  GST 18%      = ₹16,62,600
  Grand Total  = ₹1,08,99,267
  Your Profit  = ₹36,94,667
```

---

## Quick Reference: Per-Sqft All-In Estimates

For rapid ballpark quoting before doing the full calculation:

| Config | Panel + Everything (₹/sqft approx) | At 40% Margin (₹/sqft) |
|--------|-------------------------------------|------------------------|
| Indoor P1.2 | ~₹18,500 | ~₹30,800 |
| Indoor P1.8 | ~₹9,200 | ~₹15,300 |
| Indoor P2.5 | ~₹7,200 | ~₹12,000 |
| Outdoor P4 | ~₹6,500 | ~₹10,800 |
| Large Internal P2.5 | ~₹8,500 | ~₹14,200 |

These are rough estimates only. Always do the full calculation for actual quotes.
