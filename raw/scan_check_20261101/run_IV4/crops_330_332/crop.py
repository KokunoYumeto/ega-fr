"""Crop a region of a strip image and enlarge it.

Usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE NAME
Coordinates are in the original strip pixels.
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = RUN + r"\crops_330_332"

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(rf"{RUN}\page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{OUT}\{name}.png")
print(c.size)
