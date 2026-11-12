"""ink.py PAGE STRIP x0 y0 x1 y1 [THRESH] -> dark-pixel count, bbox of dark pixels, and an ASCII map."""
import sys, os
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
run = os.path.dirname(here)
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(os.path.join(run, f'page_{int(page):03d}_s{strip}.png')).convert('L')
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
dark = [(x, y) for y in range(h) for x in range(w) if px[x, y] < thr]
print('dark', len(dark))
if dark:
    xs = [p[0] for p in dark]; ys = [p[1] for p in dark]
    print('bbox', min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0)
for y in range(h):
    print(''.join('#' if px[x, y] < thr else '.' for x in range(w)))
