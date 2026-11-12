"""crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]: crop a strip of the run_IV4 page (coordinates in the strip's original
pixels) and save it enlarged as crops_130_134/NAME.png."""
import pathlib
import sys

from PIL import Image

R = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(R / f"page_{int(page):03d}_s{strip}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = R / "crops_130_134" / f"{name}.png"
c.save(out)
print(out, c.size)
