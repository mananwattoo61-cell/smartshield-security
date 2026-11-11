#!/usr/bin/env python3
"""Extend SmartShield Security site: competitor-mirrored structure (own words, SmartShield brand).
Run: python3 extend_site.py  (builds the whole site via build.py, then adds new pages + sitemap)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B

ROOT = B.ROOT; BASE = B.BASE; WA = B.WA; PHONE = B.PHONE
head, header, footer, faq_block, cta_block, write = B.head, B.header, B.footer, B.faq_block, B.cta_block, B.write

def content_page(path, title, desc, h1, prefix, body_inner, faqs=None, crumbs=None, img=None, img_alt=""):
    """Generic content page. path like 'products/index.html', prefix '../' (depth 1) or '../../' (depth 2)."""
    canon = BASE + "/" + path.replace("index.html", "")
    extra = ""
    if faqs:
        import json
        ent = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
        extra += '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ent}) + "</script>"
    if crumbs:
        items = ", ".join('{"@type":"ListItem","position":%d,"name":"%s","item":"%s"}' % (i + 1, n, u) for i, (n, u) in enumerate(crumbs))
        extra += '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[' + items + "]}</script>"
    crumb_html = ""
    if crumbs:
        links = " &rsaquo; ".join(f'<a href="{u}">{n}</a>' for n, u in crumbs[:-1]) + " &rsaquo; " + crumbs[-1][0]
        crumb_html = f'<div class="container"><nav class="breadcrumb" aria-label="Breadcrumb">{links}</nav></div>'
    img_html = f'<img src="{prefix}assets/images/{img}" alt="{img_alt}" width="800" height="600" loading="lazy" style="margin-top:28px;border-radius:14px">' if img else ""
    body = f"<main>{crumb_html}<section class=\"section\"><div class=\"container\"><p class=\"eyebrow\">SmartShield Security — Lahore</p><h1>{h1}</h1>{img_html}{body_inner}</div></section>"
    if faqs:
        body += faq_block(faqs)
    body += cta_block(prefix) + "</main>"
    return head(title, desc, canon, prefix, extra) + header(prefix) + body + footer(prefix)

def price_note():
    return ('<p class="note blue"><strong>About prices on this page:</strong> package prices are listed exactly as '
            'published. Your final quotation is confirmed after a site assessment, because camera count, cable length, '
            'recorder and installation requirements differ for every property. Use the <a href="CALCPREFIXcalculator/index.html">Smart Calculator</a> '
            'for a preliminary estimate, then contact us for a final quotation.</p>')

def related_block(items):
    """Related-pages block. items: list of (label, href) with CALCPREFIX placeholders."""
    lis = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in items)
    return f'<div class="related"><h2>Related Pages</h2><ul>{lis}</ul></div>'

def pkg_card(name, res, price, features, prefix="", upgrades=None):
    feats = "".join(f"<li>{f}</li>" for f in features)
    up = f'<p class="pkg-upgrades"><strong>Upgrades:</strong> {upgrades}</p>' if upgrades else ""
    return (f'<article class="pkg"><div class="pkg-head"><h3>{name}</h3><p>{res}</p></div>'
            f'<div class="pkg-body"><div class="pkg-price">Rs {price}<small>one-time package price</small></div>'
            f'<ul class="checklist">{feats}</ul>{up}'
            f'<div class="btn-row"><a class="btn btn-primary" href="{prefix}calculator/index.html">Get an Estimate</a>'
            f'<a class="btn wa-btn" href="https://wa.me/923059502580" target="_blank" rel="noopener">WhatsApp Us</a></div></div></article>')

# Exact packages, as published (prices + features). Descriptions rewritten; numbers kept.
HOME_PKGS = [
 ("4 CCTV Camera Package — Full HD (2MP)", "2 Megapixel — 4 cameras", "40,500",
  ["1 XVR 4-port megapixel recorder", "500GB hard disk drive", "200 feet wire", "Complete installation", "Live mobile view", "1-year warranty", "Lifetime service"], None),
 ("4 CCTV Camera Package — 4K (5MP)", "5 Megapixel — 4 cameras", "57,400",
  ["1 XVR 4-port 5MP recorder", "500GB hard disk drive", "300 feet wire", "Complete installation", "Live mobile view", "1-year warranty", "Lifetime service"], None),
 ("4 CCTV Camera Package — Full 4K (8MP)", "8 Megapixel — 4 cameras", "98,400",
  ["1 XVR 8-port 8MP recorder", "500GB hard disk drive", "300 feet wire", "Complete installation", "Live mobile view", "1-year warranty", "Lifetime service"], None),
]
MP5_PKGS = [
 ("Affordable 2 CCTV Cameras Package — 4K (5MP)", "5MP — 2 cameras", "48,500",
  ["2 × 5MP CCTV cameras", "Day and night vision", "4-channel DVR supporting up to 5MP", "500GB hard drive", "12V DC 5A power supply", "Approximately 150 feet of copper cable", "Weatherproof (IP67)", "BNC connectors", "Live mobile viewing", "Professional installation", "1-year warranty"],
  "Colour Night Vision Rs 55,000 · With Audio Rs 62,900"),
 ("Best 4 CCTV Cameras Package — 4K (5MP)", "5MP — 4 cameras", "62,400",
  ["4 × 5MP CCTV cameras", "Day and night vision", "4-channel DVR supporting up to 5MP", "500GB hard drive", "12V DC 5A power supply", "Approximately 200 feet of copper cable", "BNC connectors", "IP67 weather-resistant cameras", "Live mobile viewing", "Professional installation", "1-year warranty"],
  "Colour Night Vision Rs 73,000 · With Audio Rs 78,500"),
 ("Professional 6 CCTV Cameras Package — 4K (5MP)", "5MP — 6 cameras", "81,500",
  ["6 × 5MP CCTV cameras", "Day and night vision", "8-channel DVR supporting up to 5MP", "500GB hard drive", "12V DC 5A power supply", "Approximately 300 feet of copper cable", "BNC connectors", "IP67 weather-resistant cameras", "Live mobile viewing", "Professional installation", "1-year warranty"],
  "Colour Night Vision Rs 109,000 · With Audio Rs 124,900"),
 ("Reliable 8 CCTV Cameras Package — 4K (5MP)", "5MP — 8 cameras", "59,400",
  ["8 × 5MP CCTV cameras", "Day and night vision", "8-channel DVR supporting up to 5MP", "1TB hard drive", "12V DC 5A power supply", "Approximately 500 feet of copper cable", "BNC connectors", "IP66 weather-resistant cameras", "Live mobile viewing", "Professional installation", "1-year warranty"],
  "Colour Night Vision Rs 110,500 · With Audio Rs 138,000"),
]
K4_PKGS = [
 ("2 CCTV Cameras Package — Full 4K (8MP)", "8MP — 2 cameras", "75,400",
  ["2 × 4K CCTV cameras (8.0MP)", "Day & night vision", "4-channel DVR up to 12.0MP", "500GB hard disk drive", "12V DC 5A power supply", "150 feet copper cable", "BNC connectors", "Waterproof camera (IP67)", "Live mobile view", "Free installation", "1-year warranty"], None),
 ("4 CCTV Cameras Package — Full 4K (8MP)", "8MP — 4 cameras", "95,000",
  ["4 × 4K CCTV cameras (8.0MP)", "Day & night vision", "4-channel DVR up to 12.0MP", "500GB hard disk drive", "12V DC 5A power supply", "150 feet copper cable", "Waterproof (IP67)", "BNC connectors", "Live mobile view", "Free installation", "1-year warranty"], None),
 ("6 CCTV Cameras Package — Full 4K (8MP)", "8MP — 6 cameras", "134,500",
  ["6 × 4K CCTV cameras (8.0MP)", "Day & night vision", "8-channel DVR up to 12.0MP", "500GB hard disk drive", "12V DC 5A power supply", "300 feet copper wire", "BNC connectors", "Waterproof camera (IP67)", "Live mobile view", "Free installation", "1-year warranty"], None),
 ("8 CCTV Cameras Package — Full 4K (8MP)", "8MP — 8 cameras", "155,500",
  ["8 × full 4K CCTV cameras (8.0MP)", "Day & night vision", "8-channel DVR up to 12.0MP", "500GB hard disk drive", "12V DC 5A power supply", "500 feet copper wire & BNC connectors", "Waterproof (IP67)", "2TB hard disk drive", "Live mobile view", "Free installation", "1-year warranty"], None),
]

def _cards_section(heading, intro, pkgs):
    cards = "".join(pkg_card(n, r, pr, f, prefix="CALCPREFIX", upgrades=u) for n, r, pr, f, u in pkgs)
    return f'<h2 style="margin-top:32px">{heading}</h2><p>{intro}</p><div class="grid grid-3" style="margin-top:16px">{cards}</div>'

PKG_CARDS_MAP = {
 "2mp-cctv-camera-price-in-lahore": _cards_section("2MP Package — As Listed", "The complete 4-camera 2MP package:", [HOME_PKGS[0]]),
 "5mp-cctv-camera-packages": _cards_section("5MP Packages — As Listed", "Four 5MP packages, by camera count:", MP5_PKGS),
 "4k-cctv-cameras-price-in-pakistan": _cards_section("4K Packages — As Listed", "Four full-4K (8MP) packages, by camera count:", K4_PKGS),
}

DEFAULT_RELATED = [("CCTV Packages", "CALCPREFIXpackages/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html"), ("CCTV Camera Installation in Lahore", "CALCPREFIXcctv-camera-installation-in-lahore/index.html"), ("Our Services", "CALCPREFIXservices/index.html")]
PRICING_RELATED = {
 "2mp-cctv-camera-price-in-lahore": [("CCTV Packages", "CALCPREFIXpackages/index.html"), ("5MP Camera Packages", "CALCPREFIX5mp-cctv-camera-packages/index.html"), ("Bullet vs Dome Cameras", "CALCPREFIXblog/bullet-vs-dome-cctv-cameras/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
 "5mp-cctv-camera-packages": [("CCTV Packages", "CALCPREFIXpackages/index.html"), ("2MP Camera Prices", "CALCPREFIX2mp-cctv-camera-price-in-lahore/index.html"), ("4K Camera Prices", "CALCPREFIX4k-cctv-cameras-price-in-pakistan/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
 "4k-cctv-cameras-price-in-pakistan": [("CCTV Packages", "CALCPREFIXpackages/index.html"), ("Night Vision Camera Prices", "CALCPREFIXblog/night-vision-cctv-camera-price-in-pakistan/index.html"), ("DVR vs NVR", "CALCPREFIXblog/dvr-vs-nvr/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
 "ip-camera-prices-in-lahore": [("IP Camera Installation", "CALCPREFIXservices/ip-camera-installation/index.html"), ("IP Camera Prices Guide", "CALCPREFIXblog/ip-camera-prices-guide/index.html"), ("CCTV Packages", "CALCPREFIXpackages/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
 "wireless-cctv-camera-price-in-lahore": [("Wireless Camera Price Guide", "CALCPREFIXblog/wireless-cctv-camera-price-guide/index.html"), ("CCTV Packages", "CALCPREFIXpackages/index.html"), ("Home Security Camera Installation", "CALCPREFIXblog/home-security-camera-installation/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
}
TOPIC_RELATED = {
 "cctv-camera-installation-in-lahore": [("CCTV Packages", "CALCPREFIXpackages/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html"), ("CCTV in DHA Lahore", "CALCPREFIXcctv-camera-installation-in-dha-lahore/index.html"), ("Cost of CCTV Installation", "CALCPREFIXblog/cost-of-cctv-camera-installation-in-lahore/index.html")],
 "cctv-maintenance-and-repair-in-lahore": [("CCTV Repair Service", "CALCPREFIXservices/cctv-repair/index.html"), ("CCTV Maintenance Service", "CALCPREFIXservices/cctv-maintenance/index.html"), ("DVR vs NVR", "CALCPREFIXblog/dvr-vs-nvr/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
 "biometric-attendance-machine-in-lahore": [("Office CCTV Installation", "CALCPREFIXblog/office-cctv-installation/index.html"), ("Office Security Systems", "CALCPREFIXservices/office-security/index.html"), ("CCTV Packages", "CALCPREFIXpackages/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
 "fire-alarm-systems": [("Alarm Systems", "CALCPREFIXalarm-systems/index.html"), ("CCTV Camera Installation in Lahore", "CALCPREFIXcctv-camera-installation-in-lahore/index.html"), ("CCTV Packages", "CALCPREFIXpackages/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
 "alarm-systems": [("Fire Alarm Systems", "CALCPREFIXfire-alarm-systems/index.html"), ("CCTV Camera Installation in Lahore", "CALCPREFIXcctv-camera-installation-in-lahore/index.html"), ("Home Security Camera Installation", "CALCPREFIXblog/home-security-camera-installation/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
}
BLOG_RELATED = {
 "cost-of-cctv-camera-installation-in-lahore": [("Smart Calculator", "CALCPREFIXcalculator/index.html"), ("CCTV Packages", "CALCPREFIXpackages/index.html"), ("2MP Camera Prices", "CALCPREFIX2mp-cctv-camera-price-in-lahore/index.html")],
 "dvr-vs-nvr": [("DVR & NVR Installation", "CALCPREFIXservices/dvr-nvr-installation/index.html"), ("IP Camera Prices Guide", "CALCPREFIXblog/ip-camera-prices-guide/index.html"), ("CCTV Packages", "CALCPREFIXpackages/index.html")],
 "bullet-vs-dome-cctv-cameras": [("Home Security Camera Installation", "CALCPREFIXblog/home-security-camera-installation/index.html"), ("CCTV Camera Installation", "CALCPREFIXservices/cctv-installation/index.html"), ("2MP Camera Prices", "CALCPREFIX2mp-cctv-camera-price-in-lahore/index.html")],
 "hikvision-vs-dahua-cctv-cameras": [("IP Camera Prices Guide", "CALCPREFIXblog/ip-camera-prices-guide/index.html"), ("IP Camera Installation", "CALCPREFIXservices/ip-camera-installation/index.html"), ("CCTV Products", "CALCPREFIXproducts/index.html")],
 "wireless-cctv-camera-price-guide": [("Wireless Camera Prices", "CALCPREFIXwireless-cctv-camera-price-in-lahore/index.html"), ("Home Security Camera Installation", "CALCPREFIXblog/home-security-camera-installation/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")],
 "ip-camera-prices-guide": [("IP Camera Prices in Lahore", "CALCPREFIXip-camera-prices-in-lahore/index.html"), ("IP Camera Installation", "CALCPREFIXservices/ip-camera-installation/index.html"), ("DVR vs NVR", "CALCPREFIXblog/dvr-vs-nvr/index.html")],
 "home-security-camera-installation": [("Home CCTV Security", "CALCPREFIXservices/home-security/index.html"), ("Cost of CCTV Installation", "CALCPREFIXblog/cost-of-cctv-camera-installation-in-lahore/index.html"), ("Bullet vs Dome Cameras", "CALCPREFIXblog/bullet-vs-dome-cctv-cameras/index.html")],
 "office-cctv-installation": [("Office Security Systems", "CALCPREFIXservices/office-security/index.html"), ("Biometric Attendance Machines", "CALCPREFIXbiometric-attendance-machine-in-lahore/index.html"), ("IP Camera Prices Guide", "CALCPREFIXblog/ip-camera-prices-guide/index.html")],
 "cctv-installation-for-shops": [("Shop & Commercial Security", "CALCPREFIXservices/shop-commercial-security/index.html"), ("Cost of CCTV Installation", "CALCPREFIXblog/cost-of-cctv-camera-installation-in-lahore/index.html"), ("Bullet vs Dome Cameras", "CALCPREFIXblog/bullet-vs-dome-cctv-cameras/index.html")],
 "night-vision-cctv-camera-price-in-pakistan": [("4K Camera Prices", "CALCPREFIX4k-cctv-cameras-price-in-pakistan/index.html"), ("Hikvision vs Dahua", "CALCPREFIXblog/hikvision-vs-dahua-cctv-cameras/index.html"), ("CCTV Packages", "CALCPREFIXpackages/index.html")],
}


def new_home():
    p = ""
    svc_cards = ""
    svc_meta = [
      ("cctv-installation", "CCTV Camera Installation", "Complete CCTV installation for homes, offices and shops in Lahore.", "installation.svg", "Modern CCTV camera installation"),
      ("home-security", "Home CCTV Security", "Indoor and outdoor cameras, night vision and mobile viewing for your home.", "dome-camera.svg", "Dome camera for home security"),
      ("office-security", "Office Security Systems", "Entrance, reception and workspace coverage with controlled recording access.", "control-room.svg", "Office security monitoring"),
      ("shop-commercial-security", "Shop & Commercial Security", "Cash counters, entrances and stock areas covered with clear, reviewable video.", "bullet-camera.svg", "Bullet camera for shops"),
      ("ip-camera-installation", "IP Camera Installation", "Network cameras with high-resolution video and PoE cabling.", "ip-camera.svg", "Smart IP camera"),
      ("dvr-nvr-installation", "DVR & NVR Installation", "Recorders and storage sized to your camera count and retention needs.", "nvr-system.svg", "NVR recording system"),
      ("cctv-repair", "CCTV Camera Repair", "Fault diagnosis and repair for cameras, recorders, cabling and power supplies.", "installation.svg", "CCTV repair and installation"),
      ("cctv-maintenance", "CCTV Maintenance", "Regular checks, cleaning and storage review to keep your system reliable.", "ptz-camera.svg", "PTZ camera maintenance"),
      ("remote-monitoring", "Remote Mobile Monitoring", "Live viewing, playback and alerts on your phone, wherever you are.", "control-room.svg", "Remote CCTV monitoring"),
      ("ai-camera-solutions", "AI Camera Solutions", "Human and vehicle detection where your camera and recorder support it.", "hero-camera.svg", "AI-enabled security camera"),
      ("fire-alarm-systems", "Fire Alarm Systems", "Smoke and heat detectors, alarm panels and sirens for early fire warning.", "fire-alarm.svg", "Fire alarm system"),
      ("alarm-systems", "Alarm Systems", "Burglar alarms, door and window sensors and motion detectors for your property.", "alarm-system.svg", "Burglar alarm system"),
    ]
    # Fire alarm / alarm pages live at top level, not under services/
    SVC_LINK_OVERRIDE = {"fire-alarm-systems": "fire-alarm-systems/index.html", "alarm-systems": "alarm-systems/index.html"}
    for slug, t, d, img, alt in svc_meta:
        link = SVC_LINK_OVERRIDE.get(slug, f"services/{slug}/index.html")
        svc_cards += f'<article class="card service-card"><img src="assets/images/{img}" alt="{alt}" width="800" height="600" loading="lazy"><h3>{t}</h3><p>{d}</p><a class="btn btn-outline" href="{link}">Learn more</a></article>'
    def _icon(inner):
        return f'<div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg></div>'
    def _check():
        return '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1E9E4A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/></svg>'
    # Hero photo: the GitHub connector only pushes UTF-8 text, so the binary
    # JPG cannot be pushed to the repo. Embed it as a data URI at build time
    # so the live home page shows the real photo with no extra upload.
    # (The file also lives at assets/images/hero-installation.jpg for later upload.)
    import base64 as _b64
    try:
        with open(os.path.join(ROOT, "assets/images/hero-installation.jpg"), "rb") as _f:
            _hero_src = "data:image/jpeg;base64," + _b64.b64encode(_f.read()).decode()
    except Exception:
        _hero_src = "assets/images/hero-camera.svg"
    pkg_cards = "".join(pkg_card(n, r, pr, f, prefix="", upgrades=u) for n, r, pr, f, u in HOME_PKGS)
    body = f"""
<main>
<section class="hero"><div class="container hero-grid"><div>
<p class="eyebrow">SmartShield Security — Lahore, Pakistan</p>
<h1>CCTV Camera Installation in Lahore</h1>
<p class="sub">Professional installation, honest advice and reliable support — for homes, offices and shops</p>
<p>SmartShield Security installs complete CCTV and security systems across Lahore. Every installation is planned around your property's layout and your security needs — not a fixed box package.</p>
<div class="btn-row"><a class="btn btn-primary" href="contact/index.html">Get Free Security Consultation</a><a class="btn btn-ghost-light" href="calculator/index.html">Calculate Your CCTV Budget</a></div>
<div class="hero-badges"><span>Lahore, Pakistan</span><span>Phone 03059502580</span><span>WhatsApp Anytime</span></div>
</div><figure class="hero-visual"><img src="{_hero_src}" alt="Professional technician installing a CCTV security camera on a modern home in Lahore" width="1400" height="933"><figcaption>Professional CCTV installation by SmartShield Security, Lahore.</figcaption></figure></div></section>

<section class="trust-strip"><div class="container trust-strip-inner">
<div class="trust-item">{_check()} Professional installation</div>
<div class="trust-item">{_check()} Genuine Branded Cameras</div>
<div class="trust-item">{_check()} Mobile viewing setup</div>
<div class="trust-item">{_check()} 1-year warranty on packages</div>
</div></section>

<section class="section"><div class="container"><p class="eyebrow">Security for Every Property</p><h2>CCTV for Homes, Offices &amp; Shops in Lahore</h2>
<div class="grid grid-3" style="margin-top:24px">
<div class="card"><img src="assets/images/dome-camera.svg" alt="Dome camera for home security" width="800" height="600" loading="lazy"><h3>For Homes</h3><p>Protect entrances, gates, driveways and boundaries. Discreet indoor cameras only where you ask for them, night vision for low light, and mobile viewing so you can check in while you are away.</p><p><a href="services/home-security/index.html">Home CCTV Security &rsaquo;</a></p></div>
<div class="card"><img src="assets/images/control-room.svg" alt="Office security monitoring" width="800" height="600" loading="lazy"><h3>For Offices</h3><p>Cover reception, entrances, corridors and server areas, with recording access limited to the people you authorise. Systems scale as your office grows.</p><p><a href="services/office-security/index.html">Office Security Systems &rsaquo;</a></p></div>
<div class="card"><img src="assets/images/bullet-camera.svg" alt="Bullet camera for shop security" width="800" height="600" loading="lazy"><h3>For Shops</h3><p>Cash counter, entrance, stock room and sales floor coverage with clear video you can actually review when something happens.</p><p><a href="services/shop-commercial-security/index.html">Shop &amp; Commercial Security &rsaquo;</a></p></div>
</div></div></section>

<section class="section light"><div class="container"><p class="eyebrow">Our Security Services</p><h2>CCTV &amp; Security Services in Lahore</h2>
<p class="lead">Twelve services, one team — from a first camera at home to a full commercial system. We also cover maintenance and repair, alarm systems, fire alarm systems and biometric attendance machines.</p>
<div class="grid grid-3 center-orphan" style="margin-top:28px">{svc_cards}</div>
<ul class="link-list"><li><a href="services/index.html">View all services &rsaquo;</a></li><li><a href="products/index.html">Browse CCTV products &rsaquo;</a></li><li><a href="cctv-camera-installation-in-lahore/index.html">CCTV installation in Lahore — full guide &rsaquo;</a></li></ul></div></section>

<section class="section light"><div class="container"><p class="eyebrow">CCTV Packages</p><h2>CCTV Camera Packages in Lahore</h2>
<p class="lead">Complete 4-camera packages with recorder, storage, cabling, professional installation and mobile viewing setup. Final price is confirmed after a site survey.</p>
<div class="grid grid-3" style="margin-top:24px">{pkg_cards}</div>
<div class="btn-row"><a class="btn btn-primary" href="packages/index.html">View All 11 Packages</a><a class="btn btn-outline" href="calculator/index.html">Get an Exact Estimate</a></div></div></section>

<section class="section"><div class="container"><p class="eyebrow">Why Choose SmartShield?</p><h2>Why Choose SmartShield Security?</h2>
<div class="grid grid-3" style="margin-top:24px">
<div class="card">{_icon('<path d="M12 2l8 3v6c0 5-3.5 9.5-8 11-4.5-1.5-8-6-8-11V5l8-3z"/><path d="M9 12l2 2 4-4"/>')}<h3>Planned Around Your Property</h3><p>Camera positions chosen for your entrances, floors and coverage priorities — not a generic kit.</p></div>
<div class="card">{_icon('<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>')}<h3>Modern Camera Solutions</h3><p>IP, HD, dome, bullet and PTZ cameras from trusted brands such as Hikvision, Dahua, IMOU and CP Plus.</p></div>
<div class="card">{_icon('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>')}<h3>Clean, Professional Installation</h3><p>Neat cabling, secure mounting and tested connections, with minimal disruption to your home or business.</p></div>
<div class="card">{_icon('<line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/>')}<h3>Proper DVR/NVR Configuration</h3><p>Recording, retention and playback set up correctly from day one — so footage is there when you need it.</p></div>
<div class="card">{_icon('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>')}<h3>Mobile Monitoring Setup</h3><p>Live viewing and playback on your phone, configured before handover, with a walkthrough of how to use it.</p></div>
<div class="card">{_icon('<circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>')}<h3>Maintenance &amp; Support</h3><p>Repairs, scheduled checks and help when something stops working — including systems installed by others.</p></div>
</div></div></section>

<section class="section light"><div class="container"><p class="eyebrow">Common Problems We Fix</p><h2>Why CCTV Systems Fail — and How We Avoid It</h2>
<p class="lead">Most CCTV problems are not caused by the camera itself, but by poor installation, wrong equipment or missing configuration. These are the faults we see most often in Lahore:</p>
<div class="grid grid-3" style="margin-top:24px">
<div class="card">{_icon('<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>')}<h3>Poor Video Quality</h3><p>Blurry or unclear footage usually comes from the wrong camera for the distance or lighting, dirty lenses, or low-quality cabling. We match resolution and lens to the area being covered.</p></div>
<div class="card">{_icon('<path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/>')}<h3>Unstable Connections</h3><p>Cameras that keep disconnecting are often caused by weak Wi-Fi, overloaded networks or poor power supply. We check the network and power before recommending wireless cameras.</p></div>
<div class="card">{_icon('<circle cx="12" cy="12" r="10"/><line x1="22" y1="12" x2="18" y2="12"/><line x1="6" y1="12" x2="2" y2="12"/><line x1="12" y1="6" x2="12" y2="2"/><line x1="12" y1="22" x2="12" y2="18"/>')}<h3>Bad Camera Angles</h3><p>A camera pointed at the wrong place records everything except the incident. Placement is planned around entrances, blind spots and the areas that actually matter.</p></div>
<div class="card">{_icon('<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>')}<h3>Power Outages &amp; Load Shedding</h3><p>When power drops, recording stops unless backup is planned. We discuss UPS and backup options so your system keeps recording during outages where possible.</p></div>
<div class="card">{_icon('<rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>')}<h3>Mobile App Not Connecting</h3><p>Remote viewing fails when recorder settings, network ports or app configuration are wrong. We configure and test mobile viewing on your own phone before handover.</p></div>
<div class="card">{_icon('<line x1="22" y1="12" x2="2" y2="12"/><path d="M5.45 5.11L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><line x1="6" y1="16" x2="6.01" y2="16"/><line x1="10" y1="16" x2="10.01" y2="16"/>')}<h3>Recording Failures</h3><p>Systems that do not record are usually let down by a full or faulty hard disk, wrong retention settings or a recorder fault. We size storage to your retention period and test recording before sign-off.</p></div>
</div></div></section>

<section class="section"><div class="container"><p class="eyebrow">Installation Process</p><h2>How to Set Up a CCTV Camera — Step by Step</h2>
<p class="lead">This is the process we follow on every SmartShield installation:</p>
<div class="steps steps-3" style="margin-top:24px">
<div class="step"><h3>Choose Camera Locations</h3><p>Cover entry points first — main gate, doors, driveway and cash counter — then boundaries, corridors and stock areas.</p></div>
<div class="step"><h3>Mount the Cameras</h3><p>Cameras are fixed securely with proper brackets at the right height and angle, sheltered from direct rain where possible.</p></div>
<div class="step"><h3>Connect to DVR/NVR or Wi-Fi</h3><p>Wired cameras connect to the recorder by cable; wireless cameras join your Wi-Fi network. Power over Ethernet is used for IP cameras where suitable.</p></div>
<div class="step"><h3>Power the System</h3><p>Power supplies are connected and checked. Backup power options are discussed for areas affected by outages.</p></div>
<div class="step"><h3>Test the Video Feed</h3><p>Every camera is checked live for picture quality, angle and night vision before the job is signed off.</p></div>
<div class="step"><h3>Set Up Mobile Viewing</h3><p>The viewing app is configured on your phone, live view and playback are tested, and we show you how to use them.</p></div>
</div>
<p style="margin-top:16px">Prefer to leave it to professionals? <a href="contact/index.html">Book an installation</a> or <a href="calculator/index.html">build your CCTV package</a>.</p></div></section>

<section class="section dark"><div class="container" style="text-align:center"><p class="eyebrow">Get an Exact Estimate in 2 Minutes</p><h2>BUILD YOUR CUSTOM CCTV SECURITY PACKAGE</h2>
<p style="max-width:680px;margin:10px auto;color:#B9C9DC">Answer 8 quick questions about your property and security requirements. The Smart Calculator recommends a suitable camera setup and gives you a preliminary budget estimate — then you can share it on WhatsApp.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="calculator/index.html">Open the Smart Calculator</a><a class="btn wa-btn" href="{WA}" target="_blank" rel="noopener">WhatsApp Us</a></div>
<p style="margin-top:14px;color:#8FA3B8;font-size:.92rem">Preliminary estimate only — final pricing depends on site inspection. Demo rates are used until the business owner updates them.</p></div></section>

<section class="section light"><div class="container"><p class="eyebrow">Pricing in Lahore</p><h2>What Does CCTV Installation Cost in Lahore?</h2>
<p class="lead">Prices vary with camera count, camera type, recorder, storage and cabling — so there is no single fixed price. As a guide, typical Lahore market ranges are:</p>
<div class="grid grid-3" style="margin-top:24px">
<div class="card"><h3>Installation from <span class="nowrap">PKR 12,500</span></h3><p>Professional installation for basic setups typically starts from PKR 12,500 in Lahore.</p><div class="btn-row"><a class="btn btn-outline" href="calculator/index.html">Get an Estimate</a></div></div>
<div class="card"><h3>Typical Installation Range</h3><p><span class="nowrap"><strong>PKR 12,500 – 50,000+</strong></span></p><p>Most home and small-shop installations fall in this range, depending on camera count, DVR/NVR system and mobile connectivity setup.</p><div class="btn-row"><a class="btn btn-outline" href="calculator/index.html">Get an Estimate</a></div></div>
<div class="card"><h3>4MP Camera</h3><p><span class="nowrap"><strong>PKR 6,000 – 12,000</strong></span></p><p>A 4MP CCTV camera in Pakistan typically costs between PKR 6,000 and PKR 12,000 depending on brand and features. Installation charges are separate.</p><div class="btn-row"><a class="btn btn-outline" href="calculator/index.html">Get an Estimate</a></div></div>
</div>
<p style="margin-top:16px">These are typical market ranges for guidance, not SmartShield fixed prices. Your final quotation is confirmed after a site assessment.</p>
<ul class="link-list"><li><a href="blog/cost-of-cctv-camera-installation-in-lahore/index.html">Cost of CCTV camera installation in Lahore</a></li><li><a href="2mp-cctv-camera-price-in-lahore/index.html">2MP camera prices</a></li><li><a href="ip-camera-prices-in-lahore/index.html">IP camera prices</a></li><li><a href="wireless-cctv-camera-price-in-lahore/index.html">Wireless camera prices</a></li></ul></div></section>

<section class="section"><div class="container"><p class="eyebrow">Camera Brands</p><h2>Trusted CCTV Brands in Pakistan</h2>
<p class="lead">For long-term reliability and clear footage, the brands most commonly recommended in Pakistan are:</p>
<div class="brand-chips"><span class="brand-chip">Hikvision</span><span class="brand-chip">Dahua</span><span class="brand-chip">IMOU</span><span class="brand-chip">CP Plus</span></div>
<p style="margin-top:20px">We recommend a brand based on your budget, the camera type you need and the features that matter to you — not on a single supplier.</p>
<p><a href="blog/hikvision-vs-dahua-cctv-cameras/index.html">Hikvision vs Dahua — full comparison &rsaquo;</a></p></div></section>

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

<section class="section"><div class="container"><p class="eyebrow">How Our Process Works</p><h2>From First Call to Working System</h2><div class="steps steps-4" style="margin-top:24px">
<div class="step"><h3>Share Your Requirements</h3><p>Tell us about your property, entrances and what you want covered — by phone, WhatsApp or the calculator.</p></div>
<div class="step"><h3>Security Assessment</h3><p>We assess coverage needs and recommend camera positions and equipment.</p></div>
<div class="step"><h3>Package &amp; Budget Proposal</h3><p>You receive a recommended package and a preliminary budget estimate.</p></div>
<div class="step"><h3>Installation &amp; System Testing</h3><p>We install, configure recording and mobile viewing, and test every camera.</p></div>
</div></div></section>

<section class="section light"><div class="container"><p class="eyebrow">Service Areas</p><h2>Serving Lahore</h2>
<p class="lead">SmartShield Security serves homes, offices and shops across Lahore, including:</p>
<div class="grid grid-3 center-orphan" style="margin-top:24px">
<div class="card"><h3>DHA Lahore</h3><p>Home and commercial CCTV installation.</p><p><a href="cctv-camera-installation-in-dha-lahore/index.html">CCTV in DHA Lahore &rsaquo;</a></p></div>
<div class="card"><h3>Gulberg</h3><p>Office and retail security systems.</p><p><a href="cctv-camera-installation-in-gulberg/index.html">CCTV in Gulberg &rsaquo;</a></p></div>
<div class="card"><h3>Johar Town</h3><p>Home CCTV and residential security.</p><p><a href="cctv-camera-installation-in-johar-town/index.html">CCTV in Johar Town &rsaquo;</a></p></div>
<div class="card"><h3>Allama Iqbal Town</h3><p>Home and shop CCTV installation.</p><p><a href="cctv-camera-installation-in-allama-iqbal-town/index.html">CCTV in Allama Iqbal Town &rsaquo;</a></p></div>
<div class="card"><h3>Model Town</h3><p>Home and office CCTV installation.</p><p><a href="cctv-camera-installation-in-lahore/index.html">CCTV in Model Town &rsaquo;</a></p></div>
<div class="card"><h3>Wapda Town</h3><p>Residential and commercial security.</p><p><a href="cctv-camera-installation-in-lahore/index.html">CCTV in Wapda Town &rsaquo;</a></p></div>
<div class="card"><h3>Bahria Town Lahore</h3><p>Home, villa and commercial CCTV systems.</p><p><a href="cctv-camera-installation-in-lahore/index.html">CCTV in Bahria Town Lahore &rsaquo;</a></p></div>
<div class="card"><h3>Lahore Cantonment (Cantt)</h3><p>Home and office CCTV installation.</p><p><a href="cctv-camera-installation-in-lahore/index.html">CCTV in Lahore Cantt &rsaquo;</a></p></div>
<div class="card"><h3>Township, Lahore</h3><p>Residential and commercial security.</p><p><a href="cctv-camera-installation-in-lahore/index.html">CCTV in Township, Lahore &rsaquo;</a></p></div>
</div><p style="margin-top:16px">Service availability in other Lahore areas can be confirmed by phone or WhatsApp.</p></div></section>

<section class="section"><div class="container"><p class="eyebrow">Contact SmartShield</p><h2>Talk to SmartShield Security Today</h2>
<div class="grid grid-2" style="margin-top:24px;align-items:start">
<div>
<p class="lead">Tell us about your property and we will help you choose the right CCTV setup for it.</p>
<div class="btn-row"><a class="btn btn-primary" href="tel:+923059502580">Call 03059502580</a><a class="btn wa-btn" href="{WA}" target="_blank" rel="noopener">WhatsApp Us</a></div>
</div>
<div class="card">
<h3>Contact Information</h3>
<p>Phone: <a href="tel:+923059502580">03059502580</a><br>WhatsApp: <a href="{WA}" target="_blank" rel="noopener">+92 305 9502580</a><br>Serving all of Lahore, Pakistan — WhatsApp anytime.</p>
<p><a href="calculator/index.html">Build your CCTV package in the Smart Calculator &rsaquo;</a></p>
</div>
</div></div></section>
"""
    faqs = [
      ("What is the cost of installing a CCTV camera?", "The cost depends on the camera type (wired or wireless), its resolution and how complex the installation is. In Lahore, professional installation for basic setups typically starts from PKR 12,500. The final price is confirmed after a site assessment, because cable length, camera positions and recorder requirements differ for every property."),
      ("How much does CCTV cost to install?", "CCTV installation prices in Lahore usually range between PKR 12,500 and PKR 50,000 or more, depending on the number of cameras, the DVR or NVR system and mobile connectivity setup. Customised packages are available for homes, offices and shops — use the Smart Calculator for a preliminary estimate."),
      ("How to set up a CCTV camera step by step?", "Choose camera locations covering entry points, mount the cameras with screws and brackets, connect them to the DVR/NVR or Wi-Fi, attach cables or configure the wireless connection, power the system and test the video feed, then set up mobile viewing through the app. For a hassle-free installation, professional fitting avoids the wiring and configuration mistakes that cause most faults."),
      ("How much to install CCTV at home?", "Home CCTV installation in Lahore typically starts at PKR 12,500 for a basic wireless setup. Costs increase with advanced features such as motion detection, night vision and mobile connectivity, and with the number of cameras and the size of the house."),
      ("Can I install CCTV cameras myself?", "Yes, you can install a CCTV camera yourself if you have the right tools and technical knowledge. However, professional installation ensures correct wiring, secure setup and mobile access without errors — and it is usually the safer choice for multi-camera systems."),
      ("Can home CCTV work without Wi-Fi?", "Yes. Wired CCTV systems record directly to DVR or NVR devices without any internet connection. Wi-Fi or internet is only required if you want remote viewing on your mobile phone."),
      ("Which home CCTV camera is best?", "For home security in Lahore, IMOU and Hikvision are among the most reliable choices, offering good performance, HD resolution and mobile connectivity. The best camera for your home still depends on indoor or outdoor use, distance and lighting."),
      ("What is the price of a 4MP CCTV camera in Pakistan?", "A 4MP CCTV camera in Pakistan typically costs between PKR 6,000 and PKR 12,000 depending on the brand and features. Installation charges are separate, and the final system price depends on the recorder, storage and cabling as well."),
      ("Is a Wi-Fi CCTV camera good?", "Yes. Wi-Fi CCTV cameras are convenient for homes and small offices. They offer easy setup, no heavy wiring and direct mobile app connectivity for remote monitoring — provided your Wi-Fi signal is strong where the cameras are placed."),
      ("Which CCTV camera brand is best in Pakistan?", "Some of the best CCTV camera brands in Pakistan include Hikvision, Dahua, IMOU and CP Plus. We recommend a brand based on your budget and requirements, for long-term reliability and clear footage."),
    ]
    body += faq_block(faqs) + cta_block("")
    return head("CCTV Camera Installation Lahore | SmartShield Security — Professional Team, Honest Pricing",
      "SmartShield Security: professional CCTV camera installation in Lahore for homes, offices and shops. Modern cameras, clean installation, mobile monitoring and honest pricing guidance.",
      BASE + "/", "") + header("", "Home") + body + "</main>" + footer("")

# ---------- NEW PAGES ----------
# Each entry: (path, title, desc, h1, prefix, inner_html, faqs, crumbs, img, img_alt)
# Inner HTML uses CALCPREFIX placeholder replaced with the right relative prefix to calculator.

def P(inner):
    return inner

NEW_PAGES = []

# --- Products ---
NEW_PAGES.append(("products/index.html",
 "CCTV Products in Lahore | Cameras, DVR & NVR | SmartShield Security",
 "CCTV products in Lahore: dome, bullet, PTZ, IP and Wi-Fi cameras, DVR and NVR recorders, hard disks and accessories from trusted brands.",
 "CCTV Products in Lahore", "../",
 """<p class="lead">SmartShield Security supplies and installs CCTV products chosen for your property — not a fixed kit. Below is an overview of the products we work with. Brands commonly recommended in Pakistan include Hikvision, Dahua, IMOU and CP Plus.</p>
<h2>Cameras</h2>
<div class="grid grid-3" style="margin-top:16px">
<div class="card"><img src="../assets/images/dome-camera.svg" alt="Dome CCTV camera" width="800" height="600" loading="lazy"><h3>Dome Cameras</h3><p>Discreet, wide-angle coverage for indoors — shops, offices, hallways and living areas.</p></div>
<div class="card"><img src="../assets/images/bullet-camera.svg" alt="Bullet CCTV camera" width="800" height="600" loading="lazy"><h3>Bullet Cameras</h3><p>Long-range outdoor coverage for boundaries, driveways, gates and entrances.</p></div>
<div class="card"><img src="../assets/images/ptz-camera.svg" alt="PTZ CCTV camera" width="800" height="600" loading="lazy"><h3>PTZ Cameras</h3><p>Pan, tilt and zoom for large open areas that need active, adjustable coverage.</p></div>
<div class="card"><img src="../assets/images/ip-camera.svg" alt="IP CCTV camera" width="800" height="600" loading="lazy"><h3>IP Cameras</h3><p>High-resolution network cameras with Power over Ethernet and remote viewing.</p></div>
<div class="card"><img src="../assets/images/hero-camera.svg" alt="AI-enabled CCTV camera" width="800" height="600" loading="lazy"><h3>AI-Enabled Cameras</h3><p>Human and vehicle detection and smart alerts — only where camera and recorder both support them.</p></div>
<div class="card"><img src="../assets/images/nvr-system.svg" alt="NVR recording system" width="800" height="600" loading="lazy"><h3>Wi-Fi Cameras</h3><p>Easy setup with no heavy wiring and direct mobile app connectivity — best where Wi-Fi signal is strong.</p></div>
</div>
<h2 style="margin-top:32px">Recorders &amp; Storage</h2>
<ul class="checklist"><li><strong>DVR</strong> — for analogue / HD camera systems</li><li><strong>NVR</strong> — for IP network camera systems</li><li><strong>Hard disks</strong> — sized to your camera count and retention period (7, 15, 30 or 60 days)</li><li><strong>PoE switches, power supplies, cabling and UPS backup</strong> — matched to your system</li></ul>
<h2 style="margin-top:32px">How to Choose</h2><p>Resolution, indoor or outdoor use, distance, lighting and whether you need night vision or AI features all affect the choice. Tell us about your property and we will recommend products that fit — then build a package in the <a href="CALCPREFIXcalculator/index.html">Smart Calculator</a> or <a href="CALCPREFIXcontact/index.html">contact us</a>.</p>
<p><a href="CALCPREFIX2mp-cctv-camera-price-in-lahore/index.html">2MP camera prices</a> &middot; <a href="CALCPREFIXip-camera-prices-in-lahore/index.html">IP camera prices</a> &middot; <a href="CALCPREFIXwireless-cctv-camera-price-in-lahore/index.html">Wireless camera prices</a> &middot; <a href="CALCPREFIX4k-cctv-cameras-price-in-pakistan/index.html">4K camera prices</a></p>""" + related_block([("CCTV Packages", "CALCPREFIXpackages/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html"), ("CCTV Camera Installation in Lahore", "CALCPREFIXcctv-camera-installation-in-lahore/index.html"), ("Our Services", "CALCPREFIXservices/index.html")]),
 [("Which CCTV camera brand is best in Pakistan?", "Hikvision, Dahua, IMOU and CP Plus are among the best-regarded brands in Pakistan for reliability and clear footage. The right brand for you depends on budget, camera type and the features you need."),
  ("Do you supply the cameras or only install them?", "We supply and install as a complete package, and we also install and configure systems where equipment is already available. The package proposal lists the equipment included."),
  ("Can I view my cameras on my phone?", "Yes, where your system supports remote viewing, we configure mobile access and show you how to use live viewing and playback.")],
 [("Home", "../index.html"), ("Products", "../products/index.html")], None, ""))

# --- Pricing pages ---
def pricing_page(slug, title, desc, h1, intro, factors, range_rows, extra_html, faqs):
    rows = "".join(f"<div class=\"card\"><h3>{a}</h3><p>{b}</p></div>" for a, b in range_rows)
    cards_html = PKG_CARDS_MAP.get(slug, "")
    inner = f"""<p class="lead">{intro}</p>
PRICENOTE
<h2>What Affects the Price?</h2><ul class="checklist">{''.join(f'<li>{f}</li>' for f in factors)}</ul>
<h2 style="margin-top:32px">Typical Price Ranges in Lahore</h2><div class="grid grid-3" style="margin-top:16px">{rows}</div>
<p style="margin-top:16px">These are typical market ranges for guidance, not SmartShield fixed prices. Final pricing is confirmed after a site assessment.</p>
{extra_html}
{cards_html}
<p style="margin-top:20px">Get a preliminary estimate in the <a href="CALCPREFIXcalculator/index.html">Smart Calculator</a>, or <a href="CALCPREFIXcontact/index.html">contact SmartShield Security</a> for a final quotation.</p>"""
    inner += related_block(PRICING_RELATED.get(slug, DEFAULT_RELATED))
    return (f"{slug}/index.html", title, desc, h1, "../", inner, faqs,
            [("Home", "../index.html"), (h1, f"../{slug}/index.html")], None, "")

NEW_PAGES.append(pricing_page("2mp-cctv-camera-price-in-lahore",
 "2MP CCTV Camera Price in Lahore | SmartShield Security",
 "2MP CCTV camera price in Lahore: what a 2MP camera costs, what affects the price, and how to choose a 2MP system for home or shop.",
 "2MP CCTV Camera Price in Lahore",
 "A 2MP camera records in Full HD (1080p) and is the most common choice for homes and small shops in Lahore. It gives clear video for entrances, rooms and counters at a lower cost than higher-resolution cameras — and it needs less storage than 4MP or 4K systems.",
 ["Camera brand and build quality", "Indoor dome or outdoor bullet housing", "Night vision range and lens type", "Recorder (DVR) and hard-disk size", "Cabling length and installation complexity"],
 [("2MP camera (typical)", "Entry-level 2MP cameras are the most affordable option in the Lahore market; exact price depends on brand and features."),
  ("Basic 2–4 camera setup", "Installation for basic setups typically starts from PKR 12,500 in Lahore."),
  ("4MP comparison", "A 4MP CCTV camera in Pakistan typically costs PKR 6,000–12,000; installation is separate.")],
 "<p>2MP is usually enough for a home entrance, a shop counter or an office corridor. If you need to read number plates or recognise faces at distance, consider a 4MP or higher-resolution camera instead — see our <a href=\"CALCPREFIXblog/bullet-vs-dome-cctv-cameras/index.html\">bullet vs dome guide</a> and the <a href=\"CALCPREFIX4k-cctv-cameras-price-in-pakistan/index.html\">4K camera price guide</a>.</p>",
 [("Is a 2MP camera good enough for home security?", "For most homes, yes. 2MP Full HD video is clear enough for entrances, driveways and rooms. Higher resolution mainly helps when you need fine detail at a distance."),
  ("How much does a 2MP CCTV camera cost in Lahore?", "Prices vary by brand, housing and features. As a reference, a 4MP camera in Pakistan typically costs PKR 6,000–12,000, and 2MP cameras generally cost less than 4MP models. Installation is charged separately."),
  ("Does a 2MP camera work at night?", "Most 2MP cameras include infrared night vision. Check the stated night vision range and whether the camera is placed where its infrared light can reach.")]))
NEW_PAGES.append(pricing_page("5mp-cctv-camera-packages",
 "5MP CCTV Camera Packages in Lahore | SmartShield Security",
 "5MP CCTV camera packages in Lahore: what a 5MP package includes, typical costs, and how 5MP compares with 2MP and 4MP systems.",
 "5MP CCTV Camera Packages in Lahore",
 "A 5MP camera package sits between 4MP and 4K: noticeably sharper than 2MP, with more detail for entrances, parking areas and shop floors, while needing less storage and bandwidth than a full 4K system. A typical package includes the cameras, a compatible DVR, a hard disk, power supply and cabling, plus installation.",
 ["Number of cameras in the package (2, 4, 8 or more)", "Camera type — dome, bullet or a mix", "DVR channel count and hard-disk size", "Cable length and installation complexity", "Mobile viewing and remote access setup"],
 [("2–4 camera 5MP package", "Small home and shop packages are the most common 5MP choice; prices vary by brand and recorder."),
  ("8 camera 5MP package", "For larger homes, offices and shops — more cameras, a bigger DVR and more storage."),
  ("Typical installation range", "CCTV installation in Lahore usually ranges between PKR 12,500 and PKR 50,000+ depending on cameras, recorder and mobile setup.")],
 "<p>Before choosing 5MP, check that the DVR supports 5MP recording — a recorder that only supports 2MP will not record the full 5MP picture. We confirm recorder compatibility in every package proposal. Compare with <a href=\"CALCPREFIX2mp-cctv-camera-price-in-lahore/index.html\">2MP prices</a> and <a href=\"CALCPREFIX4k-cctv-cameras-price-in-pakistan/index.html\">4K prices</a>.</p>",
 [("Is 5MP better than 4MP?", "Yes, slightly — 5MP records more detail than 4MP, which helps for faces and number plates at moderate distances. The difference is smaller than the jump from 2MP to 4MP."),
  ("What is included in a 5MP CCTV package?", "Usually the cameras, a compatible DVR, a hard disk sized to your retention period, power supply, cabling and installation, plus mobile viewing setup. The exact list is in your package proposal."),
  ("Does 5MP need more storage?", "Yes — higher resolution uses more hard-disk space for the same retention period. Storage is sized around your camera count and how many days you want to keep recordings.")]))
NEW_PAGES.append(pricing_page("4k-cctv-cameras-price-in-pakistan",
 "4K CCTV Cameras Price in Pakistan | SmartShield Security",
 "4K CCTV cameras price in Pakistan: what 4K cameras cost, when 4K is worth it, storage and recorder requirements.",
 "4K CCTV Cameras Price in Pakistan",
 "A 4K (8MP) camera records roughly four times the detail of a 2MP camera. That matters when you need to identify faces or read number plates from a distance — for example at a main gate, a parking area or a large commercial boundary. For a small room or a shop counter, 4K is often more than you need.",
 ["Camera brand, sensor and lens quality", "Recorder must support 4K — a 2MP DVR will not record 4K", "Hard-disk storage: 4K footage needs much more space", "Network and cabling quality for IP 4K systems", "Number of cameras and installation complexity"],
 [("4K camera (typical)", "4K cameras cost more than 2MP and 4MP models; the exact price depends on brand, sensor and features."),
  ("4MP comparison", "A 4MP CCTV camera in Pakistan typically costs PKR 6,000–12,000; 4K cameras sit above this range."),
  ("Full 4K system", "A complete 4K system costs more overall because the recorder and hard disk must also be 4K-capable.")],
 "<p>4K is worth it for large areas, long distances and high-security entrances. For most homes and small shops, a good 2MP or 4MP system gives clear, usable video at a lower total cost. Read <a href=\"CALCPREFIXblog/night-vision-cctv-camera-price-in-pakistan/index.html\">night vision camera prices</a> and our <a href=\"CALCPREFIXblog/dvr-vs-nvr/index.html\">DVR vs NVR guide</a> before deciding.</p>",
 [("Is a 4K CCTV camera worth it?", "It is worth it when you need fine detail at a distance — faces, number plates, large open areas. For small rooms and short distances, 2MP or 4MP is usually enough."),
  ("Do I need a special DVR for 4K cameras?", "Yes. The recorder must support 4K resolution, and the hard disk must be large enough for 4K footage at your chosen retention period."),
  ("Does 4K use more internet for remote viewing?", "Remote viewing uses bandwidth when you watch live or play back. 4K streams use more data than 2MP streams, so a stable connection matters.")]))
NEW_PAGES.append(pricing_page("ip-camera-prices-in-lahore",
 "IP Camera Prices in Lahore | SmartShield Security",
 "IP camera prices in Lahore: what IP cameras cost, what affects the price, and when an IP system is the right choice.",
 "IP Camera Prices in Lahore",
 "IP cameras send video over your network, which gives higher-resolution images, flexible placement and remote viewing. They cost more than analogue cameras, but they are the right choice for properties that need sharp video, Power over Ethernet cabling or a system that can grow camera by camera.",
 ["Resolution — 2MP, 4MP, 5MP or 4K", "Brand and build quality (Hikvision, Dahua, IMOU, CP Plus)", "PoE switch and network cabling", "NVR channel count and hard-disk size", "AI features — only where camera and NVR both support them"],
 [("IP camera (typical)", "IP cameras cost more than analogue cameras of the same resolution; price depends on brand and features."),
  ("4MP comparison", "A 4MP CCTV camera in Pakistan typically costs PKR 6,000–12,000; IP models are usually priced above analogue equivalents."),
  ("Typical installation range", "CCTV installation in Lahore usually ranges between PKR 12,500 and PKR 50,000+ depending on cameras, recorder and mobile setup.")],
 "<p>An IP system needs proper network planning — PoE switching, cabling and NVR compatibility — or cameras will keep disconnecting. That planning is part of every SmartShield IP installation. See the <a href=\"CALCPREFIXblog/ip-camera-prices-guide/index.html\">IP camera prices guide</a> and our <a href=\"CALCPREFIXservices/ip-camera-installation/index.html\">IP camera installation service</a>.</p>",
 [("Are IP cameras better than analogue cameras?", "IP cameras give higher resolution and more flexible placement, and they are easier to expand. Analogue systems can be cheaper for simple setups. The right choice depends on your property and budget."),
  ("Do IP cameras need internet to record?", "No. Recording to the NVR happens on your local network. Internet is only needed for remote viewing on your phone."),
  ("What is PoE in an IP camera system?", "Power over Ethernet sends power and video through one network cable, which simplifies cabling. A PoE switch or PoE NVR is required.")]))
NEW_PAGES.append(pricing_page("wireless-cctv-camera-price-in-lahore",
 "Wireless CCTV Camera Price in Lahore | SmartShield Security",
 "Wireless CCTV camera price in Lahore: what wireless cameras cost, pros and cons, and when wireless is the right choice.",
 "Wireless CCTV Camera Price in Lahore",
 "A wireless camera connects to your Wi-Fi instead of a cable, which makes installation faster and cleaner — no drilling for long cable runs. Wireless cameras are popular for homes, rented properties and small shops in Lahore, where running cables is difficult or not allowed.",
 ["Camera brand and resolution (2MP, 4MP)", "Indoor or weatherproof outdoor housing", "Battery-powered or mains-powered", "Cloud storage or local SD / NVR storage", "Number of cameras and Wi-Fi coverage needed"],
 [("Wireless camera (typical)", "Wireless cameras are often priced similarly to wired cameras of the same resolution; the saving is usually in installation, not the camera."),
  ("Home basic wireless setup", "Home CCTV installation in Lahore typically starts at PKR 12,500 for a basic wireless setup."),
  ("Wi-Fi upgrades", "If Wi-Fi is weak where cameras will sit, a range extender or access point may be needed — this is checked during assessment.")],
 "<p>Wireless works best where the Wi-Fi signal is strong and stable. Thick walls, long distances and interference can cause cameras to disconnect — the most common wireless fault we are called to fix. We test signal strength at each camera position before recommending wireless. Read the <a href=\"CALCPREFIXblog/wireless-cctv-camera-price-guide/index.html\">wireless camera price guide</a>.</p>",
 [("Is a Wi-Fi CCTV camera good?", "Yes. Wi-Fi CCTV cameras are convenient for homes and small offices — easy setup, no heavy wiring and direct mobile app connectivity for remote monitoring, provided the Wi-Fi signal is strong."),
  ("Do wireless cameras work during load shedding?", "Battery-powered models keep working for a while; mains-powered cameras stop unless there is backup power. Recording also depends on the recorder or storage having power."),
  ("Can a wireless camera record without Wi-Fi?", "Most wireless cameras need Wi-Fi to send video. Some record to a memory card in the camera; check the model before buying.")]))

# --- Topic / service hub pages ---
def topic_page(slug, title, desc, h1, intro, sections, faqs, img=None, img_alt=""):
    secs = "".join(f"<h2>{h}</h2>{b}" for h, b in sections)
    inner = f"""<p class="lead">{intro}</p>{secs}
<p style="margin-top:20px">Get a preliminary estimate in the <a href="CALCPREFIXcalculator/index.html">Smart Calculator</a>, or <a href="CALCPREFIXcontact/index.html">contact SmartShield Security</a> on <a href="tel:+923059502580">03059502580</a> or <a href="https://wa.me/923059502580" target="_blank" rel="noopener">WhatsApp</a>.</p>"""
    inner += related_block(TOPIC_RELATED.get(slug, DEFAULT_RELATED))
    return (f"{slug}/index.html", title, desc, h1, "../", inner, faqs,
            [("Home", "../index.html"), (h1, f"../{slug}/index.html")], img, img_alt)

NEW_PAGES.append(topic_page("cctv-camera-installation-in-lahore",
 "CCTV Camera Installation in Lahore — Complete Guide | SmartShield Security",
 "CCTV camera installation in Lahore by SmartShield Security: complete guide to services, costs, process and areas served.",
 "CCTV Camera Installation in Lahore",
 "SmartShield Security installs CCTV camera systems for homes, offices, shops and commercial properties across Lahore. This page brings everything together: what we install, how the process works, what it typically costs, and which areas we serve.",
 [("What We Install", "<p>Complete CCTV systems — dome, bullet, PTZ, IP and Wi-Fi cameras, DVR and NVR recorders, hard-disk storage, power supplies and mobile viewing. We also install alarm systems, fire alarm systems and biometric attendance machines for offices that need them.</p><p><a href=\"CALCPREFIXservices/cctv-installation/index.html\">CCTV installation service</a> &middot; <a href=\"CALCPREFIXproducts/index.html\">Browse products</a> &middot; <a href=\"CALCPREFIXservices/index.html\">All services</a></p>"),
  ("How Installation Works", "<ol><li><strong>Share your requirements</strong> — property type, entrances and what you want covered.</li><li><strong>Assessment</strong> — we recommend camera positions and equipment.</li><li><strong>Package and budget proposal</strong> — a preliminary estimate, then a final quotation after site assessment.</li><li><strong>Installation and testing</strong> — clean cabling, recorder setup, mobile viewing configured on your phone, and every camera tested before handover.</li></ol>"),
  ("What It Typically Costs", "<p>Professional installation for basic setups typically starts from PKR 12,500 in Lahore. Most home and small-shop installations fall between PKR 12,500 and PKR 50,000 or more, depending on camera count, DVR/NVR system and mobile setup. A 4MP camera typically costs PKR 6,000–12,000, with installation separate. These are typical market ranges for guidance — your final price is confirmed after a site assessment.</p><p><a href=\"CALCPREFIXblog/cost-of-cctv-camera-installation-in-lahore/index.html\">Full cost guide</a> &middot; <a href=\"CALCPREFIXcalculator/index.html\">Smart Calculator</a></p>"),
  ("Areas We Serve", "<p>DHA Lahore, Gulberg, Johar Town, Model Town, Wapda Town, Bahria Town Lahore and Allama Iqbal Town — and other Lahore areas on confirmation. See our area pages: <a href=\"CALCPREFIXcctv-camera-installation-in-dha-lahore/index.html\">DHA Lahore</a>, <a href=\"CALCPREFIXcctv-camera-installation-in-gulberg/index.html\">Gulberg</a>, <a href=\"CALCPREFIXcctv-camera-installation-in-johar-town/index.html\">Johar Town</a>, <a href=\"CALCPREFIXcctv-camera-installation-in-allama-iqbal-town/index.html\">Allama Iqbal Town</a>.</p>"),
  ("Common Problems We Avoid", "<p>Poor video quality, unstable connections, bad camera angles, power outages, mobile apps that will not connect and recording failures — most of these come from poor installation or wrong equipment, not from the camera itself. Our process is designed to prevent them: correct camera choice, proper placement, tested connections and storage sized to your retention period.</p>")],
 [("What is the cost of installing a CCTV camera?", "It depends on camera type, resolution and installation complexity. In Lahore, professional installation for basic setups typically starts from PKR 12,500. The final price is confirmed after a site assessment."),
  ("How long does installation take?", "Most home and small-shop installations are completed in a day; larger commercial systems take longer. The timeline is confirmed in your proposal."),
  ("Can I view my cameras on my phone?", "Yes, where your system supports remote viewing, we configure mobile access and show you how to use live viewing and playback."),
  ("Which areas of Lahore do you serve?", "DHA Lahore, Gulberg, Johar Town, Model Town, Wapda Town, Bahria Town Lahore and Allama Iqbal Town, and other Lahore areas on confirmation.")],
 "installation.svg", "CCTV camera installation in Lahore"))

NEW_PAGES.append(topic_page("cctv-maintenance-and-repair-in-lahore",
 "CCTV Maintenance & Repair in Lahore | SmartShield Security",
 "CCTV maintenance and repair in Lahore: fault diagnosis, camera and recorder repairs, scheduled checks and system health reports.",
 "CCTV Maintenance and Repair in Lahore",
 "CCTV systems fail quietly — a lens gets dusty, a hard disk fills up, a camera drifts out of position. SmartShield Security maintains and repairs CCTV systems across Lahore, including systems installed by other companies.",
 [("CCTV Repair", "<p>When a camera goes dark, a recorder stops saving footage or remote viewing stops working, the fault is usually in one place — a camera, a cable, a power supply or a setting. We diagnose the fault first, explain what is wrong, and repair or replace only what is needed.</p><p><a href=\"CALCPREFIXservices/cctv-repair/index.html\">CCTV repair service</a></p>"),
  ("CCTV Maintenance", "<p>Regular maintenance catches problems before footage is needed: camera cleaning and re-alignment, recorder and hard-disk checks, cable and power-supply inspection, and a review of settings and recording. You receive a short report after each visit.</p><p><a href=\"CALCPREFIXservices/cctv-maintenance/index.html\">CCTV maintenance service</a></p>"),
  ("Common Faults We Fix", "<ul class=\"checklist\"><li>Cameras offline or showing no picture</li><li>Recorder not saving or playing back footage</li><li>Mobile app not connecting</li><li>Blurry or poor-quality night video</li><li>Power supply and cabling faults</li><li>Hard disk full or faulty</li></ul>"),
  ("How It Works", "<ol><li>Describe the problem and your system.</li><li>We diagnose the fault on site.</li><li>You approve the repair before work starts.</li><li>Repair, testing and confirmation that the system records properly.</li></ol>")],
 [("How much does CCTV repair cost in Lahore?", "It depends on the fault — a cable or power supply is usually a small repair, while a recorder or hard-disk replacement costs more. We diagnose first and explain the fault and the fix before any work starts."),
  ("Do you repair systems installed by other companies?", "Yes. We maintain and repair CCTV systems regardless of who installed them, provided compatible parts are available."),
  ("How often should CCTV be maintained?", "For most homes and shops, a check every few months is enough. Busy commercial sites and outdoor cameras benefit from more frequent checks.")],
 "installation.svg", "CCTV maintenance and repair in Lahore"))

NEW_PAGES.append(topic_page("biometric-attendance-machine-in-lahore",
 "Biometric Attendance Machine in Lahore | SmartShield Security",
 "Biometric attendance machines in Lahore: fingerprint, face and card attendance systems for offices, schools and factories.",
 "Biometric Attendance Machine in Lahore",
 "A biometric attendance machine records staff attendance with a fingerprint, face or card — no paper registers, no manual errors and no buddy punching. SmartShield Security supplies and installs attendance systems for offices, schools, clinics and factories in Lahore.",
 [("Types of Attendance Systems", "<ul class=\"checklist\"><li><strong>Fingerprint attendance</strong> — reliable and affordable for most offices</li><li><strong>Face recognition attendance</strong> — contactless, useful where hygiene matters</li><li><strong>Card and PIN attendance</strong> — simple and fast for large staff numbers</li><li><strong>Combined systems</strong> — fingerprint plus card or face, for flexibility</li></ul>"),
  ("What a System Includes", "<p>The attendance device, power supply and mounting, connection to your network or computer, attendance software setup, and staff enrolment — we register fingerprints or faces and show your admin how to pull attendance reports.</p>"),
  ("Who Needs One?", "<p>Offices with 10 or more staff, schools, factories, clinics and warehouses — anywhere attendance is tracked daily and payroll depends on accurate records.</p>"),
  ("Combining Attendance with CCTV", "<p>Many offices install an attendance machine alongside CCTV: cameras cover entrances and common areas, while the attendance machine handles staff records. Ask us about a combined package for your office.</p>")],
 [("How much does a biometric attendance machine cost in Lahore?", "It depends on the device type — fingerprint, face recognition or card — and the number of users. Contact us with your staff count and we will recommend a suitable device and give you a quotation."),
  ("Can attendance data be used for payroll?", "Yes. Attendance software exports records that can be used with payroll, including late arrivals, overtime and leave records — depending on the software supplied."),
  ("Does a fingerprint machine work for all staff?", "Fingerprint readers work for most people, but worn or dry fingerprints can be hard to read. For those cases, face recognition or card options are available.")],
 "control-room.svg", "Biometric attendance machine in Lahore"))

NEW_PAGES.append(topic_page("fire-alarm-systems",
 "Fire Alarm Systems in Lahore | SmartShield Security",
 "Fire alarm systems in Lahore: smoke and heat detectors, alarm panels, sirens and early-warning systems for homes, offices and shops.",
 "Fire Alarm Systems in Lahore",
 "A fire alarm system gives early warning when smoke or heat is detected — the extra minutes it provides can protect lives and property. SmartShield Security supplies and installs fire alarm systems for homes, offices, shops, schools and commercial buildings in Lahore.",
 [("What a Fire Alarm System Includes", "<ul class=\"checklist\"><li><strong>Smoke detectors</strong> — for rooms, corridors and common areas</li><li><strong>Heat detectors</strong> — for kitchens and areas where smoke detectors give false alarms</li><li><strong>Alarm panel</strong> — shows which zone triggered the alarm</li><li><strong>Sirens and sounders</strong> — audible warning across the building</li><li><strong>Manual call points</strong> — so anyone can raise the alarm</li></ul>"),
  ("Where Fire Alarms Matter Most", "<p>Kitchens, electrical rooms, server rooms, storage areas, corridors and stairwells — and any area where people sleep or work. Placement depends on the building layout and how it is used.</p>"),
  ("Fire Alarms and CCTV Together", "<p>Fire alarms warn people; CCTV records what happened. Together they cover both early warning and incident review. Many commercial clients install both systems at the same time.</p>"),
  ("Testing and Maintenance", "<p>Detectors and panels should be tested regularly — a system that has not been tested may not work when it is needed. We provide testing and maintenance visits for installed fire alarm systems.</p>")],
 [("Do I need a fire alarm system for my shop or office?", "It depends on the building size, use and local requirements. For larger premises and places where people gather, early warning is strongly recommended. We can assess your building and advise what is suitable."),
  ("How much does a fire alarm system cost?", "It depends on the number of detectors, the size of the building and the panel type. Contact us with your building details for a quotation after assessment."),
  ("Do smoke detectors give false alarms?", "They can, especially in kitchens or dusty areas. Heat detectors are used in those places instead, and detector placement is planned to reduce false alarms.")],
 "hero-camera.svg", "Fire alarm system in Lahore"))

NEW_PAGES.append(topic_page("alarm-systems",
 "Alarm Systems in Lahore | SmartShield Security",
 "Alarm systems in Lahore: burglar alarms, door and window sensors, motion detectors, sirens and intrusion alerts for homes and businesses.",
 "Alarm Systems in Lahore",
 "An alarm system warns you the moment someone tries to enter your property — before damage is done. SmartShield Security installs burglar and intrusion alarm systems for homes, offices, shops and warehouses in Lahore, often alongside CCTV.",
 [("What an Alarm System Includes", "<ul class=\"checklist\"><li><strong>Door and window sensors</strong> — trigger when an entry point opens</li><li><strong>Motion detectors</strong> — cover rooms, hallways and corridors</li><li><strong>Control panel</strong> — arms and disarms the system</li><li><strong>Siren</strong> — loud audible warning to deter intruders</li><li><strong>Keypad or remote</strong> — easy arming for the whole family or staff</li></ul>"),
  ("Alarm + CCTV: Better Together", "<p>An alarm tells you something is happening; a camera shows you what. When both are installed, the alarm alerts you and the cameras record the event — a combination that is much stronger than either system alone.</p>"),
  ("For Homes", "<p>Main door and window sensors, a motion detector in the main hallway, and a siren. The system is armed at night or when the house is empty, and disarmed with a code or remote.</p>"),
  ("For Shops and Offices", "<p>Entrance sensors, motion detectors in stock rooms and offices, and a loud siren. Larger premises can be divided into zones so parts of the building can stay armed while other parts are in use.</p>")],
 [("How much does an alarm system cost in Lahore?", "It depends on the number of sensors, the size of the property and whether it is combined with CCTV. Contact us with your property details for a quotation after assessment."),
  ("Will the alarm go off by mistake?", "False alarms usually come from wrong sensor placement or pets. We plan sensor positions carefully and explain how to arm and disarm the system properly."),
  ("Can the alarm work during load shedding?", "Alarm panels normally have a backup battery that keeps the system running for a period during a power cut. Battery condition is checked during maintenance.")],
 "hero-camera.svg", "Alarm system in Lahore"))

# --- Services hub ---
NEW_PAGES.append(("services/index.html",
 "Our Services | CCTV, Alarms & Security Systems in Lahore | SmartShield Security",
 "All SmartShield Security services in Lahore: CCTV installation, IP cameras, DVR/NVR, repair, maintenance, remote monitoring, alarms and more.",
 "Our Services", "../",
 """<p class="lead">Every service below is provided by SmartShield Security in Lahore, Pakistan. Click a service for full details, or <a href="CALCPREFIXcalculator/index.html">build your CCTV package</a> to get a preliminary estimate.</p>
<h2>CCTV &amp; Camera Services</h2>
<ul>
<li><a href="CALCPREFIXservices/cctv-installation/index.html">CCTV Camera Installation</a> — complete systems for homes, offices and shops</li>
<li><a href="CALCPREFIXservices/home-security/index.html">Home CCTV Security</a> — indoor and outdoor cameras, night vision, mobile viewing</li>
<li><a href="CALCPREFIXservices/office-security/index.html">Office Security Systems</a> — entrance, reception and workspace coverage</li>
<li><a href="CALCPREFIXservices/shop-commercial-security/index.html">Shop &amp; Commercial Security</a> — cash counters, entrances and stock areas</li>
<li><a href="CALCPREFIXservices/ip-camera-installation/index.html">IP Camera Installation</a> — network cameras with PoE and remote viewing</li>
<li><a href="CALCPREFIXservices/ai-camera-solutions/index.html">AI Camera Solutions</a> — human and vehicle detection where supported</li>
<li><a href="CALCPREFIXservices/dvr-nvr-installation/index.html">DVR &amp; NVR Installation</a> — recorders and storage sized to your needs</li>
<li><a href="CALCPREFIXservices/remote-monitoring/index.html">Remote CCTV Monitoring</a> — live viewing and playback on your phone</li>
</ul>
<h2>Repair &amp; Maintenance</h2>
<ul>
<li><a href="CALCPREFIXservices/cctv-repair/index.html">CCTV Camera Repair</a> — fault diagnosis and repair</li>
<li><a href="CALCPREFIXservices/cctv-maintenance/index.html">CCTV Maintenance</a> — scheduled checks, cleaning and storage review</li>
<li><a href="CALCPREFIXcctv-maintenance-and-repair-in-lahore/index.html">CCTV Maintenance and Repair in Lahore</a> — the full guide</li>
</ul>
<h2>Other Security Systems</h2>
<ul>
<li><a href="CALCPREFIXalarm-systems/index.html">Alarm Systems</a> — burglar alarms, sensors and sirens</li>
<li><a href="CALCPREFIXfire-alarm-systems/index.html">Fire Alarm Systems</a> — smoke and heat detectors, panels and sounders</li>
<li><a href="CALCPREFIXbiometric-attendance-machine-in-lahore/index.html">Biometric Attendance Machines</a> — fingerprint, face and card attendance</li>
</ul>
<h2>By Area</h2>
<ul>
<li><a href="CALCPREFIXcctv-camera-installation-in-lahore/index.html">CCTV Camera Installation in Lahore</a></li>
<li><a href="CALCPREFIXcctv-camera-installation-in-dha-lahore/index.html">CCTV in DHA Lahore</a></li>
<li><a href="CALCPREFIXcctv-camera-installation-in-gulberg/index.html">CCTV in Gulberg</a></li>
<li><a href="CALCPREFIXcctv-camera-installation-in-johar-town/index.html">CCTV in Johar Town</a></li>
<li><a href="CALCPREFIXcctv-camera-installation-in-allama-iqbal-town/index.html">CCTV in Allama Iqbal Town</a></li>
</ul>
<h2>Pricing Guides</h2>
<ul>
<li><a href="CALCPREFIX2mp-cctv-camera-price-in-lahore/index.html">2MP CCTV Camera Price in Lahore</a></li>
<li><a href="CALCPREFIX5mp-cctv-camera-packages/index.html">5MP CCTV Camera Packages</a></li>
<li><a href="CALCPREFIX4k-cctv-cameras-price-in-pakistan/index.html">4K CCTV Cameras Price in Pakistan</a></li>
<li><a href="CALCPREFIXip-camera-prices-in-lahore/index.html">IP Camera Prices in Lahore</a></li>
<li><a href="CALCPREFIXwireless-cctv-camera-price-in-lahore/index.html">Wireless CCTV Camera Price in Lahore</a></li>
</ul>""",
 None, [("Home", "../index.html"), ("Services", "../services/index.html")], None, ""))

# --- Area pages ---
def area_page(slug, area, title, desc, h1, intro, focus, faqs):
    inner = f"""<p class="lead">{intro}</p>
<h2>What We Install in {area}</h2><ul class="checklist">{''.join(f'<li>{f}</li>' for f in focus)}</ul>
<h2>How It Works in {area}</h2><p>Share your property details by phone or WhatsApp, or use the <a href="CALCPREFIXcalculator/index.html">Smart Calculator</a> for a preliminary estimate. We assess coverage needs, recommend camera positions and equipment, and confirm a final quotation after a site assessment. Installation is scheduled at a time that suits you, and mobile viewing is configured on your phone before handover.</p>
<p><strong>Note:</strong> SmartShield Security does not operate a public office in {area} — visits are arranged by appointment. Contact us on <a href="tel:+923059502580">03059502580</a> or <a href="https://wa.me/923059502580" target="_blank" rel="noopener">WhatsApp</a> to book a visit.</p>
<p>Also serving: <a href="CALCPREFIXcctv-camera-installation-in-lahore/index.html">CCTV installation across Lahore</a></p>"""
    _areas = [("DHA Lahore", "CALCPREFIXcctv-camera-installation-in-dha-lahore/index.html"), ("Gulberg", "CALCPREFIXcctv-camera-installation-in-gulberg/index.html"), ("Johar Town", "CALCPREFIXcctv-camera-installation-in-johar-town/index.html"), ("Allama Iqbal Town", "CALCPREFIXcctv-camera-installation-in-allama-iqbal-town/index.html")]
    inner += related_block([a for a in _areas if a[1] != f"CALCPREFIX{slug}/index.html"] + [("CCTV Installation Across Lahore", "CALCPREFIXcctv-camera-installation-in-lahore/index.html"), ("Smart Calculator", "CALCPREFIXcalculator/index.html")])
    return (f"{slug}/index.html", title, desc, h1, "../", inner, faqs,
            [("Home", "../index.html"), (h1, f"../{slug}/index.html")], None, "")

AREA_FAQS = [("How much does CCTV installation cost in my area?", "Prices depend on camera count, camera type, recorder and installation requirements. In Lahore, professional installation for basic setups typically starts from PKR 12,500, and most home and small-shop jobs fall between PKR 12,500 and PKR 50,000+. Your final quotation is confirmed after a site assessment."),
 ("Can I view my cameras on my phone?", "Yes, where your system supports remote viewing, we configure mobile access and show you how to use live viewing and playback."),
 ("How long does installation take?", "Most home and small-shop installations are completed in a day; larger systems take longer. The timeline is confirmed in your proposal.")]
NEW_PAGES.append(area_page("cctv-camera-installation-in-gulberg", "Gulberg",
 "CCTV Camera Installation in Gulberg Lahore | SmartShield Security",
 "CCTV camera installation in Gulberg, Lahore: office, retail and home security systems by SmartShield Security.",
 "CCTV Camera Installation in Gulberg, Lahore",
 "Gulberg is one of Lahore's main commercial areas — offices, banks, restaurants, retail stores and clinics, alongside residential streets. SmartShield Security installs CCTV systems for Gulberg offices and shops that need reliable coverage of entrances, counters, cash areas and parking, as well as home systems for Gulberg houses.",
 ["Office CCTV — reception, entrances, corridors and server rooms", "Shop and retail CCTV — cash counters, entrances and stock areas", "Restaurant and clinic security systems", "Home CCTV for Gulberg houses and apartments", "IP cameras with remote viewing for business owners"], AREA_FAQS))
NEW_PAGES.append(area_page("cctv-camera-installation-in-dha-lahore", "DHA Lahore",
 "CCTV Camera Installation in DHA Lahore | SmartShield Security",
 "CCTV camera installation in DHA Lahore: home, villa and commercial security systems by SmartShield Security.",
 "CCTV Camera Installation in DHA Lahore",
 "DHA Lahore's houses, villas and commercial areas need security systems that fit large properties — long boundaries, multiple entrances, driveways and gates. SmartShield Security installs home and commercial CCTV in DHA, with camera layouts planned around the size and shape of each property.",
 ["Home and villa CCTV — gates, driveways, boundaries and entrances", "Outdoor bullet cameras for long boundary walls", "Night vision for low-light areas", "Commercial CCTV for DHA shops and offices", "Mobile viewing for homeowners who travel"], AREA_FAQS))
NEW_PAGES.append(area_page("cctv-camera-installation-in-johar-town", "Johar Town",
 "CCTV Camera Installation in Johar Town Lahore | SmartShield Security",
 "CCTV camera installation in Johar Town, Lahore: home and shop security systems by SmartShield Security.",
 "CCTV Camera Installation in Johar Town, Lahore",
 "Johar Town is a large residential area of Lahore with houses, flats, shops, schools and small businesses. SmartShield Security installs home CCTV for Johar Town houses — covering gates, driveways and entrances — and security systems for local shops, schools and offices.",
 ["Home CCTV — gates, driveways and entrances", "Shop CCTV — counters, entrances and stock areas", "School and office security systems", "Wireless cameras where cabling is difficult", "DVR/NVR setup with mobile viewing"], AREA_FAQS))
NEW_PAGES.append(area_page("cctv-camera-installation-in-allama-iqbal-town", "Allama Iqbal Town",
 "CCTV Camera Installation in Allama Iqbal Town Lahore | SmartShield Security",
 "CCTV camera installation in Allama Iqbal Town, Lahore: home and shop security systems by SmartShield Security.",
 "CCTV Camera Installation in Allama Iqbal Town, Lahore",
 "Allama Iqbal Town is a well-established residential area of Lahore, with houses, markets and small businesses. SmartShield Security installs CCTV for Allama Iqbal Town homes and shops — practical systems that cover the areas that matter, at a sensible cost.",
 ["Home CCTV — main gate, driveway and entrances", "Shop CCTV — counters and entrances", "Budget-friendly 2MP and 4MP systems", "Wireless cameras for homes where cabling is difficult", "Mobile viewing setup on your phone"], AREA_FAQS))

# --- Packages page ---
def _pkg_cards(pkgs, prefix):
    return "".join(pkg_card(n, r, pr, f, prefix=prefix, upgrades=u) for n, r, pr, f, u in pkgs)

NEW_PAGES.append(("packages/index.html",
 "CCTV Camera Packages in Lahore | 2MP, 5MP, 4K, IP & Wireless | SmartShield Security",
 "CCTV camera packages in Lahore: 2MP, 5MP, 4K/8MP, IP and wireless packages with 2, 4, 6 or 8 cameras, recorder, storage and installation — prices as listed.",
 "CCTV Camera Packages in Lahore", "../",
 f"""<p class="lead">Choose a package by resolution and camera count, then get an exact estimate for your property. Every package below includes cameras, a compatible recorder, storage, cabling, professional installation and mobile viewing setup.</p>
PRICENOTE
<h2 style="margin-top:32px">4-Camera Home Packages</h2>
<p>Complete packages for a typical home — gate, driveway, entrance and one more key area.</p>
<div class="grid grid-3" style="margin-top:16px">{_pkg_cards(HOME_PKGS, "CALCPREFIX")}</div>
<h2 style="margin-top:32px">5MP CCTV Packages</h2>
<p>Sharper detail than 2MP — for entrances, parking areas and shop floors.</p>
<div class="grid grid-3" style="margin-top:16px">{_pkg_cards(MP5_PKGS, "CALCPREFIX")}</div>
<p class="note" style="margin-top:16px">Prices are listed exactly as published, including the 8-camera 5MP package at Rs 59,400. Upgrades are available for colour night vision and audio cameras — see each card for upgrade prices.</p>
<h2 style="margin-top:32px">4K / 8MP CCTV Packages</h2>
<p>Ultra HD detail for large properties and high-security entrances.</p>
<div class="grid grid-3" style="margin-top:16px">{_pkg_cards(K4_PKGS, "CALCPREFIX")}</div>
<p class="note" style="margin-top:16px">The 8-camera 4K package lists both a 500GB and a 2TB hard disk, as published. Your final storage is confirmed in the package proposal.</p>
<h2 style="margin-top:32px">How to Choose a Package</h2>
<ul class="checklist"><li><strong>2MP</strong> — best value for homes and small shops; clear Full HD video.</li><li><strong>5MP</strong> — more detail for entrances, parking and shop floors.</li><li><strong>4K / 8MP</strong> — finest detail for large properties and high-security entrances.</li><li><strong>IP</strong> — highest flexibility and resolution, for properties that need a network system.</li><li><strong>Wireless</strong> — fastest installation where cabling is difficult, provided Wi-Fi is strong.</li></ul>
<p>Not sure which package fits? <a href="CALCPREFIXcalculator/index.html">Build your package in the Smart Calculator</a> or call <a href="tel:+923059502580">03059502580</a> / <a href="https://wa.me/923059502580" target="_blank" rel="noopener">WhatsApp +92 305 9502580</a>.</p>""" + related_block([("Smart Calculator", "CALCPREFIXcalculator/index.html"), ("2MP Camera Prices", "CALCPREFIX2mp-cctv-camera-price-in-lahore/index.html"), ("5MP Camera Packages", "CALCPREFIX5mp-cctv-camera-packages/index.html"), ("4K Camera Prices", "CALCPREFIX4k-cctv-cameras-price-in-pakistan/index.html")]),
 [("How much does a CCTV package cost in Lahore?", "Our 4-camera home packages start at Rs 40,500 for the 2MP package, Rs 57,400 for the 5MP package and Rs 98,400 for the full 4K (8MP) package. The 5MP range runs from Rs 48,500 (2 cameras) to Rs 81,500 (6 cameras), and the 4K range from Rs 75,400 (2 cameras) to Rs 155,500 (8 cameras). The final price is confirmed after a site survey, because cable length and installation requirements differ for every property."),
  ("What is included in a CCTV package?", "Cameras, a compatible DVR or NVR recorder, a hard disk sized to your retention period, cabling, professional installation and mobile viewing setup. The exact list is in your package proposal."),
  ("Which package is best for a home?", "For most homes, a 2MP or 4MP package with 4 cameras covers the main gate, driveway and entrances. Larger houses usually need 6 or 8 cameras. The calculator can help you decide."),
  ("Can I add more cameras later?", "Yes — IP systems are the easiest to expand, and most DVR/NVR recorders have spare channels. Tell us your future plans when choosing a recorder.")],
 [("Home", "../index.html"), ("CCTV Packages", "../packages/index.html")], None, ""))

# ---------- BLOG ----------
def blog_post(slug, title, desc, h1, date, body_html):
    inner = f"""<p style="color:#526174">Published {date} &middot; SmartShield Security, Lahore</p>
<p class="lead">{desc}</p>
{body_html}
<p style="margin-top:24px">Need help choosing? Use the <a href="../../calculator/index.html">Smart Calculator</a> for a preliminary estimate, or contact SmartShield Security on <a href="tel:+923059502580">03059502580</a> / <a href="https://wa.me/923059502580" target="_blank" rel="noopener">WhatsApp</a>.</p>
<p><a href="../../blog/index.html">&larr; Back to all guides</a></p>"""
    inner += related_block(BLOG_RELATED.get(slug, DEFAULT_RELATED))
    extra = ""
    return (f"blog/{slug}/index.html", title, desc, h1, "../../", inner, None,
            [("Home", "../../index.html"), ("Blog", "../../blog/index.html"), (h1, f"../../blog/{slug}/index.html")], None, "")

BLOG_POSTS = []
BLOG_POSTS.append(blog_post("cost-of-cctv-camera-installation-in-lahore",
 "Cost of CCTV Camera Installation in Lahore (2026 Guide) | SmartShield Security",
 "How much does CCTV camera installation cost in Lahore? Typical prices, what affects the cost, and how to get an accurate quotation.",
 "Cost of CCTV Camera Installation in Lahore",
 "11 November 2026",
 """<h2>What Does CCTV Installation Cost in Lahore?</h2>
<p>There is no single fixed price for CCTV installation, because every property is different. As a guide, professional installation for basic setups in Lahore typically starts from PKR 12,500, and most home and small-shop installations fall between PKR 12,500 and PKR 50,000 or more. The final price depends on how many cameras you need, what type they are, which recorder and storage you choose, and how much cabling the job requires.</p>
<h2>What Affects the Cost?</h2>
<ul class="checklist"><li><strong>Number of cameras</strong> — a 2-camera home setup costs far less than an 8-camera office system.</li><li><strong>Camera type and resolution</strong> — 2MP cameras cost less than 4MP, 5MP or 4K models. A 4MP camera in Pakistan typically costs PKR 6,000–12,000, with installation separate.</li><li><strong>Recorder and storage</strong> — a DVR or NVR plus a hard disk sized to your retention period (7, 15, 30 or 60 days).</li><li><strong>Cabling and installation complexity</strong> — long cable runs, multiple floors and outdoor work add labour and materials.</li><li><strong>Mobile viewing setup</strong> — configuring remote viewing on your phone is part of a professional installation.</li></ul>
<h2>Home vs Shop vs Office</h2>
<p>A small home usually needs 2–4 cameras covering the gate, driveway and main entrance. A shop adds the cash counter and stock room. An office adds reception, corridors and server areas. Each extra camera adds the camera itself, cabling and a recorder channel — so the clearest way to control cost is to cover the areas that matter and skip the ones that do not.</p>
<h2>Hidden Costs to Watch For</h2>
<p>Cheap quotations sometimes leave out the hard disk, the power supply or mobile setup, and those appear as extras later. Always ask what is included: cameras, recorder, hard disk, cabling, power supply, installation and mobile viewing. A proper quotation lists every item.</p>
<h2>How to Get an Accurate Price</h2>
<p>Use our <a href="../../calculator/index.html">Smart Calculator</a> for a preliminary estimate based on your property and requirements. For a final quotation, we assess the site — camera positions, cable routes and storage needs — and confirm the price before work starts. No fixed per-package price is published, because the price genuinely depends on your property.</p>"""))
BLOG_POSTS.append(blog_post("dvr-vs-nvr",
 "DVR vs NVR: Which Recorder Is Right for Your CCTV System? | SmartShield Security",
 "DVR vs NVR explained simply: how each recorder works, which cameras they support, and how to choose the right one for your home or office in Lahore.",
 "DVR vs NVR: Which Recorder Is Right for You?",
 "11 November 2026",
 """<h2>What Is a DVR?</h2>
<p>A DVR (Digital Video Recorder) works with analogue and HD cameras. The cameras send video to the DVR over coaxial cable, and the DVR records it to a hard disk. DVR systems are usually the lower-cost option and suit homes and small shops that do not need very high resolution.</p>
<h2>What Is an NVR?</h2>
<p>An NVR (Network Video Recorder) works with IP cameras. The cameras send video over your network, usually through a PoE switch that carries power and video in one cable. NVR systems support higher resolutions — 4MP, 5MP and 4K — and are easier to expand, because adding a camera is mostly a network job rather than a new cable run.</p>
<h2>DVR vs NVR at a Glance</h2>
<ul class="checklist"><li><strong>Cameras:</strong> DVR takes analogue/HD cameras; NVR takes IP cameras.</li><li><strong>Resolution:</strong> NVR systems generally reach higher resolutions.</li><li><strong>Cabling:</strong> DVR uses coaxial cable; NVR uses network cable (Cat6) with PoE.</li><li><strong>Expansion:</strong> NVR systems are usually easier to grow camera by camera.</li><li><strong>Cost:</strong> DVR systems are typically cheaper for the same camera count.</li></ul>
<h2>Which One Should You Choose?</h2>
<p>If you already have analogue cameras, a DVR is the natural choice. If you are starting fresh and want high resolution, remote viewing and room to grow, an NVR with IP cameras is usually the better investment. For a small home with 2–4 cameras, either can work well — the decision comes down to resolution needs and budget.</p>
<h2>Storage Matters Either Way</h2>
<p>Both recorders need a hard disk sized to your camera count and retention period. A system that records 8 cameras for 30 days needs far more storage than one that records 2 cameras for 7 days. Storage is estimated from camera count, resolution and recording settings — and it is worth getting right, because a full disk stops recording.</p>
<h2>Can You Mix DVR and NVR?</h2>
<p>Some recorders, often called hybrid or XVR models, accept both analogue and IP cameras. They are useful when you already have analogue cameras but want to add one or two IP cameras later. A hybrid recorder can be a sensible middle step, but it is still worth checking which resolutions and features it supports on each input before buying.</p>"""))
BLOG_POSTS.append(blog_post("bullet-vs-dome-cctv-cameras",
 "Bullet vs Dome CCTV Cameras: Which One Do You Need? | SmartShield Security",
 "Bullet vs dome CCTV cameras compared: coverage, range, mounting, night vision and where each type works best in a Lahore home or shop.",
 "Bullet vs Dome CCTV Cameras: Which One Do You Need?",
 "11 November 2026",
 """<h2>What Is a Bullet Camera?</h2>
<p>A bullet camera is the long, cylindrical camera most people picture when they think of CCTV. It is designed for outdoor use and long-range coverage — boundaries, driveways, gates and parking areas. Its shape makes it visible, which itself deters intruders, and its lens is built for distance.</p>
<h2>What Is a Dome Camera?</h2>
<p>A dome camera sits in a rounded, discreet housing, usually mounted on a ceiling. It gives wide-angle coverage and is hard to tell exactly where it is pointing, which makes it popular indoors — shops, offices, hallways and living areas. Outdoor dome cameras exist too, but they are best for shorter distances.</p>
<h2>Bullet vs Dome at a Glance</h2>
<ul class="checklist"><li><strong>Range:</strong> bullet cameras see further; dome cameras cover a wider angle at short range.</li><li><strong>Placement:</strong> bullet cameras suit walls and outdoor boundaries; dome cameras suit ceilings and indoor spaces.</li><li><strong>Visibility:</strong> bullet cameras are an obvious deterrent; dome cameras are discreet.</li><li><strong>Weather:</strong> both come in weatherproof versions — check the rating before buying for outdoor use.</li><li><strong>Night vision:</strong> both types offer infrared night vision; the effective range depends on the model.</li></ul>
<h2>Which One for Your Property?</h2>
<p>Most Lahore homes and shops need both: bullet cameras for the gate, driveway and boundary, and dome cameras for the entrance, shop floor or hallway. A single type rarely covers everything well. When we plan a system, we mix the two — bullet where distance matters, dome where wide, discreet coverage matters.</p>
<h2>A Note on Image Quality</h2>
<p>Shape is only half the story. Resolution, lens quality and lighting matter just as much. A well-placed 2MP camera beats a badly placed 4K camera every time, because the angle and the light decide what the footage actually shows.</p>
<h2>What About PTZ Cameras?</h2>
<p>For very large areas — a warehouse yard, a big parking area or a large boundary — a PTZ camera that can pan, tilt and zoom covers more ground than a fixed bullet or dome. PTZ cameras cost more and suit active monitoring rather than set-and-forget recording, so they are usually added alongside fixed cameras rather than replacing them. For most homes and shops, a mix of bullet and dome cameras is enough.</p>"""))
BLOG_POSTS.append(blog_post("hikvision-vs-dahua-cctv-cameras",
 "Hikvision vs Dahua CCTV Cameras: An Honest Comparison | SmartShield Security",
 "Hikvision vs Dahua compared honestly: image quality, app, AI features, price and reliability — and how to choose between them in Pakistan.",
 "Hikvision vs Dahua CCTV Cameras: An Honest Comparison",
 "11 November 2026",
 """<h2>Two Brands, One Market</h2>
<p>Hikvision and Dahua are the two most common CCTV brands in Pakistan, and both are used in homes, shops and offices across Lahore. They compete directly: similar camera ranges, similar recorders, similar prices. For most buyers, the differences are smaller than the marketing suggests.</p>
<h2>Image Quality and Range</h2>
<p>Both brands offer 2MP, 4MP, 5MP and 4K cameras in dome, bullet and PTZ form, with infrared night vision and colour night vision options. At the same price point, image quality is broadly comparable. The bigger differences come from the specific model and lens — not the brand name on the box.</p>
<h2>Apps and Remote Viewing</h2>
<p>Both brands provide mobile apps for live viewing and playback. Setup quality matters more than the app itself: a correctly configured system works smoothly on either brand, while a poorly configured one disconnects on both. We configure and test mobile viewing on your own phone before handover, whichever brand you choose.</p>
<h2>AI Features</h2>
<p>Both brands offer human and vehicle detection and smart alerts — but only on camera and recorder combinations that support them. We check compatibility before recommending AI features, and we do not promise analytics that your hardware cannot deliver.</p>
<h2>Price and Availability</h2>
<p>Prices are similar at equivalent specifications, and both brands are widely available in Lahore, which makes parts and replacements easier to find. As a reference point, a 4MP camera in Pakistan typically costs PKR 6,000–12,000 depending on brand and features, with installation separate.</p>
<h2>Which Should You Choose?</h2>
<p>Choose by model, not by brand. Tell us your budget, the areas to cover and the features you need, and we will recommend the specific camera and recorder that fit — from Hikvision, Dahua, IMOU or CP Plus. The installer and the installation quality matter more than the logo.</p>
<h2>What About Warranty and Support?</h2>
<p>Both brands are sold through distributors in Pakistan, and warranty terms depend on the seller and the specific product. When comparing quotations, check that the warranty is stated in writing and that the supplier is an authorised channel — a camera bought without proper warranty support can be difficult to replace if it fails within the first year.</p>"""))
BLOG_POSTS.append(blog_post("wireless-cctv-camera-price-guide",
 "Wireless CCTV Camera Price Guide for Lahore (2026) | SmartShield Security",
 "Wireless CCTV camera prices in Lahore: what wireless cameras cost, what affects the price, and when wireless is the right choice for your home.",
 "Wireless CCTV Camera Price Guide for Lahore",
 "11 November 2026",
 """<h2>What Is a Wireless CCTV Camera?</h2>
<p>A wireless camera connects to your Wi-Fi network instead of a long cable run. It still needs power — from a nearby socket or a battery — but the video travels wirelessly to your recorder, memory card or the viewing app. Installation is faster and cleaner, with no drilling for cables through walls.</p>
<h2>What Do Wireless Cameras Cost in Lahore?</h2>
<p>Wireless cameras are often priced similarly to wired cameras of the same resolution; the saving is usually in installation, not in the camera itself. A basic home wireless setup in Lahore typically starts from PKR 12,500 for installation, with the total depending on camera count, resolution and storage. As a reference, a 4MP camera in Pakistan typically costs PKR 6,000–12,000, with installation separate.</p>
<h2>What Affects the Price?</h2>
<ul class="checklist"><li><strong>Resolution</strong> — 2MP is the most affordable; 4MP costs more.</li><li><strong>Indoor or outdoor</strong> — weatherproof outdoor models cost more.</li><li><strong>Power</strong> — battery-powered models cost more than mains-powered ones.</li><li><strong>Storage</strong> — memory card, cloud subscription or NVR recording.</li><li><strong>Wi-Fi coverage</strong> — weak signal areas may need a range extender or access point.</li></ul>
<h2>When Wireless Is the Right Choice</h2>
<p>Wireless works best in homes, rented properties and small shops where running cables is difficult or not allowed, and where the Wi-Fi signal is strong at every camera position. It is also a good choice for a first camera or a small 2–4 camera system.</p>
<h2>When Wireless Is Not Ideal</h2>
<p>Thick walls, long distances and interference can make cameras disconnect — the most common wireless fault we are called to fix. Large properties, many cameras and outdoor boundaries usually suit wired or IP systems better. We test signal strength at each camera position before recommending wireless, so you do not discover the problem after installation.</p>
<h2>Battery vs Mains Power</h2>
<p>Battery-powered wireless cameras are the easiest to place — no socket needed — but the battery must be recharged every few weeks or months depending on use, and cold weather shortens battery life. Mains-powered cameras never need charging, but they need a socket nearby. For a camera that must record all the time, mains power is usually the better choice; battery models suit places where a socket is impossible.</p>"""))

BLOG_POSTS.append(blog_post("ip-camera-prices-guide",
 "IP Camera Prices Guide for Lahore (2026) | SmartShield Security",
 "IP camera prices in Lahore: what IP cameras cost, what affects the price, PoE and NVR requirements, and when IP is worth it.",
 "IP Camera Prices Guide for Lahore",
 "11 November 2026",
 """<h2>What Is an IP Camera?</h2>
<p>An IP camera sends video over your network instead of a direct cable to a recorder. That gives higher-resolution images, flexible placement and remote viewing — and it makes the system easy to grow, because adding a camera is mostly a network job. IP cameras are the standard choice for offices, larger homes and commercial properties in Lahore.</p>
<h2>What Do IP Cameras Cost in Lahore?</h2>
<p>IP cameras cost more than analogue cameras of the same resolution, because they contain their own network hardware. Prices vary by resolution (2MP, 4MP, 5MP or 4K), brand and features. As a reference, a 4MP camera in Pakistan typically costs PKR 6,000–12,000, and IP models are usually priced above analogue equivalents. Installation for a complete system in Lahore usually ranges between PKR 12,500 and PKR 50,000 or more, depending on camera count, recorder and mobile setup.</p>
<h2>What Else Does an IP System Need?</h2>
<ul class="checklist"><li><strong>NVR</strong> — a network video recorder with enough channels for your cameras.</li><li><strong>PoE switch</strong> — sends power and video through one network cable per camera.</li><li><strong>Cat6 cabling</strong> — proper network cable, not telephone wire.</li><li><strong>Hard disk</strong> — sized to camera count, resolution and retention period.</li><li><strong>Network planning</strong> — so cameras stay connected and do not drop offline.</li></ul>
<h2>When Is IP Worth It?</h2>
<p>IP is worth it when you need sharp video, many cameras, or a system that will grow. It is also the right choice when cameras are far apart or in different buildings on the same network. For a simple 2-camera home setup, an analogue or wireless system may do the same job for less money.</p>
<h2>Common IP Mistakes</h2>
<p>The most common IP problems are weak networks, cheap switches and recorder incompatibility. A camera that keeps disconnecting is usually a network problem, not a camera problem. Proper planning — PoE capacity, cable quality and NVR compatibility — is part of every SmartShield IP installation, and we test every camera before handover.</p>
<h2>IP Cameras and Your Internet Connection</h2>
<p>Recording happens on your local network, so a slow internet connection does not affect recording quality. Internet speed only matters when you watch cameras remotely — and even then, the app usually streams a lower-resolution preview to save data. What matters more is the quality of your home or office network: a good router and proper cabling keep the system stable.</p>"""))
BLOG_POSTS.append(blog_post("home-security-camera-installation",
 "Home Security Camera Installation in Lahore: A Practical Guide | SmartShield Security",
 "Home security camera installation in Lahore: where to place cameras, which type to choose, costs, and how installation works.",
 "Home Security Camera Installation in Lahore",
 "11 November 2026",
 """<h2>Where Should Home Cameras Go?</h2>
<p>Start with the entry points: the main gate, the front door, the driveway and any side entrance. Then cover the boundary walls and the back of the house. Indoor cameras are only needed where you ask for them — a main hallway or living area — and never in bedrooms or bathrooms. The goal is to see who approaches and enters, not to watch the family.</p>
<h2>Which Cameras Suit a Home?</h2>
<p>Most Lahore homes use a mix: bullet cameras outdoors for the gate, driveway and boundary, and dome cameras indoors or at the entrance for wide, discreet coverage. Night vision matters for outdoor cameras, because most incidents happen after dark. For a typical house, 4 cameras cover the essentials; larger houses and villas usually need 6 or 8.</p>
<h2>What Does Home Installation Cost?</h2>
<p>Home CCTV installation in Lahore typically starts at PKR 12,500 for a basic wireless setup, and most home installations fall between PKR 12,500 and PKR 50,000 or more depending on camera count, type and storage. A 4MP camera typically costs PKR 6,000–12,000, with installation separate. Your final price is confirmed after a site assessment — use the <a href="../../calculator/index.html">Smart Calculator</a> for a preliminary estimate.</p>
<h2>How Installation Works</h2>
<ol><li>Share your house details — floors, entrances and what you want covered.</li><li>We recommend camera positions and a recorder.</li><li>You receive a package and budget proposal.</li><li>Installation, mobile viewing setup on your phone, and a walkthrough of viewing and playback.</li></ol>
<h2>Viewing on Your Phone</h2>
<p>Remote viewing is configured as part of installation where your system supports it. You can check the gate while you are at work, review recordings if something happens, and share access with family members. We set it up on your own phone and show you how to use it before we leave.</p>
<h2>Keeping Your Home System Working</h2>
<p>A home system needs very little care, but a little care goes a long way: wipe camera lenses every month or two, check that the recorder is still recording every week, and keep the recorder somewhere safe and ventilated. If a camera goes offline or the app stops connecting, check the power supply and the Wi-Fi first — those two causes cover most home faults.</p>"""))
BLOG_POSTS.append(blog_post("office-cctv-installation",
 "Office CCTV Installation in Lahore: Planning, Costs & Setup | SmartShield Security",
 "Office CCTV installation in Lahore: what to cover, privacy rules, recorder and access control, costs and how installation works.",
 "Office CCTV Installation in Lahore",
 "11 November 2026",
 """<h2>What Should Office Cameras Cover?</h2>
<p>Offices need coverage that protects staff, visitors and assets while respecting privacy. The areas that matter most are the entrance and reception, corridors, the server room, storage areas and the parking area. Cameras do not belong in washrooms, prayer rooms or private offices — and staff should know where cameras are and why.</p>
<h2>Planning an Office System</h2>
<p>Start with a walkthrough of the office: entrances, reception, corridors, meeting rooms, server and storage areas. Count the cameras per area, then choose the recorder — an NVR with IP cameras suits most offices, because it gives high resolution and room to grow. Recording access should be limited to the people you authorise, and retention is usually 15–30 days.</p>
<h2>What Does Office CCTV Cost?</h2>
<p>Office systems cost more than home systems because they have more cameras and longer cable runs. In Lahore, CCTV installation usually ranges between PKR 12,500 and PKR 50,000 or more, and larger offices go above that range. The exact price depends on camera count, resolution, recorder, storage and installation complexity, and is confirmed after a site assessment.</p>
<h2>Installation Without Disrupting Work</h2>
<p>Office installation is often scheduled outside working hours or in stages, so your team can keep working. Cabling is run neatly, cameras are mounted securely, and the recorder is placed somewhere safe and ventilated. Mobile viewing is set up for the authorised staff, with a short training walkthrough.</p>
<h2>Combining CCTV with Attendance</h2>
<p>Many offices install a biometric attendance machine alongside CCTV — cameras cover entrances and common areas, while the attendance machine handles staff records. Ask us about a combined office package.</p>
<h2>What to Check Before Signing Off</h2>
<p>Before the installation is signed off, check three things: every camera shows a clear live picture, playback works for recordings from earlier in the day, and the authorised staff can view the system on their phones. If any of these fail, it is fixed on the spot — not discovered weeks later when footage is actually needed. Keep a note of who has recording access, and review that list whenever staff change roles or leave.</p>
<h2>Privacy Rules Worth Knowing</h2>
<p>Staff should know where cameras are and why they are there. Cameras belong in entrances, corridors and common areas — not in washrooms, prayer rooms or private offices. A short written note telling staff what is recorded and who can view it prevents most misunderstandings, and it is good practice for any business.</p>"""))
BLOG_POSTS.append(blog_post("cctv-installation-for-shops",
 "CCTV Installation for Shops in Lahore: A Shopkeeper's Guide | SmartShield Security",
 "CCTV installation for shops in Lahore: cash counter, entrance and stock room coverage, costs, and what to check before buying.",
 "CCTV Installation for Shops in Lahore",
 "11 November 2026",
 """<h2>What a Shop Needs Covered</h2>
<p>For a shop, three positions matter most: the cash counter, the entrance and the stock room. The cash counter camera should show the till and the customer clearly. The entrance camera should show who comes in and out. The stock room camera protects inventory. A fourth camera on the sales floor covers the rest. Most small shops are well covered with 4 cameras.</p>
<h2>Choosing Cameras for a Shop</h2>
<p>Dome cameras suit the shop floor and counter — wide, discreet coverage. A bullet camera suits the entrance and any outdoor area. Night vision matters if the shop opens early or closes late. Resolution should be high enough to identify a person at the counter: 2MP is usually enough at short range, while 4MP gives more detail.</p>
<h2>What Does Shop CCTV Cost?</h2>
<p>Most small-shop installations in Lahore fall between PKR 12,500 and PKR 50,000, depending on camera count, recorder and storage. A 4MP camera typically costs PKR 6,000–12,000, with installation separate. The final price is confirmed after a site assessment — use the <a href="../../calculator/index.html">Smart Calculator</a> for a preliminary estimate.</p>
<h2>Recording and Playback</h2>
<p>Choose a retention period that fits how your shop works — 15–30 days is common, so you can review an incident discovered days later. Make sure the hard disk is large enough for your camera count and retention period, and test playback before the installer leaves. A system that records but cannot play back properly is useless when you need it.</p>
<h2>After Installation</h2>
<p>Keep lenses clean, check that recording is working every week or two, and keep the recorder in a safe, ventilated place — not on the shop floor where it can be damaged or unplugged. We offer maintenance visits that cover cleaning, storage checks and fault prevention.</p>
<h2>Common Shop Mistakes to Avoid</h2>
<p>The most common mistake is pointing the counter camera at the customer's back instead of the till — the footage then shows nothing useful when a dispute arises. Another is buying the cheapest hard disk and discovering a week later that it only keeps two days of recordings. And a third is never testing playback: a system can look fine on the live screen while recording nothing at all. Test playback on installation day, and check it again after the first week.</p>"""))
BLOG_POSTS.append(blog_post("night-vision-cctv-camera-price-in-pakistan",
 "Night Vision CCTV Camera Price in Pakistan (2026 Guide) | SmartShield Security",
 "Night vision CCTV camera prices in Pakistan: infrared vs colour night vision, what affects the price, and how to choose for your home or shop.",
 "Night Vision CCTV Camera Price in Pakistan",
 "11 November 2026",
 """<h2>Why Night Vision Matters</h2>
<p>Most security incidents happen after dark, so a camera that cannot see at night is only half a security system. Night vision cameras use infrared light or a white-light LED to record in darkness, and the quality of that night picture is often more important than the daytime picture.</p>
<h2>Infrared vs Colour Night Vision</h2>
<p>Infrared night vision records in black and white using invisible infrared light. It works in complete darkness and is the most common option. Colour night vision uses a visible white light or a sensitive sensor to record in colour at night — useful when you need to identify clothing colours or vehicle colours, but it needs some ambient light or its own LED, and it can disturb neighbours if the light is bright.</p>
<h2>What Do Night Vision Cameras Cost?</h2>
<p>Night vision is now standard on most cameras, so it does not add a large premium by itself. Prices depend mainly on resolution, brand and night vision range. As a reference, a 4MP camera in Pakistan typically costs PKR 6,000–12,000 depending on brand and features, with installation separate. Colour night vision models usually cost more than basic infrared models.</p>
<h2>What Affects Night Picture Quality?</h2>
<ul class="checklist"><li><strong>Infrared range</strong> — stated in metres; the camera must be close enough for its own light to reach the subject.</li><li><strong>Placement</strong> — infrared reflects off glass and walls, so cameras should not face windows directly.</li><li><strong>Lighting</strong> — a small amount of ambient light improves the picture noticeably.</li><li><strong>Lens and sensor quality</strong> — a better sensor gives a cleaner night image with less noise.</li></ul>
<h2>Choosing a Night Vision Camera</h2>
<p>For a gate or driveway, choose an infrared camera with a range that covers the full distance. For a shop entrance or a well-lit street, colour night vision can be worth the extra cost. Tell us where the camera will sit and how dark the area gets at night, and we will recommend a model that actually sees what you need it to see.</p>
<h2>Testing Night Vision Before You Buy</h2>
<p>Night vision specifications are measured in ideal conditions, so the real picture can differ. If possible, ask to see a sample recording from the same model at night, or have the installer demonstrate the camera after dark during installation. A camera that looks good in the shop may not perform the same way in your unlit driveway.</p>"""))

# --- Blog index ---
def blog_index():
    cards = ""
    for pth, title, desc, h1, prefix, inner, faqs, crumbs, img, alt in BLOG_POSTS:
        slug = pth.split("/")[1]
        short = title.split(" | ")[0]
        cards += f'<article class="card"><h3><a href="{slug}/index.html">{short}</a></h3><p>{desc}</p><a class="btn btn-outline" href="{slug}/index.html">Read the guide</a></article>'
    inner = f"""<p class="lead">Practical CCTV and security guides from SmartShield Security — written in plain language, based on the questions Lahore homeowners, shopkeepers and offices actually ask.</p>
<div class="grid grid-3" style="margin-top:28px">{cards}</div>"""
    return ("blog/index.html",
     "CCTV & Security Blog | Guides for Lahore Homes, Offices & Shops | SmartShield Security",
     "SmartShield Security blog: practical CCTV guides for Lahore — costs, DVR vs NVR, bullet vs dome, Hikvision vs Dahua, wireless and IP camera prices, night vision and more.",
     "CCTV & Security Blog", "../", inner, None,
     [("Home", "../index.html"), ("Blog", "../blog/index.html")], None, "")

# ---------- BUILD ----------
def build():
    B.home = new_home  # monkeypatch: build.py's build_all calls home()
    B.build_all_with_calc()
    # new pages
    all_urls = []
    for page in NEW_PAGES + BLOG_POSTS + [blog_index()]:
        path, title, desc, h1, prefix, inner, faqs, crumbs, img, img_alt = page
        html = inner
        # replace placeholders
        html = html.replace("PRICENOTE", price_note().replace("CALCPREFIX", prefix))
        html = html.replace("CALCPREFIX", prefix)
        write(path, content_page(path, title, desc, h1, prefix, html, faqs, crumbs, img, img_alt))
        all_urls.append(path.replace("index.html", ""))
    # also patch services hub links (CALCPREFIX inside NEW_PAGES already handled above)
    # sitemap: existing + new
    urls = ["", "about/", "calculator/", "projects/", "social-media/", "contact/", "privacy-policy/", "terms/"] + [f"services/{s}/" for s, *_ in B.SERVICES] + all_urls
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'  <url><loc>{BASE}/{u}</loc></url>\n' for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    print("TOTAL URLS IN SITEMAP:", len(urls))

if __name__ == "__main__":
    build()
