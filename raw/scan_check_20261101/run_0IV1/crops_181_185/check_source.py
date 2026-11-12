import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_0IV1'
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\source\ega4'
d = json.load(open(RUN + r'\findings_181_185.json', encoding='utf-8'))
srcs = {}
for name in ('ega0-21-fr.tex', 'ega0-22-fr.tex'):
    with open(SRC + '\\' + name, encoding='utf-8', newline='') as fh:
        srcs[name] = fh.read()
    print(name, 'CRLF' if '\r\n' in srcs[name] else 'LF')

def segment(text, page):
    m = re.search(r'\\oldpage\[0\\textsubscript\{IV-1\}\]\{%d\}' % page, text)
    if not m:
        return None
    m2 = re.search(r'\\oldpage\[0\\textsubscript\{IV-1\}\]\{%d\}' % (page + 1), text)
    return text[m.start(): m2.start() if m2 else len(text)]

for x in d:
    fx = x['fix']
    if not fx:
        continue
    p = x['page']
    name = 'ega0-21-fr.tex' if p <= 182 and fx['old'] in srcs['ega0-21-fr.tex'] else 'ega0-22-fr.tex'
    full = srcs[name].count(fx['old'])
    seg = segment(srcs[name], p)
    nseg = seg.count(fx['old']) if seg else -1
    pre = srcs['ega0-22-fr.tex'][:srcs['ega0-22-fr.tex'].find('\\oldpage')]
    npre = pre.count(fx['old'])
    flag = ''
    if nseg != 1:
        flag = 'OUTSIDE-SEGMENT' if npre == 1 else 'CHECK'
    print(p, name, 'file:', full, 'segment:', nseg, 'pre-first-marker(22):', npre, flag, '|', x['where'][:60])
