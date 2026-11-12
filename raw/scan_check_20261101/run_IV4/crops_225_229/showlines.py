import sys

run = 'user/Documents/ega_scan_check_20261101/run_IV4/'
p = sys.argv[1]
s = open(run + 'page_%s.tex' % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')
for i, line in enumerate(s.split('\n'), 1):
    nonascii = sorted(set(ch for ch in line if ord(ch) > 127))
    sys.stdout.buffer.write(('%3d %s\n' % (i, ' '.join('U+%04X(%s)' % (ord(c), c) for c in nonascii))).encode('utf-8'))
