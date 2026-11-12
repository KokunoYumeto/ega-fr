import re
import sys

p = sys.argv[1]
t = open(p, encoding="utf-8").read()
before_env = 0
after_env = 0
for m in re.finditer(r"\\oldpage\[0\\textsubscript\{III\}\]\{(\d+)\}", t):
    pre = t[max(0, m.start() - 120):m.start()]
    post = t[m.end():m.end() + 60]
    if re.search(r"\\begin\{[a-z]+\}(\[[^\]]*\])?\s*(\\label\{[^}]*\})?\s*$", pre):
        after_env += 1
        print("marker AFTER heading, page", m.group(1), repr(pre[-60:]))
    if re.match(r"\s*\\begin\{", post) or re.match(r"\s*\\(sub)?section", post):
        before_env += 1
        print("marker BEFORE heading, page", m.group(1), repr(post[:50]))
print("after", after_env, "before", before_env)
