import sys
from PIL import Image
# usage: dash.py page strip x0 y0 x1 y1 : report the longest horizontal dark run (thickness>=2 rows) in box
page, strip = sys.argv[1], sys.argv[2]
x0,y0,x1,y1 = map(int, sys.argv[3:7])
im = Image.open(r"user\Documents\ega_scan_check_20261101\run_II\page_%s_s%s.png" % (page, strip)).convert('L')
px = im.load()
best=(0,None,None)
for y in range(y0,y1):
    run=0; start=None
    for x in range(x0,x1):
        if px[x,y] < 110:
            if run==0: start=x
            run+=1
            if run>best[0]: best=(run,y,start)
        else:
            run=0
print(sys.argv[1:7], 'longest run px:', best[0], 'at y', best[1], 'x from', best[2])
