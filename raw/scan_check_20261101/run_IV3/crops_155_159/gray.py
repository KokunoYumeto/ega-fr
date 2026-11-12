import sys
from PIL import Image

# usage: gray.py <page> <strip> <x0> <y0> <x1> <y1>: print the darkest value per column and an ASCII map
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
chars = " .:-=+*#%@"
for y in range(y0, y1):
    row = ""
    for x in range(x0, x1):
        v = im.getpixel((x, y))
        row += chars[min(9, (255 - v) * 10 // 256)]
    print(f"{y:4d} {row}")
