EXPLORANT — DEPLOY GUIDE  (zero setup, any host)
================================================

WHAT YOU GET
------------
A completely static site. No server, no database, no build step.

  index.html                     the app (login -> dashboard -> accounts -> OPEN ACCOUNT)
  account/O8RBglzK/index.html    PhaNtoM  public page
  account/Twt7kQx2/index.html    twt      public page
  account/qsWQaSIq/index.html    Chaku Wala Jatt  public page
  account/index.html             small directory listing all public links
  generate.py + data/users.json + templates/   (used only to (re)generate — do NOT upload)

YOUR SHAREABLE LINKS (after uploading)
--------------------------------------
  https://explorant.space/account/O8RBglzK/   -> PhaNtoM
  https://explorant.space/account/Twt7kQx2/   -> twt
  https://explorant.space/account/qsWQaSIq/   -> Chaku Wala Jatt
  https://explorant.space/                    -> the app (login)

If you also create a "preview" subdomain pointing at the same files:
  https://preview.explorant.space/account/O8RBglzK/   -> PhaNtoM
  https://preview.explorant.space/account/Twt7kQx2/   -> twt
  https://preview.explorant.space/account/qsWQaSIq/   -> Chaku Wala Jatt

HOW TO DEPLOY — pick ONE host
-----------------------------
1) cPanel / shared hosting (most common for a custom domain)
   - Open File Manager -> public_html (or the folder your domain points to).
   - Upload ONLY:  index.html  and the  account/  folder.
   - Done. Visit https://explorant.space/account/O8RBglzK/

2) Netlify
   - Drag & drop the  site/  folder onto https://app.netlify.com/drop
   - Add your domain in Site settings -> Domain management.

3) Cloudflare Pages
   - Upload the contents of  site/  (index.html + account/) as a new project.

4) GitHub Pages / Vercel / any Apache or Nginx box
   - Copy  index.html  and  account/  to the web root. No config files needed.

SUBDOMAIN  preview.explorant.space
----------------------------------
In your domain's DNS, add a record:  preview  -> same IP/host as explorant.space,
then point that subdomain's document root at the SAME folder (or upload the same
two things again). The URLs above then work under preview.explorant.space.

ADD / EDIT ACCOUNTS
-------------------
Option A (with Python 3):
   1) Edit  data/users.json  — copy an existing account block, change the fields
      (username, password, name, level, skins, buddies, cards, sprays, titles,
      ranks, banner, slug, ...).
   2) Run:  python3 generate.py
   3) Re-upload  index.html  and  account/.

Option B (no Python, Notepad is enough):
   1) Copy an existing folder, e.g.  account/O8RBglzK  ->  account/MyNewCode
   2) Open the new  index.html,  replace the <title> and the line that starts
      with  var __sel = { ... };  with your new account's data (keep the ; ).

NOTES
-----
- The login and Riot-credential screens are a FRONT-END DEMO only: account data
  (including demo passwords) is embedded in the page source. Do not put real
  secrets here.
- Artwork loads live from media.valorant-api.com, so viewers need internet.
- The app always opens on the LOGIN screen (the session is not remembered).

ACCOUNT LOGIN (owner)
---------------------
  vakking22@gmail.com / vakking22@@   -> PhaNtoM (Expired)
  twt / twt123                        -> twt
  qsWQaSIq = "Chaku Wala Jatt"        -> showcase account (no login; open it from
                                          the Accounts grid or its direct link)
