"""Batches for the misprint pass of the corrected French EGA (editions/<release>/current).

The scan check recorded every misprint of the print in MISPRINTS*.json (page, where, printed reading, correct reading,
what the TeX did). The diplomatic edition keeps the printed reading; the corrected edition must give the correct one,
but it still holds whatever the TeX had before the check (the printed reading, or another slip such as v^b).
Each batch file lists the misprints of some pages with the corrected edition's text of those pages, and the
diplomatic fix that was made for it if any (OLD -> NEW).

usage: python -I make_misprint_batches.py OUTDIR [ITEMS_PER_BATCH]"""
import collections
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
CUR = E / "ega-fr" / "editions" / "2026-10-24-r20" / "current" / "packages"
out = pathlib.Path(sys.argv[1])
per = int(sys.argv[2]) if len(sys.argv) > 2 else 160
out.mkdir(parents=True, exist_ok=True)
MARK = re.compile(re.escape(BS) + r"oldpage\[([^\]]+)\]\{(\d+)\}")
mis = []
for p in sorted(E.glob("MISPRINTS*.json")):
    for k, x in enumerate(json.loads(p.read_text(encoding="utf-8"))):
        mis.append(dict(x, mid=f"{p.stem}:{k}"))
# diplomatic fixes recorded as misprints (FIXLOG.jsonl), by (part, page)
dfix = collections.defaultdict(list)
for line in open(E / "FIXLOG.jsonl", encoding="utf-8"):
    if line.strip():
        x = json.loads(line)
        if x.get("kind") == "misprint_in_print":
            dfix[(x.get("part") or "I", int(x["page"]))].append((x["old"], x["new"]))
files = sorted(CUR.glob("*/native/**/*.tex"))
segs = {}
for f in files:
    t = f.read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        segs.setdefault((m.group(1), int(m.group(2))), []).append((str(f.relative_to(CUR)).replace(BS, "/"), t[m.start():end]))
PARTS = ["0" + BS + "textsubscript{I}", "I", "II", "0" + BS + "textsubscript{III}", "III", "IV",
         "0" + BS + "textsubscript{IV-1}", "IV-1", "IV-2", "IV-3", "IV-4"]
bypage = collections.defaultdict(list)
for x in mis:
    bypage[(x.get("part") or "I", int(x["page"]))].append(x)
keys = sorted(bypage, key=lambda k: (PARTS.index(k[0]) if k[0] in PARTS else 99, k[1]))
batches, cur, n = [], [], 0
for k in keys:
    if cur and n + len(bypage[k]) > per:
        batches.append(cur)
        cur, n = [], 0
    cur.append(k)
    n += len(bypage[k])
if cur:
    batches.append(cur)
index = []
for b, ks in enumerate(batches, 1):
    name = f"misprints_{b:03d}"
    lines = [f"# Misprint pass of the corrected French EGA, {name}", ""]
    ids = []
    for part, page in ks:
        lines.append(f"=================== PAGE {part} {page} ===================")
        for fname, txt in segs.get((part, page), []):
            lines.append(f"----- corrected edition, {fname}, page {part} {page} -----")
            lines.append(txt.rstrip("\n"))
        lines.append(f"----- misprints recorded on page {part} {page} -----")
        for x in bypage[(part, page)]:
            ids.append(x["mid"])
            lines.append(f"[id {x['mid']}]")
            for key, label in (("where", "WHERE"), ("print", "PRINT"), ("correct", "CORRECT"), ("tex_did", "TEX BEFORE"),
                               ("note", "NOTE")):
                if x.get(key):
                    lines.append(f"{label}: {x[key]}")
            lines.append("")
        if dfix.get((part, page)):
            lines.append("(diplomatic edits made on this page for misprints, OLD -> NEW = the TeX before -> the printed reading:)")
            for o, nw in dfix[(part, page)]:
                lines.append("  OLD: " + o.replace("\n", "\\n") + "\n  NEW: " + nw.replace("\n", "\\n"))
            lines.append("")
    (out / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")
    index.append(dict(batch=name, items=len(ids), ids=ids, pages=[f"{p} {g}" for p, g in ks]))
(out / "BATCHES_misprints.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
sizes = [(out / f"{x['batch']}.txt").stat().st_size // 1024 for x in index]
print(len(index), "batches;", sum(x["items"] for x in index), "misprints; KB min/max/mean", min(sizes), max(sizes),
      sum(sizes) // len(sizes))
