# Deploying the Explorant clone on WordPress

These 4 files give you a **pixel-perfect copy** of the Explorant *home page* and the
*account-review page* as WordPress **custom page templates** — no theme header/footer/
sidebar, so the activated theme can't alter the design.

## Files
| File | Purpose |
|------|---------|
| `page-explorant-home.php` | WP page template → renders the landing page |
| `explorant-home.html` | The landing page HTML (loaded by the template above) |
| `page-explorant-account.php` | WP page template → renders the account-page clone |
| `explorant-account.html` | The account-page HTML (Details/Store/Skins/Agents/etc.) |

## Setup (takes ~3 minutes)

1. **Upload the files into your theme folder.**
   Use FTP or your host's file manager (or cPanel → File Manager) and put all four
   files into your **active theme folder**, e.g.
   `wp-content/themes/your-theme/`.
   > If you're already using a child theme, put them there instead
   > (`wp-content/themes/your-theme-child/`).

2. **Create the Home page.**
   - WP Admin → **Pages → Add New**
   - Title it e.g. "Home"
   - In the right panel, **Template** dropdown → select **"Explorant — Home"**
   - Leave the content body **empty**, **Publish**.

3. **Create the Account page.**
   - Pages → Add New → Title "My Account"
   - Template → **"Explorant — Account"**
   - Leave body empty, **Publish**.

4. **Set Home as the site's front page** (optional but recommended).
   - WP Admin → **Settings → Reading**
   - "Your homepage displays" → **A static page** → Homepage: **Home**
   - Save.

5. Add the pages to your menu (Appearance → Menus) so visitors can switch between them.

## How to edit the content
- Everything lives in the two `.html` files.
- **Landing page**: edit `explorant-home.html` — texts, features, prices, and the
  comparison rows are at the bottom in the `<script>` (`FEATS`, `PLANS`, `ROWS`).
- **Account page**: edit `explorant-account.html` — the editable data is at the top
  of the `<script>` (`ACCOUNT`, `GUNS`, `STORE`, `AGENTS`, `BUDDIES`, `CARDS`,
  `SPRAYS`, `TITLES`, `MISSIONS`, `RANKS`). Add/remove items in those arrays.
- To change the theme colors, edit the `:root{ --bg / --panel / --red ... }` block
  at the top of each file's `<style>`.

## Important note about the "real" features
The homepage and the account page are **static, self-contained designs**. The *live*
Explorant features — Riot account sign-in, real-time inventory/store sync, leaderboards,
Patreon checkout — are a backend service (an API app), **not** a WordPress page. Those
cannot run on a plain WordPress install. If you need them, they require a separate
custom built app/API; the WordPress pages here give you the identical design and a
place to link to those services or replace the sample data with your real content.

## Troubleshooting
- **Page shows blank/content missing** → make sure the matching `.html` file is in the
  SAME folder as the `.php` template, and names are unchanged.
- **Theme colors overriding the design** → this template intentionally skips
  `get_header()/get_footer()`. If a plugin forces styles, open the `.php` and it already
  outputs a complete page with its own styling, so nothing else should apply.
- **Images (weapons, agents, rank icons, coins) show as blanks** → they load from
  `media.valorant-api.com` which needs internet; that's normal and fine on the live site.
