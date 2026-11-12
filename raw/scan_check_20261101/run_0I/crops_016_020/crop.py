"""Crop regions from the strips of run_0I for close inspection (pages 16-20 checker).
usage: python crop.py STRIP X0 Y0 X1 Y1 OUTNAME [SCALE]   (coordinates in original strip pixels)"""
import pathlib
import sys

from PIL import Image

run = pathlib.Path(__file__).resolve().parent.parent
strip, x0, y0, x1, y1, outname = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(run / strip)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(pathlib.Path(__file__).resolve().parent / outname)
print(outname, c.size)
