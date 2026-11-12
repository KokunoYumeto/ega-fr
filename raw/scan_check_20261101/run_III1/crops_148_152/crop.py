"""Crop a region of a strip image and enlarge it.

usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 SCALE NAME
Coordinates are in the displayed (2000-px-wide) frame of the strip; they are
multiplied by 1.25 to map to the original 2508-px-wide image.
"""
import sys
from PIL import Image

run = r'user\Documents\ega_scan_check_20261101\run_III1'
out = run + r'\crops_148_152'
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(rf'{run}\page_{page}_s{strip}.png')
f = im.width / 2000.0
box = (int(x0 * f), int(y0 * f), int(x1 * f), int(y1 * f))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf'{out}\{name}.png')
print(rf'{out}\{name}.png', c.size)
