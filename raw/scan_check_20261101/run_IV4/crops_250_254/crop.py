# crop helper: python crop.py PAGE STRIP x0 y0 x1 y1 NAME [ZOOM]
# coordinates are in the ORIGINAL strip pixels
import os
import sys
from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
base = os.path.join("C:" + os.sep, "user", "Documents", "ega_scan_check_20261101", "run_IV4")
im = Image.open(os.path.join(base, "page_%s_s%s.png" % (page, strip)))
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * zoom), int(c.height * zoom)), Image.LANCZOS)
c.save(os.path.join(base, "crops_250_254", name + ".png"))
print(im.size, c.size)
