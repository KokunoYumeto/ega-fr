"""Crop a region of a strip and enlarge it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
Coordinates are in the strip's original pixels.
"""
import sys
from PIL import Image

page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
img = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png")
box = (int(x0), int(y0), int(x1), int(y1))
c = img.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(rf"{base}\crops_130_134\{out}")
print(c.size)
