import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = r"user\Documents\ega_scan_check_20261101\run_IV4"
src = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
F = json.load(open(rf"{run}\findings_125_129.json", encoding="utf-8"))

# 1. each old exactly once in its page_NNN.tex (LF)
pages = {}
bad = 0
for i, x in enumerate(F):
    p = x["page"]
    if p not in pages:
        pages[p] = open(rf"{run}\page_{p:03d}.tex", encoding="utf-8").read().replace("\r\n", "\n")
    f = x.get("fix")
    if not f:
        continue
    c = pages[p].count(f["old"])
    if c != 1:
        bad += 1
        print("PAGE-FILE COUNT", c, "finding", i, p, repr(f["old"][:80]))
print("page-file check done, bad =", bad)

# 2. simulate apply_fixes.py (sequential, page segments) on an in-memory copy of the release file
t = open(src, encoding="utf-8").read()
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(text)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


applied = 0
for i, x in enumerate(F):
    f = x.get("fix")
    if not f:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(f["old"])
    if c != 1:
        print("SIM FAIL", c, "finding", i, x["page"], repr(f["old"][:80]))
        continue
    t = t[:s] + seg.replace(f["old"], f["new"]) + t[e:]
    applied += 1
print("simulated sequential apply:", applied, "of", sum(1 for x in F if x.get("fix")))

# 3. corrected-edition simulation: skip misprint fixes
t2 = open(src, encoding="utf-8").read()
ok2 = 0
for i, x in enumerate(F):
    f = x.get("fix")
    if not f or x["kind"] == "misprint_in_print":
        continue
    s, e = locate(t2, x["page"])
    seg = t2[s:e]
    if seg.count(f["old"]) != 1:
        print("CORRECTED-SIM FAIL finding", i, x["page"], repr(f["old"][:80]))
        continue
    t2 = t2[:s] + seg.replace(f["old"], f["new"]) + t2[e:]
    ok2 += 1
print("corrected-edition simulation applied:", ok2)

# 4. brace balance of the changed region (pages 124-130)
s, _ = locate(t, 125)
_, e = locate(t, 129)
region = t[s:e]
depth = 0
for ch in re.sub(r"\\[{}]", "", region):
    if ch == "{":
        depth += 1
    elif ch == "}":
        depth -= 1
        if depth < 0:
            print("NEGATIVE brace depth"); break
print("brace balance of pages 125-129 after fixes:", depth)
print("dollar parity:", region.count("$") % 2)
open(rf"{run}\crops_125_129\simulated_125_129.txt", "w", encoding="utf-8").write(region)

# counts per page
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(125, 130):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
