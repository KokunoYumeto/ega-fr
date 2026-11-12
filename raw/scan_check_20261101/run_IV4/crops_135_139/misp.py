import json, sys
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open(r'user/Documents/ega_scan_check_20261101/MISPRINTS.json', encoding='utf-8'))
print(json.dumps(d[-1], ensure_ascii=False)[:500])
for m in d:
    s = json.dumps(m, ensure_ascii=False)
    pg = m.get('page')
    part = str(m.get('part', '')) + str(m.get('file', ''))
    try:
        pgi = int(pg)
    except Exception:
        continue
    if 125 <= pgi <= 141 and ('IV-4' in part or 'IV4' in part or 'ega4-18' in part):
        print(s[:500])
