import re
base = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/'
fn = 'ega3/ega3-1-fr.tex'
s = open(base + fn, encoding='utf-8').read()
pat = re.compile(r'\\begin\{(proposition|theorem|corollary|lemma|definition)\}(\[[^\]]*\])?\s*(?:\\label\{[^}]*\}\s*)?(.{0,40})', re.S)
for m in pat.finditer(s):
    if m.group(3).startswith('\\emph'):
        line = s.count('\n', 0, m.start()) + 1
        # find the last oldpage marker before
        pm = list(re.finditer(r'\\oldpage\[[^\]]*\]\{(\d+)\}', s[:m.start()]))
        page = pm[-1].group(1) if pm else '?'
        print(line, 'p.', page, m.group(1), m.group(2), repr(m.group(3)[:40]))
