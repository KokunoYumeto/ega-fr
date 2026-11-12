"""Crop a region of a strip image and enlarge it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
Coordinates are in the ORIGINAL strip pixels (2467 px wide).
"""
import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
OUT = RUN + "/crops_200_204"

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(RUN + "/page_%03d_s%d.png" % (page, strip))
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT + "/" + name)
print(OUT + "/" + name, c.size)
