"""letters.py PAGE STRIP x0 y0 x1 y1 NAME SCALE [THRESH]
Crop, upscale with NEAREST (no smoothing) and optionally threshold, to inspect thin strokes."""
import sys, os
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
run = os.path.dirname(here)
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = int(sys.argv[8])
thr = int(sys.argv[9]) if len(sys.argv) > 9 else None
im = Image.open(os.path.join(run, f'page_{int(page):03d}_s{strip}.png')).convert('L')
c = im.crop((x0, y0, x1, y1))
if thr is not None:
    c = c.point(lambda v: 0 if v < thr else 255)
c = c.resize((c.width * scale, c.height * scale), Image.NEAREST)
out = os.path.join(here, name + '.png')
c.save(out)
print(out, c.size)
