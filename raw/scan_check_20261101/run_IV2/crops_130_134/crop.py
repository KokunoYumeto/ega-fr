"""Crop regions of the strip images for close inspection.

usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]
Coordinates are in the 2000-px-wide display frame of the strip; they are mapped
to the original image size. Output: crops_130_134/NAME.png (upscaled by SCALE).
"""
import sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
RUN = HERE.parent

name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = map(float, sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0

img = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
f = img.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = img.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(HERE / f"{name}.png")
print(name, img.size, box, c.size)
