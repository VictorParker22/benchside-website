"""Render Benchside .dc.html app screens to PNG/WebP with a tiny stand-in for the DC runtime.

usage: python3 render_screens.py <project_dir> <out_dir> <scale> Screen1 Screen2 ...
"""
import os
import sys
from playwright.sync_api import sync_playwright

PROJ, OUT, SCALE = sys.argv[1], sys.argv[2], float(sys.argv[3])
NAMES = sys.argv[4:]
FONTS = "/tmp/claude-0/-home-claude/d31ccae4-9616-55d3-9dc7-c0ae8c086c8e/scratchpad/fontvar"
os.makedirs(OUT, exist_ok=True)

FONT_CSS = f"""
@font-face{{font-family:'Archivo';src:url('file://{FONTS}/package/files/archivo-latin-standard-normal.woff2') format('woff2');font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:'SF Pro Text';src:url('file://{FONTS}/inter/package/files/inter-latin-standard-normal.woff2') format('woff2');font-weight:100 900}}
@font-face{{font-family:'BlinkMacSystemFont';src:url('file://{FONTS}/inter/package/files/inter-latin-standard-normal.woff2') format('woff2');font-weight:100 900}}
@font-face{{font-family:'SF Pro Display';src:url('file://{FONTS}/inter/package/files/inter-latin-standard-normal.woff2') format('woff2');font-weight:100 900}}
"""

RUNTIME = r"""
() => {
  const scriptEl = document.querySelector('script[data-dc-script]');
  let vals = {};
  if (scriptEl) {
    let props = {};
    try { props = JSON.parse(scriptEl.getAttribute('data-props') || '{}'); } catch (e) {}
    delete props.$preview;
    const DCLogic = class { constructor() { this.state = {}; this.props = props; } setState() {} };
    const Component = new Function('DCLogic', scriptEl.textContent + '\nreturn Component;')(DCLogic);
    const c = new Component(); c.props = props; c.state = {};
    vals = c.renderVals() || {};
  }
  const look = (scope, expr) => {
    expr = expr.trim();
    if (expr === 'true') return true; if (expr === 'false') return false;
    if (/^-?\d+(\.\d+)?$/.test(expr)) return Number(expr);
    let v = scope;
    for (const k of expr.split('.')) { if (v == null) return undefined; v = v[k]; }
    return v;
  };
  const sub = (scope, s) => s.replace(/\{\{([^}]*)\}\}/g, (_, e) => { const v = look(scope, e); return (v == null || typeof v === 'function') ? '' : String(v); });
  const walk = (node, scope) => {
    for (const child of [...node.childNodes]) {
      if (child.nodeType === 3) { if (child.nodeValue.includes('{{')) child.nodeValue = sub(scope, child.nodeValue); continue; }
      if (child.nodeType !== 1) continue;
      const tag = child.tagName.toLowerCase();
      if (tag === 'sc-for') {
        const m = /\{\{([^}]*)\}\}/.exec(child.getAttribute('list') || '');
        const list = m ? (look(scope, m[1]) || []) : [];
        const as = child.getAttribute('as') || 'item';
        const tpl = child.innerHTML;
        const frag = document.createDocumentFragment();
        list.forEach((item, i) => {
          const holder = document.createElement('div');
          holder.innerHTML = tpl;
          walk(holder, Object.assign({}, scope, { [as]: item, index: i }));
          while (holder.firstChild) frag.appendChild(holder.firstChild);
        });
        child.replaceWith(frag);
        continue;
      }
      if (tag === 'sc-if') {
        const m = /\{\{([^}]*)\}\}/.exec(child.getAttribute('value') || '');
        const ok = m ? !!look(scope, m[1]) : false;
        if (!ok) { child.remove(); continue; }
        walk(child, scope);
        const frag = document.createDocumentFragment();
        while (child.firstChild) frag.appendChild(child.firstChild);
        child.replaceWith(frag);
        continue;
      }
      for (const a of [...child.attributes]) {
        if (/^on[A-Z]/.test(a.name) || /^on/.test(a.name) && a.value.includes('{{')) { child.removeAttribute(a.name); continue; }
        if (a.value.includes('{{')) child.setAttribute(a.name, sub(scope, a.value));
      }
      walk(child, scope);
    }
  };
  const root = document.querySelector('x-dc');
  walk(root, vals);
  return true;
}
"""

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(device_scale_factor=SCALE, viewport={"width": 390, "height": 844})
    ctx.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    ctx.route("**/support.js", lambda r: r.fulfill(status=200, content_type="text/javascript", body=""))
    pg = ctx.new_page()
    for name in NAMES:
        path = os.path.join(PROJ, name + ".dc.html")
        pg.goto("file://" + path)
        pg.add_style_tag(content=FONT_CSS)
        pg.evaluate(RUNTIME)
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(400)
        el = pg.locator("x-dc > div").first
        png = os.path.join(OUT, name + ".png")
        el.screenshot(path=png)
        print("rendered", name)
    b.close()
