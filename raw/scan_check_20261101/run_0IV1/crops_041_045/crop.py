"""Crop a region of a strip image and enlarge it.

usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
coordinates are in the strip's original pixels.
"""
import sys
from PIL import Image

run = r'user\Documents\ega_scan_check_20261101\run_0IV1'
out = run + r'\crops_041_045'
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(rf'{run}\page_{page:03d}_s{strip}.png')
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
path = rf'{out}\p{page:03d}_s{strip}_{name}.png'
c.save(path)
print(path, c.size)
