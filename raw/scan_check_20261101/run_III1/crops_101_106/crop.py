"""Crop a region of a strip image and enlarge it.
usage: python crop.py SRC_PNG X0 Y0 X1 Y1 SCALE OUT_PNG   (coordinates in the strip's own pixels)"""
import sys
from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
