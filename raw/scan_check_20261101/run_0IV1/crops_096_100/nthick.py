"""Stroke thickness (area / skeleton length) of the italic n found by nscan.py, to separate bold italic n from n."""
import json
import cv2
import numpy as np
from skimage.morphology import skeletonize

base = r"user\Documents\ega_scan_check_20261101\run_0IV1"
out = base + r"\crops_096_100"
rows = json.load(open(out + r"\nscan.json"))
cache = {}


def load(page, strip):
    k = (page, strip)
    if k not in cache:
        cache[k] = cv2.imread(rf"{base}\page_{page:03d}_s{strip}.png", cv2.IMREAD_GRAYSCALE)
    return cache[k]


res = []
for r in rows:
    img = load(r["page"], r["strip"])
    x, y, w, h = r["x"], r["y"], r["w"], r["h"]
    win = img[y:y + h, x:x + w]
    bw = (win < 140).astype(np.uint8)
    n, lab, stats, cent = cv2.connectedComponentsWithStats(bw, 8)
    if n <= 1:
        continue
    # component nearest the window centre with the largest area
    best = max(range(1, n), key=lambda i: stats[i, cv2.CC_STAT_AREA] - 0.5 * np.hypot(cent[i][0] - w / 2, cent[i][1] - h / 2))
    comp = (lab == best)
    area = int(comp.sum())
    sk = skeletonize(comp)
    L = max(int(sk.sum()), 1)
    bw_h = stats[best, cv2.CC_STAT_HEIGHT]
    bw_w = stats[best, cv2.CC_STAT_WIDTH]
    res.append(dict(r, area=area, skel=L, thick=round(area / L, 2), cw=int(bw_w), ch=int(bw_h)))
res.sort(key=lambda d: -d["thick"])
json.dump(res, open(out + r"\nthick.json", "w"), indent=0)
for d in res:
    print(d["page"], d["strip"], d["x"], d["y"], "thick", d["thick"], "area", d["area"], "skel", d["skel"], "box", d["cw"], d["ch"], d["tpl"], d["score"])
