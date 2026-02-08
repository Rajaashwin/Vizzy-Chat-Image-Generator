"""
Direct Test: Prompt-based Color Generation
Tests the color generation logic directly without HTTP calls
"""

import hashlib
import colorsys
import re

def generate_colors_from_prompt(seed_prompt: str) -> list:
    """Generate 3 distinct colors from a prompt (same as backend)"""
    hash_obj = hashlib.md5(seed_prompt.encode())
    hash_val = int(hash_obj.hexdigest()[:8], 16)
    
    base_hue_offset = hash_val % 360
    colors = []
    for i in range(3):
        hue = (base_hue_offset + i * 120) % 360
        sat = 60 + (hash_val // (i + 1) % 40)
        lum = 50 + (hash_val // (i + 2) % 30)
        
        rgb = colorsys.hls_to_rgb(hue / 360, lum / 100, sat / 100)
        hex_color = '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        colors.append(hex_color)
    
    return colors

def test_color_generation():
    print("\n" + "="*70)
    print("Direct Test: Prompt-Based Color Generation")
    print("="*70 + "\n")
    
    test_prompts = [
        "A dark, moody forest with deep shadows and mist",
        "A bright, sunny beach with golden light and waves",
        "A calm, peaceful blue lake surrounded by mountains",
        "A fiery sunset with intense orange, red and purple hues",
        "A cold, icy winter landscape covered in snow",
    ]
    
    print("Testing color generation from different prompts:\n")
    
    all_colors = {}
    for prompt in test_prompts:
        colors = generate_colors_from_prompt(prompt)
        primary_color = colors[0]
        all_colors[prompt[:35]] = primary_color
        
        print(f"📝 Prompt: {prompt[:50]}")
        print(f"   Primary Color: {primary_color}")
        print(f"   All Colors: {colors}")
        print()
    
    print("="*70)
    print("Color Summary:")
    print("="*70 + "\n")
    
    unique_colors = set(all_colors.values())
    
    print(f"Prompts tested: {len(all_colors)}")
    print(f"Unique primary colors: {len(unique_colors)}")
    
    if len(unique_colors) > 1:
        print("\n✅ SUCCESS: Different prompts generate different colors!")
        print(f"   Color variety: {len(unique_colors)}/{len(all_colors)}")
    else:
        print("\n⚠️  All prompts generated the same color")
    
    print("\nPrompt → Color Mapping:")
    for i, (prompt, color) in enumerate(all_colors.items(), 1):
        print(f"  {i}. {prompt:35} → {color}")
    
    # Test determinism: Same prompt should always give same color
    print("\n" + "="*70)
    print("Determinism Test (same prompt = same color):")
    print("="*70 + "\n")
    
    test_prompt = "Create a beautiful sunset"
    colors1 = generate_colors_from_prompt(test_prompt)
    colors2 = generate_colors_from_prompt(test_prompt)
    
    if colors1 == colors2:
        print(f"✅ PASS: Same prompt generates same colors consistently")
        print(f"   Prompt: '{test_prompt}'")
        print(f"   Colors: {colors1}")
    else:
        print(f"❌ FAIL: Same prompt generated different colors")
        print(f"   First:  {colors1}")
        print(f"   Second: {colors2}")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    test_color_generation()
