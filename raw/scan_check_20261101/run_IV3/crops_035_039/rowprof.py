import sys
from PIL import Image
import numpy as np
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
base = r"user/Documents/ega_scan_check_20261101/run_IV3"
im = np.array(Image.open(f"{base}/page_{int(page):03d}_s{strip}.png").convert("L")).astype(float)
reg = im[int(y0):int(y1), int(x0):int(x1)]
for i, row in enumerate(reg):
    dark = (row < 160).sum()
    print(int(y0)+i, int(row.min()), round(row.mean(),1), dark)
