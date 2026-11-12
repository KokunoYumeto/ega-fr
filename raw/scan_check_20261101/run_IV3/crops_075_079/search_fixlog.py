import json, collections, sys, re

path = r"user\Documents\ega_scan_check_20261101\FIXLOG_CURRENT.jsonl"
mode = sys.argv[1] if len(sys.argv) > 1 else "k"

rows = []
with open(path, encoding="utf-8") as f:
    for line in f:
        try:
            rows.append(json.loads(line))
        except Exception:
            pass

def show(x, width=500):
    d = {k: x.get(k) for k in ("file", "page", "old", "new", "note", "kind")}
    d["file"] = (d["file"] or "").split("\\")[-1]
    print(json.dumps(d, ensure_ascii=False)[:width])

if mode == "k":
    n = 0
    files = collections.Counter()
    for x in rows:
        old = x.get("old") or ""
        new = x.get("new") or ""
        if "\\boldsymbol{k}" in old and "\\mathbf{k}" in new:
            n += 1
            files[(x.get("file") or "").split("\\")[-1]] += 1
            if n <= 10:
                show(x)
    print("total", n, files)
elif mode == "grep":
    pat = sys.argv[2]
    fpat = sys.argv[3] if len(sys.argv) > 3 else ""
    lim = int(sys.argv[4]) if len(sys.argv) > 4 else 20
    n = 0
    for x in rows:
        s = json.dumps(x, ensure_ascii=False)
        if re.search(pat, s) and fpat in (x.get("file") or ""):
            n += 1
            if n <= lim:
                show(x, 700)
    print("total", n)
