"""Crop a region of a page strip and enlarge it.

usage: python -I crop.py <strip.png> <x0> <y0> <x1> <y1> <out.png> [scale]
Coordinates are in the strip's original pixel frame.
"""
import sys
from PIL import Image

src, x0, y0, x1, y1, out = sys.argv[1:7]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
