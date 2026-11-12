"""Resolve the replay leftovers of findings_215_219 (EGA IV-4 pp. 216-219) by hand on the corrected edition.

p. 216: the corrected edition replaces the print's last step of the proof of (19.7.1.16) by a corrected argument
(Koszul relations, with a correction note). That text was built on the old TeX and still writes the ideal K as
\\mathfrak R, the print's baseline dots as \\cdots and the bold 0 as $0$. The same typographic fixes are applied to the
corrected wording: every \\mathfrak R on the page (9, all the ideal K, as in the statement), the 2 \\cdots, the one ($0$, .
All nine p. 216 leftovers are resolved by these page edits.
p. 218: the corrected edition already has (\\textbf{0}, 15.1.7).
p. 219: the corrected edition has gr(O_{X,z}) where the print has gr(F_z) (the regularity that (19.7.1) needs is over
the ring); the raised bullet is applied to its wording.
Both the adapted edits and the original entries are logged to FIXLOG_CURRENT.jsonl, so that replay_to_current.py does
not list them again.
usage: python -I resolve_replay_left_20261104b.py [--dry]"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
dry = "--dry" in sys.argv
BS = chr(92)
CUR = E / "ega-fr/editions/2026-10-24-r20/current/packages/IV4/native/ega4/ega4-18-fr.tex"
# page -> list of (old, new, expected count on the page)
PAGE_EDITS = {
    216: [(BS + "mathfrak R", BS + "mathfrak K", 9),
          ("a_1f_1+" + BS + "cdots+a_nf_n", "a_1f_1+" + BS + "ldots+a_nf_n", 2),
          ("($0$, 15.1.7 et 15.1.9)", "(" + BS + "textbf{0}, 15.1.7 et 15.1.9)", 1)],
    219: [(BS + "operatorname{gr}_{" + BS + "sh K_z}^*(" + BS + "sh O_{X,z})$-r\u00e9guli\u00e8re en tout point",
           BS + "operatorname{gr}_{" + BS + "sh K_z}^" + BS + "bullet(" + BS + "sh O_{X,z})$-r\u00e9guli\u00e8re en tout point", 1)],
}
WHY = {216: "the corrected edition rewrote the end of the proof of (19.7.1.16); the fix is applied to its wording by the "
            "page edits of resolve_replay_left_20261104b.py",
       218: "the corrected edition already reads (\\textbf{0}, 15.1.7)",
       219: "the corrected edition reads gr(O_{X,z}) here; raised bullet applied to its wording"}
DECISION = {216: "adapt", 218: "skip", 219: "adapt"}

t = CUR.read_text(encoding="utf-8")
log = None if dry else open(E / "FIXLOG_CURRENT.jsonl", "a", encoding="utf-8")


def page_span(text, n):
    cuts = [(int(m.group(1)), m.start()) for m in re.finditer(re.escape(BS + "oldpage[IV-4]{") + r"(\d+)\}", text)]
    i = [k for k, (p, s) in enumerate(cuts) if p == n][0]
    return cuts[i][1], (cuts[i + 1][1] if i + 1 < len(cuts) else len(text))


for page, edits in PAGE_EDITS.items():
    for old, new, n in edits:
        s, e = page_span(t, page)
        c = t[s:e].count(old)
        assert c == n, (page, old, c, n)
        t = t[:s] + t[s:e].replace(old, new) + t[e:]
        print(("would " if dry else "") + "p.%d: %d x %r -> %r" % (page, n, old[:50], new[:50]))
        if not dry:
            log.write(json.dumps(dict(file=str(CUR), part="IV-4", page=page, old=old, new=new, count=n,
                                      source="hand_adapted_20261104b"), ensure_ascii=False) + "\n")
items = json.loads((E / "REPLAY_CURRENT_MANUAL.json").read_text(encoding="utf-8"))
assert len(items) == 11 and {int(x["page"]) for x in items} == {216, 218, 219}, [x["page"] for x in items]
if not dry:
    CUR.write_text(t, encoding="utf-8", newline="")
    for x in items:
        p = int(x["page"])
        log.write(json.dumps(dict(file=x["current_file"], part=x.get("part"), page=p, old=x["old"], new=x["new"],
                                  source="hand_resolved_20261104b", decision=DECISION[p], why=WHY[p]),
                             ensure_ascii=False) + "\n")
print(("would resolve " if dry else "resolved ") + "%d leftovers" % len(items))
