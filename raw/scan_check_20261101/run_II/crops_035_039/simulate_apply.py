"""Dry simulation of apply_fixes.py on the release files for these findings (in memory only, nothing written)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
findings = json.load(open(E / "run_II" / "findings_035_039.json", encoding="utf-8"))
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
part = "II"
files = inv[part]["files"]
print("release files for part II:", [pathlib.Path(f).name for f in files][:6])
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in files}


def locate(page):
    for f in files:
        t = texts[f]
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return f, s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    return None, None, None


applied = failed = 0
for x in findings:
    fix = x.get("fix")
    if not fix:
        continue
    f, s, e = locate(int(x["page"]))
    t = texts[f]
    seg = t[s:e]
    n = seg.count(fix["old"])
    if n != 1:
        failed += 1
        print("FAIL", x["page"], n, repr(fix["old"])[:80])
        continue
    texts[f] = t[:s] + seg.replace(fix["old"], fix["new"]) + t[e:]
    applied += 1
print("applied", applied, "failed", failed)
for p in (36, 37, 39):
    f, s, e = locate(p)
    print(f"--- end of p.{p} segment and start of the next:")
    print(texts[f][e - 120:e + 60])
