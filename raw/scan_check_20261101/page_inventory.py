"""Which ega-fr files the readers really use, and which original pages they cover.
Follows \\input{...} from EGA_FR.tex and ega4/EGA_IV{1..4}_FR.tex; collects \\oldpage[PART]{N} markers.
usage: python page_inventory.py EGA_FR_SOURCE_DIR OUT_JSON"""
import collections
import json
import pathlib
import re
import sys

src = pathlib.Path(sys.argv[1])
masters = [src / "EGA_FR.tex"] + [src / "ega4" / f"EGA_IV{i}_FR.tex" for i in range(1, 5)]
INPUT = re.compile(r"\\(?:input|include)\{([^}]+)\}")
MARK = re.compile(r"\\oldpage\[([^\]]*)\]\{(\d+)\}")


def follow(path, seen, base):
    if path in seen or not path.exists():
        return
    seen.append(path)
    for name in INPUT.findall(path.read_text(encoding="utf-8")):
        name = name if name.endswith(".tex") else name + ".tex"
        for cand in (base / name, path.parent / name):
            if cand.exists():
                follow(cand, seen, base)
                break


files = []
for m in masters:
    follow(m, files, src)
pages = collections.defaultdict(list)
for f in files:
    for part, n in MARK.findall(f.read_text(encoding="utf-8")):
        part = part.replace("\\textsubscript{", "_").replace("}", "")
        pages[part].append((int(n), str(f.relative_to(src))))
summary = {}
for part, lst in sorted(pages.items()):
    nums = [n for n, _ in lst]
    dup = sorted(n for n, c in collections.Counter(nums).items() if c > 1)
    summary[part] = dict(pages=len(set(nums)), first=min(nums), last=max(nums), duplicates=dup[:20],
                         gaps=sorted(set(range(min(nums), max(nums) + 1)) - set(nums))[:40],
                         files=sorted({f for _, f in lst}))
json.dump(dict(files=[str(f.relative_to(src)) for f in files], parts=summary), open(sys.argv[2], "w", encoding="utf-8"), indent=1)
for part, s in summary.items():
    print(f"{part:8s} pages {s['pages']:4d}  {s['first']}-{s['last']}  dup {len(s['duplicates'])}  gaps {len(s['gaps'])}  files {len(s['files'])}")
print("total pages", sum(s["pages"] for s in summary.values()), "| files", len(files))
