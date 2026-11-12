"""Check findings_155_159.json: every fix's "old" occurs exactly once in its page_NNN.tex (CRLF -> LF)
and in the page's segment of the release file that apply_fixes.py edits; edits on one page are order-independent."""
import itertools
import json
import pathlib
import re
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
E = RUN.parent
findings = json.load(open(RUN / "findings_155_159.json", encoding="utf-8"))
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["II"]["files"]
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
segs = {}
for f in inv:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        segs.setdefault(n, t[s:e])

bad = 0
for k, x in enumerate(findings):
    for key in ("page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"):
        if key not in x:
            print("missing key", key, "in item", k); bad += 1
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("misprint without corrected:", k); bad += 1
    fix = x.get("fix")
    if not fix:
        continue
    p = x["page"]
    page = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c1, c2 = page.count(fix["old"]), segs[p].count(fix["old"])
    if c1 != 1 or c2 != 1:
        print(f"item {k} (p. {p}): old occurs {c1}x in page file, {c2}x in release segment: {fix['old']!r}"); bad += 1

# order independence: apply all fixes of a page in every pairwise order
by_page = {}
for k, x in enumerate(findings):
    if x.get("fix"):
        by_page.setdefault(x["page"], []).append((k, x["fix"]))
for p, fixes in by_page.items():
    seg = segs[p]
    for (i, a), (j, b) in itertools.permutations(fixes, 2):
        s = seg.replace(a["old"], a["new"], 1)
        if s.count(b["old"]) != 1:
            print(f"p. {p}: item {j} not applicable after item {i}"); bad += 1
    s = seg
    for _, f in fixes:
        s = s.replace(f["old"], f["new"], 1)
print("items", len(findings), "| problems", bad)
from collections import Counter
cnt = Counter()
for x in findings:
    t = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], t)] += 1
for p in sorted({x["page"] for x in findings}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
sys.exit(1 if bad else 0)
