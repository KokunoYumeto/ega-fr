# Writes stub_orig.tex and stub_fixed.tex (pages 197-201 concatenated) to compile-check the proposed fixes.
import pathlib
here = pathlib.Path(__file__).resolve().parent
run = here.parent
src = run.parent / "ega-fr" / "source"
main = (src / "EGA_FR.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
pre = main.split("\\begin{document}")[0]
pre = pre.replace("\\input{preamble-base.tex}", "\\input{" + (src / "preamble-base.tex").as_posix() + "}")
head = "\\begin{remark}[7.6.11]\n\\begin{proof}\n"
tail = "\\end{proof}\n"
for name, get in (("orig", lambda n: (run / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")),
                  ("fixed", lambda n: (here / f"fixed_{n}.tex").read_text(encoding="utf-8"))):
    body = "".join(get(n) for n in range(197, 202))
    doc = pre + "\\begin{document}\n\\setcounter{section}{7}\\setcounter{subsection}{6}\n" + head + body + tail + "\\end{document}\n"
    (here / f"stub_{name}.tex").write_text(doc, encoding="utf-8")
    print("wrote", here / f"stub_{name}.tex")
