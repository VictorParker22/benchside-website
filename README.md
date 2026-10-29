# Benchside website

The Benchside marketing site: home, pricing, for athletes, help, privacy and terms.
Plain HTML, one stylesheet, one small script. No build step and no framework.

## What's in this folder

| Path | What it is |
| --- | --- |
| `index.html`, `pricing.html`, `athletes.html`, `support.html`, `privacy.html`, `terms.html`, `404.html` | The pages |
| `assets/site.css`, `assets/site.js` | All styling and the small bits of behavior (mobile menu, pricing calculator, help search, contact form) |
| `assets/screens/` | App screens shown on the site, rendered from the Benchside design canvas |
| `assets/brand/` | Wordmark and app icon (outlined vectors) |
| `assets/fonts/` | Archivo, self-hosted (SIL Open Font License, see `OFL.txt`) |
| `og-image.png` | The picture that shows up when someone shares a link |
| `vercel.json` | Clean URLs (`/pricing`), security headers, and `noindex` while this is a preview |
| `deploy.cmd` | Double-click to publish this folder to Vercel |
| `HANDOFF.md` | Notes for the FitLink team to move this into the app repo |
| `_source/` | The Python that generates the pages, if you'd rather edit there |

## Publish it

1. Double-click `deploy.cmd`.
2. The first time, your browser opens to sign in to Vercel. After that it just runs.
3. It prints the link when it's done.

It deploys to the Vercel project **benchside-site**, not to benchside.coach. Your domain keeps
serving the app's web pages (coach pages, checkout, the coach dashboard) until the FitLink team
moves this design into the app repo. The preview is only visible to people signed in to your
Vercel team; you can make a share link from the Vercel dashboard.

## Look at it on your computer

The pages use paths like `/assets/site.css`, so open them through a tiny local server rather than
double-clicking:

```
npx serve .
```

Then open the address it prints.

## Change something

Edit the HTML files directly, or edit `_source/*.py` and run `python _source/build.py`
(it rewrites the pages in this folder).

## Before it goes live on benchside.coach

- Remove the `X-Robots-Tag: noindex` header in `vercel.json`.
- Swap the "Get Benchside for iPhone" button for Apple's official App Store badge if you want the
  badge (download it from Apple's App Store marketing tools; don't redraw it).
- Replace the app screens with real screenshots once the app UI is final.
- Have the Privacy Policy and Terms read once more by you (and ideally a lawyer). See `HANDOFF.md`
  for exactly what changed from the FitLink versions.
