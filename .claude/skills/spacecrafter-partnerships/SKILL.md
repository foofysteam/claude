---
name: spacecrafter-partnerships
description: Build Space Crafter Studio's outbound pipeline. Two engines. (1) PARTNERSHIP outreach to signage manufacturers, trade fabricators and branding agencies who send continuous work. (2) CLIENT outreach to South India retail, QSR, real estate, hospitals and clinics, triggered by a live project rather than a static list. Use when Akshay says "find partners", "partnership outreach", "signage companies in [country]", "branding agencies", "enrich prospects", "who is opening", "find leads", "trigger scan", "new store openings", "hospital expansions", "export markets", "which countries", or asks to draft outbound to any signage company, design agency or end client. Also triggers on "run partnerships", "outbound", "prospect list", "special design partner".
---

# Space Crafter Partnerships & Prospecting

Two engines that share one discipline. Pick the engine, then follow the rules that never bend.

---

## The one rule that matters most

**Never invent an email address.** Every address must be read off a page you actually loaded, or it does not go in the list.

This is not fussiness. It is measured. In July 2026, 14 partnership emails sent to website-verified addresses had **zero bounces**. In the same week, four end-client emails sent to pattern-guessed addresses (`firstname.surname@company.com`) **all bounced**. Same sender, same week. The only variable was verification.

A missing prospect costs nothing. A bounced email damages the sending domain for every prospect after it.

Full rules in `references/verification-rules.md`. Read that file before building any list.

---

## Engine 1 — Partnership outreach

Partners send repeat work. One good partner beats twenty cold clients.

### Who counts as a partner

| Type | What they are | Pitch variant |
|---|---|---|
| Trade-only manufacturers | Sell fabrication *to* other sign companies. Never to end users. | **B — component supply** |
| Sign companies / architectural contractors | Own the client, do survey and install, run their own floor | **A — overflow fabrication** |
| Branding agencies already selling spatial work | Advertise environmental / experience design, no shop behind it | **D — be the shop behind that line** |
| Brand identity studios | Build the brand, hand off the physical | **C — the last mile** |

Full copy for all four in `references/pitch-library.md`. Do not reuse one variant across types. A trade manufacturer told "you keep the client and the install" will bin it, because their client *is* a sign company.

### Choosing a country

Read `references/export-markets.md` before proposing any market. It contains verified trade-agreement status as of August 2026 and, more usefully, the reasons tariffs are usually **not** the deciding factor.

The short version, so this file stands alone:

- **UAE** is the best market. India–UAE CEPA took 5% to 0%, the fit-out pipeline is enormous, freight is cheap, English works.
- **UK** went duty-free on 15 July 2026 under India–UK CETA. Very recent — most exporters have not repriced yet.
- **Australia** is fully duty-free from 1 January 2026. Small market, long freight.
- **Switzerland/EFTA gives no advantage** — Switzerland zero-rated all industrial goods for everyone in Jan 2024.
- **Japan and Singapore give no advantage** — already 0% MFN on signage codes for everyone.
- **Saudi and wider GCC have no FTA yet** and are still worth pursuing. The 5% duty is not the barrier; local content rules are.

**Correct anyone, including Akshay, who assumes duty is the constraint.** For fabricated signage the binding constraints are freight cube, local install licensing, and electrical certification. Say so plainly.

### Running the engine

1. **Check Notion first.** Query "International Signage Companies" and the campaign databases under *Spacecrafter Prospecting Lists*. Do not re-research what exists.
2. **Distrust inherited lists.** DNS-check every domain before using a list you did not build. The "London Signage Manufacturers" database in this workspace has 81 rows and **55 of the domains have never been registered**. Details in `references/verification-rules.md`.
3. **Research.** Fan out subagents by region or category. Require every returned company to have had its website successfully loaded.
4. **Classify** each into one of the four partner types. That picks the variant.
5. **Personalise the opener.** One or two sentences naming something specific and true: a client, a certification, a factory size, a service line, a second facility. Generic openers are worse than none.
6. **Draft to Gmail.** Never send. Akshay sends.
7. **Log to Notion**, build the tracker artifact, report honestly.

---

## Engine 2 — South India client outreach

Retail, QSR, real estate, hospitals, clinics. Bangalore, Chennai, Hyderabad, Kochi, Coimbatore.

### Trigger-based only

Do not build "every hospital in Karnataka" lists. They are cold, enormous and mostly ignored.

Prospect on a **live reason** instead: a company with a project happening right now that will need signage in the next two to six months. The full trigger set, sources and timing windows are in `references/trigger-playbook.md`.

The timing rule that governs everything: **signage gets specified during fit-out, roughly two to four months before opening.** Too early and there is no budget line yet. Too late and someone else has quoted. Aim at projects where the structure is up and the interiors are not finished.

### The client pitch

Different from the partner pitch. A client does not care about your capacity. They care that the thing opens on time and looks like the brand.

The frame Akshay uses: **they build the brand ethos and the core, Space Crafter creates the artifacts that make it experienceable.** Lead with the specific project you spotted, not with the company profile.

Template and worked examples in `references/pitch-library.md` under "Variant E".

### Contacts for end clients

The role, by sector:

- **Hospitals / clinics** — Facility Director, Head of Projects, Head of Infrastructure. Marketing owns the brand but not the build.
- **Retail** — VP Retail Expansion, Head of Projects, Store Development Manager
- **QSR** — Development Manager, Head of New Openings, franchise partner for the region
- **Real estate** — Project Head for that specific development, Head of Marketing for the pre-launch phase

Find these people by name, then find their address on a real page. **If you cannot verify the address, route to the corporate or projects inbox published on the site and ask for the person by name in the body.** That is exactly how the partnership emails reached named directors without a single bounce.

---

## Output, every time

1. **Gmail drafts** — one per prospect, personalised. Never send.
2. **Notion database** under *Spacecrafter Prospecting Lists* — email, source URL, tier, variant, named contact, why-this-fit, hook used, follow-up date.
3. **HTML tracker artifact** — filterable, full email body per row, copy button, delivered with SendUserFile.
4. **An honest report.** Name the weak prospects. Name what could not be verified. Name the ones that need a phone call instead.

### Send pacing

Cold email from one address has a practical ceiling. Five or six a day is safe; twenty in an hour is a spam signal. Always propose a dated calendar rather than handing over a pile. Follow up once, about a week out, in two lines with no new pitch — most cold B2B replies come off the follow-up rather than the first email.

---

## Voice

Follow the `space-crafter-studio` skill for tone. In short: specific over generic, premium but human, short sentences that land. No em dashes. Never use *elevate, stunning, innovative, world-class, transform your space, one-stop solution*.

Two things that make this copy work and are easy to lose:

- **Concede something.** "Your plastics capability is deeper than ours." "We would not improve on your deep-draw tooling." A cold email that admits a limit is read as honest, and the rest of it gets believed.
- **Give them an exit.** "If the numbers do not work, you will know inside that call." Removes the pressure that makes people ignore cold mail.

---

## Never

- Invent, pattern-guess or reconstruct an email address from a masked directory listing
- Send anything. Draft only.
- Reuse a pitch variant across partner types
- Trust an inherited prospect list without DNS-checking it
- Claim a duty rate, market size or client relationship that has not been verified on a real source
- Report a list as complete when part of it could not be verified
