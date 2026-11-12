import sys
from PIL import Image
D = 'user/Documents/ega_scan_check_20261101/run_III1/'
for p in sys.argv[1:]:
    for s in range(1, 5):
        im = Image.open(D + 'page_%s_s%d.png' % (p, s)).convert('L')
        w, h = im.size
        px = im.load()
        rows = []
        for y in range(h):
            dark = [x for x in range(0, w, 2) if px[x, y] < 110]
            rows.append((min(dark), max(dark), len(dark)) if dark else None)
        # group consecutive dark rows into lines
        lines = []
        cur = None
        for y, r in enumerate(rows):
            if r and r[2] > 3:
                if cur is None:
                    cur = [y, y, r[0], r[1]]
                else:
                    cur[1] = y
                    cur[2] = min(cur[2], r[0])
                    cur[3] = max(cur[3], r[1])
            else:
                if cur is not None and cur[1] - cur[0] >= 12:
                    lines.append(tuple(cur))
                cur = None
        if cur is not None and cur[1] - cur[0] >= 12:
            lines.append(tuple(cur))
        print('page', p, 'strip', s)
        for l in lines:
            print('   y=%4d-%4d  left=%4d right=%4d' % l)
