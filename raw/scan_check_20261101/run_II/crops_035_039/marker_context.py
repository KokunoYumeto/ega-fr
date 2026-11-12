import re
import sys

# usage: marker_context.py FILE  -- print how page markers sit between text (word split, blank lines)
sys.stdout.reconfigure(encoding='utf-8')
t = open(sys.argv[1], encoding='utf-8').read()
pat = re.compile(r'\\oldpage\[[^\]]*\]\{\d+\}')
counts = {}
for m in pat.finditer(t):
    before = t[max(0, m.start() - 40):m.start()]
    after = t[m.end():m.end() + 40]
    key = ('blank-before' if before.endswith('\n\n') else 'nl-before' if before.endswith('\n') else 'inline-before',
           'blank-after' if after.startswith('\n\n') else 'nl-after' if after.startswith('\n') else 'pct-after' if after.startswith('%') else 'inline-after')
    counts[key] = counts.get(key, 0) + 1
    stripped = before.rstrip('\n')
    if stripped.endswith('-') or stripped.endswith('-%'):
        print('SPLIT WORD?', m.group(0), repr(before[-25:]), repr(after[:25]))
print(counts)
