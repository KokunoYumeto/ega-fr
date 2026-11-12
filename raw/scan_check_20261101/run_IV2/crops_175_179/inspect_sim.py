import sys, json
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"user\Documents\ega_scan_check_20261101\run_IV2\crops_175_179\simulated_after_fixes.tex", encoding="utf-8").read()
keys = [
    r"et soit $C_\alpha$ la fermeture",
    r"$B'_\alpha$ il en",
    r"\frac{tu}",
    "\\end{proof}\n\n\\begin{proposition}[6.15.6]",
    r"\otimes_{\mathbf{k}(y)}",
    r"$C'_0=C\otimes_A A'$",
    r"$B'_\lambda=B'_\lambda\otimes_A A'$",
    r"\emph{sans que}",
    r"hypothèse on a",
]
for k in keys:
    i = t.find(k)
    print("=====", repr(k), i, "count", t.count(k))
    if i >= 0:
        print(t[max(0, i - 200):i + 260])
# also: no two markers for the same page, and marker order
import re
marks = re.findall(r"\\oldpage\[IV-2\]\{(\d+)\}", t)
print("markers:", marks)
a = t.index(r"\oldpage[IV-2]{175}"); b = t.index(r"\oldpage[IV-2]{180}")
s = t[a:b]
for m in re.finditer(r"(?<![A-Za-z\\])k\(", s):
    print("PLAIN k( at", m.start(), repr(s[max(0, m.start() - 50):m.start() + 20]))
print("boldsymbol k:", s.count(r"\boldsymbol{k}"), " mathbf k:", s.count(r"\mathbf{k}"))
d = json.load(open(r"user\Documents\ega_scan_check_20261101\run_IV2\findings_175_179.json", encoding="utf-8"))
print("json entries:", len(d), "keys:", sorted(set(k for x in d for k in x)))
