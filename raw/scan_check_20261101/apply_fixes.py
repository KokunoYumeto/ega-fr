"""Apply checker findings (with exact "fix": {"old","new"}) to the diplomatic release sources, page by page.

An edit is applied only if "old" occurs exactly once inside its page (from \\oldpage[PART]{N} to the next marker);
everything else goes to the manual list. Misprints are added to MISPRINTS.json with their corrected reading.
Every change is appended to FIXLOG.jsonl.
usage: python apply_fixes.py PART FINDINGS.json [FINDINGS.json ...] [--dry]"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
only = None  # --only=name1.tex,name2.tex: search only these release files (EGA III parts 1 and 2 share pages 137-167)
for a in sys.argv[1:]:
    if a.startswith("--only="):
        only = set(a[len("--only="):].split(","))
args = [a for a in sys.argv[1:] if a != "--dry" and not a.startswith("--only=")]
dry = "--dry" in sys.argv
part, files = args[0], args[1:]
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
key = part.replace("\\textsubscript{", "_").replace("}", "")
if only:
    inv[key]["files"] = [f for f in inv[key]["files"] if pathlib.Path(f).name in only]
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")


def locate(page):
    for f in inv[key]["files"]:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                j = i + 1
                while j < len(cuts) and cuts[j][0] == page:  # a marker moved earlier leaves the old one until removed
                    j += 1
                return pathlib.Path(f), s, cuts[j][1] if j < len(cuts) else len(t)
    for f in inv[key]["files"]:  # marker removed before its new copy is inserted: use the gap around the page
        t = pathlib.Path(f).read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
            if a < page < b:
                return pathlib.Path(f), sa, sb
    return None, None, None


mis_path = E / "MISPRINTS.json"
misprints = json.load(open(mis_path, encoding="utf-8")) if mis_path.exists() else []
log = open(E / "FIXLOG.jsonl", "a", encoding="utf-8") if not dry else None
applied = manual = 0
manual_items = []
for fn in files:
    src = pathlib.Path(fn)
    for x in json.load(open(src, encoding="utf-8")):
        page = int(x["page"])
        if x.get("kind") == "misprint_in_print":
            misprints.append(dict(part=part, page=page, where=x.get("where"), print=x.get("scan"),
                                  correct=x.get("corrected"), tex_did=x.get("tex"), note=x.get("note"), source=src.name))
        fix = x.get("fix")
        if not fix or not fix.get("old") or fix.get("old") == fix.get("new"):
            continue
        # page_NNN.tex copies use CRLF, the release files LF (read_text gives LF): normalise the edit strings
        fix = dict(fix, old=fix["old"].replace("\r\n", "\n"), new=(fix.get("new") or "").replace("\r\n", "\n"))
        path, s, e = locate(page)
        if path is None:
            manual += 1; manual_items.append(dict(x, why="page not found")); continue
        t = path.read_text(encoding="utf-8")
        seg = t[s:e]
        if seg.count(fix["old"]) != 1:
            manual += 1; manual_items.append(dict(x, why=f"old occurs {seg.count(fix['old'])} times on the page")); continue
        new_t = t[:s] + seg.replace(fix["old"], fix["new"]) + t[e:]
        if not dry:
            path.write_text(new_t, encoding="utf-8", newline="")
            log.write(json.dumps(dict(file=str(path), part=part, page=page, old=fix["old"], new=fix["new"],
                                      kind=x.get("kind"), convention=x.get("convention"), source=src.name),
                                 ensure_ascii=False) + "\n")
        applied += 1
if not dry:
    json.dump(misprints, open(mis_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(manual_items, open(E / f"MANUAL_{key}_{pathlib.Path(files[0]).stem}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"applied {applied}, manual {manual}, misprints now {len(misprints)}" + (" (dry run)" if dry else ""))
