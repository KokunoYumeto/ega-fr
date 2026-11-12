import re, io, sys
base = r'user/Documents/ega_scan_check_20261101/run_IV4/'
pat = sys.argv[1] if len(sys.argv) > 1 else r'\\sref'
for p in range(280, 285):
    t = io.open(base + 'page_%d.tex' % p, encoding='utf-8').read().replace('\r\n', '\n')
    n = 0
    for m in re.finditer(pat, t):
        n += 1
        s = max(0, m.start() - 30)
        e = min(len(t), m.end() + 45)
        print(p, repr(t[s:e]))
    print(p, 'count', n)
