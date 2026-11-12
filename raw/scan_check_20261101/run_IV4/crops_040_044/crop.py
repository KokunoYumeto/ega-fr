import sys
from PIL import Image

# usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
# coordinates in original strip pixels
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
OUT = RUN + "/crops_040_044"

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(f"{RUN}/page_{int(page):03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f"{OUT}/{name}.png")
print(c.size)
