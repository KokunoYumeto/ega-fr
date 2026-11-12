import pathlib
import shutil

base = pathlib.Path("user/Documents/ega_scan_check_20261101")
pkg = base / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native"
here = base / "run_IVback/crops_355_359"
pre_full = (pkg / "ega4/EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = pre_full[: pre_full.index("\\begin{document}")]
shutil.copy(pkg / "preamble-base.tex", here / "preamble-base.tex")
shutil.copy(pkg / "ega4/ega4-errata-addenda-list3-fr.tex", here / "errata_orig_test.tex")
for name in ("errata_orig_test", "errata_applied_test"):
    stub = pre + "\\begin{document}\n\\newcommand{\\shHom}{\\mathcal{H}\\!om}\n\\input{" + name + ".tex}\n\\end{document}\n"
    (here / ("stub_" + name + ".tex")).write_text(stub, encoding="utf-8")
    print("stub_" + name + ".tex")
