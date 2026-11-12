"""Crop a region of a strip image (coordinates in the 2000-px displayed frame) and enlarge it.

usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 OUTNAME [SCALE]
"""
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
base = r"user\Documents\ega_scan_check_20261101\run_0IV1"
im = Image.open(rf"{base}\page_{page:03d}_s{strip}.png")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{base}\crops_136_140\{out}.png")
print(c.size)
