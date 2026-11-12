import json, io, sys, os, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_0IV1'
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\source\ega4\ega0-22-fr.tex'
d = json.load(open(os.path.join(RUN, 'findings_206_210.json'), encoding='utf-8'))
keys = {'page', 'where', 'scan', 'tex', 'kind', 'convention', 'confidence', 'fix', 'note'}
kinds = {'word', 'formula', 'symbol', 'font', 'italics', 'missing', 'extra', 'number', 'punctuation',
         'misprint_in_print', 'convention', 'marker', 'other'}
ok = True
texts = {}
for p in sorted({f['page'] for f in d}):
    raw = open(os.path.join(RUN, f'page_{p:03d}.tex'), 'rb').read().decode('utf-8')
    texts[p] = raw.replace('\r\n', '\n')
orig = dict(texts)
src = open(SRC, 'rb').read().decode('utf-8')
assert '\r' not in src
MARK = '\\oldpage[0\\textsubscript{IV-1}]{%d}'
segs = {}
for p in texts:
    a = src.find(MARK % p)
    b = src.find(MARK % (p + 1))
    assert a >= 0 and src.count(MARK % p) == 1, p
    segs[p] = src[a:(b if b > 0 else len(src))]
    # the page file (after its two header lines) should be the source segment
    body = texts[p].split('\n', 1)[1]
    if not segs[p].startswith(body.rstrip()[:200]):
        print('page file does not start like the source segment', p)
counts = collections.Counter()
for i, f in enumerate(d):
    miss = keys - set(f)
    if miss:
        print('missing keys', i, miss); ok = False
    if f['kind'] not in kinds:
        print('bad kind', i, f['kind']); ok = False
    if (f['kind'] == 'convention') != (f['convention'] is not None):
        print('convention mismatch', i); ok = False
    if f['kind'] == 'misprint_in_print' and 'corrected' not in f:
        print('misprint without corrected', i); ok = False
    p = f['page']
    key = 'convention' if f['kind'] == 'convention' else ('misprint' if f['kind'] == 'misprint_in_print' else 'normal')
    counts[(p, key)] += 1
    fx = f['fix']
    if not fx:
        continue
    n0 = orig[p].count(fx['old'])
    n1 = texts[p].count(fx['old'])
    n2 = segs[p].count(fx['old'])
    if n0 != 1 or n1 != 1 or n2 != 1:
        print(f'#{i} p{p} count page={n0} sequential={n1} source-segment={n2}: {fx["old"]!r}'); ok = False
    else:
        texts[p] = texts[p].replace(fx['old'], fx['new'], 1)
print('ALL OK' if ok else 'PROBLEMS')
for p in sorted(texts):
    print(p, 'normal', counts[(p, 'normal')], 'convention', counts[(p, 'convention')], 'misprint', counts[(p, 'misprint')])
if len(sys.argv) > 1:
    print(texts[int(sys.argv[1])])
