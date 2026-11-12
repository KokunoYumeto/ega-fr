"""Crop a region of a strip image and upscale it.

usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
Coordinates are in the strip's original pixels.
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_I_b"
OUT = RUN + r"\crops_150_154"

page, strip, x0, y0, x1, y1, scale = (int(a) for a in sys.argv[1:8])
name = sys.argv[8]
im = Image.open(rf"{RUN}\page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
path = rf"{OUT}\{name}.png"
c.save(path)
print(path, c.size)
