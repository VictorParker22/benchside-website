from common import APP, EMAIL, faq, final_cta, footer, head, header, phone


def build():
    h = head("/athletes", "For athletes — Benchside",
             "Got a link from your coach? Pay on the web, get the iPhone app, and your coach’s plan is waiting. Here’s how Benchside works for athletes.")

    hero = f"""<main id="main">
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <span class="kicker">For athletes</span>
      <h1 class="display" style="font-size:clamp(56px,7.6vw,112px)">Got a link from your <span class="violet">coach?</span></h1>
      <p class="lede">You’re in the right place. Benchside is where your coach’s plan, your sessions and your messages live.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{APP}">Get Benchside for iPhone</a>
        <a class="link-arrow" href="#questions">Athlete questions</a>
      </div>
      <p class="hero-note">No link yet? Ask your coach for theirs. Benchside doesn’t list or match coaches.</p>
    </div>
    <div class="hero-art" role="img" aria-label="The Benchside app for athletes">
      {phone("athlete-workout", "Logging a box squat with the rest timer running", "back", eager=True)}
      {phone("athlete-today", "The athlete’s Today screen with the next session", "front", eager=True)}
    </div>
  </div>
</section>

<section class="on-deep pad">
  <div class="wrap">
    <div class="section-head reveal"><span class="kicker">How it works</span><h2 class="display d-l">Four steps, no surprises.</h2></div>
    <ol class="steps reveal" style="list-style:none;margin:0;padding:0">
      <li class="step"><span class="num" aria-hidden="true">01</span><h3>Open your coach’s link</h3><p>It shows their passes and prices, and for a season, how many payments it takes.</p></li>
      <li class="step"><span class="num" aria-hidden="true">02</span><h3>Pay on the web</h3><p>Card checkout, handled by Stripe. We email you a six-digit code. No password.</p></li>
      <li class="step"><span class="num" aria-hidden="true">03</span><h3>Get the app</h3><p>Sign in with the email you paid with. Your plan is already there.</p></li>
      <li class="step"><span class="num" aria-hidden="true">04</span><h3>Train and check in</h3><p>Log your sets, say how it felt, and your coach adjusts.</p></li>
    </ol>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="feature">
      <div class="feature-copy reveal">
        <span class="tag">In the gym</span>
        <h2 class="display d-l">Built for the gym floor.</h2>
        <p>Today’s session opens in one tap. Every lift has a form guide, and the rest timer keeps going with your phone locked in a pocket.</p>
        <ul class="facts"><li>Works offline: sets are saved and sent when you’re back</li><li>A weekly check-in your coach actually reads</li><li>Apple Health is optional and off by default</li></ul>
      </div>
      <div class="feature-art soft reveal">{phone("athlete-form-guide", "A form guide for the box squat")}</div>
    </div>
  </div>
</section>
"""

    q = faq([
        ("How do I cancel?", "In the app: Profile, then Manage pass. Cancelling stops the next payment. You keep your coach’s plan until the end of what you’ve paid for; after that it is no longer part of your pass. Your logged sets, check-ins and messages stay. A season stops billing by itself after its last payment, so there is nothing to cancel when it ends."),
        ("What happens when my season ends?", "A season is billed a set number of payments, shown before you pay, and then nothing more is charged. When the period the last payment covered ends, the season is complete: you keep your copy of it and everything you logged, and you stay with your coach. Open your coach’s link to start another season with them."),
        ("What does my coach see?", "Your plan, the sets you log, your check-ins, your messages and anything you send in the chat. Apple Health is optional and off by default: if you turn it on in the app, Benchside can save finished workouts to Apple Health and read resting heart rate and sleep, and your coach sees those two numbers only if you also turn on sharing."),
        ("Is my coach’s reply written by AI?", "Coaches can use an assistant that drafts a reply from your check-in and your log. Your coach reads, edits and sends every message; nothing is sent on its own."),
        ("Can I get a refund?", "Ask your coach. Refunds are at the coach’s discretion and are issued through the app, back to the card you paid with. If a coach closes their account, time you prepaid and have not had is refunded automatically. If you switch coaches or delete your account, your pass ends that day and time already paid isn’t refunded, so ask your coach before you switch."),
        ("My payment failed. What now?", "Your pass is on hold until a payment goes through; your coach can see that. Stripe emails you a link to update the card."),
        ("I have an Android phone.", "Benchside is an iPhone app today and there is no Android app. Buying a pass works in any browser, but training needs the iPhone app, so check with your coach before you pay."),
        ("I paid but can’t see my plan.", f"Sign in to the app with the same email you paid with. Your first week comes from your coach, and Today says so while it is still on its way. Still stuck? <a href=\"mailto:{EMAIL}\">Write to us</a> and include your receipt."),
    ])
    faqs = f"""<section class="on-paper pad" id="questions">
  <div class="wrap faq-grid">
    <div class="section-head" style="margin:0"><span class="kicker">Questions</span><h2 class="display d-l">Athlete questions.</h2><a class="link-arrow" href="/support">More in Help</a><a class="link-arrow" href="/">Are you a coach?</a></div>
    <div>{q}</div>
  </div>
</section>
"""
    return h + header("/athletes") + hero + faqs + final_cta("Ready to train?", "iPhone only for now. Buying a pass works in any browser.", art="athlete-done", alt="Workout done screen") + "</main>\n" + footer()
