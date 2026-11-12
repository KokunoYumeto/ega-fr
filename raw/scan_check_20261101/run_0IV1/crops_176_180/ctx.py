import sys
p = r"user/Documents/ega_scan_check_20261101/ega-fr/source/ega4/ega0-21-fr.tex"
raw = open(p, 'rb').read()
print("CRLF count:", raw.count(b'\r\n'), "LF count:", raw.count(b'\n'))
lines = raw.decode('utf-8').split('\n')
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for n in range(lo, hi + 1):
    tag = r"\oldpage[0\textsubscript{IV-1}]{%d}" % n
    idx = [i for i, l in enumerate(lines) if tag in l]
    print("=== page", n, "line(s)", [i + 1 for i in idx])
    for i in idx:
        for j in range(max(0, i - 3), min(len(lines), i + 2)):
            print("%5d| %r" % (j + 1, lines[j][:110]))
