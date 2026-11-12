import sys
from PIL import Image, ImageOps

# usage: enhance.py <in.png> <out.png> x0 y0 x1 y1 scale threshold
# Darkens every pixel lighter than white by mapping [threshold, 255] -> [0, 255] to make faint ink visible.
src, dst = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
thr = int(sys.argv[8])
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
lut = [0 if v < thr else int((v - thr) * 255 / max(1, 255 - thr)) for v in range(256)]
im = im.point(lut)
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.NEAREST)
im.save(dst)
# also print a coarse map of non-white pixels
small = Image.open(src).convert("L").crop((x0, y0, x1, y1))
w, h = small.size
for yy in range(h):
    row = ""
    for xx in range(w):
        v = small.getpixel((xx, yy))
        row += "#" if v < 100 else ("+" if v < 180 else ("." if v < 240 else " "))
    print(row)
