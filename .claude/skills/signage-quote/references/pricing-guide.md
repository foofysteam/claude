# Pricing Guide & Material Catalog

This reference contains the full material catalog, LED grading system, and calculation formulas
for signage quotations. All prices should be verified against the Notion Master Unit Pricing
database before use — this file serves as a fallback and calculation reference.

## Notion Database Reference
- **Database**: Master Unit Pricing
- **URL**: https://www.notion.so/26ef3ca89bac447e808f49c0e04e93e4
- **Data Source**: `collection://6ff2badb-adc6-489b-a1af-dc6bc32a2d20`
- **Schema fields**: Material Item (title), Category, Production Phase, Signage Type, Specs/Description, Unit, Unit Price, Wastage Factor %

---

## Pricing Model

Every material line item in the BOQ follows this structure:
```
Actual Cost = Qty × Unit Rate (from Notion or fallback)
Overhead = 10% of Actual Cost (procurement, logistics, material handling)
Base Cost = Actual Cost + Overhead
```

The client price is then calculated from the total production cost (all base costs + labour):
```
Client Price = Total Production Cost ÷ (1 - Margin%)
```

The Excel output shows margin tiers from 10% to 50% so the user can choose.

---

## LED Grading System

### LED Modules (3 LEDs per module, 1.2W, 12V)

| Grade | ₹/Module | Brand Level | Lifespan | Use Case |
|-------|----------|-------------|----------|----------|
| **Grade C** (Economy) | ₹6 | Generic/unbranded | ~20,000 hrs | Budget projects, temporary signage, events |
| **Grade B** (Standard) | ₹12 | Mid-tier (e.g., good generic) | ~35,000 hrs | Regular commercial, retail chains |
| **Grade A** (Premium) | ₹16 | Samsung/Osram equivalent | ~50,000 hrs | Premium retail, hospitality, hospitals, long-warranty projects |

**Key facts:**
- 1 module = 3 individual LEDs
- Typical spacing: 1 module every 3-4 inches (for even illumination in channel letters)
- Warm white modules (3000K) carry a premium of ~₹2-3 over cool white equivalent grade

### LED Module Sizes (by letter depth)

| Module Type | Physical Size | Fits Letter Depth | Use Case |
|------------|--------------|-------------------|----------|
| **Small Module** | 10mm | 1" (25mm) thickness | Slim channel letters, tight internal spaces |
| **Large Module** | 15mm | 3" (75mm) thickness | Deep channel letters, maximum brightness |

### LED Strips & Neon Flex

| Type | Width | ₹/Meter | Roll Spec | Use Case |
|------|-------|---------|----------|----------|
| **Strip LED** | 6mm | ₹70 | 100 LEDs/meter | Side-lit letters ≤1ft, edge lighting, cove lighting |
| **Neon Flex** | 6mm | Check Notion | 5 meter rolls | Neon-style signage, decorative outlines |

### LED Selection Rule (Critical)
```
Letter Height ≤ 1 ft  →  LED STRIPS (side-lit)
Letter Height > 1 ft  →  LED MODULES (front-lit or back-lit)
  └── Depth ≤ 1" → Small Module (10mm)
  └── Depth ≥ 3" → Large Module (15mm)
```

### LED Quantity Calculation

**For front-lit channel letters (modules):**
The number of modules depends on the letter's face area and the channel depth (deeper channels allow wider spacing because light has more room to diffuse):
```
Shallow (1" / 40mm depth):  1 module per 3-4 sq inches of face area
Medium  (2" / 60mm depth):  1 module per 5-6 sq inches of face area
Deep    (3"+ / 80mm depth): 1 module per 7-8 sq inches of face area
```
Add 10% spare modules for replacements and dead-on-arrival units.

**For side-lit channel letters (strips):**
```
Total strip length = Σ(internal perimeter of each letter in meters)
Add 15% wastage for cuts, corners, and connections
```

**For back-lit / halo letters (modules behind letter):**
```
Same face-area calculation as front-lit
Modules placed on mounting surface behind the letter
```

**SMPS sizing:**
```
Total LED wattage = (modules × 1.2W) + (strip meters × watts_per_meter)
Safety factor: multiply total wattage by 1.25 (never exceed 80% SMPS capacity)
SMPS count = ceiling(Total wattage × 1.25 ÷ SMPS_wattage)

SMPS size selection:
  - Small signs (<150W load): use 200W SMPS
  - Medium signs (150-280W): use 350W SMPS
  - Large signs (280-480W): use 600W SMPS
  - Very large: use multiple 350W (more common/available than single large units)
```

---

## Raw Material Standard Sheet Sizes

Always calculate BOQ in full sheets. See `material-reference.md` for waste optimization rules.

| Material | Sheet Size 1 | Sheet Size 2 | Area (Size 1) | Area (Size 2) |
|----------|-------------|-------------|---------------|---------------|
| Aluminium (Raw/Black) | 4' × 8' | 5' × 10' | 32 sq ft | 50 sq ft |
| Acrylic | 4' × 8' | 7' × 10' | 32 sq ft | 70 sq ft |
| ACP | 4' × 8' | 5' × 10' | 32 sq ft | 50 sq ft |
| Aluminium (Coloured) | 4' × 8' | — | 32 sq ft | — |
| PVC (Foam Board) | 4' × 8' | — | 32 sq ft | — |
| Fluted Pipes (Panel) | 8" × 9 ft | — | 6 sq ft | — |

---

## Channel Letter Rising (Depth) Specifications

| Letter Depth | Rising (mm) | Channel Material | Typical Letter Size |
|-------------|-------------|-----------------|-------------------|
| **1 Inch** | 40mm | Aluminium | Small letters (<18" tall) |
| **2 Inch** | 60mm | Aluminium | Medium letters (18-36" tall) |
| **3 Inch+** | 80mm+ | Aluminium | Large letters (>36" tall) |

---

## Material Categories & Fallback Pricing

These are reference ranges. Always verify against Notion first — use these only as fallback.

### A. Lettering Materials

| Material | Rising/Depth | Unit | Fallback Range | Notes |
|----------|-------------|------|---------------|-------|
| Aluminium Channel 40mm | 1" (40mm) | rft | ₹90-130 | Most common for standard channel letters |
| Aluminium Channel 60mm | 2" (60mm) | rft | ₹110-160 | Medium depth, balanced illumination |
| Aluminium Channel 80mm+ | 3"+ (80mm+) | rft | ₹130-200 | Deep channels for large outdoor signs |
| Acrylic 4mm Opal White | — | sq ft | ₹90-130 | Standard for front-lit letter faces |
| Acrylic 3mm Clear | — | sq ft | ₹70-100 | For side-lit/edge-lit applications |
| SS Letters (Grade 304) | — | sq ft | ₹900-1,400 | Premium, corrosion-resistant |
| MS Flat-cut Letters | — | sq ft | ₹350-550 | Budget option, needs paint/coating |

### B. Backdrop & Panels

| Material | Sheet Sizes | Unit | Fallback Range |
|----------|-----------|------|---------------|
| ACP 4mm (per sq ft) | 4'×8', 5'×10' | sq ft | ₹60-95 |
| ACP 4mm (per sheet 4'×8') | 4' × 8' | sheet | ₹2,000-2,800 |
| ACP 4mm (per sheet 5'×10') | 5' × 10' | sheet | ₹3,000-3,800 |
| PVC Foam Board (per sheet) | 4' × 8' | sheet | ₹900-1,400 |
| Fluted Pipes — Internal (per panel) | 8" × 9 ft | panel | ₹800 |
| Fluted Pipes — External (per panel) | 8" × 9 ft | panel | ₹1,600 |

### C. Vinyl & Print (Standard Roll Widths)

| Material | Standard Width | Unit | Fallback Range |
|----------|---------------|------|---------------|
| Vinyl Cut (Solid Colors) | 4 ft & 5 ft rolls | sq ft | ₹30-45 |
| Vinyl Opaque (Printed) | 4 ft & 5 ft rolls | sq ft | ₹40-65 |
| Vinyl Translucent | 4 ft & 5 ft rolls | sq ft | ₹45-75 |
| Day and Night Vinyl | 4 ft rolls | sq ft | ₹55-90 |
| Wall Graphics | 53 inch (4.4 ft) | sq ft | ₹40-65 |
| Fabric (Dye-Sub) | 50 inch (4.2 ft) | sq ft | ₹45-75 |
| Frost Film | 4 ft rolls | sq ft | ₹35-55 |
| Digital Print on Flex | — | sq ft | ₹18-40 |
| Digital Print on SAV | — | sq ft | ₹35-55 |

### D. Electrical & Wiring

| Item | Specification | Unit | Fallback Range |
|------|--------------|------|---------------|
| SMPS 200W 12V | 12V, 16.7A | pcs | ₹600-900 |
| SMPS 350W 12V | 12V, 29A | pcs | ₹900-1,400 |
| SMPS 600W 12V | 12V, 50A | pcs | ₹1,500-2,200 |
| Wire 1.5mm Single Core | 1.5mm², 1 core, 90m roll | roll | ₹1,200-1,800 |
| Wire 2.5mm Twin Core | 2.5mm², 2 core | meter | ₹25-40 |
| Electrical Wiring Kit | Complete kit | lot | ₹600-1,800 |
| Junction Box | Standard | pcs | ₹120-250 |
| MCB/Switch | Standard | pcs | ₹250-450 |

### E. Structure & Hardware

| Item | Unit | Fallback Range |
|------|------|---------------|
| MS Cleat Frame | sq ft | ₹90-170 |
| MS Box Section | kg | ₹90-110 |
| Wall Plugs + Bolts | set | ₹250-600 |
| Aluminium Profile Frame | rft | ₹170-280 |

### F. Finishing

| Item | Unit | Fallback Range |
|------|------|---------------|
| Automotive Paint | sq ft | ₹35-55 |
| Powder Coating | sq ft | ₹30-45 |
| Duco Paint (Premium) | sq ft | ₹55-90 |

---

## Labour & Machine Rates

| Activity | Unit | Rate |
|----------|------|------|
| CNC / Router Cutting (Acrylic) | rft | ₹18-22 |
| CNC / Router Cutting (Aluminium) | rft | ₹22-28 |
| CNC / Router Cutting (MS/SS) | rft | ₹28-40 |
| Laser Cutting (SS) | rft | ₹45-65 |
| Bending (Aluminium channel) | rft | ₹12-18 |
| Welding (MS) | rft | ₹55-90 |
| Welding (SS/TIG) | rft | ₹90-130 |
| Painting (Spray, per coat) | sq ft | ₹18-28 |
| Assembly Labour | % of material | 15-20% |
| Installation (Standard wall) | per sign | ₹2,500-6,000 |
| Installation (Height >15ft) | per sign | ₹6,000-12,000 |
| Installation (Pylon/Structure) | per sign | ₹12,000-30,000 |
| Crane Rental (if needed) | per day | ₹6,000-18,000 |
| Transport (within city) | per trip | ₹1,800-3,500 |
| Transport (outstation) | per km | ₹18-28 |

---

## Margin Guidelines

The Excel output provides margin tiers from 10% to 50%. Here's guidance on which tier to recommend:

| Project Type | Recommended Tier | Notes |
|-------------|-----------------|-------|
| Standard Commercial | 35-40% | Regular retail, offices — the sweet spot |
| Premium / Hospitality | 40-50% | Hotels, hospitals, luxury retail — higher service expectations |
| Budget / Volume | 25-35% | Chain rollouts, repeat clients — compensate with volume |
| Government / Institutional | 30-35% | Tender-based, competitive bidding |
| Maintenance / AMC | 50-60% | Recurring revenue, high margin |

**Margin calculation (used in the Excel tiers):**
```
Client Price = Production Cost ÷ (1 - Margin%)
Example: ₹60,000 production cost at 40% margin = ₹60,000 ÷ 0.60 = ₹1,00,000
```

---

## LED Panel Procurement Rates (Per Sq Ft)

These are SpaceCrafter's actual procurement costs for LED display panels. Use these as the base material cost when a signage project includes an LED screen/panel component.

| Pixel Pitch | Procurement Rate (₹/sq ft) | GST Status | Typical Use |
|-------------|---------------------------|------------|-------------|
| **P1.8** | ₹5,800 | + GST (18%) | Indoor premium — conference rooms, lobbies, retail |
| **P2.5** | ₹4,500 | Inclusive | Indoor standard — retail displays, reception areas |
| **P4** | ₹4,500 | Inclusive | Indoor/outdoor versatile — building facades, large format |

**Important notes:**
- P1.8 landed cost = ₹5,800 + 18% GST = ~₹6,844/sq ft
- P2.5 and P4 are ₹4,500 all-inclusive (no additional GST on procurement)
- Apply standard margin tiers (10-50%) on top of these procurement rates for client pricing
- These are panel-only rates — for full LED wall projects (with controllers, processors, receivers, MS frame), use the **led-wall-calculator** skill which handles the complete installation pricing

---

## GST
- Standard GST on signage: **18%**
- Applied on top of client price
- Show separately in the margin tiers table and client quotation

## Payment Terms (Default)
- 50% advance with order confirmation
- 40% before dispatch / pre-installation
- 10% within 7 days of installation completion

## Warranty (Default)
- LED: 2-3 years (Grade A gets 3 years, Grade B gets 2 years, Grade C gets 1 year)
- Fabrication: 1 year against manufacturing defects
- Does not cover: acts of God, vandalism, electrical surges, improper maintenance
