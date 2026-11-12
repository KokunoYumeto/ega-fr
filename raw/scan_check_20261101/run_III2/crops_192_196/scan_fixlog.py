import json, sys
pat = sys.argv[1]
path = sys.argv[2] if len(sys.argv) > 2 else r"user\Documents\ega_scan_check_20261101\FIXLOG.jsonl"
n = 0
for line in open(path, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    d = json.loads(line)
    if pat in d.get("new", "") or pat in d.get("old", ""):
        n += 1
        if n <= 6:
            out = f"{d.get('page')} {d.get('kind')} conv={d.get('convention')} OLD={d['old'][:90]!r} NEW={d['new'][:90]!r}"
            sys.stdout.buffer.write((out + "\n").encode("utf-8"))
print(n)
