"""Crop a region of a strip image and enlarge it.
usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
Coordinates are in the strip's original pixels."""
import sys
import pathlib
from PIL import Image

run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(run / "crops_132_136" / out)
print(im.size, c.size)
