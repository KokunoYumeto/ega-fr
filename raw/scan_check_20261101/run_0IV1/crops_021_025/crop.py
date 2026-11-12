"""Crop a region of a strip image and enlarge it.

Usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
Coordinates are in the displayed 2000-px-wide frame (multiplied by the
original/2000 factor here).
"""
import sys
from pathlib import Path
from PIL import Image

run = Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
out = run / "crops_021_025"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
img = Image.open(run / f"page_{page:03d}_s{strip}.png")
f = img.width / 2000.0
box = (int(x0 * f), int(y0 * f), int(x1 * f), int(y1 * f))
c = img.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out / f"{name}.png")
print(out / f"{name}.png", c.size)
