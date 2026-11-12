import sys
from PIL import Image
page, strip = sys.argv[1], sys.argv[2]
x0,y0,x1,y1 = map(int, sys.argv[3:7])
im = Image.open(r"user\Documents\ega_scan_check_20261101\run_II\page_%s_s%s.png" % (page, strip)).convert('L')
px = im.load()
for y in range(y0,y1):
    s=''.join('#' if px[x,y]<110 else ('+' if px[x,y]<180 else '.') for x in range(x0,x1))
    print('%4d %s' % (y,s))
