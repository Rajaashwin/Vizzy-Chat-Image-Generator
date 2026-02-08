@echo off
REM Vizzy Chat - Start Backend + Frontend (Windows Batch Wrapper)
REM Double-click this file to start both services

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════╗
echo ║  Vizzy Chat - Starting Backend ^+ Frontend     ║
echo ╚════════════════════════════════════════════════╝
echo.

REM Get script directory
set SCRIPT_DIR=%~dp0
set BACKEND_DIR=%SCRIPT_DIR%backend
set FRONTEND_DIR=%SCRIPT_DIR%frontend
set VENV_PYTHON=%BACKEND_DIR%\venv\Scripts\python.exe

REM Check if venv exists
if not exist "%VENV_PYTHON%" (
    color cf
    echo ❌ Error: Virtual environment not found
    echo    Expected at: %VENV_PYTHON%
    echo.
    echo Please create the virtual environment first:
    echo   cd %BACKEND_DIR%
    echo   python -m venv venv
    echo.
    pause
    exit /b 1
)

REM Check if node_modules exists, install if missing
if not exist "%FRONTEND_DIR%\node_modules" (
    echo ⚠️  Installing frontend dependencies...
    cd /d "%FRONTEND_DIR%"
    call npm install
    if errorlevel 1 (
        echo ❌ npm install failed
        pause
        exit /b 1
    )
)

echo 🚀 Starting Backend on port 8000...
cd /d "%BACKEND_DIR%"
start "Vizzy Chat - Backend" cmd /k "%VENV_PYTHON% -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

echo ⏳ Waiting for backend to start...
timeout /t 3 /nobreak

echo 🚀 Starting Frontend on port 5173...
cd /d "%FRONTEND_DIR%"
start "Vizzy Chat - Frontend" cmd /k "npm run dev"

echo.
echo ╔════════════════════════════════════════════════╗
echo ║         🎉 Vizzy Chat is Starting!           ║
echo ╚════════════════════════════════════════════════╝
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo 📝 Two terminal windows will open.
echo 📝 Close either window to stop that service.
echo 📝 Close both to fully shut down Vizzy Chat.
echo.
pause
