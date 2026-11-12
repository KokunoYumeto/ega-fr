"""Which prepared pages of a run folder differ from the same page in the release (r20) diplomatic sources.
usage: python compare_pages.py RUN_FOLDER PART"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
run, part = pathlib.Path(sys.argv[1]), sys.argv[2]
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
key = part.replace("\\textsubscript{", "_").replace("}", "")
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
r20 = {}
for f in inv[key]["files"]:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        r20[n] = t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
diff = []
for p in sorted(run.glob("page_*.tex")):
    n = int(re.findall(r"\d+", p.stem)[0])
    old = p.read_text(encoding="utf-8").split("\n", 1)[1]  # drop the "% from" line
    if n in r20 and old.replace("\r", "") != r20[n].replace("\r", ""):
        diff.append(n)
print("pages differing from r20:", diff)
