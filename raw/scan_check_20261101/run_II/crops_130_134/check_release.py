"""Read-only check: every fix's 'old' occurs exactly once in its page segment of the r20 release file
(same locate logic as apply_fixes.py), and sequential application in list order succeeds. Writes nothing."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
F = json.load(open(E / "run_II" / "findings_130_134.json", encoding="utf-8"))
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["II"]["files"]
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv}


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    return None, None


problems = 0
for i, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        continue
    for f, t in texts.items():
        s, e = locate(t, x["page"])
        if s is None:
            continue
        seg = t[s:e]
        c = seg.count(fx["old"])
        if c != 1:
            problems += 1
            print("release count", c, "entry", i, "page", x["page"], repr(fx["old"][:70]))
        else:
            texts[f] = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
        break
print("release check problems:", problems)
