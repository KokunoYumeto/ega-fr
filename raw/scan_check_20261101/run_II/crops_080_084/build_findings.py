# Builds findings_080_084.json and checks that every fix "old" occurs exactly once
# in its LF-normalised page_NNN.tex.
import json

RUN = r"user/Documents/ega_scan_check_20261101/run_II"
OUT = RUN + r"/findings_080_084.json"
N = "\n"

F = []


def add(page, where, scan, tex, kind, fix_old, fix_new, note="", convention=None,
        confidence="high", corrected=None, nofix=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
    }
    if nofix:
        d["fix"] = None
    else:
        d["fix"] = {"old": fix_old, "new": fix_new}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 80
add(80, "end of the proof of (4.4.4): 'On voit donc que a) et b) sont équivalents.'",
    "a) and b) in italics", "a) et b) upright", "italics",
    r"que a) et b) sont", r"que \emph{a)} et \emph{b)} sont",
    "Checked on the strip.")
add(80, "proof of Corollaire (4.4.5): 'la condition b) de (4.4.4) est locale sur Y'",
    "b) in italics", "b) upright", "italics",
    r"la condition b) de", r"la condition \emph{b)} de")
add(80, "Proposition (4.4.6): 'q : X→Y un morphisme de type fini, ℒ un 𝒪_X-Module inversible'",
    "'de type fini' set in roman inside the italic statement",
    "plain 'de type fini' (italic in the proposition environment)", "convention",
    r"un morphisme de type fini,", r"un morphisme \textup{de type fini},",
    "Checked on an enlarged crop.", convention=6)
add(80, "Proposition (4.4.6): 'Les conditions a) et b) de (4.4.4) sont alors équivalentes aux suivantes'",
    "a), b) and the reference (4.4.4) in roman inside the italic statement",
    "a), b) and (4.4.4) italic in the proposition environment", "convention",
    r"Les conditions a) et b) de" + N + r"(\hyperref[II.4.4.4-fr]{4.4.4}) sont alors",
    r"Les conditions \textup{a)} et \textup{b)} de" + N + r"\textup{(\hyperref[II.4.4.4-fr]{4.4.4})} sont alors",
    "Checked on an enlarged crop.", convention=6)
add(80, "Proposition (4.4.6) a'): 'un 𝒪_Y-Module quasi-cohérent de type fini ℰ'",
    "'de type fini' in roman inside the italic item",
    "plain 'de type fini' (italic in the environment)", "convention",
    r"quasi-cohérent de type" + N + r"  fini $\mathcal{E}$ et un",
    r"quasi-cohérent \textup{de type" + N + r"  fini} $\mathcal{E}$ et un",
    "Checked on an enlarged crop.", convention=6)
add(80, "Proposition (4.4.6) b'): 'un sous-𝒪_Y-Module cohérent de type fini ℰ de q_*(ℒ)'",
    "'de type fini' in roman inside the italic item",
    "plain 'de type fini' (italic in the environment)", "convention",
    r"Module cohérent de type" + N + r"  fini $\mathcal{E}$ de",
    r"Module cohérent \textup{de type" + N + r"  fini} $\mathcal{E}$ de",
    "Checked on an enlarged crop. Does not overlap the misprint entry for the same line (that one needs no edit).",
    convention=6)
add(80, "Proposition (4.4.6) b'): 'Il existe un sous-𝒪_Y-Module cohérent de type fini ℰ de q_*(ℒ)'",
    "cohérent (read on an enlarged crop)",
    "sous-$\\mathcal{O}_Y$-Module cohérent de type (keeps the printed reading)",
    "misprint_in_print", None, None,
    "The TeX keeps the printed reading. The proof obtains b') from b) 'de même' by (4.4.1), whose part (ii) "
    "yields a quasi-coherent sub-module of finite type, and a') reads 'quasi-cohérent de type fini'; a coherent "
    "Module is already of finite type, and a quasi-coherent sub-module of finite type need not be coherent when Y "
    "is only quasi-compact or has a noetherian underlying space. The corrected edition "
    "(editions/2026-10-24-r20/current) already reads 'quasi-cohérent'. Not in the authors' errata (ega3-7-fr.tex, ega4-errata-addenda-list3-fr.tex).",
    confidence="medium",
    corrected=r"sous-$\mathcal{O}_Y$-Module quasi-cohérent de type fini",
    nofix=True)
add(80, "Proposition (4.4.6) b'): 'ayant les propriétés énoncées dans a')'",
    "a') in roman inside the italic item", "a') italic in the environment", "convention",
    r"énoncées dans" + N + r"  a').", r"énoncées dans" + N + r"  \textup{a')}.",
    "Checked on an enlarged crop.", convention=6)
add(80, "proof of (4.4.6): 'Il est clair que a') ou b') implique a); d'autre part a) implique a')'",
    "a'), b'), a), a), a') in italics", "all upright", "italics",
    r"Il est clair que a') ou b') implique a)~; d'autre part a) implique a') en",
    r"Il est clair que \emph{a')} ou \emph{b')} implique \emph{a)}~; d'autre part \emph{a)} implique \emph{a')} en")
add(80, "proof of (4.4.6): 'et de même b) implique b').'",
    "b), b') in italics", "upright", "italics",
    r"et de même b) implique b').", r"et de même \emph{b)} implique \emph{b')}.")
add(80, "Corollaire (4.4.7): 'et une Y-immersion ouverte dominante i : X→P=Proj(𝒮)'",
    "'ouverte dominante' in roman inside the italic statement",
    "plain 'ouverte dominante' (italic in the corollary environment)", "convention",
    r"$Y$-immersion ouverte dominante", r"$Y$-immersion \textup{ouverte dominante}",
    "Checked on an enlarged crop ('de type fini' in the same statement is italic, as in the TeX).",
    convention=6)
add(80, "proof of (4.4.7): 'En effet, la condition b') de (4.4.6) est vérifiée'",
    "b') in italics", "b') upright", "italics",
    r"la condition b') de", r"la condition \emph{b')} de")
add(80, "proof of (4.4.7): 'Soit Z l'adhérence (I, 9.5.11)'",
    "bold I", "plain I", "convention",
    r"{I, 9.5.11}", r"{\textbf{I}, 9.5.11}",
    "The corrected edition (editions/2026-10-24-r20/current) changes this reference to (I, 9.5.10). The printed "
    "(I, 9.5.11) is not reported as a misprint: the word 'adhérence' is defined in the paragraph that ends (I, 9.5.11) "
    "(the authors' erratum '(I, 9.5.11) Ligne 7 de la p. 179' in ega3-7-fr.tex refers to that paragraph); "
    "(I, 9.5.10) proves the existence of the closure.",
    convention=2)
add(80, "end of the page: '... un 𝒪_Y-Module quasi-cohérent ℰ et une' (the sentence continues on p. 81 'Y-immersion r : X→P ...')",
    "the sentence runs on to p. 81; no paragraph break",
    "blank line after 'et une', before \\oldpage[II]{81}", "other",
    r"quasi-cohérent $\mathcal{E}$ et une" + N + N,
    r"quasi-cohérent $\mathcal{E}$ et une" + N,
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20); apply together with the "
    "p. 81 finding that removes the blank line after \\oldpage[II]{81} (both blank lines must go).",
    confidence="high")

# ---------------------------------------------------------------- page 81
add(81, "top of the page: 'Y-immersion r : X→P=P(ℰ) telle que' (continuation of the proof of (4.4.8))",
    "continues the sentence from p. 80; first line not indented",
    "blank line after \\oldpage[II]{81}: a new paragraph", "other",
    r"\oldpage[II]{81}" + N + N + r"$Y$-immersion",
    r"\oldpage[II]{81}" + N + r"$Y$-immersion",
    "Apply together with the p. 80 finding that removes the blank line before the marker.")
add(81, "proof of (4.4.8): 'il en est de même de r'' : X →(r, r') P×_YP' →ς Q'",
    "label over the first arrow: (r, r') with no subscript Y (enlarged crop)",
    "\\xrightarrow{(r,r')_Y}", "formula",
    r"\xrightarrow{(r,r')_Y}", r"\xrightarrow{(r,r')}",
    "The subscript Y is printed only in '(r, r')_Y : X→P×_YP'' two lines above.")
add(81, "proof of (4.4.8): '(r, r')_Y : X→P×_YP' (I, 5.3.14)'",
    "bold I", "plain I", "convention", r"{I, 5.3.14}", r"{\textbf{I}, 5.3.14}", convention=2)
add(81, "proof of (4.4.8): 'donc (I, 9.1.4), r''*(𝒪_Q(1)) est isomorphe à ℒ⊗ℒ''",
    "bold I", "plain I", "convention", r"{I, 9.1.4}), $r''^*", r"{\textbf{I}, 9.1.4}), $r''^*", convention=2)
add(81, "proof of (4.4.9): 'est isomorphe à ℒ (0, 5.4.3 et 5.4.5)'",
    "bold 0", "plain 0", "convention", r"{0, 5.4.3}", r"{\textbf{0}, 5.4.3}", convention=2)
add(81, "Proposition (4.4.10), item label '(i bis)'",
    "label '(i bis)' with 'bis' in italics, '(i' and ')' roman (enlarged crop)",
    "\\item[\\rm{(i bis)}]: all upright", "italics",
    r"\item[\rm{(i bis)}]", r"\item[\rm{(i \emph{bis})}]",
    "\\emph after \\rm gives italic. The same italic 'bis' recurs in every '(i bis)' of the proof (pp. 81-83).")
add(81, "proof of (4.4.10): 'La propriété (i bis) découle aussitôt'",
    "'bis' in italics", "'bis' upright", "italics",
    r"La propriété (i bis) découle", r"La propriété (i \emph{bis}) découle")
add(81, "proof of (4.4.10): 'se déduit formellement de (i bis) et de (v)'",
    "'bis' in italics", "'bis' upright", "italics",
    r"formellement de (i bis) et de (v)", r"formellement de (i \emph{bis}) et de (v)")
add(81, "proof of (4.4.10): 'calqué sur celui de (I, 5.5.12), que nous laissons au lecteur'",
    "bold I", "plain I", "convention", r"{I, 5.5.12}), que nous", r"{\textbf{I}, 5.5.12}), que nous",
    convention=2)
add(81, "proof of (4.4.10): 'comme dans (I, 5.5.12), la factorisation'",
    "bold I", "plain I", "convention", r"{I, 5.5.12}), la factorisation",
    r"{\textbf{I}, 5.5.12}), la factorisation", convention=2)
add(81, "proof of (4.4.10): 'ℒ=Γ_f*(ℒ⊗_{𝒪_Z}𝒪_Y) (I, 9.1.4), et Γ_f est une immersion'",
    "bold I", "plain I", "convention", r"{I, 9.1.4}), et", r"{\textbf{I}, 9.1.4}), et", convention=2)
add(81, "proof of (4.4.10): 'Γ_f est une immersion (I, 5.3.11)'",
    "bold I", "plain I", "convention", r"{I, 5.3.11}", r"{\textbf{I}, 5.3.11}", convention=2)
add(81, "proof of (4.4.10), last line of the page: 'on peut donc appliquer (i bis).'",
    "'bis' in italics", "'bis' upright", "italics",
    r"on peut donc appliquer (i bis).", r"on peut donc appliquer (i \emph{bis}).")

# ---------------------------------------------------------------- page 82
add(82, "proof of (4.4.10)(iii): 'i_{(Y')} est une immersion de X_{(Y')} dans P' (I, 4.3.2)'",
    "bold I", "plain I", "convention", r"{I, 4.3.2}", r"{\textbf{I}, 4.3.2}", convention=2)
add(82, "proof of (4.4.10)(iv): 'X_1×_SX_2 dans P_1×_SP_2 (I, 4.3.1)'",
    "bold I", "plain I", "convention", r"{I, 4.3.1}", r"{\textbf{I}, 4.3.1}", convention=2)
add(82, "proof of (4.4.10)(iv): '(basé notamment sur (I, 9.1.9.1 et 9.1.2))'",
    "bold I", "plain I", "convention", r"{I, 9.1.9.1}", r"{\textbf{I}, 9.1.9.1}", convention=2)
add(82, "proof of (4.4.10)(ii): 'donc X et Y sont des schémas quasi-compacts.'",
    "'schémas' in italics", "upright", "italics",
    r"sont des schémas quasi-compacts.", r"sont des \emph{schémas} quasi-compacts.",
    "Checked on an enlarged crop.")
add(82, "proof of (4.4.10)(ii): 'où ℰ est un 𝒪_Y-Module quasi-cohérent de type fini et ℒ=r*(𝒪_P(1))'",
    "'de type fini' in italics", "upright", "italics",
    r"quasi-cohérent de type fini et", r"quasi-cohérent \emph{de type fini} et",
    "Checked on an enlarged crop.")
add(82, "proof of (4.4.10)(ii): 'un 𝒪_P-Module ℳ très ample relativement au morphisme composé'",
    "'très ample' in italics", "upright", "italics",
    r"$\mathcal{M}$ très ample relativement", r"$\mathcal{M}$ \emph{très ample} relativement",
    "Checked on an enlarged crop.")
add(82, "proof of (4.4.10)(ii): 'la conclusion résultera de (i bis).'",
    "'bis' in italics", "'bis' upright", "italics",
    r"résultera de (i bis).", r"résultera de (i \emph{bis}).")

# ---------------------------------------------------------------- page 83
add(83, "end of the proof of (4.4.10): 'en vertu de (i bis), et 𝒪_P(1) est isomorphe à'",
    "'bis' in italics", "'bis' upright", "italics",
    r"(i bis), et", r"(i \emph{bis}), et")
add(83, "Proposition (4.4.11): 'X'' le préschéma somme X⨿X''",
    "small coproduct sign ⨿ (enlarged crop)", "\\sqcup (⊔)", "symbol",
    r"$X\sqcup X'$", r"$X\amalg X'$",
    "Same as GLOBAL_ISSUES item 6 and the run_II p. 11 finding.")
add(83, "Proposition (4.4.11): 'qui coïncide avec f (resp. f') dans X'",
    "'(resp. f')' roman inside the italic statement", "italic in the environment", "convention",
    r"(resp." + N + r"$f'$)", r"\textup{(resp." + N + r"$f'$)}", "Enlarged crop.", convention=6)
add(83, "Proposition (4.4.11): 'dans X (resp. X').'",
    "'(resp. X')' roman inside the italic statement", "italic in the environment", "convention",
    r"(resp. $X'$)", r"\textup{(resp. $X'$)}", "Enlarged crop.", convention=6)
add(83, "Proposition (4.4.11): 'Soit ℒ (resp. ℒ') un 𝒪_X-Module'",
    "'(resp. ℒ')' roman inside the italic statement", "italic in the environment", "convention",
    r"(resp. $\mathcal{L}'$)", r"\textup{(resp. $\mathcal{L}'$)}", "Enlarged crop.", convention=6)
add(83, "Proposition (4.4.11): '(resp. un 𝒪_{X'}-Module) inversible'",
    "'(resp.' and ')' roman, 'un 𝒪_{X'}-Module' italic", "all italic in the environment", "convention",
    r"(resp. un $\mathcal{O}_{X'}$-Module)",
    r"\textup{(resp.} un $\mathcal{O}_{X'}$-Module\textup{)}",
    "Enlarged crop. Form of the fix as in the run_II p. 9 finding.", convention=6)
add(83, "Proposition (4.4.11), last words: 'et ℒ' très ample relativement à f.'",
    "relativement à f. (no prime; enlarged crop)", "relativement à $f'$. (silently corrected)",
    "misprint_in_print",
    r"ample relativement à $f'$.", r"ample relativement à $f$.",
    "The TeX silently corrects the print; the fix restores the printed reading. ℒ' lives on X', so the condition "
    "must be relative to f' : X'→Y (as in the proof: 'si ℒ et ℒ' sont très amples'). Not in the authors' errata "
    "(ega3-7-fr.tex, ega4-errata-addenda-list3-fr.tex); the corrected edition also reads $f'$.",
    confidence="high", corrected=r"ample relativement à $f'$.")
add(83, "proof of (4.4.11): 'en vertu de (4.4.10, (i bis))'",
    "'bis' in italics", "'bis' upright", "italics",
    r"{4.4.10, (i bis)}", r"{4.4.10, (i \emph{bis})}")
add(83, "(4.5.1): 'nous poserons d'autre part S=⊕_{n≥0}Γ(X, ℒ^{⊗n}) (sous-anneau gradué ...'",
    "inline in the running text", "displayed with \\[ \\]", "other",
    r"nous poserons d'autre part" + N + r"\[" + N + r"  S=\bigoplus_{n\geq0}\Gamma(X,\mathcal{L}^{\otimes n})" + N + r"\]" + N + r"(sous-anneau",
    r"nous poserons d'autre part" + N + r"$S=\bigoplus_{n\geq0}\Gamma(X,\mathcal{L}^{\otimes n})$" + N + r"(sous-anneau",
    "Layout: the print sets this formula inline.", confidence="high")
add(83, "(4.5.1): 'sous-anneau gradué de l'anneau Γ_*(ℒ)'",
    "Γ with subscript asterisk * (enlarged crop)", "\\Gamma_\\bullet", "symbol",
    r"$\Gamma_\bullet(\mathcal{L})$", r"$\Gamma_*(\mathcal{L})$",
    "This is the only \\Gamma_\\bullet in ega2-1-fr.tex; it writes \\Gamma_* everywhere else (87 times).")
add(83, "(4.5.1): 'défini dans (0, 5.4.6)'",
    "bold 0", "plain 0", "convention", r"{0, 5.4.6}", r"{\textbf{0}, 5.4.6}", convention=2)
add(83, "(4.5.1): 'entre les homomorphismes p*(S̃)→⊕_{n≥0}ℒ^{⊗n} de 𝒪_X-Algèbres graduées'",
    "inline in the running text", "displayed with \\[ \\]", "other",
    r"entre les homomorphismes" + N + r"\[" + N + r"  p^*(\widetilde{S})\longrightarrow" + N + r"  \bigoplus_{n\geq0}\mathcal{L}^{\otimes n}" + N + r"\]" + N + r"de $\mathcal{O}_X$",
    r"entre les homomorphismes" + N + r"$p^*(\widetilde{S})\longrightarrow\bigoplus_{n\geq0}\mathcal{L}^{\otimes n}$" + N + r"de $\mathcal{O}_X$",
    "Layout: the print sets this formula inline.")
add(83, "(4.5.1): 'les endomorphismes de l'anneau gradué S (I, 2.2.5)'",
    "bold I", "plain I", "convention", r"{I, 2.2.5}", r"{\textbf{I}, 2.2.5}", convention=2)
add(83, "(4.5.1): 'l'homomorphisme ε : p*(S̃)→⊕_{n≥0}ℒ^{⊗n} qui correspond ainsi'",
    "inline in the running text", "displayed with \\[ \\]", "other",
    r"l'homomorphisme" + N + r"\[" + N + r"  \varepsilon:p^*(\widetilde{S})\longrightarrow" + N + r"  \bigoplus_{n\geq0}\mathcal{L}^{\otimes n}" + N + r"\]" + N + r"qui correspond",
    r"l'homomorphisme" + N + r"$\varepsilon:p^*(\widetilde{S})\longrightarrow\bigoplus_{n\geq0}\mathcal{L}^{\otimes n}$" + N + r"qui correspond",
    "Layout: the print sets this formula inline.")
add(83, "(4.5.1): 'à l'automorphisme identique de S sera dit canonique.'",
    "'identique' and 'canonique' in italics", "upright", "italics",
    r"l'automorphisme identique de $S$ sera dit canonique.",
    r"l'automorphisme \emph{identique} de $S$ sera dit \emph{canonique}.")
add(83, "(4.5.1): 'un morphisme G(ε)→Proj(S) qui sera aussi dit canonique.'",
    "'canonique' in italics", "upright", "italics",
    r"qui sera aussi dit canonique.", r"qui sera aussi dit \emph{canonique}.")
add(83, "Théorème (4.5.2) b): 'Le morphisme canonique G(ε)→Proj(S) (4.5.1) est partout défini'",
    "reference (4.5.1) roman inside the italic statement", "italic in the theorem environment", "convention",
    r"(\hyperref[II.4.5.1-fr]{4.5.1}) est partout",
    r"\textup{(\hyperref[II.4.5.1-fr]{4.5.1})} est partout", convention=6)

# ---------------------------------------------------------------- page 84
add(84, "Théorème (4.5.2) c'): 'La propriété c) a lieu pour tout faisceau quasi-cohérent d'idéaux'",
    "c) roman inside the italic item (enlarged crop)", "c) italic in the theorem environment", "convention",
    r"La propriété c) a lieu", r"La propriété \textup{c)} a lieu", convention=6)
add(84, "Théorème (4.5.2), after the items: 'En outre, si (f_α) est une famille ...'",
    "new paragraph: 'En outre' indented",
    "text follows \\end{enumerate} directly (no blank line), so it is set without indentation", "other",
    r"\end{enumerate}" + N + r"En outre", r"\end{enumerate}" + N + N + r"En outre",
    "Paragraph break (indentation) only.", confidence="medium")
add(84, "Théorème (4.5.2), last paragraph: 'd'éléments homogènes de S_+ telle que les X_{f_α} soient affines'",
    "no comma after S_+ (enlarged crop)", "comma after $S_+$", "punctuation",
    r"de $S_+$," + N + r"telle que", r"de $S_+$" + N + r"telle que")
add(84, "proof of (4.5.2): 'Il est clair que b) implique b'), et b') implique a)'",
    "b), b'), b'), a) in italics", "upright", "italics",
    r"Il est clair que b) implique b'), et b') implique a) en vertu",
    r"Il est clair que \emph{b)} implique \emph{b')}, et \emph{b')} implique \emph{a)} en vertu")
add(84, "proof of (4.5.2): 'La condition a) implique a'), car tout x∈X'",
    "a), a') in italics", "upright", "italics",
    r"La condition a) implique a'), car", r"La condition \emph{a)} implique \emph{a')}, car")
add(84, "proof of (4.5.2): 'c'est par suite un ouvert affine (I, 1.3.6)'",
    "bold I", "plain I", "convention", r"{I, 1.3.6}", r"{\textbf{I}, 1.3.6}", convention=2)
add(84, "proof of (4.5.2): 'Pour prouver que a') entraîne b), il suffit'",
    "a'), b) in italics", "upright", "italics",
    r"que a') entraîne b), il suffit", r"que \emph{a')} entraîne \emph{b)}, il suffit")
add(84, "proof of (4.5.2): 'résulte aussitôt de (I, 9.3.1, (i))'",
    "bold I", "plain I", "convention", r"{I, 9.3.1, (i)}", r"{\textbf{I}, 9.3.1, (i)}", convention=2)
add(84, "proof of (4.5.2): 'il suffit d'appliquer (I, 9.3.2)'",
    "bold I", "plain I", "convention", r"{I, 9.3.2}", r"{\textbf{I}, 9.3.2}", convention=2)
add(84, "proof of (4.5.2): 'Donc a), a'), b), b') sont équivalentes.'",
    "a), a'), b), b') in italics", "upright", "italics",
    r"Donc a), a'), b), b') sont", r"Donc \emph{a)}, \emph{a')}, \emph{b)}, \emph{b')} sont")
add(84, "proof of (4.5.2): 'Pour montrer que a') entraîne c), notons'",
    "a'), c) in italics", "upright", "italics",
    r"Pour montrer que a') entraîne c), notons",
    r"Pour montrer que \emph{a')} entraîne \emph{c)}, notons")
add(84, "proof of (4.5.2): 'au-dessus de X_f (I, 1.3.9)'",
    "bold I", "plain I", "convention", r"{I, 1.3.9}", r"{\textbf{I}, 1.3.9}", convention=2)
add(84, "proof of (4.5.2): 'd'autre part (I, 9.3.1, (ii))'",
    "bold I", "plain I", "convention", r"{I, 9.3.1, (ii)}", r"{\textbf{I}, 9.3.1, (ii)}", convention=2)
add(84, "proof of (4.5.2): 'ce qui prouve c). Il est clair que c) implique c'), et il reste à montrer que c') entraîne a).'",
    "c), c), c'), c'), a) in italics", "upright", "italics",
    r"ce qui prouve c). Il est clair" + N + r"que c) implique c'), et il reste à montrer que c') entraîne a).",
    r"ce qui prouve \emph{c)}. Il est clair" + N + r"que \emph{c)} implique \emph{c')}, et il reste à montrer que \emph{c')} entraîne \emph{a)}.")
add(84, "proof of (4.5.2): 'ayant X—U comme espace sous-jacent'",
    "long dash X—U (set difference)", "$X-U$", "convention",
    r"$X-U$", r"$X\setmin U$", convention=7)
add(84, "proof of (4.5.2): 'comme espace sous-jacent (I, 5.2.1)'",
    "bold I", "plain I", "convention", r"{I, 5.2.1}", r"{\textbf{I}, 5.2.1}", convention=2)
add(84, "proof of (4.5.2): 'L'hypothèse c') entraîne qu'il existe'",
    "c') in italics", "upright", "italics",
    r"L'hypothèse c') entraîne", r"L'hypothèse \emph{c')} entraîne")
add(84, "end of the proof of (4.5.2): 'ce qui prouve a).'",
    "a) in italics", "upright", "italics",
    r"qui prouve a).", r"qui prouve \emph{a)}.")
add(84, "paragraph after (4.5.2): 'impliquent que X est un schéma, puisqu'il'",
    "'schéma' in italics", "upright", "italics",
    r"est un schéma, puisqu'il", r"est un \emph{schéma}, puisqu'il")
add(84, "paragraph after (4.5.2): 'isomorphe à un sous-préschéma du schéma S=Proj(A) en vertu de (4.5.2, b))'",
    "S=Proj(A) (enlarged crop)", "$S=\\operatorname{Proj}(A)$ (keeps the printed reading)",
    "misprint_in_print", None, None,
    "The TeX keeps the printed reading. S is the graded ring of (4.5.1) and A is not defined here; by (4.5.2, b)) "
    "X is isomorphic to a sub-prescheme of the scheme Proj(S). The corrected edition "
    "(editions/2026-10-24-r20/current) reads '$P=\\operatorname{Proj}(S)$'. Not in the authors' errata (ega3-7-fr.tex, ega4-errata-addenda-list3-fr.tex).",
    confidence="high", corrected=r"$P=\operatorname{Proj}(S)$", nofix=True)
add(84, "paragraph after (4.5.2): 'en vertu de (4.5.2, b))'",
    "b) in italics", "upright", "italics",
    r"{4.5.2, b)}", r"{4.5.2, \emph{b)}}")
add(84, "Définition (4.5.3): 'ℒ est ample si X est un schéma quasi-compact'",
    "'ample' (the defined word) in roman inside the italic definition (enlarged crop)",
    "plain 'ample' (italic in the definition environment)", "convention",
    r"est ample si", r"est \textup{ample} si", convention=6)
add(84, "Définition (4.5.3): 'les conditions équivalentes de (4.5.2) sont vérifiées'",
    "reference (4.5.2) roman inside the italic definition", "italic in the environment", "convention",
    r"(\hyperref[II.4.5.2-fr]{4.5.2}) sont vérifiées",
    r"\textup{(\hyperref[II.4.5.2-fr]{4.5.2})} sont vérifiées", convention=6)
add(84, "after (4.5.3): 'Il résulte évidemment du critère (4.5.2, a))'",
    "a) in italics", "upright", "italics",
    r"{4.5.2, a)}", r"{4.5.2, \emph{a)}}")
add(84, "after (4.5.3): 'alors, pour tout ouvert U de X, ℒ|U est un (𝒪_X|U)-Module ample.'",
    "pour tout ouvert U de X (no 'quasi-compact'; enlarged crop)",
    "pour tout ouvert $U$ de $X$ (keeps the printed reading)",
    "misprint_in_print", None, None,
    "The TeX keeps the printed reading. An authorial omission rather than a typographical slip: Définition (4.5.3) "
    "requires the scheme to be quasi-compact, so ℒ|U is ample only for quasi-compact U. The corrected edition "
    "(editions/2026-10-24-r20/current) reads 'pour tout ouvert quasi-compact'. Not in the authors' errata in "
    "ega3-7-fr.tex or ega4-errata-addenda-list3-fr.tex.",
    confidence="medium",
    corrected=r"pour tout ouvert quasi-compact $U$ de $X$",
    nofix=True)
add(84, "after (4.5.3): 'que les X_f affines forment déjà une base de la topologie de X'",
    "'affines' and 'base' in italics (enlarged crop)", "upright", "italics",
    r"$X_f$ affines forment déjà une base de",
    r"$X_f$ \emph{affines} forment déjà une \emph{base} de")

# ---------------------------------------------------------------- checks
pages = {}
for p in (80, 81, 82, 83, 84):
    with open(f"{RUN}/page_{p:03d}.tex", encoding="utf-8") as fh:
        pages[p] = fh.read().replace("\r\n", "\n")

bad = 0
spans = {}
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    t = pages[f["page"]]
    n = t.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/ABSENT", f["page"], n, repr(fx["old"]))
        continue
    s = t.index(fx["old"])
    spans.setdefault(f["page"], []).append((s, s + len(fx["old"]), i))
    if fx["old"] == fx["new"]:
        print("NO-OP", f["page"], repr(fx["old"]))
        bad += 1

# overlapping fixes on the same page
for p, lst in spans.items():
    lst.sort()
    for (a0, a1, i), (b0, b1, j) in zip(lst, lst[1:]):
        if b0 < a1:
            bad += 1
            print("OVERLAP", p, repr(F[i]["fix"]["old"]), repr(F[j]["fix"]["old"]))

# apply all fixes per page to be sure they compose
for p, lst in spans.items():
    t = pages[p]
    for s0, s1, i in sorted(lst, reverse=True):
        t = t[:s0] + F[i]["fix"]["new"] + t[s1:]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)

from collections import Counter
c = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in (80, 81, 82, 83, 84):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(F), "problems", bad)
