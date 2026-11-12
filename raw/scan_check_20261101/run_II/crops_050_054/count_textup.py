import collections
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
c = collections.Counter()
ex = []
for line in open(r"user\Documents\ega_scan_check_20261101\FIXLOG.jsonl", encoding="utf-8"):
    if not line.strip():
        continue
    d = json.loads(line)
    if "\\textup{(\\hyperref" in d["new"] or "\\textup{\\hyperref" in d["new"]:
        key = (d.get("kind"), d.get("convention"), d.get("part"))
        c[key] += 1
        if d.get("part") == "II" and len(ex) < 8:
            ex.append((d.get("page"), d["old"][:70], d["new"][:90]))
print(c)
for e in ex:
    print(e)
