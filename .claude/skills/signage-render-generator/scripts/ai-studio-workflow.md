# Google AI Studio — Automated Image Generation Workflow

Step-by-step browser automation using Claude in Chrome tools to generate signage renders in Google AI Studio.

## Prerequisites

- User must be logged into their Google account in Chrome
- Google AI Studio must be accessible at aistudio.google.com

## Workflow Steps

### Phase 1: Open AI Studio

```
Tool: mcp__Claude_in_Chrome__navigate
URL: https://aistudio.google.com/prompts/new_chat
```

Wait for the page to load completely. Verify the chat interface is visible.

### Phase 2: Set Up the Model (if needed)

Check if Gemini 2.5 Flash is selected (this is the model with Nano Banana image generation).

```
Tool: mcp__Claude_in_Chrome__read_page
```

Look for model selector. If not on Gemini 2.5 Flash:
1. Click the model dropdown
2. Select "Gemini 2.5 Flash" or "Gemini Flash"

### Phase 3: Upload Site Photo (if provided)

If the user provided a site photograph for composite rendering:

```
Tool: mcp__Claude_in_Chrome__file_upload
```

Upload the site photo. Wait for upload confirmation.

### Phase 4: Enter the Prompt

```
Tool: mcp__Claude_in_Chrome__form_input
```

Paste the composed prompt into the chat input field.

**Important prompt structure for image generation:**
- Start with "Generate an image:" or "Create a photorealistic image of:"
- Include all the details from the composed prompt
- If site photo was uploaded, prefix with: "Using the uploaded photo as the background scene, "

### Phase 5: Submit and Wait

```
Tool: mcp__Claude_in_Chrome__shortcuts_execute
Action: Press Enter or click Send button
```

Wait for generation to complete (typically 10-30 seconds). The image will appear inline in the chat.

### Phase 6: Verify and Download

```
Tool: mcp__Claude_in_Chrome__read_page
```

Check that an image was generated successfully. If the response is text-only (no image), the prompt may need adjustment — try adding "Generate an image:" prefix explicitly.

To download:
1. Right-click (or find download button) on the generated image
2. Save to the outputs folder

### Phase 7: Iterate if Needed

If the first result isn't satisfactory:
- Adjust specific parameters (lighting, angle, materials)
- Add more detail to underspecified areas
- Request a variation: "Generate another version with [CHANGE]"

## Alternative: Direct Gemini API Approach

If browser automation encounters issues, fall back to the Gemini API directly:

```python
import google.generativeai as genai
import os

# User must set their API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-exp")

response = model.generate_content(
    "Generate an image: [FULL PROMPT HERE]",
    generation_config=genai.GenerationConfig(
        response_modalities=["image", "text"]
    )
)

# Save the generated image
for part in response.parts:
    if part.inline_data:
        with open("render.png", "wb") as f:
            f.write(part.inline_data.data)
        print("Image saved to render.png")
```

## Troubleshooting

| Issue | Solution |
|-------|---------|
| No image generated, only text | Add "Generate an image:" prefix. Check model supports image generation |
| Image doesn't match sign specs | Be more specific about dimensions relative to surroundings |
| Text on sign is garbled | Shorten brand text to under 15 characters, or describe text style instead |
| Wrong perspective | Explicitly state camera angle and distance in meters |
| Materials look generic | Add texture descriptions: "visible brushed grain", "welded seam details" |
| Site composite looks pasted-on | Emphasize "matching existing light direction and shadow angles" |
| Sign looks too small/large | Add scale references: "sign is 3x the height of the ground floor" |
