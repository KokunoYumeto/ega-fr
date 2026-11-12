import sys, re
from collections import Counter
for p in sys.argv[1:]:
    t = open(f"page_{p}.tex", encoding="utf-8").read()
    names = re.findall(r"\\([A-Za-z]+)", t)
    want = [n for n in names if "phi" in n.lower() or n in ("psi", "theta", "kappa", "mathfrak", "mathscr", "mathbf", "boldsymbol", "mathrm", "emph", "textup", "sh", "mathcal", "isoto", "simeq", "mapsto", "longrightarrow", "to", "cdots", "ldots", "qquad", "sref", "ref", "textbf", "widetilde", "supertilde", "otimes")]
    print(p, dict(Counter(want)))
