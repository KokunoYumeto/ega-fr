import glob
import json
import re

E = r"user\Documents\ega_scan_check_20261101"
QUERIES = {
    "italic item labels": (r"\\item\[", r"\\item\[(\\textit|\\emph|\\it |\\itshape|\{\\it)"),
    "rm item labels changed": (r"\\item\[\\rm [a-e]", None),
    "refs textup": (r"\([0-9]+\.[0-9]", r"\\textup\{\([0-9]"),
    "emph letter labels in prose": (r"[a-e]'?\)", r"\\emph\{[a-e]'?\)\}"),
    "textup a) labels": (r"[a-e]\)", r"\\textup\{[a-e]\)\}"),
}
rows = []
for f in sorted(glob.glob(E + r"\run_*\findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix")
        if isinstance(fx, dict):
            rows.append((f.split("\\")[-2], x, fx.get("old", ""), fx.get("new", "")))
for name, (po, pn) in QUERIES.items():
    po_c = re.compile(po)
    pn_c = re.compile(pn) if pn else None
    hits = [r for r in rows if po_c.search(r[2]) and (pn_c is None or pn_c.search(r[3]))]
    print("==", name, len(hits))
    for run, x, o, nw in hits[:6]:
        print("  ", run, x.get("page"), x.get("kind"), x.get("convention"), "|", repr(o)[:80], "->", repr(nw)[:100])
