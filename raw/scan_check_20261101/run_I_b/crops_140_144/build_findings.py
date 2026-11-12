"""Build findings_140_144.json; check that every fix 'old' occurs exactly once on its page
and that the fixes apply in list order."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
OUT = RUN / "findings_140_144.json"
NL = "\n"

P_NOTE = (r"The print sets the property letter P in bold italic throughout, also in roman text. "
          r"\textbf{P} gives a bold upright P in roman text; here it is italic only because the remark "
          r"environment is wrongly italic (see the remark finding), and it turns bold upright once the remark "
          r"is set roman. \textbf{\textit{P}} is bold italic in either case.")
P_SHORT = "Bold italic P in roman prose; see the first P finding on this page."
CONT = (r"In the page-140 continuation (ega1-6-fr.tex, before \oldpage[I]{141}); apply_fixes.py searches only "
        r"ega1-5-fr.tex for p. 140, so this edit lands in the manual list.")
LAB = "Labels a), b), c), ... are italic in the roman proof text of the print; the TeX sets them roman."
C6_RESP = "'resp.' roman in the print inside the italic statement; italic in the TeX environment."


def F(page, where, scan, tex, kind, conf, old, new, note=None, conv=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if old is not None else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def C2(page, where, old, new, num):
    return F(page, where, f"(0, {num}) with the chapter number 0 in bold", old, "convention", "high",
             old, new, None, 2)


def C6(page, where, scan, tex, old, new, note):
    return F(page, where, scan, tex, "convention", "high", old, new, note, 6)


def P(where, old, first=False):
    return F(140, where, "bold italic P", old, "font", "high", old,
             old.replace(r"\textbf{P}", r"\textbf{\textit{P}}"), P_NOTE if first else P_SHORT)


findings = [
    # ---------------------------------------------------------------- page 140
    F(140, "Remarque (5.5.12), its continuation on p. 140: statements (iv)-(vi), the two following paragraphs, "
           "the paragraph 'Enfin, considérons ...', and (i'), (v')",
      "remark body in roman; the statements (iv), (v), (vi), (i'), (v') and the words 'équivalentes', "
      "'conséquences' in italics",
      r"\begin{remark}[5.5.12] (opened on p. 139) ... \item[\rm(iv)] \emph{Si ...} ... sont \emph{équivalentes} "
      r"... des \emph{conséquences} ... \item[\rm(v')] \emph{Si ...} ... \end{remark}",
      "font", "high", None, None,
      r"The remark environment is \itshape (EGA_FR.tex), so the TeX sets this remark's roman prose in italics "
      r"and its \emph statements and words upright: the reverse of the print (GLOBAL_ISSUES item 2). "
      r"Environment-level fix, not a page edit. Until then the \textbf{P} inside the \emph statements also "
      r"comes out bold upright; once the remark is roman they come out bold italic as printed, and the seven "
      r"\textbf{P} of the prose turn bold upright (next seven findings)."),
    P("proof in Remarque (5.5.12): 'si g∘f possède la propriété P, il en est de même de p_2'",
      r"\textbf{P}, il en est de même de $p_2$", first=True),
    P("proof: 'donc possède aussi la propriété P par (i)'", r"aussi la propriété \textbf{P} par"),
    P("proof: 'enfin, en vertu de (ii), f possède la propriété P.'",
      r"(ii), $f$ possède la propriété \textbf{P}"),
    P("'où les flèches verticales ... donc possèdent la propriété P par (i)'",
      r"possèdent la propriété \textbf{P}"),
    P("'L'hypothèse que f possède la propriété P entraîne donc'", r"\textbf{P} entraîne"),
    P("'X_red → Y_red → Y possède la propriété P ; enfin'", r"\textbf{P}~; enfin"),
    P("'f_red possède la propriété P en vertu de (v)'", r"\textbf{P} en vertu de (v)"),
    C6(140, "(vi): 'il en est de même de f_red (5.1.5).'",
       "(5.1.5) upright inside the italic statement",
       r"(\hyperref[I.5.1.5-fr]{5.1.5}).}",
       r"(\hyperref[I.5.1.5-fr]{5.1.5}).}", r"\textup{(\hyperref[I.5.1.5-fr]{5.1.5})}.}",
       r"Reference printed upright inside the italic statement. Inside the remark the \emph currently "
       r"renders upright (remark finding); \textup keeps the reference upright once the environment is fixed."),
    C6(140, "Définition (6.1.1): 'On dit qu'un préschéma X est noethérien'",
       "'noethérien' in italics like the rest of the definition (no change of face)",
       r"\emph{noethérien}", r"\emph{noethérien}", r"noethérien",
       r"\emph inside the italic definition environment sets the word upright; drop the \emph. " + CONT),
    C6(140, "Définition (6.1.1): '(resp. localement noethérien)'",
       "'(resp.' roman inside the italic statement",
       r"(resp. \emph{localement" + NL + r"noethérien})",
       r"(resp. \emph{localement", r"\textup{(resp.} \emph{localement",
       C6_RESP + " Apply before the next finding (same phrase). " + CONT),
    C6(140, "Définition (6.1.1): '(resp. localement noethérien)'",
       "'localement noethérien' in italics like the rest of the definition (no change of face)",
       r"\emph{localement" + NL + r"noethérien}",
       r"\emph{localement" + NL + r"noethérien}", r"localement" + NL + r"noethérien",
       r"\emph inside the italic definition environment sets the words upright; drop the \emph. " + CONT),
    C6(140, "Définition (6.1.1): 's'il est réunion finie (resp. réunion)'",
       "'(resp.' roman inside the italic statement",
       r"(resp. réunion)", r"(resp. réunion)", r"\textup{(resp.} réunion)", C6_RESP + " " + CONT),
    F(140, "last line: 'la question étant locale. Tout sous-𝒪_X-'",
      "'Tout' in roman; only 'sous-𝒪_X-' (continued 'Module' on p. 141) in italics",
      r"\emph{Tout" + NL + r"sous-$\mathscr{O}_X$-}", "italics", "high",
      r"\emph{Tout" + NL + r"sous-$\mathscr{O}_X$-}", r"Tout" + NL + r"\emph{sous-$\mathscr{O}_X$-}",
      "Checked on a crop. " + CONT),
    # ---------------------------------------------------------------- page 141
    F(141, "first line: 'Module (resp. tout 𝒪_X-Module quotient) quasi-cohérent'",
      "Module, 'tout 𝒪_X-Module quotient' and 'quasi-cohérent' in italics; '(resp.' and the closing "
      "parenthesis in roman",
      r"\emph{Module (resp. tout $\mathscr{O}_X$-Module quotient) quasi-cohérent}", "italics", "high",
      r"\emph{Module (resp. tout $\mathscr{O}_X$-Module quotient) quasi-cohérent}",
      r"\emph{Module} (resp. \emph{tout $\mathscr{O}_X$-Module quotient}) \emph{quasi-cohérent}",
      "Checked on a crop. The TeX's single \\emph also italicises '(resp.' and the parenthesis."),
    F(141, "'Plus particulièrement, tout faisceau d'idéaux quasi-cohérent de 𝒪_X est cohérent.'",
      "'tout' in roman; 'faisceau d'idéaux quasi-cohérent' in italics",
      r"\emph{tout faisceau d'idéaux" + NL + r"quasi-cohérent}", "italics", "high",
      r"\emph{tout faisceau d'idéaux", r"tout \emph{faisceau d'idéaux", "Checked on a crop."),
    F(141, "the proofs of (6.1.2), (6.1.3) and (6.1.4) (the last continues on p. 142)",
      "no heading: each proof starts as an ordinary indented paragraph ('La première assertion découle ...', "
      "'L'équivalence de a) et b) ...', 'Il suffit de faire la démonstration ...')",
      r"\begin{proof} (three times)", "extra", "high", None, None,
      r"EGA_FR.tex defines proof as \textit{Démonstration. ---\ } + body, so the TeX adds 'Démonstration. —' "
      r"three times on this page. Environment-level fix (same pattern as GLOBAL_ISSUES item 10 for lemma); the "
      r"proof environment occurs 61 times in ega1-6/7/9/10-fr.tex."),
    C2(141, "proof of (6.1.2): 'tout espace réunion finie de sous-espaces noethériens est noethérien (0, 2.2.3)'",
       r"{0, 2.2.3}", r"{\textbf{0}, 2.2.3}", "2.2.3"),
    C6(141, "Proposition (6.1.3), statement: 'équivalentes : a) X est noethérien'",
       "label a) roman inside the italic statement", r"a) $X$ est noethérien",
       r"a) $X$ est noethérien", r"\textup{a)} $X$ est noethérien",
       "Labels a), b), c) are roman in the print (checked on a crop); italic in the TeX environment."),
    C6(141, "Proposition (6.1.3), statement: 'b) X est localement noethérien'",
       "label b) roman inside the italic statement", r"b) $X$ est localement",
       r"b) $X$ est localement", r"\textup{b)} $X$ est localement", None),
    C6(141, "Proposition (6.1.3), statement: 'c) A est noethérien.'",
       "label c) roman inside the italic statement", r"c) $A$ est noethérien",
       r"c) $A$ est noethérien", r"\textup{c)} $A$ est noethérien", None),
    F(141, "proof of (6.1.3): 'L'équivalence de a) et b) résulte de (6.1.2)'", "a) and b) in italics",
      r"L'équivalence de a) et b)", "italics", "high",
      r"L'équivalence de a) et b)", r"L'équivalence de \emph{a)} et \emph{b)}", LAB + " Checked on a crop."),
    F(141, "proof of (6.1.3): 'il est clair en outre que c) entraîne a).'", "c) and a) in italics",
      r"que c) entraîne a)", "italics", "high",
      r"que c) entraîne a)", r"que \emph{c)} entraîne \emph{a)}", LAB),
    F(141, "proof of (6.1.3): 'Pour voir que a) entraîne c)'", "a) and c) in italics",
      r"que a) entraîne c)", "italics", "high",
      r"que a) entraîne c)", r"que \emph{a)} entraîne \emph{c)}", LAB),
    F(141, "proof of (6.1.3): 'de faisceaux d'idéaux dans Ã=𝒪_X ;'",
      "Ã=𝒪_X with an ordinary equals sign (two bars)",
      r"$\widetilde{A}\equiv\mathscr{O}_X$", "symbol", "high",
      r"\widetilde{A}\equiv\mathscr{O}_X", r"\widetilde{A}=\mathscr{O}_X",
      "Checked on a crop at 3x: two bars, not the three-bar ≡."),
    C2(141, "proof of (6.1.3): 'par l'injection canonique V_i→X (0, 5.1.4)'",
       r"{0, 5.1.4}", r"{\textbf{0}, 5.1.4}", "5.1.4"),
    C6(141, "Proposition (6.1.4), statement: 'd'un préschéma noethérien (resp. localement noethérien)'",
       "'(resp.' roman inside the italic statement", r"d'un préschéma noethérien (resp. localement noethérien)",
       r"d'un préschéma noethérien (resp.", r"d'un préschéma noethérien \textup{(resp.}", C6_RESP),
    C6(141, "Proposition (6.1.4), statement: 'est noethérien (resp. localement noethérien).'",
       "'(resp.' roman inside the italic statement", r"est noethérien (resp. localement noethérien).",
       r"est noethérien (resp. localement noethérien).",
       r"est noethérien \textup{(resp.} localement noethérien).", C6_RESP),
    # ---------------------------------------------------------------- page 142
    F(142, "proof of (6.1.6): 'il existe des entiers n_i tels que (𝒩_X|U_i)^{n_i}=0'",
      "exponent printed 'ni' on one level: the i is not lowered as a second-order index",
      r"$(\mathscr{N}_X|U_i)^{n_i}=0$", "misprint_in_print", "medium",
      r"U_i)^{n_i}", r"U_i)^{ni}",
      "The TeX silently corrects the print. Checked on a crop at 3x: n and i have the same size and "
      "baseline. Elsewhere the print lowers second-order indices (p. 91: (fg_i)^{n_i}t, A_{g_i}), so this "
      "flat setting is a typesetting slip; the same slip occurs twice on p. 144 (𝒪_{xi}, A(Z_j)_{gj}).",
      corrected=r"(\mathscr{N}_X|U_i)^{n_i}=0"),
    C2(142, "proof of (6.1.8): 'qui ne contiennent pas x (0, 2.1.6). Soit alors W'",
       r"{0, 2.1.6}). Soit alors", r"{\textbf{0}, 2.1.6}). Soit alors", "2.1.6"),
    C2(142, "proof of (6.1.8): 'qui rencontrent W (0, 2.1.6), donc ces composantes'",
       r"{0, 2.1.6}), donc ces", r"{\textbf{0}, 2.1.6}), donc ces", "2.1.6"),
    C6(142, "Proposition (6.1.10), item a)", "label a) roman inside the italic statement", r"\item[a)]",
       r"\item[a)]", r"\item[\textup{a)}]",
       "Labels a)-e) are roman in the print (checked on a crop); \\item[a)] takes the italic of the "
       "proposition environment. (On p. 144 the labels of (6.2.2) are italic in the print.)"),
    C6(142, "Proposition (6.1.10), item b)", "label b) roman", r"\item[b)]",
       r"\item[b)]", r"\item[\textup{b)}]", None),
    C6(142, "Proposition (6.1.10), item c)", "label c) roman", r"\item[c)]",
       r"\item[c)]", r"\item[\textup{c)}]", None),
    C6(142, "Proposition (6.1.10), item d)", "label d) roman", r"\item[d)]",
       r"\item[d)]", r"\item[\textup{d)}]", None),
    C6(142, "Proposition (6.1.10), item e)", "label e) roman", r"\item[e)]",
       r"\item[e)]", r"\item[\textup{e)}]", None),
    F(142, "proof of (6.1.10): 'Il est immédiat que a) entraîne b)'", "a) and b) in italics",
      r"que a) entraîne b)", "italics", "high", r"que a) entraîne b)", r"que \emph{a)} entraîne \emph{b)}", LAB),
    F(142, "proof of (6.1.10): 'et a) entraîne que les composantes irréductibles'", "a) in italics",
      r"et" + NL + r"a) entraîne que", "italics", "high",
      r"et" + NL + r"a) entraîne que", r"et" + NL + r"\emph{a)} entraîne que", LAB),
    F(142, "proof of (6.1.10): 'Il est trivial que b) entraîne c)'", "b) and c) in italics",
      r"que b) entraîne c)", "italics", "high", r"que b) entraîne c)", r"que \emph{b)} entraîne \emph{c)}", LAB),
    # ---------------------------------------------------------------- page 143
    F(143, "proof of (6.1.10): 'par suite c) entraîne b).'", "c) and b) in italics",
      r"par suite c) entraîne b)", "italics", "high",
      r"par suite c) entraîne b)", r"par suite \emph{c)} entraîne \emph{b)}", LAB),
    F(143, "proof of (6.1.10): 'On en conclut aussitôt que c) entraîne d)'", "c) and d) in italics",
      r"que c)" + NL + r"entraîne d)", "italics", "high",
      r"que c)" + NL + r"entraîne d)", r"que \emph{c)}" + NL + r"entraîne \emph{d)}", LAB),
    F(143, "proof of (6.1.10): 'montrons que d) entraîne a) :'", "d) and a) in italics",
      r"que d) entraîne" + NL + r"a)", "italics", "high",
      r"que d) entraîne" + NL + r"a)", r"que \emph{d)} entraîne" + NL + r"\emph{a)}", LAB),
    C2(143, "proof of (6.1.10): 'en vertu de (0, 2.1.6), on peut se borner au cas'",
       r"{0, 2.1.6}), on peut", r"{\textbf{0}, 2.1.6}), on peut", "2.1.6"),
    F(143, "proof of (6.1.10): 'Enfin l'équivalence de d) et e)'", "d) and e) in italics",
      r"l'équivalence de d) et e)", "italics", "high",
      r"l'équivalence de d) et e)", r"l'équivalence de \emph{d)} et \emph{e)}", LAB),
    C2(143, "proof of (6.1.10): 'est affine en vertu de (0, 2.1.6) ; dire que x'",
       r"{0, 2.1.6})~; dire", r"{\textbf{0}, 2.1.6})~; dire", "2.1.6"),
    C6(143, "Proposition (6.1.13), statement: 'soit premier (resp. que 𝒪_x soit réduit'",
       "'(resp.' roman inside the italic statement", r"premier (resp. que",
       r"premier (resp. que", r"premier \textup{(resp.} que", C6_RESP),
    C6(143, "Proposition (6.1.13), statement: 'soit réduit, resp. intègre) ; alors'",
       "'resp.' roman inside the italic statement", r"réduit, resp. intègre)~;",
       r"réduit, resp. intègre)~;", r"réduit, \textup{resp.} intègre)~;", C6_RESP),
    C6(143, "Proposition (6.1.13), statement: 'qui est irréductible (resp. réduit'",
       "'(resp.' roman inside the italic statement", r"irréductible (resp. réduit",
       r"irréductible (resp. réduit", r"irréductible \textup{(resp.} réduit", C6_RESP),
    C6(143, "Proposition (6.1.13), statement: '(resp. réduit, resp. intègre).'",
       "'resp.' roman inside the italic statement", r"réduit, resp. intègre).",
       r"réduit, resp. intègre).", r"réduit, \textup{resp.} intègre).", C6_RESP),
    C2(143, "proof of (6.1.13): 'contenu dans Y, donc irréductible (0, 2.1.6). Si 𝒩_x=0'",
       r"{0, 2.1.6}). Si", r"{\textbf{0}, 2.1.6}). Si", "2.1.6"),
    C2(143, "proof of (6.1.13): 'la conclusion résulte de (0, 5.2.2).'",
       r"{0, 5.2.2}", r"{\textbf{0}, 5.2.2}", "5.2.2"),
    C6(143, "Définition (6.2.1): 'On dit qu'un préschéma est artinien'",
       "'artinien' in italics like the rest of the definition (no change of face)", r"\emph{artinien}",
       r"\emph{artinien}", r"artinien",
       r"\emph inside the italic definition environment sets the word upright; drop the \emph."),
    # ---------------------------------------------------------------- page 144
    C6(144, "Proposition (6.2.2), item c): 'sont fermés (condition T_1).'",
       "'(condition T_1)' roman inside the italic statement", r"(condition $\mathrm{T}_1$)",
       r"(condition $\mathrm{T}_1$)", r"\textup{(condition $\mathrm{T}_1$)}",
       "Checked on a crop. (The labels a), b), c) of this proposition are italic in the print, as in the TeX.)"),
    F(144, "proof of (6.2.2): 'On sait que a) entraîne la dernière assertion'", "a) in italics",
      r"On sait que a) entraîne", "italics", "high",
      r"On sait que a) entraîne", r"On sait que \emph{a)} entraîne", LAB),
    F(144, "proof of (6.2.2): 'a) entraîne donc b) et b) entraîne évidemment c).'", "a), b), b), c) in italics",
      r"a) entraîne donc b) et b) entraîne évidemment c)", "italics", "high",
      r"a) entraîne donc b) et b) entraîne évidemment c)",
      r"\emph{a)} entraîne donc \emph{b)} et \emph{b)} entraîne évidemment \emph{c)}", LAB),
    F(144, "proof of (6.2.2): 'Pour voir que c) entraîne a)'", "c) and a) in italics",
      r"que c) entraîne a)", "italics", "high", r"que c) entraîne a)", r"que \emph{c)} entraîne \emph{a)}", LAB),
    F(144, "proof of (6.2.2): 'et les anneaux locaux 𝒪_{x_i}=A_i sont artiniens'",
      "subscript printed 'xi' on one level: the i is not lowered as a second-order index",
      r"$\mathscr{O}_{x_i}=A_i$", "misprint_in_print", "medium",
      r"\mathscr{O}_{x_i}", r"\mathscr{O}_{xi}",
      "The TeX silently corrects the print. Checked on a crop at 3x: x and i have the same size and "
      "baseline. Same typesetting slip as (𝒩_X|U_i)^{ni} on p. 142 and A(Z_j)_{gj} below; the print "
      "normally lowers second-order indices (p. 91).",
      corrected=r"\mathscr{O}_{x_i}=A_i"),
    C6(144, "Définition (6.3.1): 'est de type fini si Y est réunion'",
       "'de type fini' in italics like the rest of the definition (no change of face)", r"\emph{de type fini}",
       r"\emph{de type fini}", r"de type fini",
       r"\emph inside the italic definition environment sets the words upright; drop the \emph."),
    C6(144, "Définition (6.3.1), condition (P): label '(P)'",
       "label (P) roman inside the italic statement", r"\item[(P)]",
       r"\item[(P)]", r"\item[\textup{(P)}]", "Checked on a crop; \\item[(P)] takes the italic of the environment."),
    C6(144, "Proposition (6.3.2), statement: 'possède la propriété (P) de la déf. (6.3.1).'",
       "(P) roman inside the italic statement ('de la déf.' italic)", r"la propriété (P) de la déf.",
       r"la propriété (P) de la déf.", r"la propriété \textup{(P)} de la déf.", None),
    C6(144, "Proposition (6.3.2), statement: 'de la déf. (6.3.1).'",
       "(6.3.1) upright inside the italic statement", r"(\hyperref[I.6.3.1-fr]{6.3.1})",
       r"(\hyperref[I.6.3.1-fr]{6.3.1})", r"\textup{(\hyperref[I.6.3.1-fr]{6.3.1})}",
       "Reference printed upright inside the italic statement; italic in the TeX environment."),
    C6(144, "Lemme (6.3.2.1), statement: 'un ouvert affine, possédant la propriété (P), alors'",
       "(P) roman inside the italic statement", r"possédant la propriété (P)",
       r"possédant la propriété (P)", r"possédant la propriété \textup{(P)}", None),
    C6(144, "Lemme (6.3.2.1), statement: 'D(g) possède la propriété (P).'",
       "(P) roman inside the italic statement", r"$D(g)$ possède la propriété (P)",
       r"$D(g)$ possède la propriété (P)", r"$D(g)$ possède la propriété \textup{(P)}", None),
    F(144, "proof of (6.3.2.1): 'Or, A(D(g_j))=A(Z_j)_{g_j}=A(Z_j)[1/g_j]'",
      "subscript of A(Z_j) printed 'gj' on one level: the j is not lowered as a second-order index",
      r"A(Z_j)_{g_j}", "misprint_in_print", "medium",
      r"A(Z_j)_{g_j}", r"A(Z_j)_{gj}",
      "The TeX silently corrects the print. Checked on a crop at 2.5x: g and j have the same size and "
      "baseline. Same typesetting slip as 𝒪_{xi} above and (𝒩_X|U_i)^{ni} on p. 142.",
      corrected=r"A(Z_j)_{g_j}"),
]

# ------------------------------------------------------------------ checks
texts = {p: (RUN / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(140, 145)}
work = dict(texts)
ok = True
for i, x in enumerate(findings):
    fx = x["fix"]
    if not fx:
        continue
    t0 = texts[x["page"]]
    n0 = t0.count(fx["old"])
    nw = work[x["page"]].count(fx["old"])
    if n0 != 1 or nw != 1:
        ok = False
        print("PROBLEM", i, x["page"], repr(fx["old"]), "original count", n0, "count at its turn", nw)
    else:
        work[x["page"]] = work[x["page"]].replace(fx["old"], fx["new"])
    if x["page"] == 140 and "ega1-6-fr.tex, before" in (x["note"] or ""):
        cut = t0.index("% (continued in")
        if t0.index(fx["old"]) < cut:
            ok = False
            print("PROBLEM: continuation fix not in continuation", i)
for p in range(140, 145):
    if work[p].count("{") != work[p].count("}"):
        ok = False
        print("PROBLEM: brace balance changed on page", p)
json.dump(findings, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in findings:
    cat = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], cat)] += 1
for p in range(140, 145):
    print(p, {c: cnt[(p, c)] for c in ("normal", "convention", "misprint")})
print("total", len(findings), "all checks ok" if ok else "CHECK FAILURES")
