"""Apply the misprint-pass decisions to the corrected French EGA (editions/<release>/current).

An "apply" edit is made when "old" occurs exactly once in the page (from its \\oldpage marker to the next marker) of the
named file. Every decision is logged in MISPRINT_PASS_LOG.jsonl; applied edits also go to FIXLOG_CURRENT.jsonl
(source "misprint_pass"), so that they can be carried into the translations. Rejected edits: MISPRINT_PASS_LEFT.json.

usage: python -I apply_misprint_decisions.py DECISIONS.json [...] [--dry]"""
import collections
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
CUR = E / "ega-fr" / "editions" / "2026-10-24-r20" / "current" / "packages"
dry = "--dry" in sys.argv
paths = [pathlib.Path(a) for a in sys.argv[1:] if not a.startswith("--")]
MARK = re.compile(re.escape(BS) + r"oldpage\[([^\]]+)\]\{(\d+)\}")
mis = {}
for p in sorted(E.glob("MISPRINTS*.json")):
    for k, x in enumerate(json.loads(p.read_text(encoding="utf-8"))):
        mis[f"{p.stem}:{k}"] = x
LOG = E / "MISPRINT_PASS_LOG.jsonl"
done = set()
if LOG.exists():
    done = {json.loads(l)["id"] for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()}
texts = {}


def page_span(f, part, page):
    t = texts[f]
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if (m.group(1), int(m.group(2))) == (part, page):
            return m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(t)
    return None


stats = collections.Counter()
recs, left, rejected = [], [], []
for path in paths:
    for d in json.loads(path.read_text(encoding="utf-8")):
        mid = d["id"]
        if mid in done or mid not in mis:
            stats["skipped"] += 1
            continue
        x = mis[mid]
        part, page = x.get("part") or "I", int(x["page"])
        rec = dict(id=mid, part=part, page=page, decision=d.get("decision"), note=d.get("note"), batch=path.stem)
        if d.get("decision") == "apply":
            old = (d.get("old") or "").replace("\r\n", "\n")
            new = (d.get("new") or "").replace("\r\n", "\n")
            cands = [f for f in CUR.glob("*/native/**/*.tex") if str(f.relative_to(CUR)).replace(BS, "/") ==
                     (d.get("file") or "") or f.name == pathlib.Path(d.get("file") or "").name]
            hit = None
            for f in cands:
                if f not in texts:
                    texts[f] = f.read_text(encoding="utf-8")
                sp = page_span(f, part, page)
                if sp and old and texts[f].count(old, sp[0], sp[1]) == 1:
                    hit = (f, texts[f].find(old, sp[0], sp[1]))
            if hit is None or MARK.search(old) or MARK.search(new) or old == new:
                rec["outcome"] = "left"
                rejected.append(mid)
                left.append(dict(d, part=part, page=page))
            else:
                f, k = hit
                if not dry:
                    texts[f] = texts[f][:k] + new + texts[f][k + len(old):]
                    f.write_text(texts[f], encoding="utf-8", newline="")
                rec.update(outcome="applied", file=str(f), old=old, new=new)
        else:
            rec["outcome"] = d.get("decision")
        stats[rec["outcome"]] += 1
        recs.append(rec)
if not dry:
    with open(LOG, "a", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(E / "FIXLOG_CURRENT.jsonl", "a", encoding="utf-8") as fh:
        for r in recs:
            if r["outcome"] == "applied":
                fh.write(json.dumps(dict(file=r["file"], part=r["part"], page=r["page"], old=r["old"], new=r["new"],
                                         source="misprint_pass", why=f"misprint {r['id']}: {r.get('note') or ''}"[:300]),
                                    ensure_ascii=False) + "\n")
    prev = json.loads((E / "MISPRINT_PASS_LEFT.json").read_text(encoding="utf-8")) if (E / "MISPRINT_PASS_LEFT.json").exists() else []
    (E / "MISPRINT_PASS_LEFT.json").write_text(json.dumps(prev + left, ensure_ascii=False, indent=1), encoding="utf-8")
print(("dry run " if dry else "") + ", ".join(f"{k} {v}" for k, v in sorted(stats.items())))
if rejected:
    print("rejected ids (old not found exactly once on the page, or an edit of a marker):", rejected)
