"""Crop a region of a strip image and enlarge it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
Coordinates are in ORIGINAL pixels of page_PAGE_sSTRIP.png.
"""
import sys
from pathlib import Path
from PIL import Image

run = Path(__file__).resolve().parent.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = Path(__file__).resolve().parent / sys.argv[8]
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
