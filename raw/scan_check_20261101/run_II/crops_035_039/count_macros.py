import sys
t = open(sys.argv[1], encoding='utf-8').read()
for m in sys.argv[2:]:
    print(m, t.count(m))
