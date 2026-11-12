"""List misprint reversions in the FIXLOGs that also carry other edits (layout, dots, inline formulas): the replay to
the corrected edition skips misprint reversions whole, so their other changes are missing there.
usage: python -I find_combined_misprints.py"""
import difflib
import glob
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
n, flagged = 0, []
for fn in sorted(glob.glob(str(E / "FIXLOG*.jsonl"))):
    if "CURRENT" in fn:
        continue
    for ln in open(fn, encoding="utf-8"):
        if not ln.strip():
            continue
        x = json.loads(ln)
        why = (x.get("why") or "") + " " + (x.get("kind") or "")
        if not (x.get("kind") == "misprint_in_print" or re.search(r"misprint|silent", why, re.I)):
            continue
        n += 1
        o, w = x["old"], x["new"]
        ops = [op for op in difflib.SequenceMatcher(None, o, w, autojunk=False).get_opcodes() if op[0] != "equal"]
        changed = sum(max(i2 - i1, j2 - j1) for _, i1, i2, j1, j2 in ops)
        if len(ops) > 2 or changed > 12 or ("\\[" in o) != ("\\[" in w) or ("\\cdots" in o) != ("\\cdots" in w):
            flagged.append((pathlib.Path(fn).name, x.get("part"), x.get("page"), len(ops), changed, o[:80], w[:80]))
print("misprint entries", n, "flagged", len(flagged))
for f in flagged:
    print(f)
