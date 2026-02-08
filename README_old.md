# Vizzy Chat - AI Art & Content Generator

A conversational AI chat interface that interprets natural-language creative requests, generates multi-image variations, and allows iterative refinement. Built with **FastAPI** (Python backend) and **React + Vite** (frontend).

## Features

✅ **Conversational Interface** - ChatGPT-like chat UI  
✅ **Intent Interpretation** - LLM-powered request understanding  
✅ **Multi-Image Generation** - Generate 3 variations per prompt  
✅ **Iterative Refinement** - "Make it more vibrant" style commands  
✅ **Session Memory** - Remembers user taste within a session  
✅ **Image Export** - Download generated images  
✅ **Copy Generation** - AI-generated descriptions & taglines  

## What's Possible in This Prototype

| Feature | Status | Notes |
|---------|--------|-------|
| Chat UI + messaging | ✅ Ready | Full ChatGPT-like experience |
| Natural-language intent detection | ✅ Ready | LLM-powered prompt interpretation |
| Multi-image generation | ✅ Ready | 3 variations per prompt |
| Refinement loop | ✅ Ready | Iterative "make it X" commands |
| Session memory | ✅ Ready | Ephemeral taste profile |
| Image download | ✅ Ready | Direct download to device |
| Copy/tagline generation | ✅ Ready | AI-written descriptions |
| Brand asset upload | ⏳ Partial | Basic file support (backend ready) |
| Simple RAG/vector memory | ⏳ Partial | Framework in place; needs DB |
| Video generation | ❌ Not included | Requires separate video model pipeline |
| Persistent user profiles | ❌ Not included | Would need auth + database |
| Email/social sharing | ❌ Stub only | Frontend ready; backend integration needed |

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- OpenAI API key (for LLM features)
- (Optional) Replicate API key (for higher-quality images; uses placeholders without it)

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your keys
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

**Environment Variables:**
```
OPENAI_API_KEY=sk-...                    # Required for LLM
REPLICATE_API_KEY=r8_...                 # Optional (uses placeholders without it)
```

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

### 3. Run the Application

**Terminal 1 - Start Backend:**
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python main.py
```

Backend runs on `http://localhost:8000`

**Terminal 2 - Start Frontend:**
```bash
cd frontend
npm run dev
```

Frontend runs on `http://localhost:5173`

### 4. Open in Browser

Navigate to `http://localhost:5173`

## API Endpoints

### `POST /chat`
Send a message and get generated images.

**Request:**
```json
{
  "session_id": "optional_session_id",
  "message": "Paint something that feels emotional",
  "num_images": 3,
  "refinement": null
}
```

**Response:**
```json
{
  "session_id": "session_123",
  "message": "A dreamy, abstract landscape...",
  "images": ["url1", "url2", "url3"],
  "copy": "Emotional Journey - Abstract Dreams",
  "intent_category": "emotional_art",
  "conversation_history": [...]
}
```

### `POST /refine`
Refine/iterate on previous generation.

**Request:**
```json
{
  "session_id": "session_123",
  "message": "Paint something that feels emotional",
  "refinement": "Make it more vibrant and golden",
  "num_images": 3
}
```

### `GET /session/{session_id}`
Retrieve full session history and taste profile.

### `GET /`
Health check and endpoint list.

## Example Prompts

**For Homes:**
- "Paint something that feels like how my last year felt."
- "Turn this photo into a renaissance-style artwork."
- "Create a dreamlike version of this memory."
- "Make a vision board with my goals for the next 3 years."
- "Help me design a quote poster for my living room."
- "Show me my inner emotional landscape right now."

**For Businesses:**
- "Create premium-looking visuals for this product without making it feel expensive."
- "Design a seasonal ambiance for evenings."
- "Generate signage for a slow-moving item."
- "Show this dish as indulgent but refined."
- "Create a memento artwork for a couple celebrating their anniversary."
- "Design in-store visuals for rainy days."

## Tech Stack

- **Backend**: FastAPI, OpenAI API, Replicate API
- **Frontend**: React 18, Vite, Axios
- **Storage**: Ephemeral (in-memory sessions)
- **LLM**: GPT-4 / GPT-3.5 for intent & copy
- **Images**: Stable Diffusion (via Replicate or OpenAI Images)

## File Structure

```
vizzy-chat/
├── backend/
│   ├── main.py              # FastAPI app, endpoints, LLM + image integration
│   ├── requirements.txt
│   └── .env.example
│
└── frontend/
    ├── src/
    │   ├── App.jsx          # Main chat component
    │   ├── App.css
    │   ├── index.css
    │   └── components/
    │       ├── ChatMessage.jsx    # Message display + image gallery
    │       ├── ImageGallery.jsx   # Image selection + refinement
    │       └── InputBar.jsx       # Chat input
    ├── index.html
    ├── vite.config.js
    └── package.json
```

## Next Steps (Not Included in MVP)

1. **Persistent Storage**: Add PostgreSQL + auth for multi-session support
2. **Brand Assets**: Implement file upload + vector embedding for RAG
3. **Video Generation**: Integrate video models (Runway, Gen-2, etc.)
4. **Export Options**: Email, social sharing, cloud storage
5. **Advanced Memory**: Long-term taste learning, campaign history
6. **Deployment**: Docker, Kubernetes, CI/CD pipeline
7. **Enterprise Features**: Multi-user, billing, analytics

## Troubleshooting

**"Connection refused" error?**
- Ensure backend is running on `http://localhost:8000`
- Check that port 8000 is not in use: `lsof -i :8000` (macOS/Linux) or `netstat -ano | findstr :8000` (Windows)

**Images are placeholders?**
- Add a Replicate or OpenAI Images API key to `.env`
- Without a key, the backend returns placeholder images for demo purposes

**CORS errors?**
- Backend has CORS enabled for all origins (dev mode)
- For production, restrict origins in `main.py`

**GPU acceleration?**
- Images run on Replicate's servers (no GPU needed locally)
- For on-device inference, use `diffusers` library + CUDA

## Performance Notes

- Image generation: 20-60 seconds per image (Stable Diffusion)
- LLM inference: 1-5 seconds
- Session memory is in-memory (lost on server restart)

## License

MIT - Free to use and modify

---

**Built for the Deckoviz Internship Challenge** 🚀
