import pathlib
from PIL import Image
D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0I")
OUT = D / "crops_036_040"
jobs = [
    ("p040_l_image", "page_040_s4.png", (1640, 295, 2060, 365), 4),
    ("p039_l_image_directe", "page_039_s2.png", (1100, 725, 2050, 790), 2),
    ("p036_l_injection", "page_036_s3.png", (280, 390, 800, 450), 3),
    ("p036_413_line1", "page_036_s3.png", (1100, 505, 2029, 560), 2),
    ("p036_413_line5", "page_036_s3.png", (280, 730, 1100, 790), 2),
    ("p036_s4_italics", "page_036_s4.png", (280, 70, 2029, 250), 1),
]
for name, f, box, z in jobs:
    im = Image.open(D / f)
    c = im.crop(box)
    c = c.resize((int(c.width * z), int(c.height * z)), Image.LANCZOS)
    c.save(OUT / (name + ".png"))
    print(name, c.size)
