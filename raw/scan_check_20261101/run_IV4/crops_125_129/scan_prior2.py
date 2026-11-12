import json, glob, sys
sys.stdout.reconfigure(encoding="utf-8")
base = r"user\Documents\ega_scan_check_20261101"
needles = sys.argv[1:]
cnt = {}
shown = 0
for fn in sorted(glob.glob(base + r"\run_*\findings_*.json")):
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        f = x.get("fix") or {}
        nw = f.get("new", "") or ""
        for nd in needles:
            if nd in nw:
                cnt[nd] = cnt.get(nd, 0) + 1
                if shown < 6:
                    shown += 1
                    print(fn.split("\\")[-2:], json.dumps(x, ensure_ascii=False)[:420])
                    print("--")
print(cnt)
