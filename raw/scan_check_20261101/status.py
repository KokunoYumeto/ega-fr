"""Progress of the EGA scan check: pages prepared and checked per run folder, findings by kind, fixes logged."""
import collections
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
tot_pages = tot_checked = 0
kinds = collections.Counter()
for run in sorted(E.glob("run_*")) + [E / "pilot", E / "pilot2"]:
    pages = {int(m.group(1)) for p in run.glob("page_*.tex") if (m := re.match(r"page_(\d+)\.tex", p.name))}
    checked = set()
    for f in run.glob("findings_*.json"):
        a, b = map(int, re.findall(r"\d+", f.stem)[:2])
        checked |= set(range(a, b + 1)) & pages
        try:
            for x in json.load(open(f, encoding="utf-8")):
                kinds[x.get("kind", "?")] += 1
        except Exception as e:
            print("unreadable", f.name, e)
    if run.name.startswith("run_"):
        tot_pages += len(pages); tot_checked += len(checked)
    print(f"{run.name:12s} pages {len(pages):4d}  checked {len(checked):4d}")
print(f"TOTAL prepared {tot_pages}, checked {tot_checked} (plus pilot pages 80-89)")
print("findings by kind:", dict(kinds.most_common()))
fl = E / "FIXLOG.jsonl"
print("fixes logged:", sum(1 for _ in open(fl, encoding="utf-8")) if fl.exists() else 0,
      "| misprints:", len(json.load(open(E / "MISPRINTS.json", encoding="utf-8"))) if (E / "MISPRINTS.json").exists() else 0)
