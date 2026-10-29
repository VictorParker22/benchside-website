from common import APP, COACH, FOUNDING, faq, final_cta, footer, head, header

CAP_NOTE = "On the free plan, your sixth paying athlete’s payment goes through and they join. From then on you need Elite to keep changing your athletes’ plans; their payments keep coming either way."


def build():
    h = head("/pricing", "Pricing — Benchside",
             "Free to start: Benchside takes 10% of the passes you sell. Coach Elite is $29.99 a month and halves the fee to 5%, with no athlete cap. Stripe card fees come out of our share.")

    plans = f"""<div class="plans">
  <article class="plan">
    <div class="plan-name">Free</div>
    <div class="price"><span class="num">$0</span><span>a month</span></div>
    <div class="fee"><b>10%</b> per pass sold · up to 5 paying athletes</div>
    <ul>
      <li>Your coaching page and passes: monthly, yearly or a season</li>
      <li>Checkout on the web and in the app, payouts through Stripe</li>
      <li>Workout builder, seasons and the season editor on the web</li>
      <li>Check-ins, messages and athlete progress</li>
    </ul>
    <a class="btn btn-ghost" href="{APP}">Start free in the app</a>
    <p class="plan-foot">{CAP_NOTE}</p>
  </article>
  <article class="plan featured">
    <div class="plan-name">Coach Elite <span class="badge">Half the fee</span></div>
    <div class="price"><span class="num">$29.99</span><span>a month, or $249 a year</span></div>
    <div class="fee"><b>5%</b> per pass sold · no athlete cap</div>
    <ul>
      <li>Everything in Free</li>
      <li>Half the fee on every pass, renewals included</li>
      <li>No athlete cap</li>
      <li>Replies drafted in your voice from the check-in and logged sets. You approve every one</li>
    </ul>
    <a class="btn btn-lime" href="{COACH}">Subscribe on the web</a>
    <p class="plan-foot">You subscribe from your coach dashboard on the web and pay on Stripe’s page. Cancel from the link in your receipt.</p>
  </article>
  <article class="plan">
    <div class="plan-name">Founding <span class="badge">15 spots · closes Dec 31</span></div>
    <div class="price"><span class="num">$0</span><span>for the first year</span></div>
    <div class="fee"><b>5%</b> per pass sold · no athlete cap</div>
    <ul>
      <li>Coach Elite free for a year, from your first athlete payment after your spot is granted</li>
      <li>A 5% fee while the free year or Elite runs</li>
      <li>The “Founding 15” badge on your coach page</li>
      <li>After the year: Elite at $29.99 a month, or the free plan</li>
    </ul>
    <a class="btn btn-primary" href="{FOUNDING}">Apply for a spot</a>
  </article>
</div>"""

    calc = """<section class="pad-s">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Calculator</span>
      <h2 class="display d-l">What you keep each month.</h2>
    </div>
    <div class="calc" id="calc">
      <div class="calc-input">
        <label for="calc-amount">What your athletes pay you each month</label>
        <div class="money-input"><span aria-hidden="true">$</span><input id="calc-amount" type="text" inputmode="decimal" autocomplete="off" size="6" value="3000"></div>
        <div class="calc-controls">
          <input id="calc-range" type="range" min="0" max="15000" step="50" value="3000" aria-label="Monthly athlete payments">
          <div class="seg" role="group" aria-label="Coach Elite billing">
            <button type="button" data-billing="monthly" aria-pressed="true">Elite monthly</button>
            <button type="button" data-billing="yearly" aria-pressed="false">Elite yearly</button>
          </div>
        </div>
      </div>
      <div class="calc-out" aria-live="polite">
        <div class="keep" data-plan="free"><div class="k-name">Free</div><div class="k-label">You keep</div><div class="num" data-k="free">$2,700</div><div class="k-sub" data-f="free">10% fee: $300</div><div class="k-sub">Up to 5 paying athletes</div></div>
        <div class="keep best" data-plan="elite"><div class="k-name">Coach Elite</div><div class="k-label">You keep</div><div class="num" data-k="elite">$2,820.01</div><div class="k-sub" data-f="elite">5% fee: $150 · Elite $29.99 a month</div></div>
        <div class="keep" data-plan="founding"><div class="k-name">Founding <i>15 spots</i></div><div class="k-label">You keep</div><div class="num" data-k="founding">$2,850</div><div class="k-sub" data-f="founding">5% fee: $150 · no subscription in year one</div></div>
      </div>
      <p class="calc-summary">Elite leaves you $120.01 more a month than Free. It pays for itself above $599.80 a month in athlete payments.</p>
    </div>
    <p class="small" style="margin-top:16px;max-width:52em">On the standard plans, athletes pay exactly the price you set. Stripe’s card processing (about 2.9% + 30¢ a payment) comes out of Benchside’s fee, not out of what you keep. Taxes on what you earn are yours to handle.</p>
  </div>
</section>
"""

    rows = [
        ("Coaching page, passes, checkout", "Included", "Included", "Included"),
        ("Workout builder, seasons, season editor", "Included", "Included", "Included"),
        ("Check-ins, messages, progress", "Included", "Included", "Included"),
        ("Paying athletes", "Up to 5*", "No cap", "No cap"),
        ("Assistant drafts your replies", "—", "Included", "Included"),
        ("Benchside fee per pass", "10%", "5%", "5%"),
        ("Lowest pass price", "$25 a payment", "$25 a payment", "$25 a payment"),
        ("Price", "$0", "$29.99 a month or $249 a year", "Free for the first year"),
    ]
    trs = ""
    dash = '<span aria-hidden="true">—</span><span class="sr">Not included</span>'
    for r in rows:
        cells = ""
        for c in r[1:]:
            cls = "yes" if c == "Included" else ("no" if c == "—" else "")
            cells += f'<td class="{cls}">{dash if c == "—" else c}</td>'
        trs += f'<tr><th scope="row">{r[0]}</th>{cells}</tr>'
    compare = f"""<section class="pad-s">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Compare</span><h2 class="display d-m">Compare plans.</h2></div>
    <div class="table-wrap" role="region" aria-label="Plan comparison" tabindex="0">
      <table class="compare">
        <thead><tr><th scope="col"><span class="sr">Feature</span></th><th scope="col">Free</th><th scope="col">Coach Elite</th><th scope="col">Founding</th></tr></thead>
        <tbody>{trs}</tbody>
      </table>
    </div>
    <p class="small" style="margin-top:14px;max-width:52em">* {CAP_NOTE}</p>
  </div>
</section>
"""

    q = faq([
        ("What is the fee charged on?", "Only on passes athletes buy through Benchside. Sell nothing, pay nothing."),
        ("Are card processing fees included?", "Yes. A pass is charged through Benchside’s Stripe account and the athlete’s payment, minus the Benchside fee, is transferred to yours. Stripe’s card processing (about 2.9% + 30¢ a payment) comes out of Benchside’s fee, not out of what you keep. When you refund a payment, Stripe may keep its processing fee."),
        ("Do my athletes pay anything extra?", "On the standard plans, athletes pay exactly the price you set: there is no processing charge or surcharge at checkout. A coach who uses a booking fee ($12 a payment) has it included in the total the athlete is shown before paying, never added after."),
        ("Is there an athlete limit?", CAP_NOTE + " Coach Elite and Founding have no cap."),
        ("Is there a minimum price?", "Yes: a pass costs at least $25 a payment."),
        ("How do I start or stop Elite?", f"Subscribe on the web from your <a href=\"{COACH}\">coach dashboard</a>; the app opens your dashboard. You pay on Stripe’s page, monthly ($29.99) or yearly ($249). Manage or cancel it from the link in your Stripe receipt; Elite stays on until the end of the period you paid for. If you already have Elite through the App Store, it stays managed in the App Store."),
        ("How does the lower fee reach my existing passes?", "The fee is set on the server from your plan and applied to every pass payment, including renewals of passes your athletes already hold."),
        ("What does a dispute cost?", "$15 for each dispute, won or lost; an inquiry costs nothing. It comes out of what Stripe pays you for that payment or for your next ones."),
        ("What is Founding?", f"15 coaches get Coach Elite free for a year and a 5% fee. The free year starts with the first payment one of your athletes makes after your spot is granted. After it, Elite is $29.99 a month if you keep it, or you move to the free plan. Applications close Dec 31. <a href=\"{FOUNDING}\">Apply for a Founding spot</a>."),
    ])
    faqs = f"""<section class="on-paper pad">
  <div class="wrap faq-grid">
    <div class="section-head" style="margin:0"><span class="kicker">Questions</span><h2 class="display d-l">Pricing questions.</h2><a class="link-arrow" href="/support">More in Help</a></div>
    <div>{q}</div>
  </div>
</section>
"""

    hero = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Pricing</span>
    <h1 class="display d-xl">Free to start<span class="dot v" aria-hidden="true"></span></h1>
    <p class="lede">No monthly bill to start. Benchside takes a share of the passes you sell, and on the standard plans your athletes pay exactly the price you set.</p>
  </div>
</section>
<section style="padding-bottom:clamp(48px,6vw,88px)"><div class="wrap">{plans}</div></section>
"""
    return h + header("/pricing") + hero + calc + compare + faqs + final_cta("Start free. Pay when it works.") + "</main>\n" + footer()
