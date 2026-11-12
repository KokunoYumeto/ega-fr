"""Resolve the replay leftovers of 4 Nov 2026 (REPLAY_CURRENT_MANUAL.json, EGA IV-4 pp. 121-199) by hand on the
corrected edition, as resolve_replay_left_20261102b.py did for the earlier set.

"adapt" applies the same typographic fix to the corrected wording (old2 -> new2, unique in the page); "skip" when the
corrected edition rewrote the passage, already has the printed reading, or the fix was already placed by hand. Both
the adapted edit and the original entry (so that replay_to_current.py does not list it again) are logged to
FIXLOG_CURRENT.jsonl.
usage: python -I resolve_replay_left_20261104.py [--dry]"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
dry = "--dry" in sys.argv
REWRITE_19_4_6 = ("the corrected edition rewrote the proof of (19.4.6) (i) as a mathematical correction (a) and b) "
                  "imply c); the converse when X is flat over S); this sentence is not there")
D = {  # (file name, page, start of the original old) -> decision
    ("ega4-18-fr.tex", 121, "on peut appliquer (18.4.6, (ii));"):
        ("skip", "the corrected edition already reads (18.4.6, (i))"),
    ("ega4-18-fr.tex", 122, "surjectif par (18.4.6, (ii))"):
        ("skip", "the corrected edition already reads (18.4.6, (i))"),
    ("ega4-18-fr.tex", 170, "donc (18.11.1) est un"):
        ("skip", "placed by hand on 4 Nov (current_items_170_191.json): the print's wording restored with the upright "
                 "reference"),
    ("ega4-18-fr.tex", 191, "d'appliquer ($0$, 15.1.6)"):
        ("skip", "placed by hand on 4 Nov (current_items_170_191.json): bold 0 applied; the corrected edition's "
                 "reference 15.1.16 kept"),
    ("ega4-18-fr.tex", 199, "\\end{enumerate}\n  Lorsqu'il"):
        ("adapt", "\\end{enumerate}\n  Lorsque la condition $a)$, ou",
         "\\end{enumerate}\n\n  Lorsque la condition $a)$, ou"),
    ("ega4-18-fr.tex", 199, "l'équivalence de $b)$ et $c)$,"):
        ("skip", REWRITE_19_4_6),
    ("ega4-18-fr.tex", 199, "la condition $c)$ implique"):
        ("skip", REWRITE_19_4_6),
}
items = json.loads((E / "REPLAY_CURRENT_MANUAL.json").read_text(encoding="utf-8"))
log = None if dry else open(E / "FIXLOG_CURRENT.jsonl", "a", encoding="utf-8")
used = set()
for x in items:
    cur = pathlib.Path(x["current_file"])
    keys = [k for k in D if k[0] == cur.name and k[1] == int(x["page"]) and x["old"].startswith(k[2])]
    if len(keys) != 1:
        print("NO DECISION", cur.name, x["page"], repr(x["old"][:60]))
        continue
    used.add(keys[0])
    dec = D[keys[0]]
    if dec[0] == "adapt":
        t = cur.read_text(encoding="utf-8")
        part = x.get("part") or "I"
        cuts = [(int(m.group(1)), m.start()) for m in
                re.finditer(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}", t)]
        i = [k for k, (n, s) in enumerate(cuts) if n == int(x["page"])][0]
        s, e = cuts[i][1], (cuts[i + 1][1] if i + 1 < len(cuts) else len(t))
        n = t[s:e].count(dec[1])
        if n != 1:
            print(f"SKIP-ADAPT {cur.name} p.{x['page']}: adapted old occurs {n} times: {dec[1][:60]!r}")
            continue
        t = t[:s] + t[s:e].replace(dec[1], dec[2]) + t[e:]
        if not dry:
            cur.write_text(t, encoding="utf-8", newline="")
            log.write(json.dumps(dict(file=str(cur), part=part, page=int(x["page"]), old=dec[1], new=dec[2],
                                      source="hand_adapted_20261104"), ensure_ascii=False) + "\n")
    if not dry:
        log.write(json.dumps(dict(file=str(cur), part=x.get("part"), page=int(x["page"]), old=x["old"], new=x["new"],
                                  source="hand_resolved_20261104", decision=dec[0],
                                  why=dec[1] if dec[0] == "skip" else "adapted to the corrected wording"),
                             ensure_ascii=False) + "\n")
    print(("would " if dry else "") + dec[0], cur.name, x["page"])
print("unused decisions:", [k for k in D if k not in used])
