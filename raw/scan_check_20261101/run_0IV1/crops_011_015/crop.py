"""Crop regions of the 300-dpi strips for close reading.
usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]
Coordinates are in the ORIGINAL strip pixels; the crop is enlarged SCALE times (default 2)."""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
run = here.parent
name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = (int(v) for v in sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(here / f"{name}.png")
print(name, im.size, c.size)
