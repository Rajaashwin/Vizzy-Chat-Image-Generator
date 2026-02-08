# Deployment Guide: Vercel (Backend) + GitHub Pages (Frontend)

This guide walks through deploying **Vizzy Chat** as a full-stack app to Vercel (backend) and GitHub Pages (frontend).

## Prerequisites

- GitHub account with your repo: https://github.com/Rajaashwin/Vizzy-Chat-Image-Generator.git
- Vercel account (free) at https://vercel.com
- API keys for:
  - OpenRouter (free tier at https://openrouter.ai)
  - HuggingFace (optional, free at https://huggingface.co)
  - Replicate (optional, at https://replicate.com)

## Step 1: Prepare Local Code

All code changes are ready. Just ensure your `.env` file in `backend/` is NOT committed (it's in `.gitignore`). 

**Create your local `backend/.env`:**
```
OPENROUTER_API_KEY=your_key_here
HUGGINGFACE_API_KEY=your_key_here
REPLICATE_API_KEY=your_key_here
ALLOWED_ORIGINS=*
```

## Step 2: Push to GitHub

From root of repo (`F:\Assessment\vizzy-chat`):

```powershell
git add .
git commit -m "Prepare for Vercel + GitHub Pages deployment: Vercel config, serverless entry point, CORS env var, config-based API base"
git branch -M main
git remote add origin https://github.com/Rajaashwin/Vizzy-Chat-Image-Generator.git
git push -u origin main
```

(Git will prompt for credentials if needed.)

## Step 3: Deploy Backend to Vercel

### 3a. Connect GitHub account to Vercel

1. Go to https://vercel.com/dashboard
2. Click **"Add New..."** → **Project**
3. Select **"Import Git Repository"**
4. Search for `Vizzy-Chat-Image-Generator` and import it

### 3b. Add Environment Variables in Vercel

After import, under **Settings** → **Environment Variables**, add:

| Variable | Value |
|----------|-------|
| `OPENROUTER_API_KEY` | your OpenRouter API key |
| `HUGGINGFACE_API_KEY` | your HuggingFace token (optional) |
| `REPLICATE_API_KEY` | your Replicate token (optional) |
| `ALLOWED_ORIGINS` | (leave as `*` for now, or set to your Pages URL) |

### 3c. Deploy

Vercel auto-deploys on push. Your backend will be live at:
```
https://<your-project-name>.vercel.app
```

**Note:** Get your exact URL from Vercel dashboard. It will look like `https://vizzy-chat-image-generator.vercel.app` or similar.

## Step 4: Update Frontend Config & Deploy to GitHub Pages

### 4a. Update the frontend to point to your Vercel backend

Edit `frontend/src/config.js`:

```javascript
// API Configuration
const isDevelopment = import.meta.env.MODE === 'development';

export const API_BASE_URL = isDevelopment 
  ? 'http://localhost:8000'
  : 'https://<your-vercel-backend-url>.vercel.app';  // <-- Replace this

export const API_ENDPOINTS = {
  chat: `${API_BASE_URL}/chat`,
  session: `${API_BASE_URL}/session`,
};

export default {
  API_BASE_URL,
  API_ENDPOINTS,
};
```

Replace `<your-vercel-backend-url>` with your actual project name from Vercel.

### 4b. Add GitHub Pages homepage to `frontend/package.json`

Edit `frontend/package.json`:

```json
{
  "name": "vizzy-chat-frontend",
  "private": true,
  "version": "0.1.0",
  "homepage": "https://Rajaashwin.github.io/Vizzy-Chat-Image-Generator",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "predeploy": "npm run build",
    "deploy": "gh-pages -d dist",
    "preview": "vite preview"
  },
  ...
}
```

### 4c. Commit, push, and deploy

From `F:\Assessment\vizzy-chat`:

```powershell
git add frontend/src/config.js frontend/package.json
git commit -m "Update frontend: point to Vercel backend, add gh-pages homepage"
git push origin main
```

Then from `frontend/` folder:

```powershell
cd frontend
npm install
npm run build
npm run deploy
```

This will:
1. Build your React app
2. Deploy to `https://Rajaashwin.github.io/Vizzy-Chat-Image-Generator`

### 4d. Enable GitHub Pages

1. Go to your GitHub repo → **Settings** → **Pages**
2. Under "Source", select **Deploy from a branch**
3. Select **branch: `gh-pages`** and save

(The `npm run deploy` command creates/updates the `gh-pages` branch automatically.)

## Step 5: Update Backend CORS for Production

Once your frontend is live on GitHub Pages, set the CORS origin in Vercel:

1. Go to Vercel dashboard → Your project → **Settings** → **Environment Variables**
2. Update `ALLOWED_ORIGINS` to:
   ```
   https://Rajaashwin.github.io/Vizzy-Chat-Image-Generator
   ```
3. Vercel will auto-redeploy with the new env var

## Step 6: Test

1. Visit: `https://Rajaashwin.github.io/Vizzy-Chat-Image-Generator`
2. Type a prompt (e.g., "a sunny forest")
3. Backend should generate images and copy via Vercel
4. Images will use your API keys (HuggingFace, Replicate, OpenRouter)

## Troubleshooting

### Frontend can't reach backend
- Check `frontend/src/config.js` has correct Vercel URL
- Check backend CORS allows your Pages origin

### Backend returns 500 error
- Check Vercel logs: https://vercel.com/dashboard → your project → **Deployments** → **Logs**
- Ensure `OPENROUTER_API_KEY` is set in Vercel env vars

### Images not generating
- Check API key limits (HuggingFace, Replicate, OpenRouter have rate limits)
- Check backend logs for which provider errors occurred

## Quick Links

- GitHub Repo: https://github.com/Rajaashwin/Vizzy-Chat-Image-Generator
- Frontend (GitHub Pages): https://Rajaashwin.github.io/Vizzy-Chat-Image-Generator
- Backend (Vercel): https://<your-project-name>.vercel.app
- Vercel Dashboard: https://vercel.com/dashboard
- GitHub Pages Settings: https://github.com/Rajaashwin/Vizzy-Chat-Image-Generator/settings/pages

---

**Done!** Your app is now live on GitHub Pages (frontend) and Vercel (backend).
