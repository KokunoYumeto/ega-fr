import re
import glob

root = 'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/'
for f in sorted(glob.glob(root + 'ega4-*.tex')):
    s = open(f, encoding='utf-8').read()
    name = f.replace('\\', '/').split('/')[-1]
    a = len(re.findall(r'\$-module', s))
    b = len(re.findall(r'\$-Module', s))
    c = len(re.findall(r'O\}?_\{?X\}?\$-module', s))
    d = len(re.findall(r'O\}?_\{?X\}?\$-Module', s))
    e = len(re.findall(r'\\vphi', s))
    g = len(re.findall(r'\\mapsto', s))
    print(name, '$-module', a, '$-Module', b, 'O_X$-module', c, 'O_X$-Module', d, 'vphi', e, 'mapsto', g)
