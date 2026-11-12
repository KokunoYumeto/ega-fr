"""crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [ZOOM]: coordinates in the 2000-px-wide display frame of the strip."""
import sys, pathlib
from PIL import Image
page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png")
f = im.width / 2000.0
box = tuple(int(round(float(v) * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * zoom / f), int(c.height * zoom / f)), Image.LANCZOS)
out = run / "crops_190_194" / f"{name}.png"
c.save(out)
print(out, c.size)
