"""Apply RECHECK_DECISIONS.json (the candidate misprints of FRENCH_RECHECK.md, decided against the scans and the
mathematics, 5 Nov): for each "misprint", apply its edits (corrected French, English, Spanish corrected edition; each
"old" must occur exactly once), log them (FIXLOG_CURRENT.jsonl for the French, PORT_EN_LOG_RECHECK.jsonl,
PORT_ES_CURRENT_LOG.jsonl), and record the misprint in MISPRINTS.json. The decision reversing the earlier (21.2.2)
correction also updates that MISPRINTS entry. Diplomatic editions are not touched (they keep the print).
usage: python -I apply_recheck_decisions.py [--apply]"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(__file__).parent
apply = "--apply" in sys.argv
dec = json.loads((E / "RECHECK_DECISIONS.json").read_text(encoding="utf-8"))
mis = json.loads((E / "MISPRINTS.json").read_text(encoding="utf-8"))
ok = bad = 0
for x in dec:
    edits = x.get("edits") or []
    print(f"{x.get('decision'):13} {x.get('part')} p.{x.get('page')} | {x.get('candidate', '')[:60]} | edits {len(edits)}")
    if x.get("decision") != "misprint":
        continue
    plan = []
    for e in edits:
        f = pathlib.Path(e["file"])
        t = f.read_text(encoding="utf-8") if f.exists() else ""
        n = t.count(e["old"])
        flag = "ok" if n == 1 else f"FOUND {n}x"
        print(f"      {flag:9} {f.name}: {e['old'][:70]!r} -> {e['new'][:70]!r}")
        if n == 1:
            plan.append((f, e))
        else:
            bad += 1
    if not apply:
        continue
    for f, e in plan:
        t = f.read_text(encoding="utf-8")
        if t.count(e["old"]) != 1:
            print("      changed meanwhile, skipped:", f)
            continue
        f.write_text(t.replace(e["old"], e["new"]), encoding="utf-8", newline="")
        s = str(f)
        log = ("FIXLOG_CURRENT.jsonl" if "ega-fr" in s else "PORT_ES_CURRENT_LOG.jsonl" if "ega-fga-es" in s
               else "PORT_EN_LOG_RECHECK.jsonl")
        with open(E / log, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"file": s, "part": x.get("part"), "page": x.get("page"), "old": e["old"],
                                 "new": e["new"], "source": "recheck_decisions", "why": x.get("argument", "")[:500]},
                                ensure_ascii=False) + "\n")
        ok += 1
    # the misprint record: update an existing entry for the same place, else add one
    prev = [m for m in mis if m.get("part") == x.get("part") and m.get("page") == x.get("page")
            and x.get("print") and m.get("print") and m["print"][:20] == str(x["print"])[:20]]
    if prev:
        prev[0]["correct"] = x.get("correct")
        prev[0]["note"] = (prev[0].get("note", "") + " Revised 5 Nov (RECHECK_DECISIONS): " + x.get("argument", ""))[:1500]
    else:
        mis.append({"part": x.get("part"), "page": x.get("page"), "where": x.get("candidate"), "print": x.get("print"),
                    "correct": x.get("correct"), "tex_did": "the printed reading (both editions)",
                    "note": x.get("argument", ""), "source": "RECHECK_DECISIONS.json"})
if apply:
    (E / "MISPRINTS.json").write_text(json.dumps(mis, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"edits applied {ok}, edits not unique {bad}; MISPRINTS {len(mis)}", "" if apply else "(dry run)")
