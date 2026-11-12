"""Crop a region of a page strip and enlarge it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 OUTNAME [scale]
coordinates are in the strip's original pixels.
"""
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{base}\crops_180_184\{out}")
print(im.size, "->", c.size)
