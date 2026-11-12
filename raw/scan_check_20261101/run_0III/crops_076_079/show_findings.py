import json, sys
sys.stdout.reconfigure(encoding='utf-8')
fn = sys.argv[1]
needle = sys.argv[2] if len(sys.argv) > 2 else None
d = json.load(open(fn, encoding='utf-8'))
print('n =', len(d))
for f in d:
    s = json.dumps(f, ensure_ascii=False)
    if needle and needle.lower() not in s.lower():
        continue
    print(f.get('page'), f.get('kind'), f.get('convention'), '|', (f.get('where') or '')[:80], '|', (f.get('scan') or '')[:150], '|', (f.get('note') or '')[:300])
    print()
