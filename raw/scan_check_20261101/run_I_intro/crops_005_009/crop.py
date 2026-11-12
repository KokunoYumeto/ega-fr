"""Crop a region of a strip and upscale it. usage: python crop.py STRIP x0 y0 x1 y1 SCALE OUTNAME (original pixel coords)"""
import sys, pathlib
from PIL import Image
d = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_intro")
strip, x0, y0, x1, y1, sc, out = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
im = Image.open(d / strip).crop((x0, y0, x1, y1))
im = im.resize((im.width * sc, im.height * sc), Image.LANCZOS)
im.save(d / "crops_005_009" / out)
print(im.size)
