"""Compile pp. 209-214 (from the 19.6 heading to marker 215) before and after the simulated edits, in a private test
folder (nothing in the release is touched). Reports LaTeX errors and overfull/undefined-control-sequence lines."""
import pathlib
import re
import shutil
import subprocess

BASE = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
NATIVE = BASE / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native"
HERE = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4\crops_210_214")
TEST = HERE / "compile_test"
TEST.mkdir(exist_ok=True)
shutil.copy(NATIVE / "preamble-base.tex", TEST / "preamble-base.tex")
pre_src = (NATIVE / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = pre_src[:pre_src.index("\\begin{document}")]

for tag, path in [("orig", NATIVE / "ega4" / "ega4-18-fr.tex"), ("sim", HERE / "simulated_ega4-18.tex")]:
    t = path.read_text(encoding="utf-8")
    s = t.index("\\subsection{Suites régulières relativement à un module filtré quotient.}")
    e = t.index("\\oldpage[IV-4]{215}")
    body = t[s:e]
    stub = pre + "\\begin{document}\n\\setcounter{section}{19}\\setcounter{subsection}{5}\n" + body + "\n\\end{document}\n"
    (TEST / f"stub_{tag}.tex").write_text(stub, encoding="utf-8")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"stub_{tag}.tex"], cwd=TEST,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    log = (TEST / f"stub_{tag}.log").read_text(encoding="utf-8", errors="replace")
    errs = [ln for ln in log.splitlines() if ln.startswith("!")]
    print(tag, "exit", r.returncode, "errors:", len(errs))
    for ln in errs[:10]:
        print("   ", ln)
    m = re.search(r"Output written on .*\((\d+) pages?", log)
    print("   ", m.group(0) if m else "no output")
