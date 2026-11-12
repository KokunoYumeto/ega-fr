"""Crop regions from the page strips (coordinates in the 2000-px display frame) and enlarge them.

usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent

name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0

img = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
f = img.width / 2000.0
box = (int(x0 * f), int(y0 * f), int(x1 * f), int(y1 * f))
crop = img.crop(box)
crop = crop.resize((int(crop.width * scale), int(crop.height * scale)), Image.LANCZOS)
crop.save(OUT / f"{name}.png")
print(name, box, crop.size)
