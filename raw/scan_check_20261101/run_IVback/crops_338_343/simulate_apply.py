"""Apply findings_338_343.json to COPIES of the two source files (in crops_338_343/sim), with the locate() logic of
apply_fixes.py, then write a stub document that compiles the edited end matter. The real .tex files are not touched."""
import json
import pathlib
import re
import shutil

E = pathlib.Path(r"user/Documents/ega_scan_check_20261101")
SRC = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4"
SIM = E / "run_IVback/crops_338_343/sim"
SIM.mkdir(exist_ok=True)
names = ["ega4-backmatter-terminology-fr.tex", "ega4-backmatter-contents-fr.tex"]
for n in names:
    shutil.copyfile(SRC / n, SIM / n)
files = [SIM / n for n in names]
marker = re.compile(r"\\oldpage\[IV\]\{(\d+)\}")


def locate(page):
    for f in files:
        t = f.read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                j = i + 1
                while j < len(cuts) and cuts[j][0] == page:
                    j += 1
                return f, s, cuts[j][1] if j < len(cuts) else len(t)
    for f in files:
        t = f.read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
            if a < page < b:
                return f, sa, sb
    return None, None, None


d = json.load(open(E / "run_IVback/findings_338_343.json", encoding="utf-8"))
for x in d:
    fx = x["fix"]
    if not fx:
        continue
    f, s, e = locate(int(x["page"]))
    t = f.read_text(encoding="utf-8")
    seg = t[s:e]
    n = seg.count(fx["old"])
    print(x["page"], x["kind"], "count in segment:", n)
    assert n == 1
    f.write_text(t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:], encoding="utf-8", newline="")
print("applied")

stub = r"""\documentclass[10pt,oneside]{book}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[french]{babel}
\usepackage{amsmath,amssymb,mathrsfs}
\usepackage[colorlinks=true,hypertexnames=false,unicode=true,pdfencoding=auto]{hyperref}
\newcommand{\sh}{\mathcal}
\newcommand{\oldpage}[2][]{\setcounter{footnote}{0}\marginpar{\scriptsize\textbf{#1}~|~#2}\ignorespaces}
\begin{document}
\input{ega4-backmatter-terminology-fr.tex}
\input{ega4-backmatter-contents-fr.tex}
\clearpage
\oldpage[IV]{345}
ERRATA
\end{document}
"""
(SIM / "stub.tex").write_text(stub, encoding="utf-8")
print("stub written")
