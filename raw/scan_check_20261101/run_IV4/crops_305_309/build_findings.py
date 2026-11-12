"""Build findings_305_309.json, check every "old" against page_NNN.tex, and dry-run the edits in order
on an in-memory copy of ega4-21c-fr.tex with the apply_fixes.py page logic (no file is modified)."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_IV4"
SRC = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-21c-fr.tex"
OUT = RUN / "findings_305_309.json"


def F(page, where, scan, tex, kind, old, new, note="", convention=None, confidence="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention, confidence=confidence,
             fix=None if old is None else dict(old=old, new=new))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


C7 = "long dash for set difference"
C7T = "minus sign"
L = []

# ---------------- p. 305 ----------------
L.append(F(305, "Proposition (21.12.2), l. 2: 'h : X'→X un morphisme plat ;'",
           "'plat' roman inside the italic statement (crop p305_plat.png)",
           "'plat' italic (proposition environment)", "convention",
           "un morphisme plat;", "un morphisme \\textup{plat};", convention=6))
L.append(F(305, "Proposition (21.12.2), l. 2: 'f' = f_(X') : U'→X''",
           "subscript (X') in round parentheses (crop p305_fX.png)",
           "f_{\\{X'\\}}: braces", "formula",
           "f'=f_{\\{X'\\}}:U'\\to X'", "f'=f_{(X')}:U'\\to X'",
           "The print's base-change notation with round parentheses, as elsewhere in § 21 (the TeX writes g_{(X')} in (21.5.8), p. 270). The same on p. 307."))
L.append(F(305, "second diagram (i_U, i_U', v^0), lower right corner: 'U'^0'",
           "no full stop after U'^0 (crop p305_diag2end.png)",
           "'U'^0.' with a full stop", "punctuation",
           "& U'^0.", "& U'^0"))

# ---------------- p. 306 ----------------
L.append(F(306, "display 'Daf(U/X) = f^0(U^0) — U'", C7, C7T, "convention",
           "=f^0(U^0)-U", "=f^0(U^0)\\setmin U", convention=7))
L.append(F(306, "second line after the display: 'l'ensemble fermé Z = X — U_1 est l'adhérence'", C7, C7T, "convention",
           "$Z=X-U_1$ est", "$Z=X\\setmin U_1$ est", convention=7))
L.append(F(306, "Théorème (21.12.6): item labels (i), (ii)",
           "labels upright (crop p306_thm_labels.png)",
           "enumerate labels italic inside the italic theorem", "convention",
           "\\begin{enumerate}[label=(\\roman*)]\n  \\item L'adhérence",
           "\\begin{enumerate}[label=\\textup{(\\roman*)}]\n  \\item L'adhérence",
           "GLOBAL_ISSUES 16; one edit covers both labels.", convention=6))
L.append(F(306, "Théorème (21.12.6) (i): 'L'adhérence Z = X — U_1 de Daf(U/X)'", C7, C7T, "convention",
           "$Z=X-U_1$ de", "$Z=X\\setmin U_1$ de", convention=7))
L.append(F(306, "Théorème (21.12.6) (ii): 'Si T = X — U ⊃ Z'", C7, C7T, "convention",
           "$T=X-U\\supset Z$", "$T=X\\setmin U\\supset Z$", convention=7))
L.append(F(306, "proof of (21.12.6) (i), l. 3: 'étant contenu dans Ū — U'", C7 + " (crop p306_UbarU.png)", C7T,
           "convention", "$\\overline U-U$", "$\\overline U\\setmin U$", convention=7))
L.append(F(306, "last line: 'appliqué suivant la méthode de (8.1.2, a)).'",
           "the label 'a)' italic, letter and parenthesis (crop p306_812a.png)",
           "plain upright 'a)'", "italics",
           "(8.1.2, a)).", "(8.1.2, \\emph{a)}).",
           "GLOBAL_ISSUES 88: the whole label italic in roman text."))

# ---------------- p. 307 ----------------
L.append(F(307, "proof of (21.12.6) (ii), l. 4: 'h : X' = Spec(A) → X, où A = Ô_X,x ;'",
           "'h : X'=Spec(A)→X, où A=𝒪̂_{X,x};' (crop p307_SpecA.png)",
           "'h:X'=Spec(𝒪̂_{X,x})→X;': the clause 'où A = 𝒪̂_{X,x}' is dropped and Spec(A) rewritten", "missing",
           "$h:X'=\\operatorname{Spec}(\\widehat{\\mathcal O}_{X,x})\\to X$;",
           "$h:X'=\\operatorname{Spec}(A)\\to X$, où $A=\\widehat{\\mathcal O}_{X,x}$;",
           "Rewording of the print (GLOBAL_ISSUES 46/102); the fix restores the printed sentence."))
L.append(F(307, "same sentence: 'f' = f_(X') est l'injection canonique'",
           "subscript (X') in round parentheses (crop p307_SpecA.png)",
           "f_{\\{X'\\}}: braces", "formula",
           "$f'=f_{\\{X'\\}}$ est", "$f'=f_{(X')}$ est", "As on p. 305."))
L.append(F(307, "l. 5: 'et puisque le morphisme h est plat, il résulte de (21.12.2)'",
           "'plat' italic (crop p307_plat.png)", "upright", "italics",
           "est plat, il résulte", "est \\emph{plat}, il résulte"))
L.append(F(307, "l. 10: 'T_1 = T ∩ X_1 = X_1 — U_1'", C7, C7T, "convention",
           "=X_1-U_1$", "=X_1\\setmin U_1$", convention=7))
L.append(F(307, "after the first diagram: 'i étant donc un morphisme affine ; on en déduit'",
           "'affine' italic (crop p307_affine.png)", "upright", "italics",
           "un morphisme affine; on en", "un morphisme \\emph{affine}; on en"))
L.append(F(307, "end of the proof of (21.12.6): 'donc le morphisme f^0 : U^0→X est fini ;'",
           "'fini' italic (crop p307_fini.png)", "upright", "italics",
           "est fini;", "est \\emph{fini};"))
L.append(F(307, "Corollaire (21.12.7), l. 3: 'supposons que j soit un morphisme affine.'",
           "'affine.' roman inside the italic statement (crop p307_cor7.png)",
           "italic (corollary environment)", "convention",
           "un morphisme\naffine. Alors", "un morphisme\n\\textup{affine}. Alors",
           "The parentheses of '(et par suite de codimension 1 si U est partout dense)' are italic in the print, "
           "as in the TeX (GLOBAL_ISSUES 101).", convention=6))
L.append(F(307, "Corollaire (21.12.7): 'T = X — U'", C7 + " (crop p307_cor7.png)", C7T, "convention",
           "$T=X-U$ est de", "$T=X\\setmin U$ est de", convention=7))

# ---------------- p. 308 ----------------
L.append(F(308, "(21.12.8), l. 1: 'Soient A un anneau local noethérien Y = Spec(A), y l'unique point'",
           "no comma after 'noethérien' (crop p308_noeth.png)",
           "'noethérien, Y=Spec(A)': silent correction", "misprint_in_print",
           "noethérien, $Y=\\operatorname{Spec}(A)$", "noethérien $Y=\\operatorname{Spec}(A)$",
           "Missing comma in the list of data. The TeX silently corrects; the fix restores the printed reading.",
           corrected="noethérien, $Y=\\operatorname{Spec}(A)$"))
L.append(F(308, "(21.12.8), l. 2: 'Y' = Y — {y}. Considérons'", C7, C7T, "convention",
           "$Y'=Y-\\{y\\}$. Considérons", "$Y'=Y\\setmin\\{y\\}$. Considérons", convention=7))
L.append(F(308, "(21.12.8): 'Cette condition est entraînée par la suivante :' after (W)",
           "indented new paragraph (page_308_s1.png)",
           "follows \\end{itemize} without a blank line: no indent", "other",
           "\\end{itemize}\nCette condition", "\\end{itemize}\n\nCette condition",
           "GLOBAL_ISSUES 80 pattern (text after a list loses the printed indent)."))
L.append(F(308, "(W'), l. 2: 'et tel que pour toute composante irréductible Y_i de Y'",
           "'tel' (page_308_s2.png)", "'tel': keeps the printed reading", "misprint_in_print",
           None, None,
           "Agreement slip: the adjective refers to 'partie fermée T' (feminine), coordinated with "
           "'dont toute composante ...'. The TeX keeps the printed reading (fix null). Medium: the authors may "
           "have thought of 'un fermé T'.",
           confidence="medium", corrected="et telle que pour toute composante"))
L.append(F(308, "(W'): 'l'ouvert U = Y — T est affine'", C7, C7T, "convention",
           "$U=Y-T$", "$U=Y\\setmin T$", convention=7))
L.append(F(308, "(21.12.8): 'En effet, si (W') est vérifiée' after (W')",
           "indented new paragraph (page_308_s2.png)",
           "follows \\end{itemize} without a blank line: no indent", "other",
           "\\end{itemize}\nEn effet, si (W')", "\\end{itemize}\n\nEn effet, si (W')",
           "GLOBAL_ISSUES 80 pattern."))
L.append(F(308, "(21.12.8): 'composante irréductible de T = Y — U'", C7, C7T, "convention",
           "$T=Y-U$", "$T=Y\\setmin U$", convention=7))
L.append(F(308, "(21.12.8): 'les composantes irréductibles Y_i — {y} de Y''", C7, C7T, "convention",
           "$Y_i-\\{y\\}$", "$Y_i\\setmin\\{y\\}$", convention=7))
L.append(F(308, "(W''): 'Y — T est un ouvert affine'", C7, C7T, "convention",
           "$Y-T$ est un ouvert affine", "$Y\\setmin T$ est un ouvert affine", convention=7))
L.append(F(308, "(21.12.8): 'En effet, il est clair que (W') entraîne (W'')' after (W'')",
           "indented new paragraph (page_308_s2.png)",
           "follows \\end{itemize} without a blank line: no indent", "other",
           "\\end{itemize}\nEn effet, il est clair", "\\end{itemize}\n\nEn effet, il est clair",
           "GLOBAL_ISSUES 80 pattern."))
L.append(F(308, "heading of (21.12.9): 'Exemples (21.12.9). — Si A est ...'",
           "examples heading, 'Exemples' italic before the number (crop p308_exemples.png)",
           "\\begin{env}[21.12.9] with a hand-made '\\emph{Exemples}. ---': prints '(21.12.9) Exemples. —'", "other",
           "\\begin{env}[21.12.9]\n\\label{IV.21.12.9}\n\\emph{Exemples}. ---\nSi $A$",
           "\\begin{examples}[21.12.9]\n\\label{IV.21.12.9}\nSi $A$",
           "Part 1 of 2: the preamble's examples environment, as the print shows. Apply together with the "
           "'\\end{examples}' entry below (same environment)."))
L.append(F(308, "(21.12.9), l. 3: 'non factoriels vérifiant (W'), par exemple ceux de dimension ⩽ 1'",
           "(W') with one prime (crop p308_Wprime_zoom.png; compare the label (W'') in p308_Wsecond_zoom.png)",
           "(W'')", "symbol",
           "vérifiant (W''),", "vérifiant (W'),",
           "The print's (W') is sound (rings of dimension ⩽ 1: every open set affine), so not a misprint; "
           "the TeX's (W'') is a change. No erratum."))
L.append(F(308, "end of (21.12.9): '... de dimension 2 vérifie (W').' (end of the environment)",
           "see the heading entry above", "\\end{env}", "other",
           "(W').\n\\end{env}", "(W').\n\\end{examples}",
           "Part 2 of 2: apply together with the heading entry above."))
L.append(F(308, "Proposition (21.12.10), l. 2: 'Y' = Y — {y}, X' = g^{-1}(Y')'", C7, C7T, "convention",
           "$Y'=Y-\\{y\\}$, $X'=g^{-1}(Y')$", "$Y'=Y\\setmin\\{y\\}$, $X'=g^{-1}(Y')$", convention=7))
L.append(F(308, "Proposition (21.12.10), l. 4: 'vérifie la condition (W) (21.12.8).'",
           "'(W)' and '(21.12.8)' upright with upright parentheses (crop p308_prop10.png)",
           "italic (proposition environment)", "convention",
           "condition (W) (21.12.8). Alors, pour", "condition \\textup{(W) (21.12.8)}. Alors, pour",
           convention=6))
L.append(F(308, "Proposition (21.12.10), l. 4: 'X_y = g^{-1}(y), ou bien Z est de codimension'",
           "'ou bien' roman (crop p308_prop10.png)", "italic (proposition environment)", "convention",
           "ou bien $Z$ est de codimension", "\\textup{ou bien} $Z$ est de codimension", convention=6))
L.append(F(308, "Proposition (21.12.10), l. 5: 'dans X, ou bien son point générique est isolé dans Z'",
           "'ou bien' roman (crop p308_prop10.png)", "italic (proposition environment)", "convention",
           "ou bien son point générique", "\\textup{ou bien} son point générique", convention=6))
L.append(F(308, "Proposition (21.12.10), l. 6: 'de type fini sur k(y)'",
           "bold italic k (page_308_s3.png)", "plain k", "convention",
           "$k(y)$, la seconde", "$\\boldsymbol{k}(y)$, la seconde", convention=1))

# ---------------- p. 309 ----------------
L.append(F(309, "l. 2: 'X_y = Z irréductible, non réduit à un point et telle que'",
           "'irréductible, non réduit à un point' italic (page_309_s1.png)", "upright", "italics",
           "$X_y=Z$ irréductible, non réduit à un point et",
           "$X_y=Z$ \\emph{irréductible, non réduit à un point} et"))
L.append(F(309, "l. 3: 'L'image g(X — X_y) = U'", C7, C7T, "convention",
           "$g(X-X_y)=U$", "$g(X\\setmin X_y)=U$", convention=7))
L.append(F(309, "l. 4: 'isomorphe à X — X_y par hypothèse'", C7, C7T, "convention",
           "isomorphe à $X-X_y$", "isomorphe à $X\\setmin X_y$", convention=7))
L.append(F(309, "l. 6: 'dont l'adhérence contient y. En effet, on peut tout d'abord'",
           "no paragraph break: 'En effet' follows on the same line (page_309_s1.png)",
           "blank line: new paragraph", "extra",
           "contient $y$.\n\nEn effet, on peut", "contient $y$.\nEn effet, on peut"))
L.append(F(309, "l. 13: 'Remplaçant X par X' = X — ∪_i T_i'", C7, C7T, "convention",
           "$X'=X-\\bigcup_iT_i$", "$X'=X\\setmin\\bigcup_iT_i$", convention=7))
L.append(F(309, "l. 14: 'l'image par g de X' — X'_y': the dash", C7 + " (crop p309_XprimeXy.png)", C7T, "convention",
           "de $X'-X", "de $X'\\setmin X",
           "Independent of the next entry (adjacent, no overlap).", convention=7))
L.append(F(309, "l. 14: 'l'image par g de X' — X'_y ne contient pas les images g(t_i)'",
           "X'_y with a prime (crop p309_XprimeXy.png)", "X_y (prime missing)", "formula",
           "_y$ ne contient pas les images", "'_y$ ne contient pas les images",
           "Inserts the prime of X'_y (the fibre of the new X'). Independent of the previous entry."))
L.append(F(309, "l. 15: 'dont l'adhérence contient y. Cela étant, comme X et Y sont affines'",
           "no paragraph break: 'Cela étant' follows on the same line (page_309_s2.png)",
           "blank line: new paragraph", "extra",
           "contient $y$.\n\nCela étant", "contient $y$.\nCela étant"))
L.append(F(309, "l. 18: 'Y'_1 = Y_1 — {y} = Y' ∩ Y_1'", C7, C7T, "convention",
           "$Y'_1=Y_1-\\{y\\}", "$Y'_1=Y_1\\setmin\\{y\\}", convention=7))
L.append(F(309, "l. 22: 'appliqué suivant la méthode de (8.1.2, a)) qu'en restreignant'",
           "the label 'a)' italic (crop p309_812a.png)", "plain upright 'a)'", "italics",
           "(8.1.2, a)) qu'en", "(8.1.2, \\emph{a)}) qu'en", "GLOBAL_ISSUES 88."))
L.append(F(309, "l. 24: 'l'ouvert X — X_y de X, isomorphe à U'", C7, C7T, "convention",
           "l'ouvert $X-X_y$", "l'ouvert $X\\setmin X_y$", convention=7))
L.append(F(309, "Corollaire (21.12.11), l. 4: 'vérifie la condition (W) (21.12.8).'",
           "'(W)' and '(21.12.8)' upright with upright parentheses (crop p309_cor11.png)",
           "italic (corollary environment)", "convention",
           "condition (W) (21.12.8). Alors toute", "condition \\textup{(W) (21.12.8)}. Alors toute",
           convention=6))
L.append(F(309, "Corollaire (21.12.11), l. 5: 'T = X — V'", C7, C7T, "convention",
           "$T=X-V$", "$T=X\\setmin V$", convention=7))
L.append(F(309, "Corollaire (21.12.11), l. 5: 'est, ou bien de codimension ⩽ 1'",
           "'ou bien' roman (crop p309_cor11.png)", "italic (corollary environment)", "convention",
           "est, ou bien\nde codimension", "est, \\textup{ou bien}\nde codimension", convention=6))
L.append(F(309, "Corollaire (21.12.11), l. 5: ', ou bien telle que son point générique z'",
           "'ou bien' roman (crop p309_cor11.png)", "italic (corollary environment)", "convention",
           "ou bien telle que", "\\textup{ou bien} telle que", convention=6))
L.append(F(309, "proof of (21.12.11), l. 1: 'ne dépendant que de la fibre g^{-1}(y) et de l'anneau O_X,z ,'",
           "𝒪_{X,z} (crop p309_Oxz.png)", "𝒪_{Y,y}", "formula",
           "l'anneau\n$\\mathcal O_{Y,y}$, on peut", "l'anneau\n$\\mathcal O_{X,z}$, on peut",
           "The print's reading is sound (the codimension of the component is dim O_X,z; base change to "
           "Spec(O_Y,y) keeps the fibre and O_X,z), so not a misprint: the TeX's O_Y,y is a rewording "
           "(GLOBAL_ISSUES 102). No erratum."))
L.append(F(309, "proof of (21.12.11), l. 2: 'on peut par changement de base, se borner au cas où'",
           "comma after 'base' (crop p309_Oxz.png)", "no comma", "punctuation",
           "changement de base se borner", "changement de base, se borner"))
L.append(F(309, "proof of (21.12.11): 'Le morphisme g peut donc être supposé séparé'",
           "'séparé' italic (crop p309_end.png)", "upright", "italics",
           "supposé\nséparé et", "supposé\n\\emph{séparé} et"))
L.append(F(309, "proof of (21.12.11): 'que g|V : V→Y est une immersion ouverte. La'",
           "'immersion ouverte' italic (crop p309_end.png)", "upright", "italics",
           "est une immersion ouverte. La restriction", "est une \\emph{immersion ouverte}. La restriction"))
L.append(F(309, "proof of (21.12.11): '{y} = Spec(k(y))'",
           "bold italic k (crop p309_end.png)", "plain k", "convention",
           "\\operatorname{Spec}(k(y))", "\\operatorname{Spec}(\\boldsymbol{k}(y))", convention=1))
L.append(F(309, "page break 308/309: printed p. 308 ends with 'Supposons qu'il existe dans X_y ... "
           "codim(Z, X) ⩾ 2. La question étant locale'; p. 309 begins 'sur X et Y puisque z est non isolé'",
           "page_308_s4.png ends with 'et telle que codim(Z, X)⩾2. La question étant locale' (page number 308 "
           "below); page_309_s1.png begins with 'sur X et Y puisque z est non isolé dans Z'",
           "\\oldpage[IV-4]{309} stands before 'Supposons qu'il existe', two printed lines too early", "marker",
           "\\oldpage[IV-4]{309}\nSupposons qu'il existe", "Supposons qu'il existe",
           "Boundary 308/309. Marker move, part 1 of 2: removes the marker (the blank line before 'Supposons' "
           "stays: new paragraph in the print). Apply after all other p. 309 entries and together with the "
           "next entry. The two lines it moves to p. 308 have no other differences."))
L.append(F(309, "page break 308/309: new position of \\oldpage[IV-4]{309}",
           "p. 309 begins with 'sur X et Y puisque z est non isolé dans Z'",
           "(marker earlier, see the entry above)", "marker",
           "La question étant locale sur $X$ et $Y$", "La question étant locale\n\\oldpage[IV-4]{309}\nsur $X$ et $Y$",
           "Marker move, part 2 of 2: mid-sentence break, no blank lines. Apply right after the entry above."))

# ---------------- checks ----------------
pages = {}
for n in range(305, 310):
    t = (RUN / f"page_{n}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    pages[n] = t
bad = 0
for x in L:
    fx = x["fix"]
    if fx is None:
        continue
    c = pages[x["page"]].count(fx["old"])
    if c != 1:
        print("PAGE-FILE COUNT", c, x["page"], repr(fx["old"]))
        bad += 1

# dry run with the apply_fixes.py locate() logic on an in-memory copy of the source
src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


t = src
for x in L:
    fx = x["fix"]
    if fx is None:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        print("DRY-RUN COUNT", c, x["page"], repr(fx["old"]))
        bad += 1
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]

json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("entries", len(L), "problems", bad)
from collections import Counter
cnt = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(305, 310):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
# show the edited segments 308-309 for a visual check
s0 = t.index("\\oldpage[IV-4]{308}")
s1 = t.index("\\oldpage[IV-4]{310}")
(RUN / "crops_305_309" / "dryrun_308_309.tex").write_text(t[s0:s1], encoding="utf-8")
s0 = t.index("\\oldpage[IV-4]{305}")
s1 = t.index("\\oldpage[IV-4]{308}")
(RUN / "crops_305_309" / "dryrun_305_307.tex").write_text(t[s0:s1], encoding="utf-8")
