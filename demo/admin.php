<?php
require __DIR__ . '/config.php';
if(!is_admin()){
  // allow login here
  if($_SERVER['REQUEST_METHOD']==='POST' && ($_POST['adminpw'] ?? '') === ADMIN_PASSWORD){
    $_SESSION['is_admin']=true;
  } else {
    ?><!DOCTYPE html><html><head><meta charset="utf-8"/><title>Admin Login</title>
    <link rel="stylesheet" href="style.css"/>
    <style>body{margin:0;background:var(--bg);color:var(--grey);font-family:Nunito,sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;}
    .box{background:var(--panel);border:1px solid var(--sep);border-radius:6px;padding:30px;width:320px;}
    h1{font-size:1.3rem;color:#fff;margin:0 0 16px;} input{width:100%;padding:10px;margin-bottom:14px;border:1px solid var(--sep);background:#1b1919;color:#e8e8e8;border-radius:4px;box-sizing:border-box;}
    button{width:100%;background:#dd3f4c;color:#fff;border:none;padding:11px;border-radius:4px;font-weight:700;cursor:pointer;}</style></head><body>
    <form class="box" method="post"><h1>Admin Login</h1>
      <input name="adminpw" type="password" placeholder="Admin password"/>
      <button type="submit">Enter</button>
    </form></body></html><?php exit;
  }
}

$users = load_users();
$msg = '';
if($_SERVER['REQUEST_METHOD']==='POST'){
  $action = $_POST['action'] ?? '';
  if($action === 'add'){
    // Build a full user from the form
    $lines = function($raw){ $out=[]; foreach(explode("\n", trim($raw)) as $l){ $l=trim($l); if($l==='')continue;
      $parts = array_map('trim', array_pad(explode('|', $l, 4), 4, ''));
      $out[] = ['name'=>$parts[0],'tier'=>$parts[1],'price'=>is_numeric($parts[2])?(int)$parts[2]:0,'img'=>img($parts[3])];
    } return $out; };
    $rankl = function($raw){ $out=[]; foreach(preg_split('/\r?\n/', trim($raw)) as $l){ $l=trim($l); if($l==='')continue;
      $p = array_map('trim', array_pad(explode('|', $l, 2), 2, '')); $out[]=['name'=>$p[0],'icon'=>img($p[1])]; } return $out; };
    $new = [
      'username'  => trim($_POST['username'] ?? ''),
      'password'  => (string)($_POST['password'] ?? ''),
      'name'      => trim($_POST['name'] ?? ''),
      'title'     => trim($_POST['title'] ?? ''),
      'region'    => trim($_POST['region'] ?? ''),
      'country'   => trim($_POST['country'] ?? ''),
      'level'     => (int)($_POST['level'] ?? 0),
      'levelNow'  => (int)($_POST['levelNow'] ?? 0),
      'levelMax'  => (int)($_POST['levelMax'] ?? 5000),
      'totalValue'=> (int)($_POST['totalValue'] ?? 0),
      'banner'    => img($_POST['banner'] ?? ''),
      'ranks'     => $rankl($_POST['ranks'] ?? ''),
      'skins'     => $lines($_POST['skins'] ?? ''),
      'buddies'   => $lines($_POST['buddies'] ?? ''),
      'cards'     => $lines($_POST['cards'] ?? ''),
      'sprays'    => $lines($_POST['sprays'] ?? ''),
      'missions'  => array_map(function($l){ $p=array_map('trim',array_pad(explode('|',$l,2),2,'')); return ['name'=>$p[0],'pct'=>is_numeric($p[1])?(float)$p[1]:0]; }, array_filter(array_map('trim', explode("\n", $_POST['missions'] ?? '')))),
      'titles'    => array_filter(array_map('trim', explode("\n", $_POST['titles'] ?? ''))),
    ];
    if($new['username']==='' || $new['password']===''){ $msg='Username and password are required.'; }
    elseif(find_user($new['username'])){ $msg='That username already exists.'; }
    else{ $users[] = $new; save_users($users); $msg='User "'.e($new['username']).'" added.'; }
  }
  elseif($action === 'delete'){
    $username = trim($_POST['username'] ?? '');
    $users = array_values(array_filter($users, fn($u)=>$u['username']!==$username));
    save_users($users); $msg='User removed.';
  }
}
?>
<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Admin — Explorant</title>
<link rel="stylesheet" href="style.css"/>
<style>
  body{margin:0;background:var(--bg);color:var(--grey);font-family:Nunito,sans-serif;}
  .wrap{max-width:1000px;margin:0 auto;padding:40px 24px;}
  h1{color:#fff;letter-spacing:2px;font-size:1.6rem;margin:0 0 4px;}
  .sub{color:var(--mut);margin:0 0 30px;font-size:.9rem;}
  h2{color:#fff;font-size:1.1rem;letter-spacing:1px;margin:0 0 14px;}
  .card{background:var(--panel);border:1px solid var(--sep);border-radius:6px;padding:24px;margin-bottom:26px;}
  .grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;}
  @media(max-width:700px){.grid{grid-template-columns:1fr;}}
  label{display:block;font-size:.72rem;color:#dd3f4c;text-transform:uppercase;letter-spacing:.5px;margin:0 0 5px;}
  input,textarea{width:100%;padding:9px 11px;border:1px solid var(--sep);border-radius:4px;background:#1b1919;color:#e8e8e8;font-size:.9rem;margin-bottom:14px;box-sizing:border-box;font-family:Nunito,sans-serif;}
  textarea{min-height:90px;resize:vertical;}
  .hint{font-size:.75rem;color:var(--mut);margin:-8px 0 14px;}
  .btn{display:inline-block;background:#dd3f4c;color:#fff;border:none;padding:11px 26px;border-radius:4px;font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:.82rem;cursor:pointer;}
  .btn.ghost{background:transparent;border:1px solid var(--sep);color:var(--grey);}
  .btn:hover{filter:brightness(1.1);}
  .msg{background:rgba(221,63,76,.12);border:1px solid #dd3f4c;color:#dd3f4c;border-radius:4px;padding:10px 14px;margin-bottom:20px;font-size:.85rem;}
  table{width:100%;border-collapse:collapse;font-size:.85rem;}
  th,td{padding:11px 12px;border-bottom:1px solid var(--sep);text-align:left;}
  th{color:var(--mut);font-weight:600;text-transform:uppercase;font-size:.7rem;letter-spacing:.5px;}
  td a{color:#dd3f4c;} td a.del{color:#b44;}
  .topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;}
  .btn-logout{color:var(--mut);font-size:.82rem;border:1px solid var(--sep);padding:8px 16px;border-radius:4px;}
  .btn-logout:hover{border-color:#dd3f4c;color:#dd3f4c;}
</style></head><body>
<div class="wrap">
  <div class="topbar">
    <h1>EXPLORANT ADMIN</h1>
    <div><a class="btn-logout" href="logout.php">Logout</a></div>
  </div>
  <p class="sub">Add as many users as you want. Each user gets their own login and account page showing the data you set (level, region, country, skins, battlepass, ranks, titles, missions…).</p>
  <?php if($msg): ?><div class="msg"><?= e($msg) ?></div><?php endif; ?>

  <div class="card">
    <h2>+ Add a user</h2>
    <form method="post">
      <input type="hidden" name="action" value="add"/>
      <div class="grid">
        <div><label>Login username</label><input name="username" required/></div>
        <div><label>Password</label><input name="password" required/></div>
        <div><label>Display name (nickname)</label><input name="name"/></div>
        <div><label>Title</label><input name="title"/></div>
        <div><label>Region</label><input name="region"/></div>
        <div><label>Country</label><input name="country"/></div>
        <div><label>Level</label><input name="level" type="number" value="1"/></div>
        <div><label>Level XP now</label><input name="levelNow" type="number" value="0"/></div>
        <div><label>Level XP max</label><input name="levelMax" type="number" value="5000"/></div>
        <div><label>Total value</label><input name="totalValue" type="number" value="0"/></div>
        <div style="grid-column:1/-1;"><label>Banner image URL (optional)</label><input name="banner" placeholder="https://…png"/></div>
      </div>

      <label style="margin-top:8px;">Skins — one per line:  Name | Tier | Price | Image-URL</label>
      <div class="hint">Tiers: Select, Deluxe, Premium, Exclusive, Rare, Ultra. Leave tier blank for no icon. e.g.<br/>Reaver Karambit | Exclusive | 4350 | https://media.valorant-api.com/weaponskinlevels/5ac106cd-45ef-a26f-2058-f382f20c64db/displayicon.png</div>
      <textarea name="skins" placeholder="Name | Tier | price | url&#10;RGX 11z Pro Vandal | Exclusive | 2175 | https://…"></textarea>

      <div class="grid">
        <div><label>Gun Buddies (same format)</label><textarea name="buddies" placeholder="Name | Tier | price | url"></textarea></div>
        <div><label>Cards (same format)</label><textarea name="cards" placeholder="Name | Tier | price | url"></textarea></div>
        <div><label>Sprays (same format)</label><textarea name="sprays" placeholder="Name | Tier | price | url"></textarea></div>
      </div>

      <div class="grid">
        <div><label>Ranks — one per line:  Name | Icon-URL</label><textarea name="ranks" placeholder="V26 - ACT IV | https://…largeicon.png"></textarea></div>
        <div><label>Missions — one per line:  Name | %</label><textarea name="missions" placeholder="Play A Match | 0&#10;Purchase Items from the Armory | 0.5"></textarea></div>
        <div><label>Titles — one per line</label><textarea name="titles" placeholder="Sweaty&#10;From the Grave"></textarea></div>
      </div>

      <button class="btn" type="submit">Add User</button>
    </form>
  </div>

  <div class="card">
    <h2>Existing users (<?= count($users) ?>)</h2>
    <?php if(empty($users)): ?><p style="color:var(--mut)">No users yet.</p>
    <?php else: ?>
    <table>
      <tr><th>Username</th><th>Name</th><th>Level</th><th>Value</th><th>Skins</th><th>Actions</th></tr>
      <?php foreach($users as $u): ?>
      <tr>
        <td><?= e($u['username']) ?></td>
        <td><?= e($u['name']) ?></td>
        <td><?= e($u['level']) ?></td>
        <td><?= e($u['totalValue']) ?></td>
        <td><?= count($u['skins'] ?? []) ?></td>
        <td><a href="account.php?u=<?= e(urlencode($u['username'])) ?>" target="_blank">view</a>
            &nbsp;<a class="del" href="#" onclick="return del('<?= e($u['username']) ?>')">delete</a></td>
      </tr>
      <?php endforeach; ?>
    </table>
    <?php endif; ?>
  </div>

  <p style="font-size:.8rem;color:var(--mut)"><a href="index.php" style="color:var(--grey)">&larr; Home</a> &nbsp; Admin password: you set it in <code>config.php</code>.</p>
</div>
<form id="delf" method="post" style="display:none"><input type="hidden" name="action" value="delete"/><input type="hidden" name="username"/></form>
<script>
function del(u){ if(!confirm('Delete "'+u+'"?')) return false; var f=document.getElementById('delf'); f.username.value=u; f.submit(); return false; }
</script>
</body></html>
