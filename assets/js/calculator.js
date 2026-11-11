/* SmartShield Security Calculator — 8 steps, demo pricing, WhatsApp share */
(function () {
  "use strict";
  var cfg = window.SMARTSHIELD_CONFIG || {};
  var state = { propertyType: "", size: "", floors: "", area: "", rooms: "", entrances: "", cameras: "", cameraType: "", tier: "Standard", features: [], retention: "", equipment: [], name: "", phone: "", city: "", requirements: "" };
  var steps = Array.prototype.slice.call(document.querySelectorAll(".calc-step"));
  var current = 0;
  var progressBar = document.getElementById("progress-bar");
  var stepLabel = document.getElementById("step-label");
  function show(i) {
    current = Math.max(0, Math.min(steps.length - 1, i));
    steps.forEach(function (s, idx) { s.classList.toggle("active", idx === current); });
    if (progressBar) progressBar.style.width = ((current + 1) / steps.length * 100) + "%";
    if (stepLabel) stepLabel.textContent = "Step " + (current + 1) + " of " + steps.length;
    window.scrollTo({ top: document.querySelector(".calc").offsetTop - 80, behavior: "smooth" });
  }
  function bindOptions(containerId, key, single) {
    var box = document.getElementById(containerId);
    if (!box) return;
    box.querySelectorAll(".opt, .chip").forEach(function (el) {
      el.addEventListener("click", function () {
        var val = el.getAttribute("data-value");
        if (single) {
          box.querySelectorAll(".opt, .chip").forEach(function (x) { x.classList.remove("selected"); });
          el.classList.add("selected"); state[key] = val;
          if (key === "cameras" && val === "custom") { document.getElementById("custom-cams-wrap").style.display = "block"; }
          if (key === "cameras" && val !== "custom") { document.getElementById("custom-cams-wrap").style.display = "none"; }
        } else {
          el.classList.toggle("selected");
          state[key] = Array.prototype.slice.call(box.querySelectorAll(".selected")).map(function (x) { return x.getAttribute("data-value"); });
        }
      });
    });
  }
  bindOptions("opt-property", "propertyType", true);
  bindOptions("opt-size", "size", true);
  bindOptions("opt-cameras", "cameras", true);
  bindOptions("opt-camtype", "cameraType", true);
  bindOptions("opt-tier", "tier", true);
  bindOptions("opt-features", "features", false);
  bindOptions("opt-retention", "retention", true);
  bindOptions("opt-equipment", "equipment", false);
  document.querySelectorAll("[data-next]").forEach(function (b) { b.addEventListener("click", function () { if (validate(current)) show(current + 1); }); });
  document.querySelectorAll("[data-prev]").forEach(function (b) { b.addEventListener("click", function () { show(current - 1); }); });
  function validate(i) {
    var need = { 0: ["propertyType"], 2: ["cameras"], 3: ["cameraType"], 5: ["retention"] };
    var missing = (need[i] || []).filter(function (k) { return !state[k]; });
    if (missing.length) { alert("Please select an option to continue."); return false; }
    return true;
  }
  /* Step 2 optional fields */
  ["floors", "area", "rooms", "entrances"].forEach(function (id) {
    var el = document.getElementById("f-" + id);
    if (el) el.addEventListener("input", function () { state[id] = el.value; });
  });
  /* Step 3 custom quantity + recommend */
  var recBtn = document.getElementById("recommend-btn");
  if (recBtn) recBtn.addEventListener("click", function () {
    var base = { "Residential Home": 4, "Villa": 6, "Office": 8, "Retail Shop": 4, "Warehouse": 8, "School": 12, "Hospital / Clinic": 8, "Factory": 12, "Restaurant": 6, "Commercial Building": 12, "Other": 4 };
    var n = base[state.propertyType] || 4;
    n += (parseInt(state.floors, 10) || 0) * 1;
    n += (parseInt(state.entrances, 10) || 0) * 1;
    var sizes = [2, 4, 6, 8, 12, 16];
    var pick = sizes.reduce(function (a, b) { return Math.abs(b - n) < Math.abs(a - n) ? b : a; });
    state.cameras = String(pick);
    document.querySelectorAll("#opt-cameras .opt").forEach(function (x) { x.classList.toggle("selected", x.getAttribute("data-value") === String(pick)); });
    document.getElementById("recommend-note").textContent = "Preliminary recommendation: " + pick + " cameras, based on property type, floors and entrances. This is a preliminary suggestion only — a site assessment is required to confirm the final quantity.";
    document.getElementById("recommend-note").style.display = "block";
  });
  /* Step 8 fields */
  ["name", "phone", "city", "requirements"].forEach(function (id) {
    var el = document.getElementById("f-" + id);
    if (el) el.addEventListener("input", function () { state[id] = el.value; });
  });
  /* Calculate */
  var calcBtn = document.getElementById("calculate-btn");
  if (calcBtn) calcBtn.addEventListener("click", function () {
    var camCount = state.cameras === "custom" ? (parseInt(document.getElementById("custom-cams").value, 10) || 4) : (parseInt(state.cameras, 10) || 4);
    var camPrice = (cfg.CAMERA_PRICES || {})[state.cameraType] || 14500;
    var tierMult = ((cfg.TIER_MULTIPLIER || {})[state.tier]) || 1;
    var camTotal = Math.round(camCount * camPrice * tierMult);
    var isIP = /IP|AI|Mixed/.test(state.cameraType);
    var recorder = isIP ? "NVR" : "DVR";
    var recorderPrice = (cfg.RECORDER_PRICES || {})[recorder] || 18000;
    var days = parseInt(state.retention, 10) || 15;
    var gbDay = ((cfg.STORAGE_GB_PER_CAM_PER_DAY || {})[state.cameraType]) || 20;
    var totalGB = camCount * gbDay * days;
    var tb = totalGB / 1024;
    var hddSize = tb <= 1 ? "1 TB" : tb <= 2 ? "2 TB" : tb <= 4 ? "4 TB" : tb <= 6 ? "6 TB" : "8 TB";
    var hddPrice = (cfg.HDD_PRICES || {})[hddSize] || 12000;
    var eq = state.equipment.slice();
    var eqTotal = 0, eqLines = [];
    eq.forEach(function (item) {
      if (item === "DVR / NVR" || item === "Hard Disk") return;
      var p = (cfg.EQUIPMENT_PRICES || {})[item] || 0;
      if (item === "Network Cabling") p = p * 15 * camCount;
      eqTotal += p; eqLines.push(item + " — PKR " + p.toLocaleString("en-PK"));
    });
    var install = camCount * (cfg.INSTALL_PER_CAMERA || 2500);
    var configFee = cfg.CONFIGURATION_CHARGE || 5000;
    var equipSubtotal = camTotal + recorderPrice + hddPrice;
    var total = equipSubtotal + eqTotal + install + configFee;
    var low = Math.round(total * 0.9), high = Math.round(total * 1.15);
    var advanced = state.features.indexOf("License Plate Recognition") >= 0 || state.features.indexOf("Human Detection") >= 0 && state.features.indexOf("Vehicle Detection") >= 0 || state.cameraType === "AI-Enabled Cameras";
    var smart = !advanced && (state.features.indexOf("Smart Alerts") >= 0 || state.features.indexOf("Color Night Vision") >= 0 || state.features.indexOf("Two-Way Audio") >= 0 || state.features.indexOf("Mobile Remote Viewing") >= 0);
    var tier = advanced ? "Advanced AI Security Package" : smart ? "Smart Security Package" : "Basic Security Package";
    var why = advanced ? "AI-enabled detection features were selected, so an AI-compatible camera and recorder setup is recommended." : smart ? "Smart monitoring features were selected, so a connected system with mobile viewing and alerts is recommended." : "Essential surveillance was selected, so a reliable standard camera system is recommended. No expensive equipment has been added where it is not required.";
    var r = document.getElementById("result");
    var fmt = function (n) { return "PKR " + n.toLocaleString("en-PK"); };
    document.getElementById("r-property").textContent = state.propertyType + (state.size ? " — " + state.size : "");
    document.getElementById("r-cameras").textContent = camCount + " × " + state.cameraType + " (" + state.tier + ")";
    document.getElementById("r-system").textContent = isIP ? "IP Camera System" : "HD Analog Camera System";
    document.getElementById("r-recorder").textContent = "Compatible " + recorder + " — " + fmt(recorderPrice);
    document.getElementById("r-storage").textContent = hddSize + " (about " + totalGB.toLocaleString("en-PK") + " GB for " + days + " days, indicative only — actual storage varies by equipment and recording settings)";
    document.getElementById("r-features").textContent = state.features.length ? state.features.join(", ") : "Recording & Playback";
    document.getElementById("r-equipment").textContent = eqLines.length ? eqLines.join("; ") : "Standard installation accessories";
    document.getElementById("r-equip-subtotal").textContent = fmt(equipSubtotal);
    document.getElementById("r-accessories").textContent = fmt(eqTotal);
    document.getElementById("r-install").textContent = fmt(install + configFee);
    document.getElementById("r-total").textContent = fmt(total);
    document.getElementById("r-range").textContent = "Indicative range: " + fmt(low) + " – " + fmt(high);
    document.getElementById("r-tier").textContent = tier;
    document.getElementById("r-why").textContent = why;
    document.getElementById("result").style.display = "block";
    document.getElementById("calc-form").style.display = "none";
    window._lastCalc = { camCount: camCount, recorder: recorder, hddSize: hddSize, days: days, total: total, low: low, high: high, tier: tier, equipSubtotal: equipSubtotal, eqTotal: eqTotal, install: install + configFee, fmt: fmt };
    window.scrollTo({ top: r.offsetTop - 80, behavior: "smooth" });
  });
  var modifyBtn = document.getElementById("modify-btn");
  if (modifyBtn) modifyBtn.addEventListener("click", function () { document.getElementById("result").style.display = "none"; document.getElementById("calc-form").style.display = "block"; show(0); });
  var restartBtn = document.getElementById("restart-btn");
  if (restartBtn) restartBtn.addEventListener("click", function () { location.reload(); });
  var waBtn = document.getElementById("whatsapp-btn");
  if (waBtn) waBtn.addEventListener("click", function () {
    var c = window._lastCalc || {};
    var lines = [
      "Hello SmartShield Security!", "",
      "I have created a CCTV security package using your website calculator.", "",
      "CUSTOMER DETAILS:",
      "Name: " + (state.name || "Not provided"),
      "Phone: " + (state.phone || "Not provided"),
      "Area: " + (state.city || "Lahore"), "",
      "PROPERTY DETAILS:",
      "Property Type: " + state.propertyType,
      "Property Size: " + (state.size || "Not specified"),
      "Floors: " + (state.floors || "Not specified"), "",
      "CAMERA REQUIREMENTS:",
      "Recommended Cameras: " + (c.camCount || ""),
      "Camera Type: " + state.cameraType + " (" + state.tier + ")",
      "Security Features: " + (state.features.length ? state.features.join(", ") : "Recording & Playback"), "",
      "RECORDING:",
      "Storage Duration: " + (state.retention ? state.retention + " days" : "Not specified"),
      "Recorder: " + (c.recorder || ""), "",
      "PACKAGE:",
      (c.tier || ""), "",
      "ESTIMATED BUDGET:",
      (c.fmt ? c.fmt(c.total) : "") + " (preliminary estimate, demo rates — not a final quotation)", "",
      "ADDITIONAL REQUIREMENTS:",
      (state.requirements || "None"), "",
      "Please review my requirements and provide a final quotation.", "",
      "Thank you.",
      "SmartShield Security Customer."
    ];
    window.open("https://wa.me/923059502580?text=" + encodeURIComponent(lines.join("\n")), "_blank");
  });
  show(0);
})();
