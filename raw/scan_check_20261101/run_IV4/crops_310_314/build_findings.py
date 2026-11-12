# Builds findings_310_314.json; "¶" in the raw strings stands for a line break.
import json, sys

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
OUT = RUN + "/findings_310_314.json"

def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf}
    if old is None:
        d["fix"] = None
    else:
        d["fix"] = {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")}
    if corrected is not None:
        d["corrected"] = corrected.replace("¶", "\n")
    d["note"] = note
    return d

L = []

# ---------------- page 310 ----------------
L.append(F(310, "l. 1: 'sur k(y), donc fermé dans X_y'", "bold italic k (page_310_s1.png)", "plain k",
           "convention", 1, "high", r"sur $k(y)$, donc", r"sur $\boldsymbol{k}(y)$, donc"))
L.append(F(310, "l. 1: 'donc fermé dans X_y (I, 6.4.2)'", "'fermé' italic (page_310_s1.png)", "upright",
           "italics", None, "high", r"fermé dans $X_y$", r"\emph{fermé} dans $X_y$",
           "Independent of the k(y) entry just before it (adjacent, no overlap)."))
L.append(F(310, "Théorème (21.12.12), l. 3: 'vérifie la condition (W) de (21.12.8)'",
           "'(W)' and '(21.12.8)' upright with upright parentheses, 'de' italic (crop p310_thm_W.png)",
           "italic (theorem environment)", "convention", 6, "high",
           r"vérifie la condition (W)¶de (21.12.8)", r"vérifie la condition \textup{(W)}¶de \textup{(21.12.8)}",
           "As (21.12.10) and (21.12.11) on pp. 308-309."))
L.append(F(310, "Théorème (21.12.12), l. 4: '(conditions remplies en particulier lorsque Y est localement factoriel (21.12.9))'",
           "the parenthesis roman, with 'localement factoriel' italic inside it; 'Si V' italic again (crop p310_thm_cond.png)",
           "the whole parenthesis italic (theorem environment)", "convention", 6, "high",
           r"(conditions remplies en particulier lorsque $Y$ est localement factoriel¶(21.12.9))",
           r"\textup{(conditions remplies en particulier lorsque $Y$ est \emph{localement factoriel}¶(21.12.9))}",
           "\\emph inside \\textup gives the print's italic 'localement factoriel'. Independent of the (W) entry before it (no overlap)."))
L.append(F(310, "Théorème (21.12.12), last line: 'T = X — V'", "long dash for set difference", "minus sign",
           "convention", 7, "high", r"$T=X-V$ sont de codimension", r"$T=X\setmin V$ sont de codimension"))
L.append(F(310, "Corollaire (21.12.13), l. 1: 'Supposons vérifiées les hypothèses de (21.12.12)'",
           "'(21.12.12)' upright (crop p310_cor13.png)", "italic (corollary environment)", "convention", 6, "high",
           r"hypothèses de (21.12.12) et en outre", r"hypothèses de \textup{(21.12.12)} et en outre"))
L.append(F(310, "Corollaire (21.12.13), l. 2-3: '(on rappelle que ce sont les points où dim(O_X,x) = 1)'",
           "the whole parenthesis roman (crop p310_cor13.png)", "italic (corollary environment)", "convention", 6, "high",
           r"(on rappelle que ce sont les points où¶$\dim(\mathcal O_{X,x})=1$)",
           r"\textup{(on rappelle que ce sont les points où¶$\dim(\mathcal O_{X,x})=1$)}"))
L.append(F(310, "Remarques (21.12.14) (i), l. 1: 'lorsque Y est régulier et intègre'", "'régulier' italic (page_310_s3.png)",
           "no \\emph", "italics", None, "high", r"lorsque $Y$ est régulier et intègre",
           r"lorsque $Y$ est \emph{régulier} et intègre", "Emphasis judged as in a roman remark body."))
L.append(F(310, "Remarques (21.12.14) (i), l. 2: 'théorème d'Auslander-Buchsbaum'", "hyphen (crop p310_auslander.png)",
           "en dash (--)", "punctuation", None, "high", r"Auslander--Buchsbaum", r"Auslander-Buchsbaum",
           "As Cohen--Macaulay (GLOBAL_ISSUES 74)."))
L.append(F(310, "Remarques (21.12.14) (ii): 'donc x ∈ X — T'", "long dash for set difference", "minus sign",
           "convention", 7, "high", r"$x\in X-T$", r"$x\in X\setmin T$"))

# ---------------- page 311 ----------------
L.append(F(311, "page break 310/311: printed p. 310 ends with the first two lines of (iii) ('... nous verrons au chap. V'); p. 311 begins 'qu'on a un résultat plus précis que (21.12.12)'",
           "page_310_s4.png: '(iii) Sans supposer ... relativement à Y (chap. V), nous verrons au chap. V' above the page number 310; page_311_s1.png begins 'qu'on a un résultat'",
           "\\oldpage[IV-4]{311} stands before '(iii) Sans supposer', two printed lines too early", "marker", None, "high",
           r"\oldpage[IV-4]{311}¶(iii) Sans supposer que $Y$ soit localement factoriel, mais en supposant par contre que¶$X$ est intersection complète relativement à $Y$ (chap.~V), nous verrons au chap.~V¶",
           r"(iii) Sans supposer que $Y$ soit localement factoriel, mais en supposant par contre que¶$X$ est intersection complète relativement à $Y$ (chap.~V), nous verrons au chap.~V¶\oldpage[IV-4]{311}¶",
           "One edit moves the marker: mid-sentence break, so no blank lines at the new place; the blank line before '(iii)' stays (new paragraph in the print). The two moved lines have no other differences."))
L.append(F(311, "Remarques (21.12.14) (v), l. 3: 'la fibre X_η soit étale sur k(η)'", "bold italic k (page_311_s2.png)",
           "plain k", "convention", 1, "high", r"sur $k(\eta)$", r"sur $\boldsymbol{k}(\eta)$"))
L.append(F(311, "(v), l. 4: 'tel que g|V' : V'→Y soit étale ;'", "'étale' italic (page_311_s2.png)", "no \\emph",
           "italics", None, "high", r"soit étale;", r"soit \emph{étale};"))
L.append(F(311, "(v), l. 6: '(« théorème de pureté » de Zariski-Nagata)'", "'théorème de pureté' italic (crop p311_zariski.png)",
           "no \\emph", "italics", None, "high", r"« théorème de pureté »", r"« \emph{théorème de pureté} »",
           "Independent of the hyphen entry below (no overlap)."))
L.append(F(311, "(v), l. 6: 'Zariski-Nagata'", "hyphen (crop p311_zariski.png)", "en dash (--)", "punctuation", None,
           "high", r"Zariski--Nagata", r"Zariski-Nagata"))
L.append(F(311, "(v), last line: '... étale sur Spec(A)) est affine.'", "'affine' italic (page_311_s2.png)", "no \\emph",
           "italics", None, "high", r"est affine.¶\end{remarks}", r"est \emph{affine}.¶\end{remarks}"))
L.append(F(311, "Proposition (21.12.15), l. 2: 'sont géométriquement irréductibles (4.5.2),'", "'(4.5.2)' upright",
           "italic (proposition environment)", "convention", 6, "high", r"irréductibles (4.5.2),",
           r"irréductibles \textup{(4.5.2)},"))
L.append(F(311, "proof of (21.12.15): '... est une immersion ouverte. Comme tout s ∈ S est générisation'",
           "no paragraph break: 'Comme tout' follows on the same line (page_311_s3.png)", "blank line: new paragraph",
           "extra", None, "high", r"est une immersion ouverte.¶¶Comme tout", r"est une immersion ouverte.¶Comme tout"))
L.append(F(311, "proof of (21.12.15): 'se ramener au cas où S est un schéma local et intègre de point fermé s'",
           "'local' and 'intègre' italic (page_311_s3.png)", "no \\emph", "italics", None, "high",
           r"un schéma local et intègre de point fermé", r"un schéma \emph{local} et \emph{intègre} de point fermé"))
L.append(F(311, "proof of (21.12.15): 'X et Y sont de présentation finie sur S.'", "'présentation finie' italic (page_311_s4.png)",
           "no \\emph", "italics", None, "high", r"sont de présentation finie", r"sont de \emph{présentation finie}",
           "Independent of the next entry (adjacent, no overlap)."))
L.append(F(311, "proof of (21.12.15): '... sur S. Il existe alors un sous-anneau local noethérien'",
           "no paragraph break: 'Il existe alors' follows on the same line (page_311_s4.png)", "blank line: new paragraph",
           "extra", None, "high", r"sur $S$.¶¶Il existe alors", r"sur $S$.¶Il existe alors"))

# ---------------- page 312 ----------------
L.append(F(312, "l. 6-7: '... géométriquement irréductible (4.5.6). On voit donc qu'on peut se borner'",
           "no paragraph break: 'On voit donc' starts the next line flush left, not indented (page_312_s1.png)",
           "blank line: new paragraph", "extra", None, "high", r"irréductible (4.5.6).¶¶On voit donc",
           r"irréductible (4.5.6).¶On voit donc"))
L.append(F(312, "l. 8: 'anneau local intègre noethérien, de point fermé s'", "'noethérien' italic (page_312_s1.png)",
           "no \\emph", "italics", None, "high", r"noethérien, de point fermé $s$", r"\emph{noethérien}, de point fermé $s$"))
L.append(F(312, "'... spectre d'un anneau de valuation discrète. Alors, puisque h : Y→S est lisse'",
           "no paragraph break: 'Alors, puisque' starts the next line flush left, not indented (page_312_s2.png)",
           "blank line: new paragraph", "extra", None, "high", r"valuation discrète}.¶¶Alors, puisque",
           r"valuation discrète}.¶Alors, puisque"))
L.append(F(312, "'Y est régulier (17.5.8)'", "'régulier' italic (page_312_s2.png)", "no \\emph", "italics", None, "high",
           r"$Y$ est régulier (17.5.8)", r"$Y$ est \emph{régulier} (17.5.8)"))
L.append(F(312, "'on peut se borner au cas où Y est intègre.'", "'intègre' italic (page_312_s2.png)", "no \\emph",
           "italics", None, "high", r"$Y$ est intègre. Comme", r"$Y$ est \emph{intègre}. Comme"))
L.append(F(312, "'et par suite intègre et f est un morphisme birationnel et séparé'",
           "'intègre' and 'birationnel' italic, 'séparé' roman (page_312_s2.png)", "no \\emph", "italics", None, "high",
           r"par suite intègre et $f$ est un¶morphisme birationnel et séparé",
           r"par suite \emph{intègre} et $f$ est un¶morphisme \emph{birationnel} et séparé"))
L.append(F(312, "'les morphismes g et h sont équidimensionnels ;'", "'équidimensionnels' italic (page_312_s3.png)",
           "no \\emph", "italics", None, "high", r"sont équidimensionnels;", r"sont \emph{équidimensionnels};"))
L.append(F(312, "'est bien quasi-fini au point x'", "'quasi-fini' italic (page_312_s3.png)", "no \\emph", "italics",
           None, "high", r"est bien quasi-fini¶au point", r"est bien \emph{quasi-fini}¶au point"))

# ---------------- page 313 ----------------
L.append(F(313, "Remarques (21.12.17) (i), l. 2: 'les fibres X_s sont irréductibles.'", "'irréductibles' italic (page_313_s2.png)",
           "no \\emph", "italics", None, "high", r"sont irréductibles. Prenons", r"sont \emph{irréductibles}. Prenons"))
L.append(F(313, "(i), l. 3: 'Y = P^1_S'", "bold upright P (crop p313_P1S_kks.png)", "\\mathbb P (blackboard bold)",
           "font", None, "high", r"$Y=\mathbb P^1_S$", r"$Y=\mathbf P^1_S$",
           "Bold upright projective P as in IV-3 p. 215 (not convention 10). ega4-21c is the only IV-4 file with \\mathbb P/A/V."))
L.append(F(313, "(i), l. 4: 'un point rationnel sur k = k(s)'", "first k light italic, second k bold italic (crop p313_kks.png)",
           "plain k in k(s)", "convention", 1, "high", r"$k=k(s)$", r"$k=\boldsymbol{k}(s)$"))
L.append(F(313, "(i), l. 7: 'f^{-1}(z) est isomorphe à P^1_k'", "bold upright P (crop p313_Z.png)", "\\mathbb P",
           "font", None, "high", r"à $\mathbb P^1_k$, et d'autre", r"à $\mathbf P^1_k$, et d'autre"))
L.append(F(313, "(i), l. 7: 'isomorphe à Y_s — {z}'", "long dash for set difference (crop p313_Z12_zoom.png)", "minus sign",
           "convention", 7, "high", r"$Y_s-\{z\}$", r"$Y_s\setmin\{z\}$"))
L.append(F(313, "(ii), l. 5: 'complémentaire d'un point fermé dans P^1_k'", "bold upright P (crop p313_V1k.png)", "\\mathbb P",
           "font", None, "high", r"dans $\mathbb P^1_k$, donc", r"dans $\mathbf P^1_k$, donc"))
L.append(F(313, "(ii), l. 5: 'donc est un schéma affine isomorphe à V^1_k'", "bold upright V^1_k, EGA's affine line (crop p313_V1k.png)",
           "\\mathbb A^1_k: the notation is rewritten", "formula", None, "high", r"$\mathbb A^1_k$", r"$\mathbf V^1_k$",
           "EGA writes the affine space V^n (IV-2 p. 21, IV-3 p. 158 fixed the same way); A^1 is not the print's notation."))
L.append(F(313, "(ii), last line: '... et f'_s n'est pas un isomorphisme, bien que f' en soit un.'",
           "'bien que f′ en soit un': f′ without subscript (crop p313_fprime_eta.png; compare f′_s in p313_fprime_s.png)",
           "f'_\\eta: silent correction", "misprint_in_print", None, "high", r"bien que $f'_\eta$ en soit",
           r"bien que $f'$ en soit",
           "The generic fibre f'_η is meant (f' itself is not even proper); the print drops the subscript η. The TeX silently corrects; the fix restores the printed reading.",
           corrected=r"bien que $f'_\eta$ en soit"))
L.append(F(313, "heading of 21.13: 'Couples parafactoriels. Anneaux locaux parafactoriels.'", "final full stop (page_313_s3.png)",
           "no final full stop", "punctuation", None, "high",
           r"\subsection{Couples parafactoriels. Anneaux locaux parafactoriels}",
           r"\subsection{Couples parafactoriels. Anneaux locaux parafactoriels.}"))
L.append(F(313, "Définition (21.13.1), l. 1: 'U = X — Y.'", "long dash for set difference (crop p313_def.png)", "minus sign",
           "convention", 7, "high", r"fermée de $X$, $U=X-Y$.", r"fermée de $X$, $U=X\setmin Y$."))
L.append(F(313, "Définition (21.13.1), last line: 'est une équivalence de catégories.'",
           "italic like the rest of the statement; only 'parafactoriel' is set roman (crop p313_def.png)",
           "\\emph inside the italic definition: printed upright", "convention", 6, "high",
           r"est une \emph{équivalence de catégories}.", r"est une équivalence de catégories."))
L.append(F(313, "Définition (21.13.1), l. 3: 'le foncteur restriction ℒ ⇝ ℒ|(U∩V)'", "wavy arrow (crop p313_leadsto.png)",
           "\\mapsto", "symbol", None, "high", r"$\mathscr L\mapsto\mathscr L|(U\cap V)$, de la catégorie",
           r"$\mathscr L\leadsto\mathscr L|(U\cap V)$, de la catégorie"))
L.append(F(313, "1°: 'le foncteur ℒ ⇝ ℒ|(U∩V) est pleinement fidèle'", "wavy arrow (page_313_s4.png)", "\\mapsto",
           "symbol", None, "high", r"$\mathscr L\mapsto\mathscr L|(U\cap V)$ est \emph{pleinement",
           r"$\mathscr L\leadsto\mathscr L|(U\cap V)$ est \emph{pleinement"))
L.append(F(313, "2°: 'le foncteur ℒ ⇝ ℒ|(U∩V) est essentiellement surjectif'", "wavy arrow (page_313_s4.png)", "\\mapsto",
           "symbol", None, "high", r"$\mathscr L\mapsto\mathscr L|(U\cap V)$ est¶  \emph{essentiellement",
           r"$\mathscr L\leadsto\mathscr L|(U\cap V)$ est¶  \emph{essentiellement"))

# ---------------- page 314 ----------------
L.append(F(314, "Lemme (21.13.2) a): 'le foncteur ℰ ⇝ f_V^*(ℰ)'", "wavy arrow (crop p314_a.png)", "\\mapsto", "symbol", None,
           "high", r"$\mathscr E\mapsto f_V^*(\mathscr E)$ de la catégorie", r"$\mathscr E\leadsto f_V^*(\mathscr E)$ de la catégorie"))
L.append(F(314, "Lemme (21.13.2) a), end: 'est fidèle (resp. pleinement fidèle).'",
           "'(resp.' and ')' upright, 'pleinement fidèle' italic (crop p314_a_aprime.png)", "all italic (lemma environment)",
           "convention", 6, "high", r"fini, est fidèle¶  (resp.\ pleinement fidèle).",
           r"fini, est fidèle¶  \textup{(resp.}\ pleinement fidèle\textup{)}."))
L.append(F(314, "Lemme (21.13.2) a'): 'le foncteur ℒ ⇝ f_V^*(ℒ)'", "wavy arrow (crop p314_a_aprime.png)", "\\mapsto", "symbol",
           None, "high", r"$\mathscr L\mapsto f_V^*(\mathscr L)$", r"$\mathscr L\leadsto f_V^*(\mathscr L)$"))
L.append(F(314, "Lemme (21.13.2) a'), end: 'est fidèle (resp. pleinement fidèle).'",
           "'(resp.' and ')' upright, 'pleinement fidèle' italic (crop p314_a_aprime.png)", "all italic (lemma environment)",
           "convention", 6, "high", r"(V)}$-Modules localement libres de rang $1$ est fidèle¶  (resp.\ pleinement fidèle).",
           r"(V)}$-Modules localement libres de rang $1$ est fidèle¶  \textup{(resp.}\ pleinement fidèle\textup{)}."))
L.append(F(314, "Lemme (21.13.2) b): 'est un monomorphisme (resp. un isomorphisme) pour tout'",
           "'(resp.' and ')' upright, 'un isomorphisme' italic (crop p314_b_bprime.png)", "all italic (lemma environment)",
           "convention", 6, "high", r"monomorphisme¶  (resp.\ un isomorphisme) pour tout",
           r"monomorphisme¶  \textup{(resp.}\ un isomorphisme\textup{)} pour tout"))
L.append(F(314, "Lemme (21.13.2) b'): 'est un monomorphisme (resp. un isomorphisme).'",
           "'(resp.' and ')' upright, 'un isomorphisme' italic (crop p314_b_bprime.png)", "all italic (lemma environment)",
           "convention", 6, "high", r"monomorphisme¶  (resp.\ un isomorphisme).¶\end{enumerate}",
           r"monomorphisme¶  \textup{(resp.}\ un isomorphisme\textup{)}.¶\end{enumerate}"))
L.append(F(314, "Lemme (21.13.2): item labels (i), (ii)", "labels upright (crop p314_i_ii.png)",
           "enumerate labels italic inside the italic lemma", "convention", 6, "high",
           r"\begin{enumerate}[label=(\roman*)]¶  \item $f_*(\mathscr E')$",
           r"\begin{enumerate}[label=\textup{(\roman*)}]¶  \item $f_*(\mathscr E')$",
           "GLOBAL_ISSUES 16; one edit covers both labels."))
L.append(F(314, "Lemme (21.13.2), last sentence: 'Lorsque ces deux conditions sont remplies, ℰ est isomorphe à f_*(ℰ′).'",
           "indented new paragraph (page_314_s3.png)", "follows \\end{enumerate} without a blank line: no indent",
           "other", None, "high", r"\end{enumerate}¶Lorsque ces deux", r"\end{enumerate}¶¶Lorsque ces deux",
           "GLOBAL_ISSUES 80 pattern."))
L.append(F(314, "proof of (21.13.2), l. 1: 'Dire que le foncteur ℰ ⇝ f_V^*(ℰ) est fidèle'", "wavy arrow (page_314_s3.png)",
           "\\mapsto", "symbol", None, "high", r"$\mathscr E\mapsto f_V^*(\mathscr E)$ est fidèle",
           r"$\mathscr E\leadsto f_V^*(\mathscr E)$ est fidèle"))
L.append(F(314, "proof of (21.13.2), l. 3: 'l'application Hom_O_V(ℰ_1, ℰ_2) → Hom_O_f^{-1}(V)(f^*(ℰ_1), f^*(ℰ_2)) est injective'",
           "formula in the running text (crop p314_hom_line.png)", "displayed formula", "other", None, "high",
           r"\[¶  \operatorname{Hom}_{\mathcal O_V}(\mathscr E_1,\mathscr E_2)¶  \longrightarrow¶  \operatorname{Hom}_{\mathcal O_{f^{-1}(V)}}¶  (f_V^*(\mathscr E_1),f_V^*(\mathscr E_2))¶\]",
           r"$\operatorname{Hom}_{\mathcal O_V}(\mathscr E_1,\mathscr E_2)¶\longrightarrow¶\operatorname{Hom}_{\mathcal O_{f^{-1}(V)}}¶(f_V^*(\mathscr E_1),f_V^*(\mathscr E_2))$",
           "Set inline as printed. Apply BEFORE the misprint entry that follows (f^* for f_V^*), whose 'old' lies inside this one and is left unchanged by it."))
L.append(F(314, "same formula: 'Hom_O_f^{-1}(V)(f^*(ℰ_1), f^*(ℰ_2))'",
           "f^*(ℰ_1), f^*(ℰ_2) without the subscript V (crop p314_hom_fstar.png)", "f_V^*: silent correction",
           "misprint_in_print", None, "medium", r"(f_V^*(\mathscr E_1),f_V^*(\mathscr E_2))",
           r"(f^*(\mathscr E_1),f^*(\mathscr E_2))",
           "The statement (a) and the display (21.13.2.1) have f_V^* (ℰ_1, ℰ_2 are O_V-Modules); here the print drops the V. Classed as a misprint (medium: it could be read as an abuse of notation); the TeX silently corrects, the fix restores the printed reading. Apply AFTER the inline entry just above.",
           corrected=r"(f_V^*(\mathscr E_1),f_V^*(\mathscr E_2))"))
L.append(F(314, "proof of (21.13.2), l. 5: 'et que Hom_O_W(ℰ_1|W, ℰ_2|W) = Γ(W, ℋom_O_V(ℰ_1, ℰ_2)), la condition signifie'",
           "formula in the running text, comma after it (crop p314_hom2_line.png)", "displayed formula (comma inside the display)",
           "other", None, "high",
           r"\[¶  \operatorname{Hom}_{\mathcal O_W}(\mathscr E_1|W,\mathscr E_2|W)¶  =\Gamma(W,\mathscr Hom_{\mathcal O_V}(\mathscr E_1,\mathscr E_2)),¶\]",
           r"$\operatorname{Hom}_{\mathcal O_W}(\mathscr E_1|W,\mathscr E_2|W)¶=\Gamma(W,\mathscr Hom_{\mathcal O_V}(\mathscr E_1,\mathscr E_2))$,",
           "Set inline as printed."))
L.append(F(314, "proof of (21.13.2): 'isomorphe à ℰ̌_1 ⊗_O_V ℰ_2'", "check accent over ℰ (ℰ̌_1), the print's dual (crop p314_check_comma.png)",
           "\\mathscr E_1^\\vee (superscript vee)", "symbol", None, "high",
           r"$\mathscr E_1^\vee\otimes_{\mathcal O_V}\mathscr E_2$", r"$\check{\mathscr E}_1\otimes_{\mathcal O_V}\mathscr E_2$",
           "Independent of the comma entry below (no overlap)."))
L.append(F(314, "proof of (21.13.2): '... ℰ̌_1 ⊗ ℰ_2 (0_I, 5.4.2) est aussi localement libre'",
           "no comma after '(0_I, 5.4.2)' (crop p314_check_comma.png)", "comma after the reference: silent correction",
           "misprint_in_print", None, "medium", r"5.4.2)$, est aussi", r"5.4.2)$ est aussi",
           "The apposition 'isomorphe à ... (0_I, 5.4.2)' opened by a comma is not closed in the print; the TeX silently adds the comma. The fix restores the printed reading.",
           corrected=r"5.4.2)$, est aussi"))
L.append(F(314, "proof of (21.13.2): 'cela montre déjà que b) entraîne a), et inversement b) est un cas particulier de a),'",
           "labels italic, letter and parenthesis (crop p314_s4_labels.png)", "$b)$: italic letter, upright parenthesis",
           "italics", None, "high",
           r"déjà que $b)$ entraîne $a)$, et inversement $b)$ est un cas particulier de $a)$,",
           r"déjà que \emph{b)} entraîne \emph{a)}, et inversement \emph{b)} est un cas particulier de \emph{a)},",
           "GLOBAL_ISSUES 88."))
L.append(F(314, "proof of (21.13.2): 'Il est clair que a') est un cas particulier de a) et b') un cas particulier de a').'",
           "labels italic (crop p314_s4_labels.png)", "math labels: italic letter, upright parenthesis", "italics", None, "high",
           r"Il est clair que $a')$ est un cas particulier de $a)$ et $b')$ un cas particulier de¶$a')$.",
           r"Il est clair que \emph{a$'$)} est un cas particulier de \emph{a)} et \emph{b$'$)} un cas particulier de¶\emph{a$'$)}.",
           "Primed labels written \\emph{b$'$)} as on IV-4 pp. 204, 211-212."))
L.append(F(314, "proof of (21.13.2): 'Inversement, comme b) est une propriété locale'", "label italic (crop p314_s4_labels.png)",
           "$b)$", "italics", None, "high", r"comme $b)$ est une propriété locale", r"comme \emph{b)} est une propriété locale"))
L.append(F(314, "proof of (21.13.2): 'et cela montre que b') entraîne b).'", "labels italic (crop p314_s4_labels.png)",
           "$b')$, $b)$", "italics", None, "high", r"cela montre que $b')$ entraîne¶$b)$.",
           r"cela montre que \emph{b$'$)} entraîne¶\emph{b)}."))

# ---------------- checks ----------------
bad = 0
for d in L:
    if d["fix"] is None:
        continue
    txt = open(f"{RUN}/page_{d['page']}.tex", encoding="utf-8").read()
    n = txt.count(d["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/MISSING", d["page"], n, repr(d["fix"]["old"])[:120])
# the misprint f^* old must also survive the inline edit on p. 314
t = open(f"{RUN}/page_314.tex", encoding="utf-8").read()
for d in L:
    if d["page"] == 314 and d["kind"] == "other" and d["fix"]["old"].startswith("\\[\n  \\operatorname{Hom}_{\\mathcal O_V}"):
        t2 = t.replace(d["fix"]["old"], d["fix"]["new"])
        print("misprint old after inline edit:", t2.count("(f_V^*(\\mathscr E_1),f_V^*(\\mathscr E_2))"))
# apply all fixes in order per page on copies to make sure they chain
for p in (310, 311, 312, 313, 314):
    t = open(f"{RUN}/page_{p}.tex", encoding="utf-8").read()
    for d in L:
        if d["page"] != p or d["fix"] is None:
            continue
        c = t.count(d["fix"]["old"])
        if c != 1:
            bad += 1
            print("CHAIN FAIL", p, c, repr(d["fix"]["old"])[:100])
        t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
# uniqueness in the current source file, and chained application there
SRC = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-21c-fr.tex"
s = open(SRC, encoding="utf-8").read()
for d in L:
    if d["fix"] is None:
        continue
    c = s.count(d["fix"]["old"])
    if c != 1:
        bad += 1
        print("SOURCE NOT UNIQUE", d["page"], c, repr(d["fix"]["old"])[:100])
for d in L:
    if d["fix"] is None:
        continue
    c = s.count(d["fix"]["old"])
    if c != 1:
        bad += 1
        print("SOURCE CHAIN FAIL", d["page"], c, repr(d["fix"]["old"])[:100])
    s = s.replace(d["fix"]["old"], d["fix"]["new"], 1)
print("entries:", len(L), "problems:", bad)
from collections import Counter
cnt = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in (310, 311, 312, 313, 314):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
if bad == 0 and "--write" in sys.argv:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(L, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
