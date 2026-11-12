"""Crop a region of a strip image and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
Coordinates are in the original strip pixels (2364 px wide).
"""
import sys
from PIL import Image

page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
base = r"user/Documents/ega_scan_check_20261101/run_II"
im = Image.open(f"{base}/page_{int(page):03d}_s{strip}.png")
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
out = f"{base}/crops_185_189/{name}.png"
c.save(out)
print(out, c.size)
