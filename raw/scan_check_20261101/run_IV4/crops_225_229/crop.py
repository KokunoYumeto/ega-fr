"""Crop a region of a strip and enlarge it.

usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 SCALE NAME
coordinates are in the strip's original pixels.
"""
import sys
from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
src = r'user\Documents\ega_scan_check_20261101\run_IV4\page_%s_s%s.png' % (page, strip)
out = r'user\Documents\ega_scan_check_20261101\run_IV4\crops_225_229\%s.png' % name
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
