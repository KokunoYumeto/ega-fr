"""Crop regions of the strip images (original pixel coordinates) and enlarge them.

usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]
writes crops_075_079/NAME.png
"""
import sys
from PIL import Image

base = r"user\Documents\ega_scan_check_20261101\run_IV3"
name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = map(int, sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
img = Image.open(rf"{base}\page_{page:03d}_s{strip}.png")
w, h = img.size
box = (max(0, x0), max(0, y0), min(w, x1), min(h, y1))
c = img.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = rf"{base}\crops_075_079\{name}.png"
c.save(out)
print(out, img.size, box, c.size)
