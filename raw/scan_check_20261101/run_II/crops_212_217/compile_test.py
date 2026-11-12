"""Compile test for findings_212_217.json: apply the fixes to COPIES of the two EGA II back-matter files inside
this crops folder (segment-wise, like apply_fixes.py) and compile them, unmodified and modified, with the stub
preamble. Never touches the release files."""
import json
import pathlib
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
NATIVE = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                      r"\diplomatic\packages\BASE\native")
FIND = HERE.parent / "findings_212_217.json"
FILES = ["ega2-indexes-and-contents-fr.tex", "ega2-errata-addenda-fr.tex"]
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")

stub_src = (NATIVE / "stub_ega1-10-fr.tex").read_text(encoding="utf-8")
pre = stub_src[:stub_src.index("\\begin{document}")]


def build(tag, modify):
    d = HERE / f"test_{tag}"
    if d.exists():
        shutil.rmtree(d)
    (d / "ega2").mkdir(parents=True)
    shutil.copy(NATIVE / "preamble-base.tex", d / "preamble-base.tex")
    texts = {f: (NATIVE / "ega2" / f).read_text(encoding="utf-8") for f in FILES}
    if modify:
        for x in json.load(open(FIND, encoding="utf-8")):
            o, n, p = x["fix"]["old"], x["fix"]["new"], int(x["page"])
            done = False
            for f in FILES:
                t = texts[f]
                cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
                for i, (q, s) in enumerate(cuts):
                    if q == p:
                        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
                        seg = t[s:e]
                        assert seg.count(o) == 1, (p, o)
                        texts[f] = t[:s] + seg.replace(o, n) + t[e:]
                        done = True
                        break
                if done:
                    break
            assert done, (p, o)
    for f in FILES:
        (d / "ega2" / f).write_text(texts[f], encoding="utf-8", newline="")
    body = "\\begin{document}\n" + "".join(f"\\input{{ega2/{f}}}\n" for f in FILES) + "\\end{document}\n"
    (d / "stub.tex").write_text(pre + body, encoding="utf-8", newline="")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "stub.tex"], cwd=d,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    log = (d / "stub.log").read_text(encoding="utf-8", errors="replace") if (d / "stub.log").exists() else ""
    errs = [l for l in log.splitlines() if l.startswith("!")]
    pages = re.findall(r"Output written on stub.pdf \((\d+) pages?", log)
    print(tag, "exit", r.returncode, "errors", errs[:5], "pages", pages)
    return d


build("orig", False)
build("fixed", True)
