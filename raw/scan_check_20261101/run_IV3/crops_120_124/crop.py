"""Crop a region of a strip, given in the 2000-px-wide display coordinates, and upscale it.
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME"""
import sys
from pathlib import Path
from PIL import Image

page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
run = Path(__file__).resolve().parent.parent
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png")
f = im.size[0] / 2000.0
box = tuple(int(round(float(v) * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.size[0] * s), int(c.size[1] * s)), Image.LANCZOS)
out = Path(__file__).resolve().parent / f"{name}.png"
c.save(out)
print(out, c.size)
