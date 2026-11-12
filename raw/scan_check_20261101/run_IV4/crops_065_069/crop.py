"""Crop a region of a strip and enlarge it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]
Coordinates are in the ORIGINAL strip pixels (2478 wide).
"""
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 3.0
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{base}\crops_065_069\{name}.png")
print(c.size)
