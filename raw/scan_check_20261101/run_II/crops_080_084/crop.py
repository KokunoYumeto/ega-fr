"""Crop a region of a strip and enlarge it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]
Coordinates are in the original strip pixels.
"""
import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_II"
OUT = RUN + r"/crops_080_084"

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(f"{RUN}/page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f"{OUT}/{name}.png")
print(f"{OUT}/{name}.png", c.size)
