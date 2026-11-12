"""Check findings_071_075.json: every fix's old occurs once in its page_NNN.tex and in the page segment of the
r20 diplomatic release file; then simulate the apply_fixes.py sequence in memory (nothing is written)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0I")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega1\ega0-1-fr.tex")
F = json.load(open(RUN / "findings_071_075.json", encoding="utf-8"))
marker = re.compile(r"\\oldpage\[0\\textsubscript\{I\}\]\{(\d+)\}")
rel = REL.read_text(encoding="utf-8")


def segment(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, (cuts[i + 1][1] if i + 1 < len(cuts) else len(t))
    raise KeyError(page)


ok = True
for k, x in enumerate(F):
    for key in ("page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"):
        if key not in x:
            print("missing key", key, k); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("misprint without corrected", k); ok = False
    for v in (x.get("fix") or {}).values():
        if "\t" in v or "\r" in v or "\u00b6" in v:
            print("bad char in fix", k, repr(v)); ok = False
    fx = x.get("fix")
    if not fx:
        continue
    pg = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c1 = pg.count(fx["old"])
    s, e = segment(rel, x["page"])
    c2 = rel[s:e].count(fx["old"])
    flag = "" if c1 == 1 and c2 == 1 else "   <-- PROBLEM"
    if flag:
        ok = False
    print(f"{k:2d} p.{x['page']} {x['kind']:<18} page_tex={c1} release_seg={c2}{flag}  old={fx['old'][:50]!r}")

# simulate apply_fixes.py in order
t = rel
applied = 0
for k, x in enumerate(F):
    fx = x.get("fix")
    if not fx or fx["old"] == fx["new"]:
        continue
    s, e = segment(t, x["page"])
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        print("SIM FAIL", k, x["page"], repr(fx["old"][:60])); ok = False
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    applied += 1
print("simulated applied:", applied, "of", sum(1 for x in F if x.get("fix")))
for n in (71, 72, 73, 74, 75, 76):
    i = t.find(r"\oldpage[0\textsubscript{I}]{%d}" % n)
    print(f"--- around marker {n} after simulation:\n{t[i-80:i+70]!r}")
print("ALL OK" if ok else "PROBLEMS FOUND")
