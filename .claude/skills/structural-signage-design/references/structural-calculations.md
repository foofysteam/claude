# Structural Calculations Reference

Complete calculation procedures for signage structural design per Indian Standards.

## Table of Contents

1. [Wind Load Calculation (IS 875 Part 3:2015)](#1-wind-load-calculation)
2. [Steel Member Design (IS 800:2007)](#2-steel-member-design)
3. [Foundation Design (IS 456 / IS 1904)](#3-foundation-design)
4. [Base Plate & Anchor Bolt Design](#4-base-plate--anchor-bolt-design)
5. [Connection Design — Welds](#5-connection-design--welds)
6. [Connection Design — Bolts](#6-connection-design--bolts)
7. [Deflection & Serviceability](#7-deflection--serviceability)
8. [Seismic Considerations (IS 1893)](#8-seismic-considerations)

---

## 1. Wind Load Calculation

### IS 875 Part 3:2015 — Step-by-Step

#### Step 1: Basic Wind Speed (Vb)

From IS 875 Part 3, Table 1 or Annexure A (Wind Zone Map):

| City | Vb (m/s) | Wind Zone |
|------|---------|-----------|
| Ahmedabad | 39 | III |
| Bangalore | 33 | I |
| Bhopal | 40 | III |
| Bhubaneswar | 50 | V |
| Chandigarh | 47 | IV |
| Chennai | 50 | V |
| Coimbatore | 39 | III |
| Delhi | 47 | IV |
| Guwahati | 50 | V |
| Hyderabad | 44 | IV |
| Jaipur | 47 | IV |
| Kochi | 39 | III |
| Kolkata | 50 | V |
| Lucknow | 47 | IV |
| Mumbai | 44 | IV |
| Nagpur | 44 | IV |
| Patna | 47 | IV |
| Pune | 39 | III |
| Thiruvananthapuram | 39 | III |
| Visakhapatnam | 50 | V |

For cities not listed, use the nearest city or interpolate from the wind zone map.

#### Step 2: Design Wind Speed (Vz)

```
Vz = Vb × k₁ × k₂ × k₃ × k₄
```

**k₁ — Risk Coefficient (IS 875 Table 1):**

| Structure Class | Design Life (years) | k₁ |
|----------------|--------------------|----|
| General structures (signs, pylons) | 50 | 1.00 |
| Temporary structures | 5 | 0.82 |
| Important structures (hospitals, etc.) | 100 | 1.06 |
| Post-disaster (fire station, etc.) | 100 | 1.08 |

For signage: **k₁ = 1.0** (general) unless the sign is on a critical facility.

**k₂ — Terrain & Height Factor (IS 875 Table 2):**

| Height (m) | Category 1 (Open) | Category 2 (Open w/ obs.) | Category 3 (Suburban) | Category 4 (Urban) |
|-----------|-------------------|--------------------------|----------------------|-------------------|
| Up to 10 | 1.05 | 1.00 | 0.91 | 0.80 |
| 15 | 1.09 | 1.05 | 0.97 | 0.80 |
| 20 | 1.12 | 1.07 | 1.01 | 0.80 |
| 30 | 1.15 | 1.12 | 1.06 | 0.97 |
| 50 | 1.20 | 1.17 | 1.12 | 1.10 |

Interpolate for intermediate heights.

**k₃ — Topography Factor:**
- Flat terrain: k₃ = 1.0
- Hilly terrain: k₃ = 1.0 to 1.36 (depends on slope, use Clause 5.3.3)
- Escarpment/cliff: k₃ up to 1.36 at crest

For most signage projects in developed areas: **k₃ = 1.0**

**k₄ — Importance Factor for Cyclonic Regions:**
- Non-cyclonic: k₄ = 1.0
- Cyclonic coast: k₄ = 1.15 (structures within 60km of coast in cyclonic zones)

#### Step 3: Design Wind Pressure

```
pd = 0.6 × Vz²  (N/m²)
```

Where Vz is in m/s and pd is in N/m² (Pa).

**Quick reference — pd for common Vz values:**

| Vz (m/s) | pd (N/m²) | pd (kN/m²) |
|----------|----------|-----------|
| 30 | 540 | 0.54 |
| 35 | 735 | 0.74 |
| 40 | 960 | 0.96 |
| 44 | 1162 | 1.16 |
| 47 | 1325 | 1.33 |
| 50 | 1500 | 1.50 |

#### Step 4: Force Coefficients for Signs

**Flat signs / Sign boards (IS 875 Table 21):**

| Aspect Ratio (b/h) | Cf (Above Ground) | Cf (On Ground with clearance) |
|--------------------|--------------------|-------------------------------|
| 1 | 1.1 | 1.2 |
| 2 | 1.2 | 1.3 |
| 5 | 1.3 | 1.4 |
| 10 | 1.4 | 1.5 |
| 20 | 1.5 | 1.6 |
| ≥40 | 1.8 | 1.9 |

**For pylon columns (drag coefficient Cd):**

| Section Shape | Cd |
|--------------|-----|
| Circular (CHS), Re < 4×10⁵ (subcritical) | 1.2 |
| Circular (CHS), Re > 4×10⁵ (supercritical) | 0.6 |
| Square (SHS) | 2.0 |
| Rectangular (RHS), wind on narrow face | 1.4 |
| Rectangular (RHS), wind on broad face | 2.0 |
| Flat plate / open section | 2.0 |
| Lattice tower (solidity 0.1-0.5) | 1.5-3.5 |

Reynolds number Re = Vz × D / ν (ν ≈ 1.5 × 10⁻⁵ m²/s for air)

#### Step 5: Wind Force Calculation

```
F_sign = Cf × pd × A_sign  (N)

F_column = Cd × pd × A_column  (N)
   where A_column = diameter (or width) × exposed height

F_total = F_sign + Σ F_column  (N)
```

#### Step 6: Moment at Base

```
M_base = F_sign × h_centroid + Σ(F_column_i × h_centroid_column_i)

where h_centroid = height from base to centroid of sign face
```

---

## 2. Steel Member Design

### Working Stress Method (IS 800:2007, Section 11)

#### Permissible Stresses

For E250 grade steel (fy = 250 MPa):

| Stress Type | Formula | Value (MPa) |
|------------|---------|-------------|
| Axial tension | 0.6 × fy | 150 |
| Bending tension/compression | 0.66 × fy | 165 |
| Shear (average) | 0.4 × fy | 100 |
| Bearing on contact | 0.75 × fy | 187.5 |

#### Axial Compression — Permissible Stress

Depends on slenderness ratio λ = KL/r:

| λ | σ_ac (MPa) for E250 |
|---|---------------------|
| 20 | 148 |
| 40 | 139 |
| 60 | 121 |
| 80 | 98 |
| 100 | 74 |
| 120 | 54 |
| 140 | 40 |
| 160 | 31 |
| 180 | 24 |
| 200 | 19 |
| 250 | 12 |

Maximum slenderness ratios:
- Compression members: λ ≤ 180
- Tension members: λ ≤ 400
- Temporary bracing: λ ≤ 350

#### Effective Length Factors (K)

| End Condition | K |
|--------------|---|
| Both ends fixed | 0.65 |
| One fixed, one pinned | 0.80 |
| Both ends pinned | 1.00 |
| One fixed, one free (cantilever) | 2.00 |
| One fixed, one guided | 1.20 |

For pylon columns fixed at base, free at top: **K = 2.0**
For pylon columns fixed at base, braced at sign cabinet: **K ≈ 1.2**

#### Combined Stress Check

For members under combined axial + bending:

```
(σ_ac,cal / σ_ac) + (Cm × σ_bc,cal) / ((1 - σ_ac,cal/σ_e) × σ_bc) ≤ 1.0

where:
  σ_ac,cal = P/A (calculated axial stress)
  σ_bc,cal = M/Z (calculated bending stress)
  σ_ac = permissible axial stress from table
  σ_bc = permissible bending stress = 0.66fy
  σ_e = π²E/(KL/r)² (Euler buckling stress)
  Cm = 0.85 for members with transverse loads (wind)
```

### Common Hollow Section Properties (IS 1161)

**CHS (Circular Hollow Sections) — Most Used for Pylon Columns:**

| NB (mm) | OD (mm) | Thickness (mm) | Weight (kg/m) | A (mm²) | I (×10⁶ mm⁴) | Z (×10³ mm³) | r (mm) |
|---------|---------|---------------|---------------|---------|--------------|--------------|--------|
| 65 | 76.1 | 3.2 | 5.71 | 732 | 0.635 | 16.7 | 25.8 |
| 80 | 88.9 | 4.0 | 8.38 | 1067 | 1.27 | 28.6 | 30.0 |
| 100 | 114.3 | 4.5 | 12.2 | 1551 | 3.07 | 53.7 | 38.9 |
| 125 | 139.7 | 5.0 | 16.6 | 2117 | 5.91 | 84.6 | 47.6 |
| 150 | 168.3 | 5.0 | 20.1 | 2564 | 10.5 | 125 | 57.7 |
| 150 | 168.3 | 6.3 | 25.2 | 3206 | 12.8 | 152 | 57.0 |
| 200 | 219.1 | 6.3 | 33.1 | 4211 | 28.3 | 258 | 75.3 |
| 200 | 219.1 | 8.0 | 41.6 | 5302 | 34.8 | 317 | 74.5 |
| 250 | 273.0 | 6.3 | 41.4 | 5276 | 55.2 | 404 | 94.1 |
| 250 | 273.0 | 8.0 | 52.3 | 6660 | 68.3 | 500 | 93.3 |
| 300 | 323.9 | 8.0 | 62.3 | 7936 | 115 | 711 | 111 |

**SHS (Square Hollow Sections):**

| Size (mm) | Thickness (mm) | Weight (kg/m) | A (mm²) | I (×10⁶ mm⁴) | Z (×10³ mm³) | r (mm) |
|-----------|---------------|---------------|---------|--------------|--------------|--------|
| 50×50 | 3.0 | 4.25 | 541 | 0.175 | 7.01 | 18.0 |
| 65×65 | 3.2 | 5.99 | 763 | 0.431 | 13.3 | 23.8 |
| 75×75 | 3.6 | 7.89 | 1006 | 0.740 | 19.7 | 27.1 |
| 80×80 | 4.0 | 9.22 | 1174 | 0.952 | 23.8 | 28.5 |
| 100×100 | 4.0 | 11.7 | 1494 | 1.94 | 38.8 | 36.0 |
| 100×100 | 5.0 | 14.4 | 1835 | 2.32 | 46.3 | 35.5 |
| 120×120 | 5.0 | 17.5 | 2235 | 4.13 | 68.8 | 43.0 |
| 150×150 | 5.0 | 22.3 | 2835 | 8.38 | 112 | 54.4 |
| 150×150 | 6.3 | 27.6 | 3517 | 10.2 | 136 | 53.8 |
| 200×200 | 6.3 | 37.6 | 4797 | 24.9 | 249 | 72.0 |
| 200×200 | 8.0 | 47.1 | 5994 | 30.5 | 305 | 71.3 |
| 250×250 | 8.0 | 59.9 | 7634 | 61.8 | 494 | 89.9 |

**RHS (Rectangular Hollow Sections) — Selected sizes:**

| Size (mm) | Thickness (mm) | Weight (kg/m) | Ix (×10⁶) | Zx (×10³) | Iy (×10⁶) | Zy (×10³) |
|-----------|---------------|---------------|-----------|-----------|-----------|-----------|
| 100×50 | 4.0 | 8.59 | 1.42 | 28.4 | 0.496 | 19.8 |
| 120×60 | 4.0 | 10.6 | 2.54 | 42.3 | 0.887 | 29.6 |
| 150×75 | 5.0 | 16.6 | 5.59 | 74.5 | 1.94 | 51.7 |
| 150×100 | 5.0 | 18.6 | 6.53 | 87.1 | 3.54 | 70.8 |
| 200×100 | 5.0 | 22.3 | 12.2 | 122 | 4.66 | 93.1 |
| 200×100 | 6.3 | 27.6 | 14.8 | 148 | 5.63 | 113 |
| 250×150 | 6.3 | 37.6 | 33.8 | 270 | 14.9 | 199 |
| 300×200 | 8.0 | 59.9 | 76.2 | 508 | 40.2 | 402 |

---

## 3. Foundation Design

### Pier / Block Foundation for Pylons

**Design Philosophy:**
The foundation must resist overturning from wind moments while keeping bearing pressure within the soil's capacity. The self-weight of the foundation and any soil above it provides the stabilising moment.

```
Stability Check:
  FoS_overturning = Stabilising Moment / Overturning Moment ≥ 1.5

  Stabilising Moment = (W_foundation + W_soil) × (B/2)
  Overturning Moment = M_wind + H_wind × D_foundation

Bearing Pressure Check:
  σ_max = P/(B×L) + M/(B×L²/6) ≤ SBC (Safe Bearing Capacity)
  σ_min = P/(B×L) - M/(B×L²/6) ≥ 0 (no tension at base)
```

**Typical Foundation Sizes for Pylons:**

| Pylon Height | Sign Size | Foundation (B×L×D) | Concrete Grade | Rebar |
|-------------|-----------|-------------------|---------------|-------|
| 3m | 1.5×1.0m | 0.8×0.8×1.0m | M25 | 4×12mm Fe500 each way |
| 5m | 2.0×1.5m | 1.0×1.0×1.2m | M25 | 6×12mm Fe500 each way |
| 7m | 3.0×1.5m | 1.2×1.2×1.5m | M25 | 6×16mm Fe500 each way |
| 10m | 4.0×2.0m | 1.5×1.5×2.0m | M25 | 8×16mm Fe500 each way |
| 12m | 5.0×2.0m | 2.0×2.0×2.5m | M30 | 10×16mm Fe500 each way |
| 15m | 6.0×3.0m | 2.5×2.5×3.0m | M30 | 12×20mm Fe500 each way |

These are starting points — always verify with calculations for the specific wind zone.

### Safe Bearing Capacity Reference

| Soil Type | SBC (kN/m²) |
|-----------|------------|
| Soft clay | 50-75 |
| Medium clay | 75-150 |
| Stiff clay | 150-300 |
| Loose sand | 50-100 |
| Medium sand | 100-200 |
| Dense sand | 200-400 |
| Gravel | 300-500 |
| Soft rock | 400-1000 |
| Hard rock | 1000+ |

**Always request a soil investigation report for pylons >7m tall.**

---

## 4. Base Plate & Anchor Bolt Design

### Base Plate Sizing

```
Minimum plate size: Column section + 2 × (edge distance for anchor bolts)
  Edge distance minimum: 2.5 × bolt diameter

Plate thickness:
  For cantilever action from face of column to bolt line:
  t = √(6 × M_plate / (b × fy))
  where M_plate = bearing pressure × cantilever length² / 2
  Minimum plate thickness: 12mm
```

### Anchor Bolt Capacity (ASTM F1554 / IS equivalents)

| Bolt Size | Grade 36 Tensile Capacity (kN) | Grade 55 Tensile Capacity (kN) | Grade 105 Tensile Capacity (kN) |
|-----------|-------------------------------|-------------------------------|--------------------------------|
| M12 | 25.4 | 39.0 | 74.5 |
| M16 | 46.1 | 70.8 | 135 |
| M20 | 72.7 | 112 | 213 |
| M24 | 105 | 161 | 308 |
| M30 | 166 | 255 | 487 |
| M36 | 241 | 370 | 706 |

### Anchor Bolt Embedment Depths (Chemical Anchors)

| Bolt Size | Minimum Embedment (mm) | Recommended Embedment (mm) | Min Edge Distance (mm) | Min Spacing (mm) |
|-----------|----------------------|---------------------------|----------------------|-----------------|
| M12 | 110 | 150 | 60 | 90 |
| M16 | 125 | 190 | 80 | 120 |
| M20 | 170 | 240 | 100 | 150 |
| M24 | 210 | 290 | 120 | 180 |
| M30 | 260 | 360 | 150 | 225 |

### Standard Bolt Patterns for Pylon Base Plates

**4-bolt pattern** (most common for small-medium pylons):
- Bolts at corners of a square/rectangle
- Bolt circle: column dimension + 100mm on each side

**6-bolt pattern** (medium-large pylons):
- 2 bolts on each long side, 1 bolt on each short side
- Better moment resistance in the primary wind direction

**8-bolt pattern** (large pylons):
- Equal spacing around the perimeter
- Required when moment exceeds 4-bolt capacity

---

## 5. Connection Design — Welds

### Fillet Weld Capacity (IS 800:2007)

```
Strength of fillet weld per mm run:
  q = 0.7 × s × fu / (√3 × γ_mw)

where:
  s = weld throat size = 0.7 × leg size (for fillet welds)
  fu = ultimate tensile strength of weld metal (410 MPa for E41xx)
  γ_mw = 1.25 (partial safety factor for welds)
```

**Quick reference — fillet weld capacity per mm length:**

| Weld Leg Size (mm) | Throat (mm) | Capacity (kN/mm) for E410xx |
|--------------------|-------------|----------------------------|
| 4 | 2.8 | 0.374 |
| 5 | 3.5 | 0.467 |
| 6 | 4.2 | 0.561 |
| 8 | 5.6 | 0.748 |
| 10 | 7.0 | 0.935 |
| 12 | 8.4 | 1.122 |

### Minimum Weld Sizes (IS 800 Table 21)

| Thicker Part Thickness (mm) | Minimum Fillet Weld Size (mm) |
|---------------------------|------------------------------|
| Up to 10 | 3 |
| 10-20 | 5 |
| 20-32 | 6 |
| 32-50 | 8 (first run), then fill |

---

## 6. Connection Design — Bolts

### Bolt Capacity (IS 800:2007)

**Grade 4.6 bolts (mild steel):**

| Bolt Size | Tensile Capacity (kN) | Shear Capacity — Single Shear (kN) | Bearing Capacity on 8mm plate (kN) |
|-----------|---------------------|-----------------------------------|-----------------------------------|
| M12 | 28.3 | 16.3 | 32.0 |
| M16 | 51.4 | 29.7 | 42.7 |
| M20 | 81.0 | 46.8 | 53.3 |
| M24 | 117 | 67.3 | 64.0 |

**Grade 8.8 bolts (high-strength):**

| Bolt Size | Tensile Capacity (kN) | Shear Capacity — Single Shear (kN) |
|-----------|---------------------|-----------------------------------|
| M12 | 56.6 | 32.7 |
| M16 | 103 | 59.3 |
| M20 | 162 | 93.6 |
| M24 | 234 | 135 |

---

## 7. Deflection & Serviceability

### Deflection Limits for Signage Structures

| Structure Type | Allowable Deflection |
|---------------|---------------------|
| Pylon column tip | Height / 200 |
| Sign cabinet frame | Span / 240 |
| Cantilevered bracket | Span / 180 |
| Overall sign face | Span / 360 (to prevent visible distortion) |

### Deflection Formulas

**Cantilever column with point load at top:**
```
δ = F × L³ / (3 × E × I)
```

**Cantilever column with uniformly distributed wind load:**
```
δ = w × L⁴ / (8 × E × I)
```

**Where:**
- E = 200,000 MPa (for steel)
- I = moment of inertia of the section (mm⁴)
- L = effective cantilever length (mm)

---

## 8. Seismic Considerations

### IS 1893 Part 1:2016

For signage structures in Seismic Zones III, IV, and V, seismic forces must be considered:

```
Base shear: Vb = Ah × W

where:
  Ah = (Z/2) × (I/R) × (Sa/g)
  Z = Zone factor (Zone II=0.10, III=0.16, IV=0.24, V=0.36)
  I = Importance factor (1.0 for general signage)
  R = Response reduction factor (2.0 for unreinforced/unbraced, 4.0 for braced)
  Sa/g = Spectral acceleration coefficient (depends on natural period and soil type)
  W = Seismic weight (dead load of sign + structure)
```

**For most signage structures, wind loads will govern over seismic forces.** However, check both and design for the critical case. Seismic may govern in:
- Low wind zones (Zone I-II) with heavy signs
- Seismic Zone V locations
- Signs with heavy LED panels or masonry elements
