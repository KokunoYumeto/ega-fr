import sys
from PIL import Image
# usage: runs.py page strip x0 y0 x1 y1 [threshold]  -> prints dark-run widths for rows in the box
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(r'user/Documents/ega_scan_check_20261101/run_IV4/page_%03d_s%d.png' % (page, strip)).convert('L')
for y in range(y0, y1):
    row = [im.getpixel((x, y)) < th for x in range(x0, x1)]
    runs = []
    x = 0
    while x < len(row):
        if row[x]:
            s = x
            while x < len(row) and row[x]:
                x += 1
            runs.append((s + x0, x - s))
        else:
            x += 1
    print(y, runs)
