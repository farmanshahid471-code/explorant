<?php
require __DIR__ . '/config.php';

/* Who are we showing? ?u=USERNAME (any logged-in or public) */
$u = $_GET['u'] ?? '';
$user = $u !== '' ? find_user($u) : (current_user() ? find_user(current_user()) : null);
if(!$user){ header('Location: index.php'); exit; }

$banner = img($user['banner'] ?? '');
$tierIcons = [
  'Select'=>'12683d76-48d7-84a3-4e09-6985794f0445',
  'Deluxe'=>'0cebb8be-46d7-c12a-d306-e9907bfc5a25',
  'Premium'=>'60bca009-4182-7998-dee7-b8a2558dc369',
  'Exclusive'=>'e046854e-406c-37f4-6607-19a9ba8426fc',
  'Rare'=>'e046854e-406c-37f4-6607-19a9ba8426fc',
  'Ultra'=>'b46f7777-49a4-8a5f-5912-9b3e2b4f5c2e',
];
function card($it){ /* item card with tier icon + price + name */
  global $tierIcons;
  $img = img($it['img'] ?? '');
  $icon = isset($tierIcons[$it['tier']]) ? 'https://media.valorant-api.com/contenttiers/'.$tierIcons[$it['tier']].'/displayicon.png' : '';
  $price = !empty($it['price']) ? '<span class="badge-price">'.e($it['price']).'</span>' : '';
  $tier  = $icon ? '<span class="badge-tier"><img src="'.e($icon).'" alt="'.e($it['tier']).'" onerror="this.parentNode.style.display=\'none\'" /></span>' : '';
  return '<div class="item"><div class="pos">'.$price.$tier
    .'<div class="thumb"><img src="'.e($img).'" alt="'.e($it['name']).'" onerror="this.style.visibility=\'hidden\'" /></div></div>'
    .'<div class="card-footer"><div class="card-subtitle">'.e($it['name']).'</div></div></div>';
}
function itemGrid($arr,$cols='grid'){ 
  if(empty($arr)) return '<div class="empty-h5">No Items to Show</div>';
  return '<div class="'.$cols.'">'.implode('', array_map('card',$arr)).'</div>';
}
$skins = $user['skins'] ?? []; $buds=$user['buddies']??[]; $crd=$user['cards']??[]; $spr=$user['sprays']??[];
$ranks = $user['ranks'] ?? []; $titles=$user['titles'] ?? []; $missions = $user['missions'] ?? [];
$totalValue = $user['totalValue'] ?? 0;
function cardTitle($t){ return '<div class="title-card"><div class="title-text">'.e($t).'</div></div>'; }
function ring($pct){
  $r=48; $c=2*M_PI*$r; $off=$c*(1-$pct/100);
  return '<svg class="CircularProgressbar" viewBox="0 0 100 100">'
    .'<path class="trail" d="M 50,50 m 0,-48 a 48,48 0 1 1 0,96 a 48,48 0 1 1 0,-96" stroke-width="4" fill-opacity="0" style="stroke-dasharray:'.$c.'px;stroke-dashoffset:0px;stroke:var(--separator-color)"/>'
    .'<path class="path" d="M 50,50 m 0,-48 a 48,48 0 1 1 0,96 a 48,48 0 1 1 0,-96" stroke-width="4" stroke-linecap="round" fill-opacity="0" style="stroke-dasharray:'.$c.'px;stroke-dashoffset:'.$off.'px;stroke:'.$GLOBALS['red'].'"/>'
    .'<text x="50" y="50" text-anchor="middle" dominant-baseline="middle" style="font-size:20px;fill:#8f8f8f;font-family:Nunito,sans-serif">'.$pct.'%</text></svg>';
}
$GLOBALS['red'] = '#dd3f4c';
$lv = $user['level'] ?? 0; $ln = $user['levelNow'] ?? 0; $lm = $user['levelMax'] ?? 5000;
?>
<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title><?= e($user['name'] ?? $user['username']) ?> — Explorant</title>
<link rel="stylesheet" href="style.css"/>
</head><body>
<?php $b64 = base64_encode(file_get_contents(__DIR__.'/logo.png')); ?>
<nav class="navbar">
  <div class="navbar-left"><a class="btn" style="color:#dd3f4c;border-color:#dd3f4c;" href="index.php">&larr; Home</a></div>
  <a class="navbar-logo" href="index.php"><img class="brand" src="data:image/png;base64,<?= $b64 ?>" alt="Explorant"/></a>
  <div class="navbar-right">
    <?php if(current_user()): ?>
      <div class="user"><span class="name"><?= e(current_user()) ?></span><a class="btn" style="color:#dd3f4c;border-color:#dd3f4c;" href="logout.php">Logout</a></div>
    <?php else: ?>
      <div class="user"><a class="btn" style="color:#dd3f4c;border-color:#dd3f4c;" href="login.php">Login</a></div>
    <?php endif; ?>
  </div>
</nav>

<main>
<h1 class="account-name"><?= e($user['name'] ?? $user['username']) ?></h1>

<nav class="tabs" id="tabs">
  <div class="tab active" data-pane="details">DETAILS</div>
  <div class="tab" data-pane="skins">WEAPON SKINS</div>
  <div class="tab" data-pane="buddies">BUDDIES</div>
  <div class="tab" data-pane="cards">CARDS</div>
  <div class="tab" data-pane="sprays">SPRAYS</div>
  <div class="tab" data-pane="titles">TITLES</div>
  <div class="tab" data-pane="progressions">PROGRESSIONS</div>
</nav>

<!-- DETAILS -->
<section class="pane active" data-pane="details">
  <div class="details-top">
    <div class="card">
      <div class="card-img-top"><?php if($banner): ?><img src="<?= e($banner) ?>" alt="" style="width:100%;height:100%;object-fit:cover;display:block;"/><?php else: ?><div style="height:100%;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:800;color:#dd3f4c;">◆ EXPLORANT</div><?php endif; ?></div>
      <div class="card-body">
        <div class="card-title">Account Info<hr/></div>
        <div class="row g-2" style="margin-top:14px;grid-template-columns:1fr 1fr;">
          <div>
            <p class="themed-lbl">Nickname</p><p class="val"><?= e($user['name'] ?? '') ?></p>
            <p class="themed-lbl">Title</p><p class="val"><?= e($user['title'] ?? '') ?></p>
            <p class="themed-lbl">Region</p><p class="val"><?= e($user['region'] ?? '') ?></p>
            <p class="themed-lbl">Country</p><p class="val"><?= e($user['country'] ?? '') ?></p>
          </div>
          <div>
            <p class="themed-lbl">Level</p>
            <div class="lvl"><?= e($lv) ?></div>
            <div class="lvl-xp"><?= e($ln) ?> / <?= e($lm) ?></div>
            <p class="themed-lbl" style="margin-top:6px;">Total Value</p><p class="val"><?= e($totalValue) ?></p>
          </div>
        </div>
      </div>
    </div>
    <div class="card"><div class="card-body"><div class="card-title">Recent Penalties<hr/></div>
      <div class="text-muted" style="text-align:center;line-height:1.8;font-size:.9rem;margin-top:24px;">No Penalties Recently</div></div></div>
    <div class="card"><div class="card-body"><div class="card-title">Ranks<hr/></div>
      <?php if(empty($ranks)): ?><div class="text-muted" style="line-height:1.8;font-size:.85rem;margin-top:8px;">Ranks Not Fetched Yet. Please Ask Owner to Refresh Account</div>
      <?php else: foreach($ranks as $r): ?>
        <div class="rank-inline"><img src="<?= e($r['icon'] ?? '') ?>" alt=""/><div><?= e($r['name'] ?? '') ?></div></div>
      <?php endforeach; endif; ?></div></div>
  </div>
</section>

<!-- WEAPON SKINS -->
<section class="pane" data-pane="skins">
  <?= cardTitle('Weapon Skins') ?>
  <?= itemGrid($skins) ?>
</section>
<!-- BUDDIES -->
<section class="pane" data-pane="buddies"><?= cardTitle('Gun Buddies') ?><?= itemGrid($buds) ?></section>
<!-- CARDS -->
<section class="pane" data-pane="cards"><?= cardTitle('Account Cards') ?><?= itemGrid($crd) ?></section>
<!-- SPRAYS -->
<section class="pane" data-pane="sprays"><?= cardTitle('Account Sprays') ?><?= itemGrid($spr) ?></section>
<!-- TITLES -->
<section class="pane" data-pane="titles"><?= cardTitle('Account Titles') ?>
  <?php if(empty($titles)): ?><div class="empty-h5">No Titles to Show</div>
  <?php else: ?><div class="grid grid-titles"><?php foreach($titles as $t): ?>
    <div class="item"><div class="pos"><div class="title-block"><?= e($t) ?></div></div>
      <div class="card-footer"><div class="card-subtitle"><?= e($t) ?> <span class="title-suffix">Title</span></div></div></div>
  <?php endforeach; ?></div><?php endif; ?>
</section>
<!-- PROGRESSIONS -->
<section class="pane" data-pane="progressions">
  <?= cardTitle('Progressions') ?>
  <div class="row g-2" style="margin-bottom:1.5rem;">
    <div class="card"><div class="card-body inline-titled"><div class="card-title">Next First Win</div><div class="muted-inline">Available</div></div></div>
    <div class="card"><div class="card-body inline-titled"><div class="card-title">Next Weekly Missions</div><div class="muted-inline">Tue 21-Jul-2026 8:15 AM</div></div></div>
  </div>
  <div class="card" style="margin-bottom:1.5rem;"><div class="card-body"><div class="card-title">Daily Missions<hr/></div><div class="empty-h5">No Daily Missions</div></div></div>
  <div class="card"><div class="card-body"><div class="card-title">Weekly Missions<hr/></div>
    <div class="mission-list"><?php foreach($missions as $m): ?>
      <div class="mission-inner"><div class="card-title"><?= e($m['name'] ?? '') ?></div><div class="progress-bar-circle"><?= ring($m['pct'] ?? 0) ?></div></div>
    <?php endforeach; ?></div></div></div>
</section>

<footer>Explorant — demo account showcase.</footer>
</main>

<script>
document.querySelectorAll('.tab').forEach(function(t){
  t.addEventListener('click',function(){
    var p=t.dataset.pane;
    document.querySelectorAll('.tab').forEach(function(x){x.classList.toggle('active',x===t);});
    document.querySelectorAll('.pane').forEach(function(x){x.classList.toggle('active',x.dataset.pane===p);});
  });
});
</script>
</body></html>
