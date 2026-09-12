#!/usr/bin/env python3
"""
Explorant preview-site generator
================================
Reads  data/users.json  +  templates/  and produces a fully static site
that works on ANY web host (no server config needed):

    index.html                      the app (login -> dashboard -> accounts)
    account/<slug>/index.html       one public page per account  (shareable link)
    account/index.html              a small directory of all public links

How to use
----------
1. Edit  data/users.json  (add / change accounts).
2. Run:  python3 generate.py
3. Done — output goes straight to the REPO ROOT, which is what
   Cloudflare Pages serves (index.html + account/ + assets/).
   The only things NOT deployed are these generator sources in site/
   (generate.py, templates/, data/).

Add a new account WITHOUT Python (works in Notepad too):
  - copy an existing  account/<slug>/  folder, rename it to a new 8-char code,
  - open its  index.html  and replace the JSON in the line that starts with
    `var __sel = {`  (keep the trailing  `;`), and the <title> tag.
"""
import json, os, re, sys

HERE    = os.path.dirname(os.path.abspath(__file__))
DATA    = os.path.join(HERE, "data", "users.json")
TPL_APP = os.path.join(HERE, "templates", "standalone.html")
TPL_ACC = os.path.join(HERE, "templates", "account.html")
OUT     = os.path.dirname(HERE)   # repo root = web root served by Cloudflare Pages

def esc_js(s):
    # never allow a "</script>" sequence to break out of the inline script
    return str(s).replace("</", "<\\/")

def bake_account(template, user):
    nickname = (user.get("name") or user.get("username") or "Account")
    page = template

    # 1) page <title>
    page = re.sub(r"<title>.*?</title>",
                  "<title>%s &mdash; Explorant</title>" % nickname,
                  page, count=1, flags=re.S)

    # 2) hide the editor-facing hint box
    page = re.sub(r'document\.getElementById\("howto"\)\.innerHTML=`.*?`;',
                  'document.getElementById("howto").style.display="none";',
                  page, count=1, flags=re.S)

    # 3) bake the account data in place of the localStorage read
    blob = json.dumps(user, ensure_ascii=False)
    old = 'var __sel = JSON.parse(localStorage.getItem("explorant_view_account")||"null");'
    new = 'var __sel = ' + esc_js(blob) + ';'
    assert old in page, "hydration read not found in template"
    page = page.replace(old, new, 1)

    return page

def listing_page(users):
    items = []
    for u in users:
        name = u.get("name") or u.get("username")
        slug = u.get("slug")
        if not slug:
            continue
        items.append(
            '<li><a href="%s/">%s</a>'
            '<span class="u">/account/%s/</span></li>' % (slug, name, slug)
        )
    body = "\n".join(items) if items else "<li>No accounts yet</li>"
    return """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Accounts &mdash; Explorant</title>
<style>
 body{margin:0;background:#222020;color:#8f8f8f;font-family:Segoe UI,Roboto,Arial,sans-serif;}
 .wrap{max-width:560px;margin:60px auto;padding:0 20px;}
 h1{color:#fff;font-size:22px;font-weight:700;}
 a{color:#dd3f4c;text-decoration:none;font-size:18px;font-weight:600;}
 li{margin:14px 0;list-style:none;}
 .u{color:#555;font-size:13px;display:block;margin-top:2px;}
</style></head><body><div class="wrap">
<h1>Explorant &mdash; Accounts</h1>
<ul>%s</ul>
</div></body></html>""" % body

def main():
    with open(DATA, encoding="utf-8") as f:
        users = json.load(f)

    with open(TPL_APP, encoding="utf-8") as f:
        app = f.read()
    with open(TPL_ACC, encoding="utf-8") as f:
        acct = f.read()

    # --- index.html : the app, with its seed kept in sync with users.json ---
    seed = json.dumps(users, ensure_ascii=False)
    app, n = re.subn(
        r'(<script id="seed" type="application/json">)(.*?)(</script>)',
        lambda m: m.group(1) + seed + m.group(3),
        app, flags=re.S)
    if n != 1:
        print("!! could not find the seed element in standalone.html", file=sys.stderr)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(app)
    print("wrote index.html")

    # --- one public page per account ---
    os.makedirs(os.path.join(OUT, "account"), exist_ok=True)
    for u in users:
        slug = u.get("slug")
        if not slug:
            print("!! user without slug:", u.get("username"), file=sys.stderr)
            continue
        d = os.path.join(OUT, "account", slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(bake_account(acct, u))
        print("wrote account/%s/index.html  (%s)" % (slug, u.get("name") or u.get("username")))

    # --- account/ index directory ---
    with open(os.path.join(OUT, "account", "index.html"), "w", encoding="utf-8") as f:
        f.write(listing_page(users))
    print("wrote account/index.html")

if __name__ == "__main__":
    main()
