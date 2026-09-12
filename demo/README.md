# Explorant Demo app (PHP)

A self-contained, data-driven demo that matches the Explorant design and gives you:

- **Login** (users only exist because YOU created them — there is no public signup)
- **Admin panel** to add as many users as you want, each with their own
  login + full account data (level, region, country, skins, buddies, cards,
  sprays, ranks, titles, missions, total value, banner).
- **Per-user account page** (Details / Weapon Skins / Buddies / Cards / Sprays /
  Titles / Progressions) rendered from that user's data.

## Quick start (any host with PHP)

Upload the whole `demo/` folder to your PHP host (or run locally). Then:

| Page | URL | Notes |
|------|-----|-------|
| Home | `index.php` | Hero matching the screenshot |
| Login | `login.php` | Admin-created users log in here |
| Dashboard | `app.php` | **Login required.** The accounts app — fed by the user store |
| Admin | `admin.php` | Log in with the admin password, then add/manage users |
| Account | `account.php?u=twt` | A user's public account page |

### Dashboard (`app.php`)

After a successful login you land in the app dashboard. The **Accounts** list and
all sub-views are **generated live from `data/users.json`**, so every user you add
in the admin panel automatically appears here.

- **Home** — Total Accounts / Total Folders cards
- **Accounts** — grid of account cards (search filters live; "Add Account" → admin)
- **Folders / Info / Reminders** — empty placeholders (structure ready)
- **Skins** — aggregates every skin added across all accounts (tier + owner)
- **Leaderboards** — ranked by account value

## Default sign-in for testing

- **User:** `twt` / password `twt123`
- **Admin:** go to `admin.php` and enter the admin password.

## Where to change things

- **Admin password** → `config.php`: `define('ADMIN_PASSWORD', 'explorant-admin');`
- **Data** → `data/users.json` (JSON: username, password, name, title, region,
  country, level, levelNow/levelMax, totalValue, banner, ranks, skins, buddies,
  cards, sprays, missions, titles). The admin panel edits this file for you —
  you usually won't touch it by hand, but you can.

## Adding a user (admin panel)

1. Go to `admin.php`, log in.
2. Fill the "Add a user" form:
   - username + password (their login)
   - display name, title, region, country, level, level XP, total value
   - **Skins** — one per line: `Name | Tier | Price | Image-URL`
     (Tier: Select / Deluxe / Premium / Exclusive / Rare / Ultra)
   - Buddies / Cards / Sprays — same format
   - **Ranks** — one per line: `V26 - ACT IV | https://…largeicon.png`
   - **Missions** — one per line: `Play A Match | 0`
   - **Titles** — one per line
3. Click **Add User**. The user can now log in and view their account page.

## Not included (on purpose)

This is a **demo**. Passwords are stored plainly in `users.json` and there is **no
Riot-API sync** — that requires a real backend service. If you go to production:

- Hash passwords (`password_hash` / `password_verify`).
- Move storage to a database (MySQL/SQLite).
- Add CSRF + rate-limiting to the admin form.
- To pull *real* inventory, build an API that talks to Riot's endpoints.
