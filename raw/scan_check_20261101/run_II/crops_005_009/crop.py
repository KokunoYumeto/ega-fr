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
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
