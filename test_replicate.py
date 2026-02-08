#!/usr/bin/env python3
"""Test Replicate image generation"""
import requests
import time

print("Testing image generation with Replicate token...\n")

# Test the /chat endpoint with image mode
response = requests.post('http://localhost:8000/chat', json={
    'message': 'A beautiful sunset over mountains',
    'num_images': 2
})

if response.status_code == 200:
    data = response.json()
    print('✓ Chat request successful')
    print(f'Image model used: {data.get("image_model", "unknown")}')
    print(f'Number of images: {len(data.get("images", []))}')
    
    image_model = data.get('image_model', 'Placeholder')
    is_real = 'Placeholder' not in image_model and 'replicate' not in image_model.lower()
    
    if not is_real and 'Replicate' in image_model:
        print(f'✓ REAL IMAGES GENERATED via Replicate!')
        for i, img in enumerate(data.get('images', [])[:2]):
            if img.startswith('http'):
                print(f'  Image {i+1}: {img[:100]}...')
            else:
                print(f'  Image {i+1}: {img[:80]}...')
    elif 'Placeholder' in image_model:
        print(f'✗ Still using placeholder images: {image_model}')
    else:
        print(f'ℹ Image model: {image_model}')
else:
    print(f'✗ Error: {response.status_code}')
    print(response.text[:200])
