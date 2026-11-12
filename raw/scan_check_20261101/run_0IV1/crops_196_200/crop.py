"""Crop a region of a strip and upscale it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
Coordinates are in DISPLAYED pixels (2000-wide view); they are converted
to original pixels using the strip's width / 2000.
"""
import sys
import os
from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
run = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(run, f"page_{page}_s{strip}.png"))
f = im.size[0] / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), name + ".png")
c.save(out)
print(out, c.size)
