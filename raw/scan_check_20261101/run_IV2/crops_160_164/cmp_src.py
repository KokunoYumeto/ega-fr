"""Compare run_IV2/page_NNN.tex copies with the current source segments (read-only)."""
import difflib
import pathlib
import re
import sys

SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
src = SRC.read_text(encoding="utf-8")
m = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(src)]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for p in range(lo, hi + 1):
    idx = [k for k, (n, s) in enumerate(cuts) if n == p]
    if not idx:
        print(p, "marker not found in source")
        continue
    i = idx[0]
    seg = src[cuts[i][1]:cuts[i + 1][1]]
    f = RUN / f"page_{p:03d}.tex"
    raw = f.read_bytes()
    t = raw.decode("utf-8").replace("\r\n", "\n")
    body = t.split("\n", 1)[1]
    cont = body.find("% (continued in")
    if cont >= 0:
        body = body[:cont]
    print(p, "CRLF" if b"\r\n" in raw else "LF",
          "identical" if body == seg else f"DIFFERENT (src {len(seg)} vs page {len(body)})")
    if body != seg:
        for line in difflib.unified_diff(body.split("\n"), seg.split("\n"), lineterm="", n=0):
            print("   ", line[:160])
