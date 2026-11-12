import json, pathlib

NATIVE = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current\packages\BASE\native")
HERE = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II\crops_140_144")
F = json.load(open(HERE.parent / "findings_140_144.json", encoding="utf-8"))

pre = (NATIVE / "EGA_FR.tex").read_text(encoding="utf-8")
pre = pre[:pre.index("\\begin{document}")]
src = (NATIVE / "ega2" / "ega2-1-fr.tex").read_text(encoding="utf-8")

def segment(p):
    a = src.index("\\oldpage[II]{%d}" % p)
    b = src.index("\\oldpage[II]{%d}" % (p + 1))
    return src[a:b]

body_fixed, body_orig = [], []
for p in range(140, 145):
    seg = segment(p)
    body_orig.append(seg)
    for f in F:
        if f["page"] == p and f["fix"]:
            assert seg.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"])
            seg = seg.replace(f["fix"]["old"], f["fix"]["new"], 1)
    body_fixed.append(seg)

head = "\\begin{document}\n\\begin{env}[7.1.5]\nDEBUT\n"
tail = "\\end{enumerate}\n\\end{theorem}\n\\end{document}\n"
for name, body in (("test_fixed.tex", body_fixed), ("test_orig.tex", body_orig)):
    (HERE / name).write_text(pre.replace("\\input{preamble-base.tex}", "\\input{" + (NATIVE / "preamble-base.tex").as_posix() + "}")
                             + head + "".join(body) + tail, encoding="utf-8")
    print(name)
