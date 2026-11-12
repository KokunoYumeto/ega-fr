import json
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
c = Counter()
ex = {}
pat = re.compile(r"\\(?:textbf|mathbf)\{[^}]*\}")
for line in open(r"user\Documents\ega_scan_check_20261101\FIXLOG.jsonl", encoding="utf-8"):
    try:
        d = json.loads(line)
    except Exception:
        continue
    if d.get("part") == "IV-2" and d.get("convention") in (2, "2"):
        m = pat.search(d["new"])
        k = m.group(0) if m else d["new"][:30]
        c[k] += 1
        ex.setdefault(k, (d["old"], d["new"]))
for k, v in c.most_common(12):
    print(v, k, ex[k])
