import json
from collections import Counter

BASE = r"user\Documents\ega_scan_check_20261101\run_II"
F = json.load(open(BASE + r"\findings_165_169.json", encoding="utf-8"))
pages = {}
for p in range(165, 170):
    with open(rf"{BASE}\page_{p}.tex", encoding="utf-8", newline="") as fh:
        pages[p] = fh.read().replace("\r\n", "\n")

ok = True
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    n = pages[d["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("BAD", i, d["page"], n, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("SAME", i)

# apply all fixes of a page in sequence to check independence
for p in range(165, 170):
    t = pages[p]
    for d in F:
        if d["page"] == p and d["fix"]:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print("SEQ-BAD", p, repr(d["fix"]["old"]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)

cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(165, 170):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("ALL OK" if ok else "PROBLEMS")
