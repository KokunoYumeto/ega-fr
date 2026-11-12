import json, glob, re
cnt = 0
for fn in sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if re.search(r'left of the (vertical )?arrow|right of the (vertical )?arrow|left side|right side|on the left|on the right', s):
            cnt += 1
            if cnt <= 12:
                f = x.get('fix') or {}
                print(fn, x['page'], x['kind'], '|', (x.get('where') or '')[:100], '|', (f.get('old') or '')[:80], '=>', (f.get('new') or '')[:80], '|', (x.get('note') or '')[:250])
                print()
print('count', cnt)
