"""Crop a region of a strip image (coordinates in original pixels) and enlarge it.

usage: python -I crop.py <page> <strip> <x0> <y0> <x1> <y1> <scale> <outname>
"""
import sys, os
from PIL import Image

run = r"user\Documents\ega_scan_check_20261101\run_IV1"
out = os.path.join(run, "crops_242_246")
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(os.path.join(run, "page_%03d_s%d.png" % (page, strip)))
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
p = os.path.join(out, name)
c.save(p)
print(p, c.size, im.size)
