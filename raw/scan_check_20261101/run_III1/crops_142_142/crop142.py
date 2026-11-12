import sys, pathlib
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
# name, strip, x0, y0, x1, y1 (original pixel coordinates), scale
jobs = [
    ("a_no3",        1, 1000, 600, 1650, 680, 2),
    ("b_kofy",       2,  420,  15, 1450,  95, 2),
    ("c_OXy",        2, 1400,  15, 2200, 100, 2),
    ("d_461",        2,  950, 110, 1650, 200, 2),
    ("e_462",        2,  440, 280, 1100, 345, 2),
    ("f_465",        2,  440, 470, 2200, 600, 1),
    ("g_II427",      2, 1750, 770, 2200, 835, 2),
    ("h_fz",         3,  440, 255, 1800, 320, 1),
    ("i_item_i",     3,  540, 305, 1700, 375, 1),
    ("j_resp2",      3, 1300, 365, 2200, 430, 2),
    ("k_item_ii",    3,  540, 480, 1000, 545, 2),
    ("l_Vy",         3,  440, 715, 1300, 790, 2),
    ("m_Vy2",        4,  440,  30,  900, 100, 2),
    ("n_II611",      4,  440,  90, 1500, 160, 2),
    ("o_proof_i",    4,  540, 265, 2200, 330, 1),
    ("p_II543",      4, 1300, 265, 2000, 330, 3),
]
for name, s, x0, y0, x1, y1, sc in jobs:
    im = Image.open(run / f"page_142_s{s}.png")
    c = im.crop((x0, y0, min(x1, im.width), min(y1, im.height)))
    if sc != 1:
        c = c.resize((c.width * sc, c.height * sc), Image.LANCZOS)
    c.save(out / f"{name}.png")
print("ok")
