"""Crop a region of a page strip for close inspection.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
Coordinates are in the 2000-px-wide display frame of the strip; they are
mapped to the original pixels, cropped, and enlarged by SCALE (default 2).
"""
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
src = f"user/Documents/ega_scan_check_20261101/run_IV2/page_{page}_s{strip}.png"
im = Image.open(src)
f = im.size[0] / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
out = f"user/Documents/ega_scan_check_20261101/run_IV2/crops_140_144/{name}.png"
c.save(out)
print(out, c.size)
