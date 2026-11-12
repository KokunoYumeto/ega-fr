import sys, re
from collections import Counter
for f in sys.argv[1:]:
    t = open(f, encoding="utf-8").read()
    c = Counter(re.findall(r"\\(vphi|varphi|phi|Phi|varPhi)(?![A-Za-z])", t))
    print(f.split("/")[-1], dict(c))
