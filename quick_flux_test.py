"""Quick test - single image request"""
import requests
import json

API_BASE = "http://localhost:8000"

print("Testing OpenRouter Flux image generation...\n")

try:
    resp = requests.post(f"{API_BASE}/chat", json={
        "message": "A beautiful sunset",
        "num_images": 2
    }, timeout=45)
    
    print(f"Status: {resp.status_code}")
    
    if resp.status_code == 200:
        data = resp.json()
        print(f"Model: {data.get('image_model')}")
        print(f"Images: {len(data.get('images', []))}")
        
        for i, img in enumerate(data.get('images', []), 1):
            if img.startswith('http'):
                print(f"  Image {i}: REAL URL (Flux)")
                print(f"    {img[:100]}...")
            elif img.startswith('data:image/svg'):
                print(f"  Image {i}: SVG PLACEHOLDER (fallback)")
            else:
                print(f"  Image {i}: UNKNOWN")
    else:
        print(f"Error: {resp.text[:200]}")
        
except Exception as e:
    print(f"ERROR: {e}")
