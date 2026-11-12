"""Check findings_185_189.json: (1) each 'old' against its page_NNN.tex (CRLF -> LF), applied in list order on a
copy of the page texts; (2) simulate apply_fixes.py on a copy of the CURRENT ega4-18-fr.tex (nothing is written)."""
import json
import re

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
F = json.load(open(rf"{RUN}\findings_185_189.json", encoding="utf-8"))

# (1) page files, sequential
pages = {}
for n in range(184, 191):
    pages[n] = open(rf"{RUN}\page_{n:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
orig = dict(pages)
print("== page files (sequential) ==")
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    c0 = orig[p].count(fx["old"])
    c = pages[p].count(fx["old"])
    flag = "" if c == 1 else "  <-- PROBLEM"
    dep = "" if c0 == 1 else f" (not in the original page text: depends on an earlier edit; original count {c0})"
    if c != 1 or c0 != 1:
        print(f"#{i} p.{p} {x['kind']}: count now {c}{dep}{flag}")
    if c == 1:
        pages[p] = pages[p].replace(fx["old"], fx["new"])

# (2) source simulation with apply_fixes.locate
t = open(SRC, encoding="utf-8").read()
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


print("== source simulation ==")
bad = 0
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        bad += 1
        print(f"#{i} p.{x['page']} FAILS: old occurs {c} times: {fx['old'][:70]!r}")
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("failures:", bad)
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
print("markers 184-191 after simulation:", [n for n, s in cuts if 184 <= n <= 191])
open(rf"{RUN}\crops_185_189\simulated_ega4-18.tex", "w", encoding="utf-8", newline="").write(t)
