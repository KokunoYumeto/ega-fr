"""Write stub_260_264.tex: the IV-4 preamble plus pp. 260-264 with all findings applied (compile check only)."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
P = HERE.parent.parent / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native"
pre = (P / "ega4/EGA_IV4_FR.tex").read_text(encoding="utf-8")
head = pre[:pre.index(r"\begin{document}")]
head = head.replace(r"\input{preamble-base}", r"\input{" + (P / "preamble-base").as_posix() + "}")
body = (HERE / "applied_preview.tex").read_text(encoding="utf-8")
stub = (head + "\\begin{document}\n\\setcounter{section}{20}\n\\begin{env}[21.2.5]\n" + body
        + "\n\\end{proof}\n\\end{document}\n")
(HERE / "stub_260_264.tex").write_text(stub, encoding="utf-8")
print("ok")
