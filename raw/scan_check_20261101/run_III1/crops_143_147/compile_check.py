"""Apply findings_143_147.json to an in-memory copy of the diplomatic ega3-1-fr.tex (as apply_fixes.py would, plus the
hand-applied p. 143 marker edit) and compile pages 142-147 with the stub preamble in this folder. The release file is
not written."""
import json
import pathlib
import re
import subprocess

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
HERE = pathlib.Path(__file__).resolve().parent
DIP = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex"
STUB = E / r"ega-fr\source\stub_ega1-1-fr.tex"
PRE = (E / r"ega-fr\source\preamble-base.tex").as_posix()
MARK = re.compile(r"\\oldpage\[III\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in MARK.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)


t = DIP.read_text(encoding="utf-8")
F = json.load(open(E / "run_III1" / "findings_143_147.json", encoding="utf-8"))
for x in F:
    if not x["fix"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    if seg.count(x["fix"]["old"]) == 1:
        t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
    elif t.count(x["fix"]["old"]) == 1:
        t = t.replace(x["fix"]["old"], x["fix"]["new"])
    else:
        raise SystemExit("cannot apply: " + x["where"])
a = t.find(r"\begin{proposition}[4.6.7]")
b = t.find(r"\oldpage[III]{148}")
body = t[a:b] + "\n\\end{proof}\n"
stub = STUB.read_text(encoding="utf-8")
pre = stub[:stub.index(r"\begin{document}")].replace(r"\input{preamble-base.tex}", r"\input{" + PRE + "}")
doc = pre + "\\begin{document}\n\\setcounter{section}{4}\\setcounter{subsection}{6}\n" + body + "\\end{document}\n"
(HERE / "check_143_147.tex").write_text(doc, encoding="utf-8")
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "check_143_147.tex"], cwd=HERE,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
log = (HERE / "check_143_147.log").read_text(encoding="utf-8", errors="replace")
errs = [l for l in log.splitlines() if l.startswith("!")]
print("exit", r.returncode, "errors:", errs[:10])
print("dollar signs balanced per paragraph:",
      all(p.replace(r"\$", "").count("$") % 2 == 0 for p in body.split("\n\n")))
