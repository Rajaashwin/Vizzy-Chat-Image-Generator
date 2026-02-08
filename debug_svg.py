"""
Debug: Check actual SVG content returned from API
"""

import requests
import urllib.parse

API_BASE = "http://localhost:8000"

def debug_svg():
    print("\n" + "="*80)
    print("Debug: Actual SVG Content from API")
    print("="*80 + "\n")
    
    prompts = [
        "A dark shadowy forest",
        "A bright sunny beach",
    ]
    
    for prompt in prompts:
        print(f"Prompt: '{prompt}'")
        print("-" * 80)
        
        resp = requests.post(f"{API_BASE}/chat", json={
            "message": prompt,
            "num_images": 1
        }, timeout=60)
        
        data = resp.json()
        images = data.get('images', [])
        
        if images:
            svg_url = images[0]
            print(f"Full URL length: {len(svg_url)} characters")
            print(f"URL prefix: {svg_url[:100]}")
            
            # Decode the data URL
            if svg_url.startswith('data:image/svg+xml;charset=utf-8,'):
                svg_content = urllib.parse.unquote(svg_url[len('data:image/svg+xml;charset=utf-8,'):])
                print(f"\nDecoded SVG ({len(svg_content)} chars):")
                print(svg_content[:500])  # First 500 chars
                
                # Look for colors in the SVG
                if 'stop-color' in svg_content:
                    import re
                    colors = re.findall(r'stop-color:([^;]+)', svg_content)
                    print(f"\nColors found: {colors}")
                else:
                    print("\n⚠️  'stop-color' not found in SVG")
                    print("Searching for any color references...")
                    if '#' in svg_content:
                        import re
                        hex_colors = re.findall(r'#[0-9a-f]{6}', svg_content)
                        print(f"Hex colors found: {hex_colors}")
        
        print("\n")

if __name__ == "__main__":
    debug_svg()
