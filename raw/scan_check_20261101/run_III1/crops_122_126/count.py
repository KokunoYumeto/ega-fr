import json, collections
F = json.load(open('user/Documents/ega_scan_check_20261101/run_III1/findings_122_126.json', encoding='utf-8'))
c = collections.defaultdict(lambda: [0, 0, 0])
for f in F:
    k = 1 if f['kind'] == 'convention' else 2 if f['kind'] == 'misprint_in_print' else 0
    c[f['page']][k] += 1
    if ('corrected' in f) != (f['kind'] == 'misprint_in_print'):
        print('corrected field mismatch', f['page'], f['where'])
for p in sorted(c):
    print(p, '%d/%d/%d' % tuple(c[p]))
print(len(F))
for f in F:
    if f['kind'] == 'misprint_in_print':
        print(f['page'], f['confidence'], 'fix' if f['fix'] else 'nofix', f['where'][:70])
