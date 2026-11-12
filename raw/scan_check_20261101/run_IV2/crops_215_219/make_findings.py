import json, os, re, sys
sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding="utf-8")

RUN = r"user\Documents\ega_scan_check_20261101\run_IV2"
OUT = os.path.join(RUN, "findings_215_219.json")
REL = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex"

def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

L = []
# ---------------------------------------------------------------- page 215
L.append(F(215, "top of the page: page break 214/215 inside the sentence 'il faut et | il suffit'",
  "p. 215 begins 'il suffit qu'il soit universellement caténaire...', continuing the last line of p. 214 ('Pour qu'un anneau local noethérien soit excellent, il faut et'); no paragraph break",
  "blank lines before and after \\oldpage[IV-2]{215} make a paragraph break",
  "marker", None, "high",
  "\\oldpage[IV-2]{215}\n\nil suffit", "\\oldpage[IV-2]{215}\nil suffit",
  "OUTSIDE-SEGMENT COMPANION: the blank line BEFORE the marker lies in p. 214's segment (page_214.tex ends 'soit excellent, il faut et\\n\\n') and must be removed with this edit: old 'soit excellent, il faut et\\n\\n' -> new 'soit excellent, il faut et\\n'."))
for lab, old in [("(ii)", "(ii) Si $A$"), ("(iii)", "(iii) Un anneau"), ("(iv)", "(iv) Soient $A$"),
                 ("(v)", "(v) Soient $A$"), ("(vi)", "(vi) Un anneau"), ("(vii)", "(vii) Soit $A$"),
                 ("(viii)", "(viii) Si $A$"), ("(ix)", "(ix) Soient $A$")]:
    L.append(F(215, "Scholie (7.8.3), label " + lab,
      "label " + lab + " printed upright", lab + " is plain text inside the italic scholium environment (comes out italic)",
      "convention", 6, "high", old, old.replace(lab, "\\textup{" + lab + "}", 1)))
L.append(F(215, "Scholie (7.8.3) (iv), l. 1: 'Reg(X) (resp. Nor(X), ...'",
  "'(resp.' upright", "italic", "convention", 6, "high",
  "(resp. $\\operatorname{Nor}(X)$,", "\\textup{(resp.} $\\operatorname{Nor}(X)$,"))
L.append(F(215, "Scholie (7.8.3) (iv), l. 2: 'est régulier (resp. normal, resp. vérifie (R_n))'",
  "both 'resp.' upright ('normal', 'vérifie' italic)", "italic", "convention", 6, "high",
  "est régulier (resp. normal,\nresp. vérifie", "est régulier \\textup{(resp.} normal,\n\\textup{resp.} vérifie",
  "Two occurrences in one edit."))
L.append(F(215, "Scholie (7.8.3) (iv), l. 3: 'U_{C_n}(F) (resp. U_{S_n}(F), CM(F))'",
  "'(resp.' upright", "italic", "convention", 6, "high",
  "(resp.\n$\\mathrm U_{\\mathrm S_n}", "\\textup{(resp.}\n$\\mathrm U_{\\mathrm S_n}"))
L.append(F(215, "Scholie (7.8.3) (iv), l. 4: 'coprof(F_x) <= n (resp. des points où F vérifie (S_n), resp. des points où'",
  "both 'resp.' upright ('des points où' italic)", "italic", "convention", 6, "high",
  "(resp. des points où\n$\\mathcal F$ vérifie $(\\mathrm S_n)$, resp. des points où",
  "\\textup{(resp.} des points où\n$\\mathcal F$ vérifie $(\\mathrm S_n)$, \\textup{resp.} des points où",
  "Two occurrences in one edit."))
L.append(F(215, "Scholie (7.8.3) (v), l. 3: '(autrement dit, plat et à fibres géométriquement régulières)'",
  "'(autrement dit,' and 'et à fibres' upright; 'plat' and 'géométriquement régulières' italic",
  "all italic", "convention", 6, "high",
  "(autrement dit, plat et à fibres", "\\textup{(autrement dit,} plat \\textup{et à fibres}"))
L.append(F(215, "Scholie (7.8.3) (v), l. 5: '(avec les notations de (iv) et en posant'",
  "reference '(iv)' upright", "italic", "convention", 6, "high",
  "de (iv) et en posant", "de \\textup{(iv)} et en posant"))
L.append(F(215, "Scholie (7.8.3) (v), after (7.8.3.1): '(par exemple si A est local et J son idéal maximal)'",
  "whole parenthesis upright", "italic", "convention", 6, "high",
  "(par\nexemple si $A$ est local et $\\mathfrak J$ son idéal maximal)",
  "\\textup{(par\nexemple si $A$ est local et $\\mathfrak J$ son idéal maximal)}"))
L.append(F(215, "Scholie (7.8.3) (v), after (7.8.3.1): 'pour que A soit régulier (resp. normal, resp. réduit, resp. vérifie'",
  "the three 'resp.' upright ('normal', 'réduit', 'vérifie' italic)", "italic", "convention", 6, "high",
  "(resp. normal, resp. réduit, resp. vérifie",
  "\\textup{(resp.} normal, \\textup{resp.} réduit, \\textup{resp.} vérifie",
  "Three occurrences in one edit. Independent of the next (misprint) entry: the two 'old' strings do not overlap."))
L.append(F(215, "Scholie (7.8.3) (v), after (7.8.3.1): 'resp. vérifie (R_n), resp. soit de coprofondeur'",
  "(R_n) with the subscript n in bold italic (wrong-font sort: clearly heavier than the n of (S_n) one line below and of (R_n) in (iv); checked on 6x crops)",
  "$(\\mathrm R_n)$ with the ordinary n: the TeX silently corrects the print",
  "misprint_in_print", None, "medium",
  "(\\mathrm R_n)$,", "(\\mathrm R_{\\boldsymbol n})$,",
  "Typographical (wrong-font) slip, as in MISPRINTS.json for EGA II p. 49 (bold n in M_{n+k}); apply only if wrong-font letters are reproduced in the diplomatic text. 'old' does not overlap the convention edits before and after it.",
  corrected="$(\\mathrm R_n)$"))
L.append(F(215, "Scholie (7.8.3) (v), after (7.8.3.1): ', resp. soit de coprofondeur'",
  "'resp.' upright", "italic", "convention", 6, "high",
  "resp. soit\nde coprofondeur", "\\textup{resp.} soit\nde coprofondeur"))
L.append(F(215, "Scholie (7.8.3) (v), after (7.8.3.1): 'resp. vérifie (S_n), resp. soit un anneau de Cohen-Macaulay'",
  "both 'resp.' upright", "italic", "convention", 6, "high",
  "resp. vérifie $(\\mathrm S_n)$, resp. soit un anneau",
  "\\textup{resp.} vérifie $(\\mathrm S_n)$, \\textup{resp.} soit un anneau",
  "Two occurrences in one edit."))
L.append(F(215, "Scholie (7.8.3) (vii), l. 1: 'Soit A un anneau local excellent réduit'",
  "'local' upright (roman emphasis inside the italic statement, as 'anneau local noethérien' in (i) on p. 214)",
  "italic", "convention", 6, "high",
  "anneau local excellent réduit", "anneau \\textup{local} excellent réduit"))
L.append(F(215, "Scholie (7.8.3) (vii), l. 2-3: '(donc un anneau semi-local)'",
  "'(donc un anneau' upright, 'semi-local' italic", "all italic", "convention", 6, "high",
  "(donc un anneau semi-local)", "\\textup{(donc un anneau} semi-local)"))
L.append(F(215, "Scholie (7.8.3) (vii), l. 4: 'isomorphe au complété Â' de A''",
  "hat over A only, prime outside (Â')", "$\\widehat {A'}$ (hat over A and the prime)",
  "formula", None, "high",
  "$\\widehat {A'}$", "$\\widehat{A}'$",
  "Same treatment as \\widehat{M'} -> \\widehat{M}' in EGA I/II (FIXLOG); cf. GLOBAL_ISSUES 63 (candidate for convention 8)."))
L.append(F(215, "Scholie (7.8.3) (vii), l. 5-6: '(autrement dit, l'ensemble des idéaux premiers minimaux de Â)'",
  "upright except 'minimaux' (italic)", "all italic", "convention", 6, "high",
  "(autrement dit, l'ensemble des idéaux premiers\nminimaux de $\\widehat A$)",
  "\\textup{(autrement dit, l'ensemble des idéaux premiers}\nminimaux \\textup{de $\\widehat A$)}"))
L.append(F(215, "Scholie (7.8.3) (vii), l. 6-7: '(autrement dit, l'ensemble des idéaux maximaux de A')'",
  "upright except 'maximaux' (italic)", "all italic", "convention", 6, "high",
  "(autrement dit, l'ensemble des idéaux maximaux de\n$A'$)",
  "\\textup{(autrement dit, l'ensemble des idéaux} maximaux \\textup{de\n$A'$)}"))
L.append(F(215, "Scholie (7.8.3) (ix), l. 1: 'U = X—Z'",
  "long dash X—Z", "minus sign X-Z", "convention", 7, "high",
  "$U=X-Z$", "$U=X\\setmin Z$", "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."))

# ---------------------------------------------------------------- page 216
L.append(F(216, "Scholie (7.8.3), label (x)",
  "label (x) printed upright", "(x) is plain text inside the italic scholium environment (comes out italic)",
  "convention", 6, "high", "(x) Soit $A$", "\\textup{(x)} Soit $A$"))
L.append(F(216, "proof of (7.8.3), (i), l. 1: 'résulte de (5.6.3, (i)) et (7.4.4, (i)); la seconde'",
  "(7.4.4, (i))", "(7.4.4, (ii))", "number", None, "high",
  "(7.4.4, (ii))", "(7.4.4, (i))",
  "Transcription error, not a misprint: (7.4.4) (i) is the localisation statement (A_p is a P-ring) that the first assertion of (7.8.3) (i) needs; checked on a crop."))
L.append(F(216, "proof of (7.8.3), (viii): 'est une A-algèbre finie, comme il résulte de (vi)'",
  "'finie' italic", "roman", "italics", None, "high",
  "algèbre finie, comme il résulte", "algèbre \\emph{finie}, comme il résulte"))
L.append(F(216, "proof of (7.8.3), (viii), end: 'résulte donc de (0, 23.2.9)'",
  "bold 0", "plain 0", "convention", 2, "high",
  "(0, 23.2.9)", "(\\textbf{0}, 23.2.9)"))
L.append(F(216, "Remarques (7.8.4) (i), end: 'en remplaçant « excellent » par « vérifiant » (7.8.2, (ii) et (iii))'",
  "« vérifiant » (7.8.2, (ii) et (iii)): the closing guillemet stands before the reference",
  "same as the print (keeps the printed reading)", "misprint_in_print", None, "high",
  None, None,
  "Authors' erratum in the IV errata list 3 (ega4-errata-addenda-list3-fr.tex, item (IV, 7.8.4)): 'Ligne 10 du bas de la p. 216, remplacer « vérifiant » (7.8.2, (ii) et (iii)) par « vérifiant (7.8.2, (ii) et (iii)) »'. Nothing to change in the diplomatic TeX. Corrected-edition edit: old '« vérifiant » (7.8.2, (ii) et (iii))' -> new '« vérifiant (7.8.2, (ii) et (iii)) »'. (Err_IV 26 and 27 rewrite/extend Remarques (7.8.4) on p. 217; they are authorial addenda, not misprints, and the TeX matches the print there.)",
  corrected="« vérifiant (7.8.2, (ii) et (iii)) »"))
L.append(F(216, "end of the page: page break 216/217 inside the sentence 'le spectre d'un anneau | excellent'",
  "p. 217 begins 'excellent, donc vérifie la condition (6.12.4, a))', continuing the sentence; no paragraph break",
  "blank line before \\oldpage[IV-2]{217}", "marker", None, "high",
  "le spectre d'un anneau\n\n", "le spectre d'un anneau\n",
  "Apply together with the first p. 217 entry (blank line after the marker)."))

# ---------------------------------------------------------------- page 217
L.append(F(217, "top of the page: page break 216/217 inside the sentence",
  "'excellent, donc vérifie ...' continues the last line of p. 216; no paragraph break",
  "blank line after \\oldpage[IV-2]{217}", "marker", None, "high",
  "\\oldpage[IV-2]{217}\n\nexcellent", "\\oldpage[IV-2]{217}\nexcellent",
  "Apply together with the last p. 216 entry (blank line before the marker)."))
L.append(F(217, "Remarques (7.8.4) (iii), display (7.8.4.1)",
  "dim(A_m) = dim(A'_i)_{m'}  (one pair of parentheses: the subscript m' stands after the parenthesis of dim)",
  "\\dim((A'_i)_{\\mathfrak m'}): the TeX silently supplies the missing parentheses",
  "misprint_in_print", None, "medium",
  "=\\dim((A'_i)_{\\mathfrak m'})", "=\\dim(A'_i)_{\\mathfrak m'}",
  "The intended reading is the dimension of the local ring (A'_i)_{m'}, written with its parentheses everywhere else in the remark ((A'_i)_{m'}, ((A'_i)_{m'})^). Independent of the next entry (the full stop): the two 'old' strings do not overlap.",
  corrected="\\dim((A'_i)_{\\mathfrak m'})"))
L.append(F(217, "Remarques (7.8.4) (iii), display (7.8.4.1), end",
  "full stop after the formula", "no full stop", "punctuation", None, "high",
  "\n\\]\n\\end{env}", ".\n\\]\n\\end{env}"))
L.append(F(217, "Remarques (7.8.4) (iii), after (7.8.4.1): 'les analogues des propriétés (ii), (v), (vi) et (vii)'",
  "'analogues' roman (the remark is printed roman)", "\\emph{analogues} (italic in the upright remark)",
  "italics", None, "high",
  "les \\emph{analogues} des", "les analogues des"))
L.append(F(217, "Remarques (7.8.4) (iii): 'les complétés ((A'_i)_{m'})^ sont intègres'",
  "raised circumflex accent after the parenthesis", "^\\wedge (logical-and sign)",
  "symbol", None, "medium",
  "((A'_i)_{\\mathfrak m'})^\\wedge", "((A'_i)_{\\mathfrak m'})^{\\widehat{\\,}}",
  "As the EGA II p. 194 page fixes; GLOBAL_ISSUES 31/47 (\\superhat pass). The only two ^\\wedge in ega4-2 are on this page."))
L.append(F(217, "Remarques (7.8.4) (iii): 'les quotients du complété (A_m/p_iA_m)^'",
  "raised circumflex accent after the parenthesis", "^\\wedge (logical-and sign)",
  "symbol", None, "medium",
  "A_{\\mathfrak m})^\\wedge", "A_{\\mathfrak m})^{\\widehat{\\,}}",
  "See the previous entry."))
L.append(F(217, "Remarques (7.8.4) (iii), 'En particulier': 'un seul idéal premier p_i (0, 16.1.5)'",
  "bold 0", "plain 0", "convention", 2, "high",
  "(0, 16.1.5)", "(\\textbf{0}, 16.1.5)"))
L.append(F(217, "(7.8.5), l. 2-3: 'chacun des anneaux A_alpha des U_alpha est excellent ;'",
  "second 'excellent' italic", "roman", "italics", None, "high",
  "des $U_\\alpha$ est excellent;", "des $U_\\alpha$ est \\emph{excellent};"))

# ---------------------------------------------------------------- page 218
L.append(F(218, "Proposition (7.8.6) (ii): 'son normalisé X' (II, 6.3.8)'",
  "reference upright (bold II, roman 6.3.8)", "inside the italic statement: 6.3.8 italic, II bold italic",
  "convention", 6, "high",
  "(\\textbf{II}, 6.3.8)", "\\textup{(\\textbf{II}, 6.3.8)}"))
L.append(F(218, "heading 7.9",
  "'7.9. Anneaux excellents et résolution des singularités.' (final full stop)", "no full stop",
  "punctuation", None, "high",
  "résolution des singularités}", "résolution des singularités.}",
  "As the heading fixes of the earlier IV-2 batches (GLOBAL_ISSUES 43)."))
L.append(F(218, "(7.9.1), l. 3-4: 'on peut résoudre les singularités de X'",
  "'de' italic too", "\\emph{résoudre les singularités} de", "italics", None, "high",
  "\\emph{résoudre les singularités} de", "\\emph{résoudre les singularités de}"))
L.append(F(218, "(7.9.1), l. 4-5: 'si A est un anneau japonais de dimension 1'",
  "'anneau japonais de dimension' italic", "\\emph{anneau japonais} de dimension", "italics", None, "high",
  "\\emph{anneau japonais} de dimension", "\\emph{anneau japonais de dimension}"))
L.append(F(218, "(7.9.2), l. 3-4: 'un ouvert partout dense contenu dans Reg(X)'",
  "'partout dense' italic", "\\emph{partout} dense", "italics", None, "high",
  "\\emph{partout} dense", "\\emph{partout dense}"))
L.append(F(218, "(7.9.2), last line: 'alors les ouverts affines de X vérifient la condition (iii) de (7.8.2)'",
  "'vérifient' roman; 'la condition' italic; '(iii)' roman; 'de' italic", "\\emph{vérifient la condition} (iii) de",
  "italics", None, "high",
  "\\emph{vérifient\nla condition} (iii) de (7.8.2)", "vérifient\n\\emph{la condition} (iii) \\emph{de} (7.8.2)",
  "Two face changes in one edit."))

# ---------------------------------------------------------------- page 219
L.append(F(219, "proof of (7.9.3), 'Or, si a ...': 'les corps résiduels k(a)'",
  "bold italic k", "plain k", "convention", 1, "high",
  "résiduels $k(a)$", "résiduels $\\boldsymbol{k}(a)$"))
L.append(F(219, "proof of (7.9.3), 'Or, si a ...': 'et k(a') sont isomorphes'",
  "bold italic k", "plain k", "convention", 1, "high",
  "et $k(a')$ sont", "et $\\boldsymbol{k}(a')$ sont"))
L.append(F(219, "proof of (7.9.3): 'son complété (0, 17.1.5) l'est'",
  "bold 0", "plain 0", "convention", 2, "high",
  "(0, 17.1.5)", "(\\textbf{0}, 17.1.5)"))
L.append(F(219, "proof of Lemme (7.9.3.1), last sentence: 'Comme B^'' = lim (B''/n^hB'')'",
  "hat over B only, primes outside (B̂'')", "\\widehat{B''} (hat over B and both primes)",
  "formula", None, "high",
  "\\widehat{B''}", "\\widehat{B}''",
  "Same treatment as the Â' entry on p. 215."))
L.append(F(219, "Proposition (7.9.5), l. 3: 'vérifient les conditions (ii) et (iii) de (7.8.2);'",
  "the references (ii), (iii), (7.8.2) upright ('et', 'de' italic)", "italic", "convention", 6, "high",
  "conditions (ii) et (iii) de (7.8.2);", "conditions \\textup{(ii)} et \\textup{(iii)} de \\textup{(7.8.2)};",
  "Three occurrences in one edit."))
L.append(F(219, "end of the page: page break 219/220 inside the sentence '(5.6.3) (et | en particulier si X est ...'",
  "p. 220 begins 'en particulier si X est localement immersible dans un préschéma régulier (5.6.4)), X est un préschéma excellent (7.8.5).', continuing the sentence; no paragraph break",
  "blank line before \\oldpage[IV-2]{220}", "marker", None, "high",
  "(et\n\n", "(et\n",
  "APPLY BEFORE the next entry (both 'old' strings contain '(et'). OUTSIDE-SEGMENT COMPANION: the blank line AFTER the marker lies in p. 220's segment (page_220.tex: '\\oldpage[IV-2]{220}\\n\\nen particulier') and must be removed with this edit: old '\\oldpage[IV-2]{220}\\n\\nen particulier' -> new '\\oldpage[IV-2]{220}\\nen particulier'."))
L.append(F(219, "Proposition (7.9.5), last line: 'universellement caténaire (5.6.3) (et'",
  "'(5.6.3)' and '(et' upright (the parenthesis '(et en particulier si X est ...' continues upright on p. 220)",
  "italic", "convention", 6, "high",
  "caténaire (5.6.3) (et", "caténaire \\textup{(5.6.3) (et}",
  "APPLY AFTER the previous (marker) entry; its 'old' still matches then. The rest of the roman parenthesis ('en particulier si X est') is on p. 220."))

# ---------------------------------------------------------------- checks
def page_text(p):
    with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")

rel = open(REL, encoding="utf-8").read()
def rel_segment(p):
    a = rel.index("\\oldpage[IV-2]{%d}" % p)
    b = rel.index("\\oldpage[IV-2]{%d}" % (p + 1))
    return rel[a:b]

ok = True
spans = {}
for i, d in enumerate(L):
    fx = d["fix"]
    if not fx:
        continue
    t = page_text(d["page"])
    n = t.count(fx["old"])
    seg = rel_segment(d["page"])
    nr = seg.count(fx["old"])
    if n != 1 or nr != 1:
        ok = False
        print("COUNT PROBLEM", i, d["page"], repr(fx["old"]), "page:", n, "release segment:", nr)
    else:
        s = t.index(fx["old"])
        spans.setdefault(d["page"], []).append((s, s + len(fx["old"]), i))
for p, sp in spans.items():
    sp.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(sp, sp[1:]):
        if a2 < b1:
            print("OVERLAP page", p, "entries", i1, i2, repr(L[i1]["fix"]["old"]), repr(L[i2]["fix"]["old"]))

# outside-segment companions
t214 = page_text(214); t220 = page_text(220)
print("p214 companion count:", t214.count("soit excellent, il faut et\n\n"), "ends with it:", t214.endswith("soit excellent, il faut et\n\n"))
print("p220 companion count:", t220.count("\\oldpage[IV-2]{220}\n\nen particulier"))

from collections import Counter
c = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in range(215, 220):
    print(p, "normal", c[(p, "normal")], "convention", c[(p, "convention")], "misprint", c[(p, "misprint")])
print("all ok:", ok, "entries:", len(L))
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(L, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
