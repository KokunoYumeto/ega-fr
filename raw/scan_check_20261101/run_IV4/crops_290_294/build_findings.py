"""Build findings_290_294.json and check every fix's old string against the page files and the source file."""
import json
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-21b-fr.tex")
OUT = RUN / "findings_290_294.json"

F = []


def add(page, where, scan, tex, kind, old, new, note, convention=None, confidence="high", corrected=None, nofix=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": None if nofix else {"old": old, "new": new},
    }
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


SEG289 = ("Printed on p. 290; the TeX has this text in its p. 289 segment because marker 290 stands too late "
          "(see the boundary fix), so the old string is taken from page_289.tex (unique in ega4-21b-fr.tex).")

# ---------------------------------------------------------------- p. 290
add(290, "p. 290, (21.10.2) A), B)", "item labels A) B) upright (roman text)", r"label=\emph{\Alph*)} (italic)",
    "italics",
    r"\begin{enumerate}[label=\emph{\Alph*)}]", r"\begin{enumerate}[label=\Alph*)]",
    "The references 'A)', 'B)' in the following text are upright in both.")
add(290, "p. 290, proof of A), last line", "l'image de Z_x par (21.10.1.1) est le nombre λ_x'",
    r"\sref{IV.21.10.1.2}", "misprint_in_print",
    r"par \sref{IV.21.10.1.2} est le nombre", r"par \sref{IV.21.10.1.1} est le nombre",
    "The print cites (21.10.1.1), the formula of the cycle Z; the image of Z_x is taken by the homomorphism "
    "(21.10.1.2). Same slip on p. 291 ('au moyen de l'homomorphisme (21.10.1.1)'). The TeX silently corrects it; "
    "the diplomatic text restores the printed number. Not in Err_IV (Liste 3).",
    corrected=r"par \sref{IV.21.10.1.2} est le nombre")

# ---------------------------------------------------------------- p. 291
add(291, "page break 290/291 (mid-word)",
    "p. 290 ends 'une générisation y' de x' dans T'_0, distincte de x', et puisque x'∈X'^(1), y' serait nécessaire-'; "
    "p. 291 begins 'ment un point maximal de X''",
    "\\oldpage[IV-4]{291} one line too early, before 'une générisation'", "marker",
    "\\oldpage[IV-4]{291}\nune générisation $y'$ de $x'$ dans $T'_0$, distincte de $x'$, et puisque $x'\\in X'^{(1)}$, "
    "$y'$ serait nécessairement un point",
    "une générisation $y'$ de $x'$ dans $T'_0$, distincte de $x'$, et puisque $x'\\in X'^{(1)}$, $y'$ serait "
    "nécessaire%\n\\oldpage[IV-4]{291}\nment un point",
    "Mid-word break split as in the edition's other marker fixes (mor%/phisme). One edit; the moved line joins the "
    "p. 290 segment.")
add(291, "p. 291, (21.10.3) 'Désignons par'", "Γ_T printed with an italic capital Gamma (the Γ of sections is upright)",
    r"\Gamma_T", "font", r"Désignons par $\Gamma_T(", r"Désignons par $\varGamma_T(",
    "Italic Γ_T throughout pp. 291 and 294 (4 occurrences, the only ones in ega4-21b).")
add(291, "p. 291, (21.10.3)", "Γ(U, Γ_T(𝒵¹_X)) with italic Γ_T, upright Γ", r"\Gamma(U,\Gamma_T(", "font",
    r"\Gamma(U,\Gamma_T(", r"\Gamma(U,\varGamma_T(", "See the previous finding.")
add(291, "p. 291, (21.10.3) display", "ψ*(Γ_T(𝒵¹_X)) → 𝒵¹_X' with italic Γ_T", r"\psi^*(\Gamma_T(", "font",
    "\\psi^*(\\Gamma_T(\\mathscr{Z}^1_X))\\to\\mathscr{Z}^1_{X'}\n\\]",
    "\\psi^*(\\varGamma_T(\\mathscr{Z}^1_X))\\to\\mathscr{Z}^1_{X'}\n\\]", "See the previous findings.")
add(291, "p. 291, proof of (21.10.4)", "le sous-préschéma Y(D) with the heavy sans-serif Y", "$Y(D)$", "font",
    r"le sous-préschéma $Y(D)$", r"le sous-préschéma $\boldsymbol{\mathsf{Y}}(D)$",
    "Coordinator decision: \\boldsymbol{\\mathsf{Y}} (as at ega4-21b line 80).")
add(291, "p. 291, proof of (21.10.4)", "cyc(D)=n_y.{y}‾ with a baseline period", r"n_y\cdot\overline{\{y\}}",
    "symbol", r"\operatorname{cyc}(D)=n_y\cdot\overline{\{y\}}", r"\operatorname{cyc}(D)=n_y.\overline{\{y\}}",
    "Baseline period (GLOBAL_ISSUES 65).")
add(291, "p. 291, proof of (21.10.4)", "dans la démonstration de (21.10.2, B))",
    r"\sref{IV.21.10.2}, B) prints '(21.10.2), B)'", "punctuation",
    r"\sref{IV.21.10.2}, B) que les points", r"\sref{IV.21.10.2}[B)] que les points", "")
add(291, "p. 291, proof of (21.10.4)", "la définition de n_x' au moyen de l'homomorphisme (21.10.1.1)",
    r"\sref{IV.21.10.1.2}", "misprint_in_print",
    r"au moyen de l'homomorphisme \sref{IV.21.10.1.2}", r"au moyen de l'homomorphisme \sref{IV.21.10.1.1}",
    "Same slip as on p. 290: the homomorphism is (21.10.1.2). The TeX silently corrects it.",
    corrected=r"au moyen de l'homomorphisme \sref{IV.21.10.1.2}")
add(291, "p. 291, proof of (21.10.4)", "et Y(f*(D))=f^{-1}(Y(D)) with the sans-serif Y twice",
    "$Y(f^*(D))=f^{-1}(Y(D))$", "font",
    r"$Y(f^*(D))=f^{-1}(Y(D))$", r"$\boldsymbol{\mathsf{Y}}(f^*(D))=f^{-1}(\boldsymbol{\mathsf{Y}}(D))$", "")
add(291, "p. 291, proof of (21.10.4)", "est donc la longueur n_x' du ...", "$n'_{x'}$ (renamed)", "formula",
    r"la longueur $n'_{x'}$ du", r"la longueur $n_{x'}$ du",
    "The TeX renames the print's n_x' to n'_x' here and in 'n_x'=λ_x' n_y' (GLOBAL_ISSUES 102/104 pattern).")
add(291, "p. 291, end of the proof of (21.10.4)",
    "inline: '... du O_X',x'-module O_X',x'/t'_x'O_X',x'; comme O_X',x'/t'_x'O_X',x' = (O_X,y/t_yO_X,y)⊗_{O_X,y}O_X',x' "
    "il résulte de (4.7.1) ...'",
    "displayed equation; the module O/t'O before the semicolon is dropped and 'comme' moved after the display",
    "word",
    "$\\sh{O}_{X',x'}$-module\n\\[\n  \\sh{O}_{X',x'}/t'_{x'}\\sh{O}_{X',x'}\n"
    "  =(\\sh{O}_{X,y}/t_y\\sh{O}_{X,y})\\otimes_{\\sh{O}_{X,y}}\\sh{O}_{X',x'};\n\\]\ncomme il résulte",
    "$\\sh{O}_{X',x'}$-module $\\sh{O}_{X',x'}/t'_{x'}\\sh{O}_{X',x'}$;\ncomme "
    "$\\sh{O}_{X',x'}/t'_{x'}\\sh{O}_{X',x'}=(\\sh{O}_{X,y}/t_y\\sh{O}_{X,y})\\otimes_{\\sh{O}_{X,y}}\\sh{O}_{X',x'}$ "
    "il résulte",
    "Rewording of the print (GLOBAL_ISSUES 102/104, inline formula set as a display): restored word by word; the "
    "print has no comma before 'il résulte'.")
add(291, "p. 291, end of the proof of (21.10.4)", "que l'on a n_x'=λ_x'n_y", "$n'_{x'}=\\lambda_{x'}n_y$",
    "formula", r"$n'_{x'}=\lambda_{x'}n_y$", r"$n_{x'}=\lambda_{x'}n_y$", "Renamed variable (see above).")
add(291, "p. 291, end of the proof of (21.10.4)", "n_y, donc les multiplicités", "'donc' missing", "missing",
    r"n_y$, les multiplicités", r"n_y$, donc les multiplicités", "")
add(292, "page break 291/292 (TeX p. 292 segment; removal)",
    "p. 291 ends with the first three lines of (21.10.5) '... f vérifie les conditions'",
    "\\oldpage[IV-4]{292} right after the (21.10.5) heading", "marker",
    "\\oldpage[IV-4]{292}\nSupposons maintenant", "Supposons maintenant",
    "Apply together with the next finding (insertion of the marker before 'de (21.10.1)'). After the move the "
    "text 'Supposons ... les conditions' belongs to the p. 291 segment.")
add(292, "page break 291/292 (insertion)", "p. 292 begins 'de (21.10.1); cela signifie encore'",
    "marker missing there", "marker",
    r"$f$ vérifie les conditions de \sref{IV.21.10.1};",
    "$f$ vérifie les conditions\n\\oldpage[IV-4]{292}\nde \\sref{IV.21.10.1};",
    "Apply together with the previous finding (removal of the old marker).")
add(292, "p. 291, last line (21.10.5) (TeX p. 292 segment)", "pour *toute partie fermée rare* T de X",
    "upright", "italics",
    r"pour toute partie fermée rare $T$ de $X$", r"pour \emph{toute partie fermée rare} $T$ de $X$",
    "Printed on p. 291 (in the TeX's p. 292 segment until the marker move; old string unaffected by the move).")

# ---------------------------------------------------------------- p. 292
add(292, "p. 292, l. 1-2 (21.10.5)", "ou bien x=f(x') est *point maximal* de X", "upright", "italics",
    "est point maximal de $X$, ou bien $x'$ vérifie l'une des conditions (ii), (iii) de",
    "est \\emph{point maximal} de $X$, ou bien $x'$ vérifie l'une des conditions (ii), (iii) de", "")
add(292, "p. 292, (21.10.5)", "un support *rare* dans X", "upright", "italics",
    r"un support rare dans $X$", r"un support \emph{rare} dans $X$", "")
add(292, "p. 292, (21.10.5)", "est défini pour *tout* cycle", "upright", "italics",
    r"on voit que $f^*(Z)$ est défini pour tout cycle", r"on voit que $f^*(Z)$ est défini pour \emph{tout} cycle", "")
add(292, "p. 292, (21.10.5)", "un *homomorphisme de faisceaux de groupes commutatifs ordonnés*", "upright", "italics",
    r"on a donc défini ainsi un homomorphisme de faisceaux de groupes commutatifs ordonnés",
    r"on a donc défini ainsi un \emph{homomorphisme de faisceaux de groupes commutatifs ordonnés}", "")
add(292, "p. 292, (21.10.5) after the display", "'Si de plus, pour tout diviseur D' begins an indented paragraph",
    "no blank line after \\]", "other",
    "\\]\nSi de plus, pour tout diviseur", "\\]\n\nSi de plus, pour tout diviseur", "")
add(292, "p. 292, Proposition (21.10.8)", "f (resp. g) est plat: 'resp.' and the parentheses upright",
    r"(resp.\ $g$) italic", "convention",
    r"que $f$ (resp.\ $g$) est plat", r"que $f$ \textup{(resp.\ $g$)} est plat", "", convention=6)
add(292, "p. 292, Proposition (21.10.8)", "dans X' (resp. X''): upright", r"(resp.\ $X''$) italic", "convention",
    "dans $X'$ (resp.\\ $X''$).\nAlors", "dans $X'$ \\textup{(resp.\\ $X''$)}.\nAlors", "", convention=6)
add(292, "p. 292, proof of (21.10.8), first display", "long(...) . long(O_X',x'/m_x O_X',x') with a baseline period",
    r"\cdot", "symbol",
    r"\cdot\operatorname{long}(\sh{O}_{X',x'}/", r".\operatorname{long}(\sh{O}_{X',x'}/",
    "Baseline period (GLOBAL_ISSUES 65).")
add(292, "p. 292, proof of (21.10.8), first display", "no full stop after the display", "final '.'", "extra",
    "\\mathfrak{m}_x\\sh{O}_{X',x'}).\n\\]", "\\mathfrak{m}_x\\sh{O}_{X',x'})\n\\]",
    "The next line 'En effet, ...' continues the sentence (flush left).")
add(292, "p. 292, proof of (21.10.8), second display", "long_A'(A'/mA') . long_A''(A''/m'A'') with a baseline period",
    r"\cdot", "symbol",
    r"\cdot\operatorname{long}_{A''}(A''/\mathfrak{m}'A'')", r".\operatorname{long}_{A''}(A''/\mathfrak{m}'A'')",
    "Baseline period (GLOBAL_ISSUES 65).")
add(292, "p. 292, (21.10.9)", "les faisceaux *simples* sur X", "upright", "italics",
    r"les faisceaux simples sur $X$", r"les faisceaux \emph{simples} sur $X$", "")
add(292, "p. 292, (21.10.9)", "(0_I, 3.6): bold 0 with a light subscript I", r"\sref[0]{0.3.6} prints '(0, 3.6)'",
    "missing", r"$\Lambda$ \sref[0]{0.3.6}", r"$\Lambda$ \sref[$\mathbf{0}_{\mathrm I}$]{0.3.6}", "")
add(292, "p. 292, (21.10.9)",
    "On appelle faisceau des germes de cycles 1-codimensionnels *à coefficients dans* Λ le faisceau",
    "the whole phrase 'faisceau ... dans Λ' in \\emph", "italics",
    r"On appelle \emph{faisceau des germes de cycles $1$-codimensionnels à coefficients dans $\Lambda$} le faisceau",
    r"On appelle faisceau des germes de cycles $1$-codimensionnels \emph{à coefficients dans} $\Lambda$ le faisceau",
    "Only 'à coefficients dans' is italic in the print.")

# ---------------------------------------------------------------- p. 293
add(293, "p. 293, (21.10.10) l. 3", "un cycle 1-codimensionnel *à coefficients rationnels* sur X'", "upright",
    "italics",
    r"un cycle $1$-codimensionnel à coefficients rationnels sur $X'$",
    r"un cycle $1$-codimensionnel \emph{à coefficients rationnels} sur $X'$", "")
add(293, "p. 293, (21.10.10) (iv)", "m_x∉Ass(O_X,x) *et en outre, si l'on pose* (no comma; 'et' italic)",
    r"$..., et \emph{en outre, si l'on pose}", "italics",
    r"\operatorname{Ass}(\sh{O}_{X,x})$, et \emph{en outre, si l'on pose}",
    r"\operatorname{Ass}(\sh{O}_{X,x})$ \emph{et en outre, si l'on pose}",
    "Two differences in one edit: the TeX adds a comma after Ass(O_X,x) and sets 'et' upright.")
add(293, "p. 293, (21.10.10) (iv)", "*alors* A' *est une* A-*algèbre* finie *et* K'=A'⊗_A K *est un* K-*module* libre "
    "('finie' and 'libre' roman)", "'finie' inside the \\emph (italic)", "italics",
    r"est une $A$-algèbre finie et $K'=A'\otimes_AK$ est un $K$-module} libre.",
    r"est une $A$-algèbre} finie \emph{et $K'=A'\otimes_AK$ est un $K$-module} libre.",
    "The print sets 'finie' upright like 'libre'.")
add(293, "p. 293, (21.10.10)", "on définit c_x'∈Q comme égal au nombre (no comma)", "comma after $c_{x'}\\in\\bb{Q}$",
    "punctuation", r"$c_{x'}\in\bb{Q}$, comme égal", r"$c_{x'}\in\bb{Q}$ comme égal", "")
add(293, "p. 293, (21.10.11)", "Cohen-|Macaulay with a hyphen (as long as the hyphen of 'A-module')",
    "Cohen--Macaulay (en dash)", "punctuation",
    r"$\sh{O}_{X',x'}$ est un anneau de Cohen--Macaulay", r"$\sh{O}_{X',x'}$ est un anneau de Cohen-Macaulay",
    "GLOBAL_ISSUES 74 pattern; the dash at the line end measures as a hyphen.")
add(293, "p. 293, last display", "f*(Z) = Σ c_x'.{x'}‾ with a baseline period", r"c_{x'}\cdot\overline", "symbol",
    r"c_{x'}\cdot\overline{\{x'\}}", r"c_{x'}.\overline{\{x'\}}", "Baseline period (GLOBAL_ISSUES 65).")
add(293, "p. 293, last display", "no full stop: the sentence continues on p. 294 'qui est donc un cycle ...'",
    "final '.'", "extra", "\\overline{\\{x'\\}}.\n\\]", "\\overline{\\{x'\\}}\n\\]", "")

# ---------------------------------------------------------------- p. 294
add(294, "p. 294, first display", "ψ*(Γ_T(𝒵¹_X)) → 𝒵¹_X'⊗_Z Q with italic Γ_T", r"\Gamma_T", "font",
    r"\psi^*(\Gamma_T(\mathscr{Z}^1_X))\to\mathscr{Z}^1_{X'}\otimes",
    r"\psi^*(\varGamma_T(\mathscr{Z}^1_X))\to\mathscr{Z}^1_{X'}\otimes", "As on p. 291.")
add(294, "p. 294, second display", "ψ*(𝒵¹_X) → 𝒵¹_X'⊗_Z Q with no punctuation after it", "final comma", "extra",
    "\\bb{Q},\n\\]\nd'où", "\\bb{Q}\n\\]\nd'où", "")
add(294, "p. 294, second display", "the right-hand 𝒵 (𝒵¹_X') printed in a bolder script Z",
    r"\mathscr{Z}^1_{X'}", "misprint_in_print",
    r"\psi^*(\mathscr{Z}^1_X)\to\mathscr{Z}^1_{X'}\otimes",
    r"\psi^*(\mathscr{Z}^1_X)\to\boldsymbol{\mathscr{Z}}^1_{X'}\otimes",
    "Wrong-fount (bold) script Z, isolated mid-line: same shape, thicker strokes (side-by-side crop "
    "z_side_by_side.png); ink 537 against 386-393 for the other three 𝒵 of this display and (21.10.11.1), while its "
    "superscript 1, subscript X', the ⊗ and the Q next to it have normal ink. Recorded under items 97/100; "
    "independent of the comma fix on the same line.",
    confidence="medium", corrected=r"\psi^*(\mathscr{Z}^1_X)\to\mathscr{Z}^1_{X'}\otimes")
add(294, "p. 294, Remarque (21.10.12)", "autrement dit les nombres μ_x', peuvent être non entiers (comma)",
    "no comma", "misprint_in_print",
    r"les nombres $\mu_{x'}$ peuvent", r"les nombres $\mu_{x'}$, peuvent",
    "Stray comma between subject and verb in the print; the TeX silently drops it.",
    corrected=r"les nombres $\mu_{x'}$ peuvent")
add(294, "p. 294, Remarque (21.10.12)", "l'anneau intègre complet A de (6.15.11, (ii)) (EGA IV's own 6.15.11, no bold 0)",
    r"$(\mathbf{0}_{\mathrm{IV}},6.15.11)$, (ii)", "number",
    r"$(\mathbf{0}_{\mathrm{IV}},6.15.11)$, (ii)", r"\sref{IV.6.15.11}[(ii)]",
    "The TeX adds 0_IV (chapter 0_IV starts at §14) and puts (ii) outside the parentheses; \\sref{...}[(ii)] prints "
    "'(6.15.11, (ii))'.")
add(294, "p. 294, Lemme (21.10.13)", "item labels (i)-(v) upright", "label=(\\roman*) italic in the lemma",
    "convention",
    "$\\mathfrak{m}\\notin\\operatorname{Ass}(A)$).\n\\begin{enumerate}[label=(\\roman*)]",
    "$\\mathfrak{m}\\notin\\operatorname{Ass}(A)$).\n\\begin{enumerate}[label=\\textup{(\\roman*)}]",
    "The opening parenthesis of '(ce qui implique que ...)' is italic in the print, as in the TeX.", convention=6)
add(294, "p. 294, Lemme (21.10.13) (i)", "d_t(M)=long P_t(M)—long N_t(M) (long dash)", "minus sign", "convention",
    r"\operatorname{long}P_t(M)-\operatorname{long}N_t(M)", r"\operatorname{long}P_t(M)\setmin\operatorname{long}N_t(M)",
    "", convention=7)
add(294, "p. 294, Lemme (21.10.13) (iv)", "d_t(M)=n.d_t(A)=n.long(A/tA) with baseline periods", r"n\cdot (twice)",
    "symbol",
    r"$d_t(M)=n\cdot d_t(A)=n\cdot\operatorname{long}(A/tA)$", r"$d_t(M)=n.d_t(A)=n.\operatorname{long}(A/tA)$",
    "Baseline periods (GLOBAL_ISSUES 65).")
add(294, "p. 294, Lemme (21.10.13) (v)", "les hypothèses de (iv): '(iv)' upright", "italic (iv)", "convention",
    r"les hypothèses de (iv) et si de plus", r"les hypothèses de \textup{(iv)} et si de plus", "", convention=6)
add(294, "p. 294, Lemme (21.10.13) (v)", "long(M/tM)=n.long(A/tA) with a baseline period", r"n\cdot", "symbol",
    r"$\operatorname{long}(M/tM)=n\cdot\operatorname{long}(A/tA)$", r"$\operatorname{long}(M/tM)=n.\operatorname{long}(A/tA)$",
    "Baseline period (GLOBAL_ISSUES 65).")


def norm(s):
    return s.replace("\r\n", "\n")


src = norm(SRC.read_text(encoding="utf-8"))
pages = {p: norm((RUN / f"page_{p}.tex").read_text(encoding="utf-8")) for p in range(289, 295)}
bad = 0
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    n_page = pages[d["page"]].count(fx["old"])
    n_src = src.count(fx["old"])
    flag = "" if n_page == 1 else "  <-- PAGE COUNT"
    if n_src != 1:
        flag += f"  (source count {n_src})"
    if flag:
        bad += 1
    print(f"{i:2d} p{d['page']} page={n_page} src={n_src} {d['kind']}{flag}")

# simulate applying all fixes in order to the source text
s = src
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    c = s.count(fx["old"])
    if c != 1:
        print("SEQUENTIAL APPLY PROBLEM", i, c, repr(fx["old"][:60]))
        bad += 1
        continue
    s = s.replace(fx["old"], fx["new"], 1)
for p in range(290, 296):
    print("marker", p, s.count("\\oldpage[IV-4]{%d}" % p))
print("problems:", bad, "findings:", len(F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
