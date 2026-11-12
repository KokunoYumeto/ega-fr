"""Build findings_046_050.json (raw strings; <NL> stands for a line break) and check every fix's old text."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_046_050.json"
NL = "<NL>"
SUB7 = "Long dash for the subtraction (GLOBAL_ISSUES 23); \\setmin as proposed for convention 7, pending that decision."


def F(page, where, scan, tex, kind, old, new, conf="high", conv=None, note="", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------- page 46 ----------------
L.append(F(46, "(17.2.14), first sentence: '(resp. sup_{x∈X}(dim. inj(ℱ_x))).'",
           "(resp. sup_{x∈X}(dim. inj(ℱ_x))). -- three closing parentheses (enlarged crop)",
           "(resp. $\\sup_{x\\in X}(\\operatorname{dim.inj}(\\mathscr{F}_x))$. -- two; the parenthesis opened by '(resp.' is not closed",
           "missing", r"(\mathscr{F}_x))$. On appelle", r"(\mathscr{F}_x))$). On appelle",
           note="Missing closing parenthesis of the '(resp. ...' clause."))
L.append(F(46, "proof of (17.3.1), 1st paragraph: 'l'opérateur bord est nul en toutes dimensions'",
           "est *nul* en toutes dimensions (nul italic)", "est nul en toutes dimensions (upright)",
           "italics", r"est nul en toutes", r"est \emph{nul} en toutes"))
L.append(F(46, "proof of (17.3.1): 'H_0(K_•(x)) = A/(x_1A + ... + x_nA) = A/m = k'",
           "x_1A + . . . + x_nA, dots on the baseline (enlarged crop)", "x_1A+\\cdots+x_nA (centred dots)",
           "symbol", r"x_1A+\cdots+x_nA", r"x_1A+\ldots+x_nA",
           note="As GLOBAL_ISSUES item 22 (\\cdots for the print's baseline dots)."))
L.append(F(46, "Lemme (17.3.1.2): 'Si tout élément de m—m² est diviseur de zéro dans A'",
           "𝔪—𝔪² (long dash, set difference)", "$\\mathfrak{m}-\\mathfrak{m}^2$",
           "convention", r"$\mathfrak{m}-\mathfrak{m}^2$ est diviseur", r"$\mathfrak{m}\setmin\mathfrak{m}^2$ est diviseur",
           conv=7))
L.append(F(46, "proof of (17.3.1.2): 'L'hypothèse entraîne que m—m² est contenu dans la réunion'",
           "𝔪—𝔪² (long dash, set difference)", "$\\mathfrak{m}-\\mathfrak{m}^2$",
           "convention", r"$\mathfrak{m}-\mathfrak{m}^2$ est contenu", r"$\mathfrak{m}\setmin\mathfrak{m}^2$ est contenu",
           conv=7))
L.append(F(46, "proof of (17.3.1.2), last line: 'chap. IV, § 1, n° 1, cor. 3 de la prop. 2'",
           "n° 1 (n with a superior o)", "no~1 (prints 'no 1')",
           "symbol", r"no~1", r"n\textsuperscript{o}~1",
           note="Same form as the n\\textsuperscript{o} used elsewhere in ega0-17-fr.tex (p. 50) and the earlier no~ fixes (III pp. 142-143, 172)."))
# ---------------- page 47 ----------------
L.append(F(47, "line 1: 'donc dans l'un des p_i puisque m⊄m²'",
           "l'un des 𝔭_i puisque (no comma; enlarged crop)", "l'un des $\\mathfrak{p}_i$, puisque",
           "punctuation", r"l'un des $\mathfrak{p}_i$, puisque", r"l'un des $\mathfrak{p}_i$ puisque"))
L.append(F(47, "line 2: '(Bourbaki, Alg. comm., chap. II, § 1, n° 1, prop. 2)'",
           "n° 1", "no~1", "symbol", r"no~1", r"n\textsuperscript{o}~1"))
L.append(F(47, "Lemme (17.3.1.3): 'Si a∈m—m², m/Aa est isomorphe'",
           "a∈𝔪—𝔪² (long dash, set difference)", "$a\\in\\mathfrak{m}-\\mathfrak{m}^2$",
           "convention", r"a\in\mathfrak{m}-\mathfrak{m}^2$, $\mathfrak{m}/Aa", r"a\in\mathfrak{m}\setmin\mathfrak{m}^2$, $\mathfrak{m}/Aa",
           conv=7))
L.append(F(47, "proof of (17.3.1.4): 'dim. proj_A(N) = h—1 (17.2.2, (iii))'",
           "h—1 (long dash)", "h-1", "convention", r"=h-1$ (17.2.2, (iii))", r"=h\setmin 1$ (17.2.2, (iii))",
           conv=7, note=SUB7))
L.append(F(47, "proof of (17.3.1.4): '(A/aA)-module de dimension projective ≤h—1'",
           "≤h—1 (long dash)", "\\leq h-1", "convention", r"$\leq h-1$, et comme", r"$\leq h\setmin 1$, et comme",
           conv=7, note=SUB7))
L.append(F(47, "case I: 'I. — Supposons d'abord'",
           "I. -- roman capital, regular weight (enlarged crop)", "\\textbf{I.} (bold)",
           "font", r"\textbf{I.} --- Supposons", r"I. --- Supposons",
           note="Only the label's weight; \\medskip\\noindent (layout) left as is."))
L.append(F(47, "case I: 'tout élément de m—m² soit diviseur de zéro dans A'",
           "𝔪—𝔪² (long dash, set difference)", "$\\mathfrak{m}-\\mathfrak{m}^2$",
           "convention", r"$\mathfrak{m}-\mathfrak{m}^2$ soit diviseur", r"$\mathfrak{m}\setmin\mathfrak{m}^2$ soit diviseur",
           conv=7))
L.append(F(47, "case I: '(Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5)'",
           "n° 2", "no~2", "symbol", r"no~2", r"n\textsuperscript{o}~2"))
L.append(F(47, "case II: 'II. — On peut donc se borner'",
           "II. -- roman capitals, regular weight (enlarged crop)", "\\textbf{II.} (bold)",
           "font", r"\textbf{II.} --- On peut", r"II. --- On peut",
           note="Only the label's weight; \\medskip\\noindent (layout) left as is."))
L.append(F(47, "case II: 'il existe a∈m—m² qui est un élément A-régulier'",
           "a∈𝔪—𝔪² (long dash, set difference)", "$a\\in\\mathfrak{m}-\\mathfrak{m}^2$",
           "convention", r"a\in\mathfrak{m}-\mathfrak{m}^2$ qui est", r"a\in\mathfrak{m}\setmin\mathfrak{m}^2$ qui est",
           conv=7))
# ---------------- page 48 ----------------
L.append(F(48, "line 1: 'il est clair que rg_k(m'/m'²) = n—1'",
           "n—1 (long dash)", "n-1", "convention", r"=n-1$. En vertu", r"=n\setmin 1$. En vertu",
           conv=7, note=SUB7))
L.append(F(48, "Proposition (17.3.3), line 1: 'ρ : A→B un homomorphisme local'",
           "ρ : A→B (Greek rho, checked on an enlarged crop against the φ of 'les φ(x_i)' in b))",
           "$\\varphi:A\\longrightarrow B$ (silently corrected)",
           "misprint_in_print", r"\varphi:A", r"\rho:A", corrected=r"\varphi:A",
           note="The TeX silently corrects the print; the fix restores the printed rho. The homomorphism is φ in the rest of "
                "the proposition and its proof ('les φ(x_i)' in b), 'y_i = φ(x_i)'). Not to be confused with Corollaire (17.3.5)(ii), "
                "p. 50, whose own homomorphism is ρ in print and TeX."))
L.append(F(48, "Proposition (17.3.3): 'm (resp. n) l'idéal maximal'",
           "(resp. 𝔫) upright inside the italic statement", "italic (statement environment)",
           "convention", r"$\mathfrak{m}$ (resp.<NL>$\mathfrak{n}$)", r"$\mathfrak{m}$ \textup{(resp.<NL>$\mathfrak{n}$)}",
           conv=6, note="The whole parenthetical, parentheses included, is upright in the print."))
L.append(F(48, "Proposition (17.3.3): 'l'idéal maximal de A (resp. B)'",
           "(resp. B) upright", "italic", "convention", r"maximal de $A$ (resp. $B$),", r"maximal de $A$ \textup{(resp. $B$)},",
           conv=6))
L.append(F(48, "Proposition (17.3.3): 'k = A/m (resp. k' = B/n) le corps résiduel'",
           "(resp. k' = B/𝔫) upright", "italic", "convention", r"(resp. $k'=B/\mathfrak{n}$)", r"\textup{(resp. $k'=B/\mathfrak{n}$)}",
           conv=6))
L.append(F(48, "Proposition (17.3.3): 'le corps résiduel de A (resp. B).'",
           "(resp. B) upright", "italic", "convention", r"résiduel de $A$<NL>(resp. $B$).", r"résiduel de $A$<NL>\textup{(resp. $B$)}.",
           conv=6))
for lab in ["a", "b", "c", "d", "e"]:
    L.append(F(48, "Proposition (17.3.3)(ii): label %s)" % lab,
               "%s) italic" % lab, "\\item[\\rm %s)] (upright)" % lab,
               "italics", r"\item[\rm %s)]" % lab, r"\item[\textit{%s)}]" % lab,
               note="Lettered labels are italic here (GLOBAL_ISSUES 16/22: page by page)." if lab == "a" else ""))
L.append(F(48, "Proposition (17.3.3)(ii) a): 'l'homomorphisme ψ (17.3.3.1) est injectif'",
           "(17.3.3.1) upright inside the italic statement", "italic",
           "convention", r"$\psi$ (17.3.3.1) est", r"$\psi$ \textup{(17.3.3.1)} est", conv=6))
L.append(F(48, "Proposition (17.3.3)(ii) b): '(auquel cas cette propriété a lieu pour tout système régulier de paramètres de A)'",
           "the parenthetical is roman, only 'tout' italic", "italic parenthetical with an upright 'tout' (\\emph inside the italic statement)",
           "convention",
           r"(auquel cas cette propriété a<NL>    lieu pour \emph{tout} système régulier de paramètres de $A$)",
           r"\textup{(auquel cas cette propriété a<NL>    lieu pour \emph{tout} système régulier de paramètres de $A$)}",
           conv=6, note="Inside \\textup the \\emph makes 'tout' italic, as printed."))
L.append(F(48, "proof of (17.3.3)(ii): 'la suite des y_i = φ(x_i) est B-régulière'",
           "y_i = φ(x_i) with both subscripts i in a heavy bold italic fount (crops at 5x and 10x against the normal i of '(x_i)' on the line above)",
           "$y_i=\\varphi(x_i)$ (ordinary subscripts)",
           "misprint_in_print", r"$y_i=\varphi(x_i)$", r"$y_{\boldsymbol{i}}=\varphi(x_{\boldsymbol{i}})$",
           conf="medium", corrected=r"$y_i=\varphi(x_i)$",
           note="Wrong fount in the print (GLOBAL_ISSUES 29: wrong-fount letters are recorded as misprints and kept in the diplomatic text); "
                "the TeX silently corrects it. Only the two subscripts are heavy; y and x are ordinary italic."))
L.append(F(48, "proof of (17.3.3)(ii): 'On voit donc que les conditions b), d) et e) équivalent'",
           "b), d), e) italic", "upright", "italics",
           r"conditions b), d) et e) équivalent", r"conditions \emph{b)}, \emph{d)} et \emph{e)} équivalent"))
L.append(F(48, "proof of (17.3.3)(ii): 'qui s'écrit aussi dim(B/mB) = dim(B)—m'",
           "dim(B)—m (long dash)", "\\dim(B)-m", "convention", r"=\dim(B)-m$", r"=\dim(B)\setmin m$",
           conv=7, note=SUB7))
for lab in ["b", "d", "e"]:
    L.append(F(48, "proof of (17.3.3)(ii): label %s')" % lab,
               "%s') italic" % lab, "\\item[\\rm %s')] (upright)" % lab,
               "italics", r"\item[\rm %s')]" % lab, r"\item[\textit{%s')}]" % lab))
L.append(F(48, "proof of (17.3.3)(ii), after the list: 'Or, b') et e') sont équivalentes'",
           "new indented paragraph", "no blank line after \\end{enumerate}: the sentence continues the paragraph unindented",
           "other", r"\end{enumerate}<NL>Or,", r"\end{enumerate}<NL><NL>Or,", conf="medium",
           note="Independent of the next edit (either order)."))
L.append(F(48, "proof of (17.3.3)(ii): 'Or, b') et e') sont équivalentes'",
           "b'), e') italic", "upright", "italics", r"Or, b') et e') sont", r"Or, \emph{b')} et \emph{e')} sont"))
L.append(F(48, "proof of (17.3.3)(ii): 'et comme d') entraîne e') (16.4.1)'",
           "d'), e') italic", "upright", "italics",
           r"comme d') entraîne<NL>e') (16.4.1)", r"comme \emph{d')} entraîne<NL>\emph{e')} (16.4.1)"))
L.append(F(48, "proof of (17.3.3)(ii), last line: 'et est entraînée par b')'",
           "entra₁née: a small lowered figure 1 in place of î (enlarged crop)", "entraînée (silently corrected)",
           "misprint_in_print", r"entraînée", r"entra\textsubscript{1}née", corrected=r"entraînée",
           note="Wrong sort in the print; the TeX silently corrects it. The fix restores the printed reading."))
L.append(F(48, "proof of (17.3.3)(ii), last line: 'est entraînée par b') (17.1.7)'",
           "b') italic", "upright", "italics", r"par b') (17.1.7)", r"par \emph{b')} (17.1.7)"))
# ---------------- page 49 ----------------
L.append(F(49, "line 1: 'de b) et d) implique trivialement c)'",
           "b), d), c) italic", "upright", "italics",
           r"de b) et d) implique trivialement c),", r"de \emph{b)} et \emph{d)} implique trivialement \emph{c)},"))
L.append(F(49, "line 1: 'et en vertu de (i), c) entraîne d);'",
           "c), d) italic; (i) upright", "upright", "italics",
           r"(i), c) entraîne d)~;", r"(i), \emph{c)} entraîne \emph{d)}~;"))
L.append(F(49, "line 2: 'l'équivalence de b), c), d) et e).'",
           "b), c), d), e) italic", "upright", "italics",
           r"l'équivalence de b), c), d) et e).", r"l'équivalence de \emph{b)}, \emph{c)}, \emph{d)} et \emph{e)}."))
L.append(F(49, "line 2: 'il est clair que b) entraîne a)'",
           "b), a) italic", "upright", "italics",
           r"clair que b)<NL>entraîne a), les", r"clair que \emph{b)}<NL>entraîne \emph{a)}, les"))
L.append(F(49, "line 5: 'Reste donc à prouver que a) entraîne e).'",
           "a), e) italic", "upright", "italics",
           r"prouver que a)<NL>entraîne e). Posons", r"prouver que \emph{a)}<NL>entraîne \emph{e)}. Posons"))
L.append(F(49, "after (17.3.3.4): 'Enfin, dans l'anneau local B⊗_A k = B/mB'",
           "new indented paragraph", "no blank line after \\end{equation}: continues unindented",
           "other", r"\end{equation}<NL>Enfin, dans", r"\end{equation}<NL><NL>Enfin, dans", conf="medium"))
L.append(F(49, "(17.3.3.5): 'dim(B⊗_A k) ≤ rg_k' W — rg_k' ψ(V⊗_k k').'",
           "long dash", "-", "convention",
           r"-\operatorname{rg}_{k'}\psi(V\otimes_k k').", r"\setmin\operatorname{rg}_{k'}\psi(V\otimes_k k').",
           conv=7, note=SUB7))
L.append(F(49, "after (17.3.3.5): 'Enfin, puisque B est supposé régulier'",
           "new indented paragraph", "no blank line after \\end{equation}: continues unindented",
           "other", r"\end{equation}<NL>Enfin, puisque", r"\end{equation}<NL><NL>Enfin, puisque", conf="medium"))
L.append(F(49, "unnumbered display: '... ≤ rg_k' W + rg_k'(V⊗_k k') — rg_k' ψ(V⊗_k k')'",
           "long dash", "-", "convention",
           r"-\operatorname{rg}_{k'}\psi(V\otimes_k k')<NL>\]", r"\setmin\operatorname{rg}_{k'}\psi(V\otimes_k k')<NL>\]",
           conv=7, note=SUB7))
L.append(F(49, "'La condition a) entraîne donc nécessairement'",
           "a) italic", "upright", "italics", r"La condition a) entraîne", r"La condition \emph{a)} entraîne"))
L.append(F(49, "end of the proof of (17.3.3): 'on a donc bien prouvé que a) entraîne e).'",
           "a), e) italic", "upright", "italics", r"prouvé que a) entraîne e).", r"prouvé que \emph{a)} entraîne \emph{e)}."))
L.append(F(49, "proof of (17.3.4): '... on a bien dim. proj(M) = n. Supposons maintenant m>0'",
           "'Supposons maintenant' continues the paragraph (starts at the left margin, not indented)",
           "blank line: new paragraph", "other", r"=n$.<NL><NL>Supposons", r"=n$.<NL>Supposons", conf="medium"))
L.append(F(49, "proof of (17.3.4): 'prof(M/xM) = m—1'",
           "m—1 (long dash)", "m-1", "convention", r"=m-1$", r"=m\setmin 1$", conv=7, note=SUB7))
# ---------------- page 50 ----------------
L.append(F(50, "Corollaire (17.3.5)(ii): '(ou, ce qui revient au même (16.1.5), que dim(B) = dim(A))'",
           "the parenthetical is roman inside the italic statement", "italic",
           "convention", r"(ou, ce qui<NL>  revient au même (16.1.5), que $\dim(B)=\dim(A)$)",
           r"\textup{(ou, ce qui<NL>  revient au même (16.1.5), que $\dim(B)=\dim(A)$)}", conv=6))
L.append(F(50, "proof of (17.3.5)(ii): 'équivaut à dire que B est un A-module de Cohen-Macaulay'",
           "A-*module* (module italic)", "upright", "italics",
           r"un $A$-module de Cohen-Macaulay (16.5.3)", r"un $A$-\emph{module} de Cohen-Macaulay (16.5.3)"))
L.append(F(50, "proof of (17.3.5)(ii): 'puisque dim B = dim A (16.1.5)'",
           "dim B = dim A, no parentheses (enlarged crop)", "$\\dim(B)=\\dim(A)$",
           "formula", r"puisque $\dim(B)=\dim(A)$", r"puisque $\dim B=\dim A$"))
L.append(F(50, "(17.3.6): 'lorsque A lui-même est un anneau local, il résulte'",
           "*local* italic", "upright", "italics", r"un anneau local, il résulte", r"un anneau \emph{local}, il résulte"))
L.append(F(50, "(17.3.6): 'Pour que A soit régulier, il suffit, en vertu de (17.3.2)'",
           "*suffit* italic", "upright", "italics", r"il suffit, en vertu", r"il \emph{suffit}, en vertu"))
L.append(F(50, "proof of (17.3.7): 'où p = q∩A (0_I, 6.3.1)'",
           "bold 0 in (0_I, 6.3.1)", "$0_{\\mathrm I}$", "convention",
           r"$0_{\mathrm I}$, 6.3.1", r"$\mathbf{0}_{\mathrm I}$, 6.3.1", conv=2))
L.append(F(50, "proof of (17.3.8.1): 'pour tout idéal maximal n de Â'",
           "*maximal* italic", "upright", "italics", r"tout idéal maximal<NL>$\mathfrak{n}$", r"tout idéal \emph{maximal}<NL>$\mathfrak{n}$"))

# ---------------- checks ----------------
ok = True
texts = {p: (RUN / ("page_%03d.tex" % p)).read_bytes().decode("utf-8").replace("\r\n", "\n") for p in range(46, 51)}
for p, t in texts.items():
    if "\r" in t:
        print("stray CR in page", p)
# the release source file (LF): every old must also occur there
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-17-fr.tex")
src = SRC.read_bytes().decode("utf-8")
print("source has CR:", "\r" in src)
a = src.index("\\oldpage[0\\textsubscript{IV-1}]{46}")
b = src.index("\\oldpage[0\\textsubscript{IV-1}]{51}") if "\\oldpage[0\\textsubscript{IV-1}]{51}" in src else len(src)
seg = src[a:b]
for x in L:
    if x["fix"] and seg.count(x["fix"]["old"]) < 1:
        ok = False
        print("NOT IN SOURCE SEGMENT", x["page"], repr(x["fix"]["old"]))
for i, x in enumerate(L):
    if x["fix"] is None:
        continue
    n = texts[x["page"]].count(x["fix"]["old"])
    if n != 1:
        ok = False
        print("COUNT", n, "page", x["page"], repr(x["fix"]["old"]))
# sequential application, in list order, on each page
for p in range(46, 51):
    t = texts[p]
    for x in L:
        if x["page"] != p or x["fix"] is None:
            continue
        o, nw = x["fix"]["old"], x["fix"]["new"]
        if t.count(o) != 1:
            ok = False
            print("SEQ", t.count(o), "page", p, repr(o))
            continue
        t = t.replace(o, nw)
# counts per page
for p in range(46, 51):
    rows = [x for x in L if x["page"] == p]
    c = sum(1 for x in rows if x["kind"] == "convention")
    m = sum(1 for x in rows if x["kind"] == "misprint_in_print")
    print("p.%d %d/%d/%d" % (p, len(rows) - c - m, c, m))
print("total", len(L), "ok" if ok else "PROBLEMS")
if ok:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
