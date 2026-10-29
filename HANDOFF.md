# Handoff: Benchside marketing site → fitlink repo

**For:** the FitLink team (web)
**From:** Victor
**Date:** 29 October 2026

## Goal

Replace the FitLink-branded marketing pages in the `fitlink` repo (Vite app on Vercel, serving
benchside.coach and fitlink.coach) with the Benchside design in this folder. This folder is the
reference implementation: static HTML, `assets/site.css`, `assets/site.js`. Port it into the app's
components; match it visually and keep every route the app already serves.

Nothing here talks to the backend. All app behavior stays where it is.

## Routes

| Route | Source in this folder | Notes |
| --- | --- | --- |
| `/` | `index.html` | Coaches first |
| `/pricing` | `pricing.html` | Includes the keep-calculator (logic in `site.js`, section "Pricing calculator") |
| `/athletes` | `athletes.html` | For people arriving from a coach's link |
| `/support` | `support.html` | Help center: search, grouped FAQ, contact form that opens a `mailto:` |
| `/privacy` | `privacy.html` | Benchside version, see "Legal changes" |
| `/terms` | `terms.html` | Benchside version, see "Legal changes" |
| 404 | `404.html` | "Rest day" |

**Keep as they are (owned by the app, not this site):** `/coach` and everything under it
(incl. `/coach/earnings`), `/c/<handle>` coach pages and web checkout, `/founding`,
`/delete-account`, `/admin`, Stripe return URLs, the PWA service worker.
This folder links to those with absolute `https://benchside.coach/...` URLs so the preview works;
make them relative when porting.

## Design system

- Tokens are CSS custom properties at the top of `assets/site.css` (ground `#F4F4F2`, ink
  `#160A3D`, violet `#6C3BFF`, lime `#D7FF3A`, hairline `#E3E1E8`, etc.).
- Headlines: Archivo 800 at `font-stretch: 72%`, uppercase, line-height 0.88. Self-hosted variable
  font in `assets/fonts/archivo-var.woff2` (wght 100–900, wdth 62–125, OFL). Body: system font stack.
- Lime is a signal only: the dot, the final CTA button on violet, small badges. Never on a light
  background (about 1:1 contrast).
- Components: sticky header with blur + mobile sheet menu, hero with two overlapping phones,
  `.phone` frame (CSS only, sized by `--w`), numbered steps band, feature rows (`.feature`,
  `.flip`), fee receipt card, sideways screens row, numbered trust list, plan cards
  (`.plan`, `.plan.featured`), calculator, `<details>` FAQ, final CTA with phone, footer.
- Motion: one fade-up on scroll (`.reveal`), only when JS runs and only without
  `prefers-reduced-motion`.
- Accessibility: axe-core (WCAG 2.1 AA + best practice) passes on every page at 1280 px and 390 px.
  Skip link, visible focus rings, 44 px targets, the sideways screens row is keyboard-focusable.

## Assets

- `assets/screens/*.webp` are rendered from the Benchside design canvas at 2x (780 × 1688).
  Replace them with real screenshots when the shipped UI is final. The coach-page image uses a
  barbell illustration in place of a coach photo; real coach pages use the coach's photo.
- `og-image.png` (1200 × 630), `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`,
  `icon-512.png`, `site.webmanifest`.
- `assets/brand/` wordmarks and app icon are outlined vectors from the logo kit.

## Copy changes from the live FitLink site

- FitLink → Benchside everywhere. Support address is now **hello@benchside.coach**
  (was support@fitlink.coach). Instagram: @benchside.coach.
- Removed the placeholder testimonials ("[Quote from a beta coach…]"). Add real quotes only with
  the coach's permission.
- The App Store button is a plain "Get Benchside for iPhone" button. The live site draws its own
  Apple logo and badge; use Apple's official badge files instead if you want a badge.
- Smart App Banner added: `<meta name="apple-itunes-app" content="app-id=6779058450">`.
- Facts kept exactly: 10% fee, Elite $29.99/month or $249/year at 5% with no athlete cap, Founding
  (15 spots, closes Dec 31), $25 lowest pass price, $15 dispute fee, $12 booking fee option,
  Stripe processing comes out of Benchside's fee, iPhone only, 16+, six-digit email code,
  Gemini for assistant drafts.

## Legal changes (Victor to review; not legal advice)

Both documents are the FitLink versions with these changes:

1. Operator: **ORYNTLabs LLC, a New Jersey limited liability company** (Terms §1, Privacy §9).
   The FitLink Terms had blanks here.
2. Governing law and venue: **New Jersey**; state or federal courts located in New Jersey
   (Terms §15). Also blanks before.
3. Coach Elite: now described as bought on the web through Stripe, with Apple in-app purchase
   covered for anyone who already bought it there (Terms plain words, §6, §11, §17; Privacy §1, §4).
   The FitLink Terms said Elite was sold only through Apple, which contradicted the pricing and
   help pages.
4. Terms "In plain words" said an account is a coach or an athlete, "not both", which contradicted
   §3 (a coach can also train). Fixed.
5. Added a Founding paragraph to §6, "Vercel hosts the website" to Privacy §4, and a note that
   Benchside was called FitLink until October 2026.
6. "Last updated" set to 29 October 2026.

## Analytics

The live site feeds the `/admin` page funnel. Re-attach the same events to the new CTAs
(header "Get the app", hero button, plan buttons, final CTA, "Apply for a spot").

## Going live

1. Port into the repo, ship behind a preview branch, compare against this folder at 390 px and 1440 px.
2. Remove `noindex` (this folder's `vercel.json` sends `X-Robots-Tag: noindex` on purpose).
3. Point `og:image` at the deployed `og-image.png`.

## Open items

- Is support staying at hello@benchside.coach, or will there be a support@ address?
- Rename the App Store listing to Benchside (same app id 6779058450).
- oryntlabs.co still lists the app as FitLink.
- fitlink.coach is set not to renew; decide whether it should redirect to benchside.coach until it lapses.
