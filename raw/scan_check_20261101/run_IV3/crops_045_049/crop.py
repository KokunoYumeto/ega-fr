import sys, pathlib
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
out = run / "crops_045_049"
# name, strip, (x0, y0, x1, y1) in original pixels, scale
jobs = [
    ("p45_factorisation_comma", "page_045_s1.png", (1650, 610, 2425, 720), 2),
    ("p45_B_C_lambda", "page_045_s2.png", (240, 270, 2000, 390), 1),
    ("p45_display_8_12_6_1", "page_045_s4.png", (900, 180, 1350, 290), 2),
    ("p46_8_10_5_xi", "page_046_s1.png", (450, 590, 1150, 670), 2),
    ("p47_quasi_fini", "page_047_s3.png", (250, 570, 1300, 645), 2),
    ("p47_P_r_Y_1", "page_047_s2.png", (650, 330, 950, 405), 3),
    ("p47_P_r_Y_2", "page_047_s2.png", (380, 560, 560, 630), 3),
    ("p48_algebre_finie", "page_048_s3.png", (1150, 185, 1800, 250), 2),
    ("p48_respectivement", "page_048_s3.png", (1100, 595, 1500, 665), 3),
    ("p48_f_inv_U", "page_048_s1.png", (1300, 720, 1650, 805), 3),
    ("p49_est_affine", "page_049_s1.png", (650, 585, 1150, 650), 2),
    ("p49_lim_X", "page_049_s1.png", (230, 640, 600, 760), 3),
    ("p49_lim_8_13_1_1", "page_049_s2.png", (740, 150, 1050, 255), 3),
    ("p49_lim_Y_rho", "page_049_s3.png", (1450, 270, 1990, 385), 3),
    ("p49_S_lambda", "page_049_s4.png", (250, 20, 1000, 125), 2),
]
for name, strip, box, s in jobs:
    im = Image.open(run / strip)
    w, h = im.size
    b = (max(0, box[0]), max(0, box[1]), min(w, box[2]), min(h, box[3]))
    c = im.crop(b)
    if s != 1:
        c = c.resize((c.width * s, c.height * s), Image.LANCZOS)
    c.save(out / f"{name}.png")
    print(name, b, c.size)
