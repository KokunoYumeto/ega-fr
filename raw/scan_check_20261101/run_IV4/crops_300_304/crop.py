"""Crop a region of a strip image and upscale it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]
Coordinates are in the ORIGINAL strip pixels.
"""
import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4/"
OUT = RUN + "crops_300_304/"

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(RUN + "page_%s_s%s.png" % (page, strip))
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT + name + ".png")
print(OUT + name + ".png", im.size, c.size)
