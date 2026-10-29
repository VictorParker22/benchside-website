from common import COACH, DELETE, EMAIL, footer, head, header

GROUPS = [
    ("coach-payouts", "For coaches", "Getting paid and Stripe", [
        ("How do I get paid?", "Connect payouts in the app (Profile, then Payouts). Stripe opens inside the app, asks for your identity and bank details, and tells Benchside when your account can take charges. Until then nobody can buy your pass. Stripe sends payouts to that bank."),
        ("What does Benchside take?", "10% of each pass payment, or 5% while Coach Elite or a Founding free year is active. On the standard plans your athlete pays exactly the price you set; that amount minus the Benchside fee goes to your Stripe balance. A booking fee, when a coach uses one, is included in the total the athlete is shown before paying. Stripe’s card processing fee comes out of Benchside’s share. See <a href=\"/pricing\">Pricing</a>."),
        ("Where do I see what I earned?", f"The Earnings tab in the app, or <a href=\"{COACH}/earnings\">Earnings on the web</a>: every pass payment with the fees on it and what reached you, by month. The payout date and the bank it goes to live in Stripe; the app opens your Stripe account from Payouts."),
        ("Why does Payouts say “in progress” or “paused”?", "Stripe still needs something from you (a document, a bank detail) or has paused payouts. Open Payouts in the app: it lists what is due and takes you to Stripe to finish it."),
    ]),
    ("coach-passes", "For coaches", "Passes and prices", [
        ("What kinds of pass can I sell?", "An open pass that renews every month (or every year) until the athlete cancels, or a season of a fixed number of weeks. You set the price per month (or per year) in the app. A season charges that price for as many payments as its weeks take and then stops billing by itself: on a monthly price, a 4-week season is one payment, 8 weeks is two and 12 weeks is three. Athletes see the number of payments and the total before they pay. A price change never applies to a period an athlete has already paid for."),
        ("What happens when a season’s payments are done?", "Nothing more is charged. The season ends when the period the last payment covered ends. The athlete keeps their copy of the season and everything they logged, stays on your roster, and is invited to start another season with you; edits you publish to the pass no longer reach them. Changing a season’s length changes the payments for athletes who buy it after the change."),
        ("How do athletes join?", "Share your link: it opens your page with your passes, in any browser. Athletes buy there or in the app, or send you a request you accept. Nobody lands on your roster without doing one of those things."),
        ("Can I stop selling a pass?", "Yes: Stop selling, from the pass’s menu. Athletes who hold it keep it; new athletes can’t buy it. Sell again brings it back."),
        ("Is there a limit on athletes?", "On the free plan, your sixth paying athlete’s payment goes through and they join. From then on you need Elite to keep changing your athletes’ plans; their payments keep coming either way. Coach Elite and Founding have no cap."),
        ("Is there a lowest price for a pass?", "Yes: $25 a payment."),
        ("Can I edit a season athletes are already in?", "Yes, in the app or in the season editor on the web. A week an athlete has already started is protected; everything else publishes to everyone on the pass, and you can tell them what changed."),
    ]),
    ("coach-refunds", "For coaches", "Refunds and cancellations", [
        ("How do I refund an athlete?", "From the athlete’s page in the app: Refund last payment. Choose the full amount or half of it, and whether their pass ends now or keeps running to the end of the period they paid for. You see the amount, the date and the pass before you confirm. The refund goes back to their card through Stripe and comes out of your balance; Stripe may keep its processing fee. Payments older than 90 days can’t be refunded this way."),
        ("Does a refund end the pass?", "Only if you choose that. You can end the pass with the refund, or refund as a goodwill gesture and let the pass run to the end of the period they paid for. Either way the athlete stays on your roster with their history; removing them from the roster is a separate action."),
        ("An athlete disputed a charge with their bank.", "Disputes run under Stripe’s and the card networks’ rules. While one is open the amount is held back from your payouts; if it closes in your favour the money is paid to you again. Each dispute costs you $15, won or lost (an inquiry costs nothing), taken from what Stripe pays you for that payment or for your next ones."),
        ("How do athletes cancel?", "From the app: Profile, then Manage pass. Cancelling stops the next payment; they keep training until the period they paid for ends, and you can see the end date. After that the pass’s plan is no longer part of what they paid for. They stay on your roster with their history and can buy a pass again."),
        ("What happens if I delete my account?", f"Every pass with you ends. Time your athletes prepaid and have not had is refunded to them automatically from your balance. They keep their accounts, logs and history and can join another coach. If you also train with another coach, that pass ends the same day; time you already paid for isn’t refunded. Delete your account <a href=\"{DELETE}\">on the web</a> or from Profile in the app."),
    ]),
    ("coach-assistant", "For coaches", "How the assistant works", [
        ("What does the assistant do?", "It reads an athlete’s check-in and their logged sets and drafts a reply in your voice. You edit, approve and send; nothing reaches an athlete on its own. It needs Coach Elite, and you agree to it in the app before the first draft."),
        ("Where does the text go?", "The check-in text is sent to Google (Gemini) to produce the draft and for nothing else. The <a href=\"/privacy\">Privacy Policy</a> says so, and athletes are told their coach may use an assistant."),
        ("How do I get Coach Elite?", f"Subscribe on the web from your <a href=\"{COACH}\">coach dashboard</a>; the app opens your dashboard. You pay on Stripe’s page, $29.99 a month or $249 a year, and manage or cancel it from the link in your Stripe receipt. If you already have Elite through the App Store, it stays managed in your Apple subscriptions."),
    ]),
    ("coach-account", "For coaches", "Your account", [
        ("How do I sign in?", "With Sign in with Apple or a six-digit code sent to your email. There are no passwords. The season editor on the web signs in with the same email code."),
        ("I signed up with Sign in with Apple and hid my email.", "Sign in in the Benchside app with Sign in with Apple; it opens the same account. To see the address Benchside has for you, on your iPhone open Settings, then your name, then Sign in with Apple, then Benchside."),
        ("Can I also train with a coach?", "Yes. From Profile, a coach can turn on training and open another coach’s link or enter their code. The account then has two modes, Coaching and Training, each with its own Home, messages and notifications; your athletes never see your own training, and you cannot coach yourself."),
        ("How old do I have to be?", "Benchside is for people aged 16 and over. We ask for your date of birth at sign-up."),
        ("Benchside used to be called FitLink.", "Yes. FitLink is now Benchside: the same app, the same account and the same payouts, with a new name and a new look."),
    ]),
    ("athlete-paying", "For athletes", "Paying and cancelling", [
        ("How do I buy a pass?", "Open your coach’s link, pick a pass, enter your email and the six-digit code we send, then pay by card. Stripe handles the card; Benchside never sees the number. The same email signs you in to the app."),
        ("How do I cancel?", "In the app: Profile, then Manage pass. Cancelling stops the next payment. You keep your coach’s plan until the end of what you have paid for; after that it is no longer part of your pass. Your logged sets, check-ins and messages stay. A season stops billing by itself after its last payment, so there is nothing to cancel when it ends."),
        ("What happens when my season ends?", "A season is billed a set number of payments, shown before you pay, and then nothing more is charged. When the period the last payment covered ends, the season is complete: you keep your copy of it and everything you logged, and you stay with your coach. Open your coach’s link to start another season with them."),
        ("Can I get a refund?", "Ask your coach. Refunds are the coach’s call and are issued through the app, back to the card you paid with. Switching coaches or deleting your account ends your pass that day, and time already paid isn’t refunded, so ask your coach before you switch."),
        ("My payment failed.", "Your pass is on hold until a payment goes through; your coach can see that. Stripe emails you a link to update the card."),
        ("Can I switch coaches?", "Yes: open the new coach’s link and confirm. Before you do, you see which of your passes end. Your pass with your current coach ends that day: it stops billing and won’t renew, and any unpaid amount on it is forgiven. Time already paid isn’t refunded, so ask your coach before you switch. Your history with the previous coach stays in their records."),
    ]),
    ("athlete-plan", "For athletes", "Finding your plan after paying", [
        ("I paid but can’t see my plan.", "Sign in to the app with the same email you paid with. Your first week is written by your coach; Today says it is on its way while they do. If it has been a while, message your coach in the app."),
        ("Do I need the app?", "To train, yes. Buying works in any browser; the plan, the timer, check-ins and messages are in the iPhone app."),
        ("I have an Android phone.", "Benchside is an iPhone app today; there is no Android app. Check with your coach before you pay."),
    ]),
    ("athlete-timer", "For athletes", "The session and the rest timer", [
        ("Does the rest timer keep going with the phone locked?", "Yes. It runs on the clock, not on the app being open: lock the phone, put it in a pocket, and it still ends on time with a notification at the deadline."),
        ("I lost signal mid-session.", "Keep logging. The app shows Offline, keeps your sets on the phone, and sends them when you are back."),
        ("What is a check-in?", "Once a week the app asks how it went: effort, whether anything hurt, which session stood out. Your coach reads it where they reply to you."),
    ]),
    ("athlete-privacy", "For athletes", "Privacy and your account", [
        ("What does my coach see?", "Your plan, the sets you log, your check-ins, your messages and what you send in the chat. Apple Health is optional and off by default: if you turn it on, Benchside can save finished workouts to Apple Health and read resting heart rate and sleep, and your coach sees those two numbers only if you also turn on sharing."),
        ("Is my coach’s reply written by AI?", "Coaches can use an assistant that drafts a reply. Your coach reads, edits and sends every message."),
        ("How do I delete my account?", f"From Profile in the app, or <a href=\"{DELETE}\">on the web</a>. You see which passes end before you confirm. Any pass you hold ends that day and stops billing; time already paid isn’t refunded. It is immediate and cannot be undone; payment records are kept where the law requires it."),
    ]),
]


def build():
    h = head("/support", "Help — Benchside",
             "Answers for coaches and athletes on Benchside: payouts, passes, refunds, the assistant, signing in, cancelling and privacy. A person reads every message.")

    nav_coach = "".join(f'<li><a href="#{gid}">{title}</a></li>' for gid, who, title, _ in GROUPS if who == "For coaches")
    nav_ath = "".join(f'<li><a href="#{gid}">{title}</a></li>' for gid, who, title, _ in GROUPS if who == "For athletes")
    groups = ""
    for gid, who, title, items in GROUPS:
        dets = "".join(f'<details><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>' for q, a in items)
        groups += f'<div class="help-group" id="{gid}"><span class="label">{who}</span><h2>{title}</h2><div class="faq">{dets}</div></div>'

    body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Help</span>
    <h1 class="display d-xl">How can we help?</h1>
    <div class="search" role="search">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
      <label class="sr" for="help-search">Search help</label>
      <input id="help-search" type="search" placeholder="Search: payouts, refund, cancel…" autocomplete="off">
    </div>
  </div>
</section>
<section style="padding-bottom:clamp(72px,9vw,120px)">
  <div class="wrap help-grid">
    <nav class="help-nav" aria-label="Help topics">
      <div><h2>For coaches</h2><ul>{nav_coach}</ul></div>
      <div><h2>For athletes</h2><ul>{nav_ath}</ul></div>
    </nav>
    <div>
      <p class="no-results" role="status">Nothing matches that yet. Write to us below and a person will answer.</p>
      {groups}
    </div>
  </div>
</section>
<section style="padding-bottom:clamp(72px,9vw,120px)" id="contact">
  <div class="wrap">
    <div class="contact">
      <div style="display:grid;gap:16px;align-content:start">
        <h2 class="display d-l">Still stuck? Write to us.</h2>
        <p style="color:#DCD3FF">A person reads every message. Send opens your email app with the message addressed to <a style="color:#fff" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        <p class="small" style="color:#B9AEE6">Want to leave Benchside? <a style="color:#fff" href="{DELETE}">Delete your account</a>.</p>
      </div>
      <form id="contact-form" data-to="{EMAIL}" action="mailto:{EMAIL}" method="post" enctype="text/plain">
        <div class="field"><label for="c-email">Your email</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
        <fieldset class="field"><legend>I’m a</legend>
          <div class="chips">
            <label><input type="radio" name="role" value="Coach" checked><span>Coach</span></label>
            <label><input type="radio" name="role" value="Athlete"><span>Athlete</span></label>
            <label><input type="radio" name="role" value="Someone else"><span>Someone else</span></label>
          </div>
        </fieldset>
        <div class="field"><label for="c-msg">What’s going on?</label><textarea id="c-msg" name="message" required></textarea></div>
        <button class="btn btn-lime" type="submit" style="justify-self:start">Send</button>
      </form>
    </div>
  </div>
</section>
</main>
"""
    return h + header("/support") + body + footer()
