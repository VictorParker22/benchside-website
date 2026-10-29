@echo off
rem Deploys this folder to the Vercel project "benchside-site" (preview site, not benchside.coach).
rem First run opens your browser to sign in to Vercel.
cd /d "%~dp0"
where node >nul 2>nul || (echo Node.js is needed: https://nodejs.org & pause & exit /b 1)
call npx --yes vercel@latest deploy --prod --yes
echo.
echo Done. The link above is your Benchside preview.
pause
