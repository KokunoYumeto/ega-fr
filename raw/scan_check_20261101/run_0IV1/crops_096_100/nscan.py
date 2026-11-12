"""Find italic n glyphs on the strips of pages 96-100 by template matching and rank them by ink weight,
to spot wrong-font (bold italic) n's. Writes contact sheets for visual review."""
import json
import cv2
import numpy as np

base = r"user\Documents\ega_scan_check_20261101\run_0IV1"
out = base + r"\crops_096_100"


def load(page, strip):
    return cv2.imread(rf"{base}\page_{page:03d}_s{strip}.png", cv2.IMREAD_GRAYSCALE)


def tight(img, box, thr=140):
    x0, y0, x1, y1 = box
    a = img[y0:y1, x0:x1]
    ys, xs = np.where(a < thr)
    return x0 + xs.min(), y0 + ys.min(), x0 + xs.max() + 1, y0 + ys.max() + 1


def main():
    src = load(98, 2)
    # normal subscript n (F_{gamma,n}) and the heavy one (F_{beta,n}) on p. 98 strip 2
    tn = tight(src, (1072, 293, 1096, 320))
    tb = tight(src, (1566, 293, 1588, 320))
    T = src[tn[1] - 2:tn[3] + 2, tn[0] - 2:tn[2] + 2]
    TB = src[tb[1] - 2:tb[3] + 2, tb[0] - 2:tb[2] + 2]
    ink_t = float((255 - T.astype(np.int32)).sum())
    print("template boxes", tn, tb, "ink normal", ink_t, "ink bold", float((255 - TB.astype(np.int32)).sum()))
    rows = []
    for page in range(96, 101):
        for strip in range(1, 5):
            img = load(page, strip)
            hits = []
            for tname, tpl in (("n", T), ("nb", TB)):
                r = cv2.matchTemplate(img, tpl, cv2.TM_CCOEFF_NORMED)
                ys, xs = np.where(r > 0.62)
                for y, x in zip(ys, xs):
                    hits.append((float(r[y, x]), int(x), int(y), tpl.shape[1], tpl.shape[0], tname))
            hits.sort(reverse=True)
            kept = []
            for h in hits:
                if all(abs(h[1] - k[1]) > 8 or abs(h[2] - k[2]) > 8 for k in kept):
                    kept.append(h)
            for score, x, y, w, hgt, tname in kept:
                patch = img[y:y + hgt, x:x + w]
                ink = float((255 - patch.astype(np.int32)).sum())
                rows.append(dict(page=page, strip=strip, x=x, y=y, w=w, h=hgt, score=round(score, 3),
                                 tpl=tname, ink_ratio=round(ink / ink_t, 2)))
    rows.sort(key=lambda r: -r["ink_ratio"])
    json.dump(rows, open(out + r"\nscan.json", "w"), indent=0)
    print(len(rows), "matches")
    for r in rows[:60]:
        print(r)
    # contact sheet of all matches, sorted by ink ratio, with context
    tiles = []
    for r in rows:
        img = load(r["page"], r["strip"])
        x, y, w, h = r["x"], r["y"], r["w"], r["h"]
        c = img[max(0, y - 25):y + h + 15, max(0, x - 60):x + w + 30]
        c = cv2.resize(c, None, fx=2, fy=2, interpolation=cv2.INTER_LANCZOS4)
        canvas = np.full((130, 320), 255, np.uint8)
        hh, ww = min(c.shape[0], 110), min(c.shape[1], 320)
        canvas[20:20 + hh, :ww] = c[:hh, :ww]
        label = f"{r['page']}s{r['strip']} {r['x']},{r['y']} ink{r['ink_ratio']} {r['tpl']}{r['score']}"
        cv2.putText(canvas, label, (2, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.38, 0, 1)
        tiles.append(canvas)
    per = 6
    sheet_rows = [np.hstack(tiles[i:i + per] + [np.full((130, 320), 255, np.uint8)] * (per - len(tiles[i:i + per])))
                  for i in range(0, len(tiles), per)]
    for k in range(0, len(sheet_rows), 8):
        cv2.imwrite(out + rf"\nsheet_{k // 8:02d}.png", np.vstack(sheet_rows[k:k + 8]))


main()
