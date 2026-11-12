import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
c = Counter()
ex = {}
for line in open(r"user\Documents\ega_scan_check_20261101\FIXLOG.jsonl", encoding="utf-8"):
    try:
        d = json.loads(line)
    except Exception:
        continue
    if d.get("part") != "IV-2":
        continue
    if "\\emph{" in d["new"] and d["new"].count("\\emph{") > d["old"].count("\\emph{"):
        k = (d.get("kind"), d.get("convention"), d.get("source"))
        c[(d.get("kind"), d.get("convention"))] += 1
        ex.setdefault((d.get("kind"), d.get("convention")), []).append((d.get("page"), d["old"][:40], d.get("source")))
for k, v in c.most_common():
    print(v, k, ex[k][:3])
src = Counter()
for line in open(r"user\Documents\ega_scan_check_20261101\FIXLOG.jsonl", encoding="utf-8"):
    try:
        d = json.loads(line)
    except Exception:
        continue
    if d.get("part") == "IV-2" and "\\emph{" in d["new"] and d["new"].count("\\emph{") > d["old"].count("\\emph{"):
        src[(d.get("source"), d.get("kind"), d.get("convention"))] += 1
for k, v in sorted(src.items()):
    print(k, v)
