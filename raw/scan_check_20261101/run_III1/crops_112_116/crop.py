"""Crop a region of a strip and enlarge it. usage: python crop.py STRIP x0 y0 x1 y1 OUTNAME [scale]
Coordinates are in the strip's original pixels."""
import sys, pathlib
from PIL import Image
run = pathlib.Path(__file__).resolve().parent.parent
strip, x0, y0, x1, y1, name = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(run / strip)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(pathlib.Path(__file__).resolve().parent / name)
print(name, c.size)
