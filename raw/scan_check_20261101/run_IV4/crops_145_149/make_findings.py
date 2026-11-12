"""Build findings_145_149.json (the scan check of EGA IV-4 pp. 145-149, ega4-18-fr.tex).

Strings use the placeholder ¶ for a line break (LF in the release files).
"""
import json
import pathlib

OUT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4\findings_145_149.json")

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace("¶", "\n")
    d["note"] = note
    F.append(d)


BK = r"\boldsymbol{k}"

# ---------------------------------------------------------------- page 145
add(145, "first paragraph: 'l'hypothèse de d) est vérifiée'",
    "label d) wholly italic, parenthesis included (crop p145_d_label.png)",
    "$d)$ (italic letter, upright parenthesis)", "italics", None, "high",
    r"l'hypothèse de $d)$ est vérifiée", r"l'hypothèse de \emph{d)} est vérifiée",
    "Label in roman text (GLOBAL_ISSUES 88). The page begins a new paragraph after Remarque (18.8.3): the marker and its blank lines are right (no boundary fix).")
add(145, "Lemme (18.8.4), line 2: 'essentiellement étale (18.6.1). Alors'",
    "reference upright inside the italic statement (crop p145_1861.png)",
    "(18.6.1) in the italic lemma", "convention", 6, "high",
    r"étale (18.6.1). Alors", r"étale \textup{(18.6.1)}. Alors")
add(145, "Lemme (18.8.4): 'homomorphisme de k(A)-algèbres'",
    "bold italic k", "$k(A)$", "convention", 1, "high",
    r"homomorphisme de $k(A)$-algèbres", r"homomorphisme de $\boldsymbol{k}(A)$-algèbres")
add(145, "Lemme (18.8.4): 'α : k(A′) → k(B)'",
    "bold italic k (twice)", "$\\alpha:k(A')\\to k(B)$", "convention", 1, "high",
    r"$\alpha:k(A')\to k(B)$", r"$\alpha:\boldsymbol{k}(A')\to\boldsymbol{k}(B)$")
add(145, "proof of (18.8.4): 'correspond à un k(s)-morphisme'",
    "bold italic k", "$k(s)$", "convention", 1, "high",
    r"correspond à un $k(s)$-morphisme", r"correspond à un $\boldsymbol{k}(s)$-morphisme")
add(145, "proof of (18.8.4): 'Spec(k(y)) → Spec(k(x))'",
    "bold italic k (twice)", "\\Spec(k(y))\\to\\Spec(k(x))", "convention", 1, "high",
    r"$\Spec(k(y))\to\Spec(k(x))$", r"$\Spec(\boldsymbol{k}(y))\to\Spec(\boldsymbol{k}(x))$")
add(145, "proof of (18.8.4): 'résulte donc de (18.8.1, c))'",
    "label c) wholly italic, followed by the reference's upright parenthesis (crop p145_c_label.png)",
    "$c)$", "italics", None, "high",
    r"(18.8.1, $c)$) puisque", r"(18.8.1, \emph{c)}) puisque",
    "GLOBAL_ISSUES 88.")
add(145, "Lemme (18.8.5), line 2: 'extension de k(A).'",
    "bold italic k", "$k(A)$", "convention", 1, "high",
    r"extension de $k(A)$.", r"extension de $\boldsymbol{k}(A)$.")
add(145, "Lemme (18.8.5), item (i)",
    "label (i) upright", "\\item[(i)] (italic in the statement)", "convention", 6, "high",
    r"\item[(i)] Pour tout", r"\item[\textup{(i)}] Pour tout",
    "GLOBAL_ISSUES 16. Adjacent to (not overlapping) the next finding. The parentheses of '(nécessairement local)' in the same item are italic in the print, as in the TeX.")
add(145, "Lemme (18.8.5) (i): 'Pour tout k(A)-homomorphisme γ : k(A_1) → k(A_2)'",
    "bold italic k (three times)", "$k(A)$-homomorphisme $\\gamma:k(A_1)\\to k(A_2)$", "convention", 1, "high",
    r"$k(A)$-homomorphisme $\gamma:k(A_1)\to k(A_2)$",
    r"$\boldsymbol{k}(A)$-homomorphisme $\gamma:\boldsymbol{k}(A_1)\to\boldsymbol{k}(A_2)$")
add(145, "Lemme (18.8.5), item (ii)",
    "label (ii) upright", "\\item[(ii)] (italic in the statement)", "convention", 6, "high",
    r"\item[(ii)] Pour tout couple", r"\item[\textup{(ii)}] Pour tout couple",
    "GLOBAL_ISSUES 16.")
add(145, "proof of (18.8.5): 'Spec(K) → X_3 (I, 3.2.1)'",
    "'(I, 3.2.1)' with a bold I (crop p145_I321.png)", "(I, 3.2.1)", "convention", 2, "high",
    r"(I, 3.2.1)", r"(\textbf{I}, 3.2.1)",
    "Genuine reference to EGA I (bold I in the print), not one of EGA IV's own (1.x.y).")
add(145, "proof of (18.8.5): 'Spec(k(x_2)) → Spec(k(x_1))'",
    "bold italic k (twice)", "\\Spec(k(x_2))\\to\\Spec(k(x_1))", "convention", 1, "high",
    r"$\Spec(k(x_2))\to\Spec(k(x_1))$", r"$\Spec(\boldsymbol{k}(x_2))\to\Spec(\boldsymbol{k}(x_1))$")
add(145, "proof of (18.8.5), last line: 'l'unicité d'une X′_2-section de X′_3'",
    "X′_2 with a prime (crop p145_X2prime.png)", "$X_2$-section (prime missing)", "formula", None, "high",
    r"d'une $X_2$-section de $X'_3$", r"d'une $X'_2$-section de $X'_3$",
    "X′_2 = Spec(A_2) of (18.6.3), whose proof uses the same 'X′_2-section de X′_3'; the print is right.")
add(145, "(18.8.6), line 2: 'Ω une clôture séparable de k'",
    "'clôture séparable' italic (crop p145_cloture.png)", "roman", "italics", None, "high",
    r"$\Omega$ une clôture séparable de $k$. Considérons", r"$\Omega$ une \emph{clôture séparable} de $k$. Considérons")
add(145, "(18.8.6), line 3: 'l'ensemble des A-homomorphismes locaux A′ → Ω'",
    "'homomorphismes locaux' italic (crop p145_cloture.png)", "roman", "italics", None, "high",
    r"l'ensemble des $A$-homomorphismes locaux $A'\to\Omega$", r"l'ensemble des $A$-\emph{homomorphismes locaux} $A'\to\Omega$")
add(145, "(18.8.6): 'se factorise en λ : A′ → k(A′) →(ω_λ) Ω, où'",
    "set in the running text (crop p145_factorise.png)", "displayed", "other", None, "high",
    "se factorise en¶\\[¶  \\lambda:A'\\longrightarrow k(A')\\xrightarrow{\\omega_\\lambda}\\Omega,¶\\]¶",
    "se factorise en $\\lambda:A'\\longrightarrow k(A')\\xrightarrow{\\omega_\\lambda}\\Omega$,¶",
    "Display vs inline only; no connecting word lost or added. Same spot as the next finding (bold k): apply THIS one first (its 'old' contains the next 'old').")
add(145, "(18.8.6): 'λ : A′ → k(A′) →(ω_λ) Ω'",
    "bold italic k", "k(A')", "convention", 1, "high",
    r"\longrightarrow k(A')\xrightarrow{\omega_\lambda}", r"\longrightarrow\boldsymbol{k}(A')\xrightarrow{\omega_\lambda}",
    "Apply after the previous finding (display made inline): this 'old' occurs exactly once before and after it.")
add(145, "(18.8.6): 'où ω_λ : k(A′) → Ω est un k-homomorphisme'",
    "bold italic k", "$\\omega_\\lambda:k(A')\\to\\Omega$", "convention", 1, "high",
    r"$\omega_\lambda:k(A')\to\Omega$", r"$\omega_\lambda:\boldsymbol{k}(A')\to\Omega$")
add(145, "page break 145/146 ('en vertu | de (18.8.5, (ii))', mid-sentence)",
    "p. 146 begins mid-sentence with 'de (18.8.5, (ii)).'", "blank lines before and after \\oldpage[IV-4]{146}",
    "marker", None, "high",
    "(que l'on note encore $\\lambda\\leq\\mu$), en vertu¶¶", "(que l'on note encore $\\lambda\\leq\\mu$), en vertu¶",
    "The marker is at the right place. Part 1 of 2: the first p. 146 finding removes the blank line after \\oldpage[IV-4]{146}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ---------------------------------------------------------------- page 146
add(146, "top of page", "continues the sentence of p. 145 ('en vertu | de (18.8.5, (ii))')",
    "blank line after \\oldpage[IV-4]{146}", "marker", None, "high",
    "\\oldpage[IV-4]{146}¶¶de (18.8.5, (ii)).", "\\oldpage[IV-4]{146}¶de (18.8.5, (ii)).",
    "Part 2 of 2 with the last p. 145 finding; both blank lines must go.")
add(146, "(18.8.6), line 3: 'Si φ̄_μλ : k(A_λ) → k(A_μ)'",
    "bold italic k (twice)", "k(A_\\lambda)\\to k(A_\\mu)", "convention", 1, "high",
    r"$\overline\varphi_{\mu\lambda}:k(A_\lambda)\to k(A_\mu)$",
    r"$\overline\varphi_{\mu\lambda}:\boldsymbol{k}(A_\lambda)\to\boldsymbol{k}(A_\mu)$")
add(146, "(18.8.6), line 4: '(k(A_λ), φ̄_μλ) est un système inductif'",
    "bold italic k", "(k(A_\\lambda),...)", "convention", 1, "high",
    r"$(k(A_\lambda),\overline\varphi_{\mu\lambda})$", r"$(\boldsymbol{k}(A_\lambda),\overline\varphi_{\mu\lambda})$")
add(146, "(18.8.6), line 5: 'les ω_λ : k(A_λ) → Ω forment'",
    "bold italic k", "$\\omega_\\lambda:k(A_\\lambda)\\to\\Omega$", "convention", 1, "high",
    r"les $\omega_\lambda:k(A_\lambda)\to\Omega$ forment", r"les $\omega_\lambda:\boldsymbol{k}(A_\lambda)\to\Omega$ forment")
add(146, "(18.8.6.1)", "bold italic k", "\\varinjlim k(A_\\lambda)", "convention", 1, "high",
    r"\omega:\varinjlim k(A_\lambda)\longrightarrow\Omega", r"\omega:\varinjlim\boldsymbol{k}(A_\lambda)\longrightarrow\Omega")
add(146, "(18.8.6), second paragraph: '(0_III, 10.3.1.3)'",
    "bold 0 with subscript III", "($0_{\\mathrm{III}}$, 10.3.1.3)", "convention", 2, "high",
    r"il résulte de ($0_{\mathrm{III}}$, 10.3.1.3) que l'anneau", r"il résulte de ($\mathbf{0}_{\mathrm{III}}$, 10.3.1.3) que l'anneau")
add(146, "(18.8.6), display 'lim k(A_λ) ⥲ k(lim A_λ);'",
    "bold italic k (twice)", "k(A_\\lambda) ... k(\\varinjlim A_\\lambda)", "convention", 1, "high",
    r"\varinjlim k(A_\lambda)\xrightarrow{\sim}k(\varinjlim A_\lambda);",
    r"\varinjlim\boldsymbol{k}(A_\lambda)\xrightarrow{\sim}\boldsymbol{k}(\varinjlim A_\lambda);")
add(146, "(18.8.6.2)", "bold italic k", "k(\\varinjlim A_\\lambda)", "convention", 1, "high",
    r"\omega^{-1}:\Omega\xrightarrow{\sim}k(\varinjlim A_\lambda).", r"\omega^{-1}:\Omega\xrightarrow{\sim}\boldsymbol{k}(\varinjlim A_\lambda).")
add(146, "Définition (18.8.7), line 1: 'k = k(A) son corps résiduel'",
    "plain italic k = bold italic k(A)", "$k=k(A)$", "convention", 1, "high",
    r"$k=k(A)$ son corps résiduel", r"$k=\boldsymbol{k}(A)$ son corps résiduel")
add(146, "Définition (18.8.7): 'on appelle hensélisé strict de A relativement à i'",
    "'relati-|vement à' printed roman, like 'hensélisé strict'; 'de' and 'et on note' italic (crops p146_relati.png, p146_ou.png)",
    "'relativement à' italic (no \\emph)", "italics", None, "high",
    r"de $A$ relativement à $i$, et on note", r"de $A$ \emph{relativement à} $i$, et on note",
    "Roman inside the italic definition, as the defined term; \\emph gives upright there.")
add(146, "Définition (18.8.7): '(où ʰˢA lorsque cela ne prête pas à confusion)'",
    "'(où' with a grave accent (crop p146_ou_zoom2.png)", "'(ou' (silent correction)", "misprint_in_print", None, "high",
    r"(ou ${}^{hs}\!A$ lorsque cela", r"(où ${}^{hs}\!A$ lorsque cela",
    "'ou' (or) is meant: 'on note ʰˢA_(i) (ou ʰˢA lorsque ...)'. The fix restores the printed accent only.",
    corrected=r"(ou ${}^{hs}\!A$ lorsque cela")
add(146, "Définition (18.8.7), end: 'défini dans (18.8.6).'",
    "reference upright inside the italic definition (crop p146_defend.png)", "(18.8.6) in the italic definition",
    "convention", 6, "high",
    r"défini dans (18.8.6).", r"défini dans \textup{(18.8.6)}.")
add(146, "after (18.8.7): 'ω⁻¹ : Ω ⥲ k(ʰˢA_(i)), Ω est muni'",
    "bold italic k", "k({}^{hs}\\!A_{(i)})", "convention", 1, "high",
    r"$\omega^{-1}:\Omega\xrightarrow{\sim}k({}^{hs}\!A_{(i)})$, $\Omega$ est muni",
    r"$\omega^{-1}:\Omega\xrightarrow{\sim}\boldsymbol{k}({}^{hs}\!A_{(i)})$, $\Omega$ est muni")
add(146, "display after (18.8.7): 'ʰˢA_(i) → k(ʰˢA_(i)) ⥲(ω) Ω.'",
    "bold italic k", "k({}^{hs}\\!A_{(i)})", "convention", 1, "high",
    r"{}^{hs}\!A_{(i)}\longrightarrow k({}^{hs}\!A_{(i)})", r"{}^{hs}\!A_{(i)}\longrightarrow\boldsymbol{k}({}^{hs}\!A_{(i)})",
    "Adjacent to (not overlapping) the next finding.")
add(146, "same display: the arrow labelled ω",
    "isomorphism arrow (tilde over the arrow) with ω above the tilde (crop p146_display.png)",
    "\\xrightarrow{\\omega} (no tilde)", "symbol", None, "high",
    r"\xrightarrow{\omega}\Omega.", r"\xrightarrow{\overset{\omega}{\sim}}\Omega.",
    "Same encoding as the earlier page fixes of labelled isomorphism arrows (\\xrightarrow{\\overset{v}{\\sim}}, 0_IV p. 93).")
add(146, "paragraph before (18.8.8), end: 'à isomorphisme unique près'",
    "'isomorphisme unique près' italic", "roman", "italics", None, "high",
    r"défini comme tel à isomorphisme unique près.", r"défini comme tel à \emph{isomorphisme unique près}.")
add(146, "paragraph before (18.8.8): '(0_III, 8.1.8)'",
    "bold 0 with subscript III", "($0_{\\mathrm{III}}$, 8.1.8)", "convention", 2, "high",
    r"($0_{\mathrm{III}}$, 8.1.8)", r"($\mathbf{0}_{\mathrm{III}}$, 8.1.8)")
add(146, "Proposition (18.8.8), item (i)",
    "label (i) upright", "\\item[(i)] (italic in the statement)", "convention", 6, "high",
    r"\item[(i)] ${}^{hs}\!A_{(i)}$ est un anneau", r"\item[\textup{(i)}] ${}^{hs}\!A_{(i)}$ est un anneau",
    "GLOBAL_ISSUES 16.")
add(146, "Proposition (18.8.8) (i): 'strictement local (18.8.2) et'",
    "reference upright inside the italic statement (crop p146_1882.png)", "(18.8.2) in the italic statement",
    "convention", 6, "high",
    r"strictement local (18.8.2) et", r"strictement local \textup{(18.8.2)} et")
add(146, "Proposition (18.8.8), item (ii)",
    "label (ii) upright", "\\item[(ii)] (italic in the statement)", "convention", 6, "high",
    r"\item[(ii)] Pour tout homomorphisme local", r"\item[\textup{(ii)}] Pour tout homomorphisme local",
    "GLOBAL_ISSUES 16.")
add(146, "Proposition (18.8.8) (ii): 'tout k-homomorphisme ψ : Ω → k(B)'",
    "bold italic k", "k(B)", "convention", 1, "high",
    r"tout $k$-homomorphisme $\psi:\Omega\to k(B)$", r"tout $k$-homomorphisme $\psi:\Omega\to\boldsymbol{k}(B)$")
add(146, "Proposition (18.8.8) (ii): 'Ω →(ω⁻¹) k(ʰˢA_(i)) →(v̄) k(B)'",
    "bold italic k (twice)", "k({}^{hs}\\!A_{(i)}) ... k(B)", "convention", 1, "high",
    r"$\Omega\xrightarrow{\omega^{-1}}k({}^{hs}\!A_{(i)})\xrightarrow{\overline v}k(B)$",
    r"$\Omega\xrightarrow{\omega^{-1}}\boldsymbol{k}({}^{hs}\!A_{(i)})\xrightarrow{\overline v}\boldsymbol{k}(B)$")

# ---------------------------------------------------------------- page 147
add(147, "Proposition (18.8.8), item (iii)",
    "label (iii) upright", "\\item[(iii)] (italic in the statement)", "convention", 6, "high",
    r"\item[(iii)] ${}^{hs}\!A_{(i)}$", r"\item[\textup{(iii)}] ${}^{hs}\!A_{(i)}$",
    "GLOBAL_ISSUES 16.")
add(147, "Proposition (18.8.8) (iii): 'et k(ʰˢA_(i)) est une clôture séparable de k'",
    "bold italic k", "k({}^{hs}\\!A_{(i)})", "convention", 1, "high",
    r"et $k({}^{hs}\!A_{(i)})$ est une clôture séparable", r"et $\boldsymbol{k}({}^{hs}\!A_{(i)})$ est une clôture séparable")
add(147, "Proposition (18.8.8), item (iv)",
    "label (iv) upright", "\\item[(iv)] (italic in the statement)", "convention", 6, "high",
    r"\item[(iv)] Pour que", r"\item[\textup{(iv)}] Pour que",
    "GLOBAL_ISSUES 16.")
add(147, "Proposition (18.8.8), item (v)",
    "label (v) upright; the parentheses of '(donc Ω = k)' are italic, as in the TeX", "\\item[(v)] (italic in the statement)",
    "convention", 6, "high",
    r"\item[(v)] Si $A$", r"\item[\textup{(v)}] Si $A$",
    "GLOBAL_ISSUES 16.")
add(147, "Proposition (18.8.8) (v): 'on a ʰˢA ≅ A'",
    "congruence sign ≅ (tilde over two bars), not an arrow (crop p147_cong.png)", "\\xrightarrow{\\sim}", "symbol", None, "high",
    r"on a ${}^{hs}\!A\xrightarrow{\sim}A$", r"on a ${}^{hs}\!A\cong A$")
add(147, "Proposition (18.8.8), item (vi)",
    "label (vi) upright", "\\item[(vi)] (italic in the statement)", "convention", 6, "high",
    r"\item[(vi)] Si $i'", r"\item[\textup{(vi)}] Si $i'",
    "GLOBAL_ISSUES 16.")
add(147, "Proposition (18.8.8) (vi): 'le A-homomorphisme correspondant (par (ii)) v_σ'",
    "outer parentheses and '(ii)' upright, 'par' italic (crops p147_par2.png, p147_parens2.png; compare the italic '(donc' of (v))",
    "'(par (ii))' all italic in the statement", "convention", 6, "high",
    r"correspondant (par (ii)) $v_\sigma", r"correspondant \textup{(}par \textup{(ii))} $v_\sigma")
add(147, "proof of (18.8.8): 'découlent encore de (0_III, 10.3.1.3)'",
    "bold 0 with subscript III", "($0_{\\mathrm{III}}$, 10.3.1.3)", "convention", 2, "high",
    r"découlent encore de ($0_{\mathrm{III}}$, 10.3.1.3)", r"découlent encore de ($\mathbf{0}_{\mathrm{III}}$, 10.3.1.3)")
add(147, "proof of (18.8.8): 'fidèlement plat (0_I, 6.5.2)'",
    "bold 0 with subscript I", "($0_{\\mathrm I}$, 6.5.2)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.5.2)", r"($\mathbf{0}_{\mathrm I}$, 6.5.2)")
add(147, "proof of (18.8.8) (ii): 'le composé k(A_λ) →(ω_λ) Ω →(ψ) k(B)'",
    "bold italic k (twice)", "k(A_\\lambda) ... k(B)", "convention", 1, "high",
    r"$k(A_\lambda)\xrightarrow{\omega_\lambda}\Omega\xrightarrow{\psi}k(B)$",
    r"$\boldsymbol{k}(A_\lambda)\xrightarrow{\omega_\lambda}\Omega\xrightarrow{\psi}\boldsymbol{k}(B)$")
add(147, "proof of (18.8.8), last words: 'ce qui prouve (v).'",
    "the v is a BOLD v (wrong fount): both strokes heavy, ink area 193 px against 129 px for the v of 'prouve' on the same line "
    "and 127 px for the v of 'la condition (iv)' above, while the parentheses and the full stop next to it are normal weight "
    "(crops p147_provev.png, p147_v_cmp.png, p147_roman_v.png)",
    "normal-weight v (silent correction)", "misprint_in_print", None, "medium",
    r"ce qui prouve (v).", r"ce qui prouve (\textbf{v}).",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99). Not the line-end heaviness of item 100: the sorts next to it are not heavier and the right stroke has the bold cut.",
    corrected=r"ce qui prouve (v).")
add(147, "(18.8.8.1), line 1: 'Soit C la catégorie'",
    "bold italic C (crop p147_C.png)", "\\mathcal C", "font", None, "high",
    r"Soit $\mathcal C$ la catégorie", r"Soit $\boldsymbol{C}$ la catégorie")
add(147, "(18.8.8.1), line 2: 'pour tout B ∈ C'",
    "bold italic C", "\\mathcal C", "font", None, "high",
    r"$B\in\mathcal C$", r"$B\in\boldsymbol{C}$")
add(147, "(18.8.8.1): 'd'un k-isomorphisme ψ : Ω → k(B)'",
    "bold italic k", "k(B)", "convention", 1, "high",
    r"d'un $k$-isomorphisme $\psi:\Omega\to k(B)$", r"d'un $k$-isomorphisme $\psi:\Omega\to\boldsymbol{k}(B)$")
add(147, "(18.8.8.1): 'le composé k(A) = k →(i) Ω →(ψ) k(B)'",
    "bold italic k in k(A) and k(B); the k after '=' plain italic", "k(A) ... k(B)", "convention", 1, "high",
    r"$k(A)=k\xrightarrow{i}\Omega\xrightarrow{\psi}k(B)$",
    r"$\boldsymbol{k}(A)=k\xrightarrow{i}\Omega\xrightarrow{\psi}\boldsymbol{k}(B)$")
add(147, "(18.8.8.1): 'le foncteur covariant F : C → Ens'",
    "C and Ens bold italic (crop p147_Ens.png)", "\\mathcal C, \\mathbf{Ens} (bold upright)", "font", None, "high",
    r"$F:\mathcal C\to\mathbf{Ens}$", r"$F:\boldsymbol{C}\to\boldsymbol{\mathit{Ens}}$",
    "Two letters in one edit; same encoding as the earlier page fixes (\\boldsymbol{C}, \\boldsymbol{\\mathit{Ens}}).")
add(147, "(18.8.8.1): '(0_III, 8.1.11)'",
    "bold 0 with subscript III", "($0_{\\mathrm{III}}$, 8.1.11)", "convention", 2, "high",
    r"($0_{\mathrm{III}}$, 8.1.11)", r"($\mathbf{0}_{\mathrm{III}}$, 8.1.11)")
add(147, "(18.8.9), line 2: 'i_j : k(A_m_j) → Ω_j'",
    "bold italic k", "k(A_{\\mathfrak m_j})", "convention", 1, "high",
    r"$i_j:k(A_{\mathfrak m_j})\to\Omega_j$", r"$i_j:\boldsymbol{k}(A_{\mathfrak m_j})\to\Omega_j$")
add(147, "(18.8.9), line 3: 'de k(A_m_j) dans une clôture séparable'",
    "bold italic k", "k(A_{\\mathfrak m_j})", "convention", 1, "high",
    r"de $k(A_{\mathfrak m_j})$ dans une clôture", r"de $\boldsymbol{k}(A_{\mathfrak m_j})$ dans une clôture")
add(147, "page break 147/148 ('homomorphismes i_j. | C'est donc', mid-paragraph)",
    "p. 148 begins flush left with 'C'est donc' (no paragraph indent; compare 'On peut évidemment' below): the paragraph of (18.8.9) continues",
    "blank lines before and after \\oldpage[IV-4]{148}", "marker", None, "high",
    "relativement aux homomorphismes $i_j$.¶¶", "relativement aux homomorphismes $i_j$.¶",
    "The marker is at the right place. Part 1 of 2: the first p. 148 finding removes the blank line after \\oldpage[IV-4]{148}; apply both.")

# ---------------------------------------------------------------- page 148
add(148, "top of page", "continues the paragraph of p. 147 without an indent",
    "blank line after \\oldpage[IV-4]{148}", "marker", None, "high",
    "\\oldpage[IV-4]{148}¶¶C'est donc", "\\oldpage[IV-4]{148}¶C'est donc",
    "Part 2 of 2 with the last p. 147 finding; both blank lines must go.")
add(148, "Proposition (18.8.10), line 2: 'Soient n_j (1 ≤ j ≤ r) les idéaux maximaux'",
    "parentheses upright inside the italic statement (crop p148_prop.png)", "($1\\leq j\\leq r$) italic parentheses",
    "convention", 6, "high",
    r"Soient $\mathfrak n_j$ ($1\leq j\leq r$) les idéaux", r"Soient $\mathfrak n_j$ \textup{($1\leq j\leq r$)} les idéaux")
add(148, "Proposition (18.8.10), last line: '(B⊗_A(ʰˢA))_q_j (1 ≤ j ≤ r).'",
    "parentheses upright inside the italic statement (crop p148_prop2.png)", "($1\\leq j\\leq r$) italic parentheses",
    "convention", 6, "high",
    r"_{\mathfrak q_j}$ ($1\leq j\leq r$).", r"_{\mathfrak q_j}$ \textup{($1\leq j\leq r$)}.")
add(148, "diagram in the proof of (18.8.10): the two arrows between C′_i and ʰˢC",
    "upper-left arrow ʰˢC → C′_i labelled w′ above it; lower-right arrow C′_i → ʰˢC labelled w below it (crop p148_diagram.png)",
    "@<0.8ex> shifts put C′_i → ʰˢC (w) upper-left and ʰˢC → C′_i (w′) lower-right, with both labels between the arrows (test compile diag_test.png)",
    "other", None, "high",
    "{}^{hs}\\!C \\ar@<0.8ex>[dl]_{w'} \\\\¶  && C'_i \\ar@<0.8ex>[ur]_{w} \\\\",
    "{}^{hs}\\!C \\ar@<-0.8ex>[dl]_{w'} \\\\¶  && C'_i \\ar@<-0.8ex>[ur]_{w} \\\\",
    "Both shifts change sign together; checked by compiling both versions (crops_145_149/diag_test.tex).")
add(148, "same diagram: label g of the vertical arrow ʰˢA → C′",
    "g to the right of the arrow", "\\ar[u]^{g} sets g to the left", "other", None, "high",
    r"\ar[u]^{g}", r"\ar[u]_{g}",
    "Label side as in the print (GLOBAL_ISSUES 30 pattern).")
add(148, "page break 148/149 ('donc est | l'identité', mid-sentence)",
    "p. 149 begins mid-sentence with 'l'identité (18.8.8).'", "blank lines before and after \\oldpage[IV-4]{149}",
    "marker", None, "high",
    "l'automorphisme identique de $K\\Omega$, donc est¶¶", "l'automorphisme identique de $K\\Omega$, donc est¶",
    "The marker is at the right place. Part 1 of 2: the first p. 149 finding removes the blank line after \\oldpage[IV-4]{149}; apply both.")

# ---------------------------------------------------------------- page 149
add(149, "top of page", "continues the sentence of p. 148 ('donc est | l'identité')",
    "blank line after \\oldpage[IV-4]{149}", "marker", None, "high",
    "\\oldpage[IV-4]{149}¶¶l'identité (18.8.8).", "\\oldpage[IV-4]{149}¶l'identité (18.8.8).",
    "Part 2 of 2 with the last p. 148 finding; both blank lines must go.")
add(149, "Remarque (18.8.11), line 2: 'le fait que B est entière sur A'",
    "'entière' italic (crop p149_rem.png)", "no \\emph", "italics", None, "high",
    r"le fait que $B$ est entière sur $A$", r"le fait que $B$ est \emph{entière} sur $A$",
    "Judged as roman remark text (remark font is document-wide).")
add(149, "Remarque (18.8.11), last line: '[k(n_j) : k]_s'",
    "bold italic k in k(n_j); the k after the colon plain italic", "k(\\mathfrak n_j)", "convention", 1, "high",
    r"$[k(\mathfrak n_j)", r"$[\boldsymbol{k}(\mathfrak n_j)",
    "Adjacent to (not overlapping) the next finding.")
add(149, "Remarque (18.8.11), last word: 'finis'",
    "'finis' italic (crop p149_degs2.png)", "no \\emph", "italics", None, "high",
    r":k]_s$ finis.", r":k]_s$ \emph{finis}.",
    "Judged as roman remark text (remark font is document-wide).")
add(149, "Proposition (18.8.12), item (i)",
    "label (i) upright", "\\item[(i)] (italic in the statement)", "convention", 6, "high",
    r"\item[(i)] Pour que ${}^{hs}", r"\item[\textup{(i)}] Pour que ${}^{hs}",
    "GLOBAL_ISSUES 16.")
add(149, "Proposition (18.8.12) (i): '(resp. normal)'",
    "'(resp.' and ')' upright, 'normal' italic (crop p149_i.png)", "all italic", "convention", 6, "high",
    r"(resp. normal), il faut", r"\textup{(resp.} normal\textup{)}, il faut",
    "Same form as Théorème (18.6.9) (i), p. 139.")
add(149, "Proposition (18.8.12), item (ii)",
    "label (ii) upright", "\\item[(ii)] (italic in the statement)", "convention", 6, "high",
    r"\item[(ii)] Supposons $A$ noethérien", r"\item[\textup{(ii)}] Supposons $A$ noethérien",
    "GLOBAL_ISSUES 16.")
add(149, "Proposition (18.8.12) (ii): 'séparables de k(p)'",
    "bold italic k", "$k(\\mathfrak p)$", "convention", 1, "high",
    r"séparables de $k(\mathfrak p)$", r"séparables de $\boldsymbol{k}(\mathfrak p)$",
    "Adjacent to (not overlapping) the next finding.")
add(149, "Proposition (18.8.12) (ii): '(ce qui entraîne ... sont géométriquement régulières et sont des espaces discrets)'",
    "the parenthesis set roman, only 'géométriquement régulières' and 'discrets' italic (crop p149_ii.png)",
    "all italic, with the two \\emph phrases upright", "convention", 6, "high",
    r"(ce qui entraîne que les fibres du morphisme canonique $\Spec({}^{hs}\!A)\to\Spec(A)$ sont \emph{géométriquement régulières} et sont des espaces \emph{discrets})",
    r"\textup{(ce qui entraîne que les fibres du morphisme canonique $\Spec({}^{hs}\!A)\to\Spec(A)$ sont \emph{géométriquement régulières} et sont des espaces \emph{discrets})}",
    "Inside \\textup the \\emph gives italic, as printed (same form as Théorème (18.6.9) (ii), p. 139).")
add(149, "Corollaire (18.8.13), item a)",
    "label a) upright (crop p149_cor13.png)", "\\item[$a)$] (italic letter)", "convention", 6, "high",
    r"\item[$a)$] être un anneau", r"\item[\textup{a)}] être un anneau",
    "GLOBAL_ISSUES 88 (upright inside italic statements); same form as Corollaire (18.6.10), p. 140.")
add(149, "Corollaire (18.8.13) a): '(0, 16.5.3)'",
    "bold 0, no subscript; parentheses and numbers upright", "(0, 16.5.3) plain 0, italic in the statement",
    "convention", 2, "high",
    r"Cohen-Macaulay (0, 16.5.3);", r"Cohen-Macaulay \textup{(\textbf{0}, 16.5.3)};",
    "One edit for convention 2 (bold 0) and convention 6 (upright reference in the italic statement); same form as Corollaire (18.6.10), p. 140.")
add(149, "Corollaire (18.8.13), item b)",
    "label b) upright", "\\item[$b)$] (italic letter)", "convention", 6, "high",
    r"\item[$b)$] vérifier", r"\item[\textup{b)}] vérifier",
    "GLOBAL_ISSUES 88.")
add(149, "Corollaire (18.8.13) b): '(S_n) (5.7.3);'",
    "reference upright", "(5.7.3) italic in the statement", "convention", 6, "high",
    r"$(S_n)$ (5.7.3);", r"$(S_n)$ \textup{(5.7.3)};")
add(149, "Corollaire (18.8.13), item c)",
    "label c) upright", "\\item[$c)$] (italic letter)", "convention", 6, "high",
    r"\item[$c)$] être régulier", r"\item[\textup{c)}] être régulier",
    "GLOBAL_ISSUES 88. The heavier ';' after 'régulier' ends its line (item 100): not reported.")
add(149, "Corollaire (18.8.13), item d)",
    "label d) upright", "\\item[$d)$] (italic letter)", "convention", 6, "high",
    r"\item[$d)$] vérifier", r"\item[\textup{d)}] vérifier",
    "GLOBAL_ISSUES 88.")
add(149, "Corollaire (18.8.13) d): '(R_n) (5.8.2);'",
    "reference upright", "(5.8.2) italic in the statement", "convention", 6, "high",
    r"$(R_n)$ (5.8.2);", r"$(R_n)$ \textup{(5.8.2)};")
add(149, "Proposition (18.8.15), item a)",
    "label a) upright (crop p149_prop15.png)", "\\item[$a)$] (italic letter)", "convention", 6, "high",
    r"\item[$a)$] $A$ est géométriquement", r"\item[\textup{a)}] $A$ est géométriquement",
    "GLOBAL_ISSUES 88.")
add(149, "Proposition (18.8.15) a): '(resp. réduit et géométriquement unibranche)'",
    "'(resp.' and ')' upright, the words italic", "all italic", "convention", 6, "high",
    r"unibranche (resp. réduit et géométriquement unibranche).",
    r"unibranche \textup{(resp.} réduit et géométriquement unibranche\textup{)}.")
add(149, "Proposition (18.8.15), item b)",
    "label b) upright", "\\item[$b)$] (italic letter)", "convention", 6, "high",
    r"\item[$b)$] Pour toute", r"\item[\textup{b)}] Pour toute",
    "GLOBAL_ISSUES 88.")
add(149, "Proposition (18.8.15) b): 'Spec(A′) est irréductible (resp. intègre).'",
    "'(resp.' and ')' upright, 'intègre' italic", "all italic", "convention", 6, "high",
    r"$\Spec(A')$ est irréductible (resp. intègre).", r"$\Spec(A')$ est irréductible \textup{(resp.} intègre\textup{)}.")
add(149, "Proposition (18.8.15), item c)",
    "label c) upright", "\\item[$c)$] (italic letter)", "convention", 6, "high",
    r"\item[$c)$] $\Spec({}^{hs}", r"\item[\textup{c)}] $\Spec({}^{hs}",
    "GLOBAL_ISSUES 88.")
add(149, "Proposition (18.8.15) c): 'Spec(ʰˢA) est irréductible (resp. intègre).'",
    "'(resp.' and ')' upright, 'intègre' italic", "all italic", "convention", 6, "high",
    "(resp. intègre).¶\\end{enumerate}", "\\textup{(resp.} intègre\\textup{)}.¶\\end{enumerate}")
add(149, "proof of (18.8.15): 'l'équivalence de b) et c) se prouve'",
    "labels b), c) wholly italic", "$b)$, $c)$", "italics", None, "high",
    r"l'équivalence de $b)$ et $c)$ se prouve", r"l'équivalence de \emph{b)} et \emph{c)} se prouve",
    "GLOBAL_ISSUES 88; two labels, one edit.")
add(149, "proof of (18.8.15): 'du fait que a) entraîne c)'",
    "labels a), c) wholly italic", "$a)$, $c)$", "italics", None, "high",
    r"du fait que $a)$ entraîne $c)$, en tenant", r"du fait que \emph{a)} entraîne \emph{c)}, en tenant",
    "GLOBAL_ISSUES 88; two labels, one edit.")
add(149, "proof of (18.8.15): 'pour démontrer que c) entraîne a)'",
    "labels c), a) wholly italic", "$c)$, $a)$", "italics", None, "high",
    r"démontrer que $c)$ entraîne $a)$, gardons", r"démontrer que \emph{c)} entraîne \emph{a)}, gardons",
    "GLOBAL_ISSUES 88; two labels, one edit.")
add(149, "Corollaire (18.8.16), line 1: '(resp. strictement local)'",
    "'(resp.' and ')' upright, 'strictement local' italic (crop p149_cor16.png)", "all italic", "convention", 6, "high",
    r"hensélien (resp. strictement local). Pour", r"hensélien \textup{(resp.} strictement local\textup{)}. Pour")
add(149, "Corollaire (18.8.16), line 2: '(resp. géométriquement unibranche)'",
    "'(resp.' and ')' upright, the words italic", "all italic", "convention", 6, "high",
    r"unibranche (resp. géométriquement unibranche), il faut", r"unibranche \textup{(resp.} géométriquement unibranche\textup{)}, il faut")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
print(len(F), "findings written")
