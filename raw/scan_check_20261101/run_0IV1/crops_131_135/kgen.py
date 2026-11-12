import sys, json
R = '\\mathfrak{R}'
K = '\\mathfrak{K}'
BASE = sys.argv[1]

def page_text(p):
    with open(f'{BASE}/page_{p:03d}.tex', encoding='utf-8', newline='') as f:
        return f.read().replace('\r\n', '\n')

def minimal(text, lines, ln):
    """Short unique substring around all R occurrences of line ln (1-based)."""
    line = lines[ln - 1]
    i = line.find(R)
    j = line.rfind(R) + len(R)
    def ext_left(i):
        k = i
        while k > 0 and line[k - 1] not in ' $':
            k -= 1
        if k > 0 and line[k - 1] == '$':
            k -= 1
        return k
    def ext_right(j):
        k = j
        while k < len(line) and line[k] not in ' $':
            k += 1
        if k < len(line) and line[k] == '$':
            k += 1
        return k
    a, b = ext_left(i), ext_right(j)
    cand = line[a:b]
    steps = 0
    while text.count(cand) != 1 and steps < 12:
        na, nb = a, b
        if na > 0:
            na = na - 1
            while na > 0 and line[na - 1] != ' ':
                na -= 1
        if nb < len(line):
            nb = nb + 1
            while nb < len(line) and line[nb] != ' ':
                nb += 1
        if (na, nb) == (a, b):
            break
        a, b = na, nb
        cand = line[a:b]
        steps += 1
    if text.count(cand) != 1:
        # add the following line
        cand = line.strip() + '\n' + lines[ln].strip()
        cand = line.lstrip() + '\n' + lines[ln]
        if text.count(cand) != 1:
            cand = lines[ln - 2] + '\n' + line
    return cand

if __name__ == '__main__':
    spec = json.loads(sys.argv[2])
    out = []
    for p, lns in spec.items():
        p = int(p)
        t = page_text(p)
        L = t.split('\n')
        for ln in lns:
            c = minimal(t, L, ln)
            out.append({'page': p, 'line': ln, 'old': c, 'count': t.count(c), 'nR': c.count(R), 'lineR': L[ln - 1].count(R)})
    print(json.dumps(out, ensure_ascii=True, indent=0))
