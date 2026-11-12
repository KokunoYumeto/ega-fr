"""Crop a region of a strip image and optionally enlarge it.
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
Coordinates are in the ORIGINAL strip pixels (2465 px wide)."""
import sys
import pathlib
from PIL import Image

run = pathlib.Path(__file__).resolve().parent.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
img = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = img.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = pathlib.Path(__file__).resolve().parent / f"{name}.png"
c.save(out)
print(out, c.size)
