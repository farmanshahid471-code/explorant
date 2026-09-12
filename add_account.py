#!/usr/bin/env python3
"""Add the 'Chaku Wala Jatt' account (slug qsWQaSIq) scraped from
preview.explorant.space/account/qsWQaSIq/ with two requested skin swaps:
  Arcane Vandal  -> Reaver Vandal   (Premium, 1775 VP)
  Helix Phantom  -> Ayakashi Phantom (Exclusive, 1775 VP)
"""
import json, os, re

HERE = "/home/user"
USERS = os.path.join(HERE, "demo/data/users.json")

def itm(name, img, tier="", price=0):
    return {"name": name, "tier": tier, "price": price, "img": img}

WL = "https://media.valorant-api.com/weaponskinlevels/"
BD = "https://media.valorant-api.com/buddies/"
PC = "https://media.valorant-api.com/playercards/"
SP = "https://media.valorant-api.com/sprays/"

new_user = {
    "username": "qsWQaSIq",
    "password": "",
    "name": "Chaku Wala Jatt",
    "title": "ZZZ",
    "region": "eu",
    "country": "pak",
    "level": 57,
    "levelNow": 657,
    "levelMax": 5000,
    "totalValue": 4550,  # skins 3550 (after swaps) + battlepass 1000
    "banner": PC + "201be320-4a18-cd81-75fa-228dba06d676/wideart.png",
    "ranks": [
        {"name": "V26 - ACT III",     "icon": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/18/largeicon.png"},
        {"name": "V26 - ACT II",      "icon": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/16/largeicon.png"},
        {"name": "V26 - ACT I",       "icon": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/16/largeicon.png"},
        {"name": "V25 - ACT I",       "icon": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/12/largeicon.png"},
        {"name": "EPISODE 9 - ACT 3", "icon": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/5/largeicon.png"},
    ],
    "skins": [
        # swap 1: Arcane Vandal -> Reaver Vandal (Premium, 1775)
        itm("Reaver Vandal",   WL + "ba42fe63-457a-78ce-4499-47950a698129/displayicon.png", "Premium", 1775),
        # swap 2: Helix Phantom -> Ayakashi Phantom (Exclusive, 1775)
        itm("Ayakashi Phantom", WL + "27acfa4d-4c6e-5f16-496e-f7baad3e00e0/displayicon.png", "Exclusive", 1775),
        itm("Soulburst Bandit",   WL + "d8606d62-4a88-39d6-4e65-3993b0f3f9b2/displayicon.png", "Select"),
        itm("Hieroscape Bulldog", WL + "b182db0d-4289-24b4-2a73-1dba55f76070/displayicon.png", "Deluxe"),
        itm("Moon Scout Sheriff", WL + "e0c772a1-45e3-4788-6430-dea1467bd1e6/displayicon.png", "Select"),
        itm("Celestia Ghost",     WL + "9c88beec-481e-e407-ff44-b2acccf3d46f/displayicon.png", "Select"),
        itm("Hieroscape Phantom", WL + "31cd5d6c-42fd-2e31-228d-9f8c1bfad552/displayicon.png", "Deluxe"),
        itm("Celestia Operator",  WL + "1954ba1b-4e97-dcf4-890f-308b967d83b2/displayicon.png", "Select"),
        itm("Celestia Spectre",   WL + "6462af7f-4e37-938a-3ca3-77a7bfdaf4bb/displayicon.png", "Select"),
        itm("Nanobreak Sheriff",  WL + "559bb49c-4839-0115-3302-d99c7813d1cb/displayicon.png", "Select"),
        itm("Moon Scout Guardian", WL + "f5b88fd8-427e-76a0-3f61-5b8c4d930c8b/displayicon.png", "Select"),
        itm("Celestia Stinger",   WL + "85068834-4751-c963-7071-efa6d19aebc3/displayicon.png", "Select"),
        itm("Moon Scout Bucky",   WL + "3a250136-49d2-a667-a882-599a048ef31f/displayicon.png", "Select"),
        itm("Hieroscape Blades",  WL + "3dff07ac-4ad7-0ac2-9125-988ba7137448/displayicon.png", "Exclusive"),
        itm("Hieroscape Ares",    WL + "0a0d85b3-447a-49f8-d0ce-199091762d7e/displayicon.png", "Deluxe"),
        itm("Moon Scout Outlaw",  WL + "efd2f811-4dae-b4dc-c9b2-d8a3fe9f27c2/displayicon.png", "Select"),
        itm("Hieroscape Frenzy",  WL + "b897b05b-4fac-c017-dce1-e9a0c6cddba5/displayicon.png", "Deluxe"),
    ],
    "buddies": [
        itm("Epilogue: Super Saver Buddy", BD + "8fd7deb8-4696-6452-aa4d-7cb35efacd69/displayicon.png"),
        itm("Space Out Homie Buddy",        BD + "973863f5-44e0-be67-e360-8795a56295b7/displayicon.png"),
        itm("V26 ACT III Coin Buddy",       BD + "996795a4-408a-0e71-2e23-5ea4aeecf76b/displayicon.png"),
        itm("Chilling Nugget Buddy",        BD + "53731622-46ad-c7a8-d2d2-5194ac70ee97/displayicon.png"),
        itm("Fresh Frags Buddy",            BD + "e54d445d-4c1b-2c90-35fa-61be5770a5b9/displayicon.png"),
        itm("V25A3: Gold Buddy",            BD + "d74c34ed-4e90-224b-bf6e-dba9d0fea145/displayicon.png"),
        itm("Epilogue: Scaredy Cow Buddy",  BD + "1789770d-43dc-ace2-bdc0-08bd60eff433/displayicon.png"),
        itm("Astro Bear Buddy",             BD + "5d91fa1b-4bd2-7cc9-692f-f798a7f3ef11/displayicon.png"),
        itm("Nest Egg Buddy",               BD + "89ac98ec-495d-680b-22cb-d3afe04eae6e/displayicon.png"),
        itm("Student TactiBear Buddy",      BD + "542bbefc-4f38-02f8-2a2c-42bd4d4170f2/displayicon.png"),
        itm("V26 ACT II Coin Buddy",        BD + "5dcc7d9e-4ef4-2189-698d-539e6257ea9e/displayicon.png"),
        itm("Hieroscape Buddy",             BD + "8824784d-4c1a-1200-338e-5c8c0d32111f/displayicon.png"),
        itm("Laser Blaster Buddy",          BD + "72973c4b-4ef3-c9c8-06c8-54a350beeae8/displayicon.png"),
        itm("VALORANT Coin Buddy",          BD + "ac72bb9a-4368-8502-5dac-698d72021c81/displayicon.png"),
        itm("Epilogue: Mummy Mance Buddy",  BD + "cf0c35fc-4560-7a57-9dc3-91b65da6cd06/displayicon.png"),
        itm("Ep 9 // 3 Coin Buddy",         BD + "a5111d11-4374-23c4-f2e9-eda50de1f475/displayicon.png"),
        itm("Celestia Buddy",               BD + "090f9c75-4581-c33c-6fe3-a8b5782a940f/displayicon.png"),
        itm("Fa Buddy",                     BD + "fee36e9f-4136-4d78-9ea4-fd8f89fa040a/displayicon.png"),
        itm("V25 ACT I Coin Buddy",         BD + "8b1100e0-4c4a-5a6e-d21d-b9ba6688f6cb/displayicon.png"),
        itm("Scaredy Cow Buddy",            BD + "068fa5af-42c2-2f91-6e39-d38d3b541c3a/displayicon.png"),
        itm("V26 ACT I Coin Buddy",         BD + "9cd37dd1-4a3c-6b6d-5683-4c9a6ec008e6/displayicon.png"),
        itm("Spoonful Buddy",               BD + "469e85db-421d-5d87-43a9-e7995f7e94bb/displayicon.png"),
        itm("Pint-Size Planet Buddy",       BD + "e18d16f4-45fa-3279-fa83-e4970716c58e/displayicon.png"),
        itm("Paracord Buddy",               BD + "1e553d0e-422f-46c6-4378-5299272355c0/displayicon.png"),
    ],
    "cards": [
        itm("Five to Nine Card",              PC + "dc9f1429-4f65-b77d-65a7-5f85dda4687c/smallart.png"),
        itm("Serpent's Celebration Card",     PC + "41244f42-43f5-f795-9be8-d2b9edba458a/smallart.png"),
        itm("Afternoon Asada Card",           PC + "c8b2f5fd-4331-b172-f3b7-c8a26f356a1f/smallart.png"),
        itm("Horse Brings The Luck Card",     PC + "5b338357-4ee4-b112-a050-bcbf542ad9ba/smallart.png"),
        itm("Halloween Bash Card",            PC + "7b75be16-4190-34d5-667c-3589418fc7c5/smallart.png"),
        itm("Tactidance Card",                PC + "42d080df-41c6-4c11-ab17-948cb440bf6c/smallart.png"),
        itm("Roll for Initiative Card",       PC + "03f88215-41f1-d3a2-7983-67b56517eb72/smallart.png"),
        itm("New Recruit Card",               PC + "612cd02d-4294-ee2a-644c-a3ba3ddf8805/smallart.png"),
        itm("Going Ghosting Card",            PC + "4ae57e72-4b7e-a3ab-1ece-1ebfa0504971/smallart.png"),
        itm("Nine to Five Card",              PC + "714965d1-469f-6661-1012-5d8664ca5e4a/smallart.png"),
        itm("Tacti-Ops Card",                 PC + "224e6a53-4463-5694-95b0-2a9dcd2fcd42/smallart.png"),
        itm("Unstoppable // Astra Card",      PC + "1e731b1b-48dd-2dff-1c64-36bfe4bef7bf/smallart.png"),
        itm("Celestia Card",                  PC + "40638788-4b84-b2b4-0581-b6832676a567/smallart.png"),
        itm("Puzzles & Bears Card",           PC + "f6f2be5f-432e-7cfb-8d5e-f8b344c51fb5/smallart.png"),
        itm("Paintbrush Tactics Card",        PC + "213c4c4a-44e6-12a5-6ab2-ae8282e93e57/smallart.png"),
        itm("Venomous Succession Card",       PC + "c27560d1-42e8-aeca-1420-f1a130d11ccb/smallart.png"),
        itm("Bandit Schema Card",             PC + "c06b12b4-4517-5608-3eb9-b1b2d4f57d84/smallart.png"),
        itm("Code Red Card",                  PC + "c89194bd-4710-b54e-8d6c-60be6274fbb2/smallart.png"),
        itm("Dimensional Folding Card",       PC + "e8787c31-4a39-9636-94a5-77b298d26ba7/smallart.png"),
        itm("Tactical Spacewar Card",         PC + "f82ce47d-4d82-92fd-debb-2d8ddd4da097/smallart.png"),
        itm("Dayglo Duo Card",                PC + "1711d20d-4b1c-c64a-14be-d4ae58a457c6/smallart.png"),
        itm("Moon Scout Card",                PC + "d34ee1fb-481d-485f-2f99-2ebc63ec5907/smallart.png"),
        itm("Prismatic Pathways Card",        PC + "0c05d003-48e9-261b-6155-938cb4b19143/smallart.png"),
        itm("The Cost Card",                  PC + "201be320-4a18-cd81-75fa-228dba06d676/smallart.png"),
        itm("Hieroscape Card",                PC + "2d976007-4dce-d01a-8a83-35b7cd1cae52/smallart.png"),
        itm("Corrode Schema Card",            PC + "a9222582-4686-0ab2-2ed4-54942463ec30/smallart.png"),
        itm("Outlaw Schema Card",             PC + "a6a45a8c-4b72-4da4-35c3-80bb63eb9e9a/smallart.png"),
        itm("Striking Distance Card",         PC + "aa521fab-4a02-341c-2a8a-ebaaa8ca1420/smallart.png"),
        itm("Tejo ID Card",                   PC + "990caf11-4397-fa5d-2d3c-3186b036cb07/smallart.png"),
        itm("Pass the Sticks Card",           PC + "eef542d2-4724-bc47-f53f-239f8c9c2623/smallart.png"),
        itm("V Protocol Card",                PC + "0819fbcd-4bd4-c379-5384-52803440f2b2/smallart.png"),
        itm("Old Dogs New Tricks Card",       PC + "57e8abe0-4d09-bfc4-0b50-7da45a3cf17d/smallart.png"),
        itm("Epilogue: Tactical Spacewar Card", PC + "535fe6a7-401e-fca2-20fe-37974d0f5dd5/smallart.png"),
    ],
    "sprays": [
        itm("No Controller Spray",        SP + "6e1cde23-4b53-d043-2005-af8479768ca4/displayicon.png"),
        itm("Boss Bear Spray",             SP + "44e7493c-4199-2987-6464-5e890120c8fa/displayicon.png"),
        itm("TactiForce: Go! Spray",       SP + "c4b5f5e7-453f-039f-1782-cbbb12db7ae7/displayicon.png"),
        itm("Hmph, Not Cool Spray",        SP + "70aed915-41ca-4313-80f9-caa5ae3594de/displayicon.png"),
        itm("A Fruitful New Year Spray",   SP + "74336670-4b54-8ec1-ffa2-668a1ae7c49a/displayicon.png"),
        itm("Cabbage Seekers Spray",       SP + "5fef8250-487e-54d8-4592-1097546d838f/displayicon.png"),
        itm("Hieroscape Spray",            SP + "aeb20e91-4779-3814-0a2d-c18be9e94e09/displayicon.png"),
        itm("V for VALORANT Spray",        SP + "5d88fd45-434d-b0d6-2331-e8b3d47b8395/displayicon.png"),
        itm("Revolving Door Spray",        SP + "f757f62e-4070-1a79-f60f-2192a5963375/displayicon.png"),
        itm("Moon Scout Spray",            SP + "da8c0610-4594-a275-169c-d2b7133fee6f/displayicon.png"),
        itm("Bullet Time Spray",           SP + "c1fbd793-4583-124a-bd38-28843faf6c32/displayicon.png"),
        itm("Scribble Speed Spray",        SP + "0bb83333-4028-0a96-f23f-78a97a895c38/displayicon.png"),
        itm("Mosh O' Lantern Spray",       SP + "45caaf15-481a-b575-6941-b0b7ce833add/displayicon.png"),
        itm("Nap Stack Tower Spray",       SP + "5d2c3e01-4d43-0859-3287-62bcd67fc88d/displayicon.png"),
        itm("Claws Are Out Spray",         SP + "fcbfde2f-4b4d-9ca6-12bf-888db350daeb/displayicon.png"),
        itm("Celestia Spray",              SP + "db889f56-41cc-4620-5ab3-7dad2ed4052c/displayicon.png"),
        itm("I Love This Gun Spray",       SP + "a0a399da-4322-83f0-e734-49a81ab6e820/displayicon.png"),
        itm("Red Fortunes Spray",          SP + "8da459cc-40ce-50d5-d2dd-dfa66503c293/displayicon.png"),
        itm("GLHF Spray",                  SP + "6983ae7c-4cb5-835c-8f62-b7affbaae20e/displayicon.png"),
        itm("It's You and Me Spray",       SP + "fb665ed3-4575-0c99-f228-519b0d42c8d4/displayicon.png"),
        itm("Riptide Ripped Spray",        SP + "914c54df-41dd-8b47-d586-f1942740506d/displayicon.png"),
        itm("Mosh Splat Spray",            SP + "23eb0866-44cc-dfc7-9466-ce98dfb4c163/displayicon.png"),
        itm("BooBat Spray",                SP + "97d13df6-4a27-7eb4-b637-57a4a2bef955/displayicon.png"),
        itm("Acorn Ops Spray",             SP + "7be05688-4141-f625-3990-c3933cdbaebd/displayicon.png"),
        itm("Whoops Spray",                SP + "6cee7e0a-4d08-6213-3ec9-479f0667b4c0/displayicon.png"),
        itm("Ashamed Cat Spray",           SP + "b35bb814-4d5f-3e1e-4976-8ea720c89d3c/displayicon.png"),
    ],
    "flexes": [
        itm("Stellar Dendrite Flex", "https://media.valorant-api.com/flex/d3f8f048-4e9c-939d-7233-67892d8b925f/displayicon.png"),
    ],
    "titles": [
        "Six Seven", "All Gas", "Serpent", "Flaming Steed", "Unc", "Treat", "Tea",
        "Ghosted", "ZZZ", "Performative", "New Year, New Me", "Pookie", "Different",
        "NPC", "Cooked", "Sweaty", "Slay", "From the Grave", "Gnarly", "Recruit",
        "Horsepower", "Aura",
    ],
    "missions": [],
    "expired": False,
    "slug": "qsWQaSIq",
}

users = json.load(open(USERS, encoding="utf-8"))
users = [u for u in users if u.get("slug") != new_user["slug"] and u.get("username") != new_user["username"]]
users.append(new_user)
json.dump(users, open(USERS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("users.json now has", len(users), "accounts:",
      [(u["name"], u["slug"]) for u in users])
print("new account counts -> skins:", len(new_user["skins"]), "buddies:", len(new_user["buddies"]),
      "cards:", len(new_user["cards"]), "sprays:", len(new_user["sprays"]),
      "titles:", len(new_user["titles"]), "ranks:", len(new_user["ranks"]))
print("weapon skin total:", sum(s["price"] for s in new_user["skins"]))
