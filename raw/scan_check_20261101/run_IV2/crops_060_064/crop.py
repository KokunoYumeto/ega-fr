"""Crop a region of a strip and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
Coordinates are in the original strip pixels.
"""
import sys
from pathlib import Path
from PIL import Image

run = Path(__file__).resolve().parent.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
src = run / f"page_{page:03d}_s{strip}.png"
im = Image.open(src)
box = im.crop((x0, y0, x1, y1))
if scale != 1:
    box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
out = Path(__file__).resolve().parent / f"p{page:03d}_s{strip}_{name}.png"
box.save(out)
print(out, im.size, box.size)
