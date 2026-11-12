import sys
from PIL import Image
import numpy as np
def runs(p, s, box, thr=128):
    im = Image.open(r'user/Documents/ega_scan_check_20261101/run_IV4/page_%s_s%s.png' % (p, s)).convert('L')
    a = np.array(im.crop(box)) < thr
    rl = []
    for row in a:
        c = 0
        for v in row:
            if v: c += 1
            elif c: rl.append(c); c = 0
        if c: rl.append(c)
    rl = np.array(rl)
    return len(rl), float(np.median(rl)) if len(rl) else 0, float(rl.mean()) if len(rl) else 0, a.mean()
for name, args in [
    ('bold lien p136 s2', ('136', '2', (405, 360, 520, 420))),
    ('lien of hensélien p136 s3', ('136', '3', (1990, 290, 2110, 350))),
    ('hensé- p136 s2', ('136', '2', (1950, 305, 2130, 365))),
]:
    print(name, runs(*args))
