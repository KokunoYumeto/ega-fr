# Writes test_202_206.tex: the patched pages 202-206 inside the edition's preamble and environments.
import os
RUN = r"user\Documents\ega_scan_check_20261101\run_III2"
C = os.path.join(RUN, "crops_202_206")
NATIVE = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/current/packages/BASE/native"
drv = open(os.path.join(NATIVE, "EGA_FR.tex"), encoding="utf-8").read().splitlines()
pre = drv[:9]                                  # documentclass .. tikz-cd
start = next(i for i, l in enumerate(drv) if l.startswith(r"\renewcommand{\thesection}"))
end = next(i for i, l in enumerate(drv) if l.startswith(r"\begin{document}"))
envs = [l for l in drv[start:end] if not l.startswith(r"\makeatletter") and "EGAReaderTarget" not in l and not l.startswith(r"\makeatother")]
body = []
for p in range(202, 207):
    body.append(open(os.path.join(C, f"patched_page_{p}.tex"), encoding="utf-8").read())
doc = "\n".join(pre) + "\n\\usepackage{hyperref}\n\\input{" + NATIVE + "/preamble-base.tex}\n" + "\n".join(envs) + \
      "\n\\begin{document}\n\\begin{proof}\n" + "".join(body) +"\n\\end{lemma}\n\\end{proof}\n\\end{document}\n"
open(os.path.join(C, "test_202_206.tex"), "w", encoding="utf-8", newline="\n").write(doc)
print("ok")
