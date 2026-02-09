# 🚀 Quick Start Guide - Vizzy Chat

## ⚡ TL;DR - Run Everything in One Command

### Windows

**PowerShell:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser -Force
.\START_BOTH.ps1
```

**Command Prompt:**
```cmd
START_BOTH.bat
```

Both services will start in separate terminals:
- **Frontend:** http://localhost:5173
- **Backend:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

---

## 📋 Prerequisites

- **Python 3.11+** (check: `python --version`)
- **Node.js 18+** (check: `npm --version`)
- **Git** (check: `git --version`)

### API Keys (Required for Features)

You'll need three free API keys. Get them in ~5 minutes:

1. **OpenRouter** (Text Generation)
   - Visit: https://openrouter.ai/keys
   - Create free account → Copy API key
   - Free: $5 monthly credits (enough for testing)

2. **HuggingFace** (Image Generation)
   - Visit: https://huggingface.co/settings/tokens
   - Create new token (read only is fine)
   - Free: Unlimited API calls

3. **Replicate** (Optional - Backup Image Source)
   - Visit: https://replicate.com/account/api-tokens
   - Create token
   - Free: $5 startup credits

---

## 🎯 Step 1: Setup (First Time Only)

```bash
# Clone the repo
git clone https://github.com/ashwin-rajakannan/vizzy-chat.git
cd vizzy-chat

# Setup Backend
cd backend
python -m venv venv
.\venv\Scripts\activate    # Windows PowerShell
# OR
venv\Scripts\activate.bat  # Windows Command Prompt

pip install -r requirements.txt

# Create .env file with your API keys
# Copy this and save as backend/.env:
# ---
# OPENROUTER_API_KEY=sk-or-v1-...your_key_here...
# HUGGINGFACE_API_KEY=hf_...your_token_here...
# REPLICATE_API_KEY=r8_...optional...
# ---

cd ..

# Setup Frontend
cd frontend
npm install
cd ..
```

---

## 🚀 Step 2: Run Everything

From the project root (`vizzy-chat/` directory):

### Option A: PowerShell (Recommended)
```powershell
.\START_BOTH.ps1
```

### Option B: Command Prompt
```cmd
START_BOTH.bat
```

### Option C: Manual (Two Terminals)

**Terminal 1 - Backend:**
```bash
cd backend
.\venv\Scripts\activate  # Windows
python main.py
# Output: INFO: Uvicorn running on http://0.0.0.0:8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
# Output: VITE v... ready in ... ms
#         Local: http://localhost:5173/
```

---

## ✅ Verify It's Working

1. **Frontend loads:**
   - Open http://localhost:5173
   - Should see the Vizzy Chat interface with Chat/Image buttons

2. **Backend responds:**
   - Open http://localhost:8000/docs
   - Should see FastAPI Swagger UI with `/chat` endpoint

3. **API keys are loaded:**
   - Send a test message in the frontend
   - Should see a real response (not a placeholder)
   - Check backend console for: `OpenRouter API configured: True`

---

## 🎨 Test the Features

### Chat Mode
1. Click "Chat" button (left in header)
2. Type a message: `"What is the meaning of life?"`
3. Should get AI response from OpenRouter

### Image Generation
1. Click "Image" button (right in header)
2. Type a prompt: `"A mystical forest with glowing mushrooms"`
3. Should see:
   - Generated image from HuggingFace, OR
   - Colorful SVG placeholder if API is slow

### Session Persistence
- Refresh the page — your conversation history loads from backend
- New browser tab with same session ID — history shared

---

## 🌐 Deploy to Production

### Frontend to GitHub Pages (Already Deployed)
```bash
npm run deploy
```
Automatically builds and publishes to: https://Rajaashwin.github.io/Vizzy-Chat-Image-Generator

### Backend to Railway (Already Deployed)
Your backend is live at: https://web-production-d4489.up.railway.app

To update with new code:
```bash
# Railway auto-deploys on git push
git add .
git commit -m "Your message"
git push origin main
```

---

## 🔧 Troubleshooting

### "Command not found: python"
- Make sure Python 3.11+ is installed
- Try: `python3 --version`

### "port 8000 already in use"
- Kill existing process: `taskkill /PID <pid> /F`
- Or use a different port: `python main.py --port 8001`

### "npm: command not found"
- Install Node.js from https://nodejs.org/
- Restart your terminal

### "venv: command not found"
- Make sure you're in the `backend/` directory
- Try: `python -m venv venv` (instead of just `venv`)

### API calls return placeholder images
- Check `.env` file exists in `backend/` with valid keys
- Check backend console for `OpenRouter API configured: True`
- HuggingFace might be slow (~10-30 sec) — wait for response

---

## 📚 More Info

- **Full Deployment Guide:** [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **Architecture & Features:** [README.md](README.md)
- **Live Demo:** https://Rajaashwin.github.io/Vizzy-Chat-Image-Generator

---

## 🎓 What's Happening Under the Hood

```
User Opens http://localhost:5173
    ↓
Frontend (React + Vite) loads
    ↓
User sends message
    ↓
Frontend calls API: POST http://localhost:8000/chat
    ↓
Backend (FastAPI) receives request
    ↓
Backend calls OpenRouter API (text) & HuggingFace API (images)
    ↓
Backend returns: {message, images, session_id}
    ↓
Frontend displays response with images
```

---

**Need help?** Check the GitHub repo: https://github.com/ashwin-rajakannan/vizzy-chat
