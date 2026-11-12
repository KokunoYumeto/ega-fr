"""Crop a region, enlarge it, and draw vertical guide lines every 5 source pixels.

Usage: python gridcrop.py PAGE STRIP x0 y0 x1 y1 SCALE NAME
"""
import sys
from PIL import Image, ImageDraw

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = RUN + r"\crops_320_324"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = int(sys.argv[7])
name = sys.argv[8]
im = Image.open(rf"{RUN}\page_{page}_s{strip}.png").convert("RGB").crop((x0, y0, x1, y1))
im = im.resize((im.width * scale, im.height * scale), Image.NEAREST)
d = ImageDraw.Draw(im)
for x in range(0, im.width, 5 * scale):
    d.line([(x, 0), (x, im.height)], fill=(255, 0, 0), width=1)
im.save(rf"{OUT}\{name}.png")
print(im.size)
