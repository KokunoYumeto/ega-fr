"""findA.py: find roman capital A glyphs on the strips of the given pages by template matching (normal A from
page 206 s3 'un A-module plat et que', x~1025 y~140) and print their stroke weight, to spot wrong-fount bold A.
usage: python findA.py PAGE [PAGE ...]"""
import sys, pathlib
import numpy as np
from PIL import Image
from scipy import ndimage

here = pathlib.Path(__file__).resolve().parent
G = 28


def comps(im):
    band = im < 140
    lab, n = ndimage.label(band, structure=np.ones((3, 3)))
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        m = lab[sl] == i
        out.append((sl, w, h, m))
    return out


def norm(m):
    return np.array(Image.fromarray((m * 255).astype(np.uint8)).resize((G, G), Image.BILINEAR)) / 255.0


def run(m):
    rs = []
    for r in m:
        d = np.diff(np.concatenate(([0], r.astype(int), [0])))
        rs += list(np.where(d == -1)[0] - np.where(d == 1)[0])
    return float(np.mean(rs)) if rs else 0.0


ref_im = np.array(Image.open(here.parent / "page_206_s3.png").convert("L"))
tmpl = None
for sl, w, h, m in comps(ref_im[120:180, 1000:1060]):
    if 20 <= h <= 30 and 20 <= w <= 30:
        tmpl = norm(m)
assert tmpl is not None
for page in map(int, sys.argv[1:]):
    for s in range(1, 5):
        im = np.array(Image.open(here.parent / f"page_{page:03d}_s{s}.png").convert("L"))
        for sl, w, h, m in comps(im):
            if not (20 <= h <= 36 and 18 <= w <= 40):
                continue
            g = norm(m)
            score = float((g * tmpl).sum() / np.sqrt((g * g).sum() * (tmpl * tmpl).sum()))
            if score > 0.80:
                print("p%d s%d x=%4d y=%4d w=%2d h=%2d ink=%4d run=%.2f score=%.2f" % (
                    page, s, sl[1].start, sl[0].start, w, h, int(m.sum()), run(m), score))
