"""Crop a region of a strip image and enlarge it.
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 [SCALE] [NAME]
coordinates are in the strip's original pixels."""
import pathlib
import sys

from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
name = sys.argv[8] if len(sys.argv) > 8 else f"p{page:03d}_s{strip}_{x0}_{y0}"
run = pathlib.Path(__file__).resolve().parent.parent
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = pathlib.Path(__file__).resolve().parent / f"{name}.png"
c.save(out)
print(out)
