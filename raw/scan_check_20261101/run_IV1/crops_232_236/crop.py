"""Crop regions of strip images and upscale them.

Usage: python crop.py <jobs.txt>
Each line of jobs.txt: <strip.png> <x0> <y0> <x1> <y1> <out.png> [scale]
Coordinates are in the original image pixels.
"""
import sys
from PIL import Image

for line in open(sys.argv[1], encoding="utf-8"):
    parts = line.split()
    if not parts or parts[0].startswith("#"):
        continue
    src, x0, y0, x1, y1, out = parts[0], *map(int, parts[1:5]), parts[5]
    scale = float(parts[6]) if len(parts) > 6 else 2.0
    im = Image.open(src)
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
