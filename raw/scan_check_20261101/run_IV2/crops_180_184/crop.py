"""Crop helper for pages 180-184 (run_IV2).

Usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 SCALE NAME
Coordinates are in ORIGINAL pixels of page_PPP_sS.png.
"""
import sys
from PIL import Image

run = r"user\Documents\ega_scan_check_20261101\run_IV2"
out = run + r"\crops_180_184"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(rf"{run}\page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{out}\{name}.png")
print(im.size, c.size)
