# Builds a small test document: the IV-4 preamble + the fixed excerpt (pp. 284-290) of ega4-21b, to check that the
# proposed edits compile. Nothing in the release tree is touched.
import pathlib, re
base = pathlib.Path(r"user/Documents/ega_scan_check_20261101")
nat = base / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native"
out = base / "run_IV4/crops_285_289/compile_test"
out.mkdir(exist_ok=True)
pre = (nat / "ega4/EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = pre.split("\\begin{document}")[0]
pre = pre.replace("\\input{preamble-base}", "\\input{" + (nat / "preamble-base.tex").as_posix() + "}")
fixed = (base / "run_IV4/crops_285_289/ega4-21b_after_fixes_preview.txt").read_text(encoding="utf-8")
a = fixed.index("\\begin{lemma}[21.9.2]")
b = fixed.index("\\begin{env}[21.10.2]")
body = fixed[a:b]
(out / "test.tex").write_text(pre + "\\begin{document}\n\\setcounter{section}{21}\n" + body + "\n\\end{document}\n",
                              encoding="utf-8", newline="")
print(len(body))
