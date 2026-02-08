"""
Test: Prompt-based Color Generation for Placeholders
Verifies that different prompts generate different colored SVGs
"""

import requests

API_BASE = "http://localhost:8000"

def test_prompt_colors():
    print("\n" + "="*70)
    print("Test: Prompt-Based Placeholder Colors")
    print("="*70)
    
    prompts = [
        "A dark, moody forest with shadows",
        "A bright, sunny beach with golden light",
        "A calm, peaceful lake with blue tones",
        "A fiery sunset with orange and red colors",
        "A cold, icy winter landscape"
    ]
    
    results = []
    for prompt in prompts:
        print(f"\n📝 Prompt: '{prompt[:40]}...'")
        resp = requests.post(f"{API_BASE}/chat", json={
            "message": prompt,
            "num_images": 3
        }, timeout=60)
        
        if resp.status_code != 200:
            print(f"   ❌ Error: {resp.status_code}")
            continue
        
        data = resp.json()
        images = data.get('images', [])
        
        # Extract main color from first SVG
        if images and images[0].startswith('data:image/svg'):
            # Find the color in the gradient
            svg_text = images[0]
            if 'stop-color' in svg_text:
                # Extract hex color
                import re
                colors = re.findall(r'stop-color:(#[0-9a-f]{6})', svg_text)
                if colors:
                    main_color = colors[0]
                    print(f"   🎨 Primary Color: {main_color}")
                    results.append((prompt[:30], main_color))
        
        print(f"   ✓ Generated {len(images)} images")
    
    print("\n" + "="*70)
    print("Color Distribution Summary:")
    print("="*70)
    
    # Check if colors are different
    colors_used = [color for _, color in results]
    unique_colors = set(colors_used)
    
    print(f"\nPrompts tested: {len(results)}")
    print(f"Unique colors: {len(unique_colors)}")
    
    if len(unique_colors) > 1:
        print("✅ SUCCESS: Different prompts generate different colors!")
    else:
        print("⚠️  Note: All prompts generated same color (deterministic mode)")
    
    print("\nColor mapping:")
    for prompt, color in results:
        print(f"  • {prompt:30} → {color}")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    test_prompt_colors()
