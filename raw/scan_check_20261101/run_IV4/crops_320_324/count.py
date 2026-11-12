"""Count occurrences of candidate strings in ega4-21c-fr.tex (LF)."""
SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions"
       r"\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-21c-fr.tex")
s = open(SRC, encoding="utf-8").read().replace("\r\n", "\n")
cands = [
    r"$U_y=T_y-\{y\}$",
    r"$U_y=T_y-\{y\}$, l'hypothèse",
    r"$U=X-\{a\}$",
    r"$U=X-\{a\}$, $U'=f^{-1}(U)$",
    "noethérien \\emph{normal},",
    "noethérien \\emph{normal},\n$(U_\\lambda)",
]
for c in cands:
    print(s.count(c), repr(c))
    i = -1
    while True:
        i = s.find(c, i + 1)
        if i < 0:
            break
        print("   line", s.count("\n", 0, i) + 1)
