"""Crop a region of a page strip for closer inspection.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 OUTNAME [SCALE]
Coordinates are in the displayed-image frame (image width shown as 2000 px);
they are mapped to the original strip resolution before cropping.
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = RUN + r"\crops_165_169"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0

im = Image.open(rf"{RUN}\page_{page:03d}_s{strip}.png")
f = im.width / 2000.0
box = (int(x0 * f), int(y0 * f), int(x1 * f), int(y1 * f))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{OUT}\{name}.png")
print(name, box, c.size)
