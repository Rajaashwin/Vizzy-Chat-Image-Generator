# 📦 INTERVIEW DEPLOYMENT - Quick Steps

**⏱️ 5-10 minutes to get live demo running**

---

## **STEP 1: Push to GitHub** (2 minutes)

```powershell
cd f:\Assessment\vizzy-chat

git remote add origin https://github.com/ashwin-rajakannan/vizzy-chat.git
git branch -M main
git push -u origin main
```

✅ Your code is now on GitHub!

---

## **STEP 2: Deploy Backend to Railway** (5 minutes)

```powershell
# Install Railway CLI
npm i -g @railway/cli

# Login with GitHub
railway login

# Go to backend directory
cd backend

# Create Railway project
railway init
railway up

# Get your Railway URL (it will show in console)
# Example: https://vizzy-backend.railway.app
```

💾 **IMPORTANT:** Note your Railway URL (you'll need it in Step 4)

---

## **STEP 3: Deploy Frontend to GitHub Pages** (3 minutes)

```powershell
# Go to frontend
cd ..\frontend

# Install gh-pages
npm install --save-dev gh-pages

# Build and deploy
npm run build
npx gh-pages -d dist
```

✅ Frontend deployed! Watch GitHub -> Settings -> Pages for confirmation

---

## **STEP 4: Update Backend URL**

Update `frontend/src/config.js` with your Railway URL:

```javascript
// Change this line:
export const API_BASE_URL = 'https://YOUR-RAILWAY-URL.railway.app';

// Example:
export const API_BASE_URL = 'https://vizzy-backend.railway.app';
```

Then redeploy:
```powershell
npm run build
npx gh-pages -d dist
```

✅ Frontend now points to your deployed backend!

---

## **FINAL: Your Live Demo URLs**

| What | URL |
|------|-----|
| **Show This to Interviewer** | https://ashwin-rajakannan.github.io/vizzy-chat/ |
| **API Docs (Optional)** | https://your-railway-url.railway.app/docs |

---

## **What Happens When They Click "Image" Button?**

1. Frontend sends request to YOUR backend on Railway
2. Backend calls HuggingFace API to generate image
3. Image appears in ~8-10 seconds
4. If HuggingFace fails, shows colored SVG placeholder

---

## **What to Tell Interviewer**

### About the Project
- "Dual-mode AI system with chat and image generation"
- "Uses OpenRouter for free tier text generation"
- "HuggingFace free inference for image generation"
- "Graceful fallback system with SVG placeholders"

### About the Architecture
- "Frontend on GitHub Pages (free), backend on Railway ($5/mo credits)"
- "FastAPI for async Python backend, React for responsive frontend"
- "Session-based conversation history, smart prompt enhancement"

### About the Tech
- "Integrated two different APIs with intelligent fallback"
- "Handles production concerns: CORS, error handling, rate limiting"
- "Deployed to real cloud platforms for scalability"

---

## **Troubleshooting**

### "Backend returning 404"
- Check Railway is still running (go to railway.app dashboard)
- Verify API key is in Railway environment variables

### "Images look like SVG placeholders"
- Normal! HuggingFace free tier works, but can be slow
- Wait 10-15 seconds, try again
- Or show the API docs to prove real requests are being made

### "Frontend showing old version"
- Hard refresh: Ctrl+Shift+R (Windows)
- Clear browser cache
- Wait 5 minutes for GitHub Pages to update

---

## **Nice-to-Know Commands**

```bash
# Check if backend is running
curl https://your-railway-url.railway.app/docs

# See Railway logs
railway logs

# Stop Railway app
railway down
```

---

**You're ready! 🚀 Go impress them!**
