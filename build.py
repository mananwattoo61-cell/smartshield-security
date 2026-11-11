#!/usr/bin/env python3
"""Build SmartShield Security static site. Run: python3 build.py"""
import os, json
ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://mananwattoo61-cell.github.io/smartshield-security"
PHONE = "03059502580"; WA = "https://wa.me/923059502580"

def head(title, desc, canon, prefix, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:type" content="website"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}/assets/images/hero-camera.svg">
<link rel="icon" type="image/svg+xml" href="{prefix}assets/images/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Manrope:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":["Organization","LocalBusiness"],"name":"SmartShield Security","url":"{BASE}/","telephone":"+92-305-9502580","priceRange":"PKR 12,500 - 155,500","areaServed":["Lahore, Pakistan","DHA Lahore","Gulberg","Johar Town","Model Town","Wapda Town","Bahria Town Lahore","Allama Iqbal Town","Lahore Cantonment","Township, Lahore"],"description":"CCTV camera installation and complete security solutions in Lahore, Pakistan."}}</script>
{extra}</head><body>
"""

NAV = [
 ("Home", "index.html"), ("About Us", "about/index.html"), ("Services", "services/index.html"),
 ("Packages", "packages/index.html"), ("Products", "products/index.html"), ("Contact Us", "contact/index.html"),
]
def header(prefix, active=""):
    links = "".join(f'<a href="{prefix}{u}" class="{"active" if a==active else ""}">{a}</a>' for a, u in NAV)
    return f"""<div class="topbar"><div class="container topbar-inner"><span>SmartShield Security &mdash; CCTV Installation in Lahore, Pakistan</span><span class="topbar-right"><a href="tel:+923059502580">Call {PHONE}</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp +92 305 9502580</a><span>WhatsApp Anytime</span></span></div></div>
<header class="site-header"><div class="container header-inner">
<a class="logo" href="{prefix}index.html"><img src="{prefix}assets/images/logo.svg" alt="SmartShield Security logo" width="40" height="40"><span>SmartShield<small>Security</small></span></a>
<button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">&#9776;</button>
<nav class="main-nav" aria-label="Main navigation">{links}</nav>
<div class="header-cta"><a class="btn btn-primary" href="{prefix}calculator/index.html">Get a Quote</a><a class="btn wa-btn" href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
</div></header>
"""

def footer(prefix):
    return f"""<footer class="site-footer"><div class="container"><div class="footer-grid">
<div><a class="logo" href="{prefix}index.html"><img src="{prefix}assets/images/logo.svg" alt="SmartShield Security logo" width="40" height="40"><span>SmartShield<small>Security</small></span></a>
<p style="margin-top:14px">SmartShield Security provides CCTV camera installation and complete security solutions in Lahore, Pakistan — modern cameras, professional installation, and reliable technical support.</p></div>
<div><h4>Quick Links</h4><p><a href="{prefix}index.html">Home</a><br><a href="{prefix}about/index.html">About Us</a><br><a href="{prefix}packages/index.html">CCTV Packages</a><br><a href="{prefix}products/index.html">CCTV Products</a><br><a href="{prefix}calculator/index.html">Smart Calculator</a><br><a href="{prefix}blog/index.html">Blog</a><br><a href="{prefix}projects/index.html">Projects</a><br><a href="{prefix}social-media/index.html">Social Media</a><br><a href="{prefix}contact/index.html">Contact Us</a></p></div>
<div><h4>Services</h4><p><a href="{prefix}services/cctv-installation/index.html">CCTV Installation</a><br><a href="{prefix}services/home-security/index.html">Home CCTV Security</a><br><a href="{prefix}services/office-security/index.html">Office Security</a><br><a href="{prefix}services/ip-camera-installation/index.html">IP Cameras</a><br><a href="{prefix}services/dvr-nvr-installation/index.html">DVR &amp; NVR</a><br><a href="{prefix}services/cctv-repair/index.html">CCTV Repair</a></p></div>
<div><h4>Contact</h4><p>Phone: <a href="tel:+923059502580">{PHONE}</a><br>WhatsApp: <a href="{WA}" target="_blank" rel="noopener">+92 305 9502580</a><br>Service area: Lahore, Pakistan<br><a href="{prefix}privacy-policy/index.html">Privacy Policy</a><br><a href="{prefix}terms/index.html">Terms &amp; Conditions</a></p></div>
</div><div class="footer-bottom">&copy; <span id="year">2026</span> SmartShield Security. All rights reserved. CCTV camera installation &amp; security solutions in Lahore, Pakistan.</div></div></footer>
<div class="sticky-cta" id="sticky-cta"><a href="{WA}" target="_blank" rel="noopener">WhatsApp Us</a></div>
<script src="{prefix}assets/js/pricing-config.js"></script><script src="{prefix}assets/js/main.js"></script>
</body></html>
"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)
    print("wrote", path)

def faq_block(faqs):
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'<section class="section"><div class="container faq"><p class="eyebrow">FAQs</p><h2>Frequently Asked Questions</h2><div class="faq-grid">{items}</div></div></section>'

def cta_block(prefix):
    return f"""<section class="section dark"><div class="container" style="text-align:center"><h2>READY TO SECURE YOUR PROPERTY?</h2>
<p style="max-width:640px;margin:10px auto">Talk to SmartShield Security about a CCTV setup for your home, office, or shop in Lahore.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="{prefix}contact/index.html">Contact SmartShield</a><a class="btn wa-btn" href="{WA}" target="_blank" rel="noopener">WhatsApp Us</a></div></div></section>"""

SERVICES = [
 ("cctv-installation", "CCTV Camera Installation in Lahore | SmartShield Security",
  "Professional CCTV camera installation in Lahore for homes, offices, shops and commercial properties. Modern cameras, clean cabling and full system testing.",
  "CCTV Camera Installation in Lahore", "cctv-installation",
  "We install complete CCTV systems for homes, offices, shops, warehouses and commercial buildings across Lahore. Every installation starts with understanding what needs to be covered — entrances, parking areas, cash counters, corridors and outdoor boundaries — and ends with a tested system you can view on your phone.",
  ["Site-based camera placement, not guesswork", "Neat, concealed cabling where possible", "DVR/NVR setup with recording and playback", "Mobile viewing configured before handover", "Testing of every camera before sign-off"],
  ["Share your requirements and property details", "We assess coverage needs and recommend a camera layout", "You receive a package and budget proposal", "Our team installs, configures and tests the system"]),
 ("home-security", "Home CCTV Installation Lahore | SmartShield Security",
  "Home CCTV installation in Lahore: indoor and outdoor cameras, night vision and mobile viewing for houses, villas and apartments — discreet setup.",
  "Home CCTV Security Installation in Lahore", "home-security",
  "A home system should protect the people inside without making the house feel like a fortress. We place cameras at entrances, driveways, gates and common areas, use indoor cameras only where you ask for them, and set up mobile viewing so you can check in while you are away.",
  ["Outdoor cameras for gates, driveways and boundaries", "Night vision for low-light areas", "Mobile viewing for the whole family", "Discreet camera placement", "Recording you can review at any time"],
  ["Tell us about your house, floors and entrances", "We recommend camera positions and a recorder", "Installation and mobile setup", "Walkthrough of viewing and playback"]),
 ("office-security", "Office CCTV Installation Lahore | SmartShield Security",
  "Office CCTV installation in Lahore: entrance, reception, workspace and server-room coverage with controlled access to recordings. Scales as your office grows.",
  "Office CCTV Security Systems in Lahore", "office-security",
  "Offices need coverage that protects staff, visitors and assets while respecting privacy in work areas. We design systems for reception areas, entrances, corridors, storage rooms and server areas, with recording access limited to the people you authorise.",
  ["Entrance and reception coverage", "Corridor and common-area monitoring", "Server and storage room cameras", "Controlled recording access", "Scalable systems as your office grows"],
  ["Share your office layout and coverage needs", "We plan camera positions and access rules", "Installation outside working hours where needed", "Handover with staff training on viewing"]),
 ("shop-commercial-security", "CCTV Installation for Shops in Lahore | SmartShield",
  "Shop and commercial CCTV installation in Lahore: cash counters, entrances, stock areas and customer floors with clear video for incident review.",
  "Shop & Commercial CCTV Installation in Lahore", "shop-commercial-security",
  "For shops and commercial premises, the camera positions that matter most are the cash counter, entrance, stock room and sales floor. We use cameras that give clear, usable video for reviewing incidents, and recorders sized for the retention period you need.",
  ["Cash counter and entrance cameras", "Stock room and storage coverage", "Clear video for incident review", "Retention matched to your needs", "Systems for single shops and multi-branch premises"],
  ["Tell us about your shop size and risk areas", "We recommend a camera layout and recorder", "Installation with minimal disruption to trading", "Testing and mobile viewing setup"]),
 ("ip-camera-installation", "IP Camera Installation Lahore | SmartShield Security",
  "IP camera installation in Lahore: high-resolution network cameras with Power over Ethernet, NVR recording and remote viewing over your network.",
  "IP Camera Installation in Lahore", "ip-camera-installation",
  "IP cameras send video over your network, which makes them a good fit for properties that need higher-resolution images, flexible camera placement and remote viewing. We plan the network side properly — PoE switching, cabling and recorder compatibility — so the system stays stable.",
  ["Higher-resolution video than analogue systems", "Power over Ethernet for simpler cabling", "Remote viewing over the network", "Easier to add cameras later", "Compatible NVR recording"],
  ["Check your network and coverage needs", "We specify compatible IP cameras and an NVR", "Cabling, PoE and recorder installation", "Network and mobile configuration"]),
 ("ai-camera-solutions", "AI CCTV Camera Solutions Lahore | SmartShield Security",
  "AI CCTV camera solutions in Lahore: human and vehicle detection, smart alerts and analytics — only where the camera and recorder support them.",
  "AI CCTV Camera Solutions in Lahore", "ai-camera-solutions",
  "AI-enabled cameras can reduce false alerts by distinguishing people and vehicles from routine movement — but only when the camera and the recorder both support the feature. We are clear about that: we recommend AI features where they are compatible and genuinely useful, and we do not promise analytics that your hardware cannot deliver.",
  ["Human and vehicle detection where supported", "Smart alerts to reduce false alarms", "Motion-based recording options", "Analytics matched to compatible hardware", "Honest advice on what AI can and cannot do"],
  ["Tell us what you want the system to detect", "We check camera and recorder compatibility", "We propose an AI-compatible package", "Installation, configuration and alert testing"]),
 ("dvr-nvr-installation", "DVR & NVR Installation Lahore | SmartShield Security",
  "DVR and NVR installation in Lahore: recorders, hard-disk storage, playback setup and recording retention planned around your cameras and needs.",
  "DVR & NVR Installation in Lahore", "dvr-nvr-installation",
  "The recorder is the part of the system you rely on when something happens — so it needs the right hard disk, the right retention period and a playback setup you can actually use. We install DVRs for analogue systems and NVRs for IP systems, and size storage around your camera count and retention needs.",
  ["DVR for analogue and NVR for IP systems", "Hard-disk storage sized to your retention period", "Playback and backup setup", "Remote viewing configuration", "Existing recorder replacement and upgrades"],
  ["Tell us your camera count and retention needs", "We specify a compatible recorder and hard disk", "Installation and storage configuration", "Playback walkthrough"]),
 ("cctv-repair", "CCTV Camera Repair in Lahore | SmartShield Security",
  "CCTV camera repair in Lahore: fast fault diagnosis for cameras, recorders, cabling, power supplies and remote viewing problems — homes and offices.",
  "CCTV Camera Repair in Lahore", "cctv-repair",
  "When a camera goes dark, a recorder stops saving footage or remote viewing stops working, the fault is usually in one place — a camera, a cable, a power supply or a setting. We diagnose the fault first, explain what is wrong, and repair or replace only what is needed.",
  ["Fault diagnosis before any replacement", "Camera, cable and power-supply repairs", "Recorder and hard-disk checks", "Remote viewing troubleshooting", "Clear explanation of the fault and the fix"],
  ["Describe the problem and your system", "We diagnose the fault on site", "You approve the repair before work starts", "Repair, testing and confirmation"]),
 ("cctv-maintenance", "CCTV Maintenance Services Lahore | SmartShield Security",
  "CCTV maintenance in Lahore: regular camera cleaning, recorder and storage checks, settings review and fault prevention for homes and offices.",
  "CCTV Maintenance in Lahore", "cctv-maintenance",
  "CCTV systems fail quietly — a lens gets dusty, a hard disk fills up, a camera drifts out of position. Regular maintenance catches those problems before footage is needed. We check cameras, connections, storage and recording, and report what was done and what needs attention.",
  ["Camera cleaning and re-alignment", "Recorder, hard-disk and storage checks", "Cable and power-supply inspection", "Settings and recording review", "A short report after each visit"],
  ["Tell us about your existing system", "We agree a maintenance schedule", "Scheduled checks and cleaning", "Report with any recommended fixes"]),
 ("remote-monitoring", "Remote CCTV Monitoring Lahore | SmartShield Security",
  "Remote CCTV monitoring setup in Lahore: view your cameras live on your phone, receive alerts and review recordings from anywhere, anytime. Alerts where supported.",
  "Remote CCTV Monitoring in Lahore", "remote-monitoring",
  "Remote monitoring means you can open your phone and see your property live, review recordings and receive alerts when the system is set up for them. We configure secure remote access on your recorder and phone, and show you how to use viewing and playback properly.",
  ["Live viewing on your phone", "Playback from anywhere", "Alerts where the system supports them", "Secure remote access setup", "Guided setup for your devices"],
  ["Tell us which devices you use", "We configure remote access on your recorder", "Phone setup and testing", "Walkthrough of viewing, alerts and playback"]),
]

# ---------- HOME ----------
def home():
    p = ""
    svc_cards = ""
    svc_meta = [
      ("cctv-installation","CCTV Camera Installation","Complete CCTV installation for homes, offices and shops in Lahore.","installation.svg","Modern CCTV camera installation"),
      ("home-security","Home CCTV Security","Indoor and outdoor cameras, night vision and mobile viewing for your home.","dome-camera.svg","Dome camera for home security"),
      ("office-security","Office Security Systems","Entrance, reception and workspace coverage with controlled recording access.","control-room.svg","Office security monitoring"),
      ("shop-commercial-security","Shop & Commercial Security","Cash counters, entrances and stock areas covered with clear, reviewable video.","bullet-camera.svg","Bullet camera for shops"),
      ("ip-camera-installation","IP Camera Installation","Network cameras with high-resolution video and PoE cabling.","ip-camera.svg","Smart IP camera"),
      ("dvr-nvr-installation","DVR & NVR Installation","Recorders and storage sized to your camera count and retention needs.","nvr-system.svg","NVR recording system"),
      ("cctv-repair","CCTV Camera Repair","Fault diagnosis and repair for cameras, recorders, cabling and power supplies.","installation.svg","CCTV repair and installation"),
      ("cctv-maintenance","CCTV Maintenance","Regular checks, cleaning and storage review to keep your system reliable.","ptz-camera.svg","PTZ camera maintenance"),
      ("remote-monitoring","Remote Mobile Monitoring","Live viewing, playback and alerts on your phone, wherever you are.","control-room.svg","Remote CCTV monitoring"),
      ("ai-camera-solutions","AI Camera Solutions","Human and vehicle detection where your camera and recorder support it.","hero-camera.svg","AI-enabled security camera"),
    ]
    for slug, t, d, img, alt in svc_meta:
        svc_cards += f'<article class="card service-card"><img src="assets/images/{img}" alt="{alt}" width="800" height="600" loading="lazy"><h3>{t}</h3><p>{d}</p><a class="btn btn-outline" href="services/{slug}/index.html">Learn more</a></article>'
    body = f"""
<main>
<section class="hero"><div class="container hero-grid"><div>
<p class="eyebrow">SmartShield Security — Lahore, Pakistan</p>
<h1>ADVANCED SECURITY. <span>SMARTER PROTECTION.</span></h1>
<p class="sub">Professional CCTV Camera Installation &amp; Security Solutions in Lahore</p>
<p>Protect your home, office, shop, and commercial property with modern surveillance systems, professional CCTV installation, smart monitoring, and reliable technical support.</p>
<div class="btn-row"><a class="btn btn-primary" href="contact/index.html">Get Free Security Consultation</a><a class="btn btn-ghost-light" href="calculator/index.html">Calculate Your CCTV Budget</a></div>
<div class="hero-badges"><span>Lahore, Pakistan</span><span>Professional Installation</span><span>Mobile Monitoring Setup</span></div>
</div><div class="hero-visual"><img src="assets/images/hero-camera.svg" alt="Premium AI-enabled surveillance camera overlooking a modern commercial building" width="800" height="600"><p style="color:#B9C9DC;margin-top:12px">AI-enabled surveillance, configured for your property — features depend on camera and recorder compatibility.</p></div></div></section>

<section class="section"><div class="container"><div class="grid grid-4">
<div class="card"><div class="icon">01</div><h3>Professional Installation</h3><p>Clean cabling, correct camera placement and full system testing before handover.</p></div>
<div class="card"><div class="icon">02</div><h3>Modern Security Technology</h3><p>IP, HD and AI-enabled cameras matched to what your property actually needs.</p></div>
<div class="card"><div class="icon">03</div><h3>Customized CCTV Solutions</h3><p>Camera layouts planned around your entrances, floors and coverage priorities.</p></div>
<div class="card"><div class="icon">04</div><h3>Technical Support</h3><p>Help with viewing, playback, repairs and maintenance after installation.</p></div>
</div></div></section>

<section class="section light"><div class="container"><p class="eyebrow">Our Security Services</p><h2>CCTV &amp; Security Services in Lahore</h2>
<p class="lead">Ten services, one team — from a first camera at home to a full commercial system.</p>
<div class="grid grid-3" style="margin-top:28px">{svc_cards}</div></div></section>

<section class="section dark"><div class="container" style="text-align:center"><p class="eyebrow">SmartShield Security Calculator</p><h2>BUILD YOUR CUSTOM CCTV SECURITY PACKAGE</h2>
<p style="max-width:680px;margin:10px auto;color:#B9C9DC">Tell us about your property and security requirements. Our smart calculator will recommend a suitable camera setup and provide an estimated project budget.</p>
<a class="btn btn-light" href="calculator/index.html">Build My Security Package</a>
<p style="margin-top:14px;color:#8FA3B8;font-size:.92rem">Preliminary estimate only — final pricing depends on site inspection. Demo rates are used until the business owner updates them.</p></div></section>

<section class="section"><div class="container"><p class="eyebrow">Why Choose SmartShield?</p><h2>Why Choose SmartShield Security?</h2>
<div class="grid grid-3" style="margin-top:24px">
<div class="card"><h3>Customized Security Planning</h3><p>Camera plans built around your property, not a fixed package.</p></div>
<div class="card"><h3>Modern Camera Solutions</h3><p>IP, HD, dome, bullet and PTZ cameras — chosen for the job, not the catalogue.</p></div>
<div class="card"><h3>Professional Installation</h3><p>Neat cabling, secure mounting and tested connections.</p></div>
<div class="card"><h3>Proper DVR/NVR Configuration</h3><p>Recording, retention and playback set up correctly from day one.</p></div>
<div class="card"><h3>Mobile Monitoring Setup</h3><p>Live viewing and playback on your phone, configured before handover.</p></div>
<div class="card"><h3>Maintenance &amp; Technical Assistance</h3><p>Repairs, checks and help when something stops working.</p></div>
</div></div></section>

<section class="section light"><div class="container"><p class="eyebrow">Camera Technology Showcase</p><h2>Camera Technology, Explained Honestly</h2>
<p class="lead">AI features depend on camera and recorder compatibility. We recommend what your hardware can actually deliver.</p>
<div class="grid grid-3" style="margin-top:24px">
<div class="card"><img src="assets/images/hero-camera.svg" alt="AI-enabled security camera" width="800" height="600" loading="lazy"><h3>AI-Enabled Cameras</h3><p>Human and vehicle detection and smart alerts — only where camera and recorder both support them.</p></div>
<div class="card"><img src="assets/images/ip-camera.svg" alt="Smart IP camera" width="800" height="600" loading="lazy"><h3>IP Cameras</h3><p>High-resolution network video with PoE cabling and remote viewing.</p></div>
<div class="card"><img src="assets/images/dome-camera.svg" alt="Modern dome camera" width="800" height="600" loading="lazy"><h3>Dome Cameras</h3><p>Discreet indoor coverage for homes, offices and shops.</p></div>
<div class="card"><img src="assets/images/bullet-camera.svg" alt="Premium bullet camera" width="800" height="600" loading="lazy"><h3>Bullet Cameras</h3><p>Long-range outdoor coverage for boundaries, driveways and entrances.</p></div>
<div class="card"><img src="assets/images/ptz-camera.svg" alt="PTZ surveillance camera" width="800" height="600" loading="lazy"><h3>PTZ Cameras</h3><p>Pan, tilt and zoom for wide areas that need active coverage.</p></div>
<div class="card"><img src="assets/images/nvr-system.svg" alt="Modern NVR recording system" width="800" height="600" loading="lazy"><h3>NVR Systems</h3><p>Network recording with storage sized to your retention period.</p></div>
</div></div></section>

<section class="section"><div class="container"><p class="eyebrow">How Our Process Works</p><h2>From First Call to Working System</h2><div class="steps" style="margin-top:24px">
<div class="step"><h3>Share Your Requirements</h3><p>Tell us about your property, entrances and what you want covered — by phone, WhatsApp or the calculator.</p></div>
<div class="step"><h3>Security Assessment</h3><p>We assess coverage needs and recommend camera positions and equipment.</p></div>
<div class="step"><h3>Package &amp; Budget Proposal</h3><p>You receive a recommended package and a preliminary budget estimate.</p></div>
<div class="step"><h3>Installation &amp; System Testing</h3><p>We install, configure recording and mobile viewing, and test every camera.</p></div>
</div></div></section>

<section class="section light"><div class="container"><p class="eyebrow">Recent Projects</p><h2>Recent Projects</h2>
<div class="placeholder"><p><strong>No project portfolio has been published yet.</strong></p><p>We do not publish invented customer projects. Completed projects will be added here with the customer's permission, including project type, location and installed camera system.</p><p><a href="projects/index.html">View the projects page</a></p></div></div></section>

<section class="section"><div class="container"><p class="eyebrow">Service Areas</p><h2>Serving Lahore</h2>
<p class="lead">SmartShield Security serves homes, offices and shops across Lahore, including:</p>
<div class="grid grid-3" style="margin-top:24px">
<div class="card"><h3>DHA Lahore</h3><p>Home and commercial CCTV installation.</p></div>
<div class="card"><h3>Gulberg</h3><p>Office and retail security systems.</p></div>
<div class="card"><h3>Johar Town</h3><p>Home CCTV and residential security.</p></div>
<div class="card"><h3>Model Town</h3><p>Home and office CCTV installation.</p></div>
<div class="card"><h3>Wapda Town</h3><p>Residential and commercial security.</p></div>
<div class="card"><h3>Bahria Town Lahore</h3><p>Home, villa and commercial CCTV systems.</p></div>
</div><p style="margin-top:16px">Service availability in other Lahore areas can be confirmed by phone or WhatsApp.</p></div></section>

<section class="section light"><div class="container"><p class="eyebrow">Customer Reviews</p><h2>What Customers Say</h2>
<div class="placeholder"><p><strong>Google reviews link to be added.</strong></p><p>We do not publish invented testimonials or star ratings. A link to our Google reviews will be added here once it is available.</p></div></div></section>
"""
    faqs = [
      ("How much does CCTV installation cost in Lahore?", "Cost depends on camera count, camera type, recorder, storage and cabling. Use the Smart Calculator for a preliminary estimate, then contact us for a final quotation after a site assessment."),
      ("How do I choose the right camera?", "It depends on indoor or outdoor use, distance, lighting and whether you need features such as night vision or AI detection. Tell us about your property and we will recommend a suitable setup."),
      ("Do AI cameras really detect people and vehicles?", "Only when the camera and the recorder both support the feature. We check compatibility before recommending AI detection, and we do not promise analytics your hardware cannot deliver."),
      ("Can I view my cameras on my phone?", "Yes — remote mobile viewing is configured as part of installation where your system supports it, and we show you how to use live viewing and playback."),
      ("What is the difference between DVR and NVR?", "A DVR works with analogue cameras; an NVR works with IP network cameras. The right choice depends on your camera system."),
      ("How long is installation?", "Most home and small-shop installations are completed in a day; larger commercial systems take longer. The timeline is confirmed in your proposal."),
      ("Do you repair existing CCTV systems?", "Yes — we diagnose faults in cameras, recorders, cabling and power supplies, and repair or replace only what is needed."),
      ("Do you provide maintenance?", "Yes — regular checks, cleaning, storage review and fault prevention are available for existing systems."),
      ("Which areas of Lahore do you serve?", "We serve DHA, Gulberg, Johar Town, Model Town, Wapda Town and Bahria Town Lahore, and other Lahore areas on confirmation."),
    ]
    body += faq_block(faqs) + cta_block("")
    import json as _json
    _faq_extra = '<script type="application/ld+json">' + _json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}) + "</script>"
    return head("CCTV Camera Installation Lahore | SmartShield Security",
      "SmartShield Security: CCTV camera installation in Lahore for homes, offices and shops. Modern cameras, clean installation and mobile monitoring.",
      BASE + "/", "", extra=_faq_extra) + header("", "Home") + body + "</main>" + footer("")

# ---------- SERVICE PAGES ----------
IMG_MAP = {"cctv-installation":"installation.svg","home-security":"dome-camera.svg","office-security":"control-room.svg","shop-commercial-security":"bullet-camera.svg","ip-camera-installation":"ip-camera.svg","ai-camera-solutions":"hero-camera.svg","dvr-nvr-installation":"nvr-system.svg","cctv-repair":"installation.svg","cctv-maintenance":"ptz-camera.svg","remote-monitoring":"control-room.svg"}
def service_page(slug, title, desc, h1, img, intro, benefits, steps):
    img = IMG_MAP.get(slug, "hero-camera.svg")
    p = "../../"
    canon = f"{BASE}/services/{slug}/"
    others = "".join(f'<li><a href="../{s}/index.html">{t}</a></li>' for s, t, _, _, _, _, _, _ in SERVICES if s != slug)
    faqs = [
      ("How much does this service cost?", "Pricing depends on the size of the job, equipment and installation requirements. Use the Smart Calculator for a preliminary estimate, then contact us for a final quotation after assessment."),
      ("How long does it take?", "Small jobs are usually completed in a day; larger systems take longer. The timeline is confirmed in your proposal."),
      ("Can I view the system on my phone?", "Yes, where your system supports remote viewing, we configure mobile access and show you how to use it."),
      ("Do you cover my area of Lahore?", "We serve DHA, Gulberg, Johar Town, Model Town, Wapda Town and Bahria Town Lahore, and other Lahore areas on confirmation."),
    ]
    guides_map = {
      "cctv-installation": [("Cost of CCTV Installation in Lahore", "../../blog/cost-of-cctv-camera-installation-in-lahore/index.html"), ("Home Security Camera Installation", "../../blog/home-security-camera-installation/index.html"), ("Bullet vs Dome Cameras", "../../blog/bullet-vs-dome-cctv-cameras/index.html")],
      "home-security": [("Home Security Camera Installation", "../../blog/home-security-camera-installation/index.html"), ("Cost of CCTV Installation in Lahore", "../../blog/cost-of-cctv-camera-installation-in-lahore/index.html"), ("Night Vision Camera Prices", "../../blog/night-vision-cctv-camera-price-in-pakistan/index.html")],
      "office-security": [("Office CCTV Installation Guide", "../../blog/office-cctv-installation/index.html"), ("DVR vs NVR", "../../blog/dvr-vs-nvr/index.html"), ("IP Camera Prices Guide", "../../blog/ip-camera-prices-guide/index.html")],
      "shop-commercial-security": [("CCTV Installation for Shops", "../../blog/cctv-installation-for-shops/index.html"), ("Cost of CCTV Installation in Lahore", "../../blog/cost-of-cctv-camera-installation-in-lahore/index.html"), ("Bullet vs Dome Cameras", "../../blog/bullet-vs-dome-cctv-cameras/index.html")],
      "ip-camera-installation": [("IP Camera Prices Guide", "../../blog/ip-camera-prices-guide/index.html"), ("DVR vs NVR", "../../blog/dvr-vs-nvr/index.html"), ("Hikvision vs Dahua", "../../blog/hikvision-vs-dahua-cctv-cameras/index.html")],
      "ai-camera-solutions": [("Hikvision vs Dahua", "../../blog/hikvision-vs-dahua-cctv-cameras/index.html"), ("Night Vision Camera Prices", "../../blog/night-vision-cctv-camera-price-in-pakistan/index.html"), ("IP Camera Prices Guide", "../../blog/ip-camera-prices-guide/index.html")],
      "dvr-nvr-installation": [("DVR vs NVR", "../../blog/dvr-vs-nvr/index.html"), ("IP Camera Prices Guide", "../../blog/ip-camera-prices-guide/index.html"), ("Cost of CCTV Installation in Lahore", "../../blog/cost-of-cctv-camera-installation-in-lahore/index.html")],
      "cctv-repair": [("Cost of CCTV Installation in Lahore", "../../blog/cost-of-cctv-camera-installation-in-lahore/index.html"), ("DVR vs NVR", "../../blog/dvr-vs-nvr/index.html"), ("Wireless Camera Price Guide", "../../blog/wireless-cctv-camera-price-guide/index.html")],
      "cctv-maintenance": [("DVR vs NVR", "../../blog/dvr-vs-nvr/index.html"), ("Home Security Camera Installation", "../../blog/home-security-camera-installation/index.html"), ("Office CCTV Installation Guide", "../../blog/office-cctv-installation/index.html")],
      "remote-monitoring": [("Wireless Camera Price Guide", "../../blog/wireless-cctv-camera-price-guide/index.html"), ("IP Camera Prices Guide", "../../blog/ip-camera-prices-guide/index.html"), ("Home Security Camera Installation", "../../blog/home-security-camera-installation/index.html")],
    }
    guides = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in guides_map.get(slug, guides_map["cctv-installation"]))
    extra = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Service","name":"{h1}","provider":{{"@type":"LocalBusiness","name":"SmartShield Security","telephone":"+92-305-9502580"}},"areaServed":"Lahore, Pakistan"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{BASE}/"}},{{"@type":"ListItem","position":2,"name":"Services","item":"{BASE}/services/cctv-installation/"}},{{"@type":"ListItem","position":3,"name":"{h1}","item":"{canon}"}}]}}</script>"""
    body = f"""
<main><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../../index.html">Home</a> &rsaquo; <a href="../cctv-installation/index.html">Services</a> &rsaquo; {h1}</nav></div>
<section class="section"><div class="container"><p class="eyebrow">SmartShield Security — Lahore</p><h1>{h1}</h1>
<p class="lead">{intro}</p>
<div class="btn-row"><a class="btn btn-primary" href="../../calculator/index.html">Calculate Your CCTV Budget</a><a class="btn wa-btn" href="{WA}" target="_blank" rel="noopener">WhatsApp Us</a></div>
<img src="{p}assets/images/{img}" alt="{h1} — SmartShield Security Lahore" width="800" height="600" loading="lazy" style="margin-top:28px;border-radius:14px">
<h2 style="margin-top:32px">What You Get</h2><ul class="checklist">{''.join(f'<li>{b}</li>' for b in benefits)}</ul>
<h2 style="margin-top:32px">How It Works</h2><div class="steps">{''.join(f'<div class="step"><h3>{s}</h3></div>' for s in steps)}</div>
<p class="note blue" style="margin-top:20px">AI detection, smart alerts and license plate recognition are only available where the selected camera and recorder support them. We confirm compatibility before recommending these features.</p>
<div class="related"><h2>Related Services</h2><ul>{others}</ul></div>
<div class="related"><h2>Related Guides</h2><ul>{guides}</ul></div>
</div></section>
"""
    body += faq_block(faqs) + cta_block(p)
    return head(title, desc, canon, p, extra) + header(p, "Services") + body + "</main>" + footer(p)

# ---------- SIMPLE PAGES ----------
def simple_page(path, title, desc, canon, h1, inner, prefix, crumbs=None):
    extra = ""
    crumb_html = ""
    if crumbs:
        import json as _json
        items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]
        extra = '<script type="application/ld+json">' + _json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}) + "</script>"
        links = " &rsaquo; ".join(f'<a href="{u}">{n}</a>' for n, u in crumbs[:-1]) + " &rsaquo; " + crumbs[-1][0]
        crumb_html = f'<div class="container"><nav class="breadcrumb" aria-label="Breadcrumb">{links}</nav></div>'
    return head(title, desc, canon, prefix, extra) + header(prefix) + f'<main>{crumb_html}<section class="section"><div class="container"><h1>{h1}</h1>{inner}</div></section></main>' + footer(prefix)

def build_all():
    write("index.html", home())
    for slug, title, desc, h1, img, intro, benefits, steps in SERVICES:
        write(f"services/{slug}/index.html", service_page(slug, title, desc, h1, img, intro, benefits, steps))
    # About
    write("about/index.html", simple_page("about/index.html",
      "About SmartShield Security | CCTV Installation Lahore",
      "About SmartShield Security — CCTV camera installation and complete security solutions in Lahore, Pakistan. How we plan, install and support systems.",
      BASE + "/about/", "About SmartShield Security",
      """<p class="lead">SmartShield Security provides CCTV camera installation and complete security solutions in Lahore, Pakistan.</p>
<p>We work with homes, offices, shops, schools, warehouses and commercial properties. Our focus is straightforward: the right cameras in the right places, installed neatly, configured properly, and supported after handover.</p>
<h2>What We Do</h2><ul class="checklist"><li>CCTV camera installation for homes, offices and shops</li><li>IP, HD and AI-enabled camera systems, where compatible</li><li>DVR and NVR installation and configuration</li><li>Remote mobile viewing setup</li><li>CCTV repair and maintenance</li></ul>
<h2>How We Work</h2><p>We start by understanding your property and what needs to be covered, recommend a camera layout and package, install and test the system, and show you how to use viewing and playback.</p>
<p>We do not publish invented experience claims, customer numbers or credentials. What we promise is careful planning, professional installation and honest advice about what your equipment can do.</p>
<p><a class="btn btn-primary" href="../calculator/index.html">Build Your CCTV Package</a> <a class="btn btn-outline" href="../contact/index.html">Contact Us</a></p>""", "../", [("Home", "../index.html"), ("About Us", "../about/index.html")]))
    # Projects
    write("projects/index.html", simple_page("projects/index.html",
      "Recent CCTV Projects in Lahore | SmartShield Security",
      "SmartShield Security CCTV projects in Lahore. No project portfolio has been published yet — completed projects will be added here soon. Meanwhile, see our services.",
      BASE + "/projects/", "Recent Projects",
      """<div class="placeholder"><p><strong>No project portfolio has been published yet.</strong></p><p>We do not invent customer projects. Completed projects will be added here with the customer's permission, including project type, location, installed camera system and a short description.</p></div>
<p style="margin-top:20px">If you would like to discuss a project for your property, <a href="../calculator/index.html">build a CCTV package</a> or <a href="../contact/index.html">contact us</a>.</p>""", "../", [("Home", "../index.html"), ("Projects", "../projects/index.html")]))
    # Social
    write("social-media/index.html", simple_page("social-media/index.html",
      "SmartShield Security on Social Media | CCTV Lahore",
      "Connect with SmartShield Security on Facebook, Instagram, TikTok, YouTube and LinkedIn — CCTV tips, new camera solutions and security updates.",
      BASE + "/social-media/", "CONNECT WITH SMARTSHIELD SECURITY",
      """<p class="lead">Follow SmartShield Security for CCTV tips, new camera solutions and security updates.</p>
<div class="social-grid" style="margin-top:24px">
<div class="card"><h3>Facebook</h3><p>Social profile link to be added.</p><a href="#" data-social="facebook" class="btn btn-outline">Facebook</a></div>
<div class="card"><h3>Instagram</h3><p>Social profile link to be added.</p><a href="#" data-social="instagram" class="btn btn-outline">Instagram</a></div>
<div class="card"><h3>TikTok</h3><p>Social profile link to be added.</p><a href="#" data-social="tiktok" class="btn btn-outline">TikTok</a></div>
<div class="card"><h3>YouTube</h3><p>Social profile link to be added.</p><a href="#" data-social="youtube" class="btn btn-outline">YouTube</a></div>
<div class="card"><h3>LinkedIn</h3><p>Social profile link to be added.</p><a href="#" data-social="linkedin" class="btn btn-outline">LinkedIn</a></div>
<div class="card"><h3>WhatsApp</h3><p>Chat with us directly on WhatsApp.</p><a href="https://wa.me/923059502580" target="_blank" rel="noopener" class="btn wa-btn">WhatsApp</a></div>
</div><p style="margin-top:16px">All social links are managed from one configuration file (SOCIAL_LINKS in assets/js/pricing-config.js) and can be updated by the business owner.</p>""", "../", [("Home", "../index.html"), ("Social Media", "../social-media/index.html")]))
    # Contact
    write("contact/index.html", simple_page("contact/index.html",
      "Contact SmartShield Security | CCTV Installation Lahore",
      "Contact SmartShield Security in Lahore: call 03059502580 or WhatsApp +92 305 9502580 for CCTV installation and security solutions. Get a free consultation.",
      BASE + "/contact/", "Contact SmartShield Security",
      """<p class="lead">SmartShield Security — CCTV Camera Installation &amp; Security Solutions, Lahore, Pakistan.</p>
<div class="grid grid-2"><div class="card"><h3>Call or WhatsApp</h3><p>Phone: <a href="tel:+923059502580">03059502580</a><br>WhatsApp: <a href="https://wa.me/923059502580" target="_blank" rel="noopener">+92 305 9502580</a></p>
<p><a class="btn btn-primary" href="tel:+923059502580">Call Now</a> <a class="btn wa-btn" href="https://wa.me/923059502580" target="_blank" rel="noopener">WhatsApp Us</a></p></div>
<div class="map-placeholder"><p><strong>Map placeholder</strong><br>Verified business location / Maps link to be added.<br>No office address is published.</p></div></div>
<h2 style="margin-top:32px">Send an Enquiry</h2>
<p>This form sends your enquiry via WhatsApp — no email backend is connected, so nothing is submitted to a server.</p>
<form id="contact-form" class="card">
<div class="field"><label for="cf-name">Name</label><input id="cf-name" type="text" autocomplete="name"></div>
<div class="field"><label for="cf-phone">Phone Number *</label><input id="cf-phone" type="tel" required autocomplete="tel"></div>
<div class="field"><label for="cf-service">Service</label><select id="cf-service"><option>CCTV Camera Installation</option><option>Home CCTV Security</option><option>Office Security Systems</option><option>Shop &amp; Commercial Security</option><option>IP Camera Installation</option><option>DVR &amp; NVR Installation</option><option>CCTV Camera Repair</option><option>CCTV Maintenance</option><option>Remote Monitoring</option><option>Other</option></select></div>
<div class="field"><label for="cf-area">City / Area</label><input id="cf-area" type="text" value="Lahore"></div>
<div class="field"><label for="cf-message">Message</label><textarea id="cf-message" rows="4"></textarea></div>
<button class="btn btn-primary" type="submit">Send via WhatsApp</button></form>""", "../", [("Home", "../index.html"), ("Contact Us", "../contact/index.html")]))
    # Privacy / Terms
    write("privacy-policy/index.html", simple_page("privacy-policy/index.html",
      "Privacy Policy | SmartShield Security, Lahore, Lahore",
      "Privacy policy for SmartShield Security, Lahore. How contact details shared through the website are used, stored and protected by us. Your details stay private.",
      BASE + "/privacy-policy/", "Privacy Policy",
      """<p>SmartShield Security respects your privacy. This page explains what happens to information you share with us through this website.</p>
<h2>Information You Share</h2><p>When you use the calculator or contact form, you may share your name, phone number, area and property details. That information is used only to prepare a quotation and contact you about your enquiry.</p>
<h2>WhatsApp</h2><p>Enquiries and calculator results are shared by you through WhatsApp. Once you send a WhatsApp message, WhatsApp's own privacy terms also apply.</p>
<h2>What We Do Not Do</h2><p>We do not sell your contact details, and we do not use tracking that identifies you personally beyond normal website analytics, if any are added in future.</p>
<p>Contact us on <a href="tel:+923059502580">03059502580</a> with any privacy question.</p>""", "../", [("Home", "../index.html"), ("Privacy Policy", "../privacy-policy/index.html")]))
    write("terms/index.html", simple_page("terms/index.html",
      "Terms & Conditions | SmartShield Security Lahore Lahore",
      "Terms and conditions for SmartShield Security CCTV services in Lahore: estimates, services, warranties and how to contact us. Read before using our services.",
      BASE + "/terms/", "Terms & Conditions",
      """<p>These terms apply to CCTV and security services provided by SmartShield Security in Lahore, Pakistan.</p>
<h2>Estimates</h2><p>Calculator results are preliminary estimates based on demo rates, not final quotations. Final pricing depends on site inspection, cable length, equipment availability and installation requirements.</p>
<h2>Services</h2><p>Services are provided as agreed in the package proposal. Equipment features, including AI detection, depend on the compatibility of the camera and recorder supplied.</p>
<h2>Contact</h2><p>For questions about these terms, contact SmartShield Security on <a href="tel:+923059502580">03059502580</a> or via <a href="https://wa.me/923059502580">WhatsApp</a>.</p>""", "../", [("Home", "../index.html"), ("Terms & Conditions", "../terms/index.html")]))
    # 404
    write("404.html", head("Page Not Found | SmartShield Security Lahore Lahore", "The page you are looking for does not exist. Return to the SmartShield Security homepage or build your CCTV package in Lahore. Or call 03059502580.", BASE + "/404.html", "") + header("") + '<main><section class="section"><div class="container" style="text-align:center"><h1>Page Not Found</h1><p>Sorry — that page does not exist or has moved.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="index.html">Go to Homepage</a><a class="btn btn-outline" href="calculator/index.html">Smart Calculator</a></div></div></section></main>' + footer(""))
    # robots, sitemap, readme, nojekyll
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: " + BASE + "/sitemap.xml\n")
    urls = ["", "about/", "calculator/", "projects/", "social-media/", "contact/", "privacy-policy/", "terms/"] + [f"services/{s}/" for s, *_ in SERVICES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'  <url><loc>{BASE}/{u}</loc><lastmod>2026-11-11</lastmod></url>\n' for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write(".nojekyll", "")
    write("README.md", "# SmartShield Security\n\nCCTV camera installation & complete security solutions — Lahore, Pakistan.\n\nPhone: 03059502580 | WhatsApp: +92 305 9502580\n\n## Hosting\nStatic site for GitHub Pages. Base URL: https://mananwattoo61-cell.github.io/smartshield-security/\n\n## Pricing\nCalculator prices are DEMO rates in `assets/js/pricing-config.js` (`DEMO_MODE: true`).\nUpdate them before publishing real prices. The result screen always states that\nthe figure is a preliminary estimate, not a final quotation.\n\n## Social links\nEdit `SOCIAL_LINKS` in `assets/js/pricing-config.js`. Empty = link to be added.\n\n## Local test\n`python3 -m http.server 8000` from this folder, then open http://localhost:8000/\n")


# ---------- CALCULATOR PAGE (appended) ----------
def opt_grid(id_, options, cls="opt"):
    items = "".join(f'<button type="button" class="{cls}" data-value="{v}">{label}</button>' for v, label in options)
    return f'<div class="opt-grid" id="{id_}">{items}</div>'

def calculator_page():
    p = "../"
    steps_html = ""
    # Step 1
    steps_html += f'''<div class="calc-step active"><h2>What type of property do you want to secure?</h2>
{opt_grid("opt-property", [("Residential Home","Residential Home"),("Villa","Villa"),("Office","Office"),("Retail Shop","Retail Shop"),("Warehouse","Warehouse"),("School","School"),("Hospital / Clinic","Hospital / Clinic"),("Factory","Factory"),("Restaurant","Restaurant"),("Commercial Building","Commercial Building"),("Other","Other")])}
<div class="calc-nav"><span></span><button type="button" class="btn btn-primary" data-next>Next</button></div></div>'''
    # Step 2
    steps_html += f'''<div class="calc-step"><h2>Property size</h2><p>Select a size. Extra details are optional and help the recommendation.</p>
{opt_grid("opt-size", [("Small","Small"),("Medium","Medium"),("Large","Large"),("Custom Size","Custom Size")])}
<div class="field"><label for="f-floors">Number of floors (optional)</label><input id="f-floors" type="number" min="1" max="50"></div>
<div class="field"><label for="f-area">Approximate covered area (optional)</label><input id="f-area" type="text" placeholder="e.g. 10 marla, 2 kanal, 5000 sq ft"></div>
<div class="field"><label for="f-rooms">Number of rooms (optional)</label><input id="f-rooms" type="number" min="0"></div>
<div class="field"><label for="f-entrances">Number of entrances (optional)</label><input id="f-entrances" type="number" min="0"></div>
<p class="note">Property size alone does not determine camera requirements — entrances, floors and coverage priorities matter too.</p>
<div class="calc-nav"><button type="button" class="btn btn-outline" data-prev>Back</button><button type="button" class="btn btn-primary" data-next>Next</button></div></div>'''
    # Step 3
    steps_html += f'''<div class="calc-step"><h2>How many cameras do you need?</h2>
{opt_grid("opt-cameras", [("2","2 Cameras"),("4","4 Cameras"),("6","6 Cameras"),("8","8 Cameras"),("12","12 Cameras"),("16","16 Cameras"),("custom","Custom Quantity")])}
<div id="custom-cams-wrap" style="display:none" class="field"><label for="custom-cams">Custom quantity</label><input id="custom-cams" type="number" min="1" max="64" value="4"></div>
<button type="button" class="btn btn-outline" id="recommend-btn">Not Sure – Recommend for Me</button>
<p class="note" id="recommend-note" style="display:none;margin-top:12px"></p>
<div class="calc-nav"><button type="button" class="btn btn-outline" data-prev>Back</button><button type="button" class="btn btn-primary" data-next>Next</button></div></div>'''
    # Step 4
    steps_html += f'''<div class="calc-step"><h2>Camera type</h2>
{opt_grid("opt-camtype", [("HD Analog Cameras","HD Analog Cameras"),("IP Cameras","IP Cameras"),("AI-Enabled Cameras","AI-Enabled Cameras"),("Dome Cameras","Dome Cameras"),("Bullet Cameras","Bullet Cameras"),("PTZ Cameras","PTZ Cameras"),("Mixed Camera Setup","Mixed Camera Setup")])}
<h3>Package tier</h3>
{opt_grid("opt-tier", [("Budget-Friendly","Budget-Friendly"),("Standard","Standard"),("Premium","Premium")])}
<p class="note">Actual AI detection features depend on camera and recorder compatibility.</p>
<div class="calc-nav"><button type="button" class="btn btn-outline" data-prev>Back</button><button type="button" class="btn btn-primary" data-next>Next</button></div></div>'''
    # Step 5
    feats = ["Night Vision","Color Night Vision","Human Detection","Vehicle Detection","Motion Detection","Two-Way Audio","Mobile Remote Viewing","Recording & Playback","Indoor Monitoring","Outdoor Monitoring","Smart Alerts","License Plate Recognition"]
    chips = "".join(f'<button type="button" class="chip" data-value="{f}">{f}</button>' for f in feats)
    steps_html += f'''<div class="calc-step"><h2>Security requirements</h2><p>Select all that apply.</p>
<div class="chip-grid" id="opt-features">{chips}</div>
<p class="note">License Plate Recognition is only available when the selected system supports it. We confirm compatibility before recommending it.</p>
<div class="calc-nav"><button type="button" class="btn btn-outline" data-prev>Back</button><button type="button" class="btn btn-primary" data-next>Next</button></div></div>'''
    # Step 6
    steps_html += f'''<div class="calc-step"><h2>How long do you want to store video recordings?</h2>
{opt_grid("opt-retention", [("7","7 Days"),("15","15 Days"),("30","30 Days"),("60","60 Days"),("15","Not Sure")])}
<p class="note">Storage is estimated from camera count, resolution, frame rate and compression assumptions. Actual storage varies by equipment and recording settings.</p>
<div class="calc-nav"><button type="button" class="btn btn-outline" data-prev>Back</button><button type="button" class="btn btn-primary" data-next>Next</button></div></div>'''
    # Step 7
    equip = ["DVR / NVR","Hard Disk","PoE Switch","Network Cabling","Power Supply","UPS / Backup","Installation Accessories","Mobile Configuration","Additional Monitors"]
    chips2 = "".join(f'<button type="button" class="chip" data-value="{e}">{e}</button>' for e in equip)
    steps_html += f'''<div class="calc-step"><h2>Additional equipment</h2><p>Select what you need. Only equipment compatible with your selected camera system is recommended.</p>
<div class="chip-grid" id="opt-equipment">{chips2}</div>
<div class="calc-nav"><button type="button" class="btn btn-outline" data-prev>Back</button><button type="button" class="btn btn-primary" data-next>Next</button></div></div>'''
    # Step 8
    steps_html += f'''<div class="calc-step"><h2>Your details (optional)</h2><p>Contact details are optional until you request a quotation.</p>
<div class="field"><label for="f-name">Name</label><input id="f-name" type="text" autocomplete="name"></div>
<div class="field"><label for="f-phone">Phone Number</label><input id="f-phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="f-city">City / Area</label><input id="f-city" type="text" value="Lahore"></div>
<div class="field"><label for="f-requirements">Additional Requirements</label><textarea id="f-requirements" rows="3"></textarea></div>
<div class="calc-nav"><button type="button" class="btn btn-outline" data-prev>Back</button><button type="button" class="btn btn-primary" id="calculate-btn">Calculate My Package</button></div></div>'''

    result = '''<div id="result" style="display:none"><div class="quote-card"><div class="quote-head"><h3>SMARTSHIELD SECURITY</h3><p>YOUR CUSTOM CCTV SECURITY PLAN</p></div>
<div class="quote-body">
<div class="quote-row"><span>Property Type</span><strong id="r-property"></strong></div>
<div class="quote-row"><span>Recommended Cameras</span><strong id="r-cameras"></strong></div>
<div class="quote-row"><span>Camera System</span><strong id="r-system"></strong></div>
<div class="quote-row"><span>Recorder</span><strong id="r-recorder"></strong></div>
<div class="quote-row"><span>Storage</span><strong id="r-storage"></strong></div>
<div class="quote-row"><span>Security Features</span><strong id="r-features"></strong></div>
<div class="quote-row"><span>Additional Equipment</span><strong id="r-equipment"></strong></div>
<div class="quote-row"><span>Equipment Subtotal</span><strong id="r-equip-subtotal"></strong></div>
<div class="quote-row"><span>Accessories</span><strong id="r-accessories"></strong></div>
<div class="quote-row"><span>Installation &amp; Configuration</span><strong id="r-install"></strong></div>
<div class="quote-row total-row"><span>Estimated Total</span><strong id="r-total"></strong></div>
<p id="r-range" style="margin-top:10px"></p>
<p><strong>Recommended Package: <span id="r-tier"></span></strong></p><p id="r-why"></p>
<p class="note" style="margin-top:16px">THIS IS A PRELIMINARY ESTIMATE, NOT A FINAL QUOTATION. Final pricing depends on site inspection, cable length, equipment availability, and installation requirements.</p>
<p class="note blue">Demo rates — to be updated by the business owner. Prices shown use placeholder demo rates in PKR.</p>
<div class="btn-row"><button type="button" class="btn wa-btn" id="whatsapp-btn">Share This Package on WhatsApp</button><button type="button" class="btn btn-outline" id="modify-btn">Modify My Requirements</button><button type="button" class="btn btn-outline" id="restart-btn">Start a New Calculation</button></div>
</div></div></div>'''

    body = f"""<main><section class="section"><div class="container">
<p class="eyebrow">SmartShield Security Calculator</p><h1>CCTV Cost Calculator Lahore</h1>
<p class="lead">Use this free CCTV cost calculator for Lahore to build your custom CCTV security package. Tell us about your property and security requirements — the calculator recommends a suitable camera setup and gives you a preliminary budget estimate.</p>
<p>Planning a system? Compare <a href="../packages/index.html">CCTV packages in Lahore</a>, read the <a href="../blog/cost-of-cctv-camera-installation-in-lahore/index.html">CCTV installation cost guide</a>, or <a href="../contact/index.html">contact SmartShield Security</a>.</p>
<div class="calc" id="calc-form" style="margin-top:28px"><p id="step-label">Step 1 of 8</p><div class="progress"><div class="progress-bar" id="progress-bar"></div></div>
{steps_html}</div>
{result}
<p style="margin-top:20px"><a href="../services/cctv-installation/index.html">CCTV Installation</a> &middot; <a href="../contact/index.html">Contact Us</a></p>
</div></section></main>"""
    extra = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is the calculator price a final quotation?","acceptedAnswer":{"@type":"Answer","text":"No. It is a preliminary estimate based on demo rates. Final pricing depends on site inspection, cable length, equipment availability and installation requirements."}}]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://mananwattoo61-cell.github.io/smartshield-security/"},{"@type":"ListItem","position":2,"name":"CCTV Cost Calculator","item":"https://mananwattoo61-cell.github.io/smartshield-security/calculator/"}]}</script>'
    html = head("CCTV Cost Calculator Lahore | SmartShield Security",
      "CCTV cost calculator Lahore: build your custom CCTV package — choose property, cameras, recording and equipment for a preliminary estimate. Free to use, no sign-up.",
      BASE + "/calculator/", p, extra) + header(p, "Smart Calculator") + body + footer(p)
    # calculator.js must load after main.js in footer; add it before </body>
    html = html.replace("</body>", '<script src="../assets/js/calculator.js"></script>\n</body>')
    return html

# patch main entry: build calculator too
_orig_main = build_all
def build_all_with_calc():
    _orig_main()
    write("calculator/index.html", calculator_page())

if __name__ == "__main__":
    build_all_with_calc()
