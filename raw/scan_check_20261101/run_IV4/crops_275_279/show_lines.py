"""Print numbered lines of a page file (CRLF normalised), optionally a line range.
usage: python show_lines.py PAGE [FROM TO]"""
import pathlib
import sys

R = pathlib.Path(__file__).resolve().parent.parent
p = int(sys.argv[1])
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
lines = (R / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
for i, l in enumerate(lines, 1):
    if a <= i <= b:
        sys.stdout.buffer.write(f"{i:3d}| {l}\n".encode("utf-8"))
