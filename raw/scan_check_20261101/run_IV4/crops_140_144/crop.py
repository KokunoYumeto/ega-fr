"""Crop a region of a strip image (coordinates in the ORIGINAL strip pixels) and save it enlarged.
usage: python crop.py PAGE STRIP x0 y0 x1 y1 OUTNAME [scale]"""
import sys
import pathlib
from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
OUT = RUN / "crops_140_144"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT / name)
print(OUT / name, im.size, c.size)
