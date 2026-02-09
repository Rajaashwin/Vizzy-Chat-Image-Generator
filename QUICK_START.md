# 🚀 Quick Start Guide - Vizzy Chat

## ⚡ TL;DR - Run Everything in One Command

```bash
node start.js
```

Or using npm:
```bash
npm start
npm run dev
npm run dev:all
```

Both services will start automatically:
- **Frontend:** http://localhost:5173/vizzy-chat/
- **Backend:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- Stop with: **Ctrl+C**

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

That's it! Just run one command from the project root (`vizzy-chat/`):

```bash
node start.js
```

Or equivalently:
```bash
npm start
npm run dev
npm run dev:all
```

Both services start in the same terminal with live logs. Press **Ctrl+C** to stop.

---

## ✅ Verify It's Working

1. **Frontend loads:**
   - Open http://localhost:5173/vizzy-chat/
   - Should see the Vizzy Chat interface with Chat/Image buttons

2. **Backend responds:**
   - Open http://localhost:8000/docs
   - Should see FastAPI Swagger UI with `/chat` endpoint

3. **API keys are loaded (check backend logs):**
   ```
   OpenRouter API configured: True
   Replicate key available: True
   ```
   If you see `False`, check that `backend/.env` has valid keys.

---

## 🎨 Test the Features

### Chat Mode
1. Click "Chat" button in the header
2. Type: `"What is the meaning of life?"`
3. Should get real AI response from OpenRouter

### Image Generation
1. Click "Image" button in the header
2. Type: `"A mystical forest with glowing mushrooms"`
3. Should see real generated image or colorful SVG fallback

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
