import json
for fn in ['run_IV2/findings_090_094.json','run_IV2/findings_100_104.json']:
    d=json.load(open(fn,encoding='utf-8'))
    for x in d:
        if x.get('page') in (95,96,97,98,99):
            print(fn, x.get('page'), x.get('kind'), x.get('where')[:120])
