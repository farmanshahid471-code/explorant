<?php
require __DIR__ . '/config.php';
$logged = current_user();
$b64 = base64_encode(file_get_contents(__DIR__.'/logo.png'));
$logo = 'data:image/png;base64,'.$b64;
?>
<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Explorant — Explore &amp; Showcase your Account</title>
<style>
  :root{--bg:#1b1919;--panel:#222020;--sep:#424242;--red:#dd3f4c;--grey:#8f8f8f;--white:#fff;}
  *{box-sizing:border-box;} body{margin:0;background:var(--bg);color:var(--grey);font-family:Nunito,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;}
  a{color:inherit;text-decoration:none;} img{max-width:100%;}
  .navbar{display:flex;align-items:center;justify-content:space-between;padding:18px 30px;background:var(--bg);}
  .navbar .logo img{height:46px;display:block;}
  .nav-r{display:flex;align-items:center;gap:26px;}
  .socials-n a{color:#7aa8d8;margin-left:22px;font-size:.9rem;display:inline-flex;align-items:center;gap:6px;}
  .socials-n a:hover{color:#fff;}
  .nav-login{color:var(--grey);font-size:.9rem;font-weight:700;letter-spacing:1px;}
  .nav-login:hover{color:var(--red);}
  .btn-register{border:1px solid var(--grey);color:var(--grey);padding:9px 20px;border-radius:3px;font-size:.85rem;font-weight:700;letter-spacing:1px;}
  .btn-register:hover{border-color:var(--red);color:var(--red);}
  .hero{padding:80px 0 90px;text-align:center;background:radial-gradient(1200px 500px at 50% -30%,rgba(221,63,76,.10),transparent 70%);}
  .hero h1{font-size:3.6rem;font-weight:800;letter-spacing:12px;color:var(--red);margin:0 0 30px;text-transform:uppercase;}
  .hero .tag{font-size:1.2rem;font-weight:600;color:var(--grey);margin:0 0 16px;}
  .hero .sub{max-width:700px;margin:0 auto 34px;color:var(--grey);font-size:1.15rem;line-height:1.7;}
  .hero .explore{font-size:1.2rem;font-weight:600;color:var(--grey);letter-spacing:2px;margin:0 0 26px;text-transform:uppercase;}
  .btn-start{display:inline-block;background:#aa5e6c;color:#fff;border-radius:5px;padding:15px 40px;font-size:.95rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;cursor:pointer;}
  .btn-start:hover{background:#c06a7c;}
  .wrap{max-width:1240px;margin:0 auto;padding:0 24px;}
  footer{padding:40px 24px;text-align:center;color:var(--grey);font-size:.82rem;}
  .btn{margin:6px;display:inline-block;background:transparent;border:1px solid var(--sep);color:var(--grey);padding:10px 22px;border-radius:4px;font-weight:700;letter-spacing:.5px;font-size:.85rem;}
  .btn:hover{border-color:var(--red);color:var(--red);}
</style></head><body>

<div class="navbar">
  <div class="logo"><img src="<?= $logo ?>" alt="Explorant"></div>
  <div class="nav-r">
    <div class="socials-n">
      <a href="#"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M23 5a10 10 0 0 1-3 .8A5 5 0 0 0 23 3a10 10 0 0 1-3.3 1.3A5 5 0 0 0 12 6.5 5 5 0 0 0 12.1 8 14 14 0 0 1 1.7 3.8a5 5 0 0 0 1.5 6.7A5 5 0 0 1 1 10a5 5 0 0 0 4 4.9 5 5 0 0 1-2.3.1 5 5 0 0 0 4.7 3.5A10 10 0 0 1 0 20.5 14 14 0 0 0 7.7 23c9.2 0 14.3-7.6 14.3-14.3v-.6A10 10 0 0 0 23 5z"/></svg>Twitter</a>
      <a href="#"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M20 5a19 19 0 0 0-4.5-1.4 16 16 0 0 0-.6 1.3A17 17 0 0 0 5.1 4.9 19 19 0 0 0 .5 18.4 19 19 0 0 0 5.3 20c.5-.7 1-1.4 1.4-2.2-.8-.3-1.5-.6-2.2-1.1l.5-.4a14 14 0 0 0 12 0l.5.4c-.7.5-1.4.8-2.2 1.1.4.8.9 1.5 1.4 2.2a19 19 0 0 0 4.8-1.6A19 19 0 0 0 20 5zM8.3 15.5c-.8 0-1.4-.7-1.4-1.6s.6-1.6 1.4-1.6 1.4.7 1.4 1.6-.6 1.6-1.4 1.6zm7.4 0c-.8 0-1.4-.7-1.4-1.6s.6-1.6 1.4-1.6 1.4.7 1.4 1.6-.6 1.6-1.4 1.6z"/></svg>Discord</a>
      <a href="#"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12z"/></svg>Facebook</a>
    </div>
    <a class="nav-login" href="login.php">LOGIN</a>
    <a class="btn-register" href="login.php">REGISTER</a>
  </div>
</div>

<header class="hero">
  <div class="wrap">
    <h1>EXPLORANT</h1>
    <p class="tag">Explore and showcase your Account with Explorant</p>
    <p class="sub">The ultimate platform for managing account, viewing stats, inventory and store, and sharing with friends.</p>
    <p class="explore">Explore Now !!</p>
    <?php if($logged): ?>
      <a class="btn-start" href="account.php?u=<?= e(urlencode($logged)) ?>">View my account ›</a>
    <?php else: ?>
      <a class="btn-start" href="login.php">GET STARTED ›</a>
    <?php endif; ?>
  </div>
</header>

<footer>
  Explored with <a href="index.php">Explorant</a>
  <?php if($logged): ?> · <a href="account.php?u=<?= e(urlencode($logged)) ?>">My Account</a>
    <?php if(is_admin()): ?> · <a href="admin.php">Admin</a><?php endif; ?>
    · <a href="logout.php">Logout</a><?php else: ?> · <a href="admin.php">Admin</a><?php endif; ?>
</footer>
</body></html>
