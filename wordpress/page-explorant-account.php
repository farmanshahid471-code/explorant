<?php
/**
 * Template Name: Explorant — Account
 *
 * Full-width custom page template that outputs the account-page clone
 * (Details / Store / Weapon Skins / Battlepasses / Agents / Buddies /
 *  Cards / Sprays / Flexes / Titles / Progressions) with NO theme chrome.
 *
 * How to use:
 *   1. Also upload `explorant-account.html` next to this file.
 *   2. In WP Admin → Pages → Add New → Template → "Explorant — Account".
 *   3. Publish.
 *
 * Note: fully custom design → we skip get_header()/get_footer() and
 * wp_head()/wp_footer() so the activated theme's CSS/JS can't override it.
 * (If you need WP's admin-bar or plugin scripts here, add a `wp_head();`
 *  call and dequeue the theme's styles instead.)
 */

readfile(__DIR__ . '/explorant-account.html');
