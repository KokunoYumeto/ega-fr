"""Crop a region of a page strip (coordinates in the strip's original pixels) and upscale it.
usage: python -I crop.py STRIP X0 Y0 X1 Y1 OUT [SCALE]"""
import sys

from PIL import Image

strip, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(strip)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
