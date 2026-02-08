@echo off
REM Run backend using the correct venv Python
cd /d "%~dp0backend"
.\venv\Scripts\python.exe main.py %*
pause
