import json
import re
import sys

base = r"user\Documents\ega_scan_check_20261101"
files = ["FIXLOG_CURRENT.jsonl", "FIXLOG.jsonl", "FIXLOG_090_097.jsonl", "FIXLOG_098_109.jsonl"]
pat = re.compile(r"[a-z,;)]\s*\n(\n)?\\oldpage\[[^\]]*\]\{\d+\}\n(\n)?[a-z(]")
seen = 0
for fn in files:
    try:
        fh = open(base + "\\" + fn, encoding="utf-8")
    except FileNotFoundError:
        continue
    for line in fh:
        try:
            d = json.loads(line)
        except Exception:
            continue
        new = d.get("new") or ""
        old = d.get("old") or ""
        if "\\oldpage" in new and "\\oldpage" in old and pat.search(new):
            m = pat.search(new)
            s = max(0, m.start() - 60)
            print(fn, d.get("page"), repr(new[s:m.end() + 40]))
            seen += 1
            if seen > 10:
                sys.exit(0)
print("count", seen)
