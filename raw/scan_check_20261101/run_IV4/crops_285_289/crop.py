import sys
from PIL import Image

# usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
base = r"user/Documents/ega_scan_check_20261101/run_IV4"
im = Image.open(f"{base}/page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f"{base}/crops_285_289/{out}")
print(c.size)
