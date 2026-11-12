import json, glob, sys, os
os.chdir(r"user\Documents\ega_scan_check_20261101")
pat = sys.argv[1] if len(sys.argv) > 1 else "run_II/findings_*.json"
per = int(sys.argv[2]) if len(sys.argv) > 2 else 12
n = 0
for f in sorted(glob.glob(pat)):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix") or {}
        o = fx.get("old") or ""
        nw = fx.get("new") or ""
        if "oldpage" in o or "oldpage" in nw or o.endswith("\n\n") or "paragraph" in (x.get("note") or ""):
            n += 1
            if n > per:
                sys.exit()
            print(f.replace(os.sep, "/"), x.get("page"), x.get("kind"), "|", repr(o), "=>", repr(nw), "|", (x.get("note") or "")[:260])
            print()
