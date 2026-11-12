"""Crop a region of a strip image and enlarge it.

Usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
Coordinates are in the strip's original pixel frame.
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0III")
OUT = RUN / "crops_015_019"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT / name)
print(OUT / name, c.size)
