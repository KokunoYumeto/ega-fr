"""Crop regions of the strip PNGs for close inspection (pages 160-164).

Usage: python crop.py name page strip x0 y0 x1 y1 scale [name page strip ...]
Coordinates are in original strip pixels. Output: crops_160_164/<name>.png
"""
import sys
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)

args = sys.argv[1:]
while args:
    name, page, strip, x0, y0, x1, y1, scale = args[:8]
    args = args[8:]
    src = os.path.join(RUN, f"page_{int(page):03d}_s{int(strip)}.png")
    im = Image.open(src)
    box = (int(x0), int(y0), int(x1), int(y1))
    c = im.crop(box)
    s = float(scale)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    out = os.path.join(HERE, f"{name}.png")
    c.save(out)
    print(out, c.size)
