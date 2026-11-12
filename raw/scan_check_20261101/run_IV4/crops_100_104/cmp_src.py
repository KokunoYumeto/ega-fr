import re, pathlib
src = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-17-fr.tex").read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]
reg = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(src)
    reg[n] = src[s:e]
base = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
for p in range(100, 105):
    raw = (base / f"page_{p:03d}.tex").read_bytes()
    t = raw.decode("utf-8")
    crlf = "\r\n" in t
    t = t.replace("\r\n", "\n")
    first, rest = t.split("\n", 1)
    same = (rest == reg[p])
    print(p, "CRLF" if crlf else "LF", "same" if same else "DIFF", len(rest), len(reg[p]))
    if not same:
        a, b = rest, reg[p]
        k = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
        print("  first diff at", k, repr(a[max(0, k - 80):k + 80]), "|||", repr(b[max(0, k - 80):k + 80]))
    print("  head:", repr(reg[p][:60]))
    print("  tail:", repr(reg[p][-60:]))
