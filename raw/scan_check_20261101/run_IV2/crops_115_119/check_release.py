"""Compare page_NNN.tex (115-119) with the current release segments and apply the findings in order to the segments (dry run, nothing written)."""
import json, pathlib, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUN = pathlib.Path(r'user\Documents\ega_scan_check_20261101\run_IV2')
SRC = pathlib.Path(r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex')
t = SRC.read_text(encoding='utf-8')
marks = [(int(m.group(1)), m.start()) for m in re.finditer(r'\\oldpage\[IV-2\]\{(\d+)\}', t)]
seg = {}
for i, (n, s) in enumerate(marks):
    if 115 <= n <= 119:
        seg[n] = t[s:marks[i + 1][1]]
F = json.load(open(RUN / 'findings_115_119.json', encoding='utf-8'))
for n in range(115, 120):
    p = (RUN / ('page_%03d.tex' % n)).read_text(encoding='utf-8').replace('\r\n', '\n')
    body = p.split('\n', 1)[1]
    print(n, 'page file == release segment:', body == seg[n], len(body), len(seg[n]))
    s = seg[n]
    for x in F:
        if x['page'] != n or not x['fix']:
            continue
        c = s.count(x['fix']['old'])
        if c != 1:
            print('  FAIL', c, repr(x['fix']['old'][:50]))
            continue
        s = s.replace(x['fix']['old'], x['fix']['new'])
print('done')
