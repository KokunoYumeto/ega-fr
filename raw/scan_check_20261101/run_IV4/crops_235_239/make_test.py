"""Copy ega4-20 (original and with findings_235_239 fixes applied) plus the IV-4 preamble into this folder as two
compile stubs. Nothing outside this folder is written."""
import json
import pathlib
import re
import shutil

HERE = pathlib.Path(__file__).resolve().parent
NAT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native")
src = (NAT / "ega4" / "ega4-20-fr.tex").read_text(encoding="utf-8")
shutil.copyfile(NAT / "preamble-base.tex", HERE / "preamble-base.tex")
main = (NAT / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = main[:main.index("\\begin{document}")]
findings = json.load(open(HERE.parent / "findings_235_239.json", encoding="utf-8"))
t = src
for x in findings:
    fx = x.get("fix")
    if not fx:
        continue
    cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", t)]
    s = dict(cuts)[x["page"]]
    e = min([c for n, c in cuts if c > s] + [len(t)])
    seg = t[s:e]
    assert seg.count(fx["old"]) == 1, (x["page"], fx["old"])
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
(HERE / "ega4-20-orig.tex").write_text(src, encoding="utf-8", newline="")
(HERE / "ega4-20-fixed.tex").write_text(t, encoding="utf-8", newline="")
for name in ("orig", "fixed"):
    stub = (pre + "\\begin{document}\n\\newcommand{\\shHom}{\\mathcal{H}\\!om}\n\\setcounter{section}{19}\n"
            "\\input{ega4-20-" + name + ".tex}\n\\end{document}\n")
    (HERE / f"stub20_{name}.tex").write_text(stub, encoding="utf-8")
print("ok", len(src), len(t))
