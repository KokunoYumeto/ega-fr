import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages'
L = r'[A-Za-zéèàùâêîôûçï]'
pats = {
    'hyphen+newline split': re.compile(L + r'-\n\\oldpage\[[^\]]*\]\{\d+\}\n' + L),
    'percent join': re.compile(L + r'-?%\n\\oldpage\[[^\]]*\]\{\d+\}%?\n?' + L),
    'inline join': re.compile(L + r'-?\\oldpage\[[^\]]*\]\{\d+\}' + L),
}
files = sorted(glob.glob(base + r'\*\native\*\*.tex'))
print('files', len(files))
for fn in files:
    t = open(fn, encoding='utf-8', errors='replace').read()
    for k, p in pats.items():
        m = p.findall(t)
        if m:
            print(fn.split('\\')[-3], fn.split('\\')[-1], k, len(m), [repr(x) for x in m[:3]])
