<?php
/**
 * Template Name: Explorant — Home
 *
 * Full-width custom page template that outputs the exact Explorant home
 * design with NO theme header / footer / sidebars, so it looks identical
 * to the linked site.
 *
 * How to use:
 *   1. Upload this file AND `explorant-home.html` into your active theme's
 *      folder (or a child theme), e.g. /wp-content/themes/your-theme/
 *   2. In WP Admin → Pages → Add New → in the "Template" dropdown choose
 *      "Explorant — Home".
 *   3. Publish. The page renders your custom HTML only.
 *
 * Note: because this is a fully custom design, we intentionally skip
 * get_header()/get_footer() and wp_head()/wp_footer() so the theme's own
 * styles/scripts don't override the design.
 */

readfile(__DIR__ . '/explorant-home.html');
