import sys, os
from PIL import Image
run = r"user\Documents\ega_scan_check_20261101\run_0IV1"
out = os.path.join(run, "crops_126_130")
# usage: compose.py outname scale page strip x0 y0 x1 y1 [page strip x0 y0 x1 y1 ...]  (stacked vertically)
name, scale = sys.argv[1], float(sys.argv[2])
a = sys.argv[3:]
ims = []
for i in range(0, len(a), 6):
    p, s, x0, y0, x1, y1 = a[i:i+6]
    im = Image.open(os.path.join(run, f"page_{int(p):03d}_s{s}.png")).convert("L").crop(tuple(map(int, (x0, y0, x1, y1))))
    ims.append(im.resize((int(im.width*scale), int(im.height*scale)), Image.LANCZOS))
W = max(i.width for i in ims); H = sum(i.height for i in ims) + 10*(len(ims)-1)
c = Image.new("L", (W, H), 255)
y = 0
for i in ims:
    c.paste(i, (0, y)); y += i.height + 10
c.save(os.path.join(out, name + ".png")); print(name, c.size)
