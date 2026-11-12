"""Search earlier findings files of run_IV3 for a regex in the fix strings or notes."""
import glob
import json
import re
import sys

pat = re.compile(sys.argv[1])
field = sys.argv[2] if len(sys.argv) > 2 else "all"
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 30
n = 0
for f in sorted(glob.glob(r"user\Documents\ega_scan_check_20261101\run_IV3\findings_*.json")):
    for x in json.load(open(f, encoding="utf-8")):
        fx = x.get("fix") or {}
        if field == "fix":
            hay = (fx.get("old", "") + "\n" + fx.get("new", "")) if isinstance(fx, dict) else ""
        else:
            hay = json.dumps(x, ensure_ascii=False)
        if pat.search(hay):
            sys.stdout.buffer.write((f.split("\\")[-1] + " " + json.dumps(x, ensure_ascii=False)[:900] + "\n\n").encode("utf-8"))
            n += 1
            if n >= limit:
                sys.exit(0)
print(n)
