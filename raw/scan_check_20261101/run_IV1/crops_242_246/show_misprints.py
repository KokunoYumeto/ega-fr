import json, glob, os, sys
sys.stdout.reconfigure(encoding="utf-8")

root = r"user\Documents\ega_scan_check_20261101"
lim = int(sys.argv[1]) if len(sys.argv) > 1 else 10
n = 0
for f in sorted(glob.glob(os.path.join(root, "run_*", "findings_*.json")), key=os.path.getmtime, reverse=True):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        if x.get("kind") == "misprint_in_print":
            n += 1
            if n <= lim:
                print(os.path.basename(os.path.dirname(f)) + "/" + os.path.basename(f), "p", x.get("page"))
                print("   scan:", (x.get("scan") or "")[:160])
                print("   tex:", (x.get("tex") or "")[:160])
                print("   fix:", json.dumps(x.get("fix"), ensure_ascii=False)[:200])
                print("   corrected:", json.dumps(x.get("corrected"), ensure_ascii=False)[:200])
                print("   note:", (x.get("note") or "")[:250])
print("total", n)
