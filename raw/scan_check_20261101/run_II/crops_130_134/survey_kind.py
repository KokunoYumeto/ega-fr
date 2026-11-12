import json, glob, sys, os
os.chdir(r"user\Documents\ega_scan_check_20261101")
kind = sys.argv[1]
per = int(sys.argv[2]) if len(sys.argv) > 2 else 10
pat = sys.argv[3] if len(sys.argv) > 3 else "run_*/findings_*.json"
n = 0
for f in sorted(glob.glob(pat)):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        if x.get("kind") == kind:
            n += 1
            if n > per:
                break
            fx = x.get("fix") or {}
            print(f.replace(os.sep, "/"), x.get("page"), "|", repr(fx.get("old")), "=>", repr(fx.get("new")), "|", (x.get("note") or "")[:300])
            print()
