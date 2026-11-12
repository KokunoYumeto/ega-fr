"""Page inventory of the latest diplomatic release (editions/2026-10-24-r20/diplomatic/packages/*/native):
the files each reader includes and the original pages each part covers, with absolute file paths."""
import collections
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
PK = E / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages"
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
for pkg in ["BASE", "IV1", "IV2", "IV3", "IV4"]:
    base = PK / pkg / "native"
    for m in [base / "EGA_FR.tex"] + sorted((base / "ega4").glob("EGA_IV*_FR.tex")):
        follow(m, files, base)
pages = collections.defaultdict(list)
for f in files:
    for part, n in MARK.findall(f.read_text(encoding="utf-8")):
        pages[part.replace("\\textsubscript{", "_").replace("}", "")].append((int(n), str(f)))
summary = {}
for part, lst in sorted(pages.items()):
    nums = [n for n, _ in lst]
    summary[part] = dict(pages=len(set(nums)), first=min(nums), last=max(nums),
                         duplicates=sorted(n for n, c in collections.Counter(nums).items() if c > 1)[:30],
                         files=sorted({f for _, f in lst}))
json.dump(dict(files=[str(f) for f in files], parts=summary), open(E / "page_inventory_r20.json", "w", encoding="utf-8"), indent=1)
for part, s in summary.items():
    print(f"{part:8s} pages {s['pages']:4d}  {s['first']}-{s['last']}  dup {len(s['duplicates'])}  files {len(s['files'])}")
print("total pages", sum(s["pages"] for s in summary.values()), "| files", len(files))
