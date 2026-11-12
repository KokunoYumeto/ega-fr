import re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
base = 'user/Documents/ega_scan_check_20261101/'
src = base + 'ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV1/native/ega4/'
labels, tags = set(), set()
for f in glob.glob(src + '*.tex'):
    t = open(f, encoding='utf-8').read()
    labels |= set(re.findall(r'\\label\{([^}]*)\}', t))
    tags |= set(re.findall(r'\\tag\{([^}]*)\}', t))
    labels |= set(re.findall(r'\\begin\{\w+\}\[([^\]]*)\]', t))
for p in range(146, 151):
    t = open(base + 'run_0IV1/page_%03d.tex' % p, encoding='utf-8').read()
    refs = re.findall(r'\\sref\{([^}]*)\}', t) + re.findall(r'\\ref\{([^}]*)\}', t)
    missing = [r for r in refs if r not in labels]
    print(p, len(refs), 'missing:', missing)
    print('   R:', t.count('\\mathfrak{R}'), 'Q:', t.count('\\mathfrak{Q}'),
          'cdots:', t.count('\\cdots'))
for x in ['18.3.4.2', '18.3.4.1', '20.6.6.4', '18.3.6.4', '18.3.6.2', '20.6.23.1', '20.7.11.1']:
    print(x, 'tag' if x in tags else 'no tag')
