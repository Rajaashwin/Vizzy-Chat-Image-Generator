# 🚀 Vizzy Chat - Running Instructions

## Current Status: ✅ Backend Running

Your Vizzy Chat backend is **live and ready** on `http://localhost:8000`

### What's Running
- ✅ FastAPI backend server
- ✅ OpenAI API key loaded
- ✅ LLM intent interpretation (GPT-4 turbo)
- ✅ Image generation pipeline (Stable Diffusion via Replicate - using placeholders without API key)
- ✅ Session memory with taste tracking
- ✅ CORS enabled for frontend

---

## Quick Test the API

### Option A: Health Check
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/" -Method GET
```

### Option B: Generate Images with LLM
```powershell
$body = @{
    session_id = "test_session"
    message = "Paint something that feels emotional and dreamy"
    num_images = 3
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://localhost:8000/chat" `
  -Method POST `
  -Body $body `
  -ContentType "application/json" `
  -TimeoutSec 120

$response.Content | ConvertFrom-Json | ConvertTo-Json
```

**Expected Response (excerpt):**
```json
{
  "session_id": "test_session",
  "intent_category": "emotional_art",
  "copy": "Ethereal Emotions - A Visual Journey Through Feeling",
  "images": [
    "https://via.placeholder.com/512x512?text=Demo+Image+1",
    "https://via.placeholder.com/512x512?text=Demo+Image+2",
    "https://via.placeholder.com/512x512?text=Demo+Image+3"
  ]
}
```

---

## Next Step: Frontend Setup

### Option 1: Use Our Web Interface (Requires Node.js)

**Install Node.js:**
Download from https://nodejs.org/ (LTS version recommended)

Then:
```powershell
cd f:\Assessment\vizzy-chat\frontend
npm install
npm run dev
```

Open browser to `http://localhost:5173`

### Option 2: Test Backend Only (No Frontend)

If Node.js isn't available, you can still test the API using curl or PowerShell.

**Example Prompts to Try:**

```powershell
# Home user: Emotional artwork
$body = @{
    session_id = "home_session_1"
    message = "Paint something that feels like how my last year felt"
    num_images = 3
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/chat" `
  -Method POST -Body $body -ContentType "application/json" -TimeoutSec 120 | Select-Object -ExpandProperty Content
```

```powershell
# Business: Product design
$body = @{
    session_id = "business_session_1"
    message = "Create premium-looking visuals for a luxury coffee brand without making it feel expensive"
    num_images = 4
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/chat" `
  -Method POST -Body $body -ContentType "application/json" -TimeoutSec 120 | Select-Object -ExpandProperty Content
```

---

## API Endpoints (Full Reference)

### 1. Chat Endpoint - Generate Images from Text
```
POST /chat
```

**Request:**
```json
{
  "session_id": "optional_or_auto_generated",
  "message": "Describe what you want to create",
  "num_images": 3,
  "refinement": null
}
```

**Response:**
```json
{
  "session_id": "session_123",
  "message": "Generated description",
  "images": ["url1", "url2", "url3"],
  "copy": "AI-generated tagline",
  "intent_category": "detected_intent",
  "conversation_history": [...]
}
```

**Processing Time:** 30-90 seconds (LLM intent + image generation)

---

### 2. Refine Endpoint - Iterate on Results
```
POST /refine
```

**Request:**
```json
{
  "session_id": "session_123",
  "message": "Original prompt here",
  "refinement": "Make it more vibrant with gold accents",
  "num_images": 2
}
```

**Response:** Same as chat endpoint with refined images

---

### 3. Session Retrieval - Get History
```
GET /session/{session_id}
```

**Response:**
```json
{
  "session_id": "session_123",
  "created_at": "2026-02-08T10:30:00",
  "messages": [...],
  "taste": {
    "styles": ["emotional", "dreamy"],
    "colors": [],
    "moods": [],
    "themes": []
  }
}
```

---

## Example User Flows

### For Homes:
1. **Emotional Artwork:** "Paint something that feels like how my last year felt"
   - System interprets as: emotional_art
   - Generates: 3 variations with LLM-enhanced prompts

2. **Photo Reimagination:** "Turn this memory into a renaissance-style artwork"
   - System interprets as: style_transfer
   - Would need photo upload (not in MVP)

3. **Vision Board:** "Create a vision board with my goals for 2026"
   - System interprets as: moodboard
   - Generates: multiple thematic images

### For Businesses:
1. **Product Design:** "Show this luxury product as indulgent but refined"
   - System interprets as: product_design
   - Generates: premium product visuals

2. **Marketing Material:** "Create a sale poster that doesn't feel cheap"
   - System interprets as: poster_design
   - Generates: professional ad visuals

3. **Seasonal Content:** "Design ambiance for rainy summer evenings"
   - System interprets as: ambiance_design
   - Generates: mood-based imagery

---

## Troubleshooting

### Backend Won't Start
```
Error: OPENAI_API_KEY not found
```
**Solution:** Check `.env` file has your API key. Backend should show:
```
OpenAI key available: True
```

### Timeout on Image Generation
Image generation takes 20-90 seconds. That's normal! The system is:
1. Using GPT-4 to interpret your intent (3-5 sec)
2. Generating images with Stable Diffusion (15-60 sec)
3. Creating copy with GPT-3.5 (1-3 sec)

### Images are Placeholders
Without a Replicate API key, images will show placeholder URLs. Get one free: https://replicate.com

To use Replicate, add to `.env`:
```
REPLICATE_API_KEY=r8_xxxxxxxxxxxxx
```

### Can't Install Node.js
You can skip the React frontend and test the API directly via curl/PowerShell. All backend functionality works without the UI.

---

## Architecture

```
User Request
    ↓
FastAPI Endpoint (/chat or /refine)
    ↓
LLM Intent Interpreter (GPT-4)
    ↓
Enhanced Prompt Generation
    ↓
Image API Call (Stable Diffusion/Replicate)
    ↓
Copy Generation (GPT-3.5)
    ↓
Session Memory Update
    ↓
Response with Images + Metadata
```

---

## What's Included ✅

- ✅ Conversational chat interface (backend ready, React frontend)
- ✅ Natural language intent detection
- ✅ Multi-image generation (3-4 variations)
- ✅ Iterative refinement ("make it X" commands)
- ✅ Session memory and taste profile
- ✅ Image export/download
- ✅ Copy generation
- ✅ Error handling and logging
- ✅ Production-ready FastAPI server

---

## What's Not Included ❌

- ❌ Video generation (would need separate model)
- ❌ Photo upload & transformation (needs file pipeline)
- ❌ Persistent database (would need PostgreSQL)
- ❌ User authentication
- ❌ Email/social sharing integration
- ❌ Brand asset management

---

## Next Steps to Extend

1. **Add Real Image Generation:** Get Replicate API key, add to `.env`
2. **Add Photo Upload:** Extend backend with `/upload` endpoint
3. **Add Persistence:** Connect PostgreSQL for user profiles
4. **Add Video:** Integrate Runway or Gen-2 for video generation
5. **Deploy:** Docker → AWS/GCP/Azure

---

## Support

For issues:
1. Check backend logs in terminal
2. Verify `.env` has OpenAI key
3. Test endpoint with curl (timeout = 120 seconds)
4. Check [README.md](./README.md) for detailed documentation

---

**Backend Status: Running on http://localhost:8000** 🎉
