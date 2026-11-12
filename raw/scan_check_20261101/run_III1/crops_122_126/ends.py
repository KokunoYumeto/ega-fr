D = r'user/Documents/ega_scan_check_20261101/run_III1/'
for p in range(121, 128):
    t = open(D + 'page_%03d.tex' % p, encoding='utf-8', newline='').read()
    print(p, 'CR' if '\r' in t else 'LF', repr(t[:80]), '...', repr(t[-90:]))
