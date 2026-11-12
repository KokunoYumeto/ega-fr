import sys
from PIL import Image
import numpy as np
# usage: rowprof.py img x0 x1 y0 y1 : print rows with dark pixel counts in the column window
im = np.array(Image.open(sys.argv[1]).convert('L'))
x0, x1, y0, y1 = map(int, sys.argv[2:6])
w = im[y0:y1, x0:x1] < 128
for i, r in enumerate(w):
    c = r.sum()
    if c:
        print(y0 + i, c, ''.join('#' if v else '.' for v in r[::max(1,(x1-x0)//100)]))
