import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
x0, y0, x1, y1 = map(int, sys.argv[2].split(','))
minlen = int(sys.argv[3]) if len(sys.argv) > 3 else 12
W, H = im.size
px = im.load()
runs = []
for y in range(y0, y1):
    x = x0
    while x < x1:
        if px[x, y] < 110:
            s = x
            while x < x1 and px[x, y] < 110:
                x += 1
            if x - s >= minlen:
                runs.append((y, s, x - 1, x - s))
        else:
            x += 1
# merge runs on adjacent rows with overlapping x
groups = []
for r in runs:
    for g in groups:
        if r[0] - g['y1'] <= 1 and not (r[2] < g['xs'] - 3 or r[1] > g['xe'] + 3):
            g['y1'] = r[0]; g['xs'] = min(g['xs'], r[1]); g['xe'] = max(g['xe'], r[2]); g['n'] += 1
            break
    else:
        groups.append({'y0': r[0], 'y1': r[0], 'xs': r[1], 'xe': r[2], 'n': 1})
for g in groups:
    print('rows %d-%d  x %d-%d  len %d' % (g['y0'], g['y1'], g['xs'], g['xe'], g['xe'] - g['xs'] + 1))
