# 🚀 Quick Start: Run Everything in One Command

## Option 1: Double-Click (Easiest) ⭐
**Windows Users:** Simply double-click `start-all.bat` in the `vizzy-chat` folder.
- Opens two terminal windows: Backend and Frontend
- No setup needed!
- Close the windows to stop services

---

## Option 2: PowerShell Command
Open PowerShell and run:
```powershell
cd f:\Assessment\vizzy-chat
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\start-all.ps1
```

---

## What Happens
- ✅ Backend starts on `http://localhost:8000` (FastAPI + Uvicorn)
- ✅ Frontend starts on `http://localhost:5173` (React + Vite)
- ✅ Opens automatically in your default browser
- ✅ Both services are live and connected

---

## First Time Setup
If this is your first time running:
1. Make sure Node.js is installed: [Download here](https://nodejs.org/)
2. Make sure Python 3.9+ is installed
3. Backend virtual environment should already exist

If backend venv is missing, run once:
```powershell
cd f:\Assessment\vizzy-chat\backend
python -m venv venv
pip install -r requirements.txt
```

---

## Verify Everything Works
After both services start:
1. Open browser to `http://localhost:5173` (Frontend)
2. Type a message like "Paint something dreamy"
3. Watch the magic happen! ✨

Backend health check:
```powershell
curl http://localhost:8000/
```
(Should return JSON with app info)

---

## Troubleshooting

**Issue:** "npm: command not found"
- **Fix:** Install Node.js from https://nodejs.org/

**Issue:** "python: command not found"
- **Fix:** Add Python to PATH or use full path to python.exe

**Issue:** Port 8000 already in use
- **Fix:** Run PowerShell version with custom port:
  ```powershell
  .\start-all.ps1 -BackendPort 8001
  ```

**Issue:** Backend won't start
- **Check:** Virtual environment exists at `backend/venv/Scripts/python.exe`
- **Fix:** Run setup command above

---

## Manual Run (If scripts don't work)

**Terminal 1 - Backend:**
```powershell
cd f:\Assessment\vizzy-chat\backend
.\venv\Scripts\Activate.ps1
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Terminal 2 - Frontend:**
```powershell
cd f:\Assessment\vizzy-chat\frontend
npm run dev
```

---

## 🎯 Default Ports
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`

Both can be customized in the start scripts if needed.

---

**That's it! One command to rule them all.** 🚀
