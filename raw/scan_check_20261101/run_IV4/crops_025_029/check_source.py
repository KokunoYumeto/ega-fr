import json, re, sys
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-16-fr.tex"
F = json.load(open(r"user\Documents\ega_scan_check_20261101\run_IV4\findings_025_029.json", encoding="utf-8"))
t = open(SRC, encoding="utf-8").read()
seg = {}
for p in range(25, 30):
    a = t.index("\\oldpage[IV-4]{%d}" % p)
    b = t.index("\\oldpage[IV-4]{%d}" % (p + 1))
    seg[p] = t[a:b]
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    o = d["fix"]["old"]
    n_seg = seg[d["page"]].count(o)
    n_all = t.count(o)
    if n_seg != 1:
        bad += 1
        print("segment count", n_seg, "page", d["page"], repr(o[:60]))
    elif n_all != 1:
        print("note: occurs", n_all, "times in the whole file (once in page segment)", d["page"], repr(o[:60]))
print("bad:", bad)
# verify the page files equal the source segments (modulo CRLF and the header line)
for p in range(25, 30):
    pf = open(r"user\Documents\ega_scan_check_20261101\run_IV4\page_%03d.tex" % p, "rb").read().decode("utf-8").replace("\r\n", "\n")
    body = pf.split("\n", 1)[1]
    print(p, "page file == source segment:", body.rstrip("\n") == seg[p].rstrip("\n"))
