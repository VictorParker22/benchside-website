"""Shared bits for the Benchside static site."""
import html

SITE = "https://benchside.coach"
APP = "https://apps.apple.com/app/id6779058450"
APP_ID = "6779058450"
EMAIL = "hello@benchside.coach"
IG = "https://www.instagram.com/benchside.coach/"
# Routes that live in the existing web app (fitlink repo). Absolute so they work from the preview too.
COACH = SITE + "/coach"
FOUNDING = SITE + "/founding"
DELETE = SITE + "/delete-account"
ENTITY = "ORYNTLabs LLC"
VERSION = "20261029"

e = html.escape


def head(path, title, desc, og_title=None):
    url = SITE + path
    og_title = og_title or title
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#F4F4F2">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Benchside">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(og_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Benchside: coach people, get paid for it">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(og_title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/og-image.png">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={VERSION}">
<script>document.documentElement.classList.add("js")</script>
<script src="/assets/site.js?v={VERSION}" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


NAV = [("/pricing", "Pricing"), ("/athletes", "For athletes"), ("/support", "Help")]


def header(active=""):
    cur = ' aria-current="page"'
    links = "".join(
        f'<a href="{h}"{cur if h == active else ""}>{t}</a>' for h, t in NAV
    )
    mlinks = "".join(f'<a href="{h}">{t}<span aria-hidden="true">→</span></a>' for h, t in NAV)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Benchside home"><img src="/assets/brand/wordmark.svg" alt="Benchside" width="128" height="19"></a>
    <nav class="nav" aria-label="Main">{links}<a class="signin" href="{COACH}">Sign in</a></nav>
    <div class="header-cta">
      <a class="btn btn-primary btn-sm" href="{APP}">Get the app</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg>
      </button>
    </div>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Main">
    {mlinks}<a href="{COACH}">Coach sign in<span aria-hidden="true">→</span></a>
    <a class="btn btn-primary" href="{APP}">Get Benchside for iPhone</a>
  </nav>
</header>
"""


def footer():
    return f"""<footer class="site-footer on-deep">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <img src="/assets/brand/wordmark-on-dark.svg" alt="Benchside" width="150" height="22" loading="lazy">
        <p>The app that runs an independent coach’s business. Passes, programs, check-ins and payouts in one place.</p>
      </div>
      <div class="foot-col">
        <h2>Benchside</h2>
        <ul>
          <li><a href="/pricing">Pricing</a></li>
          <li><a href="/athletes">For athletes</a></li>
          <li><a href="{FOUNDING}">Founding 15</a></li>
          <li><a href="{APP}">Get the app</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h2>Help</h2>
        <ul>
          <li><a href="/support">Help center</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{COACH}">Coach sign in</a></li>
          <li><a href="{DELETE}">Delete your account</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h2>More</h2>
        <ul>
          <li><a href="/privacy">Privacy</a></li>
          <li><a href="/terms">Terms</a></li>
          <li><a href="{IG}" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 {ENTITY} · New Jersey, USA</span>
      <span>Payments by Stripe · iPhone app</span>
    </div>
  </div>
</footer>
</body>
</html>
"""


def phone(name, alt, cls="", eager=False, style=""):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    st = f' style="{style}"' if style else ""
    return (f'<div class="phone {cls}"{st}><img src="/assets/screens/{name}.webp" width="780" height="1688" '
            f'alt="{e(alt)}" decoding="async" {load}></div>')


def faq(items):
    out = []
    for q, a in items:
        paras = "".join(f"<p>{p}</p>" for p in (a if isinstance(a, list) else [a]))
        out.append(f'<details><summary>{q}</summary><div class="answer">{paras}</div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"


def final_cta(title="Your next athlete is one link away.", note="On a computer? Open benchside.coach on your iPhone and tap Get the app.", art="coach-live", alt="A coach’s page is live, with a link to share"):
    return f"""<section class="final on-violet pad">
  <div class="wrap">
    <div class="final-copy">
      <h2 class="display d-xl">{title}</h2>
      <a class="btn btn-lime" href="{APP}">Get Benchside for iPhone</a>
      <p class="small" style="color:#F1ECFF">{note}</p>
    </div>
    <div class="final-art" aria-hidden="true">{phone(art, alt)}</div>
  </div>
</section>
"""


PLANS_SHORT = f"""<div class="plans">
  <article class="plan">
    <div class="plan-name">Free</div>
    <div class="price"><span class="num">$0</span><span>a month</span></div>
    <div class="fee"><b>10%</b> per pass sold</div>
    <ul><li>Your page, passes and checkout</li><li>Programs, check-ins and messages</li><li>Up to 5 paying athletes</li></ul>
    <a class="btn btn-ghost" href="{APP}">Start free in the app</a>
  </article>
  <article class="plan featured">
    <div class="plan-name">Coach Elite <span class="badge">Half the fee</span></div>
    <div class="price"><span class="num">$29.99</span><span>a month, or $249 a year</span></div>
    <div class="fee"><b>5%</b> per pass sold</div>
    <ul><li>Everything in Free</li><li>No athlete cap</li><li>Your assistant drafts replies, you approve</li></ul>
    <a class="btn btn-lime" href="{COACH}">Subscribe on the web</a>
  </article>
  <article class="plan">
    <div class="plan-name">Founding <span class="badge">15 spots</span></div>
    <div class="price"><span class="num">$0</span><span>for the first year</span></div>
    <div class="fee"><b>5%</b> per pass sold</div>
    <ul><li>Coach Elite free for a year</li><li>The “Founding 15” badge on your page</li><li>Applications close Dec 31</li></ul>
    <a class="btn btn-ghost" href="{FOUNDING}">Apply for a spot</a>
  </article>
</div>"""
