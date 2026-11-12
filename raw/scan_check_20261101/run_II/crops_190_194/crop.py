"""Crop regions of the page strips for close reading (helper for the 190-194 scan check).

Usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]
Coordinates are in original strip pixels. Output: crops_190_194/NAME.png
"""
import sys
from pathlib import Path
from PIL import Image

here = Path(__file__).resolve().parent
run = here.parent
name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = (int(v) for v in sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
w, h = im.size
box = (max(0, x0), max(0, y0), min(w, x1), min(h, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(here / f"{name}.png")
print(name, im.size, box, c.size)
