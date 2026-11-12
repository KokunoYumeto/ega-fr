"""Crop helper for the pp. 10-14 scan check.

Usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
Coordinates are in the original strip pixels (2446 px wide).
Writes crops_010_014/NAME.png next to this script.
"""
import sys
from pathlib import Path
from PIL import Image

here = Path(__file__).resolve().parent
run = here.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
img = Image.open(run / f"page_{page:03d}_s{strip}.png")
box = img.crop((x0, y0, x1, y1))
if scale != 1:
    box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
out = here / f"{name}.png"
box.save(out)
print(out, box.size)
