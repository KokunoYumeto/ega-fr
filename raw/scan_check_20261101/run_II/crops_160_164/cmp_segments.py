import re
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (E / r"ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega2/ega2-1-fr.tex").read_text(encoding="utf-8")
m = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(src)]
for i, (n, s) in enumerate(cuts):
    if 159 <= n <= 165:
        e = cuts[i + 1][1]
        seg = src[s:e]
        pf = E / ("run_II/page_%03d.tex" % n)
        if not pf.exists():
            print(n, "no page file; segment tail:", repr(seg[-200:]))
            continue
        p = pf.read_bytes().decode("utf-8")
        crlf = "\r\n" in p
        p = p.replace("\r\n", "\n")
        body = p.split("\n", 1)[1]
        cont = "% (continued in" in body
        status = "same" if body == seg else ("prefix-same" if body.startswith(seg) else "DIFF")
        print(n, "crlf" if crlf else "lf", status, len(body), len(seg), "cont" if cont else "")
        if status == "DIFF":
            import difflib
            for ln in difflib.unified_diff(seg.splitlines(), body.splitlines(), lineterm="", n=1):
                print("   ", ln)
