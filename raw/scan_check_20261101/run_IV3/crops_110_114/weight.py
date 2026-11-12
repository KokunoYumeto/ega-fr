import sys
from PIL import Image
# usage: weight.py page strip x0 y0 x1 y1 [x0 y0 x1 y1 ...]: dark pixel count, mean horizontal and vertical run (threshold 128)
page, strip = sys.argv[1:3]
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
vals = list(map(int, sys.argv[3:]))
for i in range(0, len(vals), 4):
    x0, y0, x1, y1 = vals[i:i + 4]
    dark = 0
    hr = []
    for y in range(y0, y1):
        n = 0
        for x in range(x0, x1):
            if im.getpixel((x, y)) < 128:
                dark += 1; n += 1
            elif n:
                hr.append(n); n = 0
        if n:
            hr.append(n)
    vr = []
    for x in range(x0, x1):
        n = 0
        for y in range(y0, y1):
            if im.getpixel((x, y)) < 128:
                n += 1
            elif n:
                vr.append(n); n = 0
        if n:
            vr.append(n)
    mh = sum(hr) / len(hr) if hr else 0
    mv = sum(vr) / len(vr) if vr else 0
    print((x0, y0, x1, y1), 'dark', dark, 'mean_h_run %.2f' % mh, 'mean_v_run %.2f' % mv)
