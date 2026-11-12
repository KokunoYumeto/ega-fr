"""Crop regions of the strip images for close inspection (pages 106-110).
usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [ZOOM]
Coordinates are in ORIGINAL strip pixels; output is NAME.png in this folder, enlarged by ZOOM (default 2)."""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
run = here.parent
name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = (int(v) for v in sys.argv[4:8])
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
w, h = im.size
box = (max(0, x0), max(0, y0), min(w, x1), min(h, y1))
c = im.crop(box)
c = c.resize((int(c.width * zoom), int(c.height * zoom)), Image.LANCZOS)
c.save(here / f"{name}.png")
print(name, im.size, box, c.size)
