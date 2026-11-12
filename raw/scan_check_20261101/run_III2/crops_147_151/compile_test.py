"""Compile test (temporary copies only): apply findings_147_151.json to a copy of the release ega3-6-fr.tex,
cut sections 6.4-6.5, and typeset them with the stub preamble. No source file is modified."""
import json
import pathlib
import re
import subprocess

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
NATIVE = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native"
REL = NATIVE / r"ega3\ega3-6-fr.tex"
OUTDIR = E / r"run_III2\crops_147_151\compile"
OUTDIR.mkdir(exist_ok=True)

t = REL.read_text(encoding="utf-8")
pat = re.compile(r"\\oldpage\[III\]\{(\d+)\}")


def seg_bounds(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in pat.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1]


for x in json.load(open(E / r"run_III2\findings_147_151.json", encoding="utf-8")):
    if not x.get("fix"):
        continue
    s, e = seg_bounds(t, x["page"])
    seg = t[s:e]
    assert seg.count(x["fix"]["old"]) == 1, x
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]

a = t.index(r"\subsection{Foncteurs hypertor locaux de complexes de Modules quasi-cohérents : cas des sch")
b = t.index(r"\subsection{Foncteurs hypertor globaux")
(OUTDIR / "part.tex").write_text(t[a:b], encoding="utf-8")

stub = (NATIVE / "stub_ega1-1-fr.tex").read_text(encoding="utf-8")
pre = stub[:stub.index(r"\begin{document}")]
pre = pre.replace(r"\input{preamble-base.tex}", r"\input{" + (NATIVE / "preamble-base.tex").as_posix() + "}")
(OUTDIR / "test.tex").write_text(pre + "\\begin{document}\n\\setcounter{section}{6}\\setcounter{subsection}{3}\n"
                                 "\\input{part.tex}\n\\end{document}\n", encoding="utf-8")
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "test.tex"], cwd=OUTDIR,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
log = (OUTDIR / "test.log").read_text(encoding="utf-8", errors="replace")
errs = [l for l in log.splitlines() if l.startswith("!")]
print("returncode", r.returncode, "errors", len(errs))
for l in errs[:20]:
    print(l)
print([l for l in log.splitlines() if "Output written" in l])
