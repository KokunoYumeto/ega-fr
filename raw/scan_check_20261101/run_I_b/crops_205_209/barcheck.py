"""Row darkness profile above the two K_1 of '𝔎_1=𝔎_1/𝔎_1^2' on p. 207 strip 2 (looks for an overline)."""
from PIL import Image
im = Image.open(r"user\Documents\ega_scan_check_20261101\run_I_b\page_207_s2.png").convert("L")
# first K_1 roughly x 1515-1575 (orig), second K_1 roughly x 1610-1660; line band y 455-560
for name, (x0, x1) in {"first K1": (1505, 1580), "second K1": (1610, 1665)}.items():
    print(name)
    for y in range(455, 545, 3):
        row = [im.getpixel((x, y)) for x in range(x0, x1)]
        dark = sum(1 for v in row if v < 128)
        print(f"  y={y:3d} dark={dark:3d} " + "#" * dark)
