EXPLORANT — SITE PACKAGE (v2, fixed layout)
===========================================

WHAT'S INSIDE
-------------
  index.html                  the app (login -> dashboard -> accounts -> OPEN ACCOUNT)
  account/index.html          directory listing of all public account links
  account/O8RBglzK/index.html PhaNtoM          -> share as /account/O8RBglzK/
  account/Twt7kQx2/index.html twt              -> share as /account/Twt7kQx2/
  account/qsWQaSIq/index.html Chaku Wala Jatt  -> share as /account/qsWQaSIq/
  account/z0IukRwx/index.html ln1              -> share as /account/z0IukRwx/
  assets/logo.png             app logo (referenced by index.html — do not delete)

HOW TO DEPLOY (any static host, incl. Cloudflare Pages direct upload)
---------------------------------------------------------------------
Upload EVERYTHING in this folder to your web root (public_html, or the
Pages project root). Do NOT put these files inside a subfolder — that is
what broke the previous deployment (the app ended up only reachable at /site/).

Cloudflare Pages (Git): the repo root of main must look exactly like this.
Cloudflare Pages (Direct upload): drag the FILES inside this folder
(index.html + account/ + assets/), not the containing folder.

NOTES
-----
- Fully static: no server, no database, no build step.
- Artwork loads live from media.valorant-api.com, so viewers need internet.
- The login / Riot-credential screens are a FRONT-END DEMO only — account
  data is embedded in the page source. Never use real credentials.
