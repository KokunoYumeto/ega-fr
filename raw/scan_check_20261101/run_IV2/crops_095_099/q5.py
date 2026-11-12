import json
d=json.load(open('run_IV2/findings_090_094.json',encoding='utf-8'))
for x in d:
    if x.get('kind')=='marker' and 'En particulier' in json.dumps(x,ensure_ascii=False):
        print(x['fix']['old']); print('-----NEW-----'); print(x['fix']['new']); print('-----NOTE-----'); print(x.get('note'))
d=json.load(open('run_IV2/findings_100_104.json',encoding='utf-8'))
for x in d:
    if x.get('page') in (99,100) and ('k(x)' in json.dumps(x,ensure_ascii=False) or 'boldsymbol' in json.dumps(x,ensure_ascii=False)):
        print(json.dumps(x,ensure_ascii=False)[:900]); print()
