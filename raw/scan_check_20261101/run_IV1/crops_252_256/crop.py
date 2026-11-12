"""Crop and upscale small regions of the page strips for close reading.

Usage: python -I crop.py <strip.png> <x0> <y0> <x1> <y1> <scale> <out.png>
Coordinates are in the strip's original pixels.
"""
import sys
from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
x0, y0, x1, y1 = (int(v) for v in (x0, y0, x1, y1))
scale = float(scale)
im = Image.open(src)
box = im.crop((x0, y0, x1, y1))
w, h = box.size
box = box.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
box.save(out)
print(out, box.size)
