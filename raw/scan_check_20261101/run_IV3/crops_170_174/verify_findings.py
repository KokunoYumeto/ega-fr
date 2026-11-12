import json
import os
from collections import Counter, defaultdict

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
d = json.load(open(os.path.join(RUN, "findings_170_174.json"), encoding="utf-8"))
pages = {}
ok = True
seq = defaultdict(list)
for i, x in enumerate(d):
    p = x["page"]
    if p not in pages:
        pages[p] = open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8", newline="").read().replace("\r\n", "\n")
    fx = x["fix"]
    if fx is None:
        continue
    c = pages[p].count(fx["old"])
    if c != 1:
        ok = False
        print("COUNT", c, "page", p, "item", i, repr(fx["old"]))
    seq[p].append((i, fx))

# sequential application per page
for p, fixes in seq.items():
    t = pages[p]
    for i, fx in fixes:
        c = t.count(fx["old"])
        if c != 1:
            ok = False
            print("SEQ", c, "page", p, "item", i, repr(fx["old"]))
            continue
        t = t.replace(fx["old"], fx["new"], 1)
    # crude brace balance check on the result
    if t.count("{") - t.count("\\{") != t.count("}") - t.count("\\}"):
        print("brace imbalance after edits on page", p)

cnt = defaultdict(Counter)
for x in d:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[x["page"]][k] += 1
for p in sorted(cnt):
    print(p, dict(cnt[p]))
print("CR in page files (after normalising):", {p: ("\r" in t) for p, t in pages.items()})

# uniqueness in the LF release source files (whole file and page segment)
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4"
srcfile = {170: "ega4-11-fr.tex", 171: "ega4-11-fr.tex", 172: "ega4-11-fr.tex", 173: "ega4-12-fr.tex", 174: "ega4-12-fr.tex"}
BS = chr(92)
for x in d:
    if x["fix"] is None:
        continue
    p = x["page"]
    t = open(os.path.join(SRC, srcfile[p]), encoding="utf-8", newline="").read()
    a = t.index(BS + "oldpage[IV-3]{%d}" % p)
    b = t.find(BS + "oldpage[IV-3]{%d}" % (p + 1))
    if b < 0:
        b = len(t)
    segc = t[a:b].count(x["fix"]["old"])
    filec = t.count(x["fix"]["old"])
    if segc != 1:
        ok = False
        print("SRC segment count", segc, "page", p, repr(x["fix"]["old"]))
    if filec != 1:
        print("note: occurs", filec, "times in", srcfile[p], "(once in the page segment):", repr(x["fix"]["old"])[:80])
print("ALL OK" if ok else "PROBLEMS")
print("ALL OK" if ok else "PROBLEMS")
