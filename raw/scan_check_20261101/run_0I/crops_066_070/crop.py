"""Crop a region of a strip and enlarge it.

usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
Coordinates are in ORIGINAL strip pixels.
"""
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
base = r"user/Documents/ega_scan_check_20261101/run_0I"
im = Image.open(f"{base}/page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = f"{base}/crops_066_070/{name}.png"
c.save(out)
print(out, c.size)
