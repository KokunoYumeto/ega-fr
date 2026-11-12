from PIL import Image
base = r"user\Documents\ega_scan_check_20261101\run_II"
jobs = [
    ("p62_tilde2.png", 62, 1, 1000, 655, 1420, 770, 3),
    ("p62_tilde3.png", 62, 1, 1680, 560, 2120, 640, 3),
    ("p63_tilde2.png", 63, 3, 940, 300, 1330, 400, 3),
    ("p64_nu2.png", 64, 2, 480, 300, 760, 360, 3),
    ("p64_nu3.png", 64, 2, 1880, 550, 2100, 605, 3),
    ("p64_nu4.png", 64, 3, 960, 25, 1120, 85, 3),
    ("p64_tn2.png", 64, 3, 1500, 300, 2100, 355, 2.5),
    ("p63_est2.png", 63, 4, 1300, 270, 2000, 385, 2),
]
for name, page, strip, x0, y0, x1, y1, sc in jobs:
    im = Image.open(rf"{base}\page_{page:03d}_s{strip}.png")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    c.save(rf"{base}\crops_060_064\{name}")
    print(name, c.size)
