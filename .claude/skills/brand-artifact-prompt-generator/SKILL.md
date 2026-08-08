---
name: brand-artifact-prompt-generator
description: Generate detailed AI image prompts for spatial branding artifacts (signage, murals, wall graphics, wayfinding) by analyzing brand guidelines and site images. Use when the user needs to create prompts for internal branding (office signage, wayfinding, employee spaces) or external branding (storefronts, building signage, exterior graphics) and has uploaded brand guidelines, location photos, reference images, or any combination of visual materials.
---

# Brand Artifact Prompt Generator

Transform brand guidelines and site images into detailed, AI-ready prompts for creating spatial branding artifacts.

## Workflow

### Step 1: Gather Materials

Ask the user to provide:
- **Brand guidelines** (PDFs, images, documents with logos, colors, typography, tone)
- **Site/location images** (photos of actual spaces where branding will be installed)
- **Reference images** (optional: mood boards, competitor examples, style inspiration)
- **Text description** (optional: additional context about the project)

Accept up to 5 images total. Users can upload multiple files at once.

### Step 2: Analyze Materials

When materials are provided, analyze them systematically:

**Brand Guidelines Analysis:**
- Extract brand colors (hex codes, names, primary/secondary/accent)
- Identify typography (font families, weights, styles, hierarchy)
- Note logo variations and usage rules
- Understand brand personality (modern, traditional, playful, professional, etc.)
- Identify key brand elements (patterns, textures, shapes, icons)
- Note any specific brand voice or messaging guidelines

**Site Image Analysis:**
- Identify space type (hospital, retail, office, restaurant, exterior, etc.)
- Note architectural features (materials, lighting, ceiling height, wall surfaces)
- Understand viewing angles and sight lines
- Assess existing design language
- Identify installation constraints (mounting surfaces, dimensions, accessibility)
- Note environmental factors (lighting conditions, traffic flow, surrounding elements)

**Reference Image Analysis (if provided):**
- Extract style cues (minimalist, ornate, geometric, organic, etc.)
- Note composition techniques
- Identify effective design patterns
- Understand material treatments

### Step 3: Determine Artifact Type

Based on the user's request, identify which type of branding artifact to create:

**Internal Branding:**
- Office wayfinding signage
- Department identification signs
- Conference room nameplates
- Wall murals for employee spaces
- Branded environmental graphics
- Directional signage systems
- Welcome/reception area graphics

**External Branding:**
- Building signage (channel letters, monument signs)
- Storefront graphics
- Window displays and vinyl graphics
- Exterior wall murals
- Parking garage wayfinding
- Campus directional signage
- Architectural brand integration

### Step 4: Generate Enhanced Prompt

Create a comprehensive prompt that includes:

**1. Project Context**
- Artifact type and purpose
- Installation location and environment
- Target audience and viewing distance

**2. Brand Integration**
- Specific brand colors with hex codes
- Typography specifications (fonts, sizes, hierarchy)
- Logo usage and placement
- Brand patterns or elements to incorporate
- Brand personality and tone

**3. Technical Specifications**
- Viewing angle and perspective
- Approximate dimensions and scale
- Mounting method (wall-mounted, suspended, freestanding, etc.)
- Material specifications (acrylic, metal, vinyl, paint, LED, etc.)
- Depth and dimensional details (flat, 3D relief, channel letters, etc.)

**4. Visual Style**
- Rendering type (photorealistic 3D render, architectural visualization, concept sketch)
- Lighting approach (ambient, spotlit, backlit, edge-lit, front-lit)
- Atmosphere and mood
- Level of detail

**5. Spatial Context**
- How the artifact integrates with the space
- Surrounding architectural elements
- Context showing placement in environment
- Relationship to other wayfinding or branding elements

**6. Design Elements**
- Visual hierarchy and information architecture
- Color application and contrast
- Typography treatment
- Iconography or symbols (if applicable)
- Texture and finish details

**7. Composition & Framing**
- Camera angle (straight-on, slight angle, hero shot, environmental context)
- Depth of field
- Focal points
- Background treatment

### Step 5: Output Format

Present the enhanced prompt in a clear, ready-to-use format:

```
[ENHANCED PROMPT]

[Your comprehensive prompt here, written as a single paragraph or structured sections]

[END PROMPT]
```

Then provide:
- **Artifact type identified:** [type]
- **Key brand elements applied:** [list]
- **Recommended tools:** [e.g., Midjourney, DALL-E, Stable Diffusion]
- **Suggested prompt modifiers:** [e.g., --ar 16:9, --style, etc. if applicable]

## Examples

### Example 1: Hospital Wayfinding

**User Input:**
- Brand guidelines showing blue (#2C5F9C) and white color scheme
- Site photo of hospital corridor
- Request: "Create wayfinding signage for radiology department"

**Generated Prompt:**
```
Photorealistic 3D render of modern hospital wayfinding signage system for radiology department, wall-mounted perpendicular to corridor wall with aluminum frame in brushed finish, featuring clean sans-serif typography (Helvetica Neue) in hospital brand blue (#2C5F9C) on white acrylic panel with subtle gradient, department name "RADIOLOGY" in 4-inch letters with directional arrow, secondary text showing room numbers in 2-inch type, edge-lit LED illumination creating soft glow, viewed at eye level (5 feet height) in bright hospital corridor with white walls and linear ceiling lights, contemporary healthcare design aesthetic, crisp shadows indicating daytime lighting, architectural visualization style showing sign in context with corridor perspective, clean and professional medical environment
```

### Example 2: Retail Storefront

**User Input:**
- Brand guidelines with bold orange (#FF6B35) and black
- Exterior storefront photo
- Request: "Create channel letter signage for store name"

**Generated Prompt:**
```
High-quality architectural rendering of illuminated channel letter signage spelling "URBAN ESSENCE" mounted on modern storefront facade, individual letters in brushed black aluminum with vibrant orange (#FF6B35) LED halo backlighting creating dramatic glow effect against charcoal gray building exterior, letters 24 inches tall with 2-inch depth, contemporary sans-serif typeface (Montserrat Bold), slight upward viewing angle showing dimensionality, golden hour lighting conditions with warm ambient light, urban retail environment with pedestrian context, sharp focus on signage with shallow depth of field, professional real estate photography style, high contrast and vivid colors
```

## Quality Guidelines

**Always Include:**
- Specific brand colors (with codes)
- Exact typography details
- Material specifications
- Lighting approach
- Viewing angle and scale
- Environmental context

**Avoid:**
- Vague descriptions ("nice," "modern looking")
- Generic colors ("blue" instead of specific hex)
- Unspecified materials
- Missing dimensional context
- Lack of spatial integration

## Prompt Enhancement Principles

1. **Be Specific:** Use exact measurements, colors, materials
2. **Show Context:** Include environmental setting, not just isolated object
3. **Specify Technical Details:** Mounting, lighting, materials, finishes
4. **Match Brand Personality:** Ensure visual style aligns with brand values
5. **Consider Viewing Experience:** Account for distance, angle, lighting conditions
6. **Add Professional Polish:** Mention rendering quality, photography style, focal points

## When Materials Are Limited

If brand guidelines are incomplete:
- Ask user for specific brand colors and fonts
- Work with provided materials and note assumptions
- Suggest placeholder values that can be adjusted

If site images are unavailable:
- Request description of space type and characteristics
- Use typical environments for that artifact type
- Note that final prompt may need adjustment when site is known

## Follow-Up

After generating the prompt, offer to:
- Create variations for different artifact types
- Adjust technical specifications
- Generate prompts for complementary wayfinding elements
- Refine based on generated image results
