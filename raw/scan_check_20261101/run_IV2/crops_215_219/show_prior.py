import json, glob, sys, os
sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding="utf-8")
run = r"user\Documents\ega_scan_check_20261101\run_IV2"
kinds = sys.argv[1].split(",") if len(sys.argv) > 1 else ["marker"]
pat = sys.argv[2] if len(sys.argv) > 2 else None
n = 0
for fn in sorted(glob.glob(os.path.join(run, "findings_*.json"))):
    try:
        data = json.load(open(fn, encoding="utf-8"))
    except Exception as e:
        continue
    for d in data:
        if d.get("kind") not in kinds and "all" not in kinds:
            continue
        fx = d.get("fix") or {}
        blob = json.dumps(d, ensure_ascii=False)
        if pat and pat not in blob:
            continue
        print(os.path.basename(fn), "p", d.get("page"), "|", d.get("kind"), d.get("convention"), "|", d.get("where"))
        print("   old:", repr(fx.get("old")))
        print("   new:", repr(fx.get("new")))
        print("   note:", (d.get("note") or "")[:300])
        n += 1
        if n > 40:
            sys.exit(0)
