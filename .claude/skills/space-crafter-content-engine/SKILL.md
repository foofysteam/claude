---
name: space-crafter-content-engine
description: >
  Full content engine for Space Crafter Studio — a spatial branding and experiential design studio.
  Use this skill for ANY of the following: scanning design trends and generating social media post ideas,
  generating platform-ready copy (Instagram, LinkedIn, Facebook, X, ad copy) in Space Crafter Studio's voice,
  logging posted content to a content calendar, tracking what was posted and when, or deploying the
  Content Intelligence Studio or Content Calendar as standalone tools.
  Triggers include: "scan trends", "generate post ideas", "write copy for", "log a post", "content calendar",
  "what should I post", "create content", "content studio", or any request to produce social media content
  for Space Crafter Studio. Always activate this skill before producing any content or deploying any tool
  for Space Crafter Studio.
---

# Space Crafter Studio — Content Engine

This skill bundles three things:
1. **Voice & brand rules** — governs all copy produced for Space Crafter Studio
2. **Content Intelligence Studio** — a live trend-scanning + copy generation tool (artifact)
3. **Content Calendar** — a persistent post tracker (artifact)

---

## Brand quick-reference

**What Space Crafter Studio does:**
Spatial branding and experiential design — signage (3D lit, reverse-lit, edge-lit letters, fabric light boxes, backlit boards, frost films, wall graphics), environmental branding, reception branding, wayfinding, façade branding, experience centers.

**Voice:** Premium but human. Strategic, not fluffy. Design-led and visually intelligent. Specific over generic. Minimal yet expressive. Confident and insight-led.

**Never use:** elevate, stunning, innovative, world-class, transform your space, one-stop solution, em dashes, hype-heavy claims, robotic jargon, empty superlatives.

**Preferred structures:**
- Observation → insight → design takeaway (LinkedIn, thought leadership)
- Hook → short story → insight (Instagram, reels)
- Problem → design solution → result (project showcases)
- Question → explanation → takeaway (signage education)

**Content buckets:** Spatial storytelling · Signage intelligence · Experiential branding · Material craft · Transformation stories · Behind the scenes · Project showcases · Design thinking · Client outcomes

**Platform defaults:**
- Instagram: visual-first, punchy, carousel-friendly, 3–5 hashtags in caption
- LinkedIn: 150–220 words, structured, insight-led, no question openers
- Facebook: accessible, slightly more descriptive than Instagram
- X / Twitter: under 240 chars, sharp observation-led
- Ad copy: hook + business benefit + natural CTA

---

## Tool 1 — Content Intelligence Studio

**When to deploy:** User wants to scan trends, get post ideas, or generate copy across platforms.

Deploy the Content Intelligence Studio artifact. It:
- Searches the web live (Architectural Digest, Veedu, Asian Paints, signage/environmental branding trends)
- Surfaces 5 ranked post ideas with bucket, platform, and trend tags
- On idea selection, generates full copy for all 5 platforms simultaneously
- Copy/paste ready per platform with a Refine button for chat iteration

**How to deploy:**
Present the `assets/content_studio.html` file to the user using the present_files tool, OR rebuild the widget inline using the visualize tool if the user wants it in-chat.

The in-chat version uses the Anthropic API via the artifact's built-in fetch — no extra setup needed inside Claude.ai. The downloaded HTML version requires the user's own Anthropic API key entered at the top of the file.

---

## Tool 2 — Content Calendar

**When to deploy:** User wants to log a post they've published, view their posting history, filter by platform, or export their content record.

Deploy the Content Calendar artifact. It:
- Logs posts with title, date, platforms, content bucket, and notes
- Persists data across sessions (in-chat: Claude storage; downloaded: localStorage)
- Groups entries by month with platform colour-coded tags
- Shows stats: total posts, this month, platforms active, buckets used
- Exports to CSV

**How to deploy:**
Present the `assets/content_calendar.html` file using the present_files tool, OR rebuild inline using the visualize tool.

---

## Workflow: end-to-end content cycle

When a user wants to go from zero to posted:

1. **Scan** — Open Content Intelligence Studio → scan trends → get 5 ideas
2. **Select** — User picks an idea
3. **Generate** — Copy produced for all platforms
4. **Post** — User posts on their channels
5. **Log** — Open Content Calendar → log the post with date, platforms, bucket, notes

---

## Writing copy directly (no tool)

### Step 1 — Angle selection (always do this first)

When a user gives a topic (e.g. "retail space", "corporate offices", "wayfinding"), do NOT generate copy immediately. First, present **3 angle options** — each taking a distinct strategic lens on the topic.

Each angle must have:
- **A short label** (2–5 words, e.g. "The commercial argument")
- **A one-line description** of what the post argues or reveals
- **A content bucket tag** (from the list above)

Angle types to draw from (pick 3 that are genuinely distinct for the topic):
- The commercial argument — business case for spatial investment
- The client misconception — a common wrong belief, corrected
- The process reveal — how something is actually made or decided
- The industry observation — a trend or pattern noticed in the field
- The education angle — explaining a product, material, or technique
- The transformation story — before/after or problem/solution
- The cultural/behavioural insight — how people experience space
- The design thinking lens — why design decisions matter beyond aesthetics

Format angle options exactly like this:

---
**Pick an angle:**

**1. [Label]** `[Bucket]`
[One-line description of the argument or story]

**2. [Label]** `[Bucket]`
[One-line description]

**3. [Label]** `[Bucket]`
[One-line description]

---

Wait for the user to select an angle (by number or description) before generating any copy.

### Step 2 — Copy generation

Once the user selects an angle, generate full cross-platform copy using that angle as the strategic frame. Follow brand rules and use this output structure:

```
[Platform]
Post: ...
Caption: ... (Instagram only)
```

Always produce all 5 platforms unless the user specifies otherwise. Check every output against the avoidance list before responding.

---

## Assets in this skill

| File | Purpose |
|---|---|
| `assets/content_studio.html` | Standalone Content Intelligence Studio |
| `assets/content_calendar.html` | Standalone Content Calendar |

To present either file to the user, use the `present_files` tool with the asset path.
