import glob
import re
from collections import Counter

files = sorted(glob.glob(r"user\Documents\ega_scan_check_20261101\run_IV3\crops_145_149\sim_page_14[5-9].tex"))
t = "".join(open(f, encoding="utf-8").read() for f in files)
b = Counter(re.findall(r"\\begin\{(\w+)\}", t))
e = Counter(re.findall(r"\\end\{(\w+)\}", t))
print("begin", dict(b))
print("end  ", dict(e))
# order check: walk the begin/end sequence as a stack
stack = []
for m in re.finditer(r"\\(begin|end)\{(\w+)\}", t):
    kind, name = m.groups()
    if kind == "begin":
        stack.append(name)
    else:
        if not stack or stack[-1] != name:
            print("MISMATCH at", t[max(0, m.start() - 60):m.start() + 20].replace("\n", " | "), "stack", stack)
        else:
            stack.pop()
print("open at the end of p. 149:", stack)
