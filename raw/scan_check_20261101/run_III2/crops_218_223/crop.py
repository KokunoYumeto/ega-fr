"""Crop a region of a strip image and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
Coordinates are in the original strip pixels (2479 wide).
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user/Documents/ega_scan_check_20261101/run_III2")
OUT = RUN / "crops_218_223"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT / f"{name}.png")
print(OUT / f"{name}.png", c.size)
