"""Crop a region of a strip image and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
Coordinates are in the original strip pixels.
"""
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{base}\crops_070_074\{out}")
print(c.size)
