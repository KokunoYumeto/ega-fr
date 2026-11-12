"""Crop regions of the page strips (original pixel coordinates) and enlarge them.
usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]"""
import sys
import pathlib
from PIL import Image

run = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path(__file__).resolve().parent
name, page, strip, x0, y0, x1, y1 = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{int(page):03d}_s{int(strip)}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out / f"{name}.png")
print(out / f"{name}.png", c.size)
