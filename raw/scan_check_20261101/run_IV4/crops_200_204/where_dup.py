import sys
sys.stdout.reconfigure(encoding="utf-8")
SRC = (r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/"
       r"diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex")
src = open(SRC, encoding="utf-8", newline="").read()
pats = [
    r"(resp. $X'$) où $X$ (resp. $X'$) est",
    r"un voisinage de $Y$ (resp. $Y'$).",
    r"\operatorname{Proj}(\operatorname{gr}_{\mathscr J}^*(\sh{O}_X))",
    r"\mathbf S_{\sh{O}_Y}^*(\sh{N}_{Y/X})",
    r"aux points de $U-Y$.",
    "\\end{enumerate}\nAlors on a les implications",
]
for p in pats:
    k = -1
    print("==", p.replace("\n", "\\n"))
    while True:
        k = src.find(p, k + 1)
        if k < 0:
            break
        line = src.count("\n", 0, k) + 1
        print("  line", line, "|", src[max(0, k - 120):k + len(p) + 60].replace("\n", "\\n"))
