import sys
from PIL import Image
# usage: crop.py name page strip x0 y0 x1 y1 [scale]   (coords in original strip pixels)
base = r"user/Documents/ega_scan_check_20261101/run_III2/"
name, page, strip = sys.argv[1], sys.argv[2], sys.argv[3]
x0, y0, x1, y1 = map(int, sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(base + f"page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(base + "crops_157_161/" + name + ".png")
print(name, c.size)
