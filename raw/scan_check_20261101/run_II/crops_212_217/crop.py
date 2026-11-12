"""Crop regions of the run_II strips for pages 212-217 (helper for one checker; writes into this folder only)."""
import pathlib
import sys
from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "crops_212_217"

# name: (strip file, (x0, y0, x1, y1) in original pixels, scale)
JOBS = {
    "p217_l1_intersection": ("page_217_s2.png", (380, 0, 2000, 70), 1.0),
    "p217_formula_216": ("page_217_s2.png", (1220, 60, 1800, 165), 2.0),
    "p217_faisceaux": ("page_217_s2.png", (380, 270, 1900, 330), 1.0),
    "p217_d_ref": ("page_217_s3.png", (380, 310, 1120, 370), 1.6),
    "p217_plat": ("page_217_s3.png", (380, 425, 1860, 485), 1.0),
    "p217_Kk": ("page_217_s3.png", (1040, 645, 1700, 715), 2.0),
    "p217_et": ("page_217_s4.png", (380, 60, 1000, 125), 1.6),
    "p217_heading_0": ("page_217_s2.png", (380, 0, 620, 70), 2.5),
    "p215_backmatter": ("page_215_s2.png", (220, 0, 1000, 360), 1.0),
    "p215_errata": ("page_215_s2.png", (220, 300, 900, 360), 2.0),
    "p213_chapitre": ("page_213_s1.png", (270, 540, 2000, 660), 1.0),
    "p213_pages_5": ("page_213_s1.png", (1880, 480, 2000, 660), 2.0),
}

names = sys.argv[1:] or list(JOBS)
for n in names:
    f, box, s = JOBS[n]
    im = Image.open(RUN / f).crop(box)
    if s != 1.0:
        im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    im.save(OUT / f"{n}.png")
    print(n, im.size)
