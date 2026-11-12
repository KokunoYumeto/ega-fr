import sys
fn = sys.argv[1]
pages = [int(x) for x in sys.argv[2:]]
lines = open(fn, encoding='utf-8', newline='').read().split('\n')
for n in pages:
    key = r'\oldpage[0\textsubscript{I}]{%d}' % n
    for i, l in enumerate(lines):
        if key in l:
            print('=== page', n, 'line', i + 1)
            for j in range(max(0, i - 5), min(len(lines), i + 4)):
                print(j + 1, repr(lines[j]))
