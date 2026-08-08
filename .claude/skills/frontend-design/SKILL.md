---
name: frontend-design
description: Build drop-in sections and components for the existing SpaceCrafter Studio Shopify website. Use when creating new page sections, lead-generation blocks, product explainers, or UI components for spacecrafter.studio. Outputs embeddable HTML/CSS/JS snippets that slot into the existing site without duplicating headers, footers, fonts, or navigation.
metadata:
  author: akshay-kingar
  version: '1.1'
---

# SpaceCrafter Studio — Frontend Design Skill

Build drop-in sections and components for the existing SpaceCrafter Studio Shopify website. Every output is an embeddable snippet — never a full page.

## When to Use This Skill

Use when the user asks to:

- Create new sections for spacecrafter.studio (lead capture, product explainers, service showcases, testimonials, CTAs, comparison tables, pricing, FAQ, etc.)
- Build UI components (cards, modals, interactive elements, calculators, configurators)
- Design lead-generation blocks that drive enquiries and free audit requests
- Create product/service explanation sections that communicate value clearly
- Prototype section layouts before adding them to the live Shopify site

## CRITICAL: Embeddable Sections Only

**Every output is a section that drops into the existing SpaceCrafter website.** Follow these rules strictly:

1. **NEVER generate**: `<html>`, `<head>`, `<body>`, `<!DOCTYPE>`, `<header>`, `<footer>`, `<nav>`, sitemap, or any page-level wrapper. The existing Shopify theme already provides all of these.
2. **NEVER include Google Fonts `<link>` tags.** The site already loads Garrett (serif) and Telegraph (sans) fonts. Just reference them via CSS variables.
3. **NEVER duplicate**: Navigation bars, footer sections, logo, or site-wide elements.
4. **Output format**: A `<section>` (or `<div>`) block containing its own scoped `<style>` and optional `<script>`. This is what gets pasted into a Shopify custom HTML section or page.
5. **Scope all CSS**: Prefix all class names with a section-specific namespace (e.g., `.sc-lead-capture`, `.sc-product-grid`) to avoid conflicts with the existing theme's styles.
6. **Assume the site's CSS variables are already available**: Use `var(--color-coral)`, `var(--font-serif)`, etc. directly. Include a fallback comment block at the top of `<style>` showing the expected variables, in case they need to be added to the theme.

**Output template:**
```html
<!-- SpaceCrafter Section: [Section Name] -->
<!-- Drop this into a Shopify Custom HTML section or page template -->
<section class="sc-[section-name]">
  <style>
    /* Expects these CSS vars from the theme (already defined in theme.css):
       --color-cream, --color-taupe, --color-charcoal, --color-coral
       --font-serif, --font-sans
       If not present, add them to theme.css — see docs/style-guide.html */
    
    .sc-[section-name] { /* scoped styles */ }
  </style>
  
  <!-- Section markup -->
  
  <script>
    // Optional: scoped JS for interactivity
  </script>
</section>
```

## Design Thinking

Before writing code, establish context for the specific section:

- **Goal**: What should this section achieve? Focus on lead generation (free audit requests, enquiries) or clear product/service explanation that builds trust.
- **Audience**: Business owners, facility managers, architects, and brand managers seeking spatial branding and signage solutions across India.
- **Tone**: Warm, editorial, sophisticated — premium but approachable. Never cold or corporate.
- **Conversion focus**: Every section should have a clear next action — a CTA button, a form, a link to the portfolio, or a prompt to request a free audit.
- **Context within the page**: Consider where this section sits in the page flow. It should transition smoothly from the section above and below it without visual jarring.

## Brand Identity

**Company**: SpaceCrafter Studio — Spatial Branding Studio, Bangalore
**Tagline**: "Where Spaces Become Statements."
**Services**: LED signages, wall graphics, lightboxes, ACP cladding, interior branding, wayfinding
**Industries**: Healthcare, Hospitality, Retail, Corporate, Education, F&B
**Key Stats**: 30+ Years · 9,000+ Clients · 7+ Industries
**USP**: Design to installation — all under one roof. AI-powered space visualisation for free audits.

## Design System

### Color Palette

Use CSS custom properties for all colors. Never hardcode hex values inline.

```css
:root {
  /* SpaceCrafter Studio — Core Palette */
  --color-cream:         #F0EEE9;   /* Page background, light sections */
  --color-taupe:         #D7CBC4;   /* Card borders, dividers, secondary text, image overlays */
  --color-charcoal:      #222224;   /* Body text, headings, dark hero/footer sections */
  --color-coral:         #FA9A85;   /* CTA buttons, section labels, hover states, active nav, accents */
  --color-coral-hover:   #f8836b;   /* Button hover state */

  /* Semantic Aliases */
  --color-background:    var(--color-cream);
  --color-foreground:    var(--color-charcoal);
  --color-accent:        var(--color-coral);
  --color-border:        var(--color-taupe);
  --color-text-muted:    #555;
  --color-text-faint:    #999;
}
```

**Color Usage Rules**:
- `Cream (#F0EEE9)` → Page background, light sections, nav background
- `Taupe (#D7CBC4)` → Card borders, horizontal rules, secondary text, image overlays
- `Charcoal (#222224)` → All body text, headings, dark hero sections, footer background
- `Coral (#FA9A85)` → All CTA buttons, section labels, hover states, active nav links, decorative accents

**Dark sections** (hero, contact form, footer) use Charcoal background with Cream text. These should be the minority — most of the page is light.

**NEVER**: Use purple gradients, blue accents, generic grays, or any color outside this palette.

### Typography

```css
:root {
  /* Fonts — Google Fonts equivalents */
  --font-serif: 'Cormorant Garamond', Georgia, serif;     /* Garrett equivalent */
  --font-sans:  'DM Sans', system-ui, sans-serif;          /* Telegraph equivalent */
}
```

Load from Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
```

**Type Scale**:

| Role | Font | Weight | Size | Leading | Tracking | Notes |
|------|------|--------|------|---------|----------|-------|
| Hero Display | Serif | 300 (Light) | 52px | 1.0 | -0.01em | Use `<em>` for coral italic accent word |
| Section Heading | Serif | 400 | 36px | 1.15 | — | |
| Card/Sub Heading | Serif | 500 | 24px | 1.25 | — | |
| Section Label | Sans | 600 | 11px | — | 0.2em | Uppercase, coral color, pattern: `01 — Label` |
| Body Copy | Sans | 400 | 15px | 1.7 | — | Color: #555 |
| Caption/Meta | Sans | 400 | 12px | 1.5 | — | Color: #999 |
| Button Text | Sans | 600 | 11-12px | — | 0.12em | Uppercase |

**Typography Rules**:
- Serif (Cormorant Garamond) for ALL headings and display text
- Sans (DM Sans) for body copy, labels, buttons, navigation, and UI text
- Hero headlines should use italic `<em>` tags on the last word or phrase, colored coral
- Section labels follow the pattern: `01 — Section Name` in uppercase coral

### Spacing Scale

```css
:root {
  --spacing-xs:   8px;
  --spacing-sm:  16px;
  --spacing-md:  32px;
  --spacing-lg:  64px;
  --spacing-xl: 120px;
}
```

- Section padding: `var(--spacing-xl)` vertical, `40px` horizontal
- Component internal padding: `20-32px`
- Border radius: `4px` for buttons, `12px` for cards/containers

### Button System

Five button variants, all using sans font:

```css
/* All buttons share these base styles */
.btn {
  font-family: var(--font-sans);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
  display: inline-block;
}

/* Primary CTA — Coral background */
.btn-primary { background: var(--color-coral); color: #fff; padding: 14px 32px; border-radius: 4px; }

/* Outline — Charcoal border */
.btn-outline { background: transparent; color: var(--color-charcoal); padding: 13px 32px; border-radius: 4px; border: 1.5px solid var(--color-charcoal); }

/* Ghost — Coral border */
.btn-ghost { background: transparent; color: var(--color-coral); padding: 13px 24px; border-radius: 4px; border: 1.5px solid var(--color-coral); }

/* Dark — Charcoal background */
.btn-dark { background: var(--color-charcoal); color: var(--color-cream); padding: 14px 32px; border-radius: 4px; }

/* Pill — Rounded coral */
.btn-pill { background: var(--color-coral); color: #fff; padding: 12px 28px; border-radius: 100px; }
```

### Component Patterns

**NOTE**: Navigation, header, footer, and hero are part of the existing Shopify theme. Do NOT rebuild them. The patterns below are for NEW sections that drop into the page.

**Project/Industry Cards**:
- White background, 1px taupe border, 12px border-radius
- Image area with taupe-to-cream gradient placeholder
- Tag: Sans, 10px, uppercase, coral, pattern `01 — Category`
- Title: Serif, 20px, weight 500
- Description: Sans, 13px, #888
- Link: Sans, 11px, uppercase, coral, with `→` arrow

**Process Steps**:
- Cream background container
- Step number: Serif, 32px, light 300, coral at 50% opacity
- Step title: Sans, 13px, semibold, uppercase
- Step description: Sans, 12px, #888

**Contact/Audit Form**:
- Charcoal background, two-column layout
- Left: Headline (serif) + bullet points with coral dots
- Right: Form fields with translucent inputs (rgba white 6%)
- Labels: Sans, 10px, uppercase, taupe
- Submit: Full-width coral button

**Lead Capture / CTA Blocks**:
- Can be light (cream background) or dark (charcoal background)
- Compelling headline (serif) + supporting copy (sans)
- Clear single CTA button (coral primary)
- Optional: form fields for name/email/phone
- Trust signals: stats, client logos, guarantees

**Product/Service Explainers**:
- Grid or alternating layout showing product features
- Each product: image placeholder + name (serif) + description (sans) + specs
- Should make complex offerings (LED signages, ACP cladding, lightboxes) easy to understand
- End with CTA to request a quote or free audit

**Social Proof / Testimonials**:
- Client quotes with attribution
- Before/after project showcases
- Stats and numbers (serif, large) with supporting context

**FAQ / Knowledge Sections**:
- Accordion or expandable format
- Addresses common client questions to reduce friction before enquiry

### Motion & Interaction

- Use CSS transitions (0.2s ease) for hover states on buttons and links
- Subtle fade-in animations on scroll using `@keyframes` and `IntersectionObserver`
- Coral glow or subtle background shift on CTA hover
- Keep motion restrained — this is editorial/architectural, not playful
- One well-orchestrated page load with staggered reveals creates more impact than scattered micro-interactions

### Glassmorphism (Use Sparingly)

When the design calls for overlay elements, modals, or floating cards:

```css
.glass {
  background: rgba(240, 238, 233, 0.7);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(215, 203, 196, 0.3);
  border-radius: 12px;
}
```

Use glassmorphism for: floating nav on scroll, modal overlays, tooltip cards.
Do NOT overuse — it should feel like an accent, not the dominant pattern.

### Backgrounds & Atmosphere

- Subtle decorative coral circles (large, 8-12% opacity) in dark sections
- Taupe-to-cream linear gradients for image placeholders
- Fine 1px taupe borders to separate content areas
- Generous negative space — let the typography breathe
- No noise textures or grain for this brand — keep it clean

## Technical Requirements

**Stack**: Plain HTML + CSS + vanilla JavaScript. No frameworks. No build tools.

**Structure**:
- Each section is a self-contained `<section>` or `<div>` with scoped `<style>` and optional `<script>`
- NO `<html>`, `<head>`, `<body>`, `<!DOCTYPE>` wrappers — these are snippets, not pages
- NO Google Fonts `<link>` tags — fonts are already loaded by the Shopify theme
- CSS classes must be namespaced (e.g., `.sc-lead-capture__title`) to avoid theme conflicts
- Ready to paste directly into Shopify's Custom HTML section editor

**Responsive**:
- Mobile-first or desktop-first with breakpoint at 700px
- Grid layouts collapse to single column on mobile
- Hero text scales down using `clamp()`
- Touch targets minimum 44px on mobile

**Accessibility**:
- Semantic HTML (`<nav>`, `<main>`, `<section>`, `<footer>`)
- Alt text on all images
- Sufficient color contrast (coral on white passes WCAG AA for large text)
- Focus states on interactive elements
- Skip navigation link

**Performance**:
- No external JS libraries unless specifically requested
- Optimize font loading with `font-display: swap`
- Lazy load images below the fold
- Minimal DOM depth

## Reference

The full style guide with live component previews is available at `./docs/style-guide.html`. Consult it for visual reference when building components.

### Reference Pages — Learn From These Before Generating

The `./references/` folder contains 12 fully-built drop-in pages that have shipped on spacecrafter.studio. **Read the relevant reference file before generating any new section** — they encode the latest patterns, naming conventions, and copy voice.

| File | Pattern to study |
|------|------------------|
| `01-wallvocab-landing.html` | Consumer/photographic style, JSON-LD SEO, gallery slider, multi-section landing |
| `02-wallvocab-contact-whatsapp.html` | WhatsApp-routed contact section with pre-filled message |
| `03-collections-landing.html` | Collections grid, "coming soon" tiles, parent brand pattern |
| `04-office-spaces-landing.html` | Industry landing with multi-zone breakdown (11 zones) |
| `05-new-products-page.html` | Product showcase grid (LED, kiosks, video walls, hologram, interactive) |
| `06-industry-healthcare-landing.html` | **Canonical industry-landing template** — copy this structure for any new industry page |
| `07-industry-hospitality-landing.html` | Industry variant — same skeleton, different content |
| `08-led-service-landing.html` | **Canonical service-landing template** — copy this for any new service page |
| `09-service-murals.html` | Service variant — murals & custom art |
| `10-service-wayfinding.html` | Service variant — wayfinding systems |
| `11-about-us.html` | Brand story page — Aarkay 1988 → SpaceCrafter narrative voice |
| `12-contact-us.html` | Contact page with enquiry form |

**Class-name namespacing convention** (consistent across all references):

- `sc-wv-*` → WallVocab pages
- `sc-lp-*` → Industry landing pages
- `sc-ab-*` → About page
- `sc-ct-*` → Contact page
- Pick a new 2–3 letter prefix for any new page type, then keep all classes consistent within that page.

**Reusable visual signatures across references**:

- Full-bleed dark hero: `width: 100vw; left: 50%; margin-left: -50vw;` to escape Shopify's container
- Hero label pattern: `01 — LABEL` in coral, with a `::before` pseudo-element drawing a 32px coral line to the left
- Subtle blueprint or grid overlay at 4–6% opacity on dark heroes
- Coral accent circle (~500px, 4–8% opacity) positioned off-canvas top-right
- Italic emphasis (`<em>`) on the last word of every hero headline, colored coral

### Reference Images

The `./references/images/` folder contains the three canonical visual styles for hero/section imagery:

- `01-blueprint-hero-office.png` — charcoal blueprint with cream linework + coral highlights (signature look for industry/service pages)
- `02-collection-essentials.png` — photo-realistic editorial interior (warm magazine quality, used on consumer/collections)
- `03-wallvocab-hero-backdrop.png` — dissolved blueprint at low opacity (watermark-style hero backdrop)

When generating a new section, choose the matching style and reference the corresponding image style in your design.

## Anti-Patterns — NEVER Do These

- **Full page output** — never generate `<html>`, `<head>`, `<body>`, `<!DOCTYPE>`, headers, footers, or navigation
- **Font imports** — never add Google Fonts `<link>` tags; the theme already loads them
- **Unscoped CSS** — never use generic class names like `.card`, `.btn`, `.container` that will clash with Shopify theme classes; always namespace with `sc-` prefix
- Purple gradients, blue accents, or any off-palette colors
- Generic sans-serif fonts (Arial, Helvetica, Space Grotesk, Inter)
- Cookie-cutter card layouts with rounded corners and drop shadows that look "AI-generated"
- Heavy box shadows — use subtle 1px borders instead
- Centered text blocks for body copy (left-align body text)
- Stock photo placeholder images with bright colors — use taupe/cream gradient placeholders
- Animation on every element — be selective and intentional
- Framework-specific code (no React, no Tailwind classes) unless explicitly requested
- Sections without a clear purpose or CTA — every section should drive towards lead generation or product understanding
