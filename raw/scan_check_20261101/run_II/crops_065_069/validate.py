"""Validate findings_065_069.json: every fix 'old' occurs exactly once in page_NNN.tex (CRLF normalised),
and sequential application (list order) works both on the page copies and on the release segments.
Read-only: writes nothing."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
items = json.load(open(RUN / "findings_065_069.json", encoding="utf-8"))
print("items:", len(items))
keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "italics", "missing", "extra", "number", "punctuation",
         "misprint_in_print", "convention", "marker", "other"}
ok = True
for i, x in enumerate(items):
    miss = keys - set(x)
    if miss:
        print(i, "missing keys", miss); ok = False
    if x["kind"] not in kinds:
        print(i, "bad kind", x["kind"]); ok = False
    if x["kind"] == "convention" and not x.get("convention"):
        print(i, "convention number missing"); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(i, "misprint without corrected"); ok = False

# 1. uniqueness in the page copies (original text)
pages = {}
for x in items:
    p = int(x["page"])
    if p not in pages:
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
for i, x in enumerate(items):
    fx = x["fix"]
    if fx is None:
        continue
    if fx["old"] == fx["new"]:
        print(i, "old == new"); ok = False
    c = pages[int(x["page"])].count(fx["old"])
    if c != 1:
        print(i, f"page {x['page']}: old occurs {c} times in page copy:", repr(fx["old"])); ok = False

# 2. sequential application on page copies
cur = dict(pages)
for i, x in enumerate(items):
    fx = x["fix"]
    if fx is None:
        continue
    p = int(x["page"])
    c = cur[p].count(fx["old"])
    if c != 1:
        print(i, f"sequential (page copy) p{p}: old occurs {c} times"); ok = False
        continue
    cur[p] = cur[p].replace(fx["old"], fx["new"])

# 3. sequential application on the release segments (as apply_fixes.py does)
t = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def seg(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for k, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[k + 1][1] if k + 1 < len(cuts) else len(text)
    return None, None


for i, x in enumerate(items):
    fx = x["fix"]
    if fx is None:
        continue
    p = int(x["page"])
    s, e = seg(t, p)
    sg = t[s:e]
    c = sg.count(fx["old"])
    if c != 1:
        print(i, f"release p{p}: old occurs {c} times"); ok = False
        continue
    t = t[:s] + sg.replace(fx["old"], fx["new"]) + t[e:]

# show the two page-boundary results
for p in (65, 66):
    k = t.find("\\oldpage[II]{%d}" % p)
    print(repr(t[k - 40:k + 50]))
print("OK" if ok else "PROBLEMS")
