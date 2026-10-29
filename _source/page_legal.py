from common import DELETE, EMAIL, ENTITY, footer, head, header

UPDATED = "29 October 2026"
RENAMED = "Benchside was called FitLink until October 2026. It is the same service under a new name; if you agreed to the FitLink terms or privacy policy, these replace them."


def legal_page(path, title, desc, sections, plain, intro_extra=""):
    toc = '<a href="#plain">In plain words</a>' + "".join(f'<a href="#{sid}">{t}</a>' for sid, t, _ in sections)
    body = ""
    for sid, t, html in sections:
        body += f'<h2 id="{sid}">{t}</h2>{html}'
    other = ("/terms", "Terms of Service") if path == "/privacy" else ("/privacy", "Privacy Policy")
    return (head(path, f"{title} — Benchside", desc) + header() + f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Legal</span>
    <h1 class="display d-xl">{title}</h1>
    <p class="updated">Last updated {UPDATED}</p>
  </div>
</section>
<section style="padding-bottom:clamp(72px,9vw,120px)">
  <div class="wrap legal">
    <nav class="toc" aria-label="On this page">{toc}</nav>
    <article class="legal-body">
      <div class="plain" id="plain"><h2>In plain words</h2>{plain}</div>
      <p>{RENAMED}</p>
      {intro_extra}
      {body}
      <p style="margin-top:24px" class="small">© 2026 {ENTITY} · <a href="{other[0]}">{other[1]}</a> · <a href="{DELETE}">Delete your account</a></p>
    </article>
  </div>
</section>
</main>
""" + footer())


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def privacy():
    plain = ul([
        "Benchside collects only the data needed to connect coaches with athletes and run the coaching between them.",
        "We never sell your data, and nothing is used for advertising or tracking.",
        "Your coach sees your training, check-ins and messages. Nothing else unless you send it.",
        "Stripe handles payments. We never see a card number.",
        "You can delete your account at any time.",
    ])
    S = [
        ("collect", "1. Information we collect", "<p>We collect the following categories of information:</p>" + ul([
            "<strong>Account information:</strong> name, email address, date of birth (to confirm you are 16 or older) and, if you add one, a profile photo. A coach may also add a bio and a specialisation, which appear on their public page.",
            "<strong>Training data:</strong> the workouts, seasons and notes your coach writes for you; the sets, sessions and body weight you log; your weekly check-ins.",
            "<strong>Photos and videos:</strong> a profile photo, and any photo or video you choose to send in a chat with your coach.",
            "<strong>Payment information:</strong> pass payments are processed by Stripe. We never see or store card numbers; we keep a record of which pass you bought, when, and its status. A coach who connects payouts gives their identity and bank details directly to Stripe. Coach Elite bought on the web is paid through Stripe; if you bought it in the App Store, we receive the subscription’s status from Apple and RevenueCat, not your payment details.",
            "<strong>Communications:</strong> messages exchanged between coaches and athletes within the app.",
            "<strong>Device information:</strong> device type, OS version, and a push notification token, used only to deliver the notifications you have allowed.",
            "<strong>Website:</strong> a coach’s public page on benchside.coach can be read by anyone with its link. You can sign in there with a six-digit code sent to your email or with Sign in with Apple. If you sign in with Apple, Apple gives us the same account identifier and email address (or private relay address) it gives the app, and your name the first time, if you choose to share it. Your sign-in session is kept in your browser’s local storage. When you continue with Apple from a coach’s page, that browser tab also keeps the link’s code, the pass you chose and any name you typed until you come back, for at most 30 minutes. We do not use advertising cookies.",
        ])),
        ("use", "2. How we use your data", ul([
            "To provide and maintain the Benchside service",
            "To connect athletes with their coaches, and show each the other’s training data and messages",
            "To show your training progress",
            "To process payments, pay coaches and manage subscriptions",
            "To send push notifications about workouts, messages and check-ins, when you allow them",
            "To draft a coach’s reply with an AI assistant, only after the coach has agreed to it in the app (see section 4)",
            "To keep the service secure and prevent abuse",
            "To improve our app and user experience",
        ])),
        ("health", "3. Fitness and health data", "<p>The training data Benchside holds is what you or your coach type into Benchside:</p>" + ul([
            "Apple Health is optional and off by default. If you turn it on in the app, Benchside can save the workouts you finish to Apple Health, and read your resting heart rate and sleep from it. Each of the three is a separate switch; iOS asks your permission before anything is read or written.",
            "Resting heart rate and sleep are shown to you next to your check-ins. Your coach sees them only if you also turn on “Share with your coach”, and stops seeing them the moment you turn it off. Benchside does not use Google Health Connect and reads nothing from any other health app or wearable.",
            "Logged sets, sessions, body weight and check-ins are used solely to run your coaching: they are shown to you and to the coach you train with.",
            "Never sold to third parties.",
            "Never used for advertising or marketing purposes.",
            "Health data is never used to decide prices, fees or what you are offered.",
        ])),
        ("sharing", "4. Data sharing", "<p>We share your data only in these limited circumstances:</p>" + ul([
            "<strong>With your coach:</strong> training data, logged sets, body weight, check-ins, photos you send and messages are shared with the coach you train with. A coach you leave keeps their own record of the coaching they delivered.",
            "<strong>On a coach’s public page:</strong> a coach’s name, photo, bio and passes are public on the link the coach shares.",
            "<strong>Payment processing:</strong> payment and payout data is handled by Stripe. The status of a Coach Elite subscription comes from Stripe, or from Apple and RevenueCat if it was bought in the App Store.",
            "<strong>Sign in with Apple:</strong> when you choose it, in the app or on the website, Apple confirms who you are and sends us an identifier and your email address or a private relay address that forwards to you.",
            "<strong>The coach’s assistant:</strong> when a coach asks the assistant to draft a reply, the athlete’s check-in text is sent to Google (Gemini) to produce that draft and for nothing else. The coach must agree to the assistant in the app before it is used, and reads and approves every message before it is sent.",
            "<strong>Infrastructure:</strong> Supabase hosts our database, sign-in and file storage. Vercel hosts the website.",
            "<strong>Push notifications:</strong> device tokens are shared with the Apple Push Notification service (APNs) and Expo’s push service for notification delivery.",
            "<strong>Legal requirements:</strong> when required by law or to protect our legal rights.",
        ]) + "<p>We do not sell, rent, or trade your personal information to third parties, and we do not use it for advertising or tracking.</p>"),
        ("security", "5. Data storage and security", ul([
            "Data is stored securely on Supabase cloud infrastructure",
            "All data transmission is encrypted using TLS",
            "Sign-in tokens are stored in secure device storage (the iOS keychain)",
            "Each coach and athlete can read only their own rows and those of the people they train with, enforced in the database",
            "We implement industry-standard security measures to protect your data",
        ])),
        ("rights", "6. Your rights", "<p>You have the right to:</p>" + ul([
            "<strong>Access:</strong> request a copy of your personal data",
            "<strong>Correction:</strong> update or correct inaccurate information from your profile in the app",
            f"<strong>Deletion:</strong> delete your account and its data at any time from Profile in the app, or <a href=\"{DELETE}\">on the web</a>",
            "<strong>Portability:</strong> export your data from Profile in the app, or request it in a portable format",
            "<strong>Withdraw consent:</strong> a coach can stop using the assistant at any time; notifications can be turned off in your device settings",
        ])),
        ("children", "7. Children’s privacy", "<p>Benchside is for people aged 16 and over. We ask for a date of birth at sign-up and do not knowingly collect data from anyone under 16; if we learn that we have, we delete the account. If you believe a child has provided us with personal information, please contact us.</p>"),
        ("changes", "8. Changes to this policy", "<p>We may update this privacy policy from time to time. We will notify you of significant changes through the app or by email.</p>"),
        ("contact", "9. Contact us", f"<p>Benchside is operated by {ENTITY}, a New Jersey limited liability company. If you have questions about this privacy policy or your data, contact us:</p>" + ul([
            f"Email: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>",
            "In the app: Profile → Support",
        ])),
    ]
    return legal_page("/privacy", "Privacy Policy",
                      "How Benchside collects, uses and protects coach and athlete data: what your coach sees, Stripe payments, Apple Health, the assistant, and your rights.",
                      S, plain)


def terms():
    plain = ("<p>Benchside is where independent coaches sell training passes and run their athletes’ weeks. The coach sells the pass; Benchside runs the platform and processes the payment through Stripe. "
             "An open pass renews until you cancel it; a season is billed the number of payments shown before you pay, then stops by itself. Refunds are the coach’s call and are issued through the app. "
             "Switching coaches or deleting your account ends your pass that day, and time already paid isn’t refunded, so ask your coach before you switch. "
             "Coach Elite is a subscription for coaches, bought on the web through Stripe (or, if you bought it there, through Apple under Apple’s terms). "
             "Training carries risk and nothing on Benchside is medical advice. You must be 16 or older. An account starts as a coach or an athlete; a coach can also train with another coach.</p>")
    S = [
        ("who", "1. Who we are and what these terms cover",
         f"<p>Benchside is a coaching platform: the Benchside app for iPhone, the website at benchside.coach (including a coach’s public page and web checkout) and the services behind them. Together we call them the Service. The Service is operated by {ENTITY}, a New Jersey limited liability company (“Benchside”, “we”, “us”).</p>"
         "<p>These Terms of Service are a contract between you and Benchside. By creating an account, buying a pass, publishing a pass or otherwise using the Service you agree to these terms and to our <a href=\"/privacy\">Privacy Policy</a>. If you do not agree, do not use the Service.</p>"
         "<p>If you use Benchside as a coach, the sections addressed to coaches apply to you as well as the general ones. If you use it as an athlete, the athlete sections apply. Some sections address both.</p>"),
        ("roles", "2. Coaches, athletes and Benchside", ul([
            "<strong>Coaches</strong> are independent professionals who use Benchside to sell training passes and deliver coaching. Coaches are not employees, agents, partners or representatives of Benchside. Each coach decides what they sell, at what price, and how they coach.",
            "<strong>Athletes</strong> buy a pass from a coach. The coaching relationship, including the programme, the advice and the results, is between the athlete and the coach.",
            "<strong>Benchside</strong> provides the platform: the tools a coach uses to build seasons and workouts, the roster, messaging, check-ins, the public page, the web checkout, and payment processing through Stripe. Benchside is not a party to the coaching relationship. Benchside does not supervise, direct or guarantee a coach’s services, and does not independently verify a coach’s qualifications, certifications or insurance. Ask your coach about these directly.",
        ])),
        ("account", "3. Your account", ul([
            "<strong>Age.</strong> You must be at least 16 years old to create an account. We ask for your date of birth when you sign up. If we learn that an account holder is under 16 we close the account.",
            "<strong>Two modes, one account.</strong> An account starts as a coach account or an athlete account. A coach can also turn on training from Profile and train with another coach; the account then has a Coaching mode and a Training mode, each with its own Home, messages and notifications. A coach’s athletes never see the coach’s own training, and nobody can coach themselves.",
            "<strong>Signing in.</strong> You sign in with a six-digit code sent to your email, or with Sign in with Apple. There is no password. You are responsible for keeping your email inbox and your device secure. Tell us at once if you believe someone else has used your account.",
            "<strong>Accuracy.</strong> Give us accurate information and keep it current. An account is for one person; do not share it or let someone else use it.",
            "<strong>Joining a roster takes an action by the athlete.</strong> An athlete joins a coach’s roster only by accepting that coach’s invitation, by sending a request that the coach accepts, or by buying that coach’s pass. Coaches may not add people who have not done one of these things.",
            "<strong>Switching coaches ends your current pass.</strong> When you join a new coach, every pass you hold with any other coach ends that day: it stops billing and does not renew, and any unpaid amount on it is forgiven. Time you have already paid for is not refunded. You see which passes end before you confirm, and they stay ended even if you do not finish buying the new coach’s pass. Ask your coach before you switch.",
        ])),
        ("passes", "4. Passes and subscriptions (athletes)", ul([
            "<strong>What a pass is.</strong> A pass is what the coach describes on it: an open pass, billed every month or every year until you cancel it, or a season of a fixed number of weeks. Every pass charges the price shown per month, or per year for a yearly price. A season charges it for the number of payments shown before you pay (for example, two monthly payments for an 8-week season) and then stops billing; that number is fixed when you buy, and a later change to the season by the coach does not change it. The price shown at checkout is the price you pay, plus any tax that applies where you live.",
            "<strong>Buying a pass joins the coach.</strong> When you buy a pass you join that coach’s roster, and the coach can see your training data, logged sets, check-ins and messages for as long as you are on it. If you were training with a different coach, buying a pass from a new one moves you to the new coach; your history stays in the previous coach’s records, and your pass with them ends as described in section 3 (no refund of time already paid).",
            "<strong>Renewal.</strong> An open pass renews automatically at the end of each period, at the price shown, until you cancel it. A season renews only until its last payment: nothing more is charged after it, and the season ends when the period that payment covered ends. You then keep your copy of the season and everything you logged, and you stay on the coach’s roster; to keep training on the coach’s plan, buy another pass.",
            "<strong>Cancelling.</strong> You can cancel a pass from the app at any time. Cancelling stops the next payment; you keep access to the coach’s plan until the end of the period you have already paid for. After that, access to the plan is no longer part of your pass and may be closed, including for a season cancelled before its last payment. Your logged sets, check-ins and messages stay, and you stay on the coach’s roster. A price change never applies to a period you have already paid for.",
            "<strong>Failed payments.</strong> If a renewal payment fails, the pass goes on hold until payment succeeds. Your coach can see that it is on hold.",
            "<strong>A coach may end a pass.</strong> A coach may stop selling a pass or remove you from their roster. If that happens before the end of a period you have paid for, see refunds below.",
        ])),
        ("payments", "5. Payments, fees, refunds and disputes",
         "<h3>Payments</h3>" + ul([
             "Payments for passes are processed by Stripe. Your card details go directly to Stripe and never touch Benchside’s servers. Stripe’s own terms and privacy policy apply to the payment itself.",
             "Benchside keeps a platform fee from each pass payment and pays the rest to the coach. The fee is shown to the coach in the app before they publish a pass; it does not change the price an athlete sees.",
         ]) + "<h3>Refunds</h3>" + ul([
             "Refunds are at the coach’s discretion and are issued through the app, within 90 days of the payment. If you want a refund, ask your coach. The coach refunds the full payment or half of it, and either ends the pass that day or lets it run to the end of the period you paid for. The notice you receive says which.",
             "Benchside may also refund a payment where the law, Stripe’s rules or the card network’s rules require it, or where a coach’s account has been closed before a paid period was delivered.",
             "Switching coaches or deleting your account is not a refund. Either one ends your pass that day; time already paid is not refunded, and any unpaid amount on the pass is forgiven. If you want money back, ask your coach before you switch or delete.",
             "Nothing in this section limits rights you have as a consumer under the law where you live.",
         ]) + "<h3>Disputes and chargebacks</h3>" + ul([
             "If something is wrong with a payment, contact your coach or us first; most problems are quicker to fix that way than through your bank.",
             "A chargeback or dispute raised with your bank is handled under Stripe’s and the card networks’ rules. While a dispute is open, the disputed amount is withheld from the coach and may be recovered from the coach’s payouts; if the dispute is resolved in the coach’s favour the amount is paid to them again.",
             "Raising disputes to avoid paying for coaching you received is a breach of these terms and can lead to your account being closed.",
         ]) + "<h3>For coaches: payouts and taxes</h3>" + ul([
             "To receive money you connect a payout account with Stripe from inside the app and accept Stripe’s Connected Account Agreement. Stripe may require identity and bank verification before you can be paid, and Stripe decides payout timing.",
             "Refunds you issue, and disputed amounts, are deducted from your Stripe balance or future payouts, including the platform fee on that payment.",
             "You are responsible for any tax on what you earn through Benchside and for any registration your local law requires of you as a seller.",
             "A pass sold through Benchside is delivered through Benchside. Do not use the Service to collect payment for anything other than the coaching the pass describes.",
         ])),
        ("elite", "6. Coach Elite and the App Store", ul([
            "<strong>Coach Elite</strong> is an optional subscription for coaches, $29.99 a month or $249 a year, bought on the web from your coach dashboard and paid through Stripe. It renews automatically at the end of each period until you cancel it. Manage or cancel it from the link in your Stripe receipt; Elite stays on until the end of the period you paid for. Deleting the app does not cancel it.",
            "<strong>Bought through Apple.</strong> If you bought Coach Elite as an in-app purchase, it is billed to your Apple Account, renews automatically unless you cancel it at least 24 hours before the end of the current period, and is managed in your Apple Account’s subscription settings. Refunds for it are handled by Apple under Apple’s terms; Benchside cannot issue them.",
            "<strong>Founding.</strong> A Founding spot gives a coach Coach Elite free for one year, starting with the first payment one of their athletes makes after the spot is granted. After that year, Elite continues at the standard price if the coach keeps it, or the coach moves to the free plan.",
            "While Elite or a Founding year is active Benchside charges you a lower platform fee on pass payments. The lower fee ends when Elite lapses.",
            "The app itself is licensed to you, not sold, for use on Apple devices you own or control, as Apple’s usage rules allow. This licence is between you and Benchside. Apple is not a party to these terms, has no obligation to provide maintenance or support for the app, and is not responsible for addressing any claim relating to the app or your use of it (including product liability, legal compliance and consumer protection claims) or any third-party claim that the app infringes intellectual property rights. Apple and its subsidiaries are third-party beneficiaries of this section and may enforce it. You confirm that you are not in a country subject to a U.S. government embargo and are not on any U.S. government list of prohibited or restricted parties.",
        ])),
        ("use", "7. Acceptable use", "<p>Use the Service for coaching and training. You agree not to:</p>" + ul([
            "break any law, or harass, threaten, abuse or discriminate against anyone;",
            "impersonate another person, claim qualifications you do not hold, or misrepresent a pass;",
            "upload content you have no right to share, including another person’s private information, photos or programmes;",
            "copy, resell or redistribute a coach’s programmes, workouts or messages outside the roster they were written for;",
            "access the Service by automated means, scrape it, probe or bypass its security, rate limits or access controls, or interfere with its operation;",
            "send unsolicited invitations or messages, or use the Service to advertise anything other than your own coaching;",
            "upload malware, or content that is sexually explicit, violent, or that promotes disordered eating or dangerous practices;",
            "use the Service to collect payments for anything other than the coaching a pass describes.",
        ]) + "<p>We may remove content and suspend or close accounts that break these rules.</p>"),
        ("content", "8. Content and ownership", ul([
            "<strong>Coaches own their programmes.</strong> The seasons, workouts, cues, meal plans, notes and messages a coach writes belong to that coach. You give Benchside a non-exclusive, worldwide, royalty-free licence to host, store, copy, display and transmit them so that we can run the Service: showing them to the athletes on your roster, on your public page, and in backups, for as long as they are on the Service.",
            "<strong>Athletes own their logs.</strong> Your logged sets, sessions, body weight, check-ins, photos and messages belong to you. You give Benchside the same licence so that we can run the Service, including showing them to the coach you train with. A coach you leave keeps their own record of the coaching they delivered to you, in the same way any business keeps its books.",
            "<strong>Using a coach’s programme.</strong> While you hold a pass you have a personal, non-transferable licence to use that coach’s programme for your own training. Do not share it or sell it.",
            "<strong>Public page.</strong> A coach’s name, photo, bio and passes are shown publicly on the link the coach shares. Share the link only if you want those things public.",
            "<strong>Benchside’s materials.</strong> The Service, its software, design, exercise catalogue and demonstration media belong to Benchside or its licensors. You may use them only through the Service, as these terms allow.",
            "<strong>The coach’s assistant.</strong> A coach may turn on an assistant that drafts replies from an athlete’s check-in text, after agreeing to it in the app. The coach reads and approves every message before it is sent; a draft is never sent on its own, and a draft is not medical advice.",
            "<strong>Feedback.</strong> If you send us ideas or suggestions we may use them without any obligation to you.",
        ])),
        ("health", "9. Health and safety",
         "<div class=\"callout\"><strong>Not medical advice.</strong> Nothing on Benchside, whether written by Benchside or by a coach, is medical advice, diagnosis or treatment. Coaches are not your doctor and neither is Benchside.</div>" + ul([
             "Talk to a physician before starting or changing a training programme, especially if you have a medical condition, an injury, are pregnant or have been inactive.",
             "Physical training carries a risk of injury. You choose the loads, the movements and the effort; you train at your own risk and stop if something hurts.",
             "If you feel chest pain, dizziness, shortness of breath or sudden pain, stop and seek medical care. In an emergency call your local emergency number. The app is not an emergency service and messages are not monitored for emergencies.",
             "Coaches: stay within what you are qualified to do and refer athletes to a medical professional when something is outside it.",
         ])),
        ("messages", "10. Messages and notifications", ul([
            "Messages between a coach and an athlete are private to the two of them. Benchside’s systems process them to deliver them, and we may review them where the law requires it or to investigate a report of abuse.",
            "Push notifications are optional and controlled in your device settings. We send service emails you cannot opt out of while you hold an account: sign-in codes, receipts and notices of important changes.",
        ])),
        ("ending", "11. Ending your account", ul([
            f"<strong>You can leave at any time.</strong> Delete your account from Profile in the app, or <a href=\"{DELETE}\">on the web</a>. Deletion is immediate and permanent; what is deleted and what we must keep for tax and accounting law is described there.",
            "<strong>Athletes.</strong> Deleting your account ends every pass you hold that day, before the account is deleted: it stops billing and does not renew, any unpaid amount on it is forgiven, and time already paid is not refunded. You see which passes end before you confirm, and your coach is told you left. If a pass cannot be ended, the account is not deleted.",
            "<strong>Coach Elite.</strong> Cancel Coach Elite before you delete your account: from the link in your Stripe receipt, or in your Apple Account if you bought it through Apple. Deleting your account does not cancel a subscription bought through Apple.",
            "<strong>Coaches.</strong> If you close your account, your athletes’ accounts are not deleted; their passes with you end. Time your athletes paid for and you have not yet delivered is refunded to them automatically from your Stripe balance when you close the account. If Stripe cannot issue one of those refunds, you remain responsible for it. A pass you hold yourself with another coach ends the same day, without a refund of time already paid.",
            "We may suspend or close an account that breaks these terms, is used for fraud or abusive chargebacks, puts other people at risk, or where the law requires it. Where it is practical and lawful we tell you first and give you a chance to put things right.",
            "Sections that by their nature should survive the end of an account (content licences for data we must keep, payment obligations, disclaimers, limitation of liability, indemnity, governing law) survive it.",
        ])),
        ("disclaimers", "12. Disclaimers", "<p>The Service is provided “as is” and “as available”. To the fullest extent the law allows, Benchside disclaims all warranties, express or implied, including fitness for a particular purpose, merchantability and non-infringement. We do not promise that the Service will be uninterrupted, error-free or secure, that any programme will produce a particular result, or that a coach’s content is accurate, safe or suitable for you. A coach’s content is the coach’s, not ours.</p>"),
        ("liability", "13. Limitation of liability",
         "<p>To the fullest extent the law allows, Benchside, its members, officers, employees and contractors are not liable to you for any indirect, incidental, special, consequential or punitive damages, or for loss of profits, data or goodwill, arising from your use of the Service or from the coaching you give or receive through it, however caused and under any theory of liability, even if we were told such damages were possible.</p>"
         "<p>To the same extent, Benchside’s total liability to you for all claims arising from the Service in any twelve-month period is limited to the greater of the platform fees Benchside earned from payments you made or received through the Service in that period, or one hundred US dollars (USD 100).</p>"
         "<p>Nothing in these terms limits liability that cannot be limited by law, including liability for death or personal injury caused by our negligence, for fraud, or your statutory rights as a consumer.</p>"),
        ("indemnity", "14. Indemnity", "<p>You will defend and indemnify Benchside against claims, losses and reasonable legal costs arising from your content, your coaching services (if you are a coach), your use of the Service in breach of these terms, or your breach of the law or of someone else’s rights.</p>"),
        ("law", "15. Governing law and disputes",
         "<p>These terms are governed by the laws of the State of New Jersey, USA, without regard to its conflict-of-law rules, and any dispute that cannot be resolved informally will be brought in the state or federal courts located in New Jersey. If you are a consumer, you keep any protection and any right to bring a claim in your home country that the law there gives you and that cannot be taken away by agreement.</p>"
         f"<p>Before starting any formal proceeding, write to us at <a href=\"mailto:{EMAIL}\">{EMAIL}</a> describing the problem and what you want; we will try to resolve it with you within 30 days.</p>"),
        ("changes", "16. Changes to these terms", "<p>We may update these terms as the Service changes. For a material change we give notice in the app or by email at least 14 days before it takes effect, unless the change is required by law or by a payment or platform partner, in which case it may take effect sooner. The date at the top shows when the current version took effect. Using the Service after a change takes effect means you accept it; if you do not, stop using the Service and delete your account.</p>"),
        ("contact", "17. Contact", ul([
            f"Support and questions about these terms: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>",
            f"Questions about your data: <a href=\"mailto:{EMAIL}\">{EMAIL}</a> · <a href=\"/privacy\">Privacy Policy</a>",
            "Refunds for a pass: ask your coach in the app. Coach Elite bought on the web: write to us. Bought through Apple: Apple, through your Apple Account.",
            f"{ENTITY}, New Jersey, USA.",
        ])),
    ]
    return legal_page("/terms", "Terms of Service",
                      "The terms for using Benchside as a coach or an athlete: passes, payments, refunds, Coach Elite, acceptable use, health and safety, and your account.",
                      S, plain)
