@echo off
REM ============================================================
REM  Explorant demo - start on Windows (no Apache needed)
REM  Uses the PHP bundled with XAMPP, or PHP on PATH.
REM  Double-click this file (or run it from Cmd).
REM ============================================================
cd /d "%~dp0"

set PHPEXE=php
where php >nul 2>nul
if errorlevel 1 (
  if exist "C:\xampp\php\php.exe" set PHPEXE=C:\xampp\php\php.exe
)

echo Starting Explorant demo on http://localhost:8090   (Ctrl+C to stop)
echo   Login:  vakking22@gmail.com / vakking22@@
echo   Admin:  http://localhost:8090/admin.php  (password in config.php)
echo.
%PHPEXE% -S localhost:8090
pause
