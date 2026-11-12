"""Same metric as ink.py for the p. 124 diagram labels and the p. 125 lim indices."""
from PIL import Image
D = 'user/Documents/ega_scan_check_20261101/run_III1/'
regions = {
    'phi_n (4.1.4.2)': ('page_124_s3.png', (1100, 300, 1200, 345)),
    'psi_n (4.1.4.2)': ('page_124_s3.png', (1300, 300, 1420, 345)),
    'phi_n (4.1.4.3)': ('page_124_s3.png', (1110, 770, 1210, 820)),
    'psi_nX (4.1.4.3)': ('page_124_s3.png', (1300, 770, 1450, 820)),
    'k lim (4.1.7.1)': ('page_125_s3.png', (1180, 680, 1250, 720)),
    'k lim (4.1.7.2)': ('page_125_s4.png', (1150, 225, 1220, 265)),
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
        print('   x=%d y=%d w=%d h=%d ink=%d ink/(w*h)=%.2f' % (x0, y0, cw, ch, n, n / (cw * ch)))
