"""Check findings_210_214.json: every fix 'old' occurs exactly once in its page_NNN.tex (CRLF normalised), and
simulate the sequential application (as apply_fixes.py does) on an in-memory copy of the release file."""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
run = E / "run_IV2"
findings = json.load(open(run / "findings_210_214.json", encoding="utf-8"))
ok = True
for i, x in enumerate(findings):
    fx = x.get("fix")
    if not fx:
        continue
    page_text = (run / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c = page_text.count(fx["old"])
    if c != 1:
        ok = False
        print("COUNT", c, "entry", i, "page", x["page"], repr(fx["old"][:60]))
print("page-file uniqueness:", "all ok" if ok else "PROBLEMS")

# sequential simulation on the release file
src = pathlib.Path(json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["IV-2"]["files"][0])
t = src.read_text(encoding="utf-8")
orig = t
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


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


applied = 0
for i, x in enumerate(findings):
    fx = x.get("fix")
    if not fx or fx["old"] == fx["new"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        print("SEQ FAIL entry", i, "page", x["page"], seg.count(fx["old"]), repr(fx["old"][:60]))
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    applied += 1
print("sequential: applied", applied, "of", sum(1 for x in findings if x.get("fix")))
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
if out:
    a = orig.find("\\oldpage[IV-2]{210}")
    b = orig.find("\\oldpage[IV-2]{215}")
    a2 = t.find("\\oldpage[IV-2]{210}")
    b2 = t.find("\\oldpage[IV-2]{215}")
    out.write_text(t[a2:b2 + 40], encoding="utf-8")
    print("wrote simulated pages to", out)
