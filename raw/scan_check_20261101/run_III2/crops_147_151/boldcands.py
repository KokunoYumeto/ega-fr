import sys, json
import numpy as np
from PIL import Image
# candidates of heavy words (mean horizontal dark run > ratio * line median), saved as a contact sheet
pages = sys.argv[1].split(",")
ratio = float(sys.argv[2]); out = sys.argv[3]
cands = []
for p in pages:
    for s in (1, 2, 3, 4):
        path = f"page_{p}_s{s}.png"
        g = Image.open(path).convert("L")
        im = np.array(g) < 128
        rows = im.sum(axis=1)
        lines, inl, st = [], False, 0
        for y, r in enumerate(rows):
            if r > 3 and not inl: inl, st = True, y
            elif r <= 3 and inl:
                inl = False
                if y - st > 15: lines.append((st, y))
        for (y0, y1) in lines:
            if y1 - y0 > 80: continue  # skip tall display lines
            band = im[y0:y1]; col = band.sum(axis=0)
            words, inword, start, gap = [], False, 0, 0
            for x, c in enumerate(col):
                if c > 0:
                    if not inword: inword, start = True, x
                    gap = 0
                elif inword:
                    gap += 1
                    if gap > 9: words.append((start, x - gap)); inword = False
            if inword: words.append((start, len(col) - 1))
            means = []
            for a, b in words:
                w = band[:, a:b + 1]; runs = []
                for row in w:
                    r = 0
                    for v in row:
                        if v: r += 1
                        elif r: runs.append(r); r = 0
                    if r: runs.append(r)
                means.append(np.mean(runs) if runs else 0)
            med = np.median(means)
            for (a, b), m in zip(words, means):
                if m > ratio * med and b - a > 15:
                    cands.append((p, s, y0, y1, a, b, round(m / med, 2)))
print(len(cands))
sheet_rows = []
for (p, s, y0, y1, a, b, r) in cands:
    g = Image.open(f"page_{p}_s{s}.png").convert("L")
    cr = g.crop((max(0, a - 60), y0 - 5, min(g.width, b + 60), y1 + 5))
    sheet_rows.append((cr, f"{p} s{s} y{y0} x{a}-{b} r{r}"))
    print(p, s, y0, y1, a, b, r)
W = max(c.width for c, _ in sheet_rows) if sheet_rows else 10
H = sum(c.height + 8 for c, _ in sheet_rows) if sheet_rows else 10
sheet = Image.new("L", (W, H), 255)
y = 0
for c, _ in sheet_rows:
    sheet.paste(c, (0, y)); y += c.height + 8
sheet.save(out)
