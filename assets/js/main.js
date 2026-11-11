/* SmartShield Security — main site JS: mobile nav, social links, contact form */
(function () {
  "use strict";
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("open"); });
    });
  }
  /* Social links from the single config object */
  var cfg = window.SMARTSHIELD_CONFIG || {};
  var links = cfg.SOCIAL_LINKS || {};
  document.querySelectorAll("[data-social]").forEach(function (el) {
    var key = el.getAttribute("data-social");
    var url = links[key] || "";
    if (url) { el.setAttribute("href", url); el.classList.remove("is-placeholder"); }
    else {
      el.setAttribute("href", "#");
      el.addEventListener("click", function (e) { e.preventDefault(); alert("This social profile link is to be added by the business owner."); });
    }
  });
  /* Contact form -> WhatsApp (no email backend is connected) */
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = document.getElementById("cf-name").value.trim();
      var phone = document.getElementById("cf-phone").value.trim();
      var service = document.getElementById("cf-service").value;
      var area = document.getElementById("cf-area").value.trim();
      var msg = document.getElementById("cf-message").value.trim();
      if (!phone) { alert("Please enter your phone number so we can contact you."); return; }
      var text = "Hello SmartShield Security!\n\nI would like to enquire about your CCTV services.\n\nName: " + (name || "Not provided") +
        "\nPhone: " + phone + "\nService: " + service + "\nArea: " + (area || "Lahore") +
        "\n\nMessage:\n" + (msg || "Please contact me with details.");
      window.open("https://wa.me/923059502580?text=" + encodeURIComponent(text), "_blank");
    });
  }
  document.getElementById("year") && (document.getElementById("year").textContent = new Date().getFullYear());
})();
