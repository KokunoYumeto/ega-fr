import re
import sys

for fn in sys.argv[1:]:
    t = open(fn, encoding='utf-8').read()
    m = re.findall(r'\\begin\{env\}\[([0-9.]+)\]\n\\label\{[^}]*\}\n\\\[', t)
    print(fn, len(m), m[:40])
