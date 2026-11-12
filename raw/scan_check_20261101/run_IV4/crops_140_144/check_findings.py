"""Check findings_140_144.json: every 'old' occurs exactly once in page_NNN.tex and in the current source segment,
and the edits apply in list order (each 'old' exactly once at the time it is applied). Read-only."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native\ega4\ega4-18-fr.tex")
src = SRC.read_text(encoding="utf-8")
assert "\r" not in src, "source has CR"
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = src[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src)]

pages = {}
for n in range(140, 145):
    t = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    first, rest = t.split("\n", 1)
    pages[n] = rest
    same = rest.rstrip("\n") == seg[n].rstrip("\n")
    print(f"page {n}: page file vs current segment identical: {same}")
    if not same:
        import difflib
        for line in difflib.unified_diff(seg[n].splitlines(), rest.splitlines(), lineterm="", n=0):
            print("   ", line[:200])

F = json.load(open(RUN / "findings_140_144.json", encoding="utf-8"))
work = dict(seg)
bad = 0
for k, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        continue
    n, old, new = x["page"], fx["old"], fx["new"]
    c_page = pages[n].count(old)
    c_seg = seg[n].count(old)
    c_work = work[n].count(old)
    flag = "" if (c_page == 1 and c_seg == 1 and c_work == 1) else "  <-- PROBLEM"
    if flag:
        bad += 1
    print(f"{k:2d} p{n} {x['kind']:<17} conv={x['convention']!s:<4} page={c_page} seg={c_seg} seq={c_work}{flag}  {old[:70]!r}")
    if c_work == 1:
        work[n] = work[n].replace(old, new)
print("problems:", bad, "of", len(F))
kinds = {}
for x in F:
    key = (x["page"], "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal"))
    kinds[key] = kinds.get(key, 0) + 1
for n in range(140, 145):
    print(n, "normal", kinds.get((n, "normal"), 0), "convention", kinds.get((n, "convention"), 0), "misprint", kinds.get((n, "misprint"), 0))
# show the results of the sequential application around a few spots
for n in range(140, 145):
    (RUN / "crops_140_144" / f"applied_{n}.txt").write_text(work[n], encoding="utf-8", newline="\n")
