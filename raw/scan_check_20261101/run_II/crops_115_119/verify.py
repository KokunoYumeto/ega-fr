import json
from collections import Counter, defaultdict

BASE = r"user\Documents\ega_scan_check_20261101\run_II"
F = json.load(open(BASE + r"\findings_115_119.json", encoding="utf-8"))
pages = {}
for n in range(115, 120):
    t = open(BASE + rf"\page_{n}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    # the apply script works on the segment from the marker on; drop the "% from" line
    pages[n] = t[t.index("\\oldpage"):]

ok = True
sim = dict(pages)
for i, d in enumerate(F):
    fx = d["fix"]
    if d["kind"] == "misprint_in_print" and "corrected" not in d:
        print("MISSING corrected", i)
    if not fx:
        continue
    old, new = fx["old"], fx["new"]
    c0 = pages[d["page"]].count(old)
    c1 = sim[d["page"]].count(old)
    if c0 != 1 or c1 != 1:
        ok = False
        print(f"#{i} p{d['page']} original count {c0}, sequential count {c1}: {old!r}")
    if c1 == 1:
        sim[d["page"]] = sim[d["page"]].replace(old, new)
print("all unique" if ok else "PROBLEMS")

cnt = defaultdict(Counter)
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[d["page"]][k] += 1
for n in sorted(cnt):
    print(n, dict(cnt[n]))
conv = Counter((d["page"], d["convention"]) for d in F if d["kind"] == "convention")
print(sorted(conv.items()))
# brace balance of every new string
for i, d in enumerate(F):
    fx = d["fix"]
    if fx:
        for s in (fx["old"], fx["new"]):
            if s.count("{") - s.count("\\{") != s.count("}") - s.count("\\}"):
                print("unbalanced braces", i, repr(s))
