import sys
from PIL import Image
import numpy as np
# usage: leftedge.py image y0 y1 [y0 y1 ...]  -> leftmost dark pixel x in each band
im = np.array(Image.open(sys.argv[1]).convert('L'))
args = list(map(int, sys.argv[2:]))
for y0, y1 in zip(args[::2], args[1::2]):
    band = im[y0:y1, :]
    cols = np.where((band < 128).sum(axis=0) > 0)[0]
    print(y0, y1, cols.min() if len(cols) else None, cols.max() if len(cols) else None)
