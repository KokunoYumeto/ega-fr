import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p = r'user\Documents\ega_scan_check_20261101\run_IV4\crops_215_219\make_findings.py'
s = open(p, encoding='utf-8').read()
rx = re.compile(r"r'((?:[^'\n]|'')*'')((?:[^'\n]|'')*)'")
def rep(m):
    inner = (m.group(1) + m.group(2)).replace("''", "'")
    assert '"' not in inner
    return 'r"' + inner + '"'
n = 0
out_lines = []
for line in s.split('\n'):
    new = rx.sub(rep, line)
    if new != line:
        n += 1
        print('OLD:', line[:150])
        print('NEW:', new[:150])
    out_lines.append(new)
open(p, 'w', encoding='utf-8').write('\n'.join(out_lines))
print('changed lines', n)
