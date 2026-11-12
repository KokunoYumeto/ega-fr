"""Crop a region of a strip image and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
Coordinates are in the strip's original pixel frame.
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = RUN + r"\crops_190_194"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(RUN + r"\page_%03d_s%d.png" % (page, strip))
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT + "\\" + name)
print(OUT + "\\" + name, c.size)
