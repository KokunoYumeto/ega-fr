"""Crop a region of a page strip and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
Coordinates are in the original strip's pixels.
"""
import sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
RUN = HERE.parent

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
img = Image.open(RUN / f"page_{page}_s{strip}.png")
box = img.crop((x0, y0, x1, y1))
if scale != 1.0:
    box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
out = HERE / f"{name}.png"
box.save(out)
print(out, img.size)
