"""Crop a region of a strip PNG and enlarge it.

usage: python crop.py STRIP OUT x0 y0 x1 y1 [zoom]
Coordinates are in the strip's original pixel frame.
"""
import sys
from PIL import Image

strip, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
zoom = float(sys.argv[7]) if len(sys.argv) > 7 else 3.0
im = Image.open(strip)
box = (max(0, x0), max(0, y0), min(im.width, x1), min(im.height, y1))
c = im.crop(box)
c = c.resize((int(c.width * zoom), int(c.height * zoom)), Image.LANCZOS)
c.save(out)
print(out, c.size)
