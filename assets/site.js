// Benchside marketing site — small progressive enhancements. Everything works without it.
(function () {
  "use strict";

  // Header hairline once the page scrolls
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Mobile menu
  var menuBtn = document.querySelector(".menu-btn");
  var mobileNav = document.getElementById("mobile-nav");
  if (menuBtn && mobileNav) {
    var setOpen = function (open) {
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      mobileNav.classList.toggle("open", open);
      document.body.style.overflow = open ? "hidden" : "";
    };
    menuBtn.addEventListener("click", function () { setOpen(menuBtn.getAttribute("aria-expanded") !== "true"); });
    mobileNav.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setOpen(false); });
    window.matchMedia("(min-width: 861px)").addEventListener("change", function (m) { if (m.matches) setOpen(false); });
  }

  // Reveal on scroll
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  // Pricing calculator
  var calc = document.getElementById("calc");
  if (calc) {
    var amount = document.getElementById("calc-amount");
    var range = document.getElementById("calc-range");
    var segBtns = calc.querySelectorAll(".seg button");
    var billing = "monthly";
    var money = function (n) {
      return "$" + n.toLocaleString("en-US", { minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2 });
    };
    var round2 = function (n) { return Math.round(n * 100) / 100; };
    var render = function () {
      var x = parseFloat(String(amount.value).replace(/[^0-9.]/g, "")) || 0;
      var eliteSub = billing === "monthly" ? 29.99 : round2(249 / 12);
      var free = round2(x * 0.9);
      var elite = round2(x * 0.95 - eliteSub);
      var founding = round2(x * 0.95);
      calc.querySelector("[data-k=free]").textContent = money(free);
      calc.querySelector("[data-f=free]").textContent = "10% fee: " + money(round2(x * 0.1));
      calc.querySelector("[data-k=elite]").textContent = money(elite);
      calc.querySelector("[data-f=elite]").textContent = "5% fee: " + money(round2(x * 0.05)) + " · Elite " + (billing === "monthly" ? "$29.99 a month" : "$249 a year (" + money(eliteSub) + " a month)");
      calc.querySelector("[data-k=founding]").textContent = money(founding);
      calc.querySelector("[data-f=founding]").textContent = "5% fee: " + money(round2(x * 0.05)) + " · no subscription in year one";
      var breakEven = round2(eliteSub / 0.05);
      var diff = round2(elite - free);
      var s = calc.querySelector(".calc-summary");
      if (x <= 0) { s.textContent = "Type what your athletes pay you in a month."; }
      else if (diff > 0) { s.textContent = "Elite leaves you " + money(diff) + " more a month than Free. It pays for itself above " + money(breakEven) + " a month in athlete payments."; }
      else { s.textContent = "At this amount Free leaves you more. Elite pays for itself above " + money(breakEven) + " a month in athlete payments."; }
      var cards = calc.querySelectorAll(".keep");
      cards.forEach(function (c) { c.classList.remove("best"); });
      var best = elite > free ? "elite" : "free";
      calc.querySelector(".keep[data-plan=" + best + "]").classList.add("best");
    };
    amount.addEventListener("input", function () {
      var v = parseFloat(String(amount.value).replace(/[^0-9.]/g, "")) || 0;
      range.value = Math.min(v, Number(range.max));
      render();
    });
    range.addEventListener("input", function () { amount.value = range.value; render(); });
    segBtns.forEach(function (b) {
      b.addEventListener("click", function () {
        billing = b.getAttribute("data-billing");
        segBtns.forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
        render();
      });
    });
    render();
  }

  // Help search
  var search = document.getElementById("help-search");
  if (search) {
    var items = document.querySelectorAll(".help-group details");
    var groups = document.querySelectorAll(".help-group");
    var empty = document.querySelector(".no-results");
    search.addEventListener("input", function () {
      var q = search.value.trim().toLowerCase();
      var shown = 0;
      items.forEach(function (d) {
        var hit = !q || d.textContent.toLowerCase().indexOf(q) !== -1;
        d.hidden = !hit;
        if (q && hit) d.open = true;
        if (!q) d.open = false;
        if (hit) shown++;
      });
      groups.forEach(function (g) { g.hidden = !g.querySelector("details:not([hidden])"); });
      if (empty) empty.style.display = shown ? "none" : "block";
    });
  }

  // Contact form: opens the visitor's email app, addressed to us
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var role = (form.querySelector("input[name=role]:checked") || {}).value || "Someone else";
      var email = form.querySelector("#c-email").value.trim();
      var msg = form.querySelector("#c-msg").value.trim();
      var subject = "Benchside help (" + role + ")";
      var body = msg + "\n\n—\nReply to: " + email + "\nI'm a: " + role;
      window.location.href = "mailto:" + form.getAttribute("data-to") + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
