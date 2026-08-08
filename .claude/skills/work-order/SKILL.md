---
name: work-order
description: >
  Generate simple production work orders on Notion pages. Analyzes a signage design image, selects the right departments, creates a production flow diagram, lists total materials needed, and gives 4-point instructions per team.
  Triggers: work order, production order, fabrication sheet, production plan, shop floor instructions, fabrication details, material breakdown, scope of work, create work order, generate work order, WO for this sign.
  For the PRODUCTION TEAM, not client-facing. No pricing. Outputs directly to a Notion page.
---

# Work Order Generator

Generate a clean, scannable production work order on a Notion page from a signage design image. The work order has four sections: departments involved, production flow, total materials, and 4-point team instructions.

This is for the production team on the shop floor. They need to glance at the page and immediately know: which teams are involved, what order things flow in, what materials to pull, and what each team needs to do. No letter-by-letter breakdowns — treat the signage as a whole unit.

## Critical Rules

1. **No pricing. Ever.** No unit rates, no costs, no margins. Materials and quantities only. If you catch yourself typing ₹ or "rate" or "cost" — delete it.
2. **LED specs = Type + Colour, always.** Every mention of LEDs must state both: Module or Strip, and the colour (Cool White 6500K / Warm White 3000K / RGB / Purple / etc.). "LED" by itself is never enough — the wrong LEDs getting installed is a real production mistake this prevents.
3. **Output to Notion.** Always write to a Notion page. If the user hasn't shared a page URL, ask for one before proceeding.
4. **No per-letter breakdown.** Total materials for the whole sign, not element-by-element.
5. **Exactly 4 instructions per team.** Not 3, not 5. The last one is always the handover.

## Reference Files

Read these before generating any work order — they contain sheet sizes, LED rules, channel depth charts, and team definitions:

1. `references/material-specs.md` — Sheet sizes, LED rules, channel depth charts, acrylic/ACP specs
2. `references/production-phases.md` — Team definitions, scope templates, handover protocol

---

## Departments

| Department | What They Do |
|------------|-------------|
| **Cutting** | CNC/laser cutting of acrylic faces, aluminium back plates, SS letters, shapes |
| **Printing** | ACP panel routing, V-groove bending, vinyl printing, digital print, router-cut profiles |
| **Welding** | MS frame fabrication, channel letter joining, stud welding, cleat fabrication |
| **Painting** | Surface prep, primer, automotive/powder coat paint, anti-rust treatment |
| **LED** | LED module/strip installation, wiring, SMPS mounting |
| **Assembly** | Acrylic face fitting, sealing, final assembly |
| **QC** | Quality check — dimensions, LED function, finish, alignment |
| **Packing** | Protective wrap, labelling, dispatch-ready packing |

### Default Department Mapping by Sign Type

Use this as a starting point, then verify against the actual design. If a department isn't needed, skip it. If one is missing, add it.

| Type | Departments |
|------|-------------|
| Reception Signage (Lit) | Cutting, Welding, Painting, LED, Assembly, QC, Packing |
| Room Signage | Cutting, Printing, Assembly, QC, Packing |
| Wall Graphic / Mural | Design, Printing, QC, Packing |
| External Signage (Lit) | Cutting, Welding, Painting, LED, Assembly, QC, Packing |
| External Signage (Non-Lit) | Cutting, Welding, Painting, Assembly, QC, Packing |
| Freestanding with ACP | Cutting, Printing, Welding, Painting, Assembly, QC, Packing |
| Frosting Film | Cutting, Printing, QC |
| Pylon | Cutting, Welding, Painting, LED, Assembly, QC, Packing |
| LED Panel | Cutting, LED, Assembly, QC, Packing |

---

## The 4 Steps

When the user uploads a design image and asks for a work order, follow these four steps in order. Each step becomes a section on the Notion page.

### Step 1: Select the Right Departments

Analyze the design image. Determine the signage type, then use the mapping table above to pick departments. Adjust based on what you actually see in the design — the table is a default, not gospel.

Before writing anything to Notion, confirm with the user:

```
Signage Type: [e.g., Reception Signage (Lit)]
Overall Size: [W × H from drawing]
Departments Involved: Cutting → Welding → Painting → LED → Assembly → QC → Packing
Departments NOT Involved: Printing (no vinyl/ACP printing in this design)
```

Wait for confirmation, then proceed.

### Step 2: Create the Production Flow on the Notion Page

Add a visual flow showing the sequence of departments. This tells the shop floor who works when and who hands off to whom.

Use this format on the Notion page (adjust departments based on Step 1):

```
📋 PRODUCTION FLOW

START
  ↓
🔵 CUTTING — [1-line summary of what gets cut]
  ↓
🔴 WELDING — [1-line summary]
  ↓
🟢 PAINTING — [1-line summary]
  ↓
⚡ LED — [1-line summary]
  ↓
🟣 ASSEMBLY — [1-line summary]
  ↓
✅ QC — Check all specs
  ↓
📦 PACKING — Wrap & dispatch
  ↓
DISPATCH
```

If two departments can work in parallel (e.g., Cutting and Printing often run simultaneously), show them side by side:

```
START
  ↓
🔵 CUTTING          🟠 PRINTING
  ↓                    ↓
  └──── both feed ────→ 🔴 WELDING
                          ↓
                        ...
```

### Step 3: Create Total Materials Table

List all materials needed for the entire signage in one consolidated table. No per-letter or per-element breakdown — just the totals.

**Example format:**

| S.No | Material | Specification | Qty | Unit | Notes |
|------|----------|--------------|-----|------|-------|
| 1 | Opal Acrylic | 4mm, 4'×8' sheet | 2 | sheets | Letter faces |
| 2 | Aluminium Channel | 60mm depth, 0.5mm | 14 | running ft | Returns |
| 3 | LED Modules | 3-LED, 1.2W, 15mm, **Cool White 6500K** | 480 | pcs | Front-lit |
| 4 | SMPS | 12V, 200W | 2 | pcs | Power supply |
| 5 | MS Square Tube | 25×25mm | 18 | running ft | Mounting frame |
| 6 | Paint | Purple automotive spray | 2 | cans | Channels + frame |

Rules for this table:
- LED rows must show Type + Colour (e.g., "Module, 15mm, Cool White 6500K")
- Include electrical items: SMPS, wire, connectors
- Include consumables: sealant, adhesive, screws, studs, masking tape
- Use the design image's own callouts and specs wherever visible — they override generic estimates
- No pricing columns

### Step 4: 4-Point Instructions Per Team

For each department from Step 1, write exactly 4 clear instructions. These get read on the shop floor — they need to be scannable in seconds, not paragraphs.

The format for each team:

```
🔵 CUTTING
1. [What to cut, from what material, total quantity]
2. [Second task — e.g., mark hole positions, deburr edges]
3. [Third task — any special notes for this sign]
4. Handover to [NEXT TEAM] — label all pieces by group, confirm count

🔴 WELDING
1. [Primary welding task]
2. [Frame fabrication task]
3. [Mounting hardware task]
4. Handover to [NEXT TEAM] — all joints ground smooth, frame square

🟢 PAINTING
1. [Surface prep task]
2. [Paint application — colour, type, coats]
3. [Special finish or anti-rust treatment]
4. Handover to [NEXT TEAM] — fully dry, uniform finish, no drips

⚡ LED
1. [LED installation — type, colour, total quantity]
2. [Wiring + SMPS — how many, wattage]
3. [Test all LEDs — 100% must light before face fitting]
4. Handover to [NEXT TEAM] — all LEDs tested, wiring secured

🟣 ASSEMBLY
1. [Fit faces/panels]
2. [Seal and secure]
3. [Mount on frame per drawing layout]
4. Handover to QC — fully assembled, clean, no loose parts

✅ QC
1. [Check LED function — no dead spots]
2. [Verify dimensions + spacing match drawing]
3. [Inspect finish — no scratches, drips, or gaps]
4. Handover to PACKING — QC sign-off done

📦 PACKING
1. [Wrap method — bubble wrap, foam guards, etc.]
2. [Label packages with project name + contents]
3. [Bundle mounting hardware separately]
4. DISPATCH READY — notify project manager
```

Key rules:
- Exactly 4 points. No more, no less.
- Point 4 is always the handover — who gets it next and what condition it must be in.
- Be specific: mention materials, quantities, colours, specs. "Cut the acrylic" is useless. "Cut 2 sheets of 4mm opal acrylic — all letter faces" is useful.
- Only include departments that are actually involved (from Step 1).

---

## Notion Page Structure

When writing to Notion, use this structure:

```
# Work Order — [Project Name]

Date: [today]
Sign Type: [type]
Overall Size: [W × H]
Content: [what the sign says/shows]

---

## 📋 Production Flow
[Flow diagram from Step 2]

---

## 🧱 Materials Required
[Table from Step 3]

---

## 🔧 Team Instructions

### 🔵 CUTTING
[4 points]

### 🔴 WELDING
[4 points]

### 🟢 PAINTING
[4 points]

### ⚡ LED
[4 points]

### 🟣 ASSEMBLY
[4 points]

### ✅ QC
[4 points]

### 📦 PACKING
[4 points]

---

## Notes
[Any special instructions, client preferences, or flags]
```

Only include the team sections that are actually involved.

---

## Updating Production Line Items in Notion

When creating or updating Production Line Items in the database (`collection://4b8e8797-50de-42a8-9575-b157f89d9d9a`):

1. Set **Type** to the matching signage category
2. Set **Departments Involved** multi-select from the mapping
3. Set **Current Department** to the first department in the flow
4. Leave all "Done" checkboxes unchecked
5. Set **Status** to "Not Started" or "In Production"
6. Set **Production Start** and **Installation Date** if known
7. Set **Project** relation to link to the pipeline project
