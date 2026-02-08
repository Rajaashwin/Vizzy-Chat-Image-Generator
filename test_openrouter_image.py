"""
Test OpenRouter Image Generation Integration
Tests the new image generation features and model switching
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_BASE = "http://localhost:8000"

def test_image_mode_response():
    """Test that image mode returns both LLM and image model info"""
    print("\n[TEST] Image Mode Response Structure")
    
    response = requests.post(f"{API_BASE}/chat", json={
        "message": "Create a serene mountain landscape",
        "num_images": 3
    })
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    
    print(f"  ✓ Status: {response.status_code}")
    print(f"  ✓ Session ID: {data.get('session_id')}")
    print(f"  ✓ LLM Model: {data.get('llm_model', 'openrouter/auto')}")
    print(f"  ✓ Image Model: {data.get('image_model', 'none')}")
    print(f"  ✓ Copy: {data.get('copy', '')[:50]}...")
    print(f"  ✓ Images: {len(data.get('images', []))} generated")
    
    assert 'llm_model' in data, "Missing llm_model field"
    assert 'image_model' in data, "Missing image_model field"
    assert data['llm_model'] == 'openrouter/auto', "Expected openrouter/auto LLM"
    assert len(data.get('images', [])) == 3, f"Expected 3 images, got {len(data.get('images', []))}"
    print("  ✅ PASSED")


def test_chat_mode_response():
    """Test that chat mode has no images but has LLM model info"""
    print("\n[TEST] Chat Mode Response Structure")
    
    response = requests.post(f"{API_BASE}/chat", json={
        "message": "What is the meaning of life?",
        "num_images": 0
    })
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    
    print(f"  ✓ Status: {response.status_code}")
    print(f"  ✓ LLM Model: {data.get('llm_model', 'openrouter/auto')}")
    print(f"  ✓ Image Model: {data.get('image_model', 'none')}")
    print(f"  ✓ Message: {data.get('copy', '')[:50]}...")
    print(f"  ✓ Images: {len(data.get('images', []))} (should be 0)")
    
    assert 'llm_model' in data, "Missing llm_model field"
    assert 'image_model' in data, "Missing image_model field"
    assert data['image_model'] == 'none', f"Expected 'none', got {data['image_model']}"
    assert len(data.get('images', [])) == 0, f"Expected 0 images in chat mode, got {len(data.get('images', []))}"
    print("  ✅ PASSED")


def test_mode_switching_workflow():
    """Test switching between image and chat modes in same session"""
    print("\n[TEST] Mode Switching Workflow")
    
    # First: Chat mode
    response1 = requests.post(f"{API_BASE}/chat", json={
        "message": "What are the main colors of autumn?",
        "num_images": 0
    })
    assert response1.status_code == 200
    data1 = response1.json()
    session_id = data1['session_id']
    print(f"  ✓ Chat Mode: {data1['image_model']} (expected 'none')")
    assert data1['image_model'] == 'none'
    assert len(data1['images']) == 0
    
    # Second: Image mode with same session
    response2 = requests.post(f"{API_BASE}/chat", json={
        "session_id": session_id,
        "message": "Paint an autumn forest with warm colors",
        "num_images": 3
    })
    assert response2.status_code == 200
    data2 = response2.json()
    print(f"  ✓ Image Mode: {data2['image_model']} (should have model name)")
    assert data2['image_model'] != 'none'
    assert len(data2['images']) == 3
    
    # Third: Back to chat mode
    response3 = requests.post(f"{API_BASE}/chat", json={
        "session_id": session_id,
        "message": "Do autumn colors have cultural significance?",
        "num_images": 0
    })
    assert response3.status_code == 200
    data3 = response3.json()
    print(f"  ✓ Back to Chat Mode: {data3['image_model']} (expected 'none')")
    assert data3['image_model'] == 'none'
    assert len(data3['images']) == 0
    
    print("  ✅ PASSED: Mode switching works correctly")


def test_image_generation_fallback():
    """Test that image generation falls back to placeholders gracefully"""
    print("\n[TEST] Image Generation Fallback")
    
    response = requests.post(f"{API_BASE}/chat", json={
        "message": "Generate a test image",
        "num_images": 3
    })
    
    assert response.status_code == 200
    data = response.json()
    images = data.get('images', [])
    
    print(f"  ✓ Generated {len(images)} images")
    print(f"  ✓ Image Model: {data.get('image_model')}")
    
    # Check if images are either real URLs or SVG placeholders
    for i, img in enumerate(images):
        if img.startswith('data:image/svg'):
            print(f"  ✓ Image {i+1}: SVG Placeholder (fallback)")
        elif img.startswith('http'):
            print(f"  ✓ Image {i+1}: Real image URL")
        else:
            print(f"  ✓ Image {i+1}: Generated content")
    
    assert len(images) > 0, "Should have at least some images"
    print("  ✅ PASSED")


def test_refine_endpoint_models():
    """Test that refine endpoint also returns model info"""
    print("\n[TEST] Refine Endpoint Model Info")
    
    # Create initial image request
    response1 = requests.post(f"{API_BASE}/chat", json={
        "message": "Create a abstract painting",
        "num_images": 3
    })
    assert response1.status_code == 200
    session_id = response1.json()['session_id']
    
    # Refine it
    response2 = requests.post(f"{API_BASE}/refine", json={
        "session_id": session_id,
        "message": "Create a abstract painting",
        "refinement": "with more blue tones",
        "num_images": 3
    })
    
    assert response2.status_code == 200
    data = response2.json()
    
    print(f"  ✓ LLM Model: {data.get('llm_model')}")
    print(f"  ✓ Image Model: {data.get('image_model')}")
    print(f"  ✓ Images: {len(data.get('images', []))}")
    
    assert 'llm_model' in data, "Refine response missing llm_model"
    assert 'image_model' in data, "Refine response missing image_model"
    print("  ✅ PASSED")


def test_placeholder_images_svg():
    """Test that placeholder images are valid SVG"""
    print("\n[TEST] Placeholder SVG Validation")
    
    response = requests.post(f"{API_BASE}/chat", json={
        "message": "Generate test images",
        "num_images": 2
    })
    
    assert response.status_code == 200
    data = response.json()
    images = data.get('images', [])
    
    svg_count = 0
    for img in images:
        if 'data:image/svg' in img:
            assert '<svg' in img, "Invalid SVG format"
            assert 'xmlns' in img, "SVG missing xmlns"
            svg_count += 1
    
    print(f"  ✓ Total images: {len(images)}")
    print(f"  ✓ SVG placeholders: {svg_count}")
    print("  ✅ PASSED: All placeholders are valid SVG")


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("OpenRouter Image Generation Test Suite")
    print("=" * 60)
    
    try:
        test_image_mode_response()
        test_chat_mode_response()
        test_mode_switching_workflow()
        test_image_generation_fallback()
        test_refine_endpoint_models()
        test_placeholder_images_svg()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nModel Integration Status:")
        print("  • LLM: OpenRouter (openrouter/auto)")
        print("  • Image: OpenRouter Image Generation API")
        print("  • Toggle: Chat ↔ Image mode switching verified")
        print("  • Fallback: SVG placeholders working correctly")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
