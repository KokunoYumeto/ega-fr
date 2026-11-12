"""Crop a region of a strip for close reading.
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 ZOOM NAME
X/Y are in the 2000-px-wide display coordinates of the strip (converted to original pixels here)."""
import pathlib
import sys

from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "crops_160_164"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
zoom, name = float(sys.argv[7]), sys.argv[8]
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * zoom), int(c.height * zoom)), Image.LANCZOS)
c.save(OUT / f"{name}.png")
print(OUT / f"{name}.png", c.size, "orig box", box)
