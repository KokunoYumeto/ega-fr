import sys
import numpy as np
from PIL import Image
from scipy import ndimage
# usage: stroke.py strip x0 y0 x1 y1  -> lists connected components with bbox, area, median horizontal run length
src = sys.argv[1]; x0, y0, x1, y1 = map(int, sys.argv[2:6])
im = np.array(Image.open(src).convert('L').crop((x0, y0, x1, y1)))
bw = im < 128
lab, n = ndimage.label(bw)
for k in range(1, n + 1):
    ys, xs = np.where(lab == k)
    if len(ys) < 15:
        continue
    sub = (lab[ys.min():ys.max() + 1, xs.min():xs.max() + 1] == k)
    runs = []
    for row in sub:
        r = 0
        for v in row:
            if v: r += 1
            elif r: runs.append(r); r = 0
        if r: runs.append(r)
    vr = []
    for col in sub.T:
        r = 0
        for v in col:
            if v: r += 1
            elif r: vr.append(r); r = 0
        if r: vr.append(r)
    print(f"comp bbox x{x0+xs.min()}-{x0+xs.max()} y{y0+ys.min()}-{y0+ys.max()} h={ys.max()-ys.min()+1} w={xs.max()-xs.min()+1} area={len(ys)} medHrun={np.median(runs):.1f} medVrun={np.median(vr):.1f}")
