# Raw Material Reference — Sheet Sizes, LED Selection & Fabrication Rules

This reference is derived from the Space Crafter Studio production material list.
Use it for accurate material quantity calculations, waste optimization, and correct LED/channel selection.

---

## 1. Raw Material Standard Sheet Sizes

When calculating material quantities, always work in full sheets and optimize cuts to minimize waste.

| Material | Sheet Size 1 | Sheet Size 2 | Notes |
|----------|-------------|-------------|-------|
| **Aluminium (Black/Raw)** | 4' × 8' | 5' × 10' | Used for channel letter returns, backing plates |
| **Acrylic** | 4' × 8' | 7' × 10' | Opal white, clear, colored — for letter faces, light boxes |
| **ACP (Aluminium Composite Panel)** | 4' × 8' | 5' × 10' | Backdrop panels, cladding, sign boards |
| **Aluminium (Coloured/Composite)** | 4' × 8' | — | Blue/specialty finishes for decorative panels |
| **PVC (Foam Board)** | 4' × 8' | — | Lightweight indoor signage, temporary displays |
| **Fluted Pipes (Panel)** | 8" × 9 ft | — | Signage backgrounds/backdrops, textured alternative to ACP. Narrow panels joined side-by-side. |

### Sheet Area Quick Reference
| Sheet Size | Area (sq ft) | Area (sq m) |
|-----------|-------------|-------------|
| 4' × 8' | 32 sq ft | 2.97 sq m |
| 5' × 10' | 50 sq ft | 4.65 sq m |
| 7' × 10' | 70 sq ft | 6.50 sq m |

### Material Selection Logic for BOQ
```
When calculating sheets needed:
  Total area needed (sq ft) = sign area + wastage %
  Sheets required = ceiling(Total area ÷ sheet area)

Choose sheet size to minimize waste:
  - For large signs (>32 sq ft): prefer 5'×10' or 7'×10' sheets
  - For small signs (<32 sq ft): use 4'×8' sheets
  - For acrylic letter faces: 4'×8' is standard (unless very large — then 7'×10')
  - For ACP backdrops: match sheet size to backdrop dimensions to minimize joins
  - For Fluted Pipe backdrops: panels are 8" wide × 9ft long — calculate number of panels
    needed to cover the backdrop width. Panels are joined side-by-side.
    Panels needed = ceiling(backdrop_width_in_inches ÷ 8)
    If backdrop height > 9ft, panels must be stacked vertically too.
    Waste occurs from height trimming (if backdrop < 9ft tall) and the last panel's width remainder.

Waste comparison (check both sheet sizes and pick the one with less waste):
  Option A: ceiling(total_area ÷ 32) sheets of 4'×8' → waste = (sheets × 32) - total_area
  Option B: ceiling(total_area ÷ 50) sheets of 5'×10' → waste = (sheets × 50) - total_area
  Pick the option with less waste (in sq ft).
```

---

## 2. LED Selection Rules by Letter Size

**CRITICAL RULE — This determines whether to use LED Strips or LED Modules:**

```
Letter Height ≤ 1 ft (12 inches)  →  Use LED STRIP (side-lit / edge-lit)
Letter Height > 1 ft (12 inches)  →  Use LED MODULES (front-lit / back-lit)
```

### LED Module Sizes
| Module Type | Fits Letter Thickness | Module Size | Use Case |
|------------|----------------------|-------------|----------|
| **Small Module** | 1" (25mm) letter thickness | 10mm | Slim channel letters, tight spaces |
| **Large Module** | 3" (75mm) letter thickness | 15mm | Deep channel letters, high brightness |

### LED Strip Specifications
| Type | Width | Length/Roll | Use Case |
|------|-------|-----------|----------|
| **Strip LED** | 6mm | 100 LEDs/meter | Side-lit letters ≤1ft, edge lighting |
| **Neon Flex** | 6mm | 5 meter rolls | Neon-style signage, decorative outlines |

### LED Selection Decision Tree
```
Is the letter height > 1 foot?
  ├── YES → Use LED MODULES
  │         ├── Letter depth ≤ 1" → Small Module (10mm)
  │         └── Letter depth ≥ 3" → Large Module (15mm)
  │
  └── NO (≤ 1 foot) → Use LED STRIP
                        ├── Standard look → Strip LED 6mm
                        └── Neon look → Neon Flex 6mm
```

### LED Module Quantity Calculation

The key insight: deeper channels allow wider module spacing because the light has more room to diffuse before hitting the acrylic face. Shallow channels need tighter spacing for even illumination.

```
Module density by channel depth:
  1" (40mm) depth:  1 module per 3-4 sq inches of letter face area
  2" (60mm) depth:  1 module per 5-6 sq inches of letter face area
  3"+ (80mm) depth: 1 module per 7-8 sq inches of letter face area

Calculation steps:
  1. Estimate each letter's face area (height × average width in inches)
  2. Sum all letter face areas
  3. Divide total face area by the spacing factor for the channel depth
  4. Add 10% spare for dead modules and replacements
  5. Round up to nearest whole number
```

### LED Strip Quantity Calculation
```
For letters ≤ 1ft:
  1. Calculate internal perimeter of each letter in meters
  2. Sum all letter perimeters
  3. Add 15% wastage for cuts, corners, and connections
  4. Round up to nearest 0.5m
```

### SMPS (Power Supply) Sizing

The critical thing here is not to run an SMPS at full capacity — it shortens the lifespan dramatically. Aim for 70-80% load.

```
Step 1: Calculate total LED wattage
  Module wattage = total_modules × 1.2W
  Strip wattage = total_strip_meters × wattage_per_meter
  Total LED wattage = module_wattage + strip_wattage

Step 2: Apply safety factor
  Required SMPS capacity = Total LED wattage × 1.25

Step 3: Select SMPS size
  - Required capacity < 150W  → use 200W SMPS (1 unit)
  - Required capacity 150-280W → use 350W SMPS (1 unit)
  - Required capacity 280-480W → use 600W SMPS (1 unit)
  - Required capacity > 480W → use multiple 350W units
    Number of 350W = ceiling(Required capacity ÷ 280)
    (using 280W per unit to stay at ~80% load)

Always prefer multiple smaller SMPS over one massive unit — easier to source, replace, and distribute across the sign.
```

---

## 3. Channel Letter Depth (Rising) Specifications

The letter "rising" (depth/return) determines the aluminium channel profile to use:

| Letter Depth | Rising (mm) | Channel Material | Typical Use |
|-------------|-------------|-----------------|-------------|
| **1 Inch** | 40mm | Aluminium | Standard channel letters, slim profile |
| **2 Inch** | 60mm | Aluminium | Medium depth, better light spread |
| **3 Inch+** | 80mm+ | Aluminium | Deep channel letters, large outdoor signs |

### Rising Selection Guidelines
```
Small letters (<18" tall)     → 1" / 40mm rising (compact, clean look)
Medium letters (18-36" tall)  → 2" / 60mm rising (balanced depth for good illumination)
Large letters (>36" tall)     → 3" / 80mm+ rising (deeper for even light distribution)
```

**Note:** 3 inch and above always uses Aluminium channel (not PVC or acrylic returns).

### Aluminium Channel Quantity Calculation
```
For each letter:
  Basic perimeter = 2 × (height + average_width)

  Complexity factor by letter shape:
    Simple letters (I, L, T, H, V, X, Y, Z): +0% (basic perimeter is accurate)
    Medium letters (A, C, D, E, F, J, K, M, N, P, U, W): +15%
    Complex letters (B, G, O, Q, R, S, 0-9): +30% (curves and interior cutouts)

  Letter perimeter = basic_perimeter × (1 + complexity_factor)

Total aluminium channel = sum of all letter perimeters (in running feet)
Add 10% wastage for bending losses and cuts
```

---

## 4. Printing Materials — Standard Widths

When calculating print material quantities, work from standard roll widths:

| Material | Standard Width | Use Case |
|----------|---------------|----------|
| **Vinyl (Solid/Cut)** | 4 ft and 5 ft rolls | Cut lettering, solid color graphics |
| **Day and Night Vinyl** | 4 ft rolls | Backlit applications — opaque by day, translucent at night |
| **Wall Graphics** | 53 inch (4.4 ft) | Interior wall murals, decorative wall prints |
| **Fabric (Dye-Sub)** | 50 inch (4.2 ft) | Fabric light boxes, soft signage, banners |
| **Frost Film** | 4 ft rolls | Glass frosting, privacy films, decorative glass |

### Print Material Selection Logic
```
Outdoor signage graphics     → Vinyl (4ft or 5ft)
Backlit sign panels          → Day and Night Vinyl (4ft)
Interior wall branding       → Wall Graphics (53 inch)
Fabric light box             → Fabric (50 inch)
Glass/window treatment       → Frost Film (4ft)
```

### Print Quantity Calculation
```
Print area (sq ft) = width × height of graphic
Roll length needed = print area ÷ roll width (in ft)
Add 10% for bleed, overlap, and wastage
```

---

## 5. Electrical — Wiring Specifications

| Wire Type | Specification | Roll Length | Use Case |
|-----------|--------------|-------------|----------|
| **1.5mm Single Core** | 1.5mm², 1 core | 90 meter rolls | LED module connections, internal sign wiring |
| **2.5mm Twin Core** | 2.5mm², 2 core | Standard rolls | Main power feed, SMPS connections, longer runs |

### Wiring Selection Rules
```
LED module internal wiring       → 1.5mm single core
Short runs (< 5 meters)         → 1.5mm single core
Main power supply feed           → 2.5mm 2-core
Long runs (> 5 meters)          → 2.5mm 2-core
Multiple SMPS connections        → 2.5mm 2-core
```

### Wire Quantity Estimation
```
Internal wiring (1.5mm):
  Per letter: ~1.5m (for connecting module chains within the letter)
  Total = letter_count × 1.5m
  Add 20% extra for routing and connections
  Convert to rolls: ceiling(total_meters ÷ 90) rolls

Main feed wiring (2.5mm):
  SMPS to power source: measure/estimate distance
  Between SMPS units: ~2m each
  Total = power_source_distance + (SMPS_count × 2m)
  Add 20% extra
```

---

## 6. Acrylic Face Area Estimation

When exact letter dimensions aren't available, use these rules of thumb:

```
For channel letters on a sign:
  Total letter face area ≈ 55-65% of the sign's overall area
  (The rest is spacing between letters and margins)

For individual letter estimation:
  Letter face area ≈ letter_height × (letter_height × width_ratio)

  Width ratios by letter:
    Narrow (I, l, 1):        0.25
    Medium (most letters):    0.55-0.65
    Wide (M, W, O, Q):       0.70-0.80
```

---

## 7. Material-to-Signage Type Quick Reference

| Signage Type | Raw Material | LED Type | Channel Depth | Print Material |
|-------------|-------------|----------|---------------|----------------|
| Front-lit channel (small ≤1ft) | Aluminium + Acrylic | Strip LED | 40mm | — |
| Front-lit channel (large >1ft) | Aluminium + Acrylic | LED Modules | 60-80mm | — |
| Back-lit / Halo letters | Aluminium | LED Modules | 40-60mm | — |
| ACP sign board + letters | ACP + Aluminium | Modules or Strip | 40-60mm | Vinyl |
| Light box (slim) | Aluminium frame + Acrylic | LED Strip | — | — |
| Light box (deep) | Aluminium frame + Acrylic | LED Modules | — | — |
| Printed board | ACP or PVC or Fluted Pipes | None or backlit | — | Vinyl / SAV |
| Fluted pipe backdrop + letters | Fluted Pipes + Aluminium | Modules or Strip | 40-60mm | Vinyl |
| Neon flex sign | Acrylic backing | Neon Flex | — | — |
| Interior wayfinding | Acrylic or PVC | Strip or None | — | Vinyl / Frost |
| Fabric light box | Aluminium frame + Fabric | LED Strip | — | Fabric (dye-sub) |
| Wall graphics | — | None | — | Wall Graphics (53") |
| Glass branding | — | None | — | Frost Film (4ft) |
