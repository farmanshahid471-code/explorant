<?php
require __DIR__ . '/config.php';
?>
<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Forget Password - Explorant</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="app.css"/>
<style>.login-page{min-height:100vh;}</style>
</head><body>
<div class="login-page">
  <div class="side-text"><b>DEFY</b> THE <b>LIMITS</b></div>
  <div class="login-card">
    <div class="logo"><img src="logo.png" alt="Explorant"/></div>
    <div class="row"><span class="t">Reset Password</span><span class="s">Remembered it? <a href="login.php">Login</a></span></div>
    <form method="post" novalidate>
      <div class="fld"><span class="lbl">E-mail</span><input type="text" name="email" autocomplete="username"/><span class="bar"></span></div>
      <div class="foot"><a class="forget" href="login.php">&larr; Back to Login</a>
        <button type="submit" class="btn-login" onclick="return false;">SEND</button></div>
    </form>
  </div>
</div>
</body></html>
