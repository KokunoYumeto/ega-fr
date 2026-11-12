"""List '(\\sref' occurrences (a reference macro that prints its own parentheses, inside another parenthesis)."""
import sys
from pathlib import Path

base = Path(sys.argv[1])
for name in sys.argv[2:]:
    text = (base / name).read_text(encoding="utf-8")
    start = 0
    needle = "(\\sref"
    while True:
        i = text.find(needle, start)
        if i < 0:
            break
        line = text.count("\n", 0, i) + 1
        print(name, line, text[i:i + 120].replace("\n", " "))
        start = i + 1
