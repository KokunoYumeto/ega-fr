"""Crop a region of a strip image for close inspection.

Usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
Coordinates are in the ORIGINAL strip pixels (2429 px wide).
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = RUN + r"\crops_150_154"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(RUN + rf"\page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT + "\\" + name)
print(OUT + "\\" + name, c.size)
