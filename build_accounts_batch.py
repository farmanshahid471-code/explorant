#!/usr/bin/env python3
"""Build static account pages for slug QRnJpJB9 (Chota Seth) and 0KKftpEI (ZyRoX),
clone them into users.json / account directory / login seed, rebuild the deploy zip.

QRnJpJB9 — Chota Seth (cloned 2026-09-12):
  ADDED   : Reaver Spectre (Premium 1775), Ayakashi Phantom (Exclusive 1775)
  REMOVED : Mystbloom Phantom (2175), Rogue Vandal (2175), Singularity Sheriff (2175)
  skins 8900 -> 5925 | total 9900 -> 6925

0KKftpEI — ZyRoX (cloned 2026-09-12):
  ADDED   : Soulstrife Scythe (Exclusive 3550)
  REMOVED : Kuronami no Yaiba (5350)
  skins 7525 -> 5725 | total 7525 -> 5725
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TMPL = os.path.join(HERE, "site/templates/account.html")
USERS_PATHS = [os.path.join(HERE, "demo/data/users.json"),
               os.path.join(HERE, "site/data/users.json")]
INDEX = os.path.join(HERE, "index.html")

def WL(u): return "https://media.valorant-api.com/weaponskinlevels/" + u + "/displayicon.png"
def BD(u): return "https://media.valorant-api.com/buddies/" + u + "/displayicon.png"
def PC(u): return "https://media.valorant-api.com/playercards/" + u + "/smallart.png"
def SP(u): return "https://media.valorant-api.com/sprays/" + u + "/displayicon.png"
def IT(name, tier, price, img): return {"name": name, "tier": tier, "price": price, "img": img}

CT = "03621f52-342b-cf4e-4f86-9350a49c6d04"
def RK(name, n): return {"name": name, "icon": f"https://media.valorant-api.com/competitivetiers/{CT}/{n}/largeicon.png"}

BP_IMG = "https://app.explorant.space/static/default-battlepass.png"
AG_IMG = "https://preview.explorant.space/static/agents/"
NF = "Not Fetched Yet. Please Ask Owner to Refresh Account"

# =====================================================================  
# ACCOUNT 1 — Chota Seth (QRnJpJB9)
# =====================================================================
CS_SKINS = [
    IT("VCT 2026 Sigil",       "Exclusive", 5350, WL("fb970da4-4f6a-5cb6-a484-1abf95e6f12d")),
    IT("Kuronami Vandal",      "Exclusive", 2375, WL("636c1f83-44f7-6bc4-0b24-88a1beb66c2d")),
    IT("Reaver Spectre",       "Premium",   1775, WL("0a0237d3-4d57-0ed2-ab65-c898a7bc755b")),
    IT("Ayakashi Phantom",     "Exclusive", 1775, WL("27acfa4d-4c6e-5f16-496e-f7baad3e00e0")),
    IT("Insidious Marshal",      "Select", 0, WL("c6ad0bef-4121-f0f2-1e24-9797be0b4ceb")),
    IT("Crash Out Stinger",      "Select", 0, WL("3a71ac66-4c4b-0d9a-89e8-a2a052030cbe")),
    IT("Crash Out Bandit",       "Select", 0, WL("29f343b9-4387-b17f-dfdf-2bb1f66cd75b")),
    IT("Keys to Elysium Vandal", "Deluxe", 0, WL("6a752806-4097-beff-6ef2-9c8e27100d36")),
    IT("Crash Out Spectre",      "Select", 0, WL("010c738b-4ac0-b4ea-d6d9-cca5a62133c1")),
    IT("Insidious Frenzy",       "Select", 0, WL("92b56cb5-4d2f-34d7-abb2-f1a10cff2026")),
    IT("Insidious Odin",         "Select", 0, WL("2940f37c-40cf-4094-fa0a-e9bfc62c0f5c")),
    IT("Keys to Elysium Ares",   "Deluxe", 0, WL("8fe097f6-433f-546e-aaf2-5a99fed23576")),
]
CS_STORE = [
    IT("VALORANT GO! Vol. 1 Ghost",   "Premium", 1775, WL("2dd042e4-409e-c8ed-ec76-758529e49d99")),
    IT("VALORANT GO! Vol. 2 Classic", "Premium", 1775, WL("68ee5c6c-4424-e95a-f46f-c08ec2dfeb97")),
    IT("Reaver Vandal",               "Premium", 1775, WL("ba42fe63-457a-78ce-4499-47950a698129")),
    IT("Origin Operator",             "Premium", 1775, WL("4d19c241-4350-6658-f5a6-5c99ca8e5e99")),
]
CS_ACCESSORY = [
    IT("Dream Team Spray",    "", 6000, SP("891758c9-4723-b867-2f9c-60ae7859388d")),
    IT("Warning: Viper Spray","", 4000, SP("259c5d79-474a-0f7c-52b3-7785a142ec7a")),
    IT("My Leg Spray",        "", 4000, SP("b076da33-4050-78d7-d0b1-86ad96cf14ea")),
    IT("Reyna ID Card",       "", 4500, PC("1fb0bee0-49db-fb51-b090-bc834babdb2b")),
]
CS_BUDDIES = [IT(n, "", 0, BD(u)) for n, u in [
    ("Night Regent Buddy",    "c05b209d-4a09-d7a3-634b-9bb23d63348d"),
    ("VALORANT Coin Buddy",   "ac72bb9a-4368-8502-5dac-698d72021c81"),
    ("Last Light Buddy",      "da5e2770-4b11-6c60-b468-979d0942b386"),
    ("Nest Egg Buddy",        "89ac98ec-495d-680b-22cb-d3afe04eae6e"),
    ("Insidious Buddy",       "076d1997-4ec1-d582-fc18-c790f4c3336f"),
    ("Insidious Buddy",       "076d1997-4ec1-d582-fc18-c790f4c3336f"),
    ("Last Light Buddy",      "da5e2770-4b11-6c60-b468-979d0942b386"),
    ("V26 ACT II Coin Buddy", "5dcc7d9e-4ef4-2189-698d-539e6257ea9e"),
    ("V26 ACT II Coin Buddy", "5dcc7d9e-4ef4-2189-698d-539e6257ea9e"),
    ("Keys to Elysium Buddy", "bfc0e6c2-49b2-7253-6838-158e86394f3a"),
    ("Nest Egg Buddy",        "89ac98ec-495d-680b-22cb-d3afe04eae6e"),
    ("Keep it Safer Buddy",   "c14745d0-4958-26d9-60e6-7c863080fef1"),
    ("Shadow Kitty Buddy",    "b33221a7-4fdb-507a-e4aa-1ba18111a3d9"),
    ("Night Regent Buddy",    "c05b209d-4a09-d7a3-634b-9bb23d63348d"),
    ("Keys to Elysium Buddy", "bfc0e6c2-49b2-7253-6838-158e86394f3a"),
    ("V26 ACT III Coin Buddy","996795a4-408a-0e71-2e23-5ea4aeecf76b"),
    ("Shadow Kitty Buddy",    "b33221a7-4fdb-507a-e4aa-1ba18111a3d9"),
    ("V26 ACT III Coin Buddy","996795a4-408a-0e71-2e23-5ea4aeecf76b"),
]]
CS_CARDS = [IT(n, "", 0, PC(u)) for n, u in [
    ("Fearmonger Card",             "afbb0530-47c3-cf58-c09c-359f8dfacda9"),
    ("New Recruit Card",            "612cd02d-4294-ee2a-644c-a3ba3ddf8805"),
    ("Ready, Aim Card",             "fd104d51-4304-e379-1b2c-f7af9016eb8a"),
    ("Paintbrush Tactics Card",     "213c4c4a-44e6-12a5-6ab2-ae8282e93e57"),
    ("Puzzles & Bears Card",        "f6f2be5f-432e-7cfb-8d5e-f8b344c51fb5"),
    ("Code Red Card",               "c89194bd-4710-b54e-8d6c-60be6274fbb2"),
    ("Tacti-Ops Card",              "224e6a53-4463-5694-95b0-2a9dcd2fcd42"),
    ("Corrode Schema Card",         "a9222582-4686-0ab2-2ed4-54942463ec30"),
    ("Garden of Heroes: Sage Card", "b9e318c3-4590-d095-0218-ac92e1405459"),
    ("Keys to Elysium Card",        "58595294-4eab-f19a-88f9-c2bae39ce455"),
    ("Insidious Card",              "42912d8e-41ea-767c-1912-6a85b8ca02bd"),
    ("Personal Setup // Sova Card", "5affc285-413d-cd21-54ac-b6bf16d3f8dd"),
    ("V Protocol Card",             "0819fbcd-4bd4-c379-5384-52803440f2b2"),
    ("Blue Screen of Death Card",   "478b9b69-42a8-8288-08eb-dab23289c226"),
]]
CS_SPRAYS = [IT(n, "", 0, SP(u)) for n, u in [
    ("Green Means Go Spray",        "763ab2ad-4e9b-5b74-53f0-4f96d5993efb"),
    ("Keys to Elysium Spray",       "23592b04-4518-2446-fa97-e08eb891c285"),
    ("V for VALORANT Spray",        "5d88fd45-434d-b0d6-2331-e8b3d47b8395"),
    ("Boss Bear Spray",             "44e7493c-4199-2987-6464-5e890120c8fa"),
    ("11 - 11 Spray",               "46612f44-40c8-2029-d2eb-6ba41cf379bb"),
    ("GLHF Spray",                  "6983ae7c-4cb5-835c-8f62-b7affbaae20e"),
    ("Acorn Ops Spray",             "7be05688-4141-f625-3990-c3933cdbaebd"),
    ("Insidious Spray",             "0de614da-48b7-9dab-0bd1-a09d287695aa"),
    ("Time Out Spray",              "0c8e9768-4d7e-c736-ce07-62b2767d52cd"),
    ("Stained Glass // Rose Spray", "627c2ea9-46d1-3eeb-4751-ae9747d48e3c"),
    ("Display Only Spray",          "cee8d6a2-44c3-f0e0-9f79-3ea94f957a56"),
    ("Crash Out Spray",             "589e9400-4f2d-55c2-3200-aaafe4e63716"),
    ("Seen Things Spray",           "ea4854b3-4522-df03-5f43-5a9ba4ea88db"),
]]
CS_BP = [IT("Season 2026 // Act III", "", 0, BP_IMG)]
CS_AGENTS = [{"name": n, "tier": "", "price": 0, "img": AG_IMG + u + ".png"} for n, u in [
    ("Reyna Contract", "4c9b0fcf-57cd-4e84-ae5a-ce89e396242f"),
    ("Gekko Contract", "cae6ab4a-4b4a-69a0-3c7a-48b17e313f52"),
    ("Clove Gear",     "59019709-44fe-f723-da01-848df9ac0413"),
]]
CS_WTOT = sum(s["price"] for s in CS_SKINS)     # 5925
CS_BP_T = 1000
CS_TOTAL = CS_WTOT + CS_BP_T                    # 6925

CHOTA = {
    "username": "Chota Seth", "password": "", "name": "Chota Seth", "title": "From the Grave",
    "region": "eu", "country": "tur", "level": 27, "levelNow": 3024, "levelMax": 5000,
    "totalValue": CS_TOTAL,
    "banner": "https://media.valorant-api.com/playercards/afbb0530-47c3-cf58-c09c-359f8dfacda9/wideart.png",
    "ranks": [RK("V26 - ACT III", 13), RK("V26 - ACT II", 12)],
    "skins": CS_SKINS, "buddies": CS_BUDDIES, "cards": CS_CARDS, "sprays": CS_SPRAYS,
    "flexes": [], "titles": ["Gnarly", "From the Grave", "All Gas", "Tea", "Recruit"],
    "missions": [],
    "store": CS_STORE, "accessory": CS_ACCESSORY,
    "daily": {"vp": 275, "rp": 15}, "accessoryCur": {"vp": 275, "rp": 15},
    "dailyEmptyMsg": "Daily Missions " + NF,
    "battlepasses": CS_BP, "bpTotal": CS_BP_T,
    "agents": CS_AGENTS, "agentTotal": 1000,
    "nextFirstWin": "-", "nextWeekly": "-",
    "expired": False, "slug": "QRnJpJB9",
}

# =====================================================================
# ACCOUNT 2 — ZyRoX (0KKftpEI)
# =====================================================================
ZX_SKINS = [
    IT("Soulstrife Scythe",      "Exclusive", 3550, WL("656c5de8-47ca-4eeb-6051-c9aabbf37baa")),
    IT("Prelude to Chaos Vandal","Exclusive", 2175, WL("1010fb40-4344-6ec8-2a8a-33bf076339b6")),
]
ZX_BUDDIES = [IT(n, "", 0, BD(u)) for n, u in [
    ("Smite Knife Buddy",     "9a4b137f-48f6-e46b-aef1-0a8a8df17a57"),
    ("5 Years Buddy",         "1cb1cfef-4976-ad93-27bc-7a89b5e6fb2f"),
    ("V25 ACT III Coin Buddy","d782c0e3-47af-494b-8f6e-dfad9cf0f703"),
    ("5 Years Buddy",         "1cb1cfef-4976-ad93-27bc-7a89b5e6fb2f"),
    ("V25 ACT IV Coin Buddy", "9024d9bf-466b-3592-58c3-deb9b494e7fa"),
    ("V25 ACT III Coin Buddy","d782c0e3-47af-494b-8f6e-dfad9cf0f703"),
    ("V25 ACT IV Coin Buddy", "9024d9bf-466b-3592-58c3-deb9b494e7fa"),
    ("VALORANT Coin Buddy",   "ac72bb9a-4368-8502-5dac-698d72021c81"),
    ("Smite Knife Buddy",     "9a4b137f-48f6-e46b-aef1-0a8a8df17a57"),
]]
ZX_CARDS = [IT(n, "", 0, PC(u)) for n, u in [
    ("V Protocol Card",        "0819fbcd-4bd4-c379-5384-52803440f2b2"),
    ("All Together Now Card",  "30b7c48a-45d3-a4bd-6ec6-0887a760f4d6"),
    ("Code Red Card",          "c89194bd-4710-b54e-8d6c-60be6274fbb2"),
    ("New Recruit Card",       "612cd02d-4294-ee2a-644c-a3ba3ddf8805"),
    ("5 Years: Ignition Card", "5def384f-47ce-ee1e-8a4c-d1a394fef0b5"),
    ("Thread Swap Card",       "5a6961da-4936-f39a-539a-b8b8f151b73a"),
    ("5 Years: Duelists Card", "af33fc06-4d7a-4a57-1ae5-b2b046c499ab"),
    ("Party Of One Card",      "d839e6e0-48fe-602b-cdf5-d4b3fb91618f"),
    ("Made It Myself Card",    "2ffc86da-479f-0023-1d8a-3581224a88e0"),
]]
ZX_SPRAYS = [IT(n, "", 0, SP(u)) for n, u in [
    ("5 Years Spray",        "d6646372-4fb8-bd2d-9f62-b4a9cb8e0799"),
    ("GLHF Spray",           "6983ae7c-4cb5-835c-8f62-b7affbaae20e"),
    ("V for VALORANT Spray", "5d88fd45-434d-b0d6-2331-e8b3d47b8395"),
]]
ZX_AGENTS = [{"name": "Iso Gear", "tier": "", "price": 0,
              "img": AG_IMG + "26c6e81f-4d62-e55e-24e7-3d8fa37e3b97.png"}]
ZX_WTOT = sum(s["price"] for s in ZX_SKINS)     # 5725
ZX_TOTAL = ZX_WTOT                              # bp 0

ZYROX = {
    "username": "ZyRoX", "password": "", "name": "ZyRoX", "title": "Sunkissed",
    "region": "eu", "country": "tur", "level": 20, "levelNow": 176, "levelMax": 5000,
    "totalValue": ZX_TOTAL,
    "banner": "https://media.valorant-api.com/playercards/5def384f-47ce-ee1e-8a4c-d1a394fef0b5/wideart.png",
    "ranks": [], "ranksEmptyMsg": "No Ranks to Show",
    "skins": ZX_SKINS, "buddies": ZX_BUDDIES, "cards": ZX_CARDS, "sprays": ZX_SPRAYS,
    "flexes": [], "flexesEmptyMsg": "Flexes " + NF,
    "titles": ["Recruit", "5th", "Eh?", "5K", "Sunkissed", "5 Years", "Galactic"],
    "missions": [], "dailyEmptyMsg": "Daily Missions " + NF,
    "store": [], "accessory": [],
    "daily": {"vp": 0, "rp": 0}, "accessoryCur": {"vp": 0, "rp": 0},
    "nmEmptyMsg": "Night Market Skins " + NF,
    "battlepasses": [], "bpTotal": 0, "bpEmptyMsg": "Battlepasses " + NF,
    "agents": ZX_AGENTS, "agentTotal": 0,
    "nextFirstWin": "-", "nextWeekly": "-",
    "info": [["Email", "No"], ["Phone", "No"]],
    "expired": False, "slug": "0KKftpEI",
}

ACCOUNTS = [CHOTA, ZYROX]

# =====================================================================
# TEMPLATE → PAGE BUILDER
# =====================================================================
def build_page(user):
    html = open(TMPL, encoding="utf-8").read()

    html = re.sub(r"<title>.*?</title>",
                  f"<title>{user['name']} - Explorant</title>", html, count=1, flags=re.S)

    assert "const BP_TOTAL = 0;" in html
    html = html.replace("const BP_TOTAL = 0;", "var BP_TOTAL = 0;")

    html = re.sub(r'const NEXT_FIRST_WIN\s*=\s*"[^"]*";',
                  f'const NEXT_FIRST_WIN = "{user["nextFirstWin"]}";', html, count=1)
    html = re.sub(r'const NEXT_WEEKLY\s*=\s*"[^"]*";',
                  f'const NEXT_WEEKLY    = "{user["nextWeekly"]}";', html, count=1)

    # header value slots
    html = html.replace('<div class="title-card"><div class="title-text">Agents</div><div class="title-cur"></div></div>',
                        '<div class="title-card"><div class="title-text">Agents</div><div class="title-cur" id="agentValue"></div></div>')
    html = html.replace('<div class="title-card"><div class="title-text">Accessory Store</div><div class="title-cur"></div></div>',
                        '<div class="title-card"><div class="title-text">Accessory Store</div><div class="title-cur" id="accessoryCur"></div></div>')

    # configurable empty states
    html = html.replace('el.innerHTML=`<div class="empty" style="grid-column:1/-1;">No Items to Show</div>`;',
                        'el.innerHTML=`<div class="empty" style="grid-column:1/-1;">${el.getAttribute("data-empty")||"No Items to Show"}</div>`;')
    html = html.replace('<div class="list-grid" id="dailyStore"></div>',
                        '<div class="list-grid" id="dailyStore" data-empty="Store Skins Not Fetched Yet. Please Ask Owner to Refresh Account"></div>')
    html = html.replace('<div class="list-grid" id="accessoryStore"></div>',
                        '<div class="list-grid" id="accessoryStore" data-empty="Accessory Skins Not Fetched Yet. Please Ask Owner to Refresh Account"></div>')
    html = html.replace('<div class="empty-h5">No Night Market Skins to Show</div>',
                        '<div class="empty-h5" id="nmEmpty">No Night Market Skins to Show</div>')
    html = html.replace('<div class="empty-h5">No Daily Missions</div>',
                        '<div class="empty-h5" id="dailyEmpty">No Daily Missions</div>')

    # ranks message override hook
    html = html.replace('>Ranks Not Fetched Yet. Please Ask Owner to Refresh Account</div>',
                        '>${window.RANKS_EMPTY_MSG||"Ranks Not Fetched Yet. Please Ask Owner to Refresh Account"}</div>')

    # weekly-missions empty message
    OLD_MIS = 'document.getElementById("missionList").innerHTML=MISSIONS.map((m,i)=>`'
    NEW_MIS = ('if(!MISSIONS.length){ document.getElementById("missionList").innerHTML='
               '`<div class="text-muted" style="grid-column:1/-1;text-align:center;line-height:1.8;font-size:.9rem;">'
               'Weekly Missions Not Fetched Yet. Please Ask Owner to Refresh Account</div>`; } else '
               'document.getElementById("missionList").innerHTML=MISSIONS.map((m,i)=>`')
    assert OLD_MIS in html
    html = html.replace(OLD_MIS, NEW_MIS)

    # extra info rows (Email / Phone / Registration Date)
    OLD_INFO = ('<p class="themed-lbl">Country</p><p class="val">${esc(ACCOUNT.country)}</p>`;')
    NEW_INFO = (OLD_INFO + '\nif(window.__INFO){ document.getElementById("infoCol").innerHTML += '
                'window.__INFO.map(function(r){ return \'<p class="themed-lbl">\'+r[0]+\'</p><p class="val">\'+esc(r[1])+\'</p>\'; }).join(""); }')
    assert OLD_INFO in html
    html = html.replace(OLD_INFO, NEW_INFO)

    # hydration extensions
    OLD_HYD = '    __fill(FLEXES,  __sel.flexes, "skin","#c5c5ff","rifle");\n  }catch(e){}'
    NEW_HYD = '''    __fill(FLEXES,  __sel.flexes, "skin","#c5c5ff","rifle");
    if(__sel.agents && __sel.agents.length){ __fill(AGENTS, __sel.agents, "agent","#c5c5ff","rifle"); }
    if(__sel.battlepasses && __sel.battlepasses.length){ __fill(BATTLEPASSES, __sel.battlepasses, "skin","#c5c5ff","rifle"); }
    if(__sel.store && __sel.store.length){ __fill(STORE, __sel.store, "skin","#c5c5ff","rifle"); }
    if(__sel.accessory && __sel.accessory.length){ __fill(ACCESSORY, __sel.accessory, "skin","#c5c5ff","rifle"); }
    if(typeof __sel.bpTotal==="number"){ BP_TOTAL=__sel.bpTotal; }
    if(__sel.ranksEmptyMsg){ window.RANKS_EMPTY_MSG=__sel.ranksEmptyMsg; }
    if(__sel.info){ window.__INFO=__sel.info; }
    var __VP="https://media.valorant-api.com/currencies/85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741/displayicon.png";
    var __RP="https://media.valorant-api.com/currencies/e59aa87c-4cbf-517a-5983-6e81511be9b7/displayicon.png";
    function __cur(elId,d){ var el=document.getElementById(elId); if(!el||!d) return;
      el.innerHTML='<img src="'+__VP+'" alt="vp" onerror="this.style.display=\\'none\\'"/><span class="cur">'+(d.vp||0)+'</span>&nbsp;&nbsp;'
                  +'<img src="'+__RP+'" alt="rp" onerror="this.style.display=\\'none\\'"/><span class="cur">'+(d.rp||0)+'</span>'; }
    __cur("dailyCur",__sel.daily); __cur("accessoryCur",__sel.accessoryCur);
    if(typeof __sel.agentTotal==="number"){ var __ag=document.getElementById("agentValue"); if(__ag) __ag.innerHTML='<span class="cur">Total Value: '+__sel.agentTotal+'</span><img src="'+__VP+'" alt="vp" onerror="this.style.display=\\'none\\'"/>'; }
    if(__sel.nmEmptyMsg){ var __nm=document.getElementById("nmEmpty"); if(__nm) __nm.textContent=__sel.nmEmptyMsg; }
    if(__sel.dailyEmptyMsg){ var __de=document.getElementById("dailyEmpty"); if(__de) __de.textContent=__sel.dailyEmptyMsg; }
    if(!BATTLEPASSES.length && __sel.bpEmptyMsg){ document.getElementById("bpBody").innerHTML='<div class="empty-h5">'+__sel.bpEmptyMsg+'</div>'; }
    if(!FLEXES.length && __sel.flexesEmptyMsg){ document.getElementById("flexes").textContent=__sel.flexesEmptyMsg; }
  }catch(e){}'''
    assert OLD_HYD in html
    html = html.replace(OLD_HYD, NEW_HYD)

    sel_line = 'var __sel = JSON.parse(localStorage.getItem("explorant_view_account")||"null");'
    assert sel_line in html
    payload = json.dumps(user, ensure_ascii=False, separators=(",", ": ")).replace("</", "<\\/")
    html = html.replace(sel_line, "var __sel = " + payload + ";")
    return html

for user in ACCOUNTS:
    out = os.path.join(HERE, "account", user["slug"], "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    page = build_page(user)
    open(out, "w", encoding="utf-8").write(page)
    print(f"built {out}  (skins {len(user['skins'])}, wpn {sum(s['price'] for s in user['skins'])}, total {user['totalValue']})")

# --------------------------------------------------- users.json (both) -----
existing = json.load(open(USERS_PATHS[0], encoding="utf-8"))
have = {u.get("slug") for u in existing} | {u.get("username") for u in existing}
for path in USERS_PATHS:
    users = json.load(open(path, encoding="utf-8"))
    users = [u for u in users if u.get("slug") not in {"QRnJpJB9", "0KKftpEI"}
             and u.get("username") not in {"Chota Seth", "ZyRoX"}]
    for user in ACCOUNTS:
        if user["slug"] not in {u.get("slug") for u in users}:
            users.append(user)
    json.dump(users, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{path}: {len(users)} accounts")

# ------------------------------------------------ account directory --------
DIR_ = os.path.join(HERE, "account/index.html")
d = open(DIR_, encoding="utf-8").read()
for slug, name in [("z0IukRwx", "ln1"), ("QRnJpJB9", "Chota Seth"), ("0KKftpEI", "ZyRoX")]:
    if f'href="{slug}/"' not in d:
        d = d.replace("</li></ul>", f'</li>\n<li><a href="{slug}/">{name}</a><span class="u">/account/{slug}/</span></li></ul>')
        print(f"directory: added {name}")
open(DIR_, "w", encoding="utf-8").write(d)

# ------------------------------------------------ login seed ---------------
src = open(INDEX, encoding="utf-8").read()
m = re.search(r'<script id="seed" type="application/json">(.*?)</script>', src, re.S)
assert m
seed = json.loads(m.group(1))
have = {u.get("slug") for u in seed}
allusers = json.load(open(USERS_PATHS[0], encoding="utf-8"))
added = 0
for u in allusers:
    if u.get("slug") in {"z0IukRwx", "QRnJpJB9", "0KKftpEI"} and u["slug"] not in have:
        seed.append(u); have.add(u["slug"]); added += 1
src = src.replace(m.group(1), json.dumps(seed, ensure_ascii=False, separators=(",", ": ")).replace("</", "<\\/"))
open(INDEX, "w", encoding="utf-8").write(src)
print(f"login seed: +{added} -> {len(seed)} accounts")

# ------------------------------------------------ sanity -------------------
for user, gone in [(CHOTA, ["Mystbloom Phantom", "Rogue Vandal", "Singularity Sheriff"]),
                   (ZYROX, ["Kuronami no Yaiba"])]:
    names = [s["name"] for s in user["skins"]]
    for g in gone:
        assert g not in names, f"{g} still in {user['slug']} skins!"
    print(f"{user['slug']}: removals verified ✔")
print("DONE")
