import sys
from PIL import Image

base = r"user\Documents\ega_scan_check_20261101\run_II"
# name, page, strip, x0, y0, x1, y1 (original strip pixels), scale
jobs = [
    ("p60_gamma.png", 60, 1, 1650, 350, 2140, 425, 2),
    ("p60_paren.png", 60, 1, 380, 610, 1000, 690, 2),
    ("p60_et.png", 60, 1, 1700, 545, 2160, 620, 2),
    ("p60_dot.png", 60, 2, 520, 170, 900, 240, 3),
    ("p60_ref.png", 60, 2, 1200, 690, 1700, 760, 2),
    ("p61_comma.png", 61, 2, 1450, 210, 2080, 270, 2),
    ("p61_b.png", 61, 2, 600, 435, 1000, 495, 2.5),
    ("p62_affine.png", 62, 1, 360, 325, 1000, 385, 2),
    ("p62_tilde.png", 62, 1, 1100, 690, 1340, 765, 3),
    ("p62_nu.png", 62, 1, 360, 695, 700, 765, 3),
    ("p62_etde.png", 62, 3, 1500, 700, 2100, 760, 2),
    ("p63_psi.png", 63, 1, 270, 430, 900, 485, 2),
    ("p63_tilde.png", 63, 3, 940, 335, 1330, 400, 3),
    ("p63_est.png", 63, 4, 1600, 280, 2000, 330, 3),
    ("p64_oy.png", 64, 2, 480, 85, 1300, 135, 2),
    ("p64_nu.png", 64, 2, 880, 210, 1200, 265, 3),
    ("p64_w.png", 64, 2, 590, 390, 1400, 450, 2),
    ("p64_ref.png", 64, 2, 380, 555, 1000, 605, 2.5),
    ("p64_tn.png", 64, 4, 1250, 45, 1700, 100, 3),
]
only = set(sys.argv[1:])
for name, page, strip, x0, y0, x1, y1, sc in jobs:
    if only and name not in only:
        continue
    im = Image.open(rf"{base}\page_{page:03d}_s{strip}.png")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    c.save(rf"{base}\crops_060_064\{name}")
    print(name, im.size, c.size)
