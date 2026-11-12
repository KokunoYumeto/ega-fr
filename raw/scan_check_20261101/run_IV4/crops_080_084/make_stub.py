import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
NATIVE = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native"
main = (NATIVE / "ega4/EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = main.split(r"\begin{document}")[0]
pre = pre.replace(r"\input{preamble-base}", r"\input{" + (NATIVE / "preamble-base").as_posix() + "}")
here = pathlib.Path(__file__).parent
seg = (here / "final_segment_80_85.tex").read_text(encoding="utf-8")
doc = pre + "\\begin{document}\n\\setcounter{section}{17}\\setcounter{subsection}{8}\n" + seg + "\n\\end{document}\n"
(here / "stub_080_084.tex").write_text(doc, encoding="utf-8")
print("ok", len(doc))
