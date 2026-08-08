# Verification rules

The discipline that produced a zero-bounce campaign. Read before building any list.

---

## The evidence

Two campaigns, same sender, same week of July 2026.

| Campaign | Address sourcing | Result |
|---|---|---|
| 14 Australian signage companies | Every address read off the company's own website | **0 bounces** |
| 4 South India end clients | Addresses constructed as `firstname.surname@company.com` | **4 bounces** |

Bounced: `aditya.kumar@godrejagrovet.com`, `manu.das@medibuddy.in`, `vidushi.jain@smartenspaces.com`, `superintndentgngh@yahoo.com`. All returned "Address not found."

One of the verified addresses came from a third-party directory rather than the company's own site and was flagged as risky in the tracker. It delivered fine. The rule is not "only first-party" — it is "only real pages."

---

## Rule 1 — Read it, don't build it

An address goes in the list only if it appeared on a page that loaded successfully.

**Acceptable sources**, in order of confidence:

1. The company's own contact, about or team page
2. Another page on their own domain (terms of service and privacy pages often carry an address the contact page hides)
3. An industry association or trade directory listing
4. A government or registry record

**Never acceptable:**

- Constructing `firstname@`, `firstname.surname@`, `info@` or `sales@` because it "usually works"
- Reconstructing from a masked listing. `p***@ultrasigns.com.au` on a data-broker site is not a source.
- Copying from a paid enrichment tool without confirming on a real page
- Inferring from one branch's address that another branch follows the same pattern

Record the exact source URL for every address. Put it in the Notion row. When something bounces later you need to know where it came from.

---

## Rule 2 — DNS-check every inherited list

Before using any list you did not personally build, confirm the domains exist.

This is a name lookup, not a page fetch:

```python
import socket
try:
    socket.getaddrinfo(domain, 443)
    # resolves - domain is registered
except Exception:
    # does not resolve - the domain has never existed
```

**Why this exists.** The "London Signage Manufacturers" database in this Notion workspace has 81 rows. **55 of those domains do not resolve.** Not expired — never registered.

The tell was the naming pattern: one company per London borough (Croydon Sign Makers, Bromley Signs, Kingston Signage, Wimbledon Display Works, Hackney Sign Co, Greenwich Sign Works) and one per Liverpool specialism (Liverpool LED Signs, Liverpool Safety Signs, Liverpool Wayfinding Solutions, Liverpool Fabrication Co). Formulaic, exhaustive, and fake.

**Watch for that shape.** A list that covers every borough or every specialism with perfect symmetry was generated, not researched. Real markets are lumpy.

Of the 24 that did resolve, several were still wrong: an art-supplies retailer, a US 3D-printing bureau, a parked domain. **Resolving is necessary, not sufficient.** Load the site.

---

## Rule 3 — Recovering hidden addresses

Many firms hide addresses deliberately. Trade-only manufacturers do it to keep end users out. Indian agencies do it as standard.

**Cloudflare email protection** encodes the address in a `data-cfemail` hex attribute. It can be decoded in a browser:

```javascript
document.querySelectorAll('[data-cfemail]').forEach(el => {
  const s = el.getAttribute('data-cfemail');
  const k = parseInt(s.substr(0,2),16);
  let out = '';
  for (let i=2; i<s.length; i+=2)
    out += String.fromCharCode(parseInt(s.substr(i,2),16) ^ k);
  console.log(out);
});
```

This recovered Orange Signs and Ultra Signs in the Australia campaign, including a named owner's direct address.

**Order of attempts:**

1. WebFetch the contact page
2. WebFetch other pages on the domain — terms, privacy, about, a specific service page
3. Load in the browser and decode obfuscation
4. Check association directories and trade press
5. **Stop.** Log it as phone-only with the number and any named contact.

Do not spend more than a few minutes per company. A phone call is a better first touch for a partnership anyway, and for trade-only firms it is often the *intended* route.

---

## Rule 4 — Say what you could not verify

Every deliverable states plainly:

- Which addresses came from third parties rather than the company's own site
- Which companies could not be reached at all, and what to do instead
- Which named contacts came from LinkedIn or a directory rather than the company's own pages
- Anything that looked wrong

**Real example worth repeating.** One Hyderabad agency's About page listed "Sarah Miller, Art Director" and "Alex Carter, CTO" — template placeholder names left unedited on an Indian agency site. That was flagged, the agency was held back from the send list, and Akshay was told to verify the business was real before approaching. Never use a name you have not seen on a real page you loaded.

---

## Rule 5 — Deduplicate across campaigns

Before drafting, check every address against every prior campaign database in Notion. The same company appears under different names — Bromley Signs trades on `.com` while an old list recorded `.co.uk`; Mersey Signs moved from `.co.uk` to `.com`.

Two emails from the same sender to the same company in a month reads as spam, not persistence.

---

## Quick checklist

- [ ] Every domain resolves
- [ ] Every website loaded successfully
- [ ] Every address read off a real page, with the URL recorded
- [ ] No constructed or pattern-guessed addresses anywhere
- [ ] Deduplicated against all prior campaigns
- [ ] Unreachable companies logged with phone and named contact
- [ ] Unverified items flagged explicitly in the report
