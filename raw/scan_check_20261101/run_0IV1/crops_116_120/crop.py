"""Crop a region of a strip image and upscale it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
Coordinates are in the strip's original pixel frame.
"""
import sys
import os
from PIL import Image

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.dirname(os.path.abspath(__file__))

page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
src = os.path.join(RUN, f"page_{int(page):03d}_s{strip}.png")
im = Image.open(src)
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
dst = os.path.join(OUT, f"{name}.png")
c.save(dst)
print(dst, c.size)
