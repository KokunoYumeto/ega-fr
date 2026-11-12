"""Process one finished checker batch: apply its fixes to the diplomatic edition, place the items that lie in the
text before a file's first marker (continuation of page N in the file that holds page N+1), and replay the new
transcription fixes on the corrected edition.

usage: python -I process_batch.py PART FINDINGS.json [--only=a.tex,b.tex]
Prints one summary line; leftovers stay in MANUAL_<part>_<findings stem>.json (rewritten with only the leftovers).
"""
import json
import pathlib
import re
import os
import subprocess
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
PY = sys.executable
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")
part, findings = sys.argv[1], sys.argv[2]
extra = [a for a in sys.argv[3:] if a.startswith("--only=")]
key = part.replace("\\textsubscript{", "_").replace("}", "")

r = subprocess.run([PY, "-I", str(E / "apply_fixes.py"), part, findings] + extra, capture_output=True, text=True,
                   encoding="utf-8", errors="replace", env=ENV)
line1 = (r.stdout or r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr).strip() else "apply_fixes: no output"
manual_path = E / f"MANUAL_{key}_{pathlib.Path(findings).stem}.json"
left = []
placed = 0
if manual_path.exists():
    inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"][key]["files"]
    if extra:
        only = set(extra[0][len("--only="):].split(","))
        inv = [f for f in inv if pathlib.Path(f).name in only]
    marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
    texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv}
    items = []
    for x in json.load(open(manual_path, encoding="utf-8")):
        fix = x.get("fix") or {}
        old = (fix.get("old") or "").replace("\r\n", "\n")
        page = int(x["page"])
        target = None
        for f, t in texts.items():
            pages = [int(m.group(1)) for m in marker.finditer(t)]
            if pages and pages[0] == page + 1:
                first = marker.search(t).start()
                if t[:first].count(old) == 1:
                    target = pathlib.Path(f).name
        if target:
            items.append(dict(file=target, part=part, page=page, region="before_first_marker", kind=x.get("kind"),
                              old=old, new=(fix.get("new") or "").replace("\r\n", "\n"),
                              why=(x.get("where") or "")[:200] + f" ({pathlib.Path(findings).name})"))
        else:
            left.append(x)
    if items:
        items_path = E / f"MANUAL_{key}_{pathlib.Path(findings).stem}_placed.json"
        items_path.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
        r2 = subprocess.run([PY, "-I", str(E / "apply_manual.py"), str(items_path)], capture_output=True, text=True,
                            encoding="utf-8", errors="replace", env=ENV)
        placed = sum(1 for ln in r2.stdout.splitlines() if ln.startswith("applied"))
        left += [i for i, ln in zip(items, r2.stdout.splitlines()) if not ln.startswith("applied")]
    manual_path.write_text(json.dumps(left, ensure_ascii=False, indent=1), encoding="utf-8")
logs = [str(p) for p in sorted(E.glob("FIXLOG*.jsonl")) if p.name != "FIXLOG_CURRENT.jsonl"]
r3 = subprocess.run([PY, "-I", str(E / "replay_to_current.py")] + logs, capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENV)
print(f"{pathlib.Path(findings).name}: {line1} | continuation items placed {placed} | left for hand {len(left)} | "
      f"current: {(r3.stdout or r3.stderr).strip().splitlines()[-1]}")
