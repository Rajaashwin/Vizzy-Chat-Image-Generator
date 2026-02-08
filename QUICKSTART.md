# Quick Start Without Node.js

If you don't have Node.js installed, you can still test the backend API directly using curl or Python.

## Option 1: Test Backend with curl (PowerShell)

```powershell
# Test the chat endpoint
$body = @{
    session_id = "test_session"
    message = "Create a dreamy landscape"
    num_images = 3
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/chat" `
  -Method POST `
  -Body $body `
  -ContentType "application/json"
```

## Option 2: Test with Python requests

```python
import requests
import json

url = "http://localhost:8000/chat"
payload = {
    "session_id": "test_session",
    "message": "Paint something emotional",
    "num_images": 3
}

response = requests.post(url, json=payload)
print(json.dumps(response.json(), indent=2))
```

## Option 3: Install Node.js (Recommended)

Download and install Node.js from: https://nodejs.org/

Then run:
```powershell
cd f:\Assessment\vizzy-chat\frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Testing the API

You can test the backend API endpoints using any HTTP client:

### Health Check
```
GET http://localhost:8000/
```

### Chat with Image Generation
```
POST http://localhost:8000/chat
Content-Type: application/json

{
  "session_id": "test_session",
  "message": "Create a Renaissance-style painting of a forest",
  "num_images": 3
}
```

### Refine/Iterate
```
POST http://localhost:8000/refine
Content-Type: application/json

{
  "session_id": "test_session",
  "message": "Create a Renaissance-style painting of a forest",
  "refinement": "Make it more dramatic with golden lighting",
  "num_images": 3
}
```

### Get Session History
```
GET http://localhost:8000/session/test_session
```

## Expected Response

```json
{
  "session_id": "test_session",
  "message": "A dreamy, ethereal landscape with soft colors and surreal elements.",
  "images": [
    "https://via.placeholder.com/512x512?text=Demo+Image+1",
    "https://via.placeholder.com/512x512?text=Demo+Image+2",
    "https://via.placeholder.com/512x512?text=Demo+Image+3"
  ],
  "copy": "Ethereal Dreams - A Journey Beyond Reality",
  "intent_category": "dream_visualization",
  "conversation_history": [...]
}
```

Note: Without a Replicate API key, images will be placeholder URLs. The LLM (intent + copy generation) will work perfectly with your OpenAI key.
