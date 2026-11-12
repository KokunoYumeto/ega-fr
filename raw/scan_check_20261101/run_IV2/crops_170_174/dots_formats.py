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
    if "\\cdots" in d["old"] and "\\cdots" not in d["new"]:
        key = (d.get("part"), d["new"].replace(d["old"].split("\\cdots")[0], "")[:40])
        for cand in ("\\ldots", "\\dots", "\\dotsc", ". . ."):
            if cand in d["new"]:
                c[(d.get("part"), cand)] += 1
                ex.setdefault((d.get("part"), cand), (d["old"][:60], d["new"][:60]))
                break
for k, v in c.most_common():
    print(v, k, ex[k])
