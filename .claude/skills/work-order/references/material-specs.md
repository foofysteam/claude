# Material Specifications — Quick Reference for Work Orders

This reference contains the physical specs a production team needs: sheet sizes, LED selection rules,
channel depth charts, and material properties. No pricing — just fabrication facts.

---

## 1. Standard Sheet Sizes

| Material | Sheet Size | Dimensions | Area (sq ft) | Area (sq in) | Thickness Options |
|----------|-----------|------------|-------------|-------------|-------------------|
| **Acrylic (Opal/Clear)** | Small | 4' × 8' (48" × 96") | 32 | 4,608 | 3mm, 4mm, 5mm, 6mm, 8mm |
| **Acrylic (Opal/Clear)** | Large | 7' × 10' (84" × 120") | 70 | 10,080 | 3mm, 4mm, 5mm |
| **ACP** | Small | 4' × 8' (48" × 96") | 32 | 4,608 | 3mm, 4mm |
| **ACP** | Large | 5' × 10' (60" × 120") | 50 | 7,200 | 3mm, 4mm |
| **Aluminium (Raw/Black)** | Small | 4' × 8' (48" × 96") | 32 | 4,608 | 0.5mm, 1mm, 1.5mm, 2mm |
| **Aluminium (Raw/Black)** | Large | 5' × 10' (60" × 120") | 50 | 7,200 | 0.5mm, 1mm, 1.5mm |
| **PVC Foam Board** | Standard | 4' × 8' (48" × 96") | 32 | 4,608 | 3mm, 5mm, 8mm, 10mm |
| **SS (Stainless Steel)** | Standard | 4' × 8' (48" × 96") | 32 | 4,608 | 0.5mm, 0.8mm, 1mm, 1.2mm |
| **Fluted Pipes (Panel)** | Standard | 8" × 9 ft (8" × 108") | 6 | 864 | Standard profile. Narrow panels joined side-by-side to cover backdrop. |

### Sheet Selection Logic
```
Sign element < 48" in any dimension  →  Use 4'×8' sheets
Sign element > 48" in one dimension  →  Use 5'×10' or 7'×10' sheets
Always check: will the element FIT on the sheet with at least 1" margin on all sides?
```

---

## 2. LED Selection Rules

### The 1-Foot Rule (Critical)
```
Letter height ≤ 12 inches (1 foot)  →  LED STRIPS (side-lit / edge-lit)
Letter height > 12 inches (1 foot)  →  LED MODULES (front-lit / back-lit)
```

### LED Modules — Specifications

| Property | Small Module | Large Module |
|----------|-------------|-------------|
| Physical size | 10mm | 15mm |
| Fits letter depth | ≤ 1" (25mm) | ≥ 3" (75mm) |
| LEDs per module | 3 | 3 |
| Wattage per module | 1.2W | 1.2W |
| Voltage | 12V DC | 12V DC |
| Color options | Cool White (6500K), Warm White (3000K), RGB | Same |
| Typical spacing | 3-4" apart | 3-4" apart |

### LED Module Quantity Calculation (Per Element)

```
Step 1: Calculate face area
  Face area (sq in) = Height × Width × Fill Factor

  Fill factors by script type:
    English capital letters:     0.65
    English lowercase letters:   0.55
    Kannada characters:          0.55
    Hindi/Devanagari characters: 0.55
    Tamil characters:            0.50
    Telugu characters:            0.55
    Solid logos/icons:            0.80
    Outlined logos:               0.40
    Numbers:                     0.60

Step 2: Calculate module count
  Modules = Face area ÷ Spacing Factor

  Spacing factors by letter height:
    Small letters (12-18"):   4 sq inches per module
    Medium letters (18-30"):  5 sq inches per module
    Large letters (30-48"):   5 sq inches per module
    Very large letters (>48"): 6 sq inches per module

Step 3: Add 10% spare
  Final module count = ceil(Modules × 1.10)
```

### LED Strips — Specifications

| Property | Strip LED | Neon Flex |
|----------|----------|----------|
| Width | 6mm | 6mm |
| Density | 100 LEDs/meter | Continuous |
| Voltage | 12V DC | 12V DC |
| Roll length | Per meter | 5 meter rolls |
| Use case | Side-lit letters ≤1ft | Neon-style decorative |

### LED Strip Quantity Calculation (Per Element)
```
Strip length (meters) = Internal perimeter of letter (inches) ÷ 39.37
Add 10% for connections and cuts
```

### Halo/Reverse Strip Calculation (Per Element)
```
Strip length (meters) = External perimeter of element (inches) ÷ 39.37
Add 15% for routing around mounting hardware
```

---

## 3. Channel Letter Depth (Rising) Chart

| Letter Height | Recommended Depth | Rising (mm) | Channel Profile |
|--------------|-------------------|-------------|-----------------|
| Up to 12" | 1 inch | 25-30mm | Aluminium strip bent to shape |
| 12" to 18" | 1 inch | 40mm | Aluminium channel |
| 18" to 30" | 2 inches | 60mm | Aluminium channel |
| 30" to 48" | 2-3 inches | 60-80mm | Aluminium channel |
| Over 48" | 3+ inches | 80mm+ | Aluminium channel (heavy gauge) |

### Channel Perimeter Estimation (Per Letter)

When exact perimeters aren't available from a CAD file, use these multipliers:

| Character Type | Perimeter Multiplier | Formula |
|---------------|---------------------|---------|
| English uppercase (simple: I, L, T) | 2.5 | (H + W) × 2.5 |
| English uppercase (medium: A, E, F, H, K) | 3.0 | (H + W) × 3.0 |
| English uppercase (complex: B, G, M, N, R, S, W) | 3.5 | (H + W) × 3.5 |
| English uppercase (round: C, D, O, Q, U) | 3.2 | (H + W) × 3.2 |
| Kannada / Devanagari characters | 4.0 | (H + W) × 4.0 |
| Tamil characters | 4.5 | (H + W) × 4.5 |
| Numbers (0-9) | 3.0 | (H + W) × 3.0 |
| Geometric logo (simple) | 3.5 | (H + W) × 3.5 |
| Geometric logo (complex) | 4.5 | (H + W) × 4.5 |

Result is in inches — divide by 12 for running feet.

---

## 4. SMPS (Power Supply) Sizing

| SMPS Rating | Voltage | Max Current | Max Modules (at 1.2W each) | Max Strip (at 14W/m) |
|------------|---------|-------------|---------------------------|---------------------|
| 200W | 12V | 16.7A | ~166 modules | ~14 meters |
| 350W | 12V | 29.2A | ~291 modules | ~25 meters |

### SMPS Grouping Rules
```
1. Never load an SMPS beyond 80% of its rated capacity
2. Group adjacent letters onto the same SMPS when possible
3. Keep halo/reverse circuits on a separate SMPS from face LEDs
4. Each SMPS group should be labelledfor easy maintenance
5. Plan wire runs to minimize total cable length
```

---

## 5. Wire Specifications

| Wire Type | Cross-Section | Cores | Roll Length | Use |
|-----------|-------------|-------|------------|-----|
| 1.5mm single core | 1.5mm² | 1 | 90 meters/roll | Internal LED module connections inside letters |
| 2.5mm twin core | 2.5mm² | 2 | Per meter | Main power feed, SMPS connections, runs >5m |

### Wire Estimation Per Element
```
Internal wiring per letter: 1.5-2.5 meters of 1.5mm single core
  (depends on letter size — larger letters need more internal routing)
Inter-letter connections: 0.5-1 meter between adjacent letters
Main power feed: measure from electrical panel to sign location
```

---

## 6. Fasteners & Consumables Quick Reference

| Item | Use | Typical Quantity |
|------|-----|-----------------|
| Silicone sealant (tube) | Sealing acrylic face to channel | 1 tube per 3-4 letters |
| Acrylic solvent cement | Bonding acrylic face edges | 1 bottle per 6-8 letters |
| VHB tape (3M, roll) | ACP to frame bonding | 1 roll per 30 rft of frame |
| SS pop rivets | ACP to frame fastening | ~5 per running foot of frame |
| Self-tapping screws | Back plate attachment | 4-6 per letter |
| Cable glands | Waterproof wire entry | 1 per junction box entry point |
| Foam gasket tape (roll) | Seal between letter back and mounting surface | 1 roll per 8-10 letters |
| Heat shrink tubing | Wire connection insulation | ~2 per LED connection |
