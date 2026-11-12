import sys, os
from PIL import Image
# usage: crop.py name page strip x0 y0 x1 y1 [scale]
run = r"user\Documents\ega_scan_check_20261101\run_0IV1"
out = os.path.join(run, "crops_126_130")
args = sys.argv[1:]
i = 0
while i < len(args):
    name, page, strip, x0, y0, x1, y1, scale = args[i:i+8]
    i += 8
    im = Image.open(os.path.join(run, f"page_{int(page):03d}_s{strip}.png"))
    box = tuple(int(v) for v in (x0, y0, x1, y1))
    c = im.crop(box)
    s = float(scale)
    if s != 1:
        c = c.resize((int(c.width*s), int(c.height*s)), Image.LANCZOS)
    c.save(os.path.join(out, name + ".png"))
    print(name, im.size, box, c.size)
