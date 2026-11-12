import json, glob, collections, sys, os
os.chdir(r"user\Documents\ega_scan_check_20261101")
want = set(int(a) for a in sys.argv[1].split(",")) if len(sys.argv) > 1 else {2, 3, 4, 5, 7, 8, 9, 10}
per = int(sys.argv[2]) if len(sys.argv) > 2 else 3
seen = collections.defaultdict(int)
for f in sorted(glob.glob("run_*/findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        c = x.get("convention")
        if c in want and seen[c] < per:
            seen[c] += 1
            fx = x.get("fix") or {}
            print(c, f.replace(os.sep, "/"), x.get("page"), "|", repr(fx.get("old")), "=>", repr(fx.get("new")), "|", (x.get("note") or "")[:160])
