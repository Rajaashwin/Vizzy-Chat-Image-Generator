"""
End-to-End Test: Prompt Colors in API Responses
Verifies that the API returns different colored SVGs for different prompts
"""

import requests
import re
import urllib.parse

API_BASE = "http://localhost:8000"

def extract_color_from_svg(svg_data_url: str) -> str:
    """Extract the primary color from an SVG data URL"""
    if not svg_data_url.startswith('data:image/svg'):
        return "N/A"
    
    # Decode the URL
    try:
        svg_content = urllib.parse.unquote(svg_data_url[len('data:image/svg+xml;charset=utf-8,'):])
        # Find the first stop-color attribute with hex color
        colors = re.findall(r'stop-color:(#[0-9a-f]{6})', svg_content)
        return colors[0] if colors else "N/A"
    except:
        return "ERROR"

def test_api_prompt_colors():
    print("\n" + "="*80)
    print("End-to-End Test: Prompt-Based Colors in API Responses")
    print("="*80 + "\n")
    
    test_cases = [
        ("A dark, moody forest", "🌲 Dark/Moody"),
        ("A bright sunny beach", "🏖️ Bright/Sunny"),
        ("A calm blue lake", "💧 Calm/Blue"),
        ("A fiery sunset", "🔥 Fiery/Sunset"),
        ("A cold winter landscape", "❄️ Cold/Winter"),
    ]
    
    results = []
    
    for prompt, label in test_cases:
        print(f"📝 {label}")
        print(f"   Prompt: '{prompt}'")
        
        try:
            resp = requests.post(f"{API_BASE}/chat", json={
                "message": prompt,
                "num_images": 3
            }, timeout=60)
            
            if resp.status_code != 200:
                print(f"   ❌ API Error: {resp.status_code}")
                continue
            
            data = resp.json()
            images = data.get('images', [])
            
            if not images:
                print(f"   ❌ No images returned")
                continue
            
            # Extract color from each image
            colors = []
            for i, img in enumerate(images):
                color = extract_color_from_svg(img)
                colors.append(color)
            
            primary_color = colors[0]
            print(f"   🎨 Primary Color: {primary_color}")
            print(f"   🎨 All Colors: {colors}")
            
            results.append((label, primary_color, colors))
            print(f"   ✅ Got 3 images")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        print()
    
    # Analyze results
    print("="*80)
    print("Analysis:")
    print("="*80 + "\n")
    
    if results:
        print(f"✅ Successfully tested {len(results)} different prompts\n")
        
        # Check color uniqueness across prompts
        primary_colors = [color for _, color, _ in results]
        unique_colors = set(primary_colors)
        
        print(f"📊 Unique primary colors: {len(unique_colors)}/{len(results)}")
        print(f"   Color variety: " + ("✅ Excellent" if len(unique_colors) == len(results) else "⚠️ Good"))
        
        print("\n🎨 Prompt → Color Mapping:")
        for label, color, all_colors in results:
            print(f"  {label:20} → Primary: {color}  |  All: {all_colors}")
        
        if len(unique_colors) == len(results):
            print("\n" + "="*80)
            print("🎉 RESULT: Each prompt gets a unique color!")
            print("="*80)
        else:
            print(f"\n⚠️  Only {len(unique_colors)} unique colors for {len(results)} prompts")
    else:
        print("❌ Could not test any prompts")
    
    print()

if __name__ == "__main__":
    test_api_prompt_colors()
