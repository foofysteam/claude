---
name: structural-signage-design
description: >
  Generate structural shop designs for signage pylons and building-mounted LED panels — material selection,
  wind load calculations (IS 875), fabrication-ready specs, foundation details, anchor bolt patterns, and
  steel member sizing. Replaces external shop design services. Trigger on: structural design, shop drawing,
  pylon design, pylon structure, building-mounted signage, foundation design for signs, wind load for signs,
  anchor bolt layout, base plate design, MS frame design, LED panel mounting, facade brackets, parapet sign
  structure, sign engineering, structural calculations. Also trigger when user uploads a signage design and
  asks about structural requirements or mounting methods. Covers pylons and building-mounted signs.
---

# Structural Signage Design

Generate complete structural engineering packages for signage pylons and building-mounted LED panel installations.
The output replaces external shop design services by providing all three layers of detail that a fabrication
team and structural engineer need.

## Three-Layer Output System

This skill produces output in three progressive layers. The user can request any combination, but the default
is to deliver all three as a complete structural design package.

| Layer | Name | What It Covers | Who Uses It |
|-------|------|---------------|-------------|
| **Layer 1** | Design & Material Guide | Material selection, dimensional guidelines, LED panel specs, general structural approach, mounting method options | Sales team, client presentations, initial project scoping |
| **Layer 2** | Fabrication-Ready Specs | Detailed material specs, cut lists, weld details, mounting hardware, LED panel layouts, connection types, weight calculations | Production team, procurement, fabrication shop floor |
| **Layer 3** | Full Shop Drawing Package | Wind load calculations (IS 875 Part 3), foundation design, steel member sizing, base plate & anchor bolt engineering, connection detail drawings, structural adequacy checks | Structural engineer sign-off, municipal approvals, installation team |

## Reference Files — Read Before Generating Any Structural Design

1. `references/structural-calculations.md` — Wind load formulas (IS 875 Part 3:2015), moment/shear calculations, deflection limits, foundation sizing, anchor bolt engineering, base plate design
2. `references/material-specifications.md` — Steel section properties (SHS/RHS/CHS/angles/channels), aluminium profiles, fastener grades, welding specs, corrosion protection, concrete grades
3. `references/mounting-systems.md` — Pylon foundation types, building-mounted bracket systems, facade attachment details, parapet mounting, projection sign arms, seismic considerations

---

## Workflow

```
Input (Design Image / Specs / Site Photos)
    │
    ├── Step 1: Classify the signage type & extract dimensions
    ├── Step 2: Define the structural system (pylon or building-mounted)
    ├── Step 3: Layer 1 — Material & Design Guide
    ├── Step 4: Layer 2 — Fabrication-Ready Specifications
    ├── Step 5: Layer 3 — Structural Engineering Calculations
    └── Step 6: Generate Output Package
```

---

## Step 1: Classify & Extract

### What to identify from the input

For EVERY structural design request, establish these fundamentals first:

**Sign Classification:**
- **Pylon / Freestanding**: Ground-mounted on its own structural column(s) — includes single-pole, dual-pole, box pylons, monument-style with columns
- **Building-Mounted**: Attached to an existing structure — includes facade-flush, projecting/blade, parapet-top, canopy-mounted, roof-mounted

**Dimensional Extraction:**
```
Overall sign face: Width × Height (meters and feet)
Sign depth / projection from mounting surface (mm)
Height above ground level (AGL) to sign centre
Height AGL to top of sign
If pylon: total pylon height including base to top of sign cabinet
If building-mounted: building height, floor level of mounting, facade material
```

**Site Conditions:**
```
City / Location → determines wind zone (IS 875 Part 3, Table 1)
Terrain category (1=open coast, 2=open with scattered obstructions, 3=suburban, 4=dense urban)
Topography factor (flat, hill, ridge, escarpment)
Exposure: single-faced or double-faced sign
Seismic zone (IS 1893 — Zones II through V)
```

**Present findings to user for confirmation before proceeding.**

---

## Step 2: Define the Structural System

### For Pylons / Freestanding Signs

The structural system depends on sign size, height, and wind exposure:

| Pylon Height | Typical Column System | Foundation Type |
|-------------|----------------------|-----------------|
| Up to 3m | Single MS pipe (CHS 100-150mm NB) or single SHS/RHS column | Direct burial or block footing |
| 3m to 6m | Single or dual CHS/SHS columns, cross-braced if wide | Block/pier footing with anchor bolts |
| 6m to 10m | Dual CHS columns (150-200mm NB) with lattice bracing, or tapered box column | Pier foundation with rebar cage |
| 10m to 15m | Heavy box column (fabricated plate) or lattice tower | Engineered spread or pier footing |
| 15m+ | Engineered lattice tower or tapered monopole | Deep pier or pile foundation — must have PE sign-off |

**Column Section Selection Logic:**
- CHS (Circular Hollow Section): Best for wind — uniform drag coefficient (Cd ≈ 0.6-1.2), aesthetic, but harder to attach sign cabinets
- SHS (Square Hollow Section): Good all-around — flat faces simplify cabinet mounting, Cd ≈ 1.3-2.0
- RHS (Rectangular Hollow Section): Best when bending is predominantly in one axis — orient the strong axis into the wind
- Built-up box section (welded plate): For very large pylons where rolled sections aren't sufficient
- Lattice/truss: For heights above 10m or very large sign faces where solid columns would be over-designed

### For Building-Mounted Signs

The structural system depends on the mounting method and building substrate:

| Mounting Type | Bracket System | Critical Check |
|--------------|---------------|----------------|
| Facade-flush (flat on wall) | Through-bolt brackets to structural members behind facade, MS angle cleats | Pull-out capacity of anchors, facade material capacity |
| Projecting / Blade sign | Cantilever arm (MS channel or RHS) through-bolted to structural column or beam | Cantilever moment at wall, anchor tension, torsion from wind |
| Parapet-top | Clamping brackets over parapet or through-bolt behind parapet | Parapet structural capacity, overturning moment |
| Roof-mounted | Base frame bolted to roof structure, bracing to purlins | Roof structural capacity, waterproofing penetrations |
| Canopy / Soffit | Hanging rods or brackets from canopy structure | Canopy capacity, vibration from wind |

**Building Substrate Identification:**
- RCC columns/beams → mechanical anchors (expansion or chemical) rated for the load
- Steel frame → bolted or welded connections to steel members
- Masonry/block wall → NOT structural; must find structural members behind
- ACP/glass curtain wall → NEVER attach structural loads to facade cladding; penetrate through to structure
- Concrete slab edge → chemical anchors with edge distance checks

---

## Step 3: Layer 1 — Design & Material Guide

This layer provides the material selection rationale and general structural approach. It helps the sales team scope a project and gives the client confidence that the engineering is sound.

### Output Format for Layer 1

```
PROJECT: [Name]
SIGN TYPE: [Pylon / Building-Mounted]
LOCATION: [City, State]

1. SIGN DESCRIPTION
   - Overall dimensions: W × H × D
   - Face type: LED panel / channel letters / flex / ACP with print
   - Lighting: [LED module type, wattage, colour temperature]
   - Viewing distance: [determines minimum letter height]

2. STRUCTURAL APPROACH
   - Support system: [describe column/bracket type]
   - Material: [MS / SS / Aluminium — with rationale]
   - Foundation: [type and general dimensions]
   - Key design loads: wind, dead weight, seismic (if applicable)

3. MATERIAL SELECTION GUIDE
   For each major component:
   - Primary structure: [MS section type and grade]
   - Sign cabinet frame: [section type]
   - Sign face frame: [material]
   - Cladding: [ACP / ACM / SS / aluminium sheet]
   - Fasteners: [bolt grade, type]
   - Corrosion protection: [hot-dip galvanising / powder coat / paint system]
   - Foundation: [concrete grade, rebar grade]

4. WEIGHT ESTIMATE
   - Sign cabinet (empty): [kg]
   - LED panels + electrical: [kg]
   - Structure (columns/brackets): [kg]
   - Total dead load: [kg]

5. INSTALLATION METHOD OVERVIEW
   - Access requirements (crane tonnage, boom reach)
   - Sequence: foundation → structure → cabinet → electrical → sign face
   - Timeline estimate
```

---

## Step 4: Layer 2 — Fabrication-Ready Specifications

This layer gives the production team everything needed to cut, weld, and assemble. Read `references/material-specifications.md` before generating this layer.

### Output Format for Layer 2

#### 4A. Structural Steel Cut List

For EVERY structural member, specify:

| Member ID | Description | Section | Grade | Length (mm) | Qty | Weight (kg) | End Prep | Notes |
|-----------|-------------|---------|-------|------------|-----|-------------|----------|-------|
| C1 | Main column | CHS 150×4.5 | IS 2062 E250 | 6000 | 2 | 58.4 | Base plate weld prep | Hot-dip galvanise after fabrication |
| B1 | Cross brace | SHS 50×50×3 | IS 2062 E250 | 1200 | 4 | 4.8 | Mitre cut 45° both ends | |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Include subtotal weight at bottom.**

#### 4B. Connection Details

For every joint in the structure:

```
CONNECTION C1-B1: Column to Cross Brace
Type: Fillet weld
Weld size: 6mm
Weld length: Full perimeter (4 × 50mm = 200mm)
Electrode: E7018 (IS 814)
Position: 2G (horizontal)
Inspection: Visual + spot UT for primary connections
```

#### 4C. Sign Cabinet Frame

```
Frame members: [section sizes]
Panel mounting: [track/channel system or bolt-through]
LED panel access: [hinged door / removable panel — specify which face]
Ventilation: [louvre type, size, position]
Cable entry: [bottom/top, gland size]
Drainage: [weep holes at bottom, size and spacing]
Waterproofing: [IP rating target, gasket specs]
```

#### 4D. Mounting Hardware Schedule

| Item | Specification | Grade | Size | Qty | Torque (Nm) |
|------|-------------|-------|------|-----|------------|
| Anchor bolt | Chemical anchor, M16 | Grade 8.8 | M16 × 200mm embedment | 4 | 190 |
| Base plate bolt | Hex bolt | Grade 8.8 | M16 × 50mm | 8 | 190 |
| ... | ... | ... | ... | ... | ... |

#### 4E. Surface Treatment Specification

```
PRIMARY STRUCTURE:
1. Blast clean to SA 2.5 (IS 1477)
2. Zinc primer: 75 microns DFT
3. Epoxy MIO intermediate: 125 microns DFT
4. Polyurethane topcoat: 50 microns DFT
   Total system: 250 microns minimum DFT
   OR: Hot-dip galvanise to IS 2629 (minimum 85 microns for sections <5mm thick)

SIGN CABINET:
1. Degrease and etch
2. Epoxy primer: 50 microns
3. Powder coat (polyester): 60-80 microns
   Colour: [RAL code per brand guidelines]
```

#### 4F. LED Panel Integration

```
Panel type: [manufacturer/model or generic P-value spec]
Panel size: [mm × mm]
Panel weight: [kg each]
Quantity: [number of panels]
Total LED area: [m²]
Resolution: [pixel pitch in mm]
Power per panel: [W]
Total power: [W]
Mounting: [direct-fix to cabinet frame / rear-access module system]
Structural load from panels: [total kg, distributed or point loads]
Cable management: [routing path, tray/conduit spec]
```

---

## Step 5: Layer 3 — Full Structural Engineering Calculations

This is the engineering heart. Read `references/structural-calculations.md` before generating this layer.
These calculations must be thorough enough for a licensed structural engineer to review and stamp.

### 5A. Design Wind Load (IS 875 Part 3:2015)

```
WIND LOAD CALCULATION

1. Basic Wind Speed (Vb):
   Location: [City]
   Vb = [value] m/s (IS 875 Part 3, Clause 5.2, Table 1 / Fig 1)

2. Design Wind Speed (Vz) at height z:
   Vz = Vb × k₁ × k₂ × k₃ × k₄

   k₁ (Risk coefficient, Table 1):
     Structure class: [Normal / Important / Post-disaster]
     Design life: [50 years standard]
     k₁ = [value]

   k₂ (Terrain roughness & height, Table 2):
     Terrain category: [1/2/3/4]
     Height z = [value] m (to centroid of sign face)
     k₂ = [value]

   k₃ (Topography factor, Clause 5.3.3):
     Topography: [flat / hill / escarpment]
     k₃ = [value, typically 1.0 for flat terrain]

   k₄ (Importance factor for cyclonic region):
     k₄ = [value, typically 1.0 outside cyclonic regions]

   Vz = [value] × [k₁] × [k₂] × [k₃] × [k₄] = [result] m/s

3. Design Wind Pressure (pd):
   pd = 0.6 × Vz² (N/m²)
   pd = 0.6 × [Vz]² = [result] N/m² = [result] kN/m²

4. Force Coefficient (Cf):
   Sign aspect ratio: b/d = [width/height]
   Cf = [value] (IS 875 Part 3, Table 21 for flat plates / signs)
   For single-face sign on ground: Cf typically 1.2 to 1.8
   For double-face sign: Cf applies to one face (shielding on leeward)

5. Wind Force on Sign Face:
   F_wind = Cf × pd × A_sign
   A_sign = [width] × [height] = [area] m²
   F_wind = [Cf] × [pd] × [A] = [result] kN

6. Wind Force on Column(s):
   Cd_column = [value based on section shape]
   A_column = [diameter/width] × [exposed height] m²
   F_column = Cd × pd × A_column = [result] kN

7. Total Horizontal Wind Force:
   F_total = F_wind + F_column = [result] kN
```

### 5B. Structural Member Design

```
COLUMN DESIGN CHECK

Applied loads at base:
  Axial (dead load): P = [weight of sign + structure above] = [value] kN
  Moment (wind): M = F_wind × lever arm to base = [value] kN·m
  Shear: V = F_total = [value] kN

Selected section: [e.g., CHS 168.3 × 6.3, IS 2062 E250]
  Section properties:
    A = [area] mm²
    I = [moment of inertia] × 10⁶ mm⁴
    Z = [section modulus] × 10³ mm³
    r = [radius of gyration] mm

  Yield stress: fy = 250 MPa (E250 grade)
  Allowable bending stress: 0.66 × fy = 165 MPa (IS 800:2007 working stress)
  Allowable axial stress: depends on slenderness ratio λ = L_eff / r

  Slenderness check:
    Effective length L_eff = [K × L] mm (K depends on end conditions)
    λ = L_eff / r = [value]
    Allowable compressive stress σ_ac = [from IS 800 Table 5.1] MPa

  Combined stress check (IS 800:2007, Clause 7.1.1):
    (σ_ac,cal / σ_ac) + (σ_bc,cal / σ_bc) ≤ 1.0
    ([P/A] / [σ_ac]) + ([M/Z] / [165]) = [value] ≤ 1.0

  Deflection check:
    Max tip deflection: δ = F × L³ / (3 × E × I)
    Allowable: L / 200 for signage structures
    δ = [value] mm, Allowable = [value] mm → [OK / REVISE]
```

### 5C. Foundation Design

```
FOUNDATION DESIGN

Foundation type: [Block/Pier/Spread]
Soil bearing capacity (assumed or from site investigation): [value] kN/m²
  (If no soil report: use conservative 100 kN/m² for medium clay,
   150 kN/m² for medium sand, 200+ kN/m² for rock)

Applied loads at foundation top:
  Vertical (dead load): P = [value] kN
  Horizontal (wind): H = [value] kN
  Moment (overturning): M = [value] kN·m

Foundation sizing:
  For stability against overturning:
    Factor of Safety against overturning ≥ 1.5 (IS 1904)
    Restoring moment = (Weight of foundation + soil above) × (base width / 2)
    Overturning moment = M + H × foundation depth

  For block/pier foundation:
    Width B = [value] m
    Length L = [value] m
    Depth D = [value] m
    Concrete volume = B × L × D = [value] m³
    Concrete weight = volume × 24 kN/m³ = [value] kN
    Soil overburden = [calculated if applicable]

  Bearing pressure check:
    Max bearing pressure = P_total / (B × L) + M / (B × L² / 6)
    = [value] kN/m² ≤ [allowable SBC] → [OK / REVISE]

  Minimum bearing pressure check (no tension):
    Min pressure = P_total / (B × L) - M / (B × L² / 6)
    = [value] kN/m² → must be ≥ 0 (no uplift)

Concrete specification:
  Grade: M25 minimum (IS 456:2000)
  Cover: 50mm (exposed to earth)
  Rebar: Fe 500D (IS 1786)

Reinforcement:
  Main bars: [size × qty] each way, bottom mat
  Distribution bars: [size × spacing]
  Starter bars for column: [size × qty] projecting [length] above foundation top
```

### 5D. Base Plate & Anchor Bolt Design

```
BASE PLATE DESIGN

Column section: [section description]
Base plate size: [length × width × thickness] mm

Anchor bolt layout:
  Bolt circle diameter / pattern: [description]
  Number of bolts: [qty]
  Bolt specification: [ASTM F1554 Gr 36 / IS grade equivalent]
  Bolt diameter: M[size]
  Embedment depth: [value] mm (minimum 12× bolt diameter for chemical anchors)
  Projection above concrete: [value] mm

Bolt force calculation:
  Maximum tension per bolt from overturning:
    T_max = (M / (n × bolt arm)) - (P / n)
    = [value] kN per bolt

  Bolt capacity check:
    Tensile capacity of M[size] Grade [X] bolt = [value] kN
    Factor of safety = Capacity / Applied = [value] ≥ 2.0

  Shear per bolt:
    V_bolt = H / n = [value] kN
    Shear capacity = [value] kN → [OK]

  Combined tension + shear interaction:
    (T/T_capacity)² + (V/V_capacity)² ≤ 1.0
    = [value] ≤ 1.0 → [OK]

Grout specification:
  Non-shrink cementitious grout, 28-day strength ≥ 40 MPa
  Thickness: 25-50mm
  Level: Ensure plate is level to ±1mm before grouting

Base plate bending check:
  Plate thickness t = √(6 × M_plate / (fy × 1))
  Required: [value] mm
  Provided: [value] mm → [OK]
```

### 5E. Building-Mounted Structural Checks (if applicable)

```
FACADE ATTACHMENT DESIGN

Mounting substrate: [RCC column / Steel beam / Masonry + backing]
Sign dead weight: [value] kN (distributed across [n] brackets)
Wind load on sign: [value] kN (from Step 5A)

Bracket design:
  Type: [MS angle / MS channel / RHS cantilever arm]
  Section: [size]
  Bracket arm length: [projection from wall face] mm
  Number of brackets: [qty]
  Spacing: [mm c/c]

Load per bracket:
  Vertical (dead load): P_bracket = Total DL / n = [value] kN
  Horizontal (wind): H_bracket = Total wind / n = [value] kN
  Moment at wall face: M_bracket = H × arm + P × eccentricity = [value] kN·m

Anchor design:
  Type: [Expansion anchor / Chemical anchor / Through-bolt]
  Bolt size: M[size]
  Anchor brand/model: [specify or generic spec]
  Number per bracket: [qty]
  Embedment: [value] mm
  Edge distance: ≥ [value] mm (minimum 2.5× bolt diameter from edge of concrete)
  Spacing: ≥ [value] mm (minimum 6× bolt diameter between anchors)

  Pull-out capacity per anchor: [value] kN (from manufacturer datasheet at specified embedment in [concrete grade])
  Required pull-out: [value] kN
  FoS = [value] ≥ 2.5 for life-safety attachments

  Concrete breakout check:
    Effective breakout area per anchor: [calculation]
    Breakout capacity: [value] kN
    Group effect if anchors are close: [reduction factor]

Facade panel capacity check (if sign is on cladding zone):
  Confirm brackets penetrate through to primary structure
  ACP/curtain wall/cladding CANNOT carry structural sign loads
  State clearly: "Brackets must be fixed to [RCC column at gridline X / Steel beam at level Y]"
```

---

## Step 6: Generate Output Package

### Default Output: Complete Structural Design Package

Generate all outputs as a comprehensive document. Output destination follows this priority:

1. **If user shares a Notion page**: Add as structured content to that page
2. **Otherwise**: Generate a multi-sheet Excel workbook + a separate PDF calculation report

### Excel Output Structure

Read the xlsx skill before generating.

| Sheet | Content |
|-------|---------|
| Cover | Project name, date, revision, engineer, design codes |
| Layer 1 — Design Summary | Material guide, structural approach, weight estimate |
| Layer 2 — Cut List | Every structural member with section, grade, length, qty, weight |
| Layer 2 — Connections | Weld & bolt details for every joint |
| Layer 2 — Hardware | All fasteners, anchors, plates with specs |
| Layer 2 — Surface Treatment | Paint/galvanising system |
| Layer 3 — Wind Calc | Full IS 875 wind load calculation |
| Layer 3 — Member Design | Section adequacy checks |
| Layer 3 — Foundation | Foundation sizing and reinforcement |
| Layer 3 — Base Plate | Anchor bolt and base plate design |
| Layer 3 — Building Mount | Bracket and anchor design (if applicable) |
| BOM | Consolidated Bill of Materials with weights |

### File Naming

`[ProjectName]_Structural_Design_[Date].xlsx`

---

## Design Code References

These Indian Standards govern the structural design. Always cite the applicable clause:

| Code | Title | Used For |
|------|-------|----------|
| IS 875 Part 1:1987 | Dead Loads | Self-weight of materials |
| IS 875 Part 3:2015 | Wind Loads | Wind speed, pressure, force coefficients |
| IS 800:2007 | General Construction in Steel | Steel member design, connections |
| IS 456:2000 | Plain & Reinforced Concrete | Foundation design, concrete specs |
| IS 1893 Part 1:2016 | Earthquake Resistant Design | Seismic zones III-V |
| IS 2062:2011 | Hot Rolled Steel | Material grades (E250, E350) |
| IS 1161:2014 | Steel Tubes for Structural Purposes | CHS/SHS/RHS properties |
| IS 814:2004 | Welding Electrodes | Electrode classification |
| IS 1904:1986 | Foundation Design | Bearing pressure, stability |
| IS 2629:1985 | Hot-Dip Galvanising | Corrosion protection |
| SP 6(1):1964 | Handbook for Structural Engineers | Section properties |

---

## Important Guidelines

1. **Safety factors are non-negotiable.** Wind load FoS ≥ 1.5, anchor bolt FoS ≥ 2.0 for overhead/life-safety, foundation overturning FoS ≥ 1.5. Signage falls on people — conservative design is the only design.

2. **Always specify the wind zone.** Every Indian city has a basic wind speed (Vb) from IS 875 Table 1. Common values: Delhi 47 m/s, Mumbai 44 m/s, Chennai 50 m/s, Kolkata 50 m/s, Hyderabad 44 m/s, Bangalore 33 m/s. If the city isn't in the table, interpolate from the wind map or use the nearest listed city's value.

3. **Terrain category matters enormously.** Category 1 (open coast) can produce 2-3× the wind pressure of Category 4 (dense urban). Always ask about the site surroundings.

4. **Never attach structural loads to facade cladding.** ACP panels, glass curtain walls, composite panels — these are weather barriers, not structures. Always penetrate through to the primary frame (RCC or steel). Call this out explicitly in every building-mounted design.

5. **Galvanising vs paint** — for outdoor signage exposed to weather, hot-dip galvanising is strongly preferred for the primary structure. Paint systems degrade and need maintenance; galvanising provides 20+ years of protection with minimal maintenance. The sign cabinet and visible elements can be powder-coated over galvanised steel for aesthetics.

6. **Foundation depth** — minimum 1.0m below ground level for stability, deeper in soft soils. In frost-prone areas, foundation must extend below frost line. In expansive clay soils, underream or pile foundations may be needed.

7. **Drainage is critical.** Every sign cabinet and enclosed structure must have weep holes at the lowest point. Water accumulation adds dead load and accelerates corrosion. Specify drain holes at 100mm c/c along the bottom edge.

8. **Confirm with user before proceeding past classification.** The dimensional and site data drives everything — getting it wrong wastes the entire calculation. Always present Step 1 findings and wait for confirmation.

9. **Layer 3 should be review-ready for a PE.** The calculations should be complete enough that a Professional Engineer can verify and stamp them without having to redo the work. Show all intermediate steps, cite code clauses, and state assumptions clearly.

10. **For heights above 15m or sign faces above 20m², strongly recommend independent structural engineering review.** The skill produces calculations that are structurally sound, but projects of this scale carry significant liability and should have a PE stamp.
