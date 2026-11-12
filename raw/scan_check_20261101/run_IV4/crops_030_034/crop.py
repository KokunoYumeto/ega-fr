"""Crop a region of a strip and enlarge it.

usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
coordinates are in original strip pixels.
"""
import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
OUT = RUN + "/crops_030_034"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(f"{RUN}/page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f"{OUT}/{name}.png")
print(f"{OUT}/{name}.png", c.size)
