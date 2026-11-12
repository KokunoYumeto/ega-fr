import re
import sys

path = sys.argv[1]
pat = sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 5
w = int(sys.argv[4]) if len(sys.argv) > 4 else 80
s = open(path, encoding='utf-8').read()
k = 0
for m in re.finditer(pat, s):
    k += 1
    if k > n:
        break
    a = max(0, m.start() - w)
    b = min(len(s), m.end() + w)
    sys.stdout.buffer.write(('>> ' + s[a:b].replace('\n', '\\n') + '\n').encode('utf-8'))
print('count', len(re.findall(pat, s)))
