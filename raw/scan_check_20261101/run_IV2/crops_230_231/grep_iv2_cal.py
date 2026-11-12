import json, glob, sys, os
sys.stdout.reconfigure(encoding='utf-8')
root = r'user\Documents\ega_scan_check_20261101\run_IV2'
n = 0
for f in sorted(glob.glob(os.path.join(root, 'findings_*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    for x in d:
        fx = x.get('fix') or {}
        old, new = fx.get('old', ''), fx.get('new', '')
        note = (x.get('note') or '')
        if ('mathcal' in old and 'mathscr' in new) or ('mathscr' in old and 'mathcal' in new) or 'calligraph' in note.lower() or 'item 19' in note.lower() or 'item 42' in note.lower():
            n += 1
            print(os.path.basename(f), x.get('page'), x.get('kind'), '|', old[:80], '->', new[:80], '|', note[:250])
print('total', n)
