/* ============================================================
   Explorant — content data (features, plans, comparison)
   Edit these arrays to change the homepage content.
   ============================================================ */

// ---- Featured blocks: [icon-key, title, blurb] ----
const FEATS = [
  ["Phone","Phone Friendly","Explore your account on-the-go with Explorant's phone-friendly design."],
  ["Secure","Secure","Explorant prioritizes security, keeping your account information safe and private."],
  ["Chat","Discord Community","Join the vibrant Explorant Discord community to connect with fellow enthusiasts."],
  ["Tag","Design","A sleek, modern interface designed to make your account stand out."],
  ["Support","24/7 Support","Enjoy 24/7 support to address any queries or concerns you may have while using Explorant."],
  ["Accessibility","Accessibility","Explorant prioritizes accessibility, allowing you to view your account data from anywhere at any time."],
  ["Gift","Free to use","Explorant is free to use, providing access to valuable account data without any cost."],
  ["Check","Easy to use","Explorant is easy to use, making navigation and exploration effortless."],
  ["Bolt","Fast","Explorant excels in speed, delivering quick access to your account data."],
  ["Sync","Synchronized","Explorant ensures real-time updates and accurate information every time you update."],
];

// ---- Icon SVG paths (24x24, currentColor stroke) ----
const ICONS = {
  Phone:'<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
  Secure:'<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/><circle cx="12" cy="15.5" r="1.4"/>',
  Chat:'<path d="M4 5h16v11H10l-5 4v-4H4z"/>',
  Tag:'<path d="M20 13 13 20 3 10V3h7z"/><path d="M7 7h.01"/>',
  Support:'<path d="M3 12a9 9 0 0 1 18 0v4a2 2 0 0 1-2 2h-1v-6h-3v5H9v-5H6v6H5a2 2 0 0 1-2-2z"/>',
  Accessibility:'<circle cx="12" cy="4" r="2"/><path d="M5 8h14M12 8v8m-4 6 4-6 4 6"/>',
  Gift:'<rect x="3" y="8" width="18" height="4"/><rect x="5" y="12" width="14" height="8"/><path d="M12 8v12M12 8c-2 0-4-1-4-3a2 2 0 0 1 4-1c0 1 0 3 0 4zM12 8c2 0 4-1 4-3a2 2 0 0 0-4-1z"/>',
  Check:'<path d="M4 12l5 5 11-11"/>',
  Bolt:'<path d="M13 2L4 14h6l-1 8 9-12h-6z"/>',
  Sync:'<path d="M21 12a9 9 0 1 1-3-6.7M21 3v6h-6"/>',
  Star:'<path d="M12 2l3 7 7 .5-5.5 4.5 2 7-6.5-4-6.5 4 2-7L2 9.5 9 9z"/>',
};
function icon(name){
  return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"
    stroke-linecap="round" stroke-linejoin="round">${ICONS[name]||ICONS.Star}</svg>`;
}

// ---- Tier emblem (hexagon) ----
function tier(color){
  return `<svg viewBox="0 0 64 64"><polygon points="32,3 58,17 58,42 32,58 6,42 6,17"
    fill="${color}" opacity=".85"/><polygon points="32,12 48,21 48,40 32,49 16,40 16,21" fill="${color}"/></svg>`;
}

// ---- Plans ----
const PLANS = [
  { name:"RADIANT", price:"$10", per:"/m", slots:"5000 Slots", color:"#dd3f4c",
    cta:"https://www.patreon.com/checkout/Explorant?rid=10078696",
    badge:"Early Bird (50% OFF)",
    perks:["All perks of Ascendant","No Cooldown","Public Accounts","Public Profile"] },
  { name:"ASCENDANT", price:"$5", per:"/m", slots:"500 Slots", color:"#5aa7e0",
    cta:"https://www.patreon.com/checkout/Explorant?rid=10078688",
    badge:"Early Bird (50% OFF)",
    perks:["All perks of Silver","Decreased cooldown","Account Agents","Account Management"] },
  { name:"SILVER", price:"$0", per:"(Free)/m", slots:"10 Slots", color:"#9aa0a6",
    cta:"#register", badge:null,
    perks:["Account Details","Account Inventory","Account Store","Account Shareable Links"] },
];

// ---- Comparison rows: [label, radiant, ascendant, silver] (1 = yes, 0 = no) ----
const ROWS = [
  ["Account Slots","5000","500","10"],
  ["Account Slot Cooldown","0 seconds","2 hours","24 hours"],
  ["Public Profile",1,1,1],
  ["Public Account",1,1,1],
  ["Account Folders",1,1,1],
  ["Account Always Active",1,0,0],
  ["Account in Leaderboards",1,0,0],
  ["Account Value",1,1,1],
  ["Account Match History",1,1,0],
  ["Account Purchase History (Coming soon)",1,1,0],
  ["Account Bulk Delete",1,1,0],
  ["Account Label",1,1,1],
  ["Account Details",1,1,1],
  ["Account Bans",1,1,1],
  ["Account Ranks",1,1,1],
  ["Account Store",1,1,1],
  ["Account Night Market",1,1,1],
  ["Account Skins",1,1,1],
  ["Account Skin Variants",1,1,0],
  ["Account Buddies",1,1,1],
  ["Account Agents",1,1,1],
  ["Account Challenges",1,1,1],
  ["Account Links",1,1,1],
];
