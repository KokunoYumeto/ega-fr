"""stems.py spec [spec ...]; spec = page:strip:x0:y0:x1:y1.
For each crop: dark-pixel runs (threshold 128) on every row; prints the median run length of
rows in the middle half of the glyph's dark rows, and the number of dark pixels."""
import sys, statistics
from PIL import Image
for spec in sys.argv[1:]:
    page, strip, x0, y0, x1, y1 = spec.split(':')
    im = Image.open(r'user\Documents\ega_scan_check_20261101\run_IV2\page_%s_s%s.png' % (page, strip)).convert('L')
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    w, h = c.size
    px = c.load()
    rows = []
    for y in range(h):
        runs, r = [], 0
        for x in range(w):
            if px[x, y] < 128:
                r += 1
            elif r:
                runs.append(r); r = 0
        if r:
            runs.append(r)
        rows.append(runs)
    dark_rows = [y for y in range(h) if rows[y]]
    if not dark_rows:
        print(spec, 'no ink'); continue
    top, bot = dark_rows[0], dark_rows[-1]
    mid = [run for y in range(top + (bot - top) // 4, bot - (bot - top) // 4 + 1) for run in rows[y]]
    total = sum(1 for y in range(h) for x in range(w) if px[x, y] < 128)
    print(spec, 'height %d, median mid-run %.1f, runs %s, dark px %d' % (bot - top + 1, statistics.median(mid), sorted(mid)[:12], total))
