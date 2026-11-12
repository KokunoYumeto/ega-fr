import sys
from PIL import Image

# usage: stroke.py page strip x0 y0 x1 y1 [label]
# prints dark-pixel count and mean horizontal / vertical run length of dark pixels (stroke-width proxy)
base = r'user/Documents/ega_scan_check_20261101/run_IV4/'
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = [int(v) for v in sys.argv[3:7]]
label = sys.argv[7] if len(sys.argv) > 7 else ''
im = Image.open(base + 'page_%d_s%d.png' % (page, strip)).convert('L')
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
T = 128
dark = 0
hruns = []
for y in range(h):
    run = 0
    for x in range(w):
        if px[x, y] < T:
            dark += 1
            run += 1
        elif run:
            hruns.append(run)
            run = 0
    if run:
        hruns.append(run)
vruns = []
for x in range(w):
    run = 0
    for y in range(h):
        if px[x, y] < T:
            run += 1
        elif run:
            vruns.append(run)
            run = 0
    if run:
        vruns.append(run)
def med(a):
    a = sorted(a)
    return a[len(a) // 2] if a else 0
mh = sum(hruns) / len(hruns) if hruns else 0
mv = sum(vruns) / len(vruns) if vruns else 0
print('%-22s dark=%6d  hrun mean=%.2f med=%d  vrun mean=%.2f med=%d' % (label, dark, mh, med(hruns), mv, med(vruns)))
