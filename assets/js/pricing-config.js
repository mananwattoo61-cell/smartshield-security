/* SmartShield Security — central editable pricing configuration.
 * DEMO MODE: these are placeholder demo rates in PKR, NOT real quotations.
 * The business owner should update every value below before publishing
 * real prices. The calculator reads ONLY this file for prices. */
window.SMARTSHIELD_CONFIG = {
  DEMO_MODE: true,
  CURRENCY: "PKR",
  WHATSAPP_NUMBER: "923059502580",
  PHONE_DISPLAY: "03059502580",
  PHONE_TEL: "+923059502580",
  /* Social links — update in one place. Empty string = link to be added. */
  SOCIAL_LINKS: {
    facebook: "",
    instagram: "",
    tiktok: "",
    youtube: "",
    linkedin: "",
    whatsapp: "https://wa.me/923059502580"
  },
  /* Demo camera unit prices (PKR per camera) */
  CAMERA_PRICES: {
    "HD Analog Cameras": 8500,
    "IP Cameras": 14500,
    "AI-Enabled Cameras": 22000,
    "Dome Cameras": 12000,
    "Bullet Cameras": 13500,
    "PTZ Cameras": 45000,
    "Mixed Camera Setup": 16000
  },
  TIER_MULTIPLIER: { "Budget-Friendly": 0.9, "Standard": 1.0, "Premium": 1.25 },
  RECORDER_PRICES: { DVR: 18000, NVR: 28000 },
  /* Indicative storage: GB per camera per day (2MP, H.265, motion-aware) */
  STORAGE_GB_PER_CAM_PER_DAY: { "HD Analog Cameras": 15, "IP Cameras": 25, "AI-Enabled Cameras": 30, "Dome Cameras": 20, "Bullet Cameras": 22, "PTZ Cameras": 28, "Mixed Camera Setup": 24 },
  HDD_PRICES: { "1 TB": 12000, "2 TB": 18000, "4 TB": 28000, "6 TB": 42000, "8 TB": 58000 },
  EQUIPMENT_PRICES: {
    "DVR / NVR": 0, /* priced via recorder above; kept here for display */
    "Hard Disk": 0, /* priced via storage above */
    "PoE Switch": 9500,
    "Network Cabling": 85, /* per metre, estimated 15 m per camera */
    "Power Supply": 4500,
    "UPS / Backup": 18000,
    "Installation Accessories": 3500,
    "Mobile Configuration": 3000,
    "Additional Monitors": 22000
  },
  INSTALL_PER_CAMERA: 2500,
  CONFIGURATION_CHARGE: 5000,
  TRANSPORT_CHARGE: 0
};
