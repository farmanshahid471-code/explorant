#!/usr/bin/env python3
"""Build the static account page for slug z0IukRwx (ln1).

Data was cloned from preview.explorant.space/account/z0IukRwx/ and edited
per owner request (2026-09-12):
  ADDED   : VCT 2026 Sigil, Singularity Vandal, Ayakashi Phantom,
            Primordium Vandal, Reaver Operator, Neo Frontier Sheriff,
            VCT26 x SEN Classic, Mystbloom Phantom
  REMOVED : Reaver Karambit, Primordium Spectre, Overdrive Sheriff,
            Gaia's Vengeance Vandal, Gaia's Vengeance Ghost

Weapon-skin value : 16400 - 12250 (removed) + 19920 (added) = 24070
Total Value       : 24070 + 2000 (battlepass)              = 26070
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TMPL = os.path.join(HERE, "site/templates/account.html")
OUT  = os.path.join(HERE, "account/z0IukRwx/index.html")
USERS_PATHS = [os.path.join(HERE, "demo/data/users.json"),
               os.path.join(HERE, "site/data/users.json")]

def WL(u): return "https://media.valorant-api.com/weaponskinlevels/" + u + "/displayicon.png"
def BD(u): return "https://media.valorant-api.com/buddies/" + u + "/displayicon.png"
def PC(u): return "https://media.valorant-api.com/playercards/" + u + "/smallart.png"
def SP(u): return "https://media.valorant-api.com/sprays/" + u + "/displayicon.png"
def FX(u): return "https://media.valorant-api.com/flex/" + u + "/displayicon.png"
def IT(name, tier, price, img): return {"name": name, "tier": tier, "price": price, "img": img}

CT = "03621f52-342b-cf4e-4f86-9350a49c6d04"  # competitivetiers season
def RK(name, n): return {"name": name, "icon": f"https://media.valorant-api.com/competitivetiers/{CT}/{n}/largeicon.png"}

BP_IMG = "https://app.explorant.space/static/default-battlepass.png"
AG_IMG = "https://preview.explorant.space/static/agents/"

# ------------------------------------------------------------------ skins --
SKINS = [
    # -- added (8) --
    IT("VCT 2026 Sigil",       "Exclusive", 5350, WL("fb970da4-4f6a-5cb6-a484-1abf95e6f12d")),
    IT("Kuronami Vandal",      "Exclusive", 2375, WL("636c1f83-44f7-6bc4-0b24-88a1beb66c2d")),
    IT("VCT26 x SEN Classic",  "Exclusive", 2320, WL("d1e82c9f-4f17-ab19-680a-5890365c2241")),
    IT("Singularity Vandal",   "Exclusive", 2175, WL("56c5c2cf-4213-6d98-f5d0-79954573930c")),
    IT("Primordium Vandal",    "Exclusive", 2175, WL("8820f9c1-43d3-55eb-f15a-53abaac6f49e")),
    IT("Neo Frontier Sheriff", "Exclusive", 2175, WL("d9f04b7a-4ca6-1083-3af4-e3810bf15440")),
    IT("Mystbloom Phantom",    "Exclusive", 2175, WL("284aea8b-43b6-e5fe-686f-00b58ec2b17a")),
    IT("Recon Phantom",        "Premium",   1775, WL("5be0b43b-4e66-ab8a-91d9-be9137e2e1c2")),
    IT("Ayakashi Phantom",     "Exclusive", 1775, WL("27acfa4d-4c6e-5f16-496e-f7baad3e00e0")),
    IT("Reaver Operator",      "Premium",   1775, WL("7bfab387-4e97-d815-4488-c491e3a5520c")),
    # -- kept, unpriced (original order) --
    IT("Heartseeker Phantom",    "Select", 0, WL("5ce06154-47dc-3a1d-41a4-34a32f5c111c")),
    IT("Dragon Gate Ares",       "Select", 0, WL("ed3fcae2-403a-2fa7-4c9b-889b4d70c40d")),
    IT("Soulburst Spectre",      "Select", 0, WL("b4de462b-45f2-61ea-c3e3-f49e35b5bd7d")),
    IT("Heartbreaker Operator",  "Select", 0, WL("369d25dc-46ab-dbdb-7f90-d197508acaf6")),
    IT("Heartseeker Shorty",     "Select", 0, WL("836d69fe-4a12-e316-5754-5a8fb3992474")),
    IT("Heartbreaker Sheriff",   "Select", 0, WL("c162dc88-4a08-79bd-664a-e38ca7d7bab0")),
    IT("Soulburst Bandit",       "Select", 0, WL("d8606d62-4a88-39d6-4e65-3993b0f3f9b2")),
    IT("Heartbreaker Odin",      "Select", 0, WL("5665d2db-49f3-4b39-eebf-62a5af424308")),
    IT("Paceline Guardian",      "Deluxe", 0, WL("26d6aaa9-4b61-763d-bf35-f88773d4c86b")),
    IT("Paceline Stinger",       "Deluxe", 0, WL("77acb671-4260-d01b-a5eb-bbb17b52d7fd")),
    IT("Heartbreaker Bulldog",   "Select", 0, WL("4504f23a-4d92-0587-485e-35951402eeda")),
    IT("Keys to Elysium Sheriff","Deluxe", 0, WL("a7547ee3-4143-a99c-d23c-11961c4336bd")),
    IT("Heartseeker Guardian",   "Select", 0, WL("60ad6389-4c4e-f6d0-7fae-8c8234fe7418")),
    IT("Montage Frenzy",         "Deluxe", 0, WL("19850f93-4728-f4ef-1bed-ed88e933d60d")),
    IT("Soulburst Bulldog",      "Select", 0, WL("5f0ecd25-464c-f8d1-5e72-e0922da5b311")),
    IT("Dragon Gate Shorty",     "Select", 0, WL("9bf87c46-462c-ce18-ccd4-c7be8c27124f")),
    IT("Dragon Gate Judge",      "Select", 0, WL("9a224aac-4541-4eeb-68e9-adb3f8da6fbc")),
    IT("Paceline Vandal",        "Deluxe", 0, WL("776d2b8c-4ea4-8357-c3f5-abb2a9cf3898")),
    IT("Paceline's Edge",        "Exclusive", 0, WL("9ce8ad00-477c-4103-f1b9-1a9b21d07899")),
    IT("Heartstopper Ghost",     "Deluxe", 0, WL("13f02678-40bc-c4ba-8636-9082733e8dc0")),
    IT("Paceline Frenzy",        "Deluxe", 0, WL("5a993777-400e-0d61-e351-eb98652ac9d3")),
    IT("Heartseeker Outlaw",     "Select", 0, WL("9f796ae3-491d-28dc-1beb-9bb81a5e231a")),
    IT("Heartseeker Stinger",    "Select", 0, WL("e9ed9118-4cb0-3548-580a-c39c0d11a8d9")),
    IT("Soulburst Outlaw",       "Select", 0, WL("fc793b9e-4644-0b7f-8240-47818532bb3d")),
    IT("Heartstopper Vandal",    "Deluxe", 0, WL("d33f3dff-4631-d550-4745-458ba2e2900e")),
    IT("Dragon Gate Phantom",    "Select", 0, WL("e818895a-41fe-9c4d-2fa9-6598efd21275")),
    IT("Heart Splitter",         "Exclusive", 0, WL("5da259d7-4714-2b0d-7663-3b89310dab62")),
]

BUDDIES = [IT(n, "", 0, BD(u)) for n, u in [
    ("V25 ACT VI Coin Buddy",          "d27bee0c-47bd-db44-4a06-0e9be602a9e8"),
    ("Happy Petal Buddy",              "3bff23db-431e-8ef3-476f-39b5d90c89b2"),
    ("V25A6: Gold Buddy",              "78c4cd56-43ee-96c5-06f8-eeb81f30181d"),
    ("Student TactiBear Buddy",        "542bbefc-4f38-02f8-2a2c-42bd4d4170f2"),
    ("Nest Egg Buddy",                 "89ac98ec-495d-680b-22cb-d3afe04eae6e"),
    ("Heartbreaker Buddy",             "1bf92981-42da-5148-6be2-bfbddf7a9818"),
    ("Shock & Roll Buddy",             "f95bee22-4015-efde-9349-4bb455c1b702"),
    ("Fresh Frags Buddy",              "e54d445d-4c1b-2c90-35fa-61be5770a5b9"),
    ("V26 ACT I Coin Buddy",           "9cd37dd1-4a3c-6b6d-5683-4c9a6ec008e6"),
    ("Ult Bias: Jett Buddy",           "71a62d6c-4515-044d-0c86-47af6f3d3c8f"),
    ("Happy Petal Buddy",              "3bff23db-431e-8ef3-476f-39b5d90c89b2"),
    ("Soulburst Buddy",                "7a22dad5-49f3-7404-744e-1590aa49dff8"),
    ("V26A3: Diamond Buddy",           "7f87473c-4e73-ff52-7cd8-58a4085f630a"),
    ("Super Saver Buddy",              "c39e4abb-47bd-3d9f-7f7a-a8a87213672f"),
    ("V25 ACT V Coin Buddy",           "d35dda28-4912-24af-3c72-b4adf236b537"),
    ("Keep it Safer Buddy",            "c14745d0-4958-26d9-60e6-7c863080fef1"),
    ("Fresh Frags Buddy",              "e54d445d-4c1b-2c90-35fa-61be5770a5b9"),
    ("Ult Bias: Jett Buddy",           "71a62d6c-4515-044d-0c86-47af6f3d3c8f"),
    ("Binding Thread Buddy",           "f74a8f8a-44a6-583f-d517-21b7d6a35d4d"),
    ("Fa Buddy",                       "fee36e9f-4136-4d78-9ea4-fd8f89fa040a"),
    ("Strawberry Lippie Buddy",        "228bcacd-49d6-66a2-746a-8b8c1ae68669"),
    ("Duck Chillin' Buddy",            "ab361eac-4cc7-c896-b3ae-0e8a17a97e14"),
    ("Ult Bias: Yoru Buddy",           "2fced8c3-40d1-997a-9b4e-39a15db65ed1"),
    ("V26 ACT I Coin Buddy",           "9cd37dd1-4a3c-6b6d-5683-4c9a6ec008e6"),
    ("Strawberry Lippie Buddy",        "228bcacd-49d6-66a2-746a-8b8c1ae68669"),
    ("Lethal Dose Buddy",              "84693baf-4a2f-8f25-7091-f3868bc430f8"),
    ("Epilogue: 5 Years: Beads Buddy", "0854b92d-4b95-7bbf-c3c0-4986c84afdc0"),
    ("Epilogue: Protocol Dummy Buddy", "acfd6c31-4786-6059-b93a-d49a8c23e2f6"),
    ("Student TactiBear Buddy",        "542bbefc-4f38-02f8-2a2c-42bd4d4170f2"),
    ("V25 ACT V Coin Buddy",           "d35dda28-4912-24af-3c72-b4adf236b537"),
    ("Paceline Buddy",                 "e5b58dea-4c01-58af-c67e-b48a585d2d18"),
    ("H2-Oh! Buddy",                   "21180071-452a-2c30-a041-07923e53933a"),
    ("Epilogue: Night Regent Buddy",   "66118783-462e-165c-fff7-768bb9a4d8cf"),
    ("V26 ACT II Coin Buddy",          "5dcc7d9e-4ef4-2189-698d-539e6257ea9e"),
    ("V26 ACT IV Coin Buddy",          "5a2e9133-4625-8197-0285-63b9c5ce9466"),
    ("V26 ACT IV Coin Buddy",          "5a2e9133-4625-8197-0285-63b9c5ce9466"),
    ("Boom-Bola Buddy",                "21dea727-4b7a-a6e5-b9b5-af8a17a1ba89"),
    ("Ult Bias: Iso Buddy",            "f609e15e-4cf4-af19-7488-b88886298750"),
    ("5 Years: Beads Buddy",           "f4599250-454f-b027-282b-b0b5e972c6db"),
    ("Ult Bias: Yoru Buddy",           "2fced8c3-40d1-997a-9b4e-39a15db65ed1"),
    ("5 Years: Beads Buddy",           "f4599250-454f-b027-282b-b0b5e972c6db"),
    ("Epilogue: Super Saver Buddy",    "8fd7deb8-4696-6452-aa4d-7cb35efacd69"),
    ("VALORANT Coin Buddy",            "ac72bb9a-4368-8502-5dac-698d72021c81"),
    ("V26 ACT II Coin Buddy",          "5dcc7d9e-4ef4-2189-698d-539e6257ea9e"),
    ("Dragon Gate Buddy",              "3d86f44a-4c85-dd03-4429-31b6409f3300"),
    ("Epilogue: Super Saver Buddy",    "8fd7deb8-4696-6452-aa4d-7cb35efacd69"),
    ("Fa Buddy",                       "fee36e9f-4136-4d78-9ea4-fd8f89fa040a"),
    ("Last Light Buddy",               "da5e2770-4b11-6c60-b468-979d0942b386"),
    ("V25A6: Gold Buddy",              "78c4cd56-43ee-96c5-06f8-eeb81f30181d"),
    ("Lethal Dose Buddy",              "84693baf-4a2f-8f25-7091-f3868bc430f8"),
    ("Boom-Bola Buddy",                "21dea727-4b7a-a6e5-b9b5-af8a17a1ba89"),
    ("V26 ACT III Coin Buddy",         "996795a4-408a-0e71-2e23-5ea4aeecf76b"),
    ("Super Saver Buddy",              "c39e4abb-47bd-3d9f-7f7a-a8a87213672f"),
    ("V26 ACT III Coin Buddy",         "996795a4-408a-0e71-2e23-5ea4aeecf76b"),
    ("Heartbreaker Buddy",             "1bf92981-42da-5148-6be2-bfbddf7a9818"),
    ("Dragon Gate Buddy",              "3d86f44a-4c85-dd03-4429-31b6409f3300"),
    ("Heartstopper Buddy",             "bc4ed542-484d-1766-84df-46948a390bec"),
    ("Ult Bias: Iso Buddy",            "f609e15e-4cf4-af19-7488-b88886298750"),
    ("V25 ACT VI Coin Buddy",          "d27bee0c-47bd-db44-4a06-0e9be602a9e8"),
    ("Binding Thread Buddy",           "f74a8f8a-44a6-583f-d517-21b7d6a35d4d"),
    ("Epilogue: Night Regent Buddy",   "66118783-462e-165c-fff7-768bb9a4d8cf"),
    ("Paceline Buddy",                 "e5b58dea-4c01-58af-c67e-b48a585d2d18"),
    ("Heartseeker Buddy",              "a53b80ff-4f51-d8a2-89a6-daa8f1122704"),
    ("Shock & Roll Buddy",             "f95bee22-4015-efde-9349-4bb455c1b702"),
    ("Duck Chillin' Buddy",            "ab361eac-4cc7-c896-b3ae-0e8a17a97e14"),
    ("Orange Juice Dreams Buddy",      "814acc56-4cc0-f896-7751-9494b27f2b7c"),
    ("Epilogue: 5 Years: Beads Buddy", "0854b92d-4b95-7bbf-c3c0-4986c84afdc0"),
    ("Epilogue: Protocol Dummy Buddy", "acfd6c31-4786-6059-b93a-d49a8c23e2f6"),
    ("Last Light Buddy",               "da5e2770-4b11-6c60-b468-979d0942b386"),
    ("V26A3: Diamond Buddy",           "7f87473c-4e73-ff52-7cd8-58a4085f630a"),
    ("H2-Oh! Buddy",                   "21180071-452a-2c30-a041-07923e53933a"),
    ("Orange Juice Dreams Buddy",      "814acc56-4cc0-f896-7751-9494b27f2b7c"),
    ("Heartstopper Buddy",             "bc4ed542-484d-1766-84df-46948a390bec"),
    ("Nest Egg Buddy",                 "89ac98ec-495d-680b-22cb-d3afe04eae6e"),
    ("Heartseeker Buddy",              "a53b80ff-4f51-d8a2-89a6-daa8f1122704"),
    ("Soulburst Buddy",                "7a22dad5-49f3-7404-744e-1590aa49dff8"),
]]

CARDS = [IT(n, "", 0, PC(u)) for n, u in [
    ("5 Years: Ade On Keys Card",       "aca81da3-437e-d9a0-7b6d-b89c0f936daf"),
    ("Horse Brings The Luck Card",      "5b338357-4ee4-b112-a050-bcbf542ad9ba"),
    ("Soulburst Card",                  "a94aac35-403e-d66d-9cf3-aab38f77d9a4"),
    ("V25: Prelude To Paris Card",      "d2d3caf9-499f-2ac8-9722-54961c3bcbf5"),
    ("Code Red Card",                   "c89194bd-4710-b54e-8d6c-60be6274fbb2"),
    ("5 Years: Redemption Card",        "26d403fe-4795-8c63-b6c6-119cd9f0c4da"),
    ("Playzilla Tactibunny Card",       "a78feb94-4e1f-e845-c253-c182d92db9ef"),
    ("Triple Threat Card",              "4f98df89-4d11-e0d8-f7d3-6fa3096b38db"),
    ("Heartbreaker Card",               "3eebac1c-4307-7e8f-0e90-a292749237c5"),
    ("Odin Magazine Card",              "2295a71b-4a6e-2b5b-6c22-539e376f6fa2"),
    ("The Cost Card",                   "201be320-4a18-cd81-75fa-228dba06d676"),
    ("5 Years: Why We Fight Card",      "ea5af728-4df1-b1a4-e73e-21b6235be71f"),
    ("Corrode Schema Card",             "a9222582-4686-0ab2-2ed4-54942463ec30"),
    ("Quack n' Loaded Card",            "cd3bab1a-412a-807b-bb5c-a48be2fea2a1"),
    ("Dragon Gate Card",                "0730dc82-4e93-d339-538e-498891efdb05"),
    ("5 Years: Seize The Play Card",    "edfb9497-48ca-c3d9-cb0a-109cdedf533c"),
    ("Baited Card",                     "dc22fa1e-4170-c594-aaa8-73928a9ca81e"),
    ("Sidekicks Card",                  "3e5cd6d5-4a89-23e9-fcaa-2189943a363c"),
    ("Veto ID Card",                    "effbfb4e-471a-2f6b-8ec1-2c8a29b579f9"),
    ("Epilogue: Fearmonger Card",       "4b422609-484a-ea0f-5a97-7d9695f68a4a"),
    ("V Protocol Card",                 "0819fbcd-4bd4-c379-5384-52803440f2b2"),
    ("Epilogue: Bomb Buddy Card",       "ad81a15f-4725-b75f-0c8c-519aa97ed3b6"),
    ("Boomerproof Card",                "c06e6a9b-4ba2-bbfd-b150-0c8a2a9dbc1e"),
    ("Puzzles & Bears Card",            "f6f2be5f-432e-7cfb-8d5e-f8b344c51fb5"),
    ("Miks ID Card",                    "917615cd-4164-f3e7-c4ec-4f9f6b6b1926"),
    ("Run It Back Card",                "d6e79ba5-4a68-036c-d121-5bb893eafa47"),
    ("Hitlist Card",                    "9c38c6c2-4228-a08c-4d3c-c0a639bd7ca4"),
    ("Out for Blood Card",              "4d0d96d0-4c8a-dd01-2f69-4eaf5c9dc5d7"),
    ("Venomous Succession Card",        "c27560d1-42e8-aeca-1420-f1a130d11ccb"),
    ("Tactidance Card",                 "42d080df-41c6-4c11-ab17-948cb440bf6c"),
    ("Epilogue: Pop Pawstars Card",     "e445f841-4a08-9c25-b88b-659327c8d037"),
    ("Tacti-Ops Card",                  "224e6a53-4463-5694-95b0-2a9dcd2fcd42"),
    ("Unstoppable // Omen Card",        "eba5be7e-4ec7-753b-8678-fa88da1e46ab"),
    ("New Recruit Card",                "612cd02d-4294-ee2a-644c-a3ba3ddf8805"),
    ("Bomb Buddy Card",                 "575e14fc-4c7d-2d4b-23b9-5885f5292591"),
    ("Paceline Card",                   "61ec0ea0-431e-e015-9ec7-24809989302a"),
    ("Flick of the Wrist Card",         "dac0eb01-4286-7a91-b29d-dfb0ab5751bf"),
    ("Amplify Card",                    "8e4c97ca-4364-a7fc-9d2d-92b787499d05"),
    ("Bandit Schema Card",              "c06b12b4-4517-5608-3eb9-b1b2d4f57d84"),
    ("Perfect View Card",               "e98546c6-49a2-d74f-6a5a-8286d34a1b03"),
    ("Paintbrush Tactics Card",         "213c4c4a-44e6-12a5-6ab2-ae8282e93e57"),
    ("Heartseeker Card",                "b3339535-486e-df47-8fed-788c1b2854ad"),
    ("Heartstopper Card",               "1bb056ab-4064-e550-9a04-58b963eaa518"),
    ("Dance It All Away Card",          "d32e58b1-4191-7315-ad4a-9da58b3f23dd"),
    ("Fur of the Fallen Card",          "3234d610-4c98-0b5c-a106-e090453af8d8"),
    ("Pop Pawstars Card",               "210a6c25-4c3a-7a60-27ed-0b9c26d0780f"),
    ("Into The Pit Card",               "0e435790-4300-e6a1-85df-09ade8c188ab"),
    ("Epilogue: Checkmate Protocol Card","62ec8878-45d9-aefe-ac50-ba8e3d8c2a0f"),
    ("5 Years: Saltswept Card",         "065e67f4-4b16-2d5b-49e8-72b53d73e9d4"),
    ("Cat and Mouse Card",              "c5d4cd0b-49fa-0b9c-55c7-9b828f83413f"),
    ("For Retribution Card",            "33f3c143-4da0-b595-5f70-faa2ab7eba3e"),
]]

SPRAYS = [IT(n, "", 0, SP(u)) for n, u in [
    ("Roger Duck Spray",              "13f23a75-4af3-3d30-fae5-e1a08498056c"),
    ("Beware of Dog Spray",           "e27b7950-4a86-404f-7ec5-b7918c386659"),
    ("TactiForce: Go! Spray",         "c4b5f5e7-453f-039f-1782-cbbb12db7ae7"),
    ("Heartseeker Spray",             "253b5e22-46af-6676-0390-df9a0562826c"),
    ("Acorn Ops Spray",               "7be05688-4141-f625-3990-c3933cdbaebd"),
    ("Detonation Dab Spray",          "77c1b2ea-4295-9178-3102-2c95a432a650"),
    ("Angry Ade Spray",               "ab978a9b-4467-f164-9375-3fb080ff3beb"),
    ("Red Fortunes Spray",            "8da459cc-40ce-50d5-d2dd-dfa66503c293"),
    ("Arctic Snare Spray",            "a3fa83de-4f93-a662-b43a-cdab057f95e0"),
    ("Brimstone Geometry Spray",      "3ef41afd-4e90-835a-103e-59a4333de7d3"),
    ("BooBat Spray",                  "97d13df6-4a27-7eb4-b637-57a4a2bef955"),
    ("Scribble Lightspeed Spray",     "7108a8ea-4a41-2e59-b8ad-6a85c8bf1059"),
    ("Heartstopper Spray",            "b411cd90-43aa-dc78-dc0b-49a1f548e28c"),
    ("Heartbreaker Spray",            "35a4f73d-4308-a3b4-a05a-e2a53b2d2721"),
    ("Vamos Spray",                   "adb608c3-4139-6b0c-c9f3-4090d79e06b2"),
    ("Tech-nically Speaking Spray",   "ec7df7d1-4931-da87-e2b5-a4947cf901b0"),
    ("Paceline Spray",                "a601870c-4f4b-4db9-45ac-198d3573f2b4"),
    ("Cans On Spray",                 "fe86a4c5-4e92-324b-4c0d-a7a837d0d548"),
    ("Cosmic Eyes Spray",             "7d7b77af-4f3f-f3b0-afbc-8db3974ad592"),
    ("Woke Up Thinking Lineups Spray","f165025c-4113-9b61-4465-ed956e4533e2"),
    ("Barrier Boost Spray",           "4ecfa47b-409f-c74c-3c3b-9ea6de3552b6"),
    ("On Your Feet Spray",            "cad8fddd-4297-cde3-8130-77b1a2731a27"),
    ("Storm Surge Spray",             "8ade5e91-4a18-db7a-9bda-c2a7c37f3ada"),
    ("Boss Bear Spray",               "44e7493c-4199-2987-6464-5e890120c8fa"),
    ("No Zipline Spray",              "8b9ca36a-4a26-d760-5eca-91a4bed2a065"),
    ("Rage Spray",                    "5b5fc918-4d57-9fa9-1a5d-1b84c43a121e"),
    ("Polish and Punish Spray",       "470f6ca9-4011-8ad3-df95-57b3cdeb613a"),
    ("Bump It Spray",                 "7fd664a6-4082-1877-3516-489aa0b0bdae"),
    ("Hot Seat Spray",                "7e85d0ab-4cc5-d869-5485-798aae7e8656"),
    ("Riptide Ripped Spray",          "914c54df-41dd-8b47-d586-f1942740506d"),
    ("GLHF Spray",                    "6983ae7c-4cb5-835c-8f62-b7affbaae20e"),
    ("Soulburst Spray",               "807350d7-47ec-e85f-bb69-f8b98d4c376d"),
    ("Tacti Tears Spray",             "3e808bd1-48b3-0fa3-6ae1-60a6c6cf5008"),
    ("Rush Zone Spray",               "8acf5901-49e2-beaa-cbaa-a3a335faad73"),
    ("Five and Flawless Spray",       "a44495aa-4062-8dc9-dc4f-ada69c28a597"),
    ("Agent of Chaos Spray",          "f3e98f0b-4d3b-aaed-498e-da942e81bcc0"),
    ("Agent On Route Spray",          "66b8c52b-4701-c231-835b-5fb781df3fa0"),
    ("Wingman Solo Spray",            "80afed10-4eeb-6298-32c3-49ac1f2fc9a7"),
    ("V for VALORANT Spray",          "5d88fd45-434d-b0d6-2331-e8b3d47b8395"),
    ("Dragon Gate Spray",             "0712b6de-47e1-d4b8-3ece-f99d3966e515"),
    ("Abilities Don't Kill Spray",    "7e2ba2e8-4597-060a-b41e-81acedca414e"),
    ("Radiant Riffs Spray",           "ecaa869c-4982-51bf-c0b4-54a287120ec5"),
    ("Headbang Havoc Spray",          "de3ffd7b-4908-47aa-89f1-b39d90272313"),
    ("Percussion Protocol Spray",     "d0344ba6-4765-1bd3-920e-88b411571393"),
]]

FLEXES = [IT(n, "", 0, FX(u)) for n, u in [
    ("PB&J Flex",        "aa283b9a-44dd-7c05-7017-28889664a848"),
    ("Dragon Gate Flex", "833953fa-439e-b808-de05-7c895f7cd117"),
]]

TITLES = ["Aura Farming", "Recruit", "Red Flag", "Unserious", "Big Guy", "Flaming Steed",
          "GOOOOALLLL!!!", "Performative", "Squad", "Cachando todo", "Gnarly", "Green Flag",
          "Six Seven", "Bonjour", "Bossman", "Overheating", "Harmony", "Tea", "Sweaty",
          "In Sync", "All Gas", "From the Grave", "Last Player Standing", "IGL",
          "Horsepower", "Superstar", "Unc"]

BATTLEPASSES = [IT("Season 2026 // Act II", "", 0, BP_IMG),
                IT("Season 2025 // Act VI", "", 0, BP_IMG)]

AGENTS = [{"name": n, "tier": "", "price": 0, "img": AG_IMG + u + ".png"} for n, u in [
    ("Skye Contract",     "e7e7c5e1-4e76-22f8-f423-078b33758464"),
    ("Killjoy Contract",  "9443cbd4-da4d-4395-8152-26a5b269f339"),
    ("Harbor Contract",   "5d627650-48ac-5710-5e49-78a41dc28b7b"),
    ("Clove Gear",        "59019709-44fe-f723-da01-848df9ac0413"),
    ("Reyna Contract",    "4c9b0fcf-57cd-4e84-ae5a-ce89e396242f"),
    ("Miks Gear",         "3364d1bb-4172-c0a2-0706-c795620652b2"),
    ("Veto Gear",         "079c77a8-4ee8-4b8c-2983-d8bfe08ec3f0"),
    ("Breach Contract",   "bfb8160e-eee0-46b1-a069-16f93adc7328"),
    ("Astra Contract",    "1d40b4b9-4d86-50b7-9f79-3d939e09c661"),
    ("KAY/O Contract",    "9454d42a-471f-27b9-325c-319a355c34ee"),
    ("Deadlock Gear",     "78f97f6c-4f19-bfcf-e466-a4840c7c9057"),
    ("Tejo Gear",         "d2a737e1-4a5e-07a9-b26d-dab19d92fb2c"),
    ("Chamber Contract",  "ebfd35c7-4d47-11f6-63f3-0398f055d8ab"),
    ("Vyse Gear",         "72316ecc-4e88-5b55-aed4-529a76eb75f3"),
    ("Iso Gear",          "26c6e81f-4d62-e55e-24e7-3d8fa37e3b97"),
    ("Fade Contract",     "7ae5ad85-400b-beba-989d-42924ccf39be"),
    ("Cypher Contract",   "2195e89f-20ad-4e37-b46c-cf46a6715dfd"),
    ("Omen Contract",     "eb35d061-4eed-4d22-81a3-1491ec892429"),
    ("Gekko Contract",    "cae6ab4a-4b4a-69a0-3c7a-48b17e313f52"),
    ("Raze Contract",     "60f9f1f0-2bb7-47f9-85b7-b873a5a1123b"),
    ("Viper Contract",    "f94fc320-a71f-47e3-b062-6798d14f17d6"),
]]

WEAPON_TOTAL = sum(s["price"] for s in SKINS)          # 24070
BP_TOTAL     = 2000
AGENT_TOTAL  = 2000
TOTAL_VALUE  = WEAPON_TOTAL + BP_TOTAL                  # 26070 (matches live formula)

USER = {
    "username": "ln1", "password": "", "name": "ln1", "title": "Six Seven",
    "region": "eu", "country": "tur", "level": 88, "levelNow": 2281, "levelMax": 5000,
    "totalValue": TOTAL_VALUE,
    "banner": "https://media.valorant-api.com/playercards/c5d4cd0b-49fa-0b9c-55c7-9b828f83413f/wideart.png",
    "ranks": [
        RK("V26 - ACT IV", 15), RK("V26 - ACT III", 19), RK("V26 - ACT II", 18),
        RK("V26 - ACT I", 14),  RK("V25 - ACT VI", 14),
    ],
    "skins": SKINS, "buddies": BUDDIES, "cards": CARDS, "sprays": SPRAYS,
    "flexes": FLEXES, "titles": TITLES,
    "missions": [{"name": "Purchase Items from the Armory", "percent": 0.5},
                 {"name": "Play Rounds Or Stages",          "percent": 0},
                 {"name": "Play A Match",                   "percent": 0}],
    "store": [], "accessory": [], "daily": {"vp": 0, "rp": 0},
    "battlepasses": BATTLEPASSES, "bpTotal": BP_TOTAL,
    "agents": AGENTS, "agentTotal": AGENT_TOTAL,
    "nextFirstWin": "Available", "nextWeekly": "Tue 11-Aug-2026 8:15 AM",
    "expired": False, "slug": "z0IukRwx",
}

# ------------------------------------------------------------- build page --
html = open(TMPL, encoding="utf-8").read()

# 1. title
html = re.sub(r"<title>.*?</title>", "<title>ln1 - Explorant</title>", html, count=1, flags=re.S)

# 2. BP_TOTAL must be reassignable from the hydration block
assert "const BP_TOTAL = 0;" in html
html = html.replace("const BP_TOTAL = 0;", "var BP_TOTAL = 0;")

# 3. per-account weekly reset date
html = re.sub(r'const NEXT_WEEKLY\s*=\s*"[^"]*";',
              f'const NEXT_WEEKLY    = "{USER["nextWeekly"]}";', html, count=1)

# 4. Agents header value slot
html = html.replace('<div class="title-card"><div class="title-text">Agents</div><div class="title-cur"></div></div>',
                    '<div class="title-card"><div class="title-text">Agents</div><div class="title-cur" id="agentValue"></div></div>')

# 5. per-section empty-state text support
html = html.replace('el.innerHTML=`<div class="empty" style="grid-column:1/-1;">No Items to Show</div>`;',
                    'el.innerHTML=`<div class="empty" style="grid-column:1/-1;">${el.getAttribute("data-empty")||"No Items to Show"}</div>`;')
html = html.replace('<div class="list-grid" id="dailyStore"></div>',
                    '<div class="list-grid" id="dailyStore" data-empty="Store Skins Not Fetched Yet. Please Ask Owner to Refresh Account"></div>')
html = html.replace('<div class="list-grid" id="accessoryStore"></div>',
                    '<div class="list-grid" id="accessoryStore" data-empty="Accessory Skins Not Fetched Yet. Please Ask Owner to Refresh Account"></div>')

# 6. extend hydration: battlepasses / agents / store / currency headers
OLD_HYD = '    __fill(FLEXES,  __sel.flexes, "skin","#c5c5ff","rifle");\n  }catch(e){}'
NEW_HYD = '''    __fill(FLEXES,  __sel.flexes, "skin","#c5c5ff","rifle");
    if(__sel.agents && __sel.agents.length){ __fill(AGENTS, __sel.agents, "agent","#c5c5ff","rifle"); }
    if(__sel.battlepasses && __sel.battlepasses.length){ __fill(BATTLEPASSES, __sel.battlepasses, "skin","#c5c5ff","rifle"); }
    if(__sel.store && __sel.store.length){ __fill(STORE, __sel.store, "skin","#c5c5ff","rifle"); }
    if(__sel.accessory && __sel.accessory.length){ __fill(ACCESSORY, __sel.accessory, "skin","#c5c5ff","rifle"); }
    if(typeof __sel.bpTotal==="number"){ BP_TOTAL=__sel.bpTotal; }
    var __VP="https://media.valorant-api.com/currencies/85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741/displayicon.png";
    var __VPI='<img src="'+__VP+'" alt="vp" onerror="this.style.display=\\'none\\'"/>';
    if(__sel.daily){ var __dc=document.getElementById("dailyCur"); if(__dc) __dc.innerHTML=__VPI+'<span class="cur">'+(__sel.daily.vp||0)+'</span>&nbsp;&nbsp;<img src="https://media.valorant-api.com/currencies/e59aa87c-4cbf-517a-5983-6e81511be9b7/displayicon.png" alt="rp" onerror="this.style.display=\\'none\\'"/><span class="cur">'+(__sel.daily.rp||0)+'</span>'; }
    if(typeof __sel.agentTotal==="number"){ var __ag=document.getElementById("agentValue"); if(__ag) __ag.innerHTML='<span class="cur">Total Value: '+__sel.agentTotal+'</span>'+__VPI; }
  }catch(e){}'''
assert OLD_HYD in html
html = html.replace(OLD_HYD, NEW_HYD)

# 7. inject the account payload
sel_line = 'var __sel = JSON.parse(localStorage.getItem("explorant_view_account")||"null");'
assert sel_line in html
payload = json.dumps(USER, ensure_ascii=False, separators=(",", ": ")).replace("</", "<\\/")
html = html.replace(sel_line, "var __sel = " + payload + ";")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)

# --------------------------------------------------- update users.json x2 --
for path in USERS_PATHS:
    if not os.path.exists(path):
        continue
    users = json.load(open(path, encoding="utf-8"))
    users = [u for u in users if u.get("slug") != "z0IukRwx" and u.get("username") != "ln1"]
    users.append(USER)
    json.dump(users, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{path}: {len(users)} accounts")

# ------------------------------------------------ update account directory --
DIR_ = os.path.join(HERE, "account/index.html")
d = open(DIR_, encoding="utf-8").read()
if 'href="z0IukRwx/"' not in d:
    li = '\n<li><a href="z0IukRwx/">ln1</a><span class="u">/account/z0IukRwx/</span></li>'
    d = d.replace("</li></ul>", "</li>" + li + "</ul>")
    open(DIR_, "w", encoding="utf-8").write(d)
    print("account/index.html updated")

print(f"built {OUT}")
print(f"skins: {len(SKINS)} | weapon total: {WEAPON_TOTAL} | total value: {TOTAL_VALUE}")
print("added:", [s["name"] for s in SKINS[:10] if s["price"] > 0][:8])
for gone in ["Reaver Karambit", "Primordium Spectre", "Overdrive Sheriff",
             "Gaia's Vengeance Vandal", "Gaia's Vengeance Ghost"]:
    assert gone not in html, f"{gone} still present!"
print("removal check: all 5 gone ✔")
