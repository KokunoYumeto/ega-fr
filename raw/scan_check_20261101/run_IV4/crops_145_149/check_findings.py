"""Check findings_145_149.json (read-only): every 'old' occurs exactly once in page_NNN.tex, in the current source
segment and in the whole current source file, and the edits apply in list order (each 'old' exactly once when applied)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native\ega4\ega4-18-fr.tex")
src = SRC.read_text(encoding="utf-8")
assert "\r" not in src
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = src[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src)]

pages = {}
for n in range(145, 150):
    t = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    first, rest = t.split("\n", 1)
    pages[n] = rest
    print(f"page {n}: page file identical to current segment: {rest.rstrip(chr(10)) == seg[n].rstrip(chr(10))}")

F = json.load(open(RUN / "findings_145_149.json", encoding="utf-8"))
work = dict(seg)
whole = src
bad = 0
for k, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        print(f"{k:2d} p{x['page']} {x['kind']:<17} (no fix)")
        continue
    n, old, new = x["page"], fx["old"], fx["new"]
    c_page = pages[n].count(old)
    c_seg = seg[n].count(old)
    c_file = src.count(old)
    c_work = work[n].count(old)
    c_whole = whole.count(old)
    ok = c_page == 1 and c_seg == 1 and c_file == 1 and c_work == 1 and c_whole == 1
    if not ok:
        bad += 1
    print(f"{k:2d} p{n} {x['kind']:<17} conv={x['convention']!s:<4} page={c_page} seg={c_seg} file={c_file} "
          f"seq={c_work}/{c_whole}{'' if ok else '  <-- PROBLEM'}  {old[:60]!r}")
    if c_work == 1:
        work[n] = work[n].replace(old, new)
    if c_whole == 1:
        whole = whole.replace(old, new)
    if old == new:
        print("    old == new!")
print("problems:", bad, "of", len(F))
kinds = {}
for x in F:
    key = (x["page"], "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal"))
    kinds[key] = kinds.get(key, 0) + 1
for n in range(145, 150):
    print(n, "normal", kinds.get((n, "normal"), 0), "convention", kinds.get((n, "convention"), 0),
          "misprint", kinds.get((n, "misprint"), 0))
for n in range(145, 150):
    (RUN / "crops_145_149" / f"applied_{n}.txt").write_text(work[n], encoding="utf-8", newline="\n")
