"""Build the Benchside static site into ../dist."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import APP, SITE, final_cta, footer, head, header  # noqa: E402
import page_athletes  # noqa: E402
import page_home  # noqa: E402
import page_legal  # noqa: E402
import page_pricing  # noqa: E402
import page_support  # noqa: E402

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def write(name, content):
    with open(os.path.join(DIST, name), "w", encoding="utf-8") as fh:
        fh.write(content)
    print("wrote", name, len(content))


def not_found():
    return head("/404", "Page not found — Benchside", "This page doesn’t exist on Benchside.") + header() + f"""<main id="main">
<section class="pad">
  <div class="wrap lost">
    <span class="kicker">404</span>
    <h1 class="display d-xl">Rest day<span class="dot v" aria-hidden="true"></span></h1>
    <p class="lede">This page doesn’t exist. If a coach sent you a link, check it with them, or start from the home page.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="/">Go to the home page</a><a class="link-arrow" href="/support">Help</a></div>
  </div>
</section>
</main>
""" + footer()


write("index.html", page_home.build())
write("pricing.html", page_pricing.build())
write("athletes.html", page_athletes.build())
write("support.html", page_support.build())
write("privacy.html", page_legal.privacy())
write("terms.html", page_legal.terms())
write("404.html", not_found())

write("site.webmanifest", json.dumps({
    "name": "Benchside", "short_name": "Benchside",
    "icons": [{"src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
              {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}],
    "theme_color": "#160A3D", "background_color": "#F4F4F2", "display": "browser"}, indent=2))

write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
urls = ["/", "/pricing", "/athletes", "/support", "/privacy", "/terms"]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "".join(f"  <url><loc>{SITE}{u if u != '/' else ''}</loc><lastmod>2026-10-29</lastmod></url>\n" for u in urls) + "</urlset>\n")

write("vercel.json", json.dumps({
    "cleanUrls": True,
    "trailingSlash": False,
    "headers": [
        {"source": "/(.*)", "headers": [
            {"key": "X-Content-Type-Options", "value": "nosniff"},
            {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
            {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"},
            {"key": "X-Frame-Options", "value": "DENY"},
            {"key": "X-Robots-Tag", "value": "noindex"}
        ]},
        {"source": "/assets/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
        {"source": "/assets/(screens|brand)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400"}]}
    ]
}, indent=2))
