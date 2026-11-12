"""Crop regions from the 300-dpi strips (coordinates in the 2000-px display frame) and enlarge them.
usage: python -I crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [ZOOM]"""
import pathlib
import sys

from PIL import Image

run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
out = run / "crops_210_214"
name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8])
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
f = im.size[0] / 2000.0
box = (int(x0 * f), int(y0 * f), int(x1 * f), int(y1 * f))
c = im.crop(box)
c = c.resize((int(c.size[0] * zoom), int(c.size[1] * zoom)), Image.LANCZOS)
c.save(out / f"{name}.png")
print(name, box, c.size)
