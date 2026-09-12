<?php
/* ============================================================
   Explorant demo — App dashboard (login required)
   Views: Home / Accounts / Folders / Skins / Info / Reminders / Leaderboards
   Accounts list is fed by data/users.json (users created in admin.php).
   ============================================================ */
require __DIR__ . '/config.php';

if(empty($_SESSION['user']) && !is_admin()){
  header('Location: login.php'); exit;
}

$users   = load_users();
$folders = [];
$reminders = [];

/* ---- build a JSON payload for the client to render ---- */
$accounts = array_map(function($u){
  return [
    'username' => $u['username'] ?? '',
    'name'     => ($u['name'] ?? '') ?: ($u['username'] ?? ''),
    'tag'      => ($u['totalValue'] ?? 0) > 0 ? 'Radiant' : 'Silver',
    'level'    => (int)($u['level'] ?? 0),
    'total'    => (int)($u['totalValue'] ?? 0),
    'region'   => $u['region'] ?? '',
    'skins'    => count($u['skins'] ?? []),
    'banner'   => img($u['banner'] ?? ''),
    'expired'  => !empty($u['expired']),
    'riot_user'=> $u['riot_user'] ?? '',
    'riot_pass'=> $u['riot_pass'] ?? '',
  ];
}, $users);

/* leaderboard: sort by total value desc */
$leaderboard = $accounts;
usort($leaderboard, function($a,$b){ return $b['total'] - $a['total']; });

/* skins view: aggregate all skins across accounts */
$allSkins = [];
foreach($users as $u){
  foreach(($u['skins'] ?? []) as $s){
    $allSkins[] = [
      'name'  => $s['name'] ?? '',
      'tier'  => $s['tier'] ?? '',
      'price' => $s['price'] ?? 0,
      'img'   => img($s['img'] ?? ''),
      'acc'   => ($u['name'] ?? '') ?: $u['username'],
    ];
  }
}

$me = current_user();
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Dashboard - Explorant</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="app.css" />
<style>
  /* sub-view specific bits */
  #view-folders .stat-grid,#view-leaderboards .stat-grid{grid-template-columns:repeat(auto-fill,minmax(300px,1fr));}
  .empty{color:var(--primary-color);font-size:13px;padding:40px 0;text-align:center;opacity:.7;}
  .empty .big{font-size:40px;margin-bottom:8px;color:var(--theme-color-1);}
  table.lb{width:100%;border-collapse:collapse;margin-top:6px;font-size:13px;}
  table.lb th,table.lb td{padding:11px 14px;text-align:left;border-bottom:1px solid var(--separator-color);color:var(--primary-color);}
  table.lb th{color:var(--theme-color-1);font-weight:700;text-transform:uppercase;font-size:11px;letter-spacing:.5px;}
  table.lb tr:hover td{background:var(--theme-color-1-10);}
  table.lb .rank{font-weight:800;}
  .chip{display:inline-block;border:1px solid var(--separator-color);border-radius:20px;padding:3px 10px;font-size:11px;}
  a.acc-link:hover .name{color:var(--theme-color-1);}
  a.acc-link .name{transition:color .15s;}
  /* expired badge + card */
  .acc-card .banner-tag.expired{background:var(--theme-color-1);}
  .acc-card.expired{cursor:pointer;border-color:var(--theme-color-1);}
  .acc-card.expired:hover .name{color:var(--theme-color-1);}
  .acc-card.expired .thumb:after{content:"";position:absolute;inset:0;background:rgba(221,63,76,.06);}
  /* Riot credentials modal */
  .riot-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);display:none;align-items:center;justify-content:center;z-index:200;padding:20px;}
  .riot-overlay.show{display:flex;}
  .riot-card{width:100%;max-width:420px;background:var(--foreground-color);border:1px solid var(--separator-color);border-radius:6px;padding:30px 28px;box-shadow:0 30px 80px rgba(0,0,0,.6);}
  .riot-card h2{margin:0 0 4px;font-size:18px;font-weight:700;color:var(--primary-color);}
  .riot-card p{margin:0 0 20px;font-size:12px;color:var(--primary-color);opacity:.8;}
  .riot-card .fld{margin-bottom:18px;}
  .riot-card .foot{display:flex;align-items:center;justify-content:flex-end;gap:12px;}
  .riot-card .cancel{background:none;border:1px solid var(--separator-color);color:var(--primary-color);border-radius:4px;padding:9px 18px;font-size:12px;font-weight:700;}
  .riot-card .cancel:hover{border-color:var(--theme-color-1);color:var(--theme-color-1);}
</style>
</head>
<body>

<div class="app">
  <!-- ================= SIDEBAR ================= -->
  <aside class="sidebar">
    <button class="menu-btn" aria-label="Menu"><span></span><span></span><span></span></button>
    <nav class="side-nav">
      <a class="side-item active" href="#" data-view="home">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg><span>Home</span>
      </a>
      <a class="side-item" href="#" data-view="accounts">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h16M4 18h16"/><path d="M4 6h4M4 12h4M4 18h4"/></svg><span>Accounts</span>
      </a>
      <a class="side-item" href="#" data-view="folders">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 7l2-3h14l2 3v13H3z"/><path d="M3 7h18"/></svg><span>Folders</span>
      </a>
      <a class="side-item" href="#" data-view="info">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 12v4"/></svg><span>Info</span>
      </a>
      <a class="side-item" href="#" data-view="skins">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h16M4 18h16"/><circle cx="16" cy="6" r="2"/><circle cx="8" cy="12" r="2"/><circle cx="16" cy="18" r="2"/></svg><span>Skins</span>
      </a>
      <a class="side-item" href="#" data-view="reminders">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg><span>Reminders</span>
      </a>
      <a class="side-item" href="#" data-view="leaderboards">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 20V10M10 20V4M16 20v-7M4 20h17"/></svg><span>Leaderboards</span>
      </a>
    </nav>
  </aside>

  <!-- ================= MAIN ================= -->
  <div class="main">
    <div class="topbar">
      <div class="left"><a class="contact" href="admin.php">Contact Support</a></div>
      <div class="center"><a class="logo" href="app.php"><img src="logo.png" alt="Explorant" /></a></div>
      <div class="right">
        <span class="degraded" title="Degraded Performance"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2 L23 21 H1 z"/></svg> Degraded Performance</span>
        <span class="user-chip"><?= e($me ?: ($_SESSION['user'] ?? 'guest')) ?></span>
        <a class="bell" href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg><span class="dot"></span></a>
      </div>
    </div>

    <div class="banner warn">
      <span>[+] Search: Thousands of VALORANT Daily Stores | Instant Skin Alerts | Unlimited Bulk Add Faster Than Ever</span>
      <button class="close" aria-label="dismiss">&times;</button>
    </div>
    <div class="banner gold">
      <span>&gt; Paid but no Premium? Contact support@explorant.space or DM us on Discord via Contact Support in the top left for faster assistance.</span>
      <button class="close" aria-label="dismiss">&times;</button>
    </div>

    <div class="content">

      <!-- HOME -->
      <section id="view-home">
        <div class="crumb">Home<b>Dashboard / Home</b></div>
        <div class="stat-grid">
          <div class="stat-card">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M3 6l3-3h12l3 3v13a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M3 6h18M9 6V3M15 6V3"/><path d="M9 12h6"/></svg></div>
            <div class="lbl">Total Accounts</div><div class="val"><?= count($accounts) ?></div>
          </div>
          <div class="stat-card">
            <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M3 6l3-3h12l3 3v13a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M3 6h18M9 6V3M15 6V3"/><path d="M9 12h6"/></svg></div>
            <div class="lbl">Total Folders</div><div class="val">0</div>
          </div>
        </div>
      </section>

      <!-- ACCOUNTS -->
      <section id="view-accounts" style="display:none;">
        <div class="acc-top">
          <div class="h">Accounts<b>Dashboard / Accounts</b></div>
          <div class="r">
            <span class="slots-pill"><i></i> Slots: <b id="slotCount">3</b></span>
            <a class="add-acc" href="admin.php">Add Account</a>
            <button class="icon-btn" title="More"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/></svg></button>
          </div>
        </div>
        <div class="filters">
          <button class="icon-btn" title="Grid"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg></button>
          <button class="icon-btn" title="List"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></svg></button>
          <button class="filter-pill">Order by: Descending <span>&#9662;</span></button>
          <button class="filter-pill">All Accounts</button>
          <label class="search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/></svg><input type="text" placeholder="Search Account" id="searchInput" /></label>
        </div>
        <div class="count-row"><span id="countText"></span><button class="icon-btn" title="Columns"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="16" rx="1"/><path d="M10 4v16M15 4v16"/></svg></button></div>
        <div class="acc-grid" id="accGrid"></div>
      </section>

      <!-- FOLDERS -->
      <section id="view-folders" style="display:none;">
        <div class="crumb">Folders<b>Dashboard / Folders</b></div>
        <div class="empty"><div class="big">&#128193;</div>No folders yet. Create folders to organise your accounts.</div>
      </section>

      <!-- INFO -->
      <section id="view-info" style="display:none;">
        <div class="crumb">Info<b>Dashboard / Info</b></div>
        <div class="empty"><div class="big">&#9432;</div>Account info added by your admin appears here.</div>
      </section>

      <!-- SKINS -->
      <section id="view-skins" style="display:none;">
        <div class="crumb">Skins<b>Dashboard / Skins</b></div>
        <?php if(!$allSkins): ?>
          <div class="empty"><div class="big">&#128737;</div>No skins found. Add skins to your accounts in the admin panel.</div>
        <?php else: ?>
          <div class="acc-grid">
            <?php foreach($allSkins as $s): ?>
            <div class="acc-card">
              <div class="thumb"><?php if($s['img']): ?><img src="<?= e($s['img']) ?>" alt="" onerror="this.parentNode.classList.add('noimg')"><?php endif; ?><div class="v-mark" style="font-size:16px;"><?= e($s['tier']) ?></div></div>
              <div class="rowbar"><span class="name"><?= e($s['name']) ?></span><span class="chip"><?= e($s['acc']) ?></span></div>
            </div>
            <?php endforeach; ?>
          </div>
        <?php endif; ?>
      </section>

      <!-- REMINDERS -->
      <section id="view-reminders" style="display:none;">
        <div class="crumb">Reminders<b>Dashboard / Reminders</b></div>
        <div class="empty"><div class="big">&#9203;</div>No reminders set. Set reminders to track your store and missions.</div>
      </section>

      <!-- LEADERBOARDS -->
      <section id="view-leaderboards" style="display:none;">
        <div class="crumb">Leaderboards<b>Dashboard / Leaderboards</b></div>
        <?php if(!$leaderboard): ?>
          <div class="empty"><div class="big">&#127942;</div>No accounts to rank yet.</div>
        <?php else: ?>
        <table class="lb">
          <thead><tr><th>#</th><th>Account</th><th>Level</th><th>Region</th><th>Value</th></tr></thead>
          <tbody>
            <?php $i=1; foreach($leaderboard as $a): ?>
            <tr>
              <td class="rank"><?= $i++ ?></td>
              <td><a class="acc-link" href="account.php?u=<?= urlencode($a['username']) ?>"><span class="name"><?= e($a['name']) ?></span></a></td>
              <td><?= e($a['level']) ?></td>
              <td><?= e(strtoupper($a['region'])) ?></td>
              <td><?= number_format($a['total']) ?></td>
            </tr>
            <?php endforeach; ?>
          </tbody>
        </table>
        <?php endif; ?>
      </section>

    </div>

    <div class="page-footer">
      <div class="copy">2022-2026 &copy; <a href="index.php">EXPLORANT</a> <span style="opacity:.5;margin-left:10px;">&middot; <a href="logout.php">Log out</a></span></div>
      <div>Go to settings to activate Windows.</div>
      <div class="socials">
        <a href="https://discord.gg/w43VMTjJhr" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.3 4.4A19.8 19.8 0 0 0 15.9 3c-.2.4-.5 1-.6 1.4a18 18 0 0 0-5.4 0C9.7 3.9 9.4 3.4 9.2 3a19.8 19.8 0 0 0-4.4 1.4A20.6 20.6 0 0 0 2.1 18.4 19.8 19.8 0 0 0 7.1 20.3c.5-.7.9-1.4 1.3-2.1-.7-.3-1.4-.6-2-1l.5-.4a14 14 0 0 0 12 0l.5.4c-.6.4-1.3.7-2 1 .4.7.8 1.4 1.3 2.1a19.7 19.7 0 0 0 5-1.9A20.6 20.6 0 0 0 20.3 4.4zM8.7 15.7c-1 0-1.8-.9-1.8-2s.8-2 1.8-2 1.8.9 1.8 2-.8 2-1.8 2zm6.6 0c-1 0-1.8-.9-1.8-2s.8-2 1.8-2 1.8.9 1.8 2-.8 2-1.8 2z"/></svg>Discord</a>
        <a href="https://twitter.com/TheExplorant" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 4.9c-.8.4-1.7.6-2.6.8a4.5 4.5 0 0 0-7.7 4.1A12.8 12.8 0 0 1 3.4 4.1a4.5 4.5 0 0 0 1.4 6 4.4 4.4 0 0 1-2-.5 4.5 4.5 0 0 0 3.6 4.4 4.5 4.5 0 0 1-2 .1 4.5 4.5 0 0 0 4.2 3.1A9 9 0 0 1 2 19.1a12.7 12.7 0 0 0 6.9 2c8.3 0 12.8-6.8 12.8-12.8v-.6A9 9 0 0 0 23 4.9z"/></svg>Twitter</a>
        <a href="https://facebook.com/TheExplorant" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12z"/></svg>Facebook</a>
      </div>
    </div>
  </div>
</div>

<!-- Riot credentials modal (shown when an Expired account is opened) -->
<div class="riot-overlay" id="riotOverlay">
  <div class="riot-card">
    <h2>Account Expired</h2>
    <p>This account has expired. Enter your Riot credentials to refresh and open <b id="riotAccName"></b>.</p>
    <form id="riotForm" method="post">
      <div class="fld"><span class="lbl">Riot Username</span><input type="text" name="riotuser" id="riotuser" /><span class="bar"></span></div>
      <div class="fld"><span class="lbl">Riot Password</span><input type="password" name="riotpass" id="riotpass" /><span class="bar"></span></div>
      <div class="foot">
        <button type="button" class="cancel" id="riotCancel">Cancel</button>
        <button type="submit" class="btn-login">OPEN ACCOUNT</button>
      </div>
    </form>
  </div>
</div>

<script>
var ACCOUNTS = <?= json_encode($accounts, JSON_UNESCAPED_SLASHES) ?>;
</script>
<script>
(function(){
  var grid = document.getElementById("accGrid");
  var searchInput = document.getElementById("searchInput");

  function card(a, showTag){
    var tag = a.expired
      ? '<span class="banner-tag expired">Expired</span>'
      : (a.banner ? '<span class="banner-tag">'+a.tag+'</span>' : '');
    var thumb = a.banner
      ? '<img src="'+a.banner+'" alt="" onerror="this.style.display=\'none\';">'
      : '<div class="v-mark">V</div>';
    var meta = '<div class="rowbar"><span class="chk" onclick="event.preventDefault();this.classList.toggle(\'checked\');"></span>' +
      '<span class="name">' + (a.name||a.username) + '</span><span class="menu">&#8942;</span></div>';
    if(a.expired){
      return '<div class="acc-card expired" data-username="' + encodeURIComponent(a.username) + '" data-name="' + String(a.name||a.username).replace(/"/g,'&quot;') + '"' +
        ' data-riot="' + encodeURIComponent(a.riot_user||'') + '" data-riotpass="' + encodeURIComponent(a.riot_pass||'') + '">' +
        '<div class="thumb">' + tag + thumb + '</div>' + meta + '</div>';
    }
    return '<a class="acc-card" href="account.php?u=' + encodeURIComponent(a.username) + '">' +
      '<div class="thumb">' + tag + thumb + '</div>' + meta + '</a>';
  }
  function render(list){
    grid.innerHTML = list.map(function(a){ return card(a); }).join("");
    document.getElementById("countText").textContent = "Viewing items 1-" + list.length + " total items: " + ACCOUNTS.length;
  }
  render(ACCOUNTS);

  if(searchInput){
    searchInput.addEventListener("input", function(e){
      var q = e.target.value.toLowerCase();
      render(ACCOUNTS.filter(function(a){ return (a.name||a.username).toLowerCase().indexOf(q) > -1; }));
    });
  }

  document.querySelectorAll(".side-item").forEach(function(item){
    item.addEventListener("click", function(e){
      e.preventDefault();
      var v = item.getAttribute("data-view");
      document.querySelectorAll(".side-item").forEach(function(x){ x.classList.remove("active"); });
      item.classList.add("active");
      [
        ["home","view-home"],["accounts","view-accounts"],["folders","view-folders"],
        ["info","view-info"],["skins","view-skins"],["reminders","view-reminders"],
        ["leaderboards","view-leaderboards"]
      ].forEach(function(pair){
        var el = document.getElementById(pair[1]);
        if(el) el.style.display = (pair[0] === v) ? "" : "none";
      });
    });
  });

  document.querySelectorAll(".banner .close").forEach(function(btn){
    btn.addEventListener("click", function(){ btn.closest(".banner").style.display = "none"; });
  });

  document.getElementById("slotCount").textContent = Math.max(ACCOUNTS.length, 1);

  /* ---- Riot credentials modal for Expired accounts ---- */
  var overlay = document.getElementById("riotOverlay");
  var openAs = "";
  grid.addEventListener("click", function(e){
    var cardEl = e.target.closest(".acc-card.expired");
    if(!cardEl) return;
    e.preventDefault();
    openAs = decodeURIComponent(cardEl.getAttribute("data-username"));
    document.getElementById("riotAccName").textContent = cardEl.getAttribute("data-name");
    // pre-fill from the stored Riot credentials (fall back to blank)
    document.getElementById("riotuser").value = decodeURIComponent(cardEl.getAttribute("data-riot")||"");
    document.getElementById("riotpass").value = decodeURIComponent(cardEl.getAttribute("data-riotpass")||"");
    overlay.classList.add("show");
    document.getElementById("riotuser").focus();
  });
  document.getElementById("riotCancel").addEventListener("click", function(){
    overlay.classList.remove("show");
  });
  overlay.addEventListener("click", function(e){ if(e.target === overlay) overlay.classList.remove("show"); });
  document.getElementById("riotForm").addEventListener("submit", function(e){
    e.preventDefault();
    if(!openAs) return;
    // Demo: Riot creds are collected here; the stored account then opens.
    overlay.classList.remove("show");
    window.location.href = "account.php?u=" + encodeURIComponent(openAs);
  });
})();
</script>
</body>
</html>
