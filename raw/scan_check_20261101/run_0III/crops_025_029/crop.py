"""Crop small regions of the 300-dpi strips (full-resolution pixel boxes) and enlarge them 2x.
usage: python crop.py NAME STRIP x0 y0 x1 y1 [NAME STRIP x0 y0 x1 y1 ...]"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
run = here.parent
args = sys.argv[1:]
for k in range(0, len(args), 6):
    name, strip, x0, y0, x1, y1 = args[k], args[k + 1], *map(int, args[k + 2:k + 6])
    im = Image.open(run / strip)
    w, h = im.size
    box = (max(0, x0), max(0, y0), min(w, x1), min(h, y1))
    c = im.crop(box)
    c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
    c.save(here / f"{name}.png")
    print(name, strip, box, c.size)
