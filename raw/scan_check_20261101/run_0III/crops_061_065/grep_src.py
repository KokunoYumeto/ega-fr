"""grep_src.py FILE PATTERN [MAX] : print line numbers and short contexts of a literal PATTERN in FILE (UTF-8)."""
import sys
path, pat = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 40
t = open(path, encoding='utf-8').read()
lines = t.split('\n')
n = 0
for i, line in enumerate(lines, 1):
    if pat in line:
        n += 1
        if n <= mx:
            print(i, line.strip()[:160].encode('ascii', 'backslashreplace').decode())
print('count lines:', n, 'total occurrences:', t.count(pat))
