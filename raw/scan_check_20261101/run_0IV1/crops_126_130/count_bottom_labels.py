import re
BS = "\\"
f = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-20-fr.tex"
t = open(f, encoding="utf-8").read()
marks = [(m.start(), int(m.group(1))) for m in re.finditer(re.escape(BS + "oldpage[0" + BS + "textsubscript{IV-1}]{") + r"(\d+)\}", t)]
def page_of(pos):
    p = None
    for s, n in marks:
        if s <= pos:
            p = n
    return p
n = 0
for m in re.finditer(re.escape(BS + "xymatrix{"), t):
    # find matching brace
    i = m.end(); depth = 1
    while depth:
        c = t[i]
        if c == "{": depth += 1
        elif c == "}": depth -= 1
        i += 1
    body = t[m.end():i-1]
    rows = body.split(BS + BS)
    if len(rows) == 2 and (BS + "ar[r]^") in rows[1]:
        n += 1
        print("p.", page_of(m.start()), "bottom row with \\ar[r]^:", rows[1].strip().replace("\n", " ")[:90])
print("total", n)
