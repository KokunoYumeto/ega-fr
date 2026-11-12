"""Crop a region of a strip image and enlarge it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE NAME
coordinates are in the ORIGINAL strip pixels (2323 px wide).
"""
import sys
from pathlib import Path
from PIL import Image

run = Path(__file__).resolve().parent.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
img = Image.open(run / f"page_{page:03d}_s{strip}.png")
box = img.crop((x0, y0, x1, y1))
if scale != 1:
    box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
out = Path(__file__).resolve().parent / f"{name}.png"
box.save(out)
print(out, box.size)
