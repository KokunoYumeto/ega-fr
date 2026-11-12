"""Search prior findings files for fixes matching a regex in fix.new (read-only)."""
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"user\Documents\ega_scan_check_20261101"
pat = re.compile(sys.argv[1])
field = sys.argv[2] if len(sys.argv) > 2 else "new"
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 8
n = 0
for f in sorted(glob.glob(BASE + r"\run_*\findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix") or {}
        if field in ("new", "old"):
            s = fx.get(field, "") if isinstance(fx, dict) else ""
        else:
            s = str(x.get(field) or "")
        if pat.search(s):
            n += 1
            if n <= limit:
                print(f.replace(BASE, ""), x.get("page"), x.get("kind"), x.get("convention"), "|",
                      x.get("where", "")[:90], "|", json.dumps(fx, ensure_ascii=False)[:260], "|",
                      (x.get("note") or "")[:160])
                print()
print("total", n)
