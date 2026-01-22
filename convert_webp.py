#!/usr/bin/env python3
from PIL import Image
import sys
import os

def convert_to_webp(input_path, quality=80):
    """Convert image to WebP format"""
    try:
        # Open image
        img = Image.open(input_path)
        
        # Get output path
        base = os.path.splitext(input_path)[0]
        output_path = f"{base}.webp"
        
        # Convert and save
        img.save(output_path, 'WEBP', quality=quality, method=6)
        
        # Get file sizes
        original_size = os.path.getsize(input_path) / 1024  # KB
        new_size = os.path.getsize(output_path) / 1024  # KB
        reduction = ((original_size - new_size) / original_size) * 100
        
        print(f"✓ {os.path.basename(input_path)} → {os.path.basename(output_path)}")
        print(f"  {original_size:.0f}KB → {new_size:.0f}KB ({reduction:.0f}% reduction)")
        
        return True
    except Exception as e:
        print(f"✗ Error converting {input_path}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 convert_webp.py image1.jpg image2.png ...")
        sys.exit(1)
    
    for img_path in sys.argv[1:]:
        convert_to_webp(img_path)
