import pathlib
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
jobs = [  # strip, y0, y1
    ("h1", 1, 310, 610),
    ("h2", 2, 200, 420),
    ("h3", 2, 420, 640),
    ("h4", 3, 140, 400),
    ("h5", 3, 470, 660),
]
for name, s, y0, y1 in jobs:
    im = Image.open(run / f"page_142_s{s}.png").convert("L")
    for side, (x0, x1) in (("L", (440, 1320)), ("R", (1300, 2180))):
        c = im.crop((x0, y0, x1, y1))
        c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
        c.save(out / f"{name}{side}.png")
print("ok")
