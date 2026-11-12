import re
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
F = root / 'ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega3/ega3-6-fr.tex'
t = F.read_text(encoding='utf-8')
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r'\\oldpage\[III\]\{(\d+)\}', t)]
for i, (n, s) in enumerate(cuts):
    if 167 <= n <= 171:
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        seg = t[s:e]
        p = (root / f'run_III2/page_{n}.tex').read_text(encoding='utf-8').replace('\r\n', '\n')
        body = p.split('\n', 1)[1]
        print(n, 'identical' if body == seg else 'DIFFERENT', len(body), len(seg))
        if body != seg:
            import difflib
            for line in difflib.unified_diff(body.splitlines(), seg.splitlines(), lineterm='', n=0):
                print('   ', line)
