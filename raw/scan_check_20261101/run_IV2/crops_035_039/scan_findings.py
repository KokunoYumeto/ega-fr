"""Summarise kinds/conventions used by other checkers for a given pattern in fix.new (or note)."""
import json, glob, sys, collections

pat = sys.argv[1]
where = sys.argv[2] if len(sys.argv) > 2 else 'new'
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 8
cnt = collections.Counter()
shown = 0
for fn in glob.glob(r'user\Documents\ega_scan_check_20261101\run_*\findings_*.json'):
    try:
        data = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    if not isinstance(data, list):
        continue
    for it in data:
        fx = it.get('fix') or {}
        if where == 'new':
            s = fx.get('new', '') if isinstance(fx, dict) else ''
        elif where == 'old':
            s = fx.get('old', '') if isinstance(fx, dict) else ''
        else:
            s = json.dumps(it, ensure_ascii=False)
        if pat in (s or ''):
            cnt[(it.get('kind'), it.get('convention'))] += 1
            if shown < limit:
                print(fn.split('\\')[-2], it.get('page'), it.get('kind'), it.get('convention'), repr(fx.get('old') if isinstance(fx, dict) else None)[:90], '=>', repr(fx.get('new') if isinstance(fx, dict) else None)[:90])
                shown += 1
print(cnt.most_common())
