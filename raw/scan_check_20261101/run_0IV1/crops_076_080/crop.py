"""Crop a region of a strip image and upscale it.

Usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 OUTNAME [SCALE]
Coordinates are in the original strip pixels.
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
OUT = RUN + r"\crops_076_080"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(rf"{RUN}\page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{OUT}\{name}.png")
print(rf"{OUT}\{name}.png", c.size)
