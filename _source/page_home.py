from common import APP, COACH, FOUNDING, PLANS_SHORT, faq, final_cta, footer, head, header, phone


def feature(tag, title, body, facts, art, flip=False, art_cls="", extra_art=""):
    fl = " flip" if flip else ""
    lis = "".join(f"<li>{f}</li>" for f in facts)
    return f"""<div class="feature{fl}">
      <div class="feature-copy reveal">
        <span class="tag">{tag}</span>
        <h2 class="display d-l">{title}</h2>
        <p>{body}</p>
        <ul class="facts">{lis}</ul>
      </div>
      <div class="feature-art {art_cls} reveal">{art}{extra_art}</div>
    </div>"""


def build():
    h = head("/", "Benchside — Coach people. Get paid for it.",
             "Benchside runs an independent coach’s business from one app: a link that sells your passes, a Monday screen that shows who needs you, and Stripe payouts to your bank. Free to start.",
             og_title="Benchside — Coach people. Get paid for it.")

    hero = f"""<main id="main">
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <span class="kicker">For independent coaches</span>
      <h1 class="display">Coach people.<br><span class="violet">Get paid</span><br>for it<span class="dot v" aria-hidden="true"></span></h1>
      <p class="lede">Benchside runs the business side of coaching. One link sells your passes, one screen shows who needs you on Monday, and Stripe pays you out to your bank.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{APP}">Get Benchside for iPhone</a>
        <a class="link-arrow" href="/pricing">See pricing</a>
      </div>
      <p class="hero-note">Free to start. Benchside only earns when an athlete pays you: 10% of the pass, and Stripe’s card fees come out of our share, not yours.</p>
    </div>
    <div class="hero-art" aria-label="The Benchside app" role="img">
      {phone("coach-page", "A coach’s Benchside page with two passes and a Book button", "back", eager=True)}
      {phone("coach-today", "The coach’s Today screen: athletes who need a reply, today’s sessions and this week’s earnings", "front", eager=True)}
      <div class="link-chip" aria-hidden="true">
        <div class="lc-text"><span>Your link</span><span>benchside.coach/dana-okafor</span></div>
        <span class="lc-tag">Live</span>
      </div>
    </div>
  </div>
</section>
"""

    steps = """<section class="on-deep pad">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">How it works</span>
      <h2 class="display d-l">From link to first payout.</h2>
    </div>
    <ol class="steps reveal" style="list-style:none;margin:0;padding:0">
      <li class="step"><span class="num" aria-hidden="true">01</span><h3>Set up your page</h3><p>Your name, a photo, a line about how you coach, and your first pass.</p></li>
      <li class="step"><span class="num" aria-hidden="true">02</span><h3>Share one link</h3><p>Text it, post it, or put the QR code on the gym wall. It opens on any phone.</p></li>
      <li class="step"><span class="num" aria-hidden="true">03</span><h3>Athletes pay on the web</h3><p>No download before they buy. Their plan is waiting when they open the app.</p></li>
      <li class="step"><span class="num" aria-hidden="true">04</span><h3>Get paid</h3><p>Stripe sends the money to your bank. You see every fee before it lands.</p></li>
    </ol>
  </div>
</section>
"""

    receipt = """<div class="receipt" aria-label="Example: a $120 pass on the free plan">
        <div class="r-row"><span>Athlete pays</span><span>$120.00</span></div>
        <div class="r-row"><span>Benchside fee · 10%</span><span>−$12.00</span></div>
        <div class="r-row r-total"><span>You get</span><span class="num">$108.00</span></div>
        <div class="r-elite">On Coach Elite the fee is 5%, so you’d get $114.00.</div>
      </div>"""

    features = f"""<section class="pad">
  <div class="wrap">
    {feature("Your page", "One link does the selling.",
             "Your page lists your passes, what each one includes and the price. Athletes pay by card in any browser, with no download first, and their plan is waiting when they open the app.",
             ["Monthly or yearly passes, or a season with a set number of payments", "Card checkout by Stripe, on the web or in the app", "Nobody joins your roster without buying, asking or accepting your link"],
             phone("coach-page", "A coach’s Benchside page with passes and prices"))}
    {feature("Inbox", "Monday, handled.",
             "Check-ins and messages land in one inbox, sorted by who needs you. Today shows who owes a reply, who’s slipping and who just hit a PR. If it isn’t something to do, it isn’t on the screen.",
             ["Weekly check-ins: effort, anything that hurt, the session that stood out", "Photos and videos in one thread per athlete", "Drafts waiting for you are marked"],
             phone("coach-inbox", "The coach’s inbox, with drafts ready to review"), flip=True, art_cls="soft")}
    {feature("Coach Elite", "Your assistant drafts. You send.",
             "It reads the athlete’s check-in and their logged sets and drafts a reply in your voice. Nothing reaches an athlete until you approve it, and every athlete is told you use one.",
             ["You edit, approve and send every message", "Turn it on or off whenever you like", "Included with Coach Elite and Founding"],
             phone("coach-assistant", "A chat with an athlete and a reply drafted by the assistant, waiting for the coach"), art_cls="deep")}
    {feature("Programs", "Build the block in an evening.",
             "Drop exercises onto days, set the sets and loads, add a cue. Publish when it’s right, on your phone or in the season editor on the web.",
             ["A week an athlete has started stays protected", "Tell athletes what changed when you publish", "Form guides for the lifts you program"],
             phone("coach-program", "The program builder showing a Wednesday lower-body day"), flip=True)}
    {feature("Money", "Money that’s boring, on purpose.",
             "Athletes pay the price you set. The fee is on every line before you publish a pass, so a payout never surprises you.",
             ["Payouts by Stripe, straight to your bank", "Card processing comes out of Benchside’s fee", "Every payment, fee and payout in Earnings"],
             phone("coach-earnings", "Earnings: available balance, next payout and fees by month"), art_cls="soft with-receipt", extra_art=receipt)}
  </div>
</section>
"""

    athletes = f"""<section class="on-deep pad">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">For your athletes</span>
      <h2 class="display d-l">An app worth paying for.</h2>
      <p class="lede">Your plan, your cues and a coach who answers, in an app built for the gym floor.</p>
    </div>
    <div class="screens-row reveal" role="region" aria-label="Athlete app screens, scroll sideways" tabindex="0">
      <figure>{phone("athlete-today", "The athlete’s Today screen with the next session and a check-in")}<figcaption><b>Today, one tap away</b>The week, the day and what’s next from you.</figcaption></figure>
      <figure>{phone("athlete-workout", "Logging sets during a box squat with a rest timer running")}<figcaption><b>Logging that keeps up</b>A rest timer that keeps time with the phone in a pocket.</figcaption></figure>
      <figure>{phone("athlete-form-guide", "A form guide for the box squat with steps and what to watch for")}<figcaption><b>Form guides for the lifts</b>Steps, what to watch for, and your own demo.</figcaption></figure>
      <figure>{phone("athlete-done", "Workout done: time, pounds lifted, sets and a new best")}<figcaption><b>Progress they can feel</b>Real numbers after every session, not a dashboard.</figcaption></figure>
    </div>
    <a class="link-arrow" href="/athletes">What athletes see</a>
  </div>
</section>
"""

    trust = """<section class="on-paper pad">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Trust</span>
      <h2 class="display d-l">Built so athletes trust you more, not less.</h2>
    </div>
    <ol class="trust reveal">
      <li><div><h3>You approve every message</h3><p>The assistant drafts. Athletes are told you use one, and every word is still sent by you.</p></div></li>
      <li><div><h3>Payments by Stripe</h3><p>Benchside never stores card or bank numbers. Stripe checks your identity and pays you out.</p></div></li>
      <li><div><h3>Nobody is added without asking</h3><p>An athlete joins your roster by accepting your link, sending you a request or buying your pass. Never by being added.</p></div></li>
      <li><div><h3>Their data is theirs</h3><p>Every athlete can export their training and delete their account any time, and so can you.</p></div></li>
    </ol>
  </div>
</section>
"""

    pricing = f"""<section class="pad">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Pricing</span>
      <h2 class="display d-l">Free to start.</h2>
      <p class="lede">No monthly bill until it’s worth it. Benchside takes a share of the passes you sell, and athletes pay exactly the price you set.</p>
    </div>
    <div class="reveal">{PLANS_SHORT}</div>
    <p style="margin-top:24px"><a class="link-arrow" href="/pricing">Full pricing and calculator</a></p>
  </div>
</section>
"""

    q = faq([
        ("Do my athletes need the app to pay?", "No. They pay on your page in any browser, then get the app to train. Their plan is waiting when they sign in with the same email."),
        ("Does Benchside work on Android?", "Benchside is an iPhone app today. There is no Android app yet, so an athlete needs an iPhone to train with you. Buying a pass works in any browser."),
        ("How do payouts work?", "Payments run on Stripe. You connect a bank once, inside the app, and Stripe sends your payouts to it. Athletes can’t buy a pass until Stripe says your account can take charges."),
        ("Does the AI message my athletes?", "Never on its own. With Coach Elite it drafts a reply from the check-in and the logged sets; you edit, approve and send."),
        ("Can I bring athletes I already coach?", "Yes. Send them your link. They buy a pass on your page and their plan is ready in the app."),
    ])
    faqs = f"""<section class="on-paper pad">
  <div class="wrap faq-grid">
    <div class="section-head reveal" style="margin:0">
      <span class="kicker">Questions</span>
      <h2 class="display d-l">Questions coaches ask.</h2>
      <a class="link-arrow" href="/support">More in Help</a>
    </div>
    <div class="reveal">{q}</div>
  </div>
</section>
"""

    return h + header("/") + hero + steps + features + athletes + trust + pricing + faqs + final_cta() + "</main>\n" + footer()
