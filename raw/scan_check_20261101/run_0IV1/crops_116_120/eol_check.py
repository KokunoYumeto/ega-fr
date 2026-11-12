import os
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(os.path.dirname(RUN), "ega-fr", "editions", "2026-10-24-r20", "diplomatic",
                 "packages", "IV1", "native", "ega4")
for p in (116, 117, 118, 119, 120):
    b = open(os.path.join(RUN, f"page_{p:03d}.tex"), "rb").read()
    print(p, "LF", b.count(b"\n"), "CRLF", b.count(b"\r\n"))
for f in ("ega0-19b-fr.tex", "ega0-20-fr.tex"):
    b = open(os.path.join(R, f), "rb").read()
    print(f, "LF", b.count(b"\n"), "CRLF", b.count(b"\r\n"))
