import sys
from PIL import Image

# usage: crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
# coordinates are in original strip pixels
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
base = "user/Documents/ega_scan_check_20261101/run_I_b/"
im = Image.open(f"{base}page_{page}_s{strip}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(f"{base}crops_200_204/{out}")
print(c.size)
