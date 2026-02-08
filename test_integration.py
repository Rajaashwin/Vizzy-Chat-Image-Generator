#!/usr/bin/env python3
"""
Vizzy Chat - API Integration Test
Tests the backend without external dependencies
"""

import urllib.request
import json
import time
import sys

API_BASE = "http://localhost:8000"

def test_endpoint(method, path, payload=None):
    """Generic HTTP request handler"""
    url = f"{API_BASE}{path}"
    
    if payload:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header('Content-Type', 'application/json')
    else:
        req = urllib.request.Request(url, method=method)
    
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            body = response.read().decode('utf-8')
            return response.status, json.loads(body)
    except urllib.error.URLError as e:
        return None, str(e)
    except json.JSONDecodeError:
        return None, "Invalid JSON response"

def main():
    print("=" * 70)
    print("🚀 Vizzy Chat API Integration Test")
    print("=" * 70)
    print(f"Testing: {API_BASE}")
    print()
    
    # Test 1: Health Check
    print("📡 [Test 1] Health Check")
    print("-" * 70)
    status, response = test_endpoint("GET", "/")
    
    if status == 200:
        print("✅ Backend is alive!")
        print(f"   App: {response.get('app')}")
        print(f"   Version: {response.get('version')}")
    else:
        print(f"❌ Backend error: {response}")
        return False
    
    print()
    
    # Test 2: Chat with LLM
    print("🎨 [Test 2] Chat Endpoint - LLM Intent + Image Generation")
    print("-" * 70)
    print("📤 Sending: 'Create a dreamy landscape with floating mountains'")
    print("   (This will take 30-90 seconds...)")
    print()
    
    payload = {
        "session_id": "integration_test_001",
        "message": "Create a dreamy landscape with floating mountains and soft clouds",
        "num_images": 2
    }
    
    start_time = time.time()
    status, response = test_endpoint("POST", "/chat", payload)
    elapsed = time.time() - start_time
    
    if status == 200:
        print(f"✅ Chat successful! ({elapsed:.1f}s)")
        print(f"   Intent: {response.get('intent_category')}")
        print(f"   Copy: {response.get('copy')}")
        print(f"   Images: {len(response.get('images', []))} generated")
        print(f"   Session: {response.get('session_id')}")
        
        # Show image URLs
        for i, img in enumerate(response.get('images', []), 1):
            preview = img[:65] + "..." if len(img) > 65 else img
            print(f"     {i}. {preview}")
    else:
        print(f"❌ Error: {response}")
        return False
    
    print()
    
    # Test 3: Refinement
    print("🔄 [Test 3] Refinement Endpoint")
    print("-" * 70)
    print("📤 Refining: 'Make it more vibrant with golden colors'")
    print()
    
    payload = {
        "session_id": "integration_test_001",
        "message": "Create a dreamy landscape with floating mountains and soft clouds",
        "refinement": "Make it more vibrant with golden and purple colors",
        "num_images": 2
    }
    
    start_time = time.time()
    status, response = test_endpoint("POST", "/refine", payload)
    elapsed = time.time() - start_time
    
    if status == 200:
        print(f"✅ Refinement successful! ({elapsed:.1f}s)")
        print(f"   Updated copy: {response.get('copy')}")
    else:
        print(f"❌ Error: {response}")
        return False
    
    print()
    
    # Test 4: Session Retrieval
    print("📋 [Test 4] Session Retrieval")
    print("-" * 70)
    
    status, response = test_endpoint("GET", "/session/integration_test_001")
    
    if status == 200:
        print(f"✅ Session retrieved!")
        print(f"   Created at: {response.get('created_at')}")
        print(f"   Messages: {len(response.get('messages', []))}")
        print(f"   Taste themes: {response.get('taste', {}).get('themes', [])}")
    else:
        print(f"❌ Error: {response}")
        return False
    
    print()
    print("=" * 70)
    print("✅ All tests passed!")
    print("=" * 70)
    print()
    print("Backend is ready for the React frontend.")
    print("To run the frontend:")
    print("  1. Install Node.js from https://nodejs.org/")
    print("  2. cd f:\\Assessment\\vizzy-chat\\frontend")
    print("  3. npm install")
    print("  4. npm run dev")
    print("  5. Open http://localhost:5173")
    print()
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)
