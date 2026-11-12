"""Crop a region of a strip image and upscale it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 OUTNAME [SCALE]
Coordinates are in the ORIGINAL strip pixels (2453 px wide).
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "crops_031_035"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0

im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
box = im.crop((x0, y0, x1, y1))
box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
box.save(OUT / name)
print(OUT / name, box.size)
