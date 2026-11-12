"""Crop a region of a strip given in display coordinates (the 2000-px-wide view).

usage: python crop.py PAGE STRIP x0 y0 x1 y1 NAME [ZOOM]
"""
import sys
from pathlib import Path
from PIL import Image

here = Path(__file__).resolve().parent
run = here.parent
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
name = sys.argv[7]
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{page}_s{strip}.png")
scale = im.width / 2000.0
box = (int(x0 * scale), int(y0 * scale), int(x1 * scale), int(y1 * scale))
c = im.crop(box)
c = c.resize((int(c.width * zoom), int(c.height * zoom)), Image.LANCZOS)
c.save(here / f"{name}.png")
print(here / f"{name}.png", c.size)
