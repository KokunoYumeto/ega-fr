import re, sys
p = sys.argv[1]
t = open(p, encoding='utf-8').read().split('\n')
stack = []
hits = {}
pat = re.compile(r'\\(begin|end)\{([a-zA-Z*]+)\}|\\item\[\\emph\{')
for i, line in enumerate(t, 1):
    for m in pat.finditer(line):
        if m.group(0).startswith('\\item'):
            outer = [e for e in stack if e not in ('enumerate', 'itemize', 'quote')]
            env = outer[-1] if outer else 'none'
            hits.setdefault(env, []).append(i)
        elif m.group(1) == 'begin':
            stack.append(m.group(2))
        else:
            if stack and stack[-1] == m.group(2):
                stack.pop()
            elif m.group(2) in stack:
                while stack and stack[-1] != m.group(2):
                    stack.pop()
                if stack:
                    stack.pop()
for k, v in hits.items():
    print(k, len(v), v[:60])
