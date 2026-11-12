"""Apply findings_010_014.json to a copy of the release segment for pp. II 10-14 and compile it (crops folder only)."""
import json
import pathlib
import re
import subprocess

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
HERE = E / "run_II" / "crops_010_014"
REL = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex"
STUB = E / r"ega-fr\source\stub_ega1-1-fr.tex"
BASE = (E / r"ega-fr\source\preamble-base.tex").as_posix()

F = json.load(open(E / "run_II" / "findings_010_014.json", encoding="utf-8"))
rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
start = [s for n, s in cuts if n == 10][0]
end = [s for n, s in cuts if n == 15][0]
segs = {}
for i, (n, s) in enumerate(cuts):
    if 10 <= n <= 14:
        segs[n] = rel[s:cuts[i + 1][1]]
for x in F:
    if x["fix"]:
        seg = segs[x["page"]]
        assert seg.count(x["fix"]["old"]) == 1, x["where"]
        segs[x["page"]] = seg.replace(x["fix"]["old"], x["fix"]["new"], 1)
tail = rel[end:]
tail = tail[:tail.index(r"\end{env}") + len(r"\end{env}")]  # close the (1.7.1) env that runs into p. 15
body = "".join(segs[n] for n in range(10, 15)) + tail
pre = STUB.read_text(encoding="utf-8").split(r"\begin{document}")[0]
pre = pre.replace(r"\input{preamble-base.tex}", r"\input{" + BASE + "}")
doc = pre + "\\begin{document}\n" + body + "\n\\end{document}\n"
for name, text in (("test_fixed.tex", doc),):
    (HERE / name).write_text(text, encoding="utf-8", newline="\n")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name], cwd=HERE,
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
    log = (HERE / name.replace(".tex", ".log")).read_text(encoding="utf-8", errors="replace")
    errs = [ln for ln in log.splitlines() if ln.startswith("!")]
    print(name, "exit", r.returncode, "errors:", errs[:5])
