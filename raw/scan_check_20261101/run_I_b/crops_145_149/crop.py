"""Crop small regions of the 300 dpi strips and enlarge them.
usage: python crop.py NAME STRIP x0 y0 x1 y1 [SCALE]   (coordinates in original strip pixels)"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
run = here.parent
name, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 3.0
im = Image.open(run / strip)
box = (max(0, x0), max(0, y0), min(im.width, x1), min(im.height, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = here / f"{name}.png"
c.save(out)
print(out, c.size)
