# SpaceCrafter Landing Page - Quick Start for Engineers

## ⚡ 15-Minute Installation

### What You're Installing
A complete coworking space landing page with:
- Hero section with stats
- Client logos (WeWork, Canvas, etc.)
- 6 service cards
- Process timeline
- Case studies with metrics
- Testimonials
- Contact form (uses Shopify native form)

---

## 🎯 Installation Steps

### 1️⃣ Upload Section File (Main Component)

**Location:** `Sections` folder
**Filename:** `spacecrafter-landing.liquid`
**File:** `sections/spacecrafter-landing.liquid`

1. In Shopify Admin → Online Store → Themes → Edit code
2. Click "Add a new section"
3. Name it: `spacecrafter-landing`
4. Copy-paste entire contents from provided file
5. Save

---

### 2️⃣ Upload CSS File (Styling)

**Location:** `Assets` folder
**Filename:** `spacecrafter-landing.css`
**File:** `assets/spacecrafter-landing.css`

**Method A - Upload:**
1. Assets folder → Add a new asset → Upload files
2. Select `spacecrafter-landing.css`
3. Done

**Method B - Manual:**
1. Assets folder → Add a new asset → Create blank file
2. Choose CSS
3. Name: `spacecrafter-landing.css`
4. Copy-paste entire CSS file contents
5. Save

---

### 3️⃣ Upload JS File (Interactions)

**Location:** `Assets` folder
**Filename:** `spacecrafter-landing.js`
**File:** `assets/spacecrafter-landing.js`

Same process as CSS:
1. Upload file OR create blank file
2. Name: `spacecrafter-landing.js`
3. Copy-paste contents
4. Save

---

### 4️⃣ Create Page Template

**Location:** `Templates` folder
**Filename:** `page.spacecrafter.json`

1. Templates folder → Add a new template
2. Select "page" type
3. Name it: `page.spacecrafter`
4. Paste this JSON:

```json
{
  "sections": {
    "main": {
      "type": "spacecrafter-landing"
    }
  },
  "order": [
    "main"
  ]
}
```

5. Save

**Alternative for .liquid themes:**
Create `page.spacecrafter.liquid` with:

```liquid
{% section 'spacecrafter-landing' %}
```

---

### 5️⃣ Create the Page

1. Go to: **Online Store → Pages**
2. Click: **Add page**
3. Page title: "Coworking Solutions" (or your preference)
4. Leave content empty (section handles everything)
5. **Theme template** dropdown: Select `page.spacecrafter`
6. Click: **Save**
7. Note the page URL (e.g., `/pages/coworking-solutions`)

---

## 🎨 Configure Content

### Via Theme Customizer (No Code)

1. **Online Store → Themes → Customize**
2. Navigate to your new page using page selector
3. Click on **SpaceCrafter Landing** section
4. Right sidebar shows all editable fields

### Must Configure:

**Minimum Required:**
- [ ] Hero title and subtitle
- [ ] Upload hero image
- [ ] Add 3 stat blocks
- [ ] Add 5 client logo blocks
- [ ] Add 6 service blocks
- [ ] Add 5 process step blocks
- [ ] Add 3 case study blocks
- [ ] Add 3 testimonial blocks

**Example Hero Setup:**
```
Hero Title: "Design Coworking Spaces That"
Hero Highlight: "Inspire & Perform"
Hero Subtitle: "Transform your workspace into a thriving community hub..."
```

---

## 📸 Image Requirements

Upload these via **Settings → Files** or directly in customizer:

| Image Type | Size | Count | Notes |
|------------|------|-------|-------|
| Hero | 1200x900px | 1 | Modern coworking space |
| Client Logos | 200x80px | 5 | PNG with transparency |
| Case Studies | 1600x1000px | 3 | Before/after or interiors |

**Quick Image Sources:**
- Unsplash: Search "coworking space"
- Pexels: Search "modern office"
- Your own photography

---

## 🧪 Testing Checklist

After installation, test:

- [ ] Page loads without errors
- [ ] All images display correctly
- [ ] Form submission works (test with real email)
- [ ] Mobile responsive (toggle in customizer)
- [ ] Smooth scrolling works on anchor links
- [ ] All CTAs link to correct destinations
- [ ] Console has no JavaScript errors (F12)

---

## 🔗 Setting as Homepage (Optional)

To make this your main page:

**Method 1 - Navigation:**
1. **Online Store → Navigation**
2. Edit main menu
3. Add link to your new page
4. Drag to top position

**Method 2 - As Actual Homepage:**
1. **Online Store → Preferences**
2. Scroll to "Homepage"
3. Cannot set custom pages as homepage directly
4. Alternative: Edit `index.json` in Templates:

```json
{
  "sections": {
    "spacecrafter": {
      "type": "spacecrafter-landing"
    }
  },
  "order": [
    "spacecrafter"
  ]
}
```

---

## 🎨 Brand Color Customization

To match your brand:

1. Edit: `assets/spacecrafter-landing.css`
2. Find line ~11-17:
```css
--sc-primary: #2563eb;       /* Change to your primary color */
--sc-secondary: #8b5cf6;     /* Change to your secondary */
--sc-accent: #06b6d4;        /* Change to your accent */
```
3. Replace hex codes
4. Save

---

## 🔧 Form Email Setup

Form submissions go to:

1. **Settings → Notifications**
2. Find: **Customer contact**
3. Set email recipient
4. Emails sent automatically on form submit

---

## ❗ Common Issues & Fixes

### "Section doesn't appear"
- File must be named exactly: `spacecrafter-landing.liquid`
- Must be in Sections folder
- Click Save and refresh customizer

### "Styles look broken"
- Verify CSS filename: `spacecrafter-landing.css`
- Check it's in Assets folder
- Hard refresh browser (Ctrl+Shift+R)

### "Form not sending"
- Check Settings → Notifications → Customer contact
- Verify email address
- Test in incognito mode
- Check spam folder

### "Images not showing"
- Upload images first to Settings → Files
- Then select in theme customizer
- Must click Save after selecting

---

## 📦 File Structure Summary

```
Your Shopify Theme/
├── sections/
│   └── spacecrafter-landing.liquid      ← Main component
├── assets/
│   ├── spacecrafter-landing.css         ← Styling
│   └── spacecrafter-landing.js          ← Functionality
└── templates/
    └── page.spacecrafter.json           ← Page template
```

---

## 🚀 Deploy Checklist

Before going live:

- [ ] All 3 files uploaded and saved
- [ ] Page template created
- [ ] Page created with correct template
- [ ] Content configured in customizer
- [ ] All images uploaded and displaying
- [ ] Form tested with real submission
- [ ] Mobile view checked
- [ ] Desktop view checked
- [ ] Links verified
- [ ] Spelling/grammar reviewed
- [ ] Client logos have permission for use
- [ ] Page published (not draft)

---

## 📊 Performance Tips

**Before Launch:**
1. Compress all images with [TinyPNG](https://tinypng.com)
2. Keep hero image under 300KB
3. Limit case studies to 3-4 max
4. Use WebP format when possible

**After Launch:**
1. Test with [PageSpeed Insights](https://pagespeed.web.dev)
2. Aim for 90+ mobile score
3. Check [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)

---

## 💡 Pro Tips

1. **Duplicate Before Editing:** In theme code, duplicate section before major changes
2. **Use Version Control:** Save backups of working versions
3. **Test in Development Theme:** Use a duplicate theme for testing first
4. **Preview Before Publishing:** Always preview changes before saving live
5. **Mobile First:** Configure mobile view first, then desktop

---

## 📞 Need Help?

**Check:**
1. Shopify theme documentation
2. Browser console (F12) for errors
3. Liquid syntax errors in code editor
4. This guide's troubleshooting section

**Debug Mode:**
- Add `?preview_theme_id=THEME_ID` to URL
- Check console for errors
- Validate Liquid syntax

---

## ✅ Installation Complete!

**Time to complete:** 15-30 minutes
**Result:** Professional coworking landing page
**Editable:** 100% through Shopify admin (no code required after install)
**Mobile:** Fully responsive
**Form:** Integrated with Shopify

---

**Questions?** Share this guide with your team or refer to SHOPIFY-IMPLEMENTATION-GUIDE.md for detailed documentation.

**Version:** 1.0
**Date:** 2026-01-13
**Compatibility:** Shopify OS 2.0+ themes
