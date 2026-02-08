"""
Quick Test: OpenRouter Image Generation Mode Switching
Tests only the essential model switching functionality
"""

import requests
import json

API_BASE = "http://localhost:8000"

def quick_test():
    print("\n" + "="*60)
    print("Quick Test: Image Generation with Mode Switching")
    print("="*60)
    
    # Test 1: Image Mode
    print("\n[1] Image Mode - Should request 3 images")
    resp = requests.post(f"{API_BASE}/chat", json={
        "message": "Create a beautiful sunset",
        "num_images": 3
    }, timeout=60)  # Increased timeout
    
    data = resp.json()
    print(f"    Status: {resp.status_code}")
    print(f"    LLM Model: {data.get('llm_model')}")
    print(f"    Image Model: {data.get('image_model')}")
    print(f"    Images Generated: {len(data.get('images', []))}")
    
    assert resp.status_code == 200
    assert data['llm_model'] == 'openrouter/auto'
    assert len(data.get('images', [])) == 3
    assert 'image_model' in data
    print("    ✅ PASSED")
    
    session_id = data['session_id']
    
    # Test 2: Chat Mode on same session
    print("\n[2] Chat Mode - Should NOT request images (same session)")
    resp = requests.post(f"{API_BASE}/chat", json={
        "session_id": session_id,
        "message": "What is the best way to photograph sunsets?",
        "num_images": 0
    }, timeout=60)  # Increased timeout
    
    data = resp.json()
    print(f"    Status: {resp.status_code}")
    print(f"    LLM Model: {data.get('llm_model')}")
    print(f"    Image Model: {data.get('image_model')}")
    print(f"    Images Generated: {len(data.get('images', []))}")
    
    assert resp.status_code == 200
    assert data['image_model'] == 'none'
    assert len(data.get('images', [])) == 0
    print("    ✅ PASSED")
    
    # Test 3: Back to Image Mode
    print("\n[3] Switch Back to Image Mode")
    resp = requests.post(f"{API_BASE}/chat", json={
        "session_id": session_id,
        "message": "Create a dramatic storm cloud",
        "num_images": 3
    }, timeout=60)  # Increased timeout
    
    data = resp.json()
    print(f"    Status: {resp.status_code}")
    print(f"    LLM Model: {data.get('llm_model')}")
    print(f"    Image Model: {data.get('image_model')}")
    print(f"    Images Generated: {len(data.get('images', []))}")
    
    assert resp.status_code == 200
    assert data['image_model'] != 'none'
    assert len(data.get('images', [])) == 3
    print("    ✅ PASSED")
    
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED!")
    print("="*60)
    print("\nModel Configuration Summary:")
    print(f"  • LLM: {data.get('llm_model')}")
    print(f"  • Image: {data.get('image_model')}")
    print(f"  • Session Management: ✓ Working")
    print(f"  • Mode Toggle: ✓ Chat ↔ Image switching verified")
    print("\nFrontend is ready at: http://localhost:5173")

if __name__ == "__main__":
    try:
        quick_test()
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        exit(1)
