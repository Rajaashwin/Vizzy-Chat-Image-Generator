@echo off
REM Vizzy Chat - Start Backend + Frontend
REM Usage: START_BOTH.bat

echo.
echo ========================================
echo   Vizzy Chat - Starting Services
echo ========================================
echo.

cd /d "%~dp0"

REM Start Backend
echo [1/2] Starting Backend (http://localhost:8000)...
start "Vizzy Backend" cmd /k "cd backend && venv\Scripts\python.exe main.py"

REM Wait for backend to start
timeout /t 3 /nobreak

REM Start Frontend
echo [2/2] Starting Frontend (http://localhost:5173)...
start "Vizzy Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo   Both services running!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo API Docs: http://localhost:8000/docs
echo.
echo Close these windows to stop services.
echo.

pause
