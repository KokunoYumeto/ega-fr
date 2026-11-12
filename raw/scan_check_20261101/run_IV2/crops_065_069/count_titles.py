import re, sys

sys.stdout.reconfigure(encoding='utf-8')
t = open(sys.argv[1], encoding='utf-8').read()
pat = re.compile(r'\\subsection\{((?:[^{}]|\{[^{}]*\})*)\}')
titles = pat.findall(t)
print(len(titles), 'titles;', sum(1 for x in titles if x.rstrip().endswith('.')), 'end with a full stop')
