"""List thin horizontal bars (dashes, minus signs, rules, = strokes) in a strip.
usage: python bars.py PAGE STRIP [minw]"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

d = r"user\Documents\ega_scan_check_20261101\run_IV2"
p, s = sys.argv[1:3]
minw = int(sys.argv[3]) if len(sys.argv) > 3 else 18
a = np.array(Image.open(rf"{d}\page_{int(p):03d}_s{s}.png").convert("L")) < 128
lab, n = ndimage.label(a)
objs = ndimage.find_objects(lab)
bars = []
for i, sl in enumerate(objs):
    h = sl[0].stop - sl[0].start
    w = sl[1].stop - sl[1].start
    if w >= minw and h <= 7:
        bars.append((sl[0].start, sl[1].start, w, h))
bars.sort()
# mark pairs (= signs): another bar of similar x within 6-14 px below
for y, x, w, h in bars:
    pair = any(abs(x2 - x) <= 3 and 5 <= y2 - y <= 16 or abs(x2 - x) <= 3 and 5 <= y - y2 <= 16 for y2, x2, w2, h2 in bars if (y2, x2) != (y, x))
    print(f"y={y:4d} x={x:4d} w={w:3d} h={h} {'(=)' if pair else ''}")
