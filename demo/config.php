<?php
/* ============================================================
   Explorant demo — config & storage helpers
   Change ADMIN_PASSWORD to secure the admin panel.
   ============================================================ */
session_start();
date_default_timezone_set('UTC');

define('DATA_FILE', __DIR__ . '/data/users.json');
define('ADMIN_PASSWORD', 'explorant-admin'); // <-- change this!

/* ---- read / write users ---- */
function load_users(){
  if(!file_exists(DATA_FILE)) return [];
  $j = file_get_contents(DATA_FILE);
  $a = json_decode($j, true);
  return is_array($a) ? $a : [];
}
function save_users($users){
  file_put_contents(DATA_FILE, json_encode($users, JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES));
}
function find_user($username){
  foreach(load_users() as $u){ if(strtolower($u['username'])===strtolower($username)) return $u; }
  return null;
}
function is_admin(){ return !empty($_SESSION['is_admin']); }
function current_user(){ return $_SESSION['user'] ?? null; }
function e($s){ return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }

/* ---- safe image url (only allow http(s)) ---- */
function img($u){
  $u = trim((string)$u);
  if($u!=='' && !preg_match('#^https?://#i',$u)) return '';
  return $u;
}
