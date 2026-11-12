import pathlib
import numpy as np
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
# (label, strip, x0, x1, y0, y1): a box around ONE I glyph; stem span = last-first ink column in the middle third rows
boxes = [
    ("bold I #1 of (II, 4.2.7)", 2, 1950, 1971, 782, 813),
    ("bold I #2 of (II, 4.2.7)", 2, 1972, 1993, 782, 813),
    ("(II, 6.1.1: left I", 4, 1003, 1020, 107, 139),
    ("(II, 6.1.1: right I", 4, 1020, 1038, 107, 139),
    ("I of 'et I, 4.2.4'", 4, 1259, 1278, 107, 138),
    ("(II, 5.4.3): first I", 4, 1804, 1823, 280, 312),
    ("(II, 5.4.3): second I", 4, 1832, 1846, 280, 312),
    ("roman I of VIII (1)", 1, 932, 952, 614, 646),
    ("roman I of VIII (2)", 1, 952, 972, 614, 646),
    ("roman I of VIII (3)", 1, 972, 992, 614, 646),
]
for lab, s, x0, x1, y0, y1 in boxes:
    a = np.array(Image.open(run / f"page_142_s{s}.png").convert("L"))[y0:y1, x0:x1] < 140
    h = a.shape[0]
    spans = []
    for row in a[h // 3: 2 * h // 3]:
        idx = np.flatnonzero(row)
        if len(idx):
            spans.append(idx[-1] - idx[0] + 1)
    print(f"{lab:28s} stem span median {np.median(spans):.1f}  ink {int(a.sum())}")
