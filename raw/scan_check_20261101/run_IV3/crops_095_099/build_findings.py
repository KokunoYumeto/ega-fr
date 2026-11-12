"""Build findings_095_099.json for the EGA IV-3 pp. 95-99 scan check and verify every fix.

Strings use <NL> for a line break (the release files use LF).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
OUT = os.path.join(RUN, "findings_095_099.json")

ARROW_NOTE = "Wavy maps-to arrow (GLOBAL_ISSUES 33), \\leadsto as in the earlier page fixes."
C7_NOTE = "Convention 7 (\\setmin, global pass)."


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": nl(old), "new": nl(new)},
    }
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 95 ----------------
    F(95, "introduction to §10, last sentence: 'les ensembles de points fermés des préschémas algébriques sur un corps'",
      "'préschémas algébriques' italic, 'sur un corps' roman (enlarged crop)",
      "\\emph{préschémas algébriques sur un corps}",
      "italics", None, "high",
      r"\emph{préschémas algébriques sur un corps}",
      r"\emph{préschémas algébriques} sur un corps",
      "The italics end after 'algébriques' in the print."),
    F(95, "(10.1.1): 'Le raisonnement de (0_III, 9.1.3), où on supprime le mot « rétrocompact »'",
      "'où on supprime' (enlarged crop)",
      "'où l'on supprime'",
      "word", None, "high",
      r"où l'on supprime", r"où on supprime"),
    F(95, "heading 10.1",
      "'10.1. Parties très denses d'un espace topologique.' (final full stop)",
      "\\subsection{Parties très denses d'un espace topologique} (no full stop)",
      "punctuation", None, "high",
      r"\subsection{Parties très denses d'un espace topologique}",
      r"\subsection{Parties très denses d'un espace topologique.}",
      "GLOBAL_ISSUES 43/58 pattern (subsection titles lack the printed full stop); same fix as the 8.13 heading on p. 49."),

    # ---------------- page 96 ----------------
    F(96, "Proposition (10.1.2) b'): '(autrement dit Z∩X_0 est dense dans Z)'",
      "the parenthesis is roman inside the italic statement, with 'dense' italic (enlarged crop)",
      "(autrement dit ... est \\emph{dense} dans $Z$) inside the italic proposition: italic, 'dense' upright",
      "convention", 6, "high",
      r"(autrement dit $Z\cap X_0$ est<NL>  \emph{dense} dans $Z$)",
      r"\textup{(autrement dit $Z\cap X_0$ est<NL>  \emph{dense} dans $Z$)}",
      "Inside \\textup the \\emph makes 'dense' italic, as printed."),
    F(96, "Proposition (10.1.2) c): 'L'application U⇝U∩X_0 de O(X) dans O(X_0)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"$U\mapsto U\cap X_0$", r"$U\leadsto U\cap X_0$", ARROW_NOTE),
    F(96, "Proposition (10.1.2) c): '(donc bijective)'",
      "'(donc' and ')' roman, 'bijective' italic, inside the italic statement (enlarged crop)",
      "'(donc bijective)' all italic (proposition environment)",
      "convention", 6, "high",
      r"$\mathfrak O(X_0)$ est injective (donc bijective)",
      r"$\mathfrak O(X_0)$ est injective \textup{(donc \emph{bijective})}",
      "Inside \\textup the \\emph keeps 'bijective' italic, as printed."),
    F(96, "Proposition (10.1.2) c'): 'L'application F⇝F∩X_0 de F(X) dans F(X_0)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"$F\mapsto F\cap X_0$", r"$F\leadsto F\cap X_0$", ""),
    F(96, "Proposition (10.1.2) c'): '(donc bijective)'",
      "'(donc' and ')' roman, 'bijective' italic (enlarged crop)",
      "'(donc bijective)' all italic (proposition environment)",
      "convention", 6, "high",
      r"$\mathfrak F(X_0)$ est injective (donc bijective)",
      r"$\mathfrak F(X_0)$ est injective \textup{(donc \emph{bijective})}", ""),
    F(96, "Proposition (10.1.2) c''): 'L'application Z⇝Z∩X_0 de Qc(X) dans Qc(X_0)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"L'application $Z\mapsto Z\cap X_0$ de<NL>  $\mathfrak{Qc}(X)$",
      r"L'application $Z\leadsto Z\cap X_0$ de<NL>  $\mathfrak{Qc}(X)$", ""),
    F(96, "Proposition (10.1.2) c''): '(donc bijective)'",
      "'(donc' and ')' roman, 'bijective' italic (enlarged crop)",
      "'(donc bijective)' all italic (proposition environment)",
      "convention", 6, "high",
      r"$\mathfrak{Qc}(X_0)$ est injective (donc bijective)",
      r"$\mathfrak{Qc}(X_0)$ est injective \textup{(donc \emph{bijective})}", ""),
    F(96, "Proposition (10.1.2) c'''): 'L'application Z⇝Z∩X_0 de Lqc(X) dans Lqc(X_0)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"L'application $Z\mapsto Z\cap X_0$ de<NL>  $\mathfrak{Lqc}(X)$",
      r"L'application $Z\leadsto Z\cap X_0$ de<NL>  $\mathfrak{Lqc}(X)$", ""),
    F(96, "Proposition (10.1.2), last sentence: 'En outre, ... l'application Z⇝Z∩X_0 de Lqc(X) dans Lqc(X_0) est bijective'",
      "wavy arrow ⇝", "\\mapsto",
      "symbol", None, "high",
      r"l'application<NL>$Z\mapsto Z\cap X_0$", r"l'application<NL>$Z\leadsto Z\cap X_0$", ""),
    F(96, "after (10.1.2): 'Notons que les assertions de surjectivité dans c) et c') sont triviales; elles entraînent'",
      "semicolon after 'triviales' (enlarged crop)", "colon '~:'",
      "punctuation", None, "high",
      r"triviales~: elles", r"triviales~; elles", ""),
    F(96, "proof of a') ⇒ a): 'on peut écrire Z=F—F''",
      "long dash for set difference", "$Z=F-F'$",
      "convention", 7, "high",
      r"$Z=F-F'$", r"$Z=F\setmin F'$", C7_NOTE),
    F(96, "proof of a') ⇒ a): 'd'où Z∩X_0=(F∩X_0)—(F'∩X_0)'",
      "long dash for set difference", "(F\\cap X_0)-(F'\\cap X_0)",
      "convention", 7, "high",
      r"(F\cap X_0)-(F'\cap X_0)", r"(F\cap X_0)\setmin(F'\cap X_0)", C7_NOTE),
    F(96, "proof of a) ⇒ c'''): '((Z'∪Z'')—(Z'∩Z''))∩X_0=∅'",
      "long dash for set difference", "((Z'\\cup Z'')-(Z'\\cap Z''))",
      "convention", 7, "high",
      r"((Z'\cup Z'')-(Z'\cap Z''))", r"((Z'\cup Z'')\setmin(Z'\cap Z''))", C7_NOTE),
    F(96, "proof of a) ⇒ c'''): 'on est bien ramené au cas où Z est localement fermé dans X, d'où la conclusion'",
      "'localement fermé dans X' (masculine; enlarged crop)",
      "'localement fermée dans $X$'",
      "word", None, "high",
      r"localement fermée dans $X$, d'où la conclusion",
      r"localement fermé dans $X$, d'où la conclusion",
      "The masculine agrees with Z read as an ensemble (the proof of c) ⇒ b) has 'Z est localement fermée' for the partie Z of b)); grammatical, so not treated as a misprint: the fix applies to both editions."),

    # ---------------- page 97 ----------------
    F(97, "page break 96/97: '(et donc aussi dans X_0). En vertu de c), il y a pour tout α un seul ouvert U_α de X | tel que X_0∩U_α=V_α'",
      "printed p. 96 ends with 'donc aussi dans X_0). En vertu de c), il y a pour tout α un seul ouvert U_α de X'; p. 97 begins 'tel que X_0∩U_α=V_α'",
      "\\oldpage[IV-3]{97} stands before 'donc aussi dans $X_0$)' (one printed line too early)",
      "marker", None, "high",
      r"\oldpage[IV-3]{97}<NL>donc aussi dans $X_0$). En vertu de \emph{c)}, il y a pour tout $\alpha$ un<NL>seul ouvert $U_\alpha$ de $X$ tel que",
      r"donc aussi dans $X_0$). En vertu de \emph{c)}, il y a pour tout $\alpha$ un<NL>seul ouvert $U_\alpha$ de $X$<NL>\oldpage[IV-3]{97}<NL>tel que",
      "One atomic edit ('old' lies in page_097.tex): moves the marker down one printed line, mid-sentence, on its own line without blank lines. Afterwards the p. 96 segment ends with the last printed line of p. 96."),
    F(97, "proof of (10.1.2): 'on a Z_β∩U_α∩X_0=U_α∩Z_0∩V_β=V_α∩Z_0∩V_β=Z_α∩X_0∩V_β⊂Z_α∩X_0; comme'",
      "the formula is in the running text (same line as 'comme Z_β∩U_α et Z_α')",
      "set as a display \\[ ... \\] with '~;' inside",
      "other", None, "high",
      r"on a<NL>\[<NL>Z_\beta\cap U_\alpha\cap X_0<NL>=U_\alpha\cap Z_0\cap V_\beta<NL>=V_\alpha\cap Z_0\cap V_\beta<NL>=Z_\alpha\cap X_0\cap V_\beta<NL>\subset Z_\alpha\cap X_0~;<NL>\]<NL>comme",
      r"on a<NL>$Z_\beta\cap U_\alpha\cap X_0<NL>=U_\alpha\cap Z_0\cap V_\beta<NL>=V_\alpha\cap Z_0\cap V_\beta<NL>=Z_\alpha\cap X_0\cap V_\beta<NL>\subset Z_\alpha\cap X_0$~;<NL>comme",
      "Formula displayed where the print has it inline (GLOBAL_ISSUES 21)."),
    F(97, "Définition (10.1.3): 'vérifie les conditions équivalentes de (10.1.2), on dit'",
      "the reference (10.1.2) is upright inside the italic statement (enlarged crop)",
      "(10.1.2) inside the italic definition environment: italic",
      "convention", 6, "high",
      r"équivalentes de (10.1.2), on dit", r"équivalentes de \textup{(10.1.2)}, on dit", ""),
    F(97, "Définition (10.1.3): 'on dit que X_0 est très dense dans X'",
      "'très dense' italic like the rest of the statement, no change of face (enlarged crop)",
      "\\emph{très dense} inside the italic definition environment: upright",
      "convention", 6, "high",
      r"on dit que $X_0$ est \emph{très dense} dans $X$.", r"on dit que $X_0$ est très dense dans $X$.",
      "Printed italic words left upright: drop \\emph inside the italic environment (FIX_POLICY 2.6)."),
    F(97, "heading 10.2",
      "'10.2. Quasi-homéomorphismes.' (final full stop)",
      "\\subsection{Quasi-homéomorphismes} (no full stop)",
      "punctuation", None, "high",
      r"\subsection{Quasi-homéomorphismes}", r"\subsection{Quasi-homéomorphismes.}",
      "As heading 10.1 on p. 95."),
    F(97, "Proposition (10.2.1) a): 'L'application U⇝f^{-1}(U) de O(X) dans O(X_0)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"L'application $U\mapsto f^{-1}(U)$", r"L'application $U\leadsto f^{-1}(U)$", ARROW_NOTE),
    F(97, "Proposition (10.2.1) a'): 'L'application F⇝f^{-1}(F) de F(X) dans F(X_0)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"$F\mapsto f^{-1}(F)$", r"$F\leadsto f^{-1}(F)$", ""),
    F(97, "Proposition (10.2.1) b): 'f(X_0) est très dense (10.1.3) dans X'",
      "the reference (10.1.3) is upright inside the italic statement (enlarged crop)",
      "(10.1.3) inside the italic proposition environment: italic",
      "convention", 6, "high",
      r"très dense (10.1.3) dans", r"très dense \textup{(10.1.3)} dans", ""),
    F(97, "Proposition (10.2.1) c): 'Le foncteur F⇝f^*(F)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"$\mathcal F\mapsto f^*(\mathcal F)$", r"$\mathcal F\leadsto f^*(\mathcal F)$", ""),
    F(97, "Proposition (10.2.1) c): 'faisceaux d'ensembles (resp. des faisceaux de groupes abéliens) sur X dans'",
      "'resp.' upright inside the italic statement (enlarged crop)",
      "(resp. ...): italic",
      "convention", 6, "high",
      r"(resp. des faisceaux de groupes abéliens) sur $X$",
      r"(\textup{resp.} des faisceaux de groupes abéliens) sur $X$", ""),
    F(97, "Proposition (10.2.1) c): 'faisceaux d'ensembles (resp. des faisceaux de groupes abéliens) sur X_0'",
      "'resp.' upright inside the italic statement (enlarged crop)",
      "(resp. ...): italic",
      "convention", 6, "high",
      r"(resp. des faisceaux de groupes<NL>  abéliens)",
      r"(\textup{resp.} des faisceaux de groupes<NL>  abéliens)", ""),
    F(97, "proof of (10.2.1): 'les applications U⇝U∩f(X_0) de O(X) dans O(f(X_0))'",
      "wavy arrow ⇝", "\\mapsto",
      "symbol", None, "high",
      r"$U\mapsto U\cap f(X_0)$", r"$U\leadsto U\cap f(X_0)$", ""),
    F(97, "proof of (10.2.1): 'et V⇝f^{-1}(V) de O(f(X_0)) dans O(X_0)'",
      "wavy arrow ⇝", "\\mapsto",
      "symbol", None, "high",
      r"$V\mapsto f^{-1}(V)$", r"$V\leadsto f^{-1}(V)$", ""),
    F(97, "proof of (10.2.1): 'leur composée U⇝f^{-1}(U)'",
      "wavy arrow ⇝", "\\mapsto",
      "symbol", None, "high",
      r"composée $U\mapsto f^{-1}(U)$", r"composée $U\leadsto f^{-1}(U)$", ""),

    # ---------------- page 98 ----------------
    F(98, "proof of (10.2.1): 'on a un isomorphisme canonique Γ(X,F) ⥲ Hom(Z_X,F) fonctoriel en F'",
      "the formula is in the running text (same line as 'on a un isomorphisme canonique')",
      "set as a display \\[ ... \\]",
      "other", None, "high",
      r"canonique<NL>\[<NL>\Gamma(X,\mathcal F)\xrightarrow{\sim}\operatorname{Hom}(\mathbf Z_X,\mathcal F)<NL>\]<NL>fonctoriel",
      r"canonique<NL>$\Gamma(X,\mathcal F)\xrightarrow{\sim}\operatorname{Hom}(\mathbf Z_X,\mathcal F)$<NL>fonctoriel",
      "Formula displayed where the print has it inline (GLOBAL_ISSUES 21)."),
    F(98, "proof of (10.2.1): 'soit F_0 le faisceau sur X image directe par l'injection canonique Y_0→X_0'",
      "'le faisceau sur X' (no subscript; enlarged crop)",
      "'sur $X$ image directe': the TeX keeps the printed reading",
      "misprint_in_print", None, "high",
      None, None,
      "F_0 is the direct image of the constant sheaf Z on Y_0 by Y_0→X_0, a sheaf on X_0 (it is isomorphic to f^*(F) and has the section s_0 over X_0). Diplomatic TeX already right; in the corrected edition replace 'sur $X$ image directe par l'injection canonique $Y_0\\to X_0$' (once on the page) by the corrected reading.",
      corrected=r"sur $X_0$ image directe par l'injection canonique $Y_0\to X_0$"),
    F(98, "end of the proof of (10.2.1): 'des x∈X tels que s_x≠0_x, et y est fermé dans X. C.Q.F.D.'",
      "lower-case italic y (enlarged crop)",
      "'et $y$ est fermé': the TeX keeps the printed reading",
      "misprint_in_print", None, "high",
      None, None,
      "The closed set is the set Y of the x∈X with s_x≠0_x, named in the same sentence; y is not defined. Diplomatic TeX already right; in the corrected edition replace 'et $y$ est fermé' by the corrected reading.",
      corrected=r"et $Y$ est fermé"),
    F(98, "Définition (10.2.2): 'vérifie les conditions équivalentes de (10.2.1), on dit'",
      "the reference (10.2.1) is upright inside the italic statement (enlarged crop)",
      "(10.2.1) inside the italic definition environment: italic",
      "convention", 6, "high",
      r"équivalentes de (10.2.1), on dit", r"équivalentes de \textup{(10.2.1)}, on dit", ""),
    F(98, "Définition (10.2.2): 'on dit que f est un quasi-homéomorphisme de X_0 dans X'",
      "'quasi-homéomorphisme' italic like the rest of the statement, no change of face (enlarged crop)",
      "\\emph{quasi-homéomorphisme} inside the italic definition environment: upright",
      "convention", 6, "high",
      r"\emph{quasi-homéomorphisme} de", r"quasi-homéomorphisme de",
      "Printed italic words left upright: drop \\emph inside the italic environment (FIX_POLICY 2.6). The \\emph{quasi-homéomorphisme} in the roman paragraph after the definition is right."),

    # ---------------- page 99 ----------------
    F(99, "proof of (10.2.4): 'soit réunion d'un nombre fini de parties Y'_i fermées dans U'",
      "Y'_i (subscript i; enlarged crop); the following 'si j est un indice tel que z∈Y'_j' has j",
      "$Y'_j$",
      "formula", None, "high",
      r"parties $Y'_j$ fermées", r"parties $Y'_i$ fermées",
      "Not a misprint: the family is indexed by i, then an index j is chosen; the fix applies to both editions."),
    F(99, "proof of (10.2.4): 'parties Y'_i fermées dans U; si j est'",
      "'dans' italic (enlarged crop), as in 'une partie fermée dans Y'' on the line above",
      "'dans' upright",
      "italics", None, "high",
      r"fermées dans $U$~;", r"fermées \emph{dans} $U$~;", ""),
    F(99, "Corollaire (10.2.6): 'Pour que Y' soit quasi-compact (resp. noethérien'",
      "'resp.' upright inside the italic statement (enlarged crop)",
      "(resp. ...): italic",
      "convention", 6, "high",
      r"quasi-compact<NL>(resp. noethérien", r"quasi-compact<NL>(\textup{resp.} noethérien", ""),
    F(99, "Corollaire (10.2.6): 'resp. rétrocompact dans Y)'",
      "'resp.' upright inside the italic statement (enlarged crop)",
      "resp.: italic",
      "convention", 6, "high",
      r"resp. rétrocompact dans $Y$", r"\textup{resp.} rétrocompact dans $Y$", ""),
    F(99, "Corollaire (10.2.6): 'il faut et il suffit que X' soit quasi-compact (resp. noethérien'",
      "'resp.' upright inside the italic statement (enlarged crop)",
      "(resp. ...): italic",
      "convention", 6, "high",
      r"soit quasi-compact (resp. noethérien", r"soit quasi-compact (\textup{resp.} noethérien", ""),
    F(99, "Corollaire (10.2.6): 'resp. rétrocompact dans X)'",
      "'resp.' upright inside the italic statement (enlarged crop)",
      "resp.: italic",
      "convention", 6, "high",
      r"resp. rétrocompact dans $X$", r"\textup{resp.} rétrocompact dans $X$", ""),
    F(99, "proof of (10.2.6): 'Comme U⇝f^{-1}(U) est une bijection de O(Y) sur O(X)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"$U\mapsto f^{-1}(U)$ est une bijection", r"$U\leadsto f^{-1}(U)$ est une bijection", ARROW_NOTE),
    F(99, "Proposition (10.2.7): 'Alors l'application Z⇝f^{-1}(Z) de P(Y) dans P(X)'",
      "wavy arrow ⇝ (enlarged crop)", "\\mapsto",
      "symbol", None, "high",
      r"$Z\mapsto f^{-1}(Z)$", r"$Z\leadsto f^{-1}(Z)$", ""),
    F(99, "Proposition (10.2.7): '(cf. (10.1.1) pour les notations)'",
      "the whole parenthesis is roman inside the italic statement (enlarged crop)",
      "italic (proposition environment)",
      "convention", 6, "high",
      r"(cf. (10.1.1) pour les notations)", r"\textup{(cf. (10.1.1) pour les notations)}", ""),
    F(100, "page break 99/100 (printed p. 99): '... de celle de f(X) les cinq dernières appli-|cations, où l'on remplace Y par f(X)'",
      "printed p. 99 ends with the paragraph 'Pour les deux premières, ce n'est autre que la définition (10.2.2); comme la topologie de X est l'image réciproque par f de celle de f(X) les cinq dernières appli-'; p. 100 begins 'cations, où l'on remplace Y par f(X)' (top strip of p. 100 checked)",
      "\\oldpage[IV-3]{100} stands before 'Pour les deux premières' (two printed lines too early)",
      "marker", None, "high",
      r"\oldpage[IV-3]{100}<NL>Pour les deux premières, ce n'est autre que la définition (10.2.2)~; comme la<NL>topologie de $X$ est l'image réciproque par $f$ de celle de $f(X)$ les cinq<NL>dernières applications",
      r"Pour les deux premières, ce n'est autre que la définition (10.2.2)~; comme la<NL>topologie de $X$ est l'image réciproque par $f$ de celle de $f(X)$ les cinq<NL>dernières appli%<NL>\oldpage[IV-3]{100}<NL>cations",
      "OUTSIDE pages 95-99: 'old' lies in page_100.tex (filed under page 100 so that apply_fixes finds it). One atomic edit: removes the marker before 'Pour les deux premières' (the blank line after \\end{proposition} stays: the print starts a paragraph there) and inserts it at the printed word break appli-|cations, as homo%|morphisme (0_IV-1 p. 138) and irréduc%|tible (IV-1 p. 226). The moved text matches the print of p. 99. The pp. 100-104 checker may report the same move; apply only one."),
]


def main():
    pages = {}
    bad = 0
    for x in findings:
        p = x["page"]
        if p not in pages:
            with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
                pages[p] = fh.read().replace("\r\n", "\n")
        fx = x["fix"]
        if fx is None:
            continue
        n = pages[p].count(fx["old"])
        if n != 1:
            bad += 1
            print("NOT UNIQUE (%d) p.%d: %r" % (n, p, fx["old"][:80]))
        if fx["old"] == fx["new"]:
            bad += 1
            print("NO-OP p.%d: %r" % (p, fx["old"][:80]))
    # misprint 'corrected' anchors: check the printed reading is on the page once
    anchors = {98: [r"sur $X$ image directe par l'injection canonique $Y_0\to X_0$", r"et $y$ est fermé"]}
    for p, lst in anchors.items():
        for a in lst:
            n = pages[p].count(a)
            if n != 1:
                bad += 1
                print("MISPRINT ANCHOR NOT UNIQUE (%d) p.%d: %r" % (n, p, a))
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(findings, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    counts = {}
    for x in findings:
        c = counts.setdefault(x["page"], [0, 0, 0])
        if x["kind"] == "misprint_in_print":
            c[2] += 1
        elif x["kind"] == "convention":
            c[1] += 1
        else:
            c[0] += 1
    print("written", OUT, len(findings), "findings; problems:", bad)
    for p in sorted(counts):
        print(p, "normal/convention/misprint =", "/".join(str(v) for v in counts[p]))


if __name__ == "__main__":
    main()
