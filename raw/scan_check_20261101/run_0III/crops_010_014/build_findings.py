"""Build and validate findings for EGA III ch. 0, pages 10-14 (run_0III).

Manual findings are listed below; the bold italic category letter C is
generated occurrence by occurrence (minimal unique context per page).
Every fix's "old" is checked to occur exactly once in its page (CRLF -> LF),
fix spans on a page must not overlap, and all fixes are applied in sequence
to confirm they stay applicable.
"""
import json
import re
import sys
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0III")
OUTFILE = RUN / "findings_010_014.json"

def page_text(p):
    return (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")

TEXT = {p: page_text(p) for p in range(10, 15)}

def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

LEADSTO_NOTE = ("The print has the wavy maps-to arrow (squiggly arrow, as \\leadsto, which "
                "ega3-1-fr.tex already uses elsewhere); the TeX has \\mapsto. Not convention 3 "
                "(the printed arrow is not plain). Checked on an enlarged crop.")
E_NOTE = ("The final object e of (8.2.7) is printed bold italic (enlarged crop); the TeX has a plain "
          "italic e. e_X (the neutral element) is plain italic in the print and stays as it is.")

manual = [
    # ---------------- page 10 ----------------
    F(10, "(8.2.2), 1st line: 'loi de composition interne γ_{X''} et w' : X'→X''...'",
      "interne γ_{X''} et w' : X'→X''  (no comma)",
      "interne $\\gamma_{X''}$, et", "punctuation", None, "high",
      "interne $\\gamma_{X''}$, et", "interne $\\gamma_{X''}$ et",
      "Enlarged crop: no comma after γ_{X''}; the TeX adds one."),
    F(10, "(8.2.2): 'est appelé isomorphisme pour les lois de composition γ_X et γ_{X'}'",
      "isomorphisme pour les lois de composition in italics; 'et' between γ_X and γ_{X'} roman",
      "\\emph{isomorphisme pour les lois de composition $\\gamma_X$ et $\\gamma_{X'}$} ('et' italic)",
      "italics", None, "high",
      "\\emph{isomorphisme pour les lois de composition $\\gamma_X$ et\n$\\gamma_{X'}$}",
      "\\emph{isomorphisme pour les lois de composition} $\\gamma_X$ et\n$\\gamma_{X'}$",
      "Enlarged crop: the italic stops after 'composition'; 'et' is upright."),
    F(10, "(8.2.3): 'que γ_X(Y) soit une loi de groupe sur h_X(Y)'",
      "loi de *groupe* (only 'groupe' italic)",
      "\\emph{loi de groupe}", "italics", None, "high",
      "\\emph{loi de groupe}", "loi de \\emph{groupe}",
      "Enlarged crop: 'loi de' is roman."),
    F(10, "(8.2.4): 'lorsque C est la catégorie Ens'",
      "Ens in bold italic (like the category letter C)",
      "$\\mathrm{Ens}$ (roman)", "font", None, "high",
      "catégorie $\\mathrm{Ens}$", "catégorie \\textbf{\\textit{Ens}}",
      "Enlarged view: category name printed bold italic, like C. ega3-1-fr.tex writes \\mathrm{Ens} 23 times (other pages not checked here)."),
    F(10, "(8.2.5): 'la loi interne γ_X(Y) est associative, ou que le diagramme'",
      "associative (roman)",
      "\\emph{associative}", "italics", None, "high",
      "\\emph{associative}", "associative",
      "Enlarged crop: 'associative' is upright; the TeX adds emphasis."),
    # ---------------- page 11 ----------------
    F(11, "(8.2.6), 2nd line: 'la loi interne γ_X(Y) est une loi de groupe'",
      "loi de *groupe* (only 'groupe' italic)",
      "\\emph{loi de groupe}", "italics", None, "high",
      "\\emph{loi de\ngroupe}", "loi de\n\\emph{groupe}",
      "Enlarged crop: 'loi de' is roman (same as (8.2.3) on p. 10)."),
    F(11, "(8.2.6): 'les propriétés caractéristiques de l'inverse s⇝s^{-1}'",
      "s ⇝ s^{-1} (wavy arrow)", "$s\\mapsto s^{-1}$", "symbol", None, "high",
      "$s\\mapsto s^{-1}$", "$s\\leadsto s^{-1}$", LEADSTO_NOTE),
    F(11, "(8.2.6): 'il suffit d'écrire que les deux applications composées'",
      "'que' set in bold roman (wrong font)",
      "que (roman)", "misprint_in_print", None, "high",
      "d'écrire que les deux", "d'écrire \\textbf{que} les deux",
      "Wrong-font slip in the print (3x crop: q, u, e clearly heavier than the surrounding roman). "
      "The TeX silently corrects it; the fix restores the printed bold word.",
      corrected="d'écrire que les deux"),
    F(11, "(8.2.6), first displayed line '(s,t)⇝(s,s^{-1},t)⇝(s,s^{-1}t)⇝s(s^{-1}t)'",
      "three wavy arrows ⇝", "three \\mapsto", "symbol", None, "high",
      "(s,t)\\mapsto(s,s^{-1},t)\\mapsto(s,s^{-1}t)\\mapsto s",
      "(s,t)\\leadsto(s,s^{-1},t)\\leadsto(s,s^{-1}t)\\leadsto s", LEADSTO_NOTE),
    F(11, "(8.2.6), end of the first displayed line '... s(s^{-1}t)'",
      "s(s^{-1}t) with no punctuation (2.5x crop)", "s(s^{-1}t),", "punctuation", None, "high",
      "^{-1}t),\n", "^{-1}t)\n",
      "The print ends both displayed lines without punctuation; the TeX adds a comma after the first. "
      "Does not overlap the arrow fix on the same line."),
    F(11, "(8.2.6), second displayed line '(s,t)⇝(s,s^{-1},t)⇝(s,ts^{-1})⇝(ts^{-1})s'",
      "three wavy arrows ⇝", "three \\mapsto", "symbol", None, "high",
      "(s,t)\\mapsto(s,s^{-1},t)\\mapsto(s,ts^{-1})\\mapsto(ts^{-1})s",
      "(s,t)\\leadsto(s,s^{-1},t)\\leadsto(s,ts^{-1})\\leadsto(ts^{-1})s", LEADSTO_NOTE),
    F(11, "(8.2.6): 'sont égales à la seconde projection (s,t)⇝t de G×G dans G'",
      "(s, t) ⇝ t (wavy arrow)", "$(s,t)\\mapsto t$", "symbol", None, "high",
      "$(s,t)\\mapsto t$", "$(s,t)\\leadsto t$", LEADSTO_NOTE),
    F(11, "(8.2.7), 1st line: 'un objet final e (8.1.10)'",
      "bold italic e", "plain $e$", "font", None, "high",
      "\\emph{objet final} $e$", "\\emph{objet final} $\\boldsymbol{e}$", E_NOTE),
    F(11, "(8.2.7): 'prenant en particulier Y' = e'",
      "bold italic e", "plain $e$", "font", None, "high",
      "$Y'=e$", "$Y'=\\boldsymbol{e}$", E_NOTE),
    F(11, "(8.2.7): 'l'unique élément ε de Hom(Y, e)'",
      "bold italic e", "plain $e$", "font", None, "high",
      "\\operatorname{Hom}(Y,e)", "\\operatorname{Hom}(Y,\\boldsymbol{e})", E_NOTE),
    F(11, "(8.2.7): 'l'élément η_X(e) détermine complètement'",
      "bold italic e", "plain $e$", "font", None, "high",
      "$\\eta_X(e)$", "$\\eta_X(\\boldsymbol{e})$", E_NOTE),
    F(11, "(8.2.7), diagram, top left vertex h_X(e)",
      "bold italic e", "plain $e$", "font", None, "high",
      "h_X(e)\\ar[r]^", "h_X(\\boldsymbol{e})\\ar[r]^", E_NOTE),
    F(11, "(8.2.7), diagram, label of the left vertical arrow h_{e_X}(e)",
      "e in bold (small label type)", "plain $e$", "font", None, "medium",
      "h_{e_X}(e)}", "h_{e_X}(\\boldsymbol{e})}",
      E_NOTE + " In this small label the bold e is clear; whether it is italic is hard to judge at that size."),
    F(11, "(8.2.7), diagram, bottom left vertex h_X(e)",
      "bold italic e", "plain $e$", "font", None, "high",
      "h_X(e)\\ar[r]_", "h_X(\\boldsymbol{e})\\ar[r]_", E_NOTE),
    # ---------------- page 12 ----------------
    F(12, "top line (end of (8.2.7)): 's⇝η_X(Y) transformant tout élément'",
      "s ⇝ η_X(Y) (wavy arrow)", "$s\\mapsto\\eta_X(Y)$", "symbol", None, "high",
      "$s\\mapsto\\eta_X(Y)$", "$s\\leadsto\\eta_X(Y)$", LEADSTO_NOTE),
    F(12, "(8.2.7), last line: 'sont tous deux égaux à 1_X'",
      "*égaux à* (both words italic)", "\\emph{égaux} à", "italics", None, "high",
      "\\emph{égaux} à", "\\emph{égaux à}",
      "Enlarged crop: 'à' is italic as well."),
    F(12, "Définition (9.1.1): 'est quasi-compacte si pour tout ouvert'",
      "quasi-compacte italic like the rest of the definition",
      "\\emph{quasi-compacte} inside the italic definition (comes out upright)",
      "convention", 6, "high",
      "\\emph{quasi-compacte} si", "quasi-compacte si",
      "No change of face in the print; \\emph inside the italic environment sets the word upright."),
    F(12, "Définition (9.1.1): 'est rétrocompacte dans X si l'injection canonique'",
      "rétrocompacte dans X italic like the rest of the definition",
      "\\emph{rétrocompacte dans $X$} inside the italic definition (comes out upright)",
      "convention", 6, "high",
      "\\emph{rétrocompacte\ndans $X$}", "rétrocompacte\ndans $X$",
      "No change of face in the print."),
    F(12, "Définition (9.1.2): 'on dit qu'une partie de X est constructible si'",
      "constructible italic like the rest of the definition",
      "\\emph{constructible} inside the italic definition (comes out upright)",
      "convention", 6, "high",
      "\\emph{constructible}", "constructible",
      "No change of face in the print."),
    F(12, "Définition (9.1.2): 'contenant toutes les parties ouvertes rétrocompactes de 𝔉'",
      "rétrocompactes de 𝔉 (Fraktur F)", "rétrocompactes de $\\mathfrak{F}$ (keeps the print)",
      "misprint_in_print", None, "high", None, None,
      "The print has 𝔉 where the sense requires X (𝔉 is the set of parts being defined: it must contain "
      "the retrocompact open parts of X). The TeX keeps the printed reading.",
      corrected="rétrocompactes de\n$X$"),
    F(12, "Définition (9.1.2): '(ce qui implique que 𝔉 est aussi stable par réunion finie)'",
      "'(ce qui implique que 𝔉 est aussi' and ')' roman; only 'stable par réunion finie' italic",
      "whole parenthesis italic (inside the definition environment)",
      "convention", 6, "high",
      "(ce qui implique que $\\mathfrak{F}$ est aussi stable par réunion finie).",
      "\\textup{(ce qui implique que $\\mathfrak{F}$ est aussi} stable par réunion finie\\textup{)}.",
      "Enlarged crop: the parenthesis is set roman with an italic 'stable par réunion finie'."),
    F(12, "proof of (9.1.3), last lines: 'on a ∁Z = ⋂(V_i∪∁U_i), donc Z est réunion finie'",
      "donc Z est réunion finie (no ∁)", "donc $\\complement{Z}$ est réunion finie",
      "misprint_in_print", None, "high",
      "donc\n$\\complement{Z}$ est réunion", "donc\n$Z$ est réunion",
      "The print drops the complement sign (enlarged crop); the sense requires ∁Z. The TeX silently corrects it; "
      "the fix restores the printed reading.",
      corrected="donc\n$\\complement{Z}$ est réunion"),
    # ---------------- page 13 ----------------
    F(13, "(9.1.6): '(cf. I, 5.5.6)'",
      "bold I", "plain I", "convention", 2, "high",
      "{I, 5.5.6}", "{\\textbf{I}, 5.5.6}",
      "Bold chapter numeral in the reference."),
    F(13, "Proposition (9.1.8), label (i)",
      "(i) upright", "\\item[(i)] italic inside the italic proposition", "convention", 6, "high",
      "\\item[(i)] Si $T$", "\\item[\\textup{(i)}] Si $T$",
      "Roman-numeral item labels are upright in the print (GLOBAL_ISSUES item 16)."),
    F(13, "Proposition (9.1.8), label (ii)",
      "(ii) upright", "\\item[(ii)] italic inside the italic proposition", "convention", 6, "high",
      "\\item[(ii)] Supposons", "\\item[\\textup{(ii)}] Supposons",
      "Roman-numeral item labels are upright in the print (GLOBAL_ISSUES item 16)."),
    F(13, "proof of (9.1.8)(ii): 'il s'ensuivra alors que U—Z est constructible dans X'",
      "U—Z (long dash)", "$U\\setminus Z$ (backslash set minus)", "convention", 7, "high",
      "$U\\setminus Z$", "$U\\setmin Z$",
      "Set difference printed with the long dash; the TeX has \\setminus here, not a minus sign. "
      "Fix as for EGA II (\\setminus -> \\setmin); it shows the dash only once \\setmin is redefined."),
    F(13, "proof of (9.1.8)(ii): 'Z∩(U—Z') sera bien constructible dans X'",
      "Z∩(U—Z') (long dash)", "$Z\\cap(U\\setminus Z')$", "convention", 7, "high",
      "(U\\setminus Z')", "(U\\setmin Z')",
      "As the previous finding."),
    # ---------------- page 14 ----------------
    F(14, "Définition (9.1.11): 'est localement constructible dans X si, pour tout x∈X'",
      "localement constructible dans X italic like the rest of the definition",
      "\\emph{localement constructible dans $X$} inside the italic definition (comes out upright)",
      "convention", 6, "high",
      "\\emph{localement constructible dans $X$}", "localement constructible dans $X$",
      "No change of face in the print (enlarged crop)."),
    F(14, "(9.2.1): 'sont les réunions finies de parties localement fermées de X.'",
      "*réunions finies de parties localement fermées* de X ('de' roman)",
      "\\emph{réunions finies de parties localement fermées de $X$}", "italics", None, "high",
      "localement fermées de $X$}.", "localement fermées} de $X$.",
      "Enlarged crop: the italic stops after 'fermées'."),
]

# ---------------- bold italic category letter C (pp. 10-12) ----------------
C_RE = re.compile(r"(?<![A-Za-z\\])C(?![A-Za-z])")

TOP = {10: "(8.2.2), continued", 11: "(8.2.5), continued", 12: "(8.2.7), continued"}

def statement_at(text, i, page):
    last = None
    for m in re.finditer(r"\\begin\{(\w+)\}\[([^\]]*)\]", text[:i]):
        last = m
    if last is None:
        return TOP[page]
    return f"({last.group(2)})"

def snippet(text, i, width=28):
    a = max(text.rfind("\n", 0, i) + 1, i - width)
    b = text.find("\n", i)
    b = len(text) if b < 0 else min(b, i + width)
    return text[a:b]

def minimal_context(text, i):
    a, b = _context(text, i, 1)
    if len(C_RE.findall(text[a:b])) > 1:   # window must not swallow a neighbouring C
        a, b = _context(text, i, 0)
    return a, b

def _context(text, i, pad):
    toks = [m.span() for m in re.finditer(r"\S+", text)]
    k = next(j for j, (a, b) in enumerate(toks) if a <= i < b)
    lo, hi = max(k - pad, 0), min(k + pad, len(toks) - 1)
    turn = 0
    while True:
        a, b = toks[lo][0], toks[hi][1]
        s = text[a:b]
        if text.count(s) == 1:
            return a, b
        if turn % 2 == 0 and hi + 1 < len(toks):
            hi += 1
        elif lo > 0:
            lo -= 1
        else:
            hi += 1
        turn += 1

C_NOTE = ("Category letter C printed bold italic throughout (checked on the strips and enlarged crops); "
          "the TeX has a plain italic C. Same issue as K in 0_I and convention 10; \\boldsymbol as in FIX_POLICY.")

auto = []
for p in (10, 11, 12):
    text = TEXT[p]
    body_start = text.index("\n", text.index("\\oldpage")) + 1
    for m in C_RE.finditer(text, body_start):
        i = m.start()
        a, b = minimal_context(text, i)
        old = text[a:b]
        rel = i - a
        new = old[:rel] + "\\boldsymbol{C}" + old[rel + 1:]
        shown = snippet(text, i)
        auto.append(F(p, f"{statement_at(text, i, p)}: '{shown}'", "bold italic C", "plain $C$",
                      "font", None, "high", old, new, C_NOTE))

findings = manual + auto

# ---------------- validation ----------------
ok = True
spans = {p: [] for p in TEXT}
for f in findings:
    fx = f["fix"]
    if fx is None:
        continue
    t = TEXT[f["page"]]
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print(f"NOT UNIQUE ({n}): p{f['page']} {fx['old']!r}")
        continue
    a = t.index(fx["old"])
    spans[f["page"]].append((a, a + len(fx["old"]), fx["old"]))

for p, lst in spans.items():
    lst.sort()
    for (a1, b1, o1), (a2, b2, o2) in zip(lst, lst[1:]):
        if a2 < b1:
            print(f"OVERLAP p{p}: {o1!r} / {o2!r}")

# apply in list order and in reverse order: each old must match exactly once at its turn
for order_name, seq in (("forward", findings), ("reverse", list(reversed(findings)))):
    work = dict(TEXT)
    for f in seq:
        fx = f["fix"]
        if fx is None:
            continue
        t = work[f["page"]]
        n = t.count(fx["old"])
        if n != 1:
            ok = False
            print(f"{order_name}: old matches {n}x at its turn: p{f['page']} {fx['old']!r}")
            continue
        work[f["page"]] = t.replace(fx["old"], fx["new"], 1)
    # remaining plain C letters after all fixes (pp. 10-12)
    for p in (10, 11, 12):
        body = work[p][work[p].index("\n", work[p].index("\\oldpage")) + 1:]
        left = re.findall(r"(?<!\\boldsymbol\{)(?<![A-Za-z\\])C(?![A-Za-z])", body)
        if left:
            ok = False
            print(f"{order_name}: plain C left on p{p}: {len(left)}")
    if order_name == "forward":
        for p in sorted(work):
            print(f"--- page {p}: \\mapsto left: {work[p].count(chr(92) + 'mapsto')}")

counts = {}
for f in findings:
    c = counts.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})
    if f["kind"] == "convention":
        c["convention"] += 1
    elif f["kind"] == "misprint_in_print":
        c["misprint"] += 1
    else:
        c["normal"] += 1
print(json.dumps(counts))
print("total", len(findings), "valid" if ok else "INVALID")

if ok and "--write" in sys.argv:
    findings.sort(key=lambda f: f["page"])
    OUTFILE.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUTFILE)
