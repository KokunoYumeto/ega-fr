import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'user\Documents\ega_scan_check_20261101\run_IV4\crops_215_219'
for n in [215, 216, 217, 218, 219]:
    t = open(rf'{base}\page_{n}_lf.tex', encoding='utf-8').read()
    print('=== page', n)
    k = 0
    for m in re.finditer(r'\\mathfrak [A-Za-z]', t):
        k += 1
        s = max(0, m.start() - 30)
        e = min(len(t), m.end() + 15)
        ctx = t[s:e].replace('\n', '\\n')
        sub = t[m.start()-1] == '_' or t[m.start()-2:m.start()] == '_{'
        print(f'{k:3d} {m.group(0)[-1]} {"SUB" if sub else "   "} ...{ctx}...')
