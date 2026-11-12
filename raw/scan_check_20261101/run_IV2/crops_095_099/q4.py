import json,glob
for f in ['run_IV2/findings_100_104.json','run_IV2/findings_090_094.json']:
    try:
        d=json.load(open(f,encoding='utf-8'))
    except Exception as e:
        print(f, 'not available', e); continue
    for x in d:
        if x.get('page') in (94,95,99,100) and (x.get('kind')=='marker' or x.get('page') in (94,95,99) or 'caténaire n' in json.dumps(x,ensure_ascii=False) or 'deg.tr' in json.dumps(x,ensure_ascii=False)):
            print(f, json.dumps(x,ensure_ascii=False)[:1200]); print()
