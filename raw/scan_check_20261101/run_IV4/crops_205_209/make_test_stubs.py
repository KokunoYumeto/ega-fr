import pathlib

HERE = pathlib.Path(__file__).parent
pre_path = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                        r"\packages\IV4\native\ega4\EGA_IV4_FR.tex")
t = pre_path.read_text(encoding="utf-8")
pre = t[:t.index(r"\begin{document}")]
for name in ("test_patched", "test_orig", "test_corrected"):
    stub = (pre + "\\begin{document}\n\\setcounter{section}{19}\\setcounter{subsection}{4}\n"
            + "\\input{" + name + "}\n\\end{document}\n")
    (HERE / ("stub_" + name + ".tex")).write_text(stub, encoding="utf-8", newline="\n")
print("ok")
