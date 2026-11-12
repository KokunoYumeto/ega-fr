"""Write two LaTeX test files (.ltx, not edition sources) for pages 137-142: the original diplomatic segment and the
segment after the simulated fixes, each with the EGA_FR.tex preamble."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
C = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1\crops_137_141")
NAT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native")
pre_t = (NAT / "EGA_FR.tex").read_text(encoding="utf-8")
pre = pre_t[:pre_t.index("\\begin{document}")]
pre = pre.replace("\\input{preamble-base.tex}", "\\input{" + (NAT / "preamble-base.tex").as_posix() + "}")


def seg(t):
    a = t.index("\\oldpage[III]{137}")
    b = t.index("\\oldpage[III]{143}")
    return t[a:b]


orig = (NAT / "ega3" / "ega3-1-fr.tex").read_text(encoding="utf-8")
sim = (C / "sim_after_fixes.txt").read_text(encoding="utf-8")
for name, t in (("test_orig", orig), ("test_fixed", sim)):
    s = seg(t)
    closers = ""
    for env in ("enumerate", "proof", "corollary", "proposition", "remarks", "env"):
        open_n = s.count("\\begin{" + env + "}") - s.count("\\end{" + env + "}")
        closers += ("\\end{" + env + "}\n") * max(0, open_n)
    body = "\\begin{document}\n\\setcounter{section}{4}\\setcounter{subsection}{4}\n" + s + "\n" + closers + "\\end{document}\n"
    (C / (name + ".ltx")).write_text(pre + body, encoding="utf-8", newline="\n")
    print("written", name + ".ltx")
