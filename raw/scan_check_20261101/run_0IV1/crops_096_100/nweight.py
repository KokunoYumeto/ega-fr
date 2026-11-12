"""Measure the ink of small glyphs: dark-pixel count and the median horizontal run length (stroke width)."""
import sys
import numpy as np
from PIL import Image

base = r"user\Documents\ega_scan_check_20261101\run_0IV1"


def measure(page, strip, box, thr=120):
    a = np.array(Image.open(rf"{base}\page_{page:03d}_s{strip}.png").convert("L").crop(box))
    dark = a < thr
    runs = []
    for row in dark:
        c = 0
        for v in row:
            if v:
                c += 1
            elif c:
                runs.append(c)
                c = 0
        if c:
            runs.append(c)
    runs = sorted(runs)
    med = runs[len(runs) // 2] if runs else 0
    return int(dark.sum()), med, runs[-5:] if runs else []


def save(page, strip, box, name, s=8):
    c = Image.open(rf"{base}\page_{page:03d}_s{strip}.png").convert("L").crop(box)
    c.resize((c.width * s, c.height * s), Image.LANCZOS).save(rf"{base}\crops_096_100\{name}.png")


if __name__ == "__main__":
    items = [l.split() for l in sys.argv[1:]]
    for it in items:
        name, page, strip, x0, y0, x1, y1 = it[0], *map(int, it[1:])
        print(name, measure(page, strip, (x0, y0, x1, y1)))
        save(page, strip, (x0, y0, x1, y1), name)
