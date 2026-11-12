"""usage: python crop.py PAGE STRIP x0 y0 x1 y1 NAME [scale]  (coordinates in original strip pixels)"""
import sys
from PIL import Image
run = r"user\Documents\ega_scan_check_20261101\run_I_b"
page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(rf"{run}\page_{int(page):03d}_s{strip}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{run}\crops_140_144\{name}.png")
print(c.size)
