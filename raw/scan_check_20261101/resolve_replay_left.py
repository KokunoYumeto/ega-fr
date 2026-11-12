"""Resolve replay leftovers (REPLAY_CURRENT_MANUAL.json) by hand on the corrected edition, from a decisions file.

Same rules as resolve_replay_left_20261102b.py: "adapt" applies the same typographic fix to the corrected wording
(old2 -> new2, unique in the page); "skip" when the corrected edition rewrote the passage or already has the printed
reading. Both the adapted edit and the original entry are logged to FIXLOG_CURRENT.jsonl.
DECISIONS.json: a list of {"file": "<file name>", "page": N, "old_start": "<start of the original old>",
"decision": "adapt"|"skip", "old2": ..., "new2": ... (adapt) | "why": ... (skip)}.
usage: python -I resolve_replay_left.py DECISIONS.json [--dry]"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
dry = "--dry" in sys.argv
decisions = json.loads(pathlib.Path([a for a in sys.argv[1:] if a != "--dry"][0]).read_text(encoding="utf-8"))
tag = "hand_" + pathlib.Path([a for a in sys.argv[1:] if a != "--dry"][0]).stem
items = json.loads((E / "REPLAY_CURRENT_MANUAL.json").read_text(encoding="utf-8"))
log = None if dry else open(E / "FIXLOG_CURRENT.jsonl", "a", encoding="utf-8")
used = set()
for x in items:
    cur = pathlib.Path(x["current_file"])
    keys = [i for i, d in enumerate(decisions) if d["file"] == cur.name and int(d["page"]) == int(x["page"])
            and x["old"].startswith(d["old_start"])]
    if len(keys) != 1:
        print("NO DECISION", cur.name, x["page"], repr(x["old"][:60]))
        continue
    used.add(keys[0])
    dec = decisions[keys[0]]
    if dec["decision"] == "adapt":
        t = cur.read_text(encoding="utf-8")
        part = x.get("part") or "I"
        cuts = [(int(m.group(1)), m.start()) for m in
                re.finditer(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}", t)]
        i = [k for k, (n, s) in enumerate(cuts) if n == int(x["page"])][0]
        s, e = cuts[i][1], (cuts[i + 1][1] if i + 1 < len(cuts) else len(t))
        n = t[s:e].count(dec["old2"])
        if n != 1:
            print(f"SKIP-ADAPT {cur.name} p.{x['page']}: adapted old occurs {n} times: {dec['old2'][:60]!r}")
            continue
        t = t[:s] + t[s:e].replace(dec["old2"], dec["new2"]) + t[e:]
        if not dry:
            cur.write_text(t, encoding="utf-8", newline="")
            log.write(json.dumps(dict(file=str(cur), part=part, page=int(x["page"]), old=dec["old2"], new=dec["new2"],
                                      source=tag), ensure_ascii=False) + "\n")
    if not dry:
        log.write(json.dumps(dict(file=str(cur), part=x.get("part"), page=int(x["page"]), old=x["old"], new=x["new"],
                                  source=tag, decision=dec["decision"],
                                  why=dec.get("why") or "adapted to the corrected wording"), ensure_ascii=False) + "\n")
    print(("would " if dry else "") + dec["decision"], cur.name, x["page"])
print("unused decisions:", [i for i in range(len(decisions)) if i not in used])
