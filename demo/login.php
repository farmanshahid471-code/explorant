<?php
require __DIR__ . '/config.php';
$err = '';
if($_SERVER['REQUEST_METHOD']==='POST'){
  $u = trim($_POST['username'] ?? '');
  $p = (string)($_POST['password'] ?? '');
  $user = find_user($u);
  if($user && $user['password'] === $p){
    $_SESSION['user'] = $user['username'];
    header('Location: app.php'); exit;
  }
  if($u === 'admin' && $p === ADMIN_PASSWORD){ $_SESSION['is_admin']=true; header('Location: admin.php'); exit; }
  $err = 'Invalid username or password.';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Login - Explorant</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="app.css" />
<style>
  /* error message shown inside the card */
  .err{display:block;background:var(--theme-color-1-10);border:1px solid var(--theme-color-1);
    color:var(--theme-color-1);border-radius:4px;padding:9px 12px;font-size:12px;margin:0 0 18px;text-align:center;}
  .login-page{min-height:100vh;}
</style>
</head>
<body>

<div class="login-page">
  <!-- decorative accents (matching the reference layout) -->
  <span class="deco line" style="left:9%;top:20%;"></span>
  <span class="deco sq"    style="left:11%;top:27%;color:var(--theme-color-1);"></span>
  <span class="deco sq"    style="left:12%;top:30%;color:var(--primary-color);"></span>
  <span class="deco line"  style="left:9%;top:70%;"></span>
  <span class="deco sq"    style="left:11%;top:76%;color:var(--theme-color-1);"></span>
  <span class="deco line"  style="right:9%;top:22%;"></span>
  <span class="deco sq"    style="right:11%;top:30%;color:var(--theme-color-1);"></span>
  <span class="deco sq"    style="right:13%;top:33%;color:var(--primary-color);"></span>
  <span class="deco" style="right:12%;top:26%;font-size:34px;font-weight:800;letter-spacing:2px;color:var(--theme-color-1);">03.</span>
  <span class="deco line"  style="left:22%;bottom:9%;"></span>
  <span class="deco sq"    style="left:24%;bottom:13%;color:var(--theme-color-1);"></span>
  <span class="deco line"  style="right:22%;bottom:9%;"></span>

  <!-- vertical tagline -->
  <div class="side-text"><b>DEFY</b> THE <b>LIMITS</b></div>

  <!-- login card -->
  <div class="login-card">
    <div class="logo"><img src="logo.png" alt="Explorant" /></div>

    <div class="row">
      <span class="t">Login</span>
      <span class="s">Not Registered? <a href="register.php">Register</a></span>
    </div>

    <?php if($err): ?><div class="err"><?= e($err) ?></div><?php endif; ?>

    <form method="post" novalidate>
      <div class="fld">
        <span class="lbl">E-mail</span>
        <input type="text" name="username" autocomplete="username" autofocus />
        <span class="bar"></span>
      </div>
      <div class="fld">
        <span class="lbl">Password</span>
        <input type="password" name="password" autocomplete="current-password" />
        <span class="bar"></span>
      </div>

      <div class="foot">
        <a class="forget" href="forgot-password.php">Forget password?</a>
        <button type="submit" class="btn-login">LOGIN</button>
      </div>
    </form>
  </div>
</div>

</body>
</html>
