import json, glob, collections, sys
# Read-only survey of other run_II checkers' findings: conventions used, and notes about P, mathcal, item labels.
root = r'user\Documents\ega_scan_check_20261101\run_II'
out = sys.stdout.buffer
for f in sorted(glob.glob(root + r'\findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        out.write((f + ' unreadable ' + str(e) + '\n').encode('utf-8')); continue
    c = collections.Counter((x.get('kind'), x.get('convention')) for x in d)
    out.write((f.split('\\')[-1] + ' ' + str(len(d)) + ' ' + str(dict(c)) + '\n').encode('utf-8'))
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if x.get('convention') == 10 or 'mathcal' in (x.get('note') or '') or 'bold' in (x.get('note') or '').lower() and 'P' in s or '\\item[' in s:
            out.write(('   ' + json.dumps({k: x.get(k) for k in ('page', 'kind', 'convention', 'fix', 'note')}, ensure_ascii=False)[:400] + '\n').encode('utf-8'))
