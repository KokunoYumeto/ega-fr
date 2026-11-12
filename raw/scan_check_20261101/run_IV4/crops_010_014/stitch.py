"""Stitch the four strips of a page into one image (pp. 10-14 scan check).

Usage: python -I stitch.py PAGE            -> writes full_PAGE.png, prints row offsets
       python -I stitch.py PAGE X0 Y0 X1 Y1 SCALE NAME   -> crop from the stitched page
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image

here = Path(__file__).resolve().parent
run = here.parent


def stitched(page):
    strips = [Image.open(run / f"page_{page:03d}_s{i}.png").convert("L") for i in range(1, 5)]
    arrays = [np.asarray(s).astype(float) for s in strips]
    parts = [arrays[0]]
    offsets = [0]
    top = arrays[0].shape[0]
    for prev, cur in zip(arrays, arrays[1:]):
        # the strips overlap by 80 rows (checked on pp. 10-14; blank overlaps make a search ambiguous)
        ov = 80
        assert np.mean(np.abs(prev[-ov:, :] - cur[:ov, :])) == 0
        offsets.append(top - ov)
        parts.append(cur[ov:, :])
        top += cur.shape[0] - ov
    full = np.vstack(parts).astype(np.uint8)
    return Image.fromarray(full), offsets


page = int(sys.argv[1])
img, offsets = stitched(page)
if len(sys.argv) == 2:
    out = here / f"full_{page:03d}.png"
    img.save(out)
    print(out, img.size, "strip tops:", offsets)
else:
    x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
    scale = float(sys.argv[6])
    name = sys.argv[7]
    box = img.crop((x0, y0, x1, y1))
    if scale != 1:
        box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
    out = here / f"{name}.png"
    box.save(out)
    print(out, box.size)
