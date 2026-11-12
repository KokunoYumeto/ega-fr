"""Crop a region of a page strip and enlarge it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 OUTNAME [SCALE]
Coordinates are in the ORIGINAL strip pixels.
"""
import sys
from pathlib import Path
from PIL import Image

run = Path(__file__).resolve().parent.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
img = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = img.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(Path(__file__).resolve().parent / out)
print(img.size, c.size)
