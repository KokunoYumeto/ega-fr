import json, glob, sys, os
os.chdir(r"user\Documents\ega_scan_check_20261101")
needle = sys.argv[1]
pat = sys.argv[2] if len(sys.argv) > 2 else "run_II/findings_*.json"
per = int(sys.argv[3]) if len(sys.argv) > 3 else 8
n = 0
for f in sorted(glob.glob(pat)):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if needle in s:
            n += 1
            if n > per:
                sys.exit()
            fx = x.get("fix") or {}
            print(f.replace(os.sep, "/"), x.get("page"), x.get("kind"), x.get("convention"), "|", repr(fx.get("old")), "=>", repr(fx.get("new")), "|", (x.get("note") or "")[:220])
            print()
