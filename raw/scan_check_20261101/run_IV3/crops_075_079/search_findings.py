import json, glob, re, collections, sys, os

base = r"user\Documents\ega_scan_check_20261101"
mode = sys.argv[1]

files = sorted(glob.glob(os.path.join(base, "run_*", "findings_*.json")))

def load(fn):
    try:
        with open(fn, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

if mode == "conv7sub":
    cnt = collections.Counter()
    ex = []
    for fn in files:
        for x in load(fn):
            s = " | ".join(str(x.get(k) or "") for k in ("note", "scan", "where"))
            if x.get("convention") == 7 and re.search(r"subtract|minus|soustr", s, re.I):
                cnt[os.path.basename(os.path.dirname(fn))] += 1
                if len(ex) < 10:
                    ex.append((os.path.basename(fn), x["page"], json.dumps(x.get("fix"), ensure_ascii=False)[:160], s[:220]))
    print(cnt)
    for e in ex:
        print(e)
elif mode == "grep":
    pat = sys.argv[2]
    lim = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    run = sys.argv[4] if len(sys.argv) > 4 else ""
    n = 0
    for fn in files:
        if run and run not in fn:
            continue
        for x in load(fn):
            s = json.dumps(x, ensure_ascii=False)
            if re.search(pat, s):
                n += 1
                if n <= lim:
                    print(os.path.basename(os.path.dirname(fn)), os.path.basename(fn), x.get("page"), x.get("kind"), x.get("convention"),
                          json.dumps(x.get("fix"), ensure_ascii=False)[:220], "|", (x.get("note") or "")[:220])
    print("total", n)
