import json,glob,re,sys
pat = re.compile(sys.argv[1])
for fn in sorted(glob.glob('findings_*.json')):
    d=json.load(open(fn,encoding='utf-8'))
    for x in d:
        s=json.dumps(x,ensure_ascii=False)
        if pat.search(s):
            print(fn, s[:1000])
            print()
