"""Replay the diplomatic edition's transcription fixes on the corrected edition (editions/<release>/current).

Transcription errors, conventions and page markers are common to both editions; the reversions to a printed misprint
are not (the corrected edition keeps the correct reading) and are skipped. An entry is applied when its "old" occurs
exactly once in the same page of the corresponding current file (or, for text before a file's first marker, in that
opening text); everything else is listed in REPLAY_CURRENT_MANUAL.json. Applied entries go to FIXLOG_CURRENT.jsonl.
usage: python -I replay_to_current.py FIXLOG.jsonl [FIXLOG_...jsonl ...] [--dry]
"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
dry = "--dry" in sys.argv
logs = [a for a in sys.argv[1:] if a != "--dry"]
done_path = E / "FIXLOG_CURRENT.jsonl"
done = set()
if done_path.exists():
    for line in done_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            d = json.loads(line)
            done.add((d["file"], d["page"], d["old"], d["new"]))
out = None if dry else open(done_path, "a", encoding="utf-8")
manual, applied, skipped = [], 0, 0


def is_misprint_reversion(x):
    why = (x.get("why") or "") + " " + (x.get("kind") or "")
    return x.get("kind") == "misprint_in_print" or re.search(r"misprint|silent", why, re.I) is not None


for log in logs:
    for line in open(log, encoding="utf-8"):
        if not line.strip():
            continue
        x = json.loads(line)
        src = x["file"].replace("\\", "/")
        if not pathlib.Path(src).is_absolute():
            src = str(E / src).replace("\\", "/")  # logs written with paths relative to the work folder
        if src.endswith("source/ega1/ega1-1-fr.tex") and "/editions/" not in src:
            # pp. 80-89 were logged against the root copy, then replayed on the identical release file
            src = str(E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega1/ega1-1-fr.tex").replace("\\", "/")
        if "/diplomatic/" not in src:
            skipped += 1
            continue
        if is_misprint_reversion(x):
            skipped += 1
            continue
        cur = pathlib.Path(src.replace("/diplomatic/", "/current/"))
        key = (str(cur), int(x["page"]), x["old"], x["new"])
        if key in done:
            continue
        if not cur.exists():
            manual.append(dict(x, why_manual="no corresponding current file"))
            continue
        t = cur.read_text(encoding="utf-8")
        part = x.get("part") or "I"
        marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        idx = [i for i, (n, s) in enumerate(cuts) if n == int(x["page"])]
        regions = []
        if idx:
            i = idx[0]
            j = i + 1
            while j < len(cuts) and cuts[j][0] == int(x["page"]):  # moved marker: old copy not yet removed
                j += 1
            regions.append((cuts[i][1], cuts[j][1] if j < len(cuts) else len(t)))
        if cuts:
            regions.append((0, cuts[0][1]))  # opening text continuing the previous page
        regions.append((0, len(t)))
        for s, e in regions:
            if t[s:e].count(x["old"]) == 1 and (s, e) != (0, len(t)) or ((s, e) == (0, len(t)) and t.count(x["old"]) == 1):
                t = t[:s] + t[s:e].replace(x["old"], x["new"]) + t[e:]
                if not dry:
                    cur.write_text(t, encoding="utf-8", newline="")
                    out.write(json.dumps(dict(file=str(cur), part=part, page=int(x["page"]), old=x["old"], new=x["new"],
                                              source=pathlib.Path(log).name), ensure_ascii=False) + "\n")
                applied += 1
                break
        else:
            n_page = t[regions[0][0]:regions[0][1]].count(x["old"]) if idx else None
            manual.append(dict(x, current_file=str(cur), why_manual=f"old occurs {n_page} times on the page, "
                                                                    f"{t.count(x['old'])} times in the file"))
if not dry:
    (E / "REPLAY_CURRENT_MANUAL.json").write_text(json.dumps(manual, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"applied {applied}, manual {len(manual)}, skipped {skipped} (misprint reversions and root copies)"
      + (" (dry run)" if dry else ""))
