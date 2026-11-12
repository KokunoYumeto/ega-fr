import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_II"
OUT = os.path.join(RUN, "findings_135_139.json")
NL = "\n"


def L(*parts):
    return NL.join(parts)


F = []


def add(page, where, scan, tex, kind, conv, conf, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


def c2(page, where, ref, bold):
    # convention 2: bold chapter number in a reference
    add(page, where, "(%s) with bold %s" % (ref, bold),
        "(%s) with plain %s in the link text" % (ref, bold),
        "convention", 2, "high",
        fx("{" + ref + "}", "{\\textbf{" + bold + "}" + ref[len(bold):] + "}"))


def c1(page, where, old, new, note=""):
    add(page, where, "k(..) with bold italic k", "plain k", "convention", 1, "high",
        fx(old, new), note)


# ---------------------------------------------------------------- page 135
c2(135, "proof of (6.6.11): 'Comme B_i (x) R(X_i) est un préfaisceau constant (I, 7.3.5)'",
   "I, 7.3.5", "I")
c2(135, "proof of (6.6.11): 'induit sur l'ouvert g^{-1}(U_j) (I, 9.5.11)'", "I, 9.5.11", "I")
add(135, "proof of (6.6.11), construction of X'': 'et pour chaque λ, k/k_{i_λ}=n_{i_λ} préschémas isomorphes à X'_{i_λ}'",
    "k/k_{i_λ}=n_{i_λ}", "$k/k_{i_\\lambda}$ (the '=n_{i_\\lambda}' is missing)", "formula", None, "high",
    fx(r"$k/k_{i_\lambda}$ préschémas", r"$k/k_{i_\lambda}=n_{i_\lambda}$ préschémas"),
    "Checked on an enlarged crop; n_i=k/k_i is defined in the preceding sentence.")
add(135, "proof of (6.6.11): 'se réduisant à l'injection canonique dans chacun des sommandes de X''",
    "sommandes", "summandes", "word", None, "high", fx("summandes", "sommandes"),
    "Checked on an enlarged crop.")
c2(135, "proof of (6.6.11): 'compte tenu de (I, 7.3.3)'", "I, 7.3.3", "I")
add(135, "end of the proof of (6.6.11): 'pour tout ouvert affine T de X, (g'_*(O_{X''}) (x)_{O_X} R(X))|T est un (R(X)|T)-Module'",
    "formula inline in the running text", "displayed \\[ ... \\]", "other", None, "high",
    fx(L(r"affine $T$ de $X$,", r"\[", r"\bigl(g'_*(\mathcal{O}_{X''})",
         r"\otimes_{\mathcal{O}_X}\mathcal{R}(X)\bigr)|T", r"\]", r"est un"),
       L(r"affine $T$ de $X$,",
         r"$\bigl(g'_*(\mathcal{O}_{X''})\otimes_{\mathcal{O}_X}\mathcal{R}(X)\bigr)|T$",
         r"est un")),
    "Layout only (display vs inline); the formula itself matches.")
add(135, "Corollaire (6.6.12): 'Si, dans l'énoncé de (6.6.11), on a W=X'",
    "(6.6.11) upright (roman parentheses and figures) inside the italic statement",
    "italic (corollary environment)", "convention", 6, "high",
    fx(r"(\hyperref[II.6.6.11-fr]{6.6.11})", r"\textup{(\hyperref[II.6.6.11-fr]{6.6.11})}"),
    "Checked on a crop.")
add(135, "Remarque (6.6.13): 'au sous-préschéma fermé réduit de X ayant X—W pour espace sous-jacent'",
    "long dash X—W (set difference)", "$X-W$", "convention", 7, "high",
    fx(r"$X-W$", r"$X\setmin W$"), "\\setmin is not yet the long dash (global change pending).")
add(135, "Remarque (6.6.13): 'bien que O_{X'} le soit (5.1.2) et que le morphisme X'->X soit fini surjectif'",
    "(5.1.2)", "(5.1.12), linked to II.5.1.12-fr", "number", None, "high",
    fx(r"(\hyperref[II.5.1.12-fr]{5.1.12}) et que", r"(\hyperref[II.5.1.2-fr]{5.1.2}) et que"),
    "Checked on an enlarged crop. The print is right: by (5.1.2) c') O_X is ample when X is "
    "quasi-affine, which is the claim here for the quasi-affine X'. The (5.1.12) earlier on this "
    "page (g'^*(L) ample) is correct and stays. Label II.5.1.2-fr exists.")

# ---------------------------------------------------------------- page 136
add(136, "proof of (6.7.1): 'puisque Y est noethérien (I, 6.1.7), on voit qu'on peut supposer Y réduit'",
    "(I, 6.1.7) with bold I", "(I, 6.1.7) with plain I in the link text", "convention", 2, "high",
    fx(r"{I, 6.1.7}), on voit", r"{\textbf{I}, 6.1.7}), on voit"))
c2(136, "proof of (6.7.1): 'ayant Y' comme espace sous-jacent (I, 5.1.2)'", "I, 5.1.2", "I")
c2(136, "proof of (6.7.1): 'canoniquement isomorphe à X x_Y Y' (I, 4.4.1)'", "I, 4.4.1", "I")
c2(136, "proof of (6.7.1): 'principe de récurrence noethérienne (0, 2.2.2)'", "0, 2.2.2", "0")
add(136, "proof of (6.7.1): 'on peut donc (compte tenu de (I, 6.1.7)) se ramener'",
    "(compte tenu de (I, 6.1.7)): the reference in its own parentheses",
    "(compte tenu de I, 6.1.7): the inner parentheses are missing", "punctuation", None, "high",
    fx(L(r"(compte tenu de", r"\hyperref[I.6.1.7-fr]{I, 6.1.7}) se ramener"),
       L(r"(compte tenu de", r"(\hyperref[I.6.1.7-fr]{\textbf{I}, 6.1.7})) se ramener")),
    "Checked on a crop. The edit also sets the bold I of this reference (convention 2; next entry, fix null), since the two changes overlap.")
add(136, "proof of (6.7.1): 'compte tenu de (I, 6.1.7)) se ramener', bold I",
    "(I, 6.1.7) with bold I", "(I, 6.1.7) with plain I in the link text", "convention", 2, "high",
    None, "Applied by the punctuation entry above (same reference).")
add(136, "proof of (6.7.1): 'sous l'hypothèse que pour toute partie fermée Y'≠Y, tout sous-préschéma'",
    "only 'toute' in italics", "\\emph covers 'toute partie fermée Y'≠Y'", "italics", None, "high",
    fx(r"\emph{toute partie fermée $Y'\neq Y$}", r"\emph{toute} partie fermée $Y'\neq Y$"),
    "Checked on a crop.")
c2(136, "proof of (6.7.1): 'on ait F=j_*(j^*(F)) (I, 9.3.5)'", "I, 9.3.5", "I")
c2(136, "proof of (6.7.1): 'H^1(Y', j^*(F))=0 d'après (I, 5.1.9.2)'", "I, 5.1.9.2", "I")
add(136, "proof of (6.7.1): 'Supposons d'abord que Y ne soit pas irréductible, et soient Y' une composante irréductible de Y'",
    "soient", "soit", "word", None, "high",
    fx(r"et soit $Y'$ une", r"et soient $Y'$ une"),
    "Checked on a crop (plural: the sentence introduces Y' and Y'').")
add(136, "proof of (6.7.1): 'et Y''=Y—Y'; on désignera encore par Y''",
    "long dash Y—Y' (set difference)", "$Y''=Y-Y'$", "convention", 7, "high",
    fx(r"$Y''=Y-Y'$", r"$Y''=Y\setmin Y'$"), "\\setmin is not yet the long dash (global change pending).")
c2(136, "proof of (6.7.1): 'rho : F->F'=j_*(j^*(F)) (0, 4.4.3)'", "0, 4.4.3", "0")
c2(136, "proof of (6.7.1): 'cohérent en vertu de (0, 5.3.10)'", "0, 5.3.10", "0")
c2(136, "proof of (6.7.1): 'et (0, 5.3.12), car on a'", "0, 5.3.12", "0")
c2(136, "proof of (6.7.1): 'sont aussi des O_Y-Modules cohérents (0, 5.3.4)'", "0, 5.3.4", "0")
c2(136, "proof of (6.7.1): 'les composantes irréductibles de X (I, 5.2.1)'", "I, 5.2.1", "I")
add(136, "proof of (6.7.1), reduction to X intègre: 'et par g_i la restriction de g à X_i, un des g_i au moins est dominant'",
    "g_i ... g ... g_i", "f_i ... f ... f_i (silently corrected)", "misprint_in_print", None, "high",
    fx(r"$f_i$ la restriction de $f$ à $X_i$, un des $f_i$ au moins",
       r"$g_i$ la restriction de $g$ à $X_i$, un des $g_i$ au moins"),
    "Checked on a crop. The morphism of (6.7.1) is f : X->Y and no g is defined in this proof "
    "(the letter matches g : X'->X of (6.6.11)). The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$f_i$ la restriction de $f$ à $X_i$, un des $f_i$ au moins")
add(136, "Lemme (6.7.1.1): 'x (resp. y) le point générique'",
    "'(resp. y)' upright inside the italic statement", "italic (lemma environment)",
    "convention", 6, "high", fx(r"(resp. $y$)", r"\textup{(resp. $y$)}"), "Checked on a crop.")
add(136, "Lemme (6.7.1.1): 'le point générique de X (resp. Y)'",
    "'(resp. Y)' upright inside the italic statement", "italic (lemma environment)",
    "convention", 6, "high", fx(r"(resp. $Y$)", r"\textup{(resp. $Y$)}"), "Checked on a crop.")

# ---------------------------------------------------------------- page 137
add(137, "proof of (6.7.1.1): 'La fibre f^{-1}(y)=X x_Y Spec(k(y))=X x_Y Spec(O_y) s'identifie à Spec(K)'",
    "formula inline in the running text", "displayed \\[ ... \\]", "other", None, "high",
    fx(L(r"La fibre", r"\[", r"f^{-1}(y)=X\times_Y\operatorname{Spec}(k(y))",
         r"=X\times_Y\operatorname{Spec}(\mathcal{O}_y)", r"\]", r"s'identifie"),
       L(r"La fibre",
         r"$f^{-1}(y)=X\times_Y\operatorname{Spec}(\boldsymbol{k}(y))=X\times_Y\operatorname{Spec}(\mathcal{O}_y)$",
         r"s'identifie")),
    "Layout (display vs inline). The edit also sets the bold italic k of k(y) (convention 1; next entry, fix null), since the two changes overlap.")
add(137, "proof of (6.7.1.1): 'X x_Y Spec(k(y))'", "k(y) with bold italic k", "plain k",
    "convention", 1, "high", None,
    "Applied by the display-to-inline entry above. Checked on an enlarged crop; the other k on this "
    "page (k=O_y, 'extension de rang fini de k', 'base de K sur k', 'sur k, g_x') are plain italic in the print.")
c2(137, "proof of (6.7.1.1): 's'identifie à Spec(K) (I, 3.6.6)'", "I, 3.6.6", "I")
F[-1]["note"] = "The link target is I.3.6.5-fr (EGA I has no label I.3.6.6-fr); the link text matches the print."
c2(137, "proof of (6.7.1.1): 'de L^{(x)n} au-dessus de X (I, 9.3.1)'", "I, 9.3.1", "I")
c2(137, "proof of (6.7.1.1): 'u : O_Y^m->f_*(L^{(x)n}) (0, 5.1.1)'", "0, 5.1.1", "0")
c2(137, "proof of (6.7.1.1): 'f_*(L^{(x)n})|U=(M_[phi])~ (I, 1.6.3) est cohérent'", "I, 1.6.3", "I")
add(137, "proof of (6.7.1.1): 'u_y=theta_y est l'homomorphisme theta(x)1 : K^m=C^m(x)K->M_[phi](x)K; or ce dernier'",
    "formula inline, followed by a semicolon", "displayed \\[ ... \\] ending with a comma",
    "punctuation", None, "high",
    fx(L(r"l'homomorphisme", r"\[", r"\theta\otimes1:K^m=C^m\otimes K\longrightarrow",
         r"M_{[\varphi]}\otimes K,", r"\]", r"or ce dernier"),
       L(r"l'homomorphisme",
         r"$\theta\otimes1:K^m=C^m\otimes K\longrightarrow M_{[\varphi]}\otimes K$~;",
         r"or ce dernier")),
    "Checked on a crop. Two differences in one edit: ',' -> ';' and display -> inline.")
c2(137, "proof of (6.7.1.1): 'ces O_Y-Modules sont cohérents (0, 5.3.3)'", "0, 5.3.3", "0")
c2(137, "proof of (6.7.1.1): 'leurs supports sont fermés (0, 5.2.2)'", "0, 5.2.2", "0")
c2(137, "proof of (6.7.1): 'puisque X est affine (I, 1.1.10)'", "I, 1.1.10", "I")
add(137, "proof of (6.7.1): 'Montrons d'abord que v est injectif : par hypothèse T=Coker u a un support'",
    "no comma after 'par hypothèse'", "'par hypothèse,'", "punctuation", None, "high",
    fx(L(r"par hypothèse,", r"$\mathcal{T}"), L(r"par hypothèse", r"$\mathcal{T}")),
    "Checked on a crop.")
add(137, "proof of (6.7.1): 'donc est un O_Y-Module de torsion (I, 7.4.6)'",
    "'de torsion' in italics", "upright", "italics", None, "high",
    fx(r"-Module de torsion", r"-Module \emph{de torsion}"), "Checked on a crop.")
c2(137, "proof of (6.7.1): 'un O_Y-Module de torsion (I, 7.4.6)'", "I, 7.4.6", "I")
c2(137, "proof of (6.7.1): 'Hom_A(T, F)=0 (0, 5.2.6)'", "0, 5.2.6", "0")

# ---------------------------------------------------------------- page 138
c2(138, "end of the proof of (6.7.1): 'sont des O_Y-Modules cohérents (0, 5.3.4 et 5.3.5)'",
   "0, 5.3.4", "0")
add(138, "end of the proof of (6.7.1): 'D'autre part, G est un B-Module cohérent (I, 9.6.4)'",
    "'B-Module' in italics (hyphen and 'Module' italic)", "upright '-Module'", "italics", None, "high",
    fx(r"$\mathcal{B}$-Module cohérent", r"\emph{$\mathcal{B}$-Module} cohérent"),
    "Checked on an enlarged crop.")
c2(138, "end of the proof of (6.7.1): 'B-Module cohérent (I, 9.6.4)'", "I, 9.6.4", "I")
c2(138, "end of the proof of (6.7.1): 'on a H^1(X, K)=0 (I, 5.1.9.2)'", "I, 5.1.9.2", "I")
add(138, "Corollaire (6.7.3): 'Pour qu'un préschéma noethérien X soit affine il faut et il suffit que'",
    "no comma after 'affine'", "'soit affine, il faut'", "punctuation", None, "high",
    fx(r"noethérien $X$ soit affine, il faut", r"noethérien $X$ soit affine il faut"),
    "Checked on a crop. Corollaire (6.7.2) above does print the comma ('Pour que X soit affine, il faut').")
c2(138, "(7.1.1): 'pour la relation de domination (I, 8.1.1)'", "I, 8.1.1", "I")

# ---------------------------------------------------------------- page 139
add(139, "(7.1.2), l. 2: 'qui domine A ([1], p. 1-07, lemme 2)'",
    "([1], p. 1-07, lemme 2)", "(\\cite[p.~1-07, lemme~2]{I-1}), which prints ([1, p. 1-07, lemme 2])",
    "punctuation", None, "high",
    fx(r"(\cite[p.~1-07, lemme~2]{I-1})", r"(\cite{I-1}, p.~1-07, lemme~2)"),
    "GLOBAL_ISSUES item 27; same form of fix as pp. 118-122. \\bibitem{I-1} is the first item of bib-fr.tex, so \\cite{I-1} prints [1].")
add(139, "(7.1.2): 'de sorte que L' soit le corps des restes de cette valuation ([24], p. 98)'",
    "([24], p. 98)", "(\\cite[p.~98]{II-24}), which prints ([24, p. 98])", "punctuation", None, "high",
    fx(r"(\cite[p.~98]{II-24})", r"(\cite{II-24}, p.~98)"),
    "As above; \\bibitem[24]{II-24} prints [24].")
add(139, "(7.1.3): 'ayant K pour corps des fractions ([11], p. 51, th. 2)'",
    "([11], p. 51, th. 2)", "(\\cite[p.~51, th.~2]{I-11}), which prints ([11, p. 51, th. 2])",
    "punctuation", None, "high",
    fx(r"(\cite[p.~51, th.~2]{I-11})", r"(\cite{I-11}, p.~51, th.~2)"),
    "As above; \\bibitem{I-11} is the 11th item of bib-fr.tex.")
add(139, "Proposition (7.1.4): 'y'≠y une spécialisation (0, 2.1.2) de y'",
    "(0, 2.1.2) upright (roman parentheses and figures) inside the italic statement",
    "italic (proposition environment)", "convention", 6, "high",
    fx(r"(\hyperref[0.2.1.2-fr]{0, 2.1.2})", r"\textup{(\hyperref[0.2.1.2-fr]{\textbf{0}, 2.1.2})}"),
    "Checked on a crop. The edit also sets the bold 0 (convention 2; next entry, fix null), since the two changes overlap.")
add(139, "Proposition (7.1.4): 'une spécialisation (0, 2.1.2)', bold 0",
    "(0, 2.1.2) with bold 0", "(0, 2.1.2) with plain 0 in the link text", "convention", 2, "high",
    None, "Applied by the convention-6 entry above.")
add(139, "Proposition (7.1.4) (i): 'Y' est le spectre d'un anneau de valuation complet dont le corps des restes'",
    "'complet' in the italic of the statement (no change of face)",
    "\\emph{complet} inside the italic proposition environment, which sets it upright",
    "convention", 6, "high", fx(L(r"\emph{complet}", r"dont"), L(r"complet", r"dont")),
    "Checked on a crop. The \\emph{complet} of (7.1.2), in roman text, is right and stays.")
c1(139, "Proposition (7.1.4) (i): 'il existe un k(y)-homomorphisme k(x)->k(b)', k(y)",
   r"$k(y)$-homo", r"$\boldsymbol{k}(y)$-homo", "Checked on a crop.")
c1(139, "Proposition (7.1.4) (i): 'k(y)-homomorphisme k(x)->k(b)', k(x)",
   r"morphisme $k(x)", r"morphisme $\boldsymbol{k}(x)")
c1(139, "Proposition (7.1.4) (i): 'k(x)->k(b)', k(b)", r"\to k(b)$", r"\to \boldsymbol{k}(b)$")
c1(139, "Proposition (7.1.4) (ii): 'Il existe un k(y)-isomorphisme k(x)~>k(b)', k(y)",
   r"$k(y)$-iso", r"$\boldsymbol{k}(y)$-iso")
c1(139, "Proposition (7.1.4) (ii): 'k(x)~>k(b)', k(x)", r"$k(x)\xrightarrow", r"$\boldsymbol{k}(x)\xrightarrow")
c1(139, "Proposition (7.1.4) (ii): 'k(x)~>k(b)', k(b)", r"{\sim}k(b)$", r"{\sim}\boldsymbol{k}(b)$")
c2(139, "proof of (7.1.4): 'ayant {y}- comme espace sous-jacent (I, 5.2.1)'", "I, 5.2.1", "I")
c1(139, "proof of (7.1.4): 'et que k(x) est le même dans X et dans X_1'",
   r"que $k(x)$ est le même", r"que $\boldsymbol{k}(x)$ est le même", "Checked on a crop.")
c1(139, "proof of (7.1.4): 'dont le corps des fractions est O_y=k(y)'",
   r"\mathcal{O}_y=k(y)$", r"\mathcal{O}_y=\boldsymbol{k}(y)$")
c1(139, "proof of (7.1.4): 'et k(x) est une extension de k(y)', k(x)",
   r"et $k(x)$ est une", r"et $\boldsymbol{k}(x)$ est une")
c1(139, "proof of (7.1.4): 'une extension de k(y). Pour réaliser'",
   r"de $k(y)$. Pour", r"de $\boldsymbol{k}(y)$. Pour")
c1(139, "proof of (7.1.4): 'algébriquement clos extension de k(x) (resp. un'",
   r"clos extension de $k(x)$", r"clos extension de $\boldsymbol{k}(x)$")
c1(139, "proof of (7.1.4): 'dominant O_{y'} et dont k(x) est le corps des fractions'",
   r"et dont $k(x)$ est le corps", r"et dont $\boldsymbol{k}(x)$ est le corps")

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for p in sorted({d["page"] for d in F}):
    with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")
work = dict(texts)
for i, d in enumerate(F):
    for key in ("where", "scan", "tex", "note"):
        if any(ord(ch) < 32 for ch in d[key]):
            print("CONTROL CHAR in", key, "entry", i); ok = False
    if d["fix"] is None:
        continue
    old, new = d["fix"]["old"], d["fix"]["new"]
    for s in (old, new):
        if any(ord(ch) < 32 and ch != "\n" for ch in s):
            print("CONTROL CHAR in fix, entry", i, repr(s)); ok = False
    n = texts[d["page"]].count(old)
    if n != 1:
        print("NOT UNIQUE (%d) page %d entry %d: %r" % (n, d["page"], i, old)); ok = False
    m = work[d["page"]].count(old)
    if m != 1:
        print("SEQUENTIAL CLASH (%d) page %d entry %d: %r" % (m, d["page"], i, old)); ok = False
    else:
        work[d["page"]] = work[d["page"]].replace(old, new)
    if "corrected" in d and d["kind"] != "misprint_in_print":
        print("corrected on non-misprint", i); ok = False

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print("entries:", len(F))
for p in sorted(counts):
    print(p, "normal/convention/misprint = %d/%d/%d" % tuple(counts[p]))
conv = {}
for d in F:
    if d["kind"] == "convention":
        conv.setdefault(d["page"], {}).setdefault(d["convention"], 0)
        conv[d["page"]][d["convention"]] += 1
print("conventions by page:", conv)
if not ok:
    print("CHECKS FAILED; not writing")
    sys.exit(1)
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("written", OUT)
