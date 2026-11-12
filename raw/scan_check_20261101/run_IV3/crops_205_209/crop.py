"""Crop a region of a page strip and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
Coordinates are in the strip's original pixel frame.
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "crops_205_209"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0

img = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
box = img.crop((x0, y0, x1, y1))
if scale != 1:
    box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
box.save(OUT / name)
print(OUT / name, box.size)
