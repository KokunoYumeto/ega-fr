"""Mean stroke width (median horizontal dark-run length) and ink per column in regions of a strip.

usage: python stroke.py PAGE STRIP name:x0:y0:x1:y1 [name:x0:y0:x1:y1 ...]
"""
import sys
from PIL import Image
import numpy as np

page, strip = int(sys.argv[1]), int(sys.argv[2])
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = np.array(Image.open(rf"{base}\page_{page:03d}_s{strip}.png").convert("L"))
for spec in sys.argv[3:]:
    name, x0, y0, x1, y1 = spec.split(":")
    x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
    a = im[y0:y1, x0:x1] < 128
    runs = []
    for row in a:
        n = 0
        for v in row:
            if v:
                n += 1
            elif n:
                runs.append(n)
                n = 0
        if n:
            runs.append(n)
    vruns = []
    for col in a.T:
        n = 0
        for v in col:
            if v:
                n += 1
            elif n:
                vruns.append(n)
                n = 0
        if n:
            vruns.append(n)
    cols = a.any(axis=0).sum()
    print(f"{name:12s} hrun median {np.median(runs):.1f} mean {np.mean(runs):.2f} | vrun median {np.median(vruns):.1f} "
          f"| ink/col {a.sum() / max(cols, 1):.2f}")
