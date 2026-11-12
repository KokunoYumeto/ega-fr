"""List \\oldpage markers (same part, same page) that occur more than once across the release files of each package."""
import collections
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])
pat = re.compile(r"\\oldpage\[([^\]]*)\]\{(\d+)\}")
for pkg in sorted(p for p in root.iterdir() if p.is_dir()):
    seen = collections.defaultdict(list)
    for f in sorted(pkg.glob("native/**/*.tex")):
        t = f.read_text(encoding="utf-8")
        for m in pat.finditer(t):
            line = t.count("\n", 0, m.start()) + 1
            seen[(m.group(1), int(m.group(2)))].append(f"{f.name}:{line}")
    dups = {k: v for k, v in seen.items() if len(v) > 1}
    print(pkg.name, "markers", len(seen), "duplicated", len(dups))
    for k, v in sorted(dups.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        print("  ", k[0], k[1], v)
