# Website Build Instructions — [BUSINESS NAME]

Use this document as the full brief for building a static website. Follow it exactly; where something isn't specified, make a sensible default choice and note the assumption at the end of your response.

---

## 1. Project Overview

- **Business name:** [e.g. "Coastal Bloom Florist"]
- **Industry / what the business does:** [e.g. "Boutique florist offering arrangements, weddings, and subscriptions"]
- **Location:** [e.g. "Torquay, Victoria, Australia"]
- **Target customer:** [e.g. "Locals booking flowers for events and gifts"]
- **Primary goal of the site:** [e.g. "Showcase work, build trust, capture enquiries via a contact form"]
- **Tone/voice:** [e.g. "Warm, elegant, understated — not corporate"]

## 2. Technical Requirements

- Output as a **single static HTML file** (`index.html`), with CSS and JS inline or in the same file unless told otherwise.
- Must be **deployable to Netlify** with zero configuration (no build step, no backend, no npm install required).
- The contact form at the bottom must use **Netlify Forms**. Requirements for this:
  - Add `data-netlify="true"` and a `name` attribute to the `<form>` tag.
  - Include a hidden input: `<input type="hidden" name="form-name" value="[form-name]" />`
  - Include a honeypot field for spam protection (`data-netlify-honeypot="bot-field"`).
  - Do NOT use a JS `fetch`/`onSubmit` handler unless I ask for an AJAX success message — default to a plain HTML form so Netlify can detect it at build time.
  - Remind me in your reply that Netlify Forms only get detected on the **first deploy**, and that I need to check the Netlify dashboard (Forms tab) to see submissions or set up email notifications.
- Site must be **fully responsive** (mobile, tablet, desktop).
- No external frameworks/build tools (no React, no Tailwind CDN dependency issues) — plain HTML/CSS/JS only, unless I explicitly ask for something else.
- Use semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`, etc.) for accessibility and SEO.
- Include basic on-page SEO: `<title>`, meta description, Open Graph tags, favicon placeholder.
- Optimise for fast load: no heavy libraries, compressed/placeholder images, minimal render-blocking scripts.

## 3. Pages / Sections

(Since this is a single-page static site, list sections in order. Delete/add as needed.)

1. **Header/Nav** — logo/business name, nav links (anchor-linked to sections below), possibly a phone number or "Get a Quote" button.
2. **Hero section** — headline, subheadline, primary call-to-action button.
3. **About section** — short business story, what makes it different.
4. **Services/Products section** — [list what should appear, e.g. "3–5 service cards with icon, title, short description"].
5. **Testimonials/Social proof** (optional) — [quotes, star ratings, or logos].
6. **Gallery/Portfolio** (optional) — [describe what images/content should go here].
7. **FAQ** (optional) — [list common questions if known].
8. **Contact/Enquiry form section** (see Section 4 below).
9. **Footer** — business hours, ABN (if applicable), social links, address, copyright.

## 4. Contact Form Fields

List exactly what fields the form should capture:

- Name (required)
- Email (required)
- Phone (optional/required — specify)
- Message (required)
- [Add any business-specific fields, e.g. "Preferred appointment date", "Event type"]

Confirmation behaviour: [e.g. "Redirect to a simple thank-you message on the same page" or "Redirect to /thank-you.html"]

## 5. Design & Branding

- **Colour palette:** [hex codes if known, or descriptive e.g. "sage green, cream, charcoal"]
- **Fonts:** [e.g. "A modern serif for headings, clean sans-serif for body — Google Fonts only"]
- **Logo:** [attach if available, otherwise "use business name as text logo"]
- **Imagery style:** [e.g. "warm natural photography" / "use placeholder image blocks with labelled alt text if no real images supplied"]
- **Reference sites** (optional): [links to sites whose look/feel you like]

## 6. Australian Business Compliance/Content Notes

- Include ABN in the footer if provided: [ABN number or "N/A"]
- Use Australian English spelling (colour, organisation, etc.)
- Use Australian date format (DD/MM/YYYY) and phone format (e.g. 04XX XXX XXX)
- Currency in AUD ($) if prices are shown
- Include a simple privacy note near the form if collecting personal data (e.g. "Your details are only used to respond to your enquiry")

## 7. Content Supplied

Paste or attach any existing copy, images, testimonials, or business details here so the LLM doesn't have to invent facts:

```
[Paste business description, service list, pricing, testimonials, opening hours, address, socials, etc.]
```

## 8. Deployment Notes

- Final file(s) should be ready to drag-and-drop into Netlify or push via a connected Git repo.
- If multiple files are needed (e.g. separate CSS/JS, or a `thank-you.html`), keep the folder structure flat and clearly named.
- Remind me of the steps to deploy: drag the folder into Netlify's "Deploys" tab, or connect a GitHub repo.

---

### Instructions to the LLM

Build the site described above as a single, complete, production-ready `index.html` file (plus any additional files only if necessary). Do not use placeholder lorem ipsum for anything I've provided real content for — only use clearly-labelled placeholders where I haven't supplied content. At the end, tell me:
1. Any assumptions you made.
2. What I still need to supply (images, copy, ABN, etc.).
3. The steps to deploy this to Netlify and confirm the form is working.
