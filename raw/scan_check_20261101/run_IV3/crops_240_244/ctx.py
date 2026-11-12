"""Show context around \\oldpage[IV-3]{N} markers in the r20 sources (read-only)."""
import sys

root = "user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/"
files = sys.argv[1].split(",")
pages = [int(x) for x in sys.argv[2].split(",")]
for v in ("current", "diplomatic"):
    for fn in files:
        p = root + v + "/packages/IV3/native/ega4/" + fn
        try:
            t = open(p, "rb").read()
        except FileNotFoundError:
            print(v, fn, "missing")
            continue
        print("==", v, fn, "CRLF" if b"\r\n" in t else "LF", len(t))
        first = t.find(b"\\oldpage[")
        print("   first marker at", first, repr(t[first:first + 25]))
        for n in pages:
            m = ("\\oldpage[IV-3]{%d}" % n).encode()
            i = t.find(m)
            if i < 0:
                continue
            line = t[:i].count(b"\n") + 1
            print("  ", n, "line", line, repr(t[max(0, i - 70):i + 70]))
