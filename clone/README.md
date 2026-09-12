# Explorant — full site clone (static)

A pixel-matched, fully responsive static replica of the Explorant public site.
Palette, typography (Nunito), spacing, buttons and dark theme are matched to the
live site and the reference screenshot.

## Pages

| File                  | Page                                  |
|-----------------------|---------------------------------------|
| `index.html`          | Home (hero, features, pricing, comparison, CTA, footer) |
| `login.html`          | Login                                 |
| `register.html`       | Register (name + password + confirm + reCAPTCHA) |
| `forgot-password.html`| Forgot / reset password               |
| `account.html`        | Account dashboard (11 tabs, data-driven) |
| `404.html`            | Custom 404                            |

## Run it

No build step. Open `index.html` directly, or serve the folder:

```bash
cd clone
python3 -m http.server 8080
# → http://localhost:8080/index.html
```

(Or any static host / `npx serve`.)

## Structure

```
clone/
  index.html          Home
  login.html          Login
  register.html       Register
  forgot-password.html
  account.html        Dashboard (self-contained, edit its data arrays)
  404.html
  assets/
    style.css         shared design system (tokens in :root)
    data.js           features / plans / comparison content (edit here)
    main.js           interactions + rendering
    logo.png          brand logo
```

## Where to edit content

- **Homepage features / pricing / comparison** → `assets/data.js` (`FEATS`, `PLANS`, `ROWS`).
- **Colors / fonts / spacing** → `assets/style.css` at the `:root` tokens at the top.
- **Account data** → `account.html` (its editable arrays near the bottom: `GUNS`,
  `STORE`, `ACCESSORY`, `AGENTS`, `BUDDIES`, `CARDS`, `SPRAYS`, `TITLES`,
  `MISSIONS`, `RANKS`, `ACCOUNT`, `CURRENCIES`, `BATTLEPASSES`, …).

## Design tokens (sampled from the live site)

- Background `#1b1919`, navbar/cards `#222020`, lighter panel `#2a2828`, borders `#424242`
- Accent red `#dd3f4c`, GET-STARTED pink `#aa5e6c` (hover `#c06a7c`)
- Text grey `#8f8f8f`, white headings
- Scrollbar `#24b299` · Font **Nunito** (400/500/600/700/800)

## Interactive behaviour

- Sticky navbar gains a border + shadow on scroll.
- Mobile hamburger toggles a slide-down menu (socials move under it).
- Feature cards, pricing and the comparison table are rendered from `data.js`.
- `data-reveal` elements fade/slide in on scroll (IntersectionObserver).
- Login / Register / Forgot forms validate client-side and route to the dashboard;
  in production wire them to a real backend (see the PHP app in `demo/`).
