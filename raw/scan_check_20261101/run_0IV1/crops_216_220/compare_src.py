import difflib

BASE = 'user/Documents/ega_scan_check_20261101/'
SRCS = {
    'r20pkg': BASE + 'ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV1/native/ega4/ega0-23-fr.tex',
    'source': BASE + 'ega-fr/source/ega4/ega0-23-fr.tex',
}


def rd(p):
    with open(p, encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')


def seg(t, n):
    a = t.find('\\oldpage[0\\textsubscript{IV-1}]{%d}' % n)
    b = t.find('\\oldpage[0\\textsubscript{IV-1}]{%d}' % (n + 1))
    return t[a:b]


texts = {k: rd(v) for k, v in SRCS.items()}
for n in [216, 217, 218, 219, 220]:
    pg = rd(BASE + f'run_0IV1/page_{n}.tex').split('\n', 1)[1]
    for k, t in texts.items():
        s = seg(t, n)
        same = pg == s
        print(n, k, 'identical' if same else 'DIFFERENT', len(pg), len(s))
        if not same:
            for line in difflib.unified_diff(pg.split('\n'), s.split('\n'), lineterm='', n=0):
                print('    ' + line)
