#!/usr/bin/env bash
# ============================================================
# Explorant demo — local dev server
# Usage:  ./start.sh     (or)   skip "start.sh" and run:
#         php -S localhost:8090
# Then open http://localhost:8090/login.php
# ============================================================
cd "$(dirname "$0")"
echo "Starting Explorant demo on http://localhost:8090  (Ctrl+C to stop)"
echo "  Login:  vakking22@gmail.com / vakking22@@"
echo "  Admin:  open /admin.php   (password in config.php)"
exec php -S localhost:8090
