# 🚀 Vizzy Chat - Deployment Guide for Interview

This guide helps you deploy Vizzy Chat to GitHub Pages + Railway for a live demo.

---

## **Architecture**

```
┌─────────────────────────────────────────┐
│     Frontend (GitHub Pages)             │
│  https://ashwin-rajakannan.github.io/   │
│           vizzy-chat/                   │
└──────────────┬──────────────────────────┘
               │ API Calls
               ▼
┌─────────────────────────────────────────┐
│     Backend (Railway.app)               │
│  https://vizzy-backend.railway.app/     │
│  FastAPI + OpenRouter + HuggingFace     │
└─────────────────────────────────────────┘
```

---

## **Step 1: Setup Backend Environment Variables**

Create `.env` file in `backend/` directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
REPLICATE_API_KEY=your_replicate_api_key_here
```

**Note:** Keep these keys secure! Add them to your `.env` file locally.

---

## **Step 2: Push to GitHub**

```bash
# Add your remote (if not already added)
git remote add origin https://github.com/ashwin-rajakannan/vizzy-chat.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## **Step 3: Deploy Backend to Railway**

### **Option A: Using Railway CLI (Fastest)**

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway (creates account if needed)
railway login

# Link to your project
cd backend
railway init
railway up

# Get your Railway URL
railway open
```

### **Option B: Manual Railway Deployment**

1. Go to https://railway.app
2. Sign up with GitHub
3. Create new project → "Deploy from GitHub"
4. Select your `vizzy-chat` repo
5. Configure:
   - **Root Directory:** `backend`
   - **Environment Variables:** Add your API keys from `.env`

---

## **Step 4: Deploy Frontend to GitHub Pages**

```bash
# Install gh-pages
cd frontend
npm install --save-dev gh-pages

# Build for production
npm run build

# Deploy to GitHub Pages
npx gh-pages -d dist
```

Or add to `package.json` scripts:
```json
{
  "scripts": {
    "build": "vite build",
    "deploy": "gh-pages -d dist"
  }
}
```

Then run:
```bash
npm run deploy
```

---

## **Step 5: Configure GitHub Pages**

1. Go to GitHub repo Settings
2. Pages section → Select:
   - **Source:** Deploy from branch
   - **Branch:** `gh-pages` (auto-created)
   - **Folder:** `/ (root)`
3. Save

Your site will be at: `https://ashwin-rajakannan.github.io/vizzy-chat/`

---

## **Step 6: Update Backend URL in Frontend**

After deploying backend to Railway:

1. Get your Railway domain (e.g., `https://vizzy-backend.railway.app`)
2. Update `frontend/src/config.js`:

```javascript
export const API_BASE_URL = 'https://vizzy-backend.railway.app';
```

3. Rebuild and redeploy frontend:
```bash
npm run build
npm run deploy
```

---

## **Live Demo URLs (After Deployment)**

| Service | URL |
|---------|-----|
| **Frontend Demo** | https://ashwin-rajakannan.github.io/vizzy-chat/ |
| **Backend API** | https://vizzy-backend.railway.app/ |
| **API Docs** | https://vizzy-backend.railway.app/docs |

---

## **Features to Showcase**

### **Chat Mode**
- ✅ Text generation via OpenRouter
- ✅ Session management
- ✅ Real-time API responses

### **Image Mode**
- ✅ AI image generation via HuggingFace
- ✅ High-quality Stable Diffusion XL
- ✅ Base64 image rendering

### **Technical Highlights**
- ✅ Dual-mode intelligent system
- ✅ Graceful fallbacks (SVG placeholders)
- ✅ CORS-enabled FastAPI backend
- ✅ Production-ready deployment

---

## **Troubleshooting**

### Backend Won't Deploy
```bash
# Check logs in Railway dashboard
# Ensure all requirements installed:
cd backend
pip install -r requirements.txt
```

### Frontend Shows 404
```bash
# Ensure vite.config.js has correct base:
base: '/vizzy-chat/'
```

### API Not Responding
1. Check backend is running: `https://vizzy-backend.railway.app/docs`
2. Verify CORS is enabled (it is in main.py)
3. Check environment variables in Railway dashboard

### Images Not Generating
Verify HuggingFace token is valid:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  https://huggingface.co/api/user
```

---

## **Interview Talking Points**

1. **Architecture:** Explain frontend/backend separation and deployment strategy
2. **APIs:** Demo text via OpenRouter, images via HuggingFace
3. **Scalability:** Can handle multiple concurrent users with session management
4. **Reliability:** Graceful fallbacks when services unavailable
5. **Cost:** All free tier services (OpenRouter free, HuggingFace free, Railway $5/month)

---

## **Quick Commands**

```bash
# Local development
./START_BOTH.ps1

# Build frontend
cd frontend && npm run build

# Deploy frontend to GitHub Pages
npm run deploy

# Check backend status
curl https://vizzy-backend.railway.app/docs
```

---

**Good luck with your interview! 🚀**
