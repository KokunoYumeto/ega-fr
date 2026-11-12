"""Measure the slant of parentheses: x of the top-most and bottom-most dark pixel of a glyph box."""
import sys
from PIL import Image
RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
def measure(page, strip, box):
    im = Image.open(RUN + rf"\page_{page}_s{strip}.png").convert("L")
    px = im.load()
    x0, y0, x1, y1 = box
    pts = [(x, y) for y in range(y0, y1) for x in range(x0, x1) if px[x, y] < 110]
    if not pts:
        return None
    ys = [p[1] for p in pts]
    top, bot = min(ys), max(ys)
    topx = sum(x for x, y in pts if y <= top + 2) / len([1 for x, y in pts if y <= top + 2])
    botx = sum(x for x, y in pts if y >= bot - 2) / len([1 for x, y in pts if y >= bot - 2])
    minx = min(p[0] for p in pts)
    return dict(top=top, bot=bot, topx=round(topx, 1), botx=round(botx, 1), leftmost=minx, slant=round((topx - botx) / (bot - top), 3))
for arg in sys.argv[1:]:
    page, strip, x0, y0, x1, y1 = arg.split(',')
    print(arg, measure(page, int(strip), tuple(int(v) for v in (x0, y0, x1, y1))))
