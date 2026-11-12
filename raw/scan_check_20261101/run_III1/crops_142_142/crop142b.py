import pathlib
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
jobs = [
    ("q_II543_x4",   4, 1700, 270, 1880, 330, 5),
    ("r_II611_x4",   4,  830,  95, 1010, 160, 5),
    ("s_VIII_x4",    1,  740, 605,  960, 665, 5),
    ("t_I424_x4",    4, 1220,  95, 1340, 160, 5),
    ("u_Vy_x4",      3,  540, 720,  700, 795, 6),
    ("v_Vy_line_x2", 3, 1200, 715, 1600, 795, 3),
    ("w_Vy2_x4",     4,  640,  30,  760, 105, 6),
]
for name, s, x0, y0, x1, y1, sc in jobs:
    im = Image.open(run / f"page_142_s{s}.png")
    c = im.crop((x0, y0, min(x1, im.width), min(y1, im.height)))
    c = c.resize((c.width * sc, c.height * sc), Image.LANCZOS)
    c.save(out / f"{name}.png")
print("ok")
