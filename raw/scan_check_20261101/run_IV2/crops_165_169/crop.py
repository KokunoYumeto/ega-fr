"""Crop a region of a strip image and enlarge it.
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME   (coordinates in original strip pixels)"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
run = here.parent
page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
im = Image.open(run / f"page_{int(page):03d}_s{int(strip)}.png")
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
out = here / f"{name}.png"
c.save(out)
print(out, c.size)
