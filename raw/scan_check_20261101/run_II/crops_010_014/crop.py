"""Crop a region of a strip image and upscale it.

Usage: python crop.py <strip.png> <x0> <y0> <x1> <y1> <out.png> [scale]
Coordinates are in the original image's pixels.
"""
import sys
from PIL import Image

src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
region = im.crop((x0, y0, x1, y1))
region = region.resize((int(region.width * scale), int(region.height * scale)), Image.LANCZOS)
region.save(out)
print(out, region.size)
