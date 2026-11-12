"""Crop and enlarge spots of the page strips for the 205-209 check.
usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]
Coordinates are in ORIGINAL strip pixels. Output: crops_205_209/NAME.png"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
OUT = RUN / "crops_205_209"

name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = (int(v) for v in sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT / f"{name}.png")
print(name, im.size, "->", c.size)
