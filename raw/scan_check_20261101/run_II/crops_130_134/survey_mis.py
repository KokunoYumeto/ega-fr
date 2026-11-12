import json, glob, sys, os
sys.stdout.reconfigure(encoding="utf-8")
os.chdir(r"user\Documents\ega_scan_check_20261101")
n = 0
for f in sorted(glob.glob("run_*/findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        if x.get("kind") == "misprint_in_print":
            fx = x.get("fix") or {}
            if "hyperref" in (fx.get("old") or "") or "hyperref" in (x.get("corrected") or ""):
                n += 1
                if n > 6:
                    sys.exit()
                print(f.replace(os.sep, "/"), x.get("page"), "|", repr(fx.get("old")), "=>", repr(fx.get("new")), "| corrected:", repr(x.get("corrected")), "|", (x.get("note") or "")[:200])
                print()
