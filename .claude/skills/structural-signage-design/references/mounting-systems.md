# Mounting Systems Reference

Detailed specifications for pylon foundations, building-mounted brackets, and installation systems.

## Table of Contents

1. [Pylon Foundation Systems](#1-pylon-foundation-systems)
2. [Building-Mounted Bracket Systems](#2-building-mounted-bracket-systems)
3. [Parapet & Roof Mounting](#3-parapet--roof-mounting)
4. [Projection / Blade Sign Arms](#4-projection--blade-sign-arms)
5. [Installation Sequence & Checklists](#5-installation-sequence--checklists)
6. [Crane & Access Requirements](#6-crane--access-requirements)
7. [Seismic Mounting Details](#7-seismic-mounting-details)

---

## 1. Pylon Foundation Systems

### 1A. Block / Pier Foundation (Most Common)

**When to use:** Pylons up to 15m, standard soil conditions (SBC ≥ 100 kN/m²)

**Components:**
```
┌─────────────────────────┐
│     Base Plate          │  ← MS plate, welded to column base
│  ┌──[AB]──[AB]──┐      │  ← Anchor bolts (AB) projecting from concrete
│  │              │      │
│  └──[AB]──[AB]──┘      │
└─────────────────────────┘
│         Grout pad       │  ← Non-shrink grout, 25-50mm
├─────────────────────────┤
│    ┌ Concrete Pier ┐   │  ← M25 concrete, rebar cage
│    │   (column up   │   │
│    │    through)     │   │
│    └───────────────┘   │
│         │              │
│    Rebar cage:         │
│    Vertical: Fe500D    │
│    Ties: Fe500, @200mm │
│    Cover: 50mm (earth) │
│         │              │
├─────────────────────────┤  ← Ground Level
│                         │
│    Foundation Block      │  ← Wider at base for bearing
│    M25 concrete         │
│    Bottom rebar mat     │
│    PCC blinding: 75mm   │
│                         │
└─────────────────────────┘
```

**Rebar Cage Detail for Pier:**
```
Pier diameter/width: Base plate width + 200mm minimum
Vertical bars: Min 4 nos, spaced equally around perimeter
  For pier up to 400mm: 4 × 12mm Fe500D
  For pier 400-600mm: 6 × 16mm Fe500D
  For pier 600-900mm: 8 × 16mm Fe500D
  For pier 900mm+: 8 × 20mm Fe500D

Lateral ties: 8mm Fe500 @ 200mm c/c
  Reduce to 150mm c/c within 300mm of top and bottom
  All ties with 135° hooks (not 90°)

Lap length: 50 × bar diameter
Development length: 40 × bar diameter (in tension, M25 concrete)
```

**Anchor bolt embedment in pier:**
```
Anchor bolt cage: typically J-bolt or L-bolt bent bars
  Material: Fe500 or ASTM F1554 Gr 36
  Embedment: minimum 20 × bolt diameter for cast-in bolts
  Projection above concrete: 100mm + grout thickness + base plate thickness + nut + washer + 25mm
  Template: fabricate a steel template (MS plate 6mm with bolt holes) to hold bolts in position during concrete pour
```

### 1B. Direct Burial / Caisson Foundation

**When to use:** Very tall pylons (>10m), poor soil, limited footprint area

```
┌── Column ──┐
│            │
│   Collar plate (welded to column)
│            │
├────────────┤  ← Ground Level
│            │
│  Concrete  │  ← Poured around column
│  caisson   │     M25 minimum
│  (circular │     Rebar cage around column
│   or square)│
│            │
│            │
│            │
└────────────┘  ← Caisson base: typically 1.5-3.0m deep

Caisson diameter: 600mm to 1500mm depending on load
Concrete: M25 minimum, vibrated
Rebar: Spiral or cage, 12mm @ 150mm pitch
```

### 1C. Spread Footing

**When to use:** Wide sign faces requiring large base moment resistance, good bearing soil

```
     ┌── Column ──┐
     │  Base plate │
     │  Pedestal   │  ← Short concrete pedestal from footing to grade
     ├─────────────┤  ← Ground Level
     │             │
     │   Pedestal  │
     │  concrete   │
┌────┴─────────────┴────┐
│    Spread Footing     │  ← Wide, shallow pad
│    Bottom rebar mat   │     M25 concrete
│    (both directions)  │     Cover: 50mm
│    PCC blinding 75mm  │
└───────────────────────┘

Footing proportions:
  Width B ≥ 2 × resultant eccentricity (to keep resultant in middle third)
  Depth D ≥ 300mm (minimum for reinforced concrete footing)
```

### 1D. Foundation Construction Sequence

1. **Excavation**: Dig to required depth + 75mm for PCC blinding
2. **PCC blinding**: Pour 75mm M15 plain concrete pad, level and cure
3. **Rebar placement**: Set bottom mat on chairs (50mm cover), place pier cage
4. **Anchor bolt template**: Fix template at correct position and height
5. **Concrete pour (Phase 1)**: Pour footing block up to pier start level, vibrate
6. **Concrete pour (Phase 2)**: Continue pier to ground level, hold anchor bolts vertical
7. **Cure**: Minimum 7 days wet curing (28 days for full strength)
8. **Backfill**: Compacted fill around foundation, grade for drainage away from base
9. **Grout bed**: Level the top of pier, place non-shrink grout pad
10. **Column erection**: Place column on base plate, align, tighten anchor bolts
11. **Grout pour**: Pour non-shrink grout under base plate, minimum 25mm thick

---

## 2. Building-Mounted Bracket Systems

### 2A. Facade-Flush Mounting (Sign flat on building face)

**Typical bracket arrangement:**
```
Building Wall (section view)
│
│←── Standoff spacer (MS tube or solid bar, 25-75mm)
│    ├── Top bracket (MS angle 65×65×6 or RHS 60×40×3)
│    │   ├── 2× M16 chemical anchors into RCC column
│    │   └── Sign cleat bolted to bracket
│    │
│    │   SIGN FACE (mounted on cleats)
│    │
│    ├── Bottom bracket (same as top)
│    │   ├── 2× M16 chemical anchors into RCC column
│    │   └── Sign cleat bolted to bracket
│
│←── Minimum 25mm gap for ventilation and drainage
```

**Key design considerations:**
- Every bracket must hit a structural member (RCC column or beam, steel frame)
- Minimum 2 bolts per bracket point
- Standoff spacers allow drainage behind sign
- Cable routing through wall: core-drill holes, seal with fire-rated sealant

**Bracket spacing:**
```
Maximum bracket spacing (for wind suction):
  Sign face pressure: pd × Cf (from wind calc)
  Bracket capacity: determined by anchor pull-out strength
  Spacing = Bracket capacity / (pd × Cf × tributary width)

Typical: 900mm to 1500mm horizontal, 600mm to 1200mm vertical
  depending on sign size and wind zone
```

### 2B. Through-Wall Bracket (Preferred for large signs)

```
Interior                     Exterior
│                           │
│←── Backing plate          │←── Sign mounting bracket
│    (MS plate 150×150×8)   │    (MS RHS 100×50×4)
│         ↕                 │         ↕
│    Through-bolts M16 × [wall thickness + 50mm]
│    Grade 8.8              │
│    Plate washer both sides│
│                           │
│    Wall (RCC or masonry)  │
```

**Through-bolt torque values:**

| Bolt Size | Grade 8.8 Torque (Nm) |
|-----------|----------------------|
| M12 | 80 |
| M16 | 190 |
| M20 | 370 |
| M24 | 640 |

### 2C. Steel Frame Attachment

When the building has exposed or accessible steel frame:

```
Steel Beam (IPE/UB section)
  │
  ├── Clamp bracket (MS angle 75×75×6 with bolt through beam flange)
  │   OR
  ├── Welded bracket (direct weld to beam — only with building owner approval)
  │   OR
  ├── Beam clamp (proprietary Lindapter or Halfen type)
  │
  └── Sign mounting arm extends from bracket
```

**Rules for connecting to existing steel:**
- NEVER weld to existing structural steel without PE approval
- Drilling through existing beams: only in web, never in flanges, minimum edge distance = 2×hole diameter
- Beam clamps (Lindapter type) are preferred — reversible, no permanent modification

---

## 3. Parapet & Roof Mounting

### 3A. Parapet-Top Mounting

```
       SIGN
        │
   ┌────┴────┐
   │ Cabinet │
   └────┬────┘
        │
   ┌────┴────┐  ← Clamping bracket (MS channel or RHS)
   │  ╔══════╗│
   │  ║Parapet║│← Parapet wall (RCC or masonry)
   │  ║  wall ║│
   │  ╚══════╝│
   └──────────┘
     Internal backing plate

Bracket type: U-bracket clamping over parapet
  Material: MS RHS 100×50×5 or ISMC 100
  Through-bolts: M16 Grade 8.8, min 4 per bracket
  Backing plate: MS plate 200×200×10, inside face
  Rubber/neoprene pad between bracket and parapet to prevent damage
```

**Critical checks:**
- Parapet must be structurally adequate — verify with building drawings
- Masonry parapets often lack reinforcement; may need strengthening
- Overturning moment at parapet base: sign wind load × height above parapet
- If parapet is too weak: extend brackets down to roof slab or beam below

### 3B. Roof-Mounted Framework

```
          SIGN
           │
      ┌────┴────┐
      │ Cabinet │
      └────┬────┘
           │
      ┌────┴────┐
      │  Steel   │  ← Sign support frame (MS SHS/RHS)
      │  frame   │
      └──┬───┬──┘
         │   │
    ┌────┴───┴────┐  ← Base frame (MS angle/channel)
    │             │
    └──┬──┬──┬──┬─┘
       │  │  │  │   ← Anchor bolts to roof structure
       ▼  ▼  ▼  ▼
    ═══════════════  ← Roof slab / beam
```

**Waterproofing penetrations:**
- Drill through existing waterproofing membrane
- Install EPDM rubber boot around each penetration
- Apply liquid waterproofing (polyurethane) around boot
- Flash with aluminium cap flashing
- Slope all surfaces away from penetrations

---

## 4. Projection / Blade Sign Arms

### 4A. Single Cantilever Arm

```
Building Face
│
│←── Wall bracket plate (MS plate 300×200×12)
│    ├── 4× M16 chemical anchors into RCC column
│    │   Embedment: 190mm minimum
│    │
│    ├── Cantilever arm (MS RHS 150×75×5)
│    │   Length: sign projection + 50mm clearance
│    │   Welded to wall plate with full-penetration butt weld
│    │
│    └── Diagonal brace (optional, for long projections)
│        MS RHS 60×40×3 from wall plate to arm tip
│
│         └──── Sign cabinet attached to arm end
```

**Maximum cantilever projections without bracing:**

| Arm Section | Max Projection (for sign ≤50kg) | Max Projection (for sign ≤100kg) |
|------------|-------------------------------|--------------------------------|
| RHS 100×50×4 | 800mm | 500mm |
| RHS 120×60×5 | 1200mm | 750mm |
| RHS 150×75×5 | 1500mm | 1000mm |
| RHS 200×100×6 | 2000mm | 1500mm |

Add diagonal brace for projections exceeding these limits.

### 4B. Double Arm (Blade Sign)

```
Building Face
│
│←── Wall bracket plate (MS plate 400×250×12)
│    ├── 6× M16 chemical anchors
│    │
│    ├── Top arm (MS RHS 100×50×4)
│    │   └── Top fixing to sign cabinet
│    │
│    ├── Bottom arm (MS RHS 100×50×4)
│    │   └── Bottom fixing to sign cabinet
│    │
│    └── Vertical connector between arms at sign plane
│
│         SIGN (hangs between two arms)
```

---

## 5. Installation Sequence & Checklists

### 5A. Pylon Installation Sequence

```
Phase 1: Foundation (Days 1-3)
  □ Survey and mark exact location
  □ Excavate to design depth
  □ Place PCC blinding, level
  □ Set rebar cage + anchor bolt template
  □ Pour concrete, vibrate, finish top level
  □ Begin curing (7 days minimum before loading)

Phase 2: Structure Erection (Day 10+, after concrete reaches 70% strength)
  □ Inspect foundation: level, bolt positions, concrete quality
  □ Position crane at safe distance
  □ Lift column section(s) — single lift if <12m, multi-lift with splices if taller
  □ Place column on base plate, align with plumb bob/theodolite
  □ Hand-tighten anchor bolts
  □ Check plumb in two directions (tolerance: ±3mm per 3m height)
  □ Snug-tighten bolts in star pattern
  □ Final torque bolts to specification
  □ Pour non-shrink grout under base plate

Phase 3: Sign Cabinet (Day 11+)
  □ Lift sign cabinet — may need separate lift or assembled in-situ
  □ Bolt cabinet to column bracket
  □ Level cabinet (tolerance: ±2mm across face)
  □ Install access doors, gaskets

Phase 4: Electrical & LED (Day 12+)
  □ Run power cable from supply to SMPS location
  □ Install SMPS / LED drivers in ventilated compartment
  □ Install LED panels/modules per manufacturer sequence
  □ Connect module cables, test each panel before closing
  □ Seal all cable entries with glands, test IP integrity

Phase 5: Commissioning (Day 13+)
  □ Power on, full brightness test
  □ Check for dead pixels / modules
  □ Verify ventilation fans operational (if fitted)
  □ Install external cladding, trim, cap strips
  □ Clean all surfaces
  □ Record completion photos from 4 sides
  □ Hand over to client
```

### 5B. Building-Mounted Installation Sequence

```
Phase 1: Site Survey (Day 1)
  □ Verify building structural drawings match reality
  □ Mark bracket positions on facade
  □ Verify all bracket points hit structural members (use rebar scanner/GPR)
  □ Check electrical supply location
  □ Plan access (scaffolding / cherry picker / rope access)

Phase 2: Bracket Installation (Day 2-3)
  □ Drill anchor holes (hammer drill for concrete, core drill for large holes)
  □ Clean holes (compressed air + wire brush, 3× per hole)
  □ Install chemical anchors per manufacturer instructions
  □ Wait for cure time before loading
  □ Install brackets, torque bolts
  □ Check alignment: all brackets in same plane (laser level)

Phase 3: Sign Mounting (Day 4)
  □ Lift sign sections to working height
  □ Fix to brackets progressively (don't remove lifting gear until 4+ bolts are in)
  □ Level and plumb the sign
  □ Complete all fixings, torque to spec

Phase 4: Electrical & Finishing (Day 5)
  □ Run cables through wall penetrations
  □ Seal penetrations with fire-rated sealant
  □ Connect power, test illumination
  □ Install trim, flashings, weather seals
  □ Clean facade around installation
  □ Completion photos and handover
```

---

## 6. Crane & Access Requirements

### Crane Selection Guide

| Pylon Height | Sign Weight (approx) | Minimum Crane | Typical Crane |
|-------------|---------------------|--------------|--------------|
| Up to 5m | <200 kg | Truck-mounted Hiab (3T) | 8T mobile crane |
| 5-8m | 200-500 kg | 8T mobile crane | 12-15T mobile crane |
| 8-12m | 500-1000 kg | 15T mobile crane | 25T mobile crane |
| 12-18m | 1000-2000 kg | 25T mobile crane | 35-50T mobile crane |
| 18m+ | 2000+ kg | 35T+ mobile crane | 50-80T mobile crane |

**Crane positioning:**
- Minimum working radius = pylon height × 0.8 (for safety angle)
- Ground must be level and firm — use outrigger pads on soft ground
- Confirm overhead clearance (power lines, buildings)
- Night work may require lighting and permits

### Access Equipment for Building-Mounted

| Building Height | Access Method | Notes |
|----------------|--------------|-------|
| Up to 6m | Scaffold tower or ladder (light work) | Tower scaffold preferred for stability |
| 6-12m | Mobile scaffold or cherry picker | Cherry picker if ground access allows |
| 12-25m | Boom lift (cherry picker/JLG type) | Need clear working zone at ground |
| 25m+ | Rope access (IRATA trained) or suspended scaffold | Specialist contractor required |
| Restricted ground | Mast climber platform | Fixed to building, independent of ground |

---

## 7. Seismic Mounting Details

### For Seismic Zones IV and V

**Additional requirements beyond wind design:**

1. **Anchor bolts must resist combined wind + seismic forces**
   - Check both load cases independently
   - Use the critical (higher) force for anchor design

2. **Ductile connections preferred**
   - Use Grade 8.8 bolts (not Grade 10.9) — more ductile failure mode
   - Avoid welded connections where possible — bolted joints can dissipate energy
   - If welding is necessary, use full-penetration butt welds at critical connections

3. **Base plate flexibility**
   - Base plate thickness should be such that the plate yields before the anchor bolts fail
   - This provides a ductile "fuse" in the connection

4. **Non-structural element provisions (IS 1893 Part 1, Clause 7.13)**
   - Signs and their supports are classified as "non-structural elements"
   - Design force: Fp = (Z/2) × (I) × (ap/Rp) × Wp × (1 + 2z/h)
     where:
     - ap = component amplification factor (2.5 for cantilever elements)
     - Rp = component response modification (2.5 for sign structures)
     - Wp = weight of component
     - z = height of attachment
     - h = building height
   - Minimum Fp = 0.10 × Wp
   - Maximum Fp = 0.40 × Wp (in Zone V)

5. **Vibration isolation for LED panels**
   - LED panels mounted on rubber grommets or neoprene pads to absorb vibration
   - Cable connectors must have strain relief and flex allowance
