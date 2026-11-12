"""Compare page_NNN.tex bodies with the current source segments; optionally check fix 'old' strings.

usage: python segcheck.py [FINDINGS.json]
"""
import json
import pathlib
import re
import sys
import difflib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
SRC = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-21a-fr.tex"
RUN = E / "run_IV4"
PAGES = range(265, 270)

src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(src)
    seg[n] = src[s:e]

pages = {}
for p in PAGES:
    pt = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pt.split("\n", 1)[1]
    pages[p] = body
    same = body == seg[p]
    print(p, "same" if same else "DIFF", len(body), len(seg[p]))
    if not same:
        for line in difflib.unified_diff(body.splitlines(), seg[p].splitlines(), "page", "source", lineterm="", n=1):
            print("   ", line[:220])

if len(sys.argv) > 1:
    items = json.load(open(sys.argv[1], encoding="utf-8"))
    # simulate sequential application per page, as apply_fixes.py does
    cur = {p: seg[p] for p in PAGES}
    bad = 0
    for k, x in enumerate(items):
        fx = x.get("fix")
        p = int(x["page"])
        if not fx:
            continue
        old, new = fx["old"], fx["new"]
        c_page = pages[p].count(old)
        c_seq = cur[p].count(old)
        c_file = src.count(old)
        flag = "" if (c_seq == 1) else "  <-- PROBLEM"
        if c_seq != 1:
            bad += 1
        print(f"#{k:02d} p{p} page_tex={c_page} seq={c_seq} whole_file={c_file}{flag}  {old[:70]!r}")
        if c_seq == 1:
            cur[p] = cur[p].replace(old, new)
    print("problems:", bad)
    for p in PAGES:
        (RUN / "crops_265_269" / f"after_{p}.tex").write_text(cur[p], encoding="utf-8", newline="\n")
