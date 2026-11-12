import json, os, sys
RUN = r'user\Documents\ega_scan_check_20261101\run_0IV1'
F = json.load(open(os.path.join(RUN, 'findings_056_060.json'), encoding='utf-8'))
pages = [int(a) for a in sys.argv[1:]] or [56, 57, 58, 59, 60]
for p in pages:
    t = open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='').read().replace('\r\n', '\n')
    for x in F:
        if x['page'] == p and x['fix']:
            t = t.replace(x['fix']['old'], x['fix']['new'], 1)
    # brace balance check
    depth = 0; bad = False
    for ch in t:
        if ch == '{': depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0: bad = True
    print('==== page', p, 'brace balance', depth, 'negative' if bad else '')
    print(t)
