import sys
import numpy as np
from PIL import Image
# usage: ink.py page strip x0 y0 x1 y1 [label]  -> stats of dark pixels in the box
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
a = sys.argv[1:]
for i in range(0, len(a), 7):
    p, s, x0, y0, x1, y1 = map(int, a[i:i+6]); lab = a[i+6]
    im = np.array(Image.open(rf"{base}\page_{p:03d}_s{s}.png").convert("L")).astype(int)
    c = im[y0:y1, x0:x1] < 128
    ys, xs = np.nonzero(c)
    if len(ys) == 0:
        print(lab, 'empty'); continue
    h = ys.max()-ys.min()+1; w = xs.max()-xs.min()+1
    # horizontal run lengths
    runs = []
    for row in c:
        r = 0
        for v in row:
            if v: r += 1
            elif r: runs.append(r); r = 0
        if r: runs.append(r)
    runs = np.array(runs)
    print(f"{lab}: dark={c.sum()} bbox={w}x{h} ink/height={c.sum()/h:.1f} median_run={np.median(runs):.1f} mean_run={runs.mean():.2f}")
