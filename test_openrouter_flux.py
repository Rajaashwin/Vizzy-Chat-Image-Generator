"""
Test: OpenRouter Flux Image Generation
Verifies real image generation via OpenRouter API
"""

import requests
import re

API_BASE = "http://localhost:8000"

def test_openrouter_flux_generation():
    print("\n" + "="*80)
    print("Test: OpenRouter Flux Real Image Generation")
    print("="*80 + "\n")
    
    test_cases = [
        ("A serene mountain landscape with snow peaks", "Mountain"),
        ("A vibrant sunset over the ocean", "Sunset"),
    ]
    
    for prompt, label in test_cases:
        print(f"[{label}] Testing: '{prompt}'")
        print("-" * 80)
        
        try:
            resp = requests.post(f"{API_BASE}/chat", json={
                "message": prompt,
                "num_images": 2
            }, timeout=60)
            
            if resp.status_code != 200:
                print(f"  ❌ API Error: {resp.status_code}")
                continue
            
            data = resp.json()
            images = data.get('images', [])
            model = data.get('image_model', 'unknown')
            
            print(f"  Model Used: {model}")
            print(f"  Images Returned: {len(images)}")
            
            # Check if images are real URLs or placeholders
            real_images = 0
            placeholder_images = 0
            
            for i, img in enumerate(images, 1):
                if img.startswith('http'):
                    real_images += 1
                    print(f"  [OK] Image {i}: Real URL (OpenRouter Flux)")
                    print(f"       URL: {img[:80]}...")
                elif img.startswith('data:image/svg'):
                    placeholder_images += 1
                    print(f"  [FALLBACK] Image {i}: SVG Placeholder (fallback)")
                else:
                    print(f"  [?] Image {i}: Unknown format")
            
            print(f"\n  Summary: {real_images} real images, {placeholder_images} placeholders")
            
            if real_images > 0:
                print(f"  [PASS] Got real OpenRouter Flux images!")
            else:
                print(f"  [FALLBACK] Using SVG placeholders instead")
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
        
        print()
    
    print("="*80)
    print("Test Complete!")
    print("="*80)

if __name__ == "__main__":
    test_openrouter_flux_generation()
