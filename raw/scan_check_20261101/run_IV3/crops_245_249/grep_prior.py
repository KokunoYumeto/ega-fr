import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
pat = re.compile(sys.argv[1])
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 8
n = 0
for f in sorted(glob.glob(r"user/Documents/ega_scan_check_20261101/run_IV3/findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        print("ERR", f, e)
        continue
    for x in d:
        fx = x.get("fix") or {}
        s = json.dumps(fx, ensure_ascii=False) + " || " + str(x.get("note", ""))
        if pat.search(s):
            n += 1
            if n <= limit:
                print(f[-20:], x.get("page"), x.get("kind"), x.get("convention"), "|", json.dumps(fx, ensure_ascii=False)[:300], "|", str(x.get("note", ""))[:250])
print("total", n)
