# SpaceCrafter Landing Page - Shopify Implementation Guide

## 📦 Files Provided

```
shopify-integration/
├── sections/
│   └── spacecrafter-landing.liquid    (Main section file)
├── assets/
│   ├── spacecrafter-landing.css       (Styles)
│   └── spacecrafter-landing.js        (JavaScript)
└── SHOPIFY-IMPLEMENTATION-GUIDE.md    (This file)
```

---

## 🚀 Quick Installation (5 Steps)

### Step 1: Access Your Shopify Theme Files

1. Log in to your Shopify Admin
2. Go to **Online Store** → **Themes**
3. Click **Actions** → **Edit code** on your live/active theme

### Step 2: Upload the Section File

1. In the left sidebar, find the **Sections** folder
2. Click **Add a new section**
3. Name it: `spacecrafter-landing`
4. Copy the entire contents of `sections/spacecrafter-landing.liquid`
5. Paste into the editor
6. Click **Save**

### Step 3: Upload CSS File

1. In the left sidebar, find the **Assets** folder
2. Click **Add a new asset** → **Upload files**
3. Upload `assets/spacecrafter-landing.css`
4. Click **Save**

OR manually create:
1. Click **Add a new asset** → **Create a blank file**
2. Choose CSS file type
3. Name it: `spacecrafter-landing.css`
4. Copy contents from `assets/spacecrafter-landing.css`
5. Paste and **Save**

### Step 4: Upload JavaScript File

1. In the **Assets** folder
2. Click **Add a new asset** → **Upload files**
3. Upload `assets/spacecrafter-landing.js`
4. Click **Save**

OR manually create:
1. Click **Add a new asset** → **Create a blank file**
2. Choose JavaScript file type
3. Name it: `spacecrafter-landing.js`
4. Copy contents from `assets/spacecrafter-landing.js`
5. Paste and **Save**

### Step 5: Create a New Page

#### Option A: Create via Shopify Admin (Recommended)

1. Go to **Online Store** → **Pages**
2. Click **Add page**
3. Title: "Home" or "Coworking Solutions" (your choice)
4. In the page editor, look for **Theme template** dropdown
5. If you don't see the option, you'll need to create a custom template (see Option B)

#### Option B: Create Custom Page Template

1. In theme code editor, find **Templates** folder
2. Click **Add a new template**
3. Select **page** from dropdown
4. Name it: `page.spacecrafter`
5. Paste this code:

```liquid
{% section 'spacecrafter-landing' %}
```

6. **Save**
7. Now go to **Online Store** → **Pages** → **Add page**
8. Create your page
9. In **Theme template** dropdown, select **page.spacecrafter**
10. **Save**

---

## ⚙️ Configuration & Customization

### Editing Content in Shopify Theme Editor

1. Go to **Online Store** → **Themes**
2. Click **Customize** on your active theme
3. Navigate to the page where you added the section
4. Click on the **SpaceCrafter Landing** section
5. You'll see all editable fields in the right sidebar:

#### Available Settings:

**Hero Section:**
- Hero Title
- Hero Title Highlight (the gradient text)
- Hero Subtitle
- Hero Image (upload your coworking space photo)
- Primary CTA Text & URL
- Secondary CTA Text

**Statistics (Blocks):**
- Add "Hero Stat" blocks
- Set number and label for each stat

**Trusted By:**
- Title text
- Add "Client Logo" blocks
- Upload logo images or enter client names

**Services:**
- Section labels and titles
- Add "Service Card" blocks
- Icon (use emojis like 🎨, 📊, 🛠️)
- Title, description, features
- Mark as featured (optional)

**Process Steps:**
- Add "Process Step" blocks
- Enter title, description, duration

**Case Studies:**
- Add "Case Study" blocks
- Upload images
- Client name, project title, description
- 3 metrics per case study

**Testimonials:**
- Add "Testimonial" blocks
- Quote, author name, author title

**CTA Form:**
- CTA title and subtitle
- Button text
- Privacy text

### Adding Your Content

1. **Upload Images First:**
   - Go to **Settings** → **Files** in Shopify Admin
   - Upload all your images (hero, case studies, logos)
   - Or upload directly in Theme Customizer when configuring

2. **Configure Blocks:**
   - In Theme Customizer, click **Add block**
   - Choose block type (Stat, Service, Client Logo, etc.)
   - Fill in the fields
   - Reorder by dragging blocks up/down
   - Delete unwanted blocks with trash icon

3. **Preview Changes:**
   - Click **Preview** button to see live preview
   - Test on different devices (desktop/mobile toggle)

4. **Publish:**
   - Click **Save** when satisfied
   - Your changes are live!

---

## 🎨 Pre-Populated Content Template

Here's a JSON you can use to quickly populate content via Shopify's section settings:

### Recommended Block Structure:

**Hero Stats (3 blocks):**
1. Stat: "50+" - "Spaces Designed"
2. Stat: "15K+" - "Happy Members"
3. Stat: "35%" - "Avg. Utilization Increase"

**Client Logos (5 blocks):**
1. WeWork
2. Canvas
3. Aurbis
4. Hanto
5. Table Space

**Services (6 blocks):**
1. 🎨 Interior Design
2. 📊 Space Optimization (Featured)
3. 🛠️ Renovation & Build-Out
4. ♻️ Space Refresh
5. 🌱 Sustainability Consulting
6. 🔧 Furniture & FF&E

**Process Steps (5 blocks):**
1. Discovery & Analysis - Week 1
2. Concept Development - Weeks 2-3
3. Design Development - Weeks 4-6
4. Implementation - Weeks 7-11
5. Launch & Support - Week 12+

**Case Studies (3 blocks):**
1. WeWork - Downtown Hub Redesign
2. Canvas - Multi-Location Standardization
3. Table Space - Sustainable Space Transformation

**Testimonials (3 blocks):**
1. Sarah Chen, VP of Operations, WeWork
2. Michael Rodriguez, Founder & CEO, Canvas
3. Emma Thompson, Sustainability Director, Table Space

---

## 📱 Setting as Homepage

To make this your store's homepage:

### Method 1: Via Admin

1. Go to **Online Store** → **Themes**
2. Click **Customize**
3. Use the page selector at top to switch to "Home page"
4. Click **Add section**
5. Select **SpaceCrafter Landing**
6. Configure and **Save**

### Method 2: Via Custom Template

1. In theme code, go to **Templates**
2. Edit `index.json` or `index.liquid`
3. If `.json`:
```json
{
  "sections": {
    "spacecrafter_landing": {
      "type": "spacecrafter-landing"
    }
  },
  "order": [
    "spacecrafter_landing"
  ]
}
```

4. If `.liquid`, add:
```liquid
{% section 'spacecrafter-landing' %}
```

---

## 🔧 Advanced Customization

### Connecting Form to Email

The form uses Shopify's native contact form. To receive submissions:

1. Go to **Settings** → **Notifications**
2. Find **Customer contact** notification
3. Set recipient email
4. Customize email template if needed

### Adding Google Analytics Tracking

Form submissions automatically trigger Shopify analytics. For additional tracking:

1. Go to **Settings** → **Analytics**
2. Add Google Analytics tracking ID
3. Events are auto-tracked

### Modifying Colors

To change brand colors, edit the CSS file:

1. Go to **Assets** → `spacecrafter-landing.css`
2. Find the CSS variables at the top:
```css
--sc-primary: #2563eb;       /* Main blue */
--sc-secondary: #8b5cf6;     /* Purple */
--sc-accent: #06b6d4;        /* Cyan */
```
3. Replace with your brand colors
4. **Save**

### Removing/Hiding Sections

In Theme Customizer:
1. Click on section you want to hide
2. Scroll to bottom of settings
3. Toggle visibility or delete section

---

## 🖼️ Image Specifications

| Location | Dimensions | Format | Notes |
|----------|-----------|--------|-------|
| Hero Image | 1200x900px | JPG/PNG | High quality, bright |
| Client Logos | 200x80px | PNG/SVG | Transparent background |
| Case Study Images | 1600x1000px | JPG | Professional photography |

**Image Optimization:**
- Compress images before uploading (use TinyPNG or Squoosh)
- Max file size: 500KB per image
- Use WebP format for better performance (Shopify auto-converts)

---

## 📋 Pre-Launch Checklist

- [ ] All 3 files uploaded to theme
- [ ] Page created with custom template
- [ ] Hero section configured with title and image
- [ ] All 3 hero stats added
- [ ] 5 client logos added (or removed if not ready)
- [ ] 6 service cards configured
- [ ] 5 process steps added
- [ ] 3 case studies with images and metrics
- [ ] 3 testimonials added
- [ ] CTA section text updated
- [ ] Form tested (submit test entry)
- [ ] Mobile view tested in Theme Customizer
- [ ] Desktop view tested
- [ ] Page published and live

---

## 🐛 Troubleshooting

### Form Not Submitting

**Issue:** Form doesn't send emails

**Solution:**
1. Ensure form template uses `{% form 'contact' %}`
2. Check **Settings** → **Notifications** → **Customer contact** is enabled
3. Verify email address is correct
4. Check spam folder

### Images Not Displaying

**Issue:** Placeholders still showing

**Solution:**
1. In Theme Customizer, click section
2. Click on image field
3. Click **Select image** → **Upload** or choose from library
4. Must click **Save** after uploading

### Section Not Appearing

**Issue:** Can't find section in Theme Customizer

**Solution:**
1. Ensure file is named exactly: `spacecrafter-landing.liquid`
2. Must be in **Sections** folder, not Templates
3. Click **Save** after creating
4. Refresh Theme Customizer page
5. Check for Liquid syntax errors in code editor

### Styling Looks Broken

**Issue:** CSS not loading properly

**Solution:**
1. Verify CSS filename: `spacecrafter-landing.css` (exact)
2. Check file is in **Assets** folder
3. Clear browser cache (Ctrl+Shift+R / Cmd+Shift+R)
4. Check for CSS syntax errors
5. Ensure Liquid file has: `{{ 'spacecrafter-landing.css' | asset_url | stylesheet_tag }}`

### JavaScript Not Working

**Issue:** Animations or smooth scroll not working

**Solution:**
1. Verify JS filename: `spacecrafter-landing.js` (exact)
2. Check file is in **Assets** folder
3. Clear browser cache
4. Check browser console for errors (F12)
5. Ensure Liquid file has: `{{ 'spacecrafter-landing.js' | asset_url | script_tag }}`

---

## 🔐 Best Practices

### Performance
- Compress all images before upload
- Use lazy loading (built-in)
- Limit to 3-5 case studies max
- Keep testimonials to 3-6 items

### SEO
- Add page title and meta description in page settings
- Use descriptive alt text for all images
- Ensure heading hierarchy (H1 → H2 → H3)

### Mobile
- Test thoroughly on mobile devices
- Ensure touch targets are 44x44px minimum
- Check text readability on small screens

### Accessibility
- Provide alt text for all images
- Ensure color contrast meets WCAG standards
- Test keyboard navigation

---

## 📞 Support Contact

If you encounter issues:

1. Check Shopify's theme documentation
2. Review Liquid syntax reference
3. Test in incognito mode (rule out caching)
4. Check browser console for errors
5. Contact your dev team with specific error messages

---

## 🎯 Quick Reference Links

**Shopify Docs:**
- [Sections](https://shopify.dev/docs/themes/architecture/sections)
- [Liquid Reference](https://shopify.dev/docs/api/liquid)
- [Theme Customizer](https://help.shopify.com/en/manual/online-store/themes/customizing-themes)

**Testing:**
- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- [PageSpeed Insights](https://pagespeed.web.dev/)

---

## ✅ Success!

Once installed, your landing page will:
- ✨ Look professional and modern
- 📱 Work perfectly on all devices
- 🚀 Load quickly
- 🎨 Be fully customizable via Theme Editor
- 📝 Collect leads via native Shopify forms
- 🔒 Be secure and GDPR compliant

Your engineering team can complete this installation in **15-30 minutes**.

---

**Last Updated:** 2026-01-13
**Version:** 1.0
**Compatibility:** Shopify OS 2.0+ themes
