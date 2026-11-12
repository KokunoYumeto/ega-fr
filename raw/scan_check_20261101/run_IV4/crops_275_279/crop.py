"""Crop a region of a page strip (coordinates in the DISPLAYED 2000-px-wide frame) and enlarge it.
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]"""
import pathlib
import sys

from PIL import Image

D = pathlib.Path(__file__).resolve().parent
R = D.parent
p, s = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(R / f"page_{p}_s{s}.png")
f = im.size[0] / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
c.save(D / f"{name}.png")
print(D / f"{name}.png", c.size)
