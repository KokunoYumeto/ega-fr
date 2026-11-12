"""Crop a region of a strip and enlarge it.
usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE NAME   (coordinates in original strip pixels)"""
import sys
from PIL import Image

d = r"user\Documents\ega_scan_check_20261101\run_IV2"
p, s, x0, y0, x1, y1, sc, name = sys.argv[1:9]
im = Image.open(rf"{d}\page_{int(p):03d}_s{s}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
f = float(sc)
c = c.resize((int(c.width * f), int(c.height * f)), Image.LANCZOS)
c.save(rf"{d}\crops_155_159\{name}.png")
print(c.size)
