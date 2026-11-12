"""Check every fix 'old' occurs exactly once in its page_NNN.tex (CRLF normalised to LF),
then apply each page's fixes in order (and in reverse order) to check they do not interfere.
Also check the edits against the release file, where cross-page pairs meet."""
import json
from collections import defaultdict

D = 'user/Documents/ega_scan_check_20261101/run_III1/'
REL = ('user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/current/'
       'packages/BASE/native/ega3/ega3-1-fr.tex')
F = json.load(open(D + 'findings_122_126.json', encoding='utf-8'))

def page_text(p):
    return open(D + 'page_%03d.tex' % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')

bad = 0
by_page = defaultdict(list)
for i, f in enumerate(F):
    fx = f.get('fix')
    if fx is None:
        continue
    t = page_text(f['page'])
    n = t.count(fx['old'])
    if n != 1:
        bad += 1
        print('NOT UNIQUE (%d)' % n, f['page'], repr(fx['old'])[:100])
    by_page[f['page']].append((i, fx))
    if f['kind'] == 'misprint_in_print' and 'corrected' not in f:
        print('misprint without corrected', i)
print('uniqueness problems:', bad)

for p, fixes in sorted(by_page.items()):
    for order in (fixes, list(reversed(fixes))):
        t = page_text(p)
        for i, fx in order:
            if t.count(fx['old']) != 1:
                print('INTERFERENCE page', p, 'finding', i, repr(fx['old'])[:80])
            t = t.replace(fx['old'], fx['new'], 1)

# release file: apply all edits (each must occur exactly once there too)
r = open(REL, encoding='utf-8', newline='').read()
print('release CRLF?', '\r' in r)
for i, f in enumerate(F):
    fx = f.get('fix')
    if fx is None:
        continue
    n = r.count(fx['old'])
    if n != 1:
        print('release count %d' % n, f['page'], repr(fx['old'])[:100])
    r = r.replace(fx['old'], fx['new'], 1)
# show the joined page breaks after all edits
for key in [r'\oldpage[III]{122}', r'\oldpage[III]{123}', r'\oldpage[III]{124}', r'\oldpage[III]{125}',
            r'\oldpage[III]{126}', r'\oldpage[III]{127}']:
    k = r.find(key)
    print('----', key)
    print(r[k - 120:k + 90])
print('label 4.1.7.11 count (0 expected here: the tag is added by findings_127_131.json):', r.count(r'\label{III.4.1.7.11-fr}'))
