"""Connected components in a crop: bbox, ink pixels, ink per bbox height (a stroke-weight proxy)."""
import sys
from PIL import Image
D = 'user/Documents/ega_scan_check_20261101/run_III1/'
regions = {
    'Soit x':        ('page_126_s2.png', (850, 610, 905, 665)),
    'par x':         ('page_126_s2.png', (1880, 610, 1940, 665)),
    'mu_xm display': ('page_126_s2.png', (925, 765, 1040, 825)),
    'mu_xm text':    ('page_126_s3.png', (2075, 75, 2170, 130)),
    'mu_x0 text':    ('page_126_s3.png', (2075, 520, 2170, 580)),
    'R_k':           ('page_126_s3.png', (1230, 415, 1305, 475)),
    'R_k+m':         ('page_126_s3.png', (1325, 415, 1445, 478)),
    'J^m (4.1.7.10)':('page_126_s3.png', (1175, 405, 1235, 450)),
    'H_k (4.1.7.6)': ('page_126_s2.png', (1380, 505, 1460, 560)),
}
for name, (f, box) in regions.items():
    im = Image.open(D + f).convert('L').crop(box)
    w, h = im.size
    px = im.load()
    seen = set()
    comps = []
    for y in range(h):
        for x in range(w):
            if px[x, y] < 128 and (x, y) not in seen:
                stack = [(x, y)]
                seen.add((x, y))
                pts = []
                while stack:
                    a, b = stack.pop()
                    pts.append((a, b))
                    for da in (-1, 0, 1):
                        for db in (-1, 0, 1):
                            c, d = a + da, b + db
                            if 0 <= c < w and 0 <= d < h and (c, d) not in seen and px[c, d] < 128:
                                seen.add((c, d))
                                stack.append((c, d))
                xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                if len(pts) > 25:
                    comps.append((min(xs) + box[0], min(ys) + box[1], max(xs) - min(xs) + 1, max(ys) - min(ys) + 1, len(pts)))
    comps.sort()
    print(name)
    for c in comps:
        x0, y0, cw, ch, n = c
        print('   x=%d y=%d w=%d h=%d ink=%d ink/h=%.1f ink/(w*h)=%.2f' % (x0, y0, cw, ch, n, n / ch, n / (cw * ch)))
