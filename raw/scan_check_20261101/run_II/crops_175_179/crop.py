import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname   (coordinates in original strip pixels)
base = r"user/Documents/ega_scan_check_20261101/run_II"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
im = Image.open(f"{base}/page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f"{base}/crops_175_179/{out}")
print(out, c.size)
