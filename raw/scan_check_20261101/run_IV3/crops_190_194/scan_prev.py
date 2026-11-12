"""Search earlier findings files for fixes whose new text matches a pattern.

Usage: python scan_prev.py RUNGLOB NEEDLE_IN_NEW [NEEDLE_NOT_IN_OLD] [MAX]
"""
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
pat = sys.argv[1]
needle = sys.argv[2].encode().decode('unicode_escape')
notold = sys.argv[3].encode().decode('unicode_escape') if len(sys.argv) > 3 and sys.argv[3] else None
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 8
n = 0
for f in sorted(glob.glob(pat)):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix')
        if not fx:
            continue
        new = fx.get('new', '')
        old = fx.get('old', '')
        if needle in new and (notold is None or notold not in old):
            n += 1
            if n <= mx:
                print(f, json.dumps(x, ensure_ascii=False)[:700])
                print()
print('total', n)
