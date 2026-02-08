# 🎯 QUICK START GUIDE

## ✅ Current Status: BOTH SERVERS RUNNING

### Access Points

| Service | URL |
|---------|-----|
| 🎨 **Frontend** | http://localhost:5173 |
| 🔌 **Backend API** | http://localhost:8000 |
| 📖 **API Docs** | http://localhost:8000/docs |

---

## 🚀 To Restart Everything

### Option 1: PowerShell Script (Recommended)
```powershell
cd f:\Assessment\vizzy-chat
.\start-all.ps1
```

### Option 2: Manual - Terminal 1 (Backend)
```powershell
cd f:\Assessment\vizzy-chat\backend
python main.py
```

### Option 2: Manual - Terminal 2 (Frontend)
```powershell
cd f:\Assessment\vizzy-chat\frontend
npm run dev
```

---

## 🧪 Test the System

### Quick Integration Test
```powershell
cd f:\Assessment\vizzy-chat
python integration_test.py
```

### Test Single Endpoint
```powershell
cd f:\Assessment\vizzy-chat\backend
python quick_test.py
```

### Test Backend Only
```powershell
cd f:\Assessment\vizzy-chat\backend
python test_openrouter.py
```

---

## 📝 Example API Calls

### 1. Chat (Text Only)
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Create a beautiful sunset landscape",
    "num_images": 0
  }'
```

### 2. Chat with Images
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Create a beautiful sunset landscape", 
    "num_images": 3
  }'
```

### 3. Get Session History
```bash
curl http://localhost:8000/session/{SESSION_ID}
```

### 4. View API Documentation
Open: http://localhost:8000/docs

---

## ⚙️ Configuration Files

### Backend (.env)
Location: `f:\Assessment\vizzy-chat\backend\.env`

```env
REPLICATE_API_KEY=        # Optional, for image generation
HUGGINGFACE_API_KEY=...   # Backup (deprecated)
OPENROUTER_API_KEY=sk-or-v1-...  # Primary LLM provider
```

### Frontend (vite.config.js)
Location: `f:\Assessment\vizzy-chat\frontend\vite.config.js`

Default backend URL: `http://localhost:8000`

---

## 🔧 Environment Info

| Item | Value |
|------|-------|
| Python | 3.12+ |
| Node.js | 14+ |
| Backend Port | 8000 |
| Frontend Port | 5173 |
| LLM Provider | OpenRouter (Mistral) |
| Storage | In-memory sessions |

---

## ✨ Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| GET | `/docs` | Swagger UI |
| POST | `/chat` | Send message, get response |
| GET | `/session/{id}` | Get session history |

---

## 🐛 Troubleshooting

### Backend Won't Start
```powershell
# Check if port 8000 is in use
Get-NetTCPConnection -LocalPort 8000

# Kill existing process
Stop-Process -Name python -Force
```

### Frontend Won't Start
```powershell
# Update execution policy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Clear npm cache
npm cache clean --force

# Reinstall dependencies
cd frontend && npm install
```

### API Calls Failing
- ✅ Check http://localhost:8000 is accessible
- ✅ Verify OPENROUTER_API_KEY is set in .env
- ✅ Check backend logs for errors
- ✅ Try test: `python quick_test.py`

---

## 📊 Test Results

```
Integration Test Results: 5/5 PASSED ✅

✓ Backend Service
✓ Frontend Service  
✓ Chat Endpoint
✓ Session Management
✓ OpenRouter Integration

FULL STACK IS OPERATIONAL!
```

---

## 🎉 You're All Set!

Everything is configured and running. Simply:
1. Open http://localhost:5173 in your browser
2. Start chatting!
3. Request images by setting num_images > 0

Enjoy Vizzy Chat! 🚀
