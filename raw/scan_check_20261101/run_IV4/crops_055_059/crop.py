"""Crop a region of a strip image and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
Coordinates are in the strip's original pixels.
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
img = Image.open(RUN / f"page_{int(page):03d}_s{strip}.png")
box = (int(x0), int(y0), int(x1), int(y1))
c = img.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(Path(__file__).resolve().parent / out)
print(out, c.size)
