import json, glob, os, sys
from collections import defaultdict

root = r"user\Documents\ega_scan_check_20261101"
want = [int(a) for a in sys.argv[1:]] or [1, 2, 7, 10]
ex = defaultdict(list)
for f in sorted(glob.glob(os.path.join(root, "run_*", "findings_*.json"))):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        c = x.get("convention")
        if c in want and x.get("fix"):
            ex[c].append((os.path.basename(os.path.dirname(f)) + "/" + os.path.basename(f), x["fix"]["old"], x["fix"]["new"]))
for c in want:
    print("== conv", c, len(ex[c]))
    for e in ex[c][-15:]:
        print(e)
