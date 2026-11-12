"""Build test_page.tex (original pages 10-14) and test_applied.tex (with the findings' fixes) for a compile check."""
from pathlib import Path

here = Path(__file__).resolve().parent
run = here.parent
pkg = run.parent / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "IV4" / "native"
pre = (pkg / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
head = pre.split("\\begin{document}")[0]
head = head.replace("\\input{preamble-base}", "\\input{" + (pkg / "preamble-base.tex").as_posix() + "}")
for tag in ("applied", "page"):
    body = []
    for p in range(10, 15):
        src = here / f"applied_{p:03d}.tex" if tag == "applied" else run / f"page_{p:03d}.tex"
        body.append(src.read_text(encoding="utf-8"))
    doc = (head + "\\begin{document}\n\\setcounter{section}{16}\n\\begin{env}[16.2.1]\n"
           + "\n".join(body) + "\n\\end{proposition}\n\\end{document}\n")
    (here / f"test_{tag}.tex").write_text(doc, encoding="utf-8", newline="\n")
print("ok")
