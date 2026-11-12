import json
import os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.dirname(RUN)
F = json.load(open(os.path.join(RUN, "findings_196_200.json"), encoding="utf-8"))
src = open(os.path.join(BASE, "ega-fr", "source", "ega4", "ega0-22-fr.tex"), encoding="utf-8").read()
marks = {}
for p in range(196, 202):
    key = "\\oldpage[0\\textsubscript{IV-1}]{%d}" % p
    assert src.count(key) == 1, (p, src.count(key))
    marks[p] = src.index(key)
bad = 0
for f in F:
    p = f["page"]
    o = f["fix"]["old"]
    seg = src[marks[p]:marks[p + 1]]
    n = seg.count(o)
    if n != 1:
        bad += 1
        print("SRC SEGMENT COUNT", p, n, repr(o))
print("checked", len(F), "bad", bad)
# show two entries raw to confirm escaping
print(json.dumps(F[0]["fix"], ensure_ascii=False))
print(json.dumps(F[2]["fix"], ensure_ascii=False))
print(json.dumps(F[7], ensure_ascii=False))
