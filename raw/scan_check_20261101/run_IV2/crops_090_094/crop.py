"""Crop a region of a strip and enlarge it.
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]
coordinates are in the original strip pixels."""
import sys
import pathlib
from PIL import Image

run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
out = run / "crops_090_094"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out / f"{name}.png")
print(out / f"{name}.png", c.size)
