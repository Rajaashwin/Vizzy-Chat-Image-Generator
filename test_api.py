"""
Test script for Vizzy Chat API
Tests the chat endpoint with real LLM and image generation
"""

import requests
import json
import sys

API_BASE = "http://localhost:8000"

def test_health():
    """Test backend health"""
    print("🔍 Testing backend health...")
    try:
        response = requests.get(f"{API_BASE}/")
        print(f"✅ Backend is alive: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return True
    except Exception as e:
        print(f"❌ Backend error: {e}")
        return False

def test_chat():
    """Test chat endpoint with real LLM and image generation"""
    print("\n🎨 Testing chat endpoint with LLM intent + image generation...")
    
    payload = {
        "session_id": "test_session_001",
        "message": "Create a dreamy landscape with floating mountains and soft clouds",
        "num_images": 3
    }
    
    try:
        print(f"📤 Sending: {payload['message']}")
        response = requests.post(
            f"{API_BASE}/chat",
            json=payload,
            timeout=120  # 2 minute timeout for LLM + image generation
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Chat successful!")
            print(f"Intent detected: {data.get('intent_category')}")
            print(f"Generated copy: {data.get('copy')}")
            print(f"Number of images: {len(data.get('images', []))}")
            print(f"Session ID: {data.get('session_id')}")
            print(f"\nImage URLs:")
            for i, img in enumerate(data.get('images', []), 1):
                print(f"  {i}. {img[:80]}...")
            return True
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return False
    except requests.exceptions.Timeout:
        print("❌ Request timed out (image generation takes 20-60 seconds)")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_refine():
    """Test refinement endpoint"""
    print("\n🔄 Testing refinement endpoint...")
    
    payload = {
        "session_id": "test_session_001",
        "message": "Create a dreamy landscape with floating mountains and soft clouds",
        "refinement": "Make it more vibrant with golden and purple colors",
        "num_images": 2
    }
    
    try:
        print(f"📤 Refining with: {payload['refinement']}")
        response = requests.post(
            f"{API_BASE}/refine",
            json=payload,
            timeout=120
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Refinement successful!")
            print(f"Updated copy: {data.get('copy')}")
            return True
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_session():
    """Test session retrieval"""
    print("\n📋 Testing session retrieval...")
    
    try:
        response = requests.get(f"{API_BASE}/session/test_session_001")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Session retrieved!")
            print(f"Messages in session: {len(data.get('messages', []))}")
            print(f"Session created at: {data.get('created_at')}")
            return True
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Vizzy Chat API Test Suite")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Health Check", test_health()))
    
    if results[-1][1]:  # Only continue if health check passed
        results.append(("Chat Endpoint", test_chat()))
        results.append(("Refinement", test_refine()))
        results.append(("Session Retrieval", test_session()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {name}")
    
    all_passed = all(result[1] for result in results)
    print("=" * 60)
    print(f"\n{'🎉 All tests passed!' if all_passed else '⚠️  Some tests failed'}")
