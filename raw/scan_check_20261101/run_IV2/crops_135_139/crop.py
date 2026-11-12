"""Crop a region of a strip image and enlarge it.
usage: python crop.py IMAGE X0 Y0 X1 Y1 SCALE OUT   (original pixel coordinates)"""
import sys

from PIL import Image

img, x0, y0, x1, y1, scale, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(img).convert("L").crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(out)
print(out, im.size)
