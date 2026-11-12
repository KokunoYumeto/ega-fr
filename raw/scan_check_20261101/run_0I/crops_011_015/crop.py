"""Crop a region of a strip image (coordinates in the original pixel frame) and upscale it.
usage: python crop.py STRIP_PNG X0 Y0 X1 Y1 SCALE OUT_PNG"""
import sys
from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
im = Image.open(src)
box = tuple(int(v) for v in (x0, y0, x1, y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(out)
print(out, c.size)
