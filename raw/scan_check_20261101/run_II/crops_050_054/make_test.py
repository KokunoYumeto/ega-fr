# Writes test_after.tex: the EGA_FR preamble plus the fixed segments of pp. 50-54 (from build_findings.py).
import pathlib

C = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II\crops_050_054")
NATIVE = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                      r"\diplomatic\packages\BASE\native")
pre = (NATIVE / "EGA_FR.tex").read_text(encoding="utf-8").split("\\begin{document}")[0]
pre = pre.replace("\\input{preamble-base.tex}",
                  "\\input{" + str(NATIVE / "preamble-base.tex").replace("\\", "/") + "}")
body = "".join((C / f"p{p:03d}_after_fixes.tex").read_text(encoding="utf-8") for p in range(50, 55))
doc = pre + "\\begin{document}\n\\begin{env}[3.1.1]\n" + body + "\n\\end{document}\n"
(C / "test_after.tex").write_text(doc, encoding="utf-8")
print("written", len(doc))
