"""Crop helper for the pp. 110-114 scan check.

Usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]
Coordinates are in the displayed (2000-px-wide) frame of the strip; they are
mapped to the original image by the strip's width / 2000. SCALE enlarges.
"""
import sys
from PIL import Image

run = r"user\Documents\ega_scan_check_20261101\run_IV2"
name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(rf"{run}\page_{page}_s{strip}.png")
f = im.size[0] / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
c.save(rf"{run}\crops_110_114\{name}.png")
print(name, box, c.size)
