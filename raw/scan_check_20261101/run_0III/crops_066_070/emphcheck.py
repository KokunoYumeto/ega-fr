import re
base = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/'
pat = re.compile(r'\\begin\{(proposition|theorem|corollary|lemma|definition)\}(?:\[[^\]]*\])?\s*(?:\\label\{[^}]*\}\s*)?(.{0,12})', re.S)
for fn in ['ega3/ega3-1-fr.tex', 'ega1/ega1-2-fr.tex', 'ega2/ega2-1-fr.tex']:
    try:
        s = open(base + fn, encoding='utf-8').read()
    except Exception as e:
        print(fn, e)
        continue
    envs = pat.findall(s)
    n = len(envs)
    m = sum(1 for e in envs if e[1].startswith('\\emph'))
    print(fn, 'statements:', n, 'starting with \\emph:', m)
