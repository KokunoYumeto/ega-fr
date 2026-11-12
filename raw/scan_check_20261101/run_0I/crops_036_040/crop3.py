import pathlib
from PIL import Image
D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0I")
OUT = D / "crops_036_040"
jobs = [
    ("p038_puissance", "page_038_s3.png", (300, 40, 1050, 105), 2),
    ("p037_sousalg", "page_037_s2.png", (1150, 485, 2118, 545), 1.8),
    ("p037_integre", "page_037_s3.png", (280, 365, 2118, 420), 1),
    ("p036_GF_context", "page_036_s2.png", (280, 195, 2029, 255), 1),
]
for name, f, box, z in jobs:
    im = Image.open(D / f)
    c = im.crop(box)
    c = c.resize((int(c.width * z), int(c.height * z)), Image.LANCZOS)
    c.save(OUT / (name + ".png"))
    print(name, c.size)
