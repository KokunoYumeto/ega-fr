import re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current\packages\BASE\native\ega3\ega3-1-fr.tex'
lines = open(p, encoding='utf-8').read().split('\n')
for i, l in enumerate(lines):
    m = re.match(r'\\oldpage\[III\]\{(\d+)\}', l)
    if m:
        n = int(m.group(1))
        before = lines[i-1] if i > 0 else ''
        after = lines[i+1] if i + 1 < len(lines) else ''
        bb = (before.strip() == '')
        ab = (after.strip() == '')
        if bb or ab:
            print(n, 'blank_before' if bb else '', 'blank_after' if ab else '', '| prev:', lines[i-2][-50:] if bb else before[-50:], '| next:', (lines[i+2] if ab else after)[:50])
