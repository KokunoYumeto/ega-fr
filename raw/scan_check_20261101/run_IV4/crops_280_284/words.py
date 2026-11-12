import sys
from PIL import Image

# usage: words.py page strip y0 y1 [gap]
# splits the band into words by vertical white gaps and prints stroke metrics per word
base = r'user/Documents/ega_scan_check_20261101/run_IV4/'
page, strip, y0, y1 = [int(v) for v in sys.argv[1:5]]
gap = int(sys.argv[5]) if len(sys.argv) > 5 else 14
im = Image.open(base + 'page_%d_s%d.png' % (page, strip)).convert('L')
w, h = im.size
px = im.load()
T = 128
cols = [sum(1 for y in range(y0, y1) if px[x, y] < T) for x in range(w)]
words = []
x = 0
while x < w:
    if cols[x] > 0:
        s = x
        last = x
        while x < w:
            if cols[x] > 0:
                last = x
            elif x - last > gap:
                break
            x += 1
        words.append((s, last + 1))
    x += 1


def metrics(x0, x1):
    hr = []
    dark = 0
    for y in range(y0, y1):
        run = 0
        for xx in range(x0, x1):
            if px[xx, y] < T:
                dark += 1
                run += 1
            elif run:
                hr.append(run)
                run = 0
        if run:
            hr.append(run)
    vr = []
    for xx in range(x0, x1):
        run = 0
        for y in range(y0, y1):
            if px[xx, y] < T:
                run += 1
            elif run:
                vr.append(run)
                run = 0
        if run:
            vr.append(run)
    return dark, (sum(hr) / len(hr) if hr else 0), (sum(vr) / len(vr) if vr else 0)


for i, (a, b) in enumerate(words):
    d, mh, mv = metrics(a, b)
    print('%2d x=%4d-%4d w=%3d dark=%5d hrun=%.2f vrun=%.2f' % (i, a, b, b - a, d, mh, mv))
