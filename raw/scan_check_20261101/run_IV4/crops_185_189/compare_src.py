"""Compare run_IV4 page_NNN.tex (185-190) with the CURRENT diplomatic source segments."""
import re

SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
t = open(SRC, encoding="utf-8").read()
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    seg[n] = t[s:e]
for n in range(184, 191):
    p = open(rf"{RUN}\page_{n:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    body = p.split("\n", 1)[1]
    cont = ""
    if "% (continued in" in body:
        body, cont = body.split("% (continued in", 1)
    same = body == seg[n]
    print(n, "identical" if same else "DIFFERENT", len(body), len(seg[n]), "continued" if cont else "")
    if not same:
        # show first difference
        k = next((i for i, (a, b) in enumerate(zip(body, seg[n])) if a != b), min(len(body), len(seg[n])))
        print("   page:", repr(body[max(0, k - 80):k + 80]))
        print("   src :", repr(seg[n][max(0, k - 80):k + 80]))
