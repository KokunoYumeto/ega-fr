"""Crop a region of a page strip and enlarge it.
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
Coordinates are in the strip's original pixels; output goes next to this script."""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
run = here.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(here / f"{name}.png")
print(name, c.size)
