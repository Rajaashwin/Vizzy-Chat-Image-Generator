# 🚀 Vizzy Chat - Quick Start

## **Run Everything (Pick One)**

### **Option A: PowerShell (Easiest)**
```powershell
# From project root directory
./START_BOTH.ps1
```
Opens both services in new windows:
- Backend: http://localhost:8000
- Frontend: http://localhost:5173

---

### **Option B: Command Prompt (Windows)**
```cmd
# From project root directory  
START_BOTH.bat
```
Opens two CMD windows for backend and frontend.

---

### **Option C: Two Separate Terminals (Manual)**

**Terminal 1 - Backend:**
```powershell
cd backend
.\venv\Scripts\python.exe main.py
```
Runs on `http://localhost:8000`

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm run dev
```
Runs on `http://localhost:5173`

---

## **Access Your App**

| Service | URL |
|---------|-----|
| **Chat App** | http://localhost:5173 |
| **Backend API** | http://localhost:8000 |
| **API Docs** | http://localhost:8000/docs |

---

## **What's Running**

**Backend (FastAPI on 8000):**
- ✅ Text generation via OpenRouter
- ✅ Image generation via HuggingFace
- ✅ Session management
- ✅ Full REST API

**Frontend (Vite + React on 5173):**
- ✅ Chat & Image toggle
- ✅ Model indicator in header
- ✅ Real-time API calls
- ✅ Image gallery

---

## **Stop Services**

- **PowerShell/Batch**: Close the windows or press `Ctrl+C`
- **Manual terminals**: Press `Ctrl+C` in each terminal

---

## **Troubleshooting**

### Backend won't start
```powershell
# Ensure dependencies are installed
cd backend
.\venv\Scripts\pip install -r requirements.txt
```

### Frontend won't start
```powershell
# Install deps if needed
cd frontend
npm install
npm run dev
```

### Port already in use
If port 8000 or 5173 is in use, modify:
- Backend: `backend/main.py` line with `port=8000`
- Frontend: `frontend/vite.config.js` (change port)

---

**Ready to go!** 🎉
