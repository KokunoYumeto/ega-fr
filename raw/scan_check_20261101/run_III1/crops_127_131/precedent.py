import json
import sys

# Print FIXLOG entries whose old or new contains any of the given substrings (argv), limited per pattern.
pats = sys.argv[1:]
lim = 6
count = {p: 0 for p in pats}
for name in ("FIXLOG.jsonl",):
    with open(r"user\Documents\ega_scan_check_20261101\\" + name, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            o = d.get("old") or ""
            n = d.get("new") or ""
            for p in pats:
                if (p in o or p in n) and count[p] < lim:
                    count[p] += 1
                    print(p, "|", d.get("part"), d.get("page"), "|", repr(o)[:160], "=>", repr(n)[:200])
print(count)
