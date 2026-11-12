# Read-only: print the source lines around the \oldpage markers of the given pages.
# usage: markers.py SOURCE.tex N1 N2 ...
import sys

sys.stdout.reconfigure(encoding="utf-8")
src = sys.argv[1]
raw = open(src, "rb").read().decode("utf-8")
print("line ends:", "CRLF" if "\r\n" in raw else "LF")
L = raw.replace("\r\n", "\n").split("\n")
for n in map(int, sys.argv[2:]):
    key = "{IV-1}]{%d}" % n
    for i, line in enumerate(L):
        if "oldpage" in line and key in line:
            print("== marker", n, "at line", i + 1)
            for j in range(max(0, i - 2), min(len(L), i + 3)):
                print("   %5d|%s" % (j + 1, L[j][:110]))
