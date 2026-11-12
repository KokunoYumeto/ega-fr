"""Turn the leftovers of a MANUAL_<part>_<stem>.json into apply_manual.py items for one file and region, apply them,
and clear the leftovers that were applied.
usage: python -I resolve_manual.py MANUAL.json PART FILE REGION
REGION: before_first_marker | file | page"""
import json
import os
import pathlib
import subprocess
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # -I ignores PYTHONIOENCODING
manual, part, fname, region = sys.argv[1:5]
left = json.load(open(manual, encoding="utf-8"))
items = [dict(file=fname, part=part, page=int(x["page"]), region=region, kind=x.get("kind"),
              old=x["fix"]["old"].replace("\r\n", "\n"), new=(x["fix"].get("new") or "").replace("\r\n", "\n"),
              why=(x.get("where") or "")[:200] + " (" + pathlib.Path(manual).name + ")") for x in left]
out = pathlib.Path(manual).with_name(pathlib.Path(manual).stem + "_resolved.json")
out.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
r = subprocess.run([sys.executable, "-I", str(E / "apply_manual.py"), str(out)], capture_output=True, text=True,
                   encoding="utf-8", errors="replace", env=dict(os.environ, PYTHONIOENCODING="utf-8"))
print(r.stdout.strip() or r.stderr.strip())
done = [ln.startswith("applied") for ln in r.stdout.splitlines()]
rest = [x for x, ok in zip(left, done) if not ok] + left[len(done):]
pathlib.Path(manual).write_text(json.dumps(rest, ensure_ascii=False, indent=1), encoding="utf-8")
print("left", len(rest))
