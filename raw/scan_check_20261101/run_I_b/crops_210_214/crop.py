"""Crop a region of a strip image and enlarge it.

Usage: python crop.py <strip.png> <x0> <y0> <x1> <y1> <scale> <out.png>
Coordinates are in the strip's original pixels.
"""
import sys
from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
x0, y0, x1, y1 = (int(v) for v in (x0, y0, x1, y1))
scale = float(scale)
im = Image.open(src)
region = im.crop((x0, y0, x1, y1))
if scale != 1:
    region = region.resize((int(region.width * scale), int(region.height * scale)), Image.LANCZOS)
region.save(out)
print(out, region.size)
