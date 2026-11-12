import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_065_069.json")

F = []


def add(page, where, scan, tex, kind, old, new, conf="high", conv=None,
        note="", corrected=None, fix_null=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if fix_null else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


C7 = ("Long dash for set difference printed; minus sign in the TeX. "
      "\\setmin pending the convention-7 decision (GLOBAL_ISSUES 5).")

# ---------------------------------------------------------------- page 64 (end)
add(64, "end of p. 64, before \\oldpage[IV-3]{65}: '... deux O_Z-Modules | cohérents G, H ...'",
    "page break inside the sentence (p. 65 begins 'cohérents'); no paragraph break",
    "blank line before \\oldpage[IV-3]{65}, making a paragraph break mid-sentence",
    "marker",
    "deux $\\mathcal O_Z$-Modules\n\n", "deux $\\mathcal O_Z$-Modules\n",
    note="Outside pp. 65-69: old lies at the end of page_064.tex. Apply together with the p. 65 entry "
         "that removes the blank line after \\oldpage[IV-3]{65} (GLOBAL_ISSUES 20). The pp. 60-64 batch "
         "may file the same edit; apply it once.")

# ---------------------------------------------------------------- page 65
add(65, "top of p. 65, after \\oldpage[IV-3]{65}",
    "'des O_Z-Modules | cohérents' continues the sentence of p. 64",
    "blank line after \\oldpage[IV-3]{65}",
    "marker",
    "\\oldpage[IV-3]{65}\n\ncohérents", "\\oldpage[IV-3]{65}\ncohérents",
    note="Mid-sentence page break (GLOBAL_ISSUES 20); marker position itself is right. Apply together "
         "with the p. 64 entry removing the blank line before the marker.")
add(65, "line 3: 'supposer U_0 pris tel que pour s∈U_0, u_s : ...'",
    "pris tel que pour s∈U₀, u_s : G_s→H_s", "pris tel que, pour $s\\in U_0$",
    "punctuation",
    "tel que, pour $s\\in U_0$", "tel que pour $s\\in U_0$",
    note="No comma after 'que' in the print.")
add(65, "4°, line 1: 'η∈S—E''", "η∈S—E'", "$\\eta\\in S-E'$", "convention",
    "$4^\\circ$ $\\eta\\in S-E'$", "$4^\\circ$ $\\eta\\in S\\setmin E'$", conv=7, note=C7)
add(65, "4°, line 1: 'S—E⊂S—E'' (first dash)", "S—E⊂", "$S-E\\subset", "convention",
    "$S-E\\subset", "$S\\setmin E\\subset", conv=7, note=C7)
add(65, "4°, line 1: 'S—E⊂S—E'' (second dash)", "⊂S—E', et si", "\\subset S-E'$, et si", "convention",
    " S-E'$, et si", " S\\setmin E'$, et si", conv=7, note=C7)
add(65, "4°, line 1: 'et si η∈S—E,'", "η∈S—E,", "$\\eta\\in S-E$,", "convention",
    "$\\eta\\in S-E$,", "$\\eta\\in S\\setmin E$,", conv=7, note=C7)
add(65, "4°, line 1: 'S—E' est a fortiori'", "S—E' est a fortiori", "$S-E'$ est \\emph{a fortiori}", "convention",
    "$S-E'$ est \\emph{a fortiori}", "$S\\setmin E'$ est \\emph{a fortiori}", conv=7, note=C7)
add(65, "Prop. (9.4.8): 'Alors l'ensemble E (resp. E')'",
    "'resp.' upright (roman) inside the italic statement", "\\textnormal{(}resp. $E'$ (resp. italic)",
    "convention",
    "\\textnormal{(}resp. $E'$", "\\textnormal{(resp.} $E'$", conv=6)
add(65, "Prop. (9.4.8): 'de torsion (resp. un O_{X_s}-Module sans torsion)'",
    "'resp.' upright (roman); 'un ... sans torsion' italic", "\\textnormal{(}resp. un (resp. italic)",
    "convention",
    "\\textnormal{(}resp. un", "\\textnormal{(resp.} un", conv=6)
add(65, "proof of (9.4.8): 'prouver que E ou S—E'", "E ou S—E (resp.", "$E$ ou $S-E$ (resp.", "convention",
    "ou $S-E$ (resp.", "ou $S\\setmin E$ (resp.", conv=7, note=C7)
add(65, "proof of (9.4.8): '(resp. E' ou S—E')'", "E' ou S—E')", "$E'$ ou $S-E'$)", "convention",
    "ou $S-E'$)", "ou $S\\setmin E'$)", conv=7, note=C7)
add(65, "proof of (9.4.8): 'B_s=B⊗_A k(s)'", "bold italic k in k(s)", "$B_s=B\\otimes_A k(s)$", "convention",
    "$B_s=B\\otimes_A k(s)$", "$B_s=B\\otimes_A \\boldsymbol{k}(s)$", conv=1)
add(65, "proof of (9.4.8): 'M_s=M⊗_A k(s)'", "bold italic k in k(s)", "$M_s=M\\otimes_A k(s)$", "convention",
    "$M_s=M\\otimes_A k(s)$", "$M_s=M\\otimes_A \\boldsymbol{k}(s)$", conv=1)
add(65, "end of p. 65, before \\oldpage[IV-3]{66}: '... appliqué suivant la méthode | de (8.1.2, a)) ...'",
    "page break inside the sentence; no paragraph break",
    "blank line before \\oldpage[IV-3]{66}",
    "marker",
    "la méthode\n\n", "la méthode\n",
    note="Mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 66 entry removing the "
         "blank line after \\oldpage[IV-3]{66}.")

# ---------------------------------------------------------------- page 66
add(66, "top of p. 66, after \\oldpage[IV-3]{66}",
    "'la méthode | de (8.1.2, a))' continues the sentence of p. 65",
    "blank line after \\oldpage[IV-3]{66}",
    "marker",
    "\\oldpage[IV-3]{66}\n\nde (8.1.2", "\\oldpage[IV-3]{66}\nde (8.1.2",
    note="Mid-sentence page break (GLOBAL_ISSUES 20); marker position itself is right. Apply together "
         "with the p. 65 entry removing the blank line before the marker.")
add(66, "1°, line 4: 'l'endomorphisme u_s : F_s→F_s, défini par la multiplication par g_s, est nul'",
    "u_s : F_s→F_s, défini", "$u_s:\\mathcal F_s\\to\\mathcal F_s$ défini",
    "punctuation",
    "$u_s:\\mathcal F_s\\to\\mathcal F_s$ défini", "$u_s:\\mathcal F_s\\to\\mathcal F_s$, défini",
    note="The print has a comma after the formula (paired with the comma after 'g_s').")
add(66, "2°: 'η∈S—E. Dire'", "η∈S—E", "$\\eta\\in S-E$", "convention",
    "$\\eta\\in S-E$. Dire", "$\\eta\\in S\\setmin E$. Dire", conv=7, note=C7)
add(66, "4°: 'η∈S—E'. Soit'", "η∈S—E'", "$\\eta\\in S-E'$", "convention",
    "$\\eta\\in S-E'$. Soit", "$\\eta\\in S\\setmin E'$. Soit", conv=7, note=C7)
add(66, "Remarque (9.4.9), last lines: 'posons X=X_0×_{S_0}S, F=F_0⊗_{O_{S_0}}O_S'",
    "roman upright F (not script) before '=': 'F=𝓕_0⊗...'",
    "$\\mathcal F=\\mathcal F_0\\otimes_{\\mathcal O_{S_0}}...",
    "misprint_in_print",
    "$\\mathcal F=\\mathcal F_0", "$F=\\mathcal F_0",
    corrected="\\mathcal F",
    note="Wrong font in the print: the sheaf defined here is the script F (used as F_s just after). "
         "The TeX silently corrects it; the diplomatic text takes the printed roman F.")
add(66, "end of p. 66, before \\oldpage[IV-3]{67}: '... (resp. sans | torsion) est encore ...'",
    "page break inside the sentence; no paragraph break",
    "blank line before \\oldpage[IV-3]{67}",
    "marker",
    "(resp. sans\n\n", "(resp. sans\n",
    note="Mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 67 entry removing the "
         "blank line after \\oldpage[IV-3]{67}.")

# ---------------------------------------------------------------- page 67
add(67, "top of p. 67, after \\oldpage[IV-3]{67}",
    "'(resp. sans | torsion)' continues the sentence of p. 66",
    "blank line after \\oldpage[IV-3]{67}",
    "marker",
    "\\oldpage[IV-3]{67}\n\ntorsion)", "\\oldpage[IV-3]{67}\ntorsion)",
    note="Mid-sentence page break (GLOBAL_ISSUES 20); marker position itself is right. Apply together "
         "with the p. 66 entry removing the blank line before the marker.")
add(67, "end of Remarque (9.4.9): 'T⊗_{k(s_0)} k(s)' (subscript)",
    "bold upright k in the subscript k(s_0)", "\\otimes_{k(s_0)}", "convention",
    "\\otimes_{k(s_0)}", "\\otimes_{\\mathbf{k}(s_0)}", conv=1,
    note="Bold upright in subscripts, bold italic on the line (GLOBAL_ISSUES 48).")
add(67, "end of Remarque (9.4.9): 'T⊗_{k(s_0)} k(s)' (on the line)",
    "bold italic k in k(s)", "k(s)$ (qui", "convention",
    "k(s)$ (qui", "\\boldsymbol{k}(s)$ (qui", conv=1)
add(67, "Cor. (9.5.2): 'tels que Z'_s⊂Z''_s (resp. Z'_s=Z''_s)'",
    "'resp.' upright (roman) inside the italic statement", "\\textnormal{(}resp. (resp. italic)",
    "convention",
    "\\textnormal{(}resp.", "\\textnormal{(resp.}", conv=6)
add(67, "proof of (9.5.3), first line: 'les deux conditions de (9.2.2, (ii))'",
    "(9.2.2, (ii))", "(9.2.2, (iii))", "number",
    "(9.2.2, (iii))", "(9.2.2, (ii))",
    note="The print is right: the two conditions 1° and 2° are in Remarques (9.2.2, (ii)); (9.2.2) has "
         "no item with two conditions under (iii). Same on p. 68 (TeX has (ii) there) and twice on p. 69.")
add(67, "proof of (9.5.3): 'la relation Z̄=Z̄'' est équivalente'",
    "bar over Z only in the second term, prime outside: \\overline{Z}'",
    "\\overline Z=\\overline{Z'}", "formula",
    "\\overline Z=\\overline{Z'}$ est", "\\overline Z=\\overline Z'$ est",
    note="In the same sentence p^{-1}(\\overline{Z'}) has the bar over Z' (as in the TeX); here the bar "
         "covers Z only. Typographic, as in earlier \\overline{X'} -> \\overline{X}' fixes.")
add(67, "1°: 'η∈S—E, autrement dit'", "η∈S—E", "$\\eta\\in S-E$", "convention",
    "$\\eta\\in S-E$, autrement", "$\\eta\\in S\\setmin E$, autrement", conv=7, note=C7)
add(67, "1°, last line: 'autrement dit U⊂S—E.'", "U⊂S—E", "$U\\subset S-E$", "convention",
    "$U\\subset S-E$.", "$U\\subset S\\setmin E$.", conv=7, note=C7)

# ---------------------------------------------------------------- page 68
add(68, "2°, line 2: 'posons V_η=X_η—Z̄_η'", "V_η=X_η—Z̄_η", "$V_\\eta=X_\\eta-\\overline{Z_\\eta}$",
    "convention",
    "$V_\\eta=X_\\eta-", "$V_\\eta=X_\\eta\\setmin", conv=7, note=C7)
add(68, "2°, lines 2-3: 'posons V_η=X_η—Z̄_η qui est ouvert dans X_η'",
    "no comma after the formula (line ends 'X_η—Z̄_η', next line 'qui est ouvert')",
    "$V_\\eta=X_\\eta-\\overline{Z_\\eta}$, qui est ouvert", "punctuation",
    "$, qui est ouvert dans $X_\\eta$", "$ qui est ouvert dans $X_\\eta$",
    note="Disjoint from the convention-7 edit in the same formula.")
add(68, "2°: 'donc V∩Z̄'=∅ (adhérence prise dans X)'",
    "bar over Z only, prime outside: V∩\\overline{Z}'=∅", "$V\\cap\\overline{Z'}=\\varnothing$", "formula",
    "$V\\cap\\overline{Z'}=\\varnothing$", "$V\\cap\\overline Z'=\\varnothing$",
    note="In the next line (\\overline{Z'})_\\eta has the bar over Z' (as in the TeX); here only over Z.")
add(68, "2°: 'et l'on est ainsi ramené au cas où Z' est irréductible.'",
    "'irréductible' in italics", "$Z'$ est irréductible.", "italics",
    "$Z'$ est irréductible.", "$Z'$ est \\emph{irréductible}.")
add(68, "Cor. (9.5.4): 'soit fermé (resp. ouvert, resp. localement fermé)' (first resp.)",
    "'resp.' upright (roman); 'ouvert' italic", "\\textnormal{(}resp. ouvert (resp. italic)", "convention",
    "\\textnormal{(}resp. ouvert", "\\textnormal{(resp.} ouvert", conv=6)
add(68, "Cor. (9.5.4): 'resp. localement fermé' (second resp.)",
    "'resp.' upright (roman); 'localement fermé' italic", ", resp. localement fermé (resp. italic)",
    "convention",
    ", resp. localement", ", \\textup{resp.} localement", conv=6)
add(68, "proof of (9.5.4): '(X—Z)_s'", "(X—Z)_s", "$(X-Z)_s", "convention",
    "$(X-Z)_s", "$(X\\setmin Z)_s", conv=7, note=C7)
add(68, "proof of (9.5.4): '=X_s—Z_s'", "X_s—Z_s", "=X_s-Z_s$", "convention",
    "=X_s-Z_s$", "=X_s\\setmin Z_s$", conv=7, note=C7)
add(68, "proof of (9.5.4): 'et comme X—Z est localement constructible'", "X—Z", "$X-Z$", "convention",
    "comme $X-Z$ est", "comme $X\\setmin Z$ est", conv=7, note=C7)
add(68, "proof of (9.5.4): 'où Z''=Z'—Z'", "Z''=Z'—Z", "$Z''=Z'-Z$", "convention",
    "$Z''=Z'-Z$", "$Z''=Z'\\setmin Z$", conv=7, note=C7)
add(68, "proof of (9.5.4): 'E ou S—E contienne'", "E ou S—E", "$E$ ou $S-E$", "convention",
    "ou $S-E$ contienne", "ou $S\\setmin E$ contienne", conv=7, note=C7)

# ---------------------------------------------------------------- page 69
add(69, "Prop. (9.5.5): 'D(s)⊂Z∪{—∞}'", "long dash before ∞: {—∞}", "\\{-\\infty\\}", "convention",
    "\\mathbf Z\\cup\\{-\\infty\\}$ l'ensemble", "\\mathbf Z\\cup\\{\\setmin\\infty\\}$ l'ensemble",
    conv=7, note="Unary minus printed as the long dash (GLOBAL_ISSUES 23/49); \\setmin pending the "
                 "convention-7 decision, as in the IV-2 findings.")
add(69, "Prop. (9.5.5): 'Alors la fonction s⇝D(s)'", "wavy arrow ⇝ (\\leadsto)", "$s\\mapsto D(s)$", "symbol",
    "$s\\mapsto D(s)$", "$s\\leadsto D(s)$",
    note="Not convention 3: the print's arrow is the wavy one, as in earlier \\mapsto -> \\leadsto fixes.")
add(69, "proof of (9.5.5), line 1: 'partie finie de Z∪{—∞}'", "long dash before ∞: {—∞}", "\\{-\\infty\\}",
    "convention",
    "\\{-\\infty\\}$~;", "\\{\\setmin\\infty\\}$~;",
    conv=7, note="Unary minus printed as the long dash (GLOBAL_ISSUES 23/49); \\setmin pending the "
                 "convention-7 decision.")
add(69, "proof of (9.5.5), line 3: 'les deux conditions de (9.2.2, (ii))'",
    "(9.2.2, (ii))", "(9.2.2, (iii))", "number",
    "conditions de (9.2.2, (iii))", "conditions de (9.2.2, (ii))",
    note="The print is right: the two conditions are those of Remarques (9.2.2, (ii)) (see p. 67).")
add(69, "proof of (9.5.5): 'Pour la seconde condition de (9.2.2, (ii))'",
    "(9.2.2, (ii))", "(9.2.2, (iii))", "number",
    "seconde condition de (9.2.2, (iii))", "seconde condition de (9.2.2, (ii))",
    note="As above.")
add(69, "proof of (9.5.5): 'composantes irréductibles Z_{iη}, qui sont localement fermées dans X.'",
    "localement fermées dans X. (no subscript η; the full stop follows X directly)",
    "localement fermées dans $X_\\eta$.",
    "misprint_in_print",
    "fermées dans $X_\\eta$. Il", "fermées dans $X$. Il",
    conf="high", corrected="X_\\eta",
    note="The components Z_{iη} of Z_η are locally closed in X_η, not in general in X (X_η need not be "
         "locally closed in X); the next sentence deduces Z_i from local closedness in X_η. The TeX "
         "silently corrects; the diplomatic text takes the printed X.")
add(69, "proof of (9.5.5): 'pour i≠j, Z_{iη}∩Z_{jη} est rare et fermé dans Z_{iη}'",
    "both 'rare' and 'fermé' in italics", "est rare et \\emph{fermé}", "italics",
    "est rare et \\emph{fermé}", "est \\emph{rare} et \\emph{fermé}",
    note="In the next clause '(Z_i)_s∩(Z_j)_s est rare et fermé' both words are upright, as in the TeX.")
add(69, "proof of (9.5.5): 'un sous-préschéma de X ayant Z_i pour espace sous-jacent Z_i (et encore noté Z_i)'",
    "pour espace sous-jacent Z_i (et encore noté Z_i)",
    "pour espace sous-jacent (et encore noté $Z_i$)",
    "misprint_in_print",
    "pour espace sous-jacent (et encore", "pour espace sous-jacent $Z_i$ (et encore",
    corrected="pour espace sous-jacent (et encore",
    note="The print repeats Z_i ('ayant Z_i pour espace sous-jacent Z_i'). The TeX silently drops the "
         "second Z_i; the diplomatic text restores it.")
add(69, "proof of (9.5.5): 'Posons U_i=Z_i—⋃_{j≠i}(Z_i∩Z_j)'", "Z_i—⋃", "$U_i=Z_i-\\bigcup", "convention",
    "$U_i=Z_i-\\bigcup", "$U_i=Z_i\\setmin\\bigcup", conv=7, note=C7)
add(69, "proof of (9.5.5): '..., qui est ouvert dans Z et tel que'",
    "ouvert dans Z (no subscript i; line ends with Z)", "ouvert dans $Z_i$", "formula",
    "ouvert dans $Z_i$ et tel que", "ouvert dans $Z$ et tel que",
    conf="high",
    note="Plain Z in the print. Not recorded as a misprint: U_i=Z−⋃_{j≠i}Z_j, and openness of the U_i in "
         "Z is what the next sentence uses (components of the union of the (U_i)_s). If the coordinator "
         "prefers Z_i as an editorial correction, file it as a misprint instead.")
add(69, "proof of (9.5.5): 'Comme (Z_i)_s est un k(s)-préschéma algébrique'",
    "bold italic k in k(s)", "$k(s)$-préschéma", "convention",
    "$k(s)$-préschéma", "$\\boldsymbol{k}(s)$-préschéma", conv=1)
add(69, "proof of (9.5.5): 'qui rencontre X_η (0_I, 2.1.8), et l'on peut'",
    "comma after (0_I, 2.1.8)", "$(\\mathbf 0_{\\mathrm I},2.1.8)$ et", "punctuation",
    "2.1.8)$ et\nl'on", "2.1.8)$, et\nl'on")
add(69, "proof of (9.5.6), last line: 'qui est de type fini (1.5.4, (vi))'",
    "(1.5.4, (vi))", "(1.5.4, (vii))", "number",
    "(1.5.4, (vii))", "(1.5.4, (vi))",
    note="The print is right: (1.5.4) has items (i)-(vi), and (vi) is the one about f_red.")
add(69, "end of p. 69, before \\oldpage[IV-3]{70}: '... on peut | supposer A intègre ...'",
    "page break inside the sentence; no paragraph break",
    "blank line before \\oldpage[IV-3]{70}",
    "marker",
    "on peut\n\n", "on peut\n",
    note="Mid-sentence page break (GLOBAL_ISSUES 20). Pairs with the p. 70 entry (next batch) removing the "
         "blank line after \\oldpage[IV-3]{70}; that batch may file this same edit; apply it once.")

# ---------------------------------------------------------------- checks
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    p = os.path.join(RUN, "page_%03d.tex" % d["page"])
    txt = open(p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    n = txt.count(fx["old"])
    if n != 1:
        ok = False
        print("COUNT", n, d["page"], repr(fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("SAME", d["page"], repr(fx["old"]))

# overlap check per page: no two olds may overlap in the page text
from collections import defaultdict
spans = defaultdict(list)
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    p = os.path.join(RUN, "page_%03d.tex" % d["page"])
    txt = open(p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    i = txt.find(fx["old"])
    spans[d["page"]].append((i, i + len(fx["old"]), fx["old"]))
for pg, ss in spans.items():
    ss.sort()
    for a, b in zip(ss, ss[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", pg, repr(a[2]), repr(b[2]))

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for pg in sorted(set(p for p, _ in cnt)):
    print(pg, cnt[(pg, "normal")], cnt[(pg, "convention")], cnt[(pg, "misprint")])
print("OK" if ok else "PROBLEMS", len(F))
