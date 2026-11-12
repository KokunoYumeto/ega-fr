import json
from collections import Counter, defaultdict

base = r"user\Documents\ega_scan_check_20261101\run_IV2"
F = json.load(open(base + r"\findings_190_194.json", encoding="utf-8"))
texts = {}
for p in sorted({x["page"] for x in F}):
    texts[p] = open(base + r"\page_%03d.tex" % p, encoding="utf-8").read().replace("\r\n", "\n")

ok = True
# 1. each old exactly once in the original page text
for i, x in enumerate(F):
    fx = x["fix"]
    if fx is None:
        continue
    n = texts[x["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, x["page"], n, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("NO-OP", i, repr(fx["old"]))
# 2. sequential application per page in listed order
cur = dict(texts)
for i, x in enumerate(F):
    fx = x["fix"]
    if fx is None:
        continue
    p = x["page"]
    n = cur[p].count(fx["old"])
    if n != 1:
        ok = False
        print("SEQUENTIAL PROBLEM", i, p, n, repr(fx["old"]))
        continue
    cur[p] = cur[p].replace(fx["old"], fx["new"])
# 3. counts per page
cnt = defaultdict(Counter)
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[x["page"]][k] += 1
for p in sorted(cnt):
    print(p, dict(cnt[p]))
conv = Counter(x["convention"] for x in F if x["kind"] == "convention")
print("conventions:", dict(conv))
# sanity: required keys
for x in F:
    for k in ("page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"):
        if k not in x:
            ok = False
            print("MISSING KEY", k, x["where"])
    if x["kind"] == "convention" and not x["convention"]:
        ok = False
        print("convention kind without number", x["where"])
    if x["kind"] != "convention" and x["convention"] is not None:
        ok = False
        print("number on non-convention", x["where"])
print("ALL OK" if ok else "PROBLEMS")
