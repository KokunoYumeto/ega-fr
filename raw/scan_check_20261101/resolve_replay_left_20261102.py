"""Resolve the replay leftovers of 2 Nov 2026 (REPLAY_CURRENT_MANUAL.json) by hand on the corrected edition.

Each leftover is a diplomatic fix whose "old" no longer occurs in the corrected edition because that edition corrects
the text there. Decisions: "adapt" applies the same typographic fix to the corrected wording (old2 -> new2, unique in
the page); "skip" when the corrected edition rewrote the passage so the fix has no counterpart. Both the adapted edit
and the original entry (so that replay_to_current.py does not list it again) are logged to FIXLOG_CURRENT.jsonl.
usage: python -I resolve_replay_left_20261102.py [--dry]"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
dry = "--dry" in sys.argv
D = {  # (file name, page, start of the original old) -> decision
    ("ega1-3-fr.tex", 114, r"un $k(s)$-monomorphisme"):
        ("adapt", r"donc un $k(s)$-homomorphisme", r"donc un $\boldsymbol{k}(s)$-homomorphisme"),
    ("ega1-7-fr.tex", 163, r"surjection sur l'ensemble"):
        ("skip", "the corrected edition restates (7.3.8) for a dominant morphism of integral preschemes; no 'surjection'"),
    ("ega1-9-fr.tex", 175, r"{0, 3.3.1}) r"):
        ("skip", "the corrected edition rewrote this step of the proof; the reference (0, 3.3.1) is not there"),
    ("ega2-1-fr.tex", 75, r"[III.2.1.14-fr]{III,"):
        ("adapt", r"[III.2.1.15-fr]{III,", r"[III.2.1.15-fr]{\textbf{III},"),
    ("ega2-1-fr.tex", 80, "Module coh\u00e9rent de type\n  fini"):
        ("adapt", "Module quasi-coh\u00e9rent de type\n  fini $\\mathcal{E}$ de",
         "Module quasi-coh\u00e9rent \\textup{de type\n  fini} $\\mathcal{E}$ de"),
    ("ega2-1-fr.tex", 130, r"(\hyperref[II.6.5.5.1-fr]{6.5.5.1})"):
        ("adapt", r"(\hyperref[II.6.5.5.3-fr]{6.5.5.3})", r"\textup{(\hyperref[II.6.5.5.3-fr]{6.5.5.3})}"),
    ("ega2-1-fr.tex", 150, r"{I, 9.5.11}"):
        ("skip", "already bold in the corrected edition"),
    ("ega2-errata-addenda-fr.tex", 221, r"canonique (1.8.8.1) soit"):
        ("adapt", r"canonique (1.8.9.1) soit", r"canonique \textup{(1.8.9.1)} soit"),
    ("ega3-1-fr.tex", 35, r"existent dans $\mathcal C$ et"):
        ("adapt", r"existent dans $\mathcal C''$.", r"existent dans $\boldsymbol{C}''$."),
    ("ega3-1-fr.tex", 60, "\\[\n\\operatorname{Ext}"):
        ("adapt", "\\[\n\\mathcal{E}xt_{\\mathcal O_X|U}^p(\\mathcal L|U,\\mathcal G|U)=0\n\\]",
         "$\\mathcal{E}xt_{\\mathcal O_X|U}^p(\\mathcal L|U,\\mathcal G|U)=0$"),
    ("ega3-1-fr.tex", 45, "et de ce que les\n\\[\nH^q"):
        ("adapt", "et de ce que les\n\\[\nH_q(\\mathrm C_\\bullet(|\\sigma|)\\otimes\\mathrm C_\\bullet(|\\tau|))\n"
                  "\\quad\\text{et}\\quad\nH_q(\\mathrm P_\\bullet(|\\sigma|,|\\tau|))\n\\]\n",
         "et de ce que les\n$H_q(\\mathrm C_\\bullet(|\\sigma|)\\otimes\\mathrm C_\\bullet(|\\tau|))$ et\n"
         "$H_q(\\mathrm P_\\bullet(|\\sigma|,|\\tau|))$\n"),
    ("ega3-1-fr.tex", 43, "rang\u00e9s dans l'ordre croissant dans"):
        ("adapt", "rang\u00e9s dans l'ordre croissant. Il est clair", "rang\u00e9s \\emph{dans l'ordre croissant}. Il est clair"),
    ("ega3-1-fr.tex", 43, "\\[\nd(\\sigma,\\tau)"):
        ("adapt", "\\[\nd(\\sigma,\\tau)=(d'\\sigma,\\tau)+(-1)^{h+1}(\\sigma,d''\\tau)\n\\quad\\text{si }\\deg\\sigma=h.\n\\]\n"
                  "Les homomorphismes naturels",
         "$d(\\sigma,\\tau)=(d'\\sigma,\\tau)+(-1)^{h+1}(\\sigma,d''\\tau)$ si $\\deg\\sigma=h$.\n\nLes homomorphismes naturels"),
    ("ega3-1-fr.tex", 95, "V\u00e9rifions maintenant d~2)"):
        ("adapt", "V\u00e9rifions maintenant d~1)", "V\u00e9rifions maintenant \\textit{d}\\,1)"),
    ("ega3-1-fr.tex", 99, r"\bigl(S_{\mathcal O_Y}(\mathcal E)\bigr)_{-n}"):
        ("adapt", r"\bigl(S_{\mathcal O_Y}(\mathcal E)\bigr)_{-n-r-1}", r"\bigl(\mathbf S_{\mathcal O_Y}(\mathcal E)\bigr)_{-n-r-1}"),
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
                                      source="hand_adapted_20261102"), ensure_ascii=False) + "\n")
    if not dry:
        log.write(json.dumps(dict(file=str(cur), part=x.get("part"), page=int(x["page"]), old=x["old"], new=x["new"],
                                  source="hand_resolved_20261102", decision=dec[0],
                                  why=dec[1] if dec[0] == "skip" else "adapted to the corrected wording"),
                             ensure_ascii=False) + "\n")
    print(("would " if dry else "") + dec[0], cur.name, x["page"])
print("unused decisions:", [k for k in D if k not in used])
