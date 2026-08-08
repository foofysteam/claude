---
name: signage-render-generator
description: >
  Generate photorealistic signage renders using Google AI Studio (Nano Banana / Gemini image generation).
  Takes structural signage specs (from structural-signage-design skill or manual input) and produces
  optimized AI image prompts, then automates the generation workflow in Google AI Studio via browser.
  Trigger on: signage render, signage mockup, realistic signage image, pylon render, building sign render,
  AI Studio signage, Nano Banana signage, generate signage image, visualize signage, client presentation render,
  signage visualization, render pylon, render building sign, mockup signage design, photo-realistic sign.
  Also trigger when user has structural specs and wants to see what the sign will look like installed.
---

# Signage Render Generator

Generate photorealistic signage renders using Google AI Studio's Nano Banana (Gemini) image generation.
This skill bridges the gap between structural engineering specs and client-ready visual presentations.

## How It Works

```
Input (Structural Specs / Design Image / Manual Description)
    │
    ├── Step 1: Extract sign parameters (type, dimensions, materials, mounting)
    ├── Step 2: Select prompt template based on sign category
    ├── Step 3: Compose the full Nano Banana prompt with all details
    ├── Step 4: Open Google AI Studio in browser and generate the image
    └── Step 5: Download and deliver the render
```

## Step 1: Extract Sign Parameters

From the input (structural skill output, uploaded image, or description), extract:

```
SIGN_TYPE:        pylon | facade-flush | projecting | parapet-top | roof-mounted | monument
DIMENSIONS:       Width × Height (e.g., 3m × 1.5m)
TOTAL_HEIGHT:     Height above ground to top of sign (for pylons)
STRUCTURE:        Single pole / Dual pole / Box frame / Cantilever arm / Bracket system
MATERIAL_FINISH:  Brushed SS / Painted MS / Powder-coated aluminium / ACP cladding / Raw steel
SIGN_FACE:        Channel letters / LED panel (P-value) / Flex / Acrylic / Composite
ILLUMINATION:     Front-lit / Back-lit / Halo / Edge-lit / Non-illuminated / Full LED panel
BRAND_TEXT:       The text displayed on the sign
BRAND_COLORS:     Primary color, secondary color (hex codes if available)
MOUNTING_SURFACE: Concrete wall / Glass facade / ACP cladding / Steel frame / Ground
ENVIRONMENT:      Commercial zone / Highway / Mall exterior / Office park / Industrial area
TIME_OF_DAY:      Day (golden hour) / Day (noon) / Dusk / Night
CAMERA_ANGLE:     Street level / Slight upward / Eye level / Aerial / 3/4 perspective
```

If any parameter is missing, use smart defaults based on the sign type (see reference templates).

## Step 2: Select Prompt Template

Based on SIGN_TYPE, select the appropriate base template from `references/prompt-templates.md`.

**Template Categories:**

| Sign Type | Template | Best For |
|-----------|----------|----------|
| Pylon (Single Pole) | `PYLON_SINGLE` | Petrol stations, standalone retail, highway signage |
| Pylon (Dual Pole) | `PYLON_DUAL` | Large commercial, auto dealerships, malls |
| Pylon (Monument/Box) | `PYLON_MONUMENT` | Corporate campuses, hotels, hospitals |
| Facade-Flush | `BUILDING_FLUSH` | Retail storefronts, office buildings |
| Projecting/Blade | `BUILDING_BLADE` | Corner shops, narrow streets, heritage areas |
| Parapet-Top | `BUILDING_PARAPET` | Rooftop branding, tall buildings |
| Roof-Mounted | `BUILDING_ROOF` | Industrial, warehouses, factories |
| LED Panel (Outdoor) | `LED_OUTDOOR` | Digital billboards, P10/P16 displays |
| LED Panel (Building) | `LED_BUILDING` | Facade-integrated LED screens |

## Step 3: Compose the Full Prompt

Combine the template with extracted parameters. The prompt structure MUST follow this order for best Nano Banana results:

```
[RENDERING_STYLE] of [SIGN_DESCRIPTION] [MOUNTING_CONTEXT],
[MATERIAL_AND_FINISH_DETAILS], [DIMENSIONAL_CONTEXT],
[ILLUMINATION_DETAILS], [ENVIRONMENTAL_SETTING],
[CAMERA_AND_LIGHTING], [QUALITY_MODIFIERS]
```

**Rendering Style Options:**
- `Photorealistic architectural photograph` — best for client presentations
- `High-quality 3D render` — best for design review
- `Professional real estate photography style` — best for site context
- `Construction documentation photograph` — best for engineering review

**Quality Modifiers (always append):**
- `sharp focus, high detail, professional architectural photography`
- `8K resolution, ray-traced lighting` (for night scenes with LED)
- `shallow depth of field, bokeh background` (for hero shots)

## Step 4: Generate in Google AI Studio

This skill automates the browser workflow. Read `scripts/ai-studio-workflow.md` for the exact steps.

**Quick workflow:**
1. Open Google AI Studio (aistudio.google.com)
2. Select Gemini 2.5 Flash model (Nano Banana)
3. If user provided a site photo → upload it as reference with instruction to place the sign in this scene
4. Paste the composed prompt
5. Click Generate
6. Wait for image generation (typically 10-30 seconds)
7. Download the generated image
8. Save to outputs folder

**If user provides a site photo** — use this prompt prefix:
```
Using the uploaded photograph as the exact background scene, add [SIGN_DESCRIPTION] to the building/location shown. Maintain the exact perspective, lighting, and environment from the photo. The sign should look naturally installed, with correct shadows, scale, and perspective matching the scene.
```

## Step 5: Deliver Results

Save generated images to the outputs folder with descriptive names:
```
[project-name]-[sign-type]-[view]-render.png
```

For client packages, generate multiple views:
1. **Hero shot** — 3/4 angle, golden hour, shallow DOF
2. **Street view** — eye level, daytime, full context
3. **Night view** — illuminated sign, dramatic lighting
4. **Detail shot** — close-up of sign face, materials visible

## Prompt Enhancement Tips

These tips improve Nano Banana output quality for signage specifically:

**For metal finishes:** Specify "brushed stainless steel with visible grain direction" rather than just "stainless steel"

**For LED illumination:** Describe the glow: "warm white LED backlighting creating a soft halo glow on the wall behind each letter, with slight light bloom at letter edges"

**For scale reference:** Include humans, vehicles, or architectural elements: "two pedestrians walking past for scale reference"

**For Indian architectural context:** Reference common building materials: "mounted on a modern commercial building with grey granite cladding and aluminium composite panel facade sections"

**For text rendering:** Nano Banana 2 handles text well, but keep brand names under 15 characters for best results. For longer names, describe the text style without spelling it out.

**For foundations (pylons):** Include the base: "hexagonal granite-clad base plinth with hidden foundation below grade level"

## When Structural Skill Output Is Available

If the user has already run the `structural-signage-design` skill, map the outputs directly:

| Structural Output | Render Parameter |
|-------------------|-----------------|
| Sign Classification → Pylon/Building-mounted | SIGN_TYPE |
| Overall sign face dimensions | DIMENSIONS |
| Total pylon height / mounting height | TOTAL_HEIGHT |
| Column system (SHS/CHS/dual pole) | STRUCTURE |
| Surface treatment spec | MATERIAL_FINISH |
| Sign cabinet frame material | SIGN_FACE |
| LED panel spec (P-value) | ILLUMINATION |
| City/location | ENVIRONMENT context |
| Foundation type | Base/plinth description |
| Bracket system | Mounting detail description |

## Multiple Render Workflow

For a complete client presentation package, generate renders in this sequence:

1. **Primary daytime hero** — establishes the design
2. **Night illuminated** — shows LED/lighting impact
3. **Context/street view** — shows scale and surroundings
4. **Optional: site photo composite** — if site photos provided

Each render uses the same base parameters but adjusts TIME_OF_DAY, CAMERA_ANGLE, and QUALITY_MODIFIERS.
