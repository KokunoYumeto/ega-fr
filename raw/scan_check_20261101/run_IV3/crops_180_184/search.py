import json, glob, sys

DISP_END_BLANK = "\\]\n\n"
n = 0
for f in sorted(glob.glob(r'user/Documents/ega_scan_check_20261101/run_IV3/findings_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for x in d:
        fx = x.get('fix') or {}
        if not isinstance(fx, dict):
            continue
        old = fx.get('old', '')
        new = fx.get('new', '')
        if x.get('kind') != 'marker' and (DISP_END_BLANK in old and DISP_END_BLANK not in new):
            n += 1
            if n < 10:
                print(f.split('\\')[-1], '|', x.get('page'), '|', x.get('kind'), '|', x.get('scan'), '|', x.get('tex'))
                print('   FIX', json.dumps(fx, ensure_ascii=False))
print(n)
