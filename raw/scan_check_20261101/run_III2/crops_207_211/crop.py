"""Crop a region of a page strip (coordinates in the 2000-px-wide display frame) and enlarge it.

usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
"""
import sys
from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
src = rf'user\Documents\ega_scan_check_20261101\run_III2\page_{page}_s{strip}.png'
im = Image.open(src)
r = im.width / 2000.0
box = (int(x0 * r), int(y0 * r), int(x1 * r), int(y1 * r))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = rf'user\Documents\ega_scan_check_20261101\run_III2\crops_207_211\{name}.png'
c.save(out)
print(out, c.size)
