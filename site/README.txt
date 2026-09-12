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

YOUR SHAREABLE LINKS (live on Cloudflare Pages)
-----------------------------------------------
  https://explorant.pages.dev/account/O8RBglzK/   -> PhaNtoM
  https://explorant.pages.dev/account/Twt7kQx2/   -> twt
  https://explorant.pages.dev/account/qsWQaSIq/   -> Chaku Wala Jatt
  https://explorant.pages.dev/                    -> the app (login)
  (same paths work on every custom domain attached to the Pages project)

IMPORTANT — WHAT GETS DEPLOYED
------------------------------
Cloudflare Pages serves the REPO ROOT. The web root is:

  index.html                     the app (login -> dashboard -> accounts)
  account/<slug>/index.html      one public page per account
  account/index.html             small directory listing all public links
  assets/logo.png                app logo
  legacy/vanta-account.html      the old single-account VANTA page (kept only
                                 for reference — not linked anywhere)

To add/edit accounts: edit site/data/users.json, run
  python3 site/generate.py
from the repo root — it writes index.html and account/ straight into the
repo root. Commit + push to main and Cloudflare redeploys automatically.

The login and Riot-credential screens are a FRONT-END DEMO only: account data
is embedded in the page source. Do not put real secrets here.
