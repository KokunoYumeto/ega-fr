import glob
import sys

root = sys.argv[1]
n = 0
for fn in sorted(glob.glob(root + '/ega*/*-fr.tex')):
    with open(fn, encoding='utf-8') as fh:
        for i, line in enumerate(fh, 1):
            k = line.find('\\oldpage')
            while k != -1:
                if k > 0:
                    n += 1
                    before = line[max(0, k - 70):k]
                    # report only markers that sit inside an open brace group
                    depth = line[:k].count('{') - line[:k].count('}')
                    if depth > 0 or n <= 6:
                        print(fn, i, 'depth', depth, repr(before + line[k:k + 45]))
                k = line.find('\\oldpage', k + 1)
print('total mid-line markers:', n)
