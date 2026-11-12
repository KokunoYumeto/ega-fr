import re, pathlib
D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4")
pat = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}\n\n?(\\subsection|\\section)")
for fn in ["ega4-16-fr.tex", "ega4-17-fr.tex", "ega4-18-fr.tex", "ega4-20-fr.tex", "ega4-21a-fr.tex", "ega4-21b-fr.tex", "ega4-21c-fr.tex"]:
    t = (D / fn).read_text(encoding="utf-8")
    for m in pat.finditer(t):
        line = t.count("\n", 0, m.start()) + 1
        print(fn, line, repr(t[m.start():m.start() + 120]))
    # headings directly followed by a marker (marker after heading)
    pat2 = re.compile(r"(\\subsection\{[^\n]*\}\n(?:\\EGAReaderTarget[^\n]*\n)?)\n?\\oldpage\[IV-4\]\{(\d+)\}")
    for m in pat2.finditer(t):
        line = t.count("\n", 0, m.start()) + 1
        print("AFTER-HEADING", fn, line, repr(t[m.start():m.end()][:200]))
