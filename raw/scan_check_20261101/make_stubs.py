"""Compile stubs: the EGA_FR.tex preamble plus one section file, to check edits quickly.
usage: python make_stubs.py SOURCE_DIR REL_PATH [REL_PATH ...]   (REL_PATH like ega1/ega1-1-fr.tex)"""
import pathlib
import sys

src = pathlib.Path(sys.argv[1])
t = (src / "EGA_FR.tex").read_text(encoding="utf-8")
pre = t[:t.index("\\begin{document}")]
for name in sys.argv[2:]:
    stub = pre + "\\begin{document}\n\\input{" + name + "}\n\\end{document}\n"
    (src / ("stub_" + pathlib.Path(name).stem + ".tex")).write_text(stub, encoding="utf-8")
    print("stub_" + pathlib.Path(name).stem + ".tex")
