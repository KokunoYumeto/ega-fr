import sys, pathlib
from PIL import Image
D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0I")
OUT = D / "crops_036_040"
# name, strip file, (x0, y0, x1, y1) in original pixels, zoom
jobs = [
    ("p036_omega_flat", "page_036_s3.png", (470, 320, 720, 400), 3),
    ("p036_theta_GF", "page_036_s2.png", (1080, 185, 1420, 265), 3),
    ("p036_413_italics", "page_036_s3.png", (280, 505, 2029, 610), 1.2),
    ("p037_reduit", "page_037_s3.png", (270, 15, 780, 90), 3),
    ("p037_gradues", "page_037_s3.png", (380, 530, 1060, 610), 2.5),
    ("p038_dual", "page_038_s2.png", (1380, 540, 2097, 625), 2.5),
    ("p039_psiA", "page_039_s2.png", (600, 185, 920, 270), 3),
    ("p039_BModule", "page_039_s2.png", (300, 715, 640, 800), 3),
    ("p039_4221_end", "page_039_s4.png", (1100, 300, 1620, 405), 2.5),
    ("p040_restriction", "page_040_s2.png", (250, 185, 1150, 270), 2),
    ("p040_BAlgebre", "page_040_s2.png", (880, 575, 1260, 655), 3),
    ("p040_soient", "page_040_s3.png", (1400, 675, 2060, 765), 2.5),
    ("p040_image_reci", "page_040_s4.png", (1050, 285, 2060, 370), 2),
]
sel = set(sys.argv[1:])
for name, f, box, z in jobs:
    if sel and name not in sel:
        continue
    im = Image.open(D / f)
    c = im.crop(box)
    c = c.resize((int(c.width * z), int(c.height * z)), Image.LANCZOS)
    c.save(OUT / (name + ".png"))
    print(name, c.size)
