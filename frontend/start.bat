@echo off
echo ============================================================
echo Installing Frontend Dependencies
echo ============================================================
cd /d f:\Assessment\vizzy-chat\frontend
call npm install

echo.
echo ============================================================
echo Starting Development Server
echo ============================================================
echo Open browser to: http://localhost:5173
echo.
call npm run dev
pause
