import json
import pathlib

OUT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0IV1\findings_096_100.json")
F = []


def add(page, where, scan, tex, kind, fix, note="", conv=None, conf="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


BOLDGR = "The print sets this gr in bold upright; \\gr is \\operatorname{gr} (roman). Arrow labels gr(...) are roman in the print and stay \\gr."
BULLET = "Raised bullet in the print (GLOBAL_ISSUES item 60); the TeX has an asterisk."
NFRAK = "Fraktur N in the print (compared with the nilradical N and the radical R of 0_I p. 12 and with the K and N of 0_IV p. 149): not R, not K."

# ---------------- page 96 ----------------
add(96, "top of p. 96: '... E_{α,n}/(J_α/J_α^{n+1}); | comme C est une A-algèbre formellement lisse'",
    "p. 96 begins flush left inside the sentence begun on p. 95",
    "blank lines before and after \\oldpage{96}: paragraph break",
    "other", fx(r"\oldpage[0\textsubscript{IV-1}]{96}" + "\n\n" + r"  comme $C$ est",
                r"\oldpage[0\textsubscript{IV-1}]{96}" + "\n" + r"  comme $C$ est"),
    "Spurious paragraph break at a page break inside a sentence (GLOBAL_ISSUES item 20). Apply together with the removal of the blank line BEFORE the marker, which lies in the p. 95 segment (ega0-19-fr.tex: '...\\mathfrak J_\\alpha^{n+1})$~;\\n\\n\\oldpage[0\\textsubscript{IV-1}]{96}' -> one newline).")
add(96, "(19.5.6.4)(i), after the first diagram: 'Comme f_α et g_α sont continus, il y a un β≥α ...'",
    "new indented paragraph after the diagram",
    "no blank line after \\]: same paragraph",
    "other", fx("  \\]\n  Comme $f_\\alpha$ et $g_\\alpha$ sont continus",
                "  \\]\n\n  Comme $f_\\alpha$ et $g_\\alpha$ sont continus"))
add(96, "(19.5.6.4)(i), display 'C → C_β --f'_{αβ}--> E_{α,n}'",
    "no punctuation after E_{α,n} (crop)",
    "E_{\\alpha,n}, (trailing comma)",
    "punctuation", fx(r"\xrightarrow{f'_{\alpha\beta}}E_{\alpha,n},", r"\xrightarrow{f'_{\alpha\beta}}E_{\alpha,n}"))
add(96, "(19.5.6.4)(i), display 'S•_{C_β}(J_β/J_β²) → E_{α,n}'",
    "S with a raised bullet", "\\mathbf S_{C_\\beta}^*",
    "symbol", fx("\\mathbf S_{C_\\beta}^*(\\mathfrak J_\\beta/\\mathfrak J_\\beta^2)\n    \\longrightarrow E_{\\alpha,n}",
                 "\\mathbf S_{C_\\beta}^\\bullet(\\mathfrak J_\\beta/\\mathfrak J_\\beta^2)\n    \\longrightarrow E_{\\alpha,n}"), BULLET)
add(96, "(19.5.6.4)(i): 's'annule dans la puissance (n+1)^e de l'idéal d'augmentation'",
    "(n+1) followed by a superior e", "$(n+1)$-ième",
    "word", fx(r"puissance $(n+1)$-ième de l'idéal", r"puissance $(n+1)$\textsuperscript{e} de l'idéal"),
    "Same as the p. 32 fix (3\\textsuperscript{e}). p. 95 has the same printed (n+1)^e, written -ième (ega0-19-fr.tex, 19.5.6.2).")
add(96, "(19.5.6.4)(i): 'de l'idéal d'augmentation de S•_{C_β}(J_β/J_β²);'",
    "S with a raised bullet", "\\mathbf S_{C_\\beta}^*",
    "symbol", fx(r"\mathbf S_{C_\beta}^*(\mathfrak J_\beta/\mathfrak J_\beta^2)$~; passant",
                 r"\mathbf S_{C_\beta}^\bullet(\mathfrak J_\beta/\mathfrak J_\beta^2)$~; passant"), BULLET)
add(96, "(19.5.6.4)(i): 'passant au quotient par cette puissance (n+1)^e'",
    "(n+1) followed by a superior e", "$(n+1)$-ième",
    "word", fx(r"puissance $(n+1)$-ième, on obtient", r"puissance $(n+1)$\textsuperscript{e}, on obtient"))
add(96, "(19.5.6.4)(i): 'des deux homomorphismes gr⁰(v_{αβ}) et gr¹(v_{αβ})'",
    "bold gr (crop)", "\\gr (roman)",
    "font", fx("$\\gr^0(v_{\\alpha\\beta})$ et\n  $\\gr^1(v_{\\alpha\\beta})$, puisque",
               "$\\mathbf{gr}^0(v_{\\alpha\\beta})$ et\n  $\\mathbf{gr}^1(v_{\\alpha\\beta})$, puisque"), BOLDGR)
add(96, "(19.5.6.4)(i): 'que gr(v_{αβ}) est surjectif'",
    "bold gr", "\\gr", "font",
    fx(r"$\gr(v_{\alpha\beta})$ est surjectif", r"$\mathbf{gr}(v_{\alpha\beta})$ est surjectif"), BOLDGR)
add(96, "(19.5.6.4)(i): '(l'algèbre gr•(E_{α,n}) étant engendrée par gr⁰(E_{α,n}) et gr¹(E_{α,n}))'",
    "gr with a raised bullet; all three gr bold", "\\gr^*, \\gr^0, \\gr^1 (roman; asterisk)",
    "symbol", fx("$\\gr^*(E_{\\alpha,n})$ étant engendrée par $\\gr^0(E_{\\alpha,n})$ et\n  $\\gr^1(E_{\\alpha,n})$)",
                 "$\\mathbf{gr}^\\bullet(E_{\\alpha,n})$ étant engendrée par $\\mathbf{gr}^0(E_{\\alpha,n})$ et\n  $\\mathbf{gr}^1(E_{\\alpha,n})$)"),
    BULLET + " The same edit sets the three gr bold (font).")
add(96, "(19.5.6.4)(ii): 'égal à (b_α + J^{n+1})/(b_γ + J^{n+1}), est nilpotent'",
    "italic b_α and b_γ (wrong fount; enlarged crop), while the ideals b_α are Fraktur everywhere else, e.g. two lines above",
    "\\mathfrak b_\\alpha, \\mathfrak b_\\gamma: silent correction",
    "misprint_in_print", fx("(\\mathfrak b_\\alpha+\\mathfrak J^{n+1})/\n  (\\mathfrak b_\\gamma+\\mathfrak J^{n+1})",
                            "(b_\\alpha+\\mathfrak J^{n+1})/\n  (b_\\gamma+\\mathfrak J^{n+1})"),
    "Wrong-fount letters, recorded like EGA II's (GLOBAL_ISSUES item 29). p. 95 (19.5.6.2) prints the same italic b in '(b_α+J^{n+1})/J^{n+1}'.",
    corrected="(\\mathfrak b_\\alpha+\\mathfrak J^{n+1})/(\\mathfrak b_\\gamma+\\mathfrak J^{n+1})")
add(96, "(19.5.6.4)(ii), triangle diagram C → E_{α,n}, E_{γ,n}: label of the upper arrow",
    "the upper arrow is labelled 'α' only (no f; enlarged crop); the lower one 'f_γ'",
    "\\ar[ur]^{f_\\alpha}: silent correction",
    "misprint_in_print", fx(r"\ar[ur]^{f_\alpha}", r"\ar[ur]^{\alpha}"),
    "The text defines the arrow as f_α.", corrected=r"\ar[ur]^{f_\alpha}")
add(96, "printed at the top of p. 97 (TeX before the misplaced p. 97 marker): 'en construisant v_{δγ} comme dans (i)'",
    "(i) upright", "\\emph{(i)} (italic)",
    "italics", fx(r"comme dans \emph{(i)}, d'obtenir", r"comme dans (i), d'obtenir"),
    "Printed on p. 97; the edit lies in page_096.tex because of the misplaced p. 97 marker. Apply before the marker insertion below.")
add(96, "printed at the top of p. 97 (TeX before the misplaced p. 97 marker): 'en construisant v_{δγ} comme dans (i)'",
    "v_{δγ} (δ before γ; enlarged crop)", "v_{\\gamma\\delta}: silent correction",
    "misprint_in_print", fx(r"$v_{\gamma\delta}$", r"$v_{\delta\gamma}$"),
    "(19.5.6.3, (ii)) gives v_{γδ}: F_{δ,n} → E_{γ,n} with δ≥γ. Printed on p. 97; the edit lies in page_096.tex. Apply before the marker insertion below.",
    corrected=r"$v_{\gamma\delta}$")
add(96, "page break p. 96/97 inside (19.5.6.4)(ii): '... dans ce module produit du | module P=J_γ/J_γ^{n+1}, et d'appliquer ...'",
    "p. 96 ends with 'du'; p. 97 begins 'module P=J_γ/J_γ^{n+1}, et d'appliquer la définition (19.2.1)'",
    "\\oldpage[0\\textsubscript{IV-1}]{97} stands after the end of (19.5.6.4)(ii), before Lemme (19.5.6.5): the first three printed lines of p. 97 lie in the p. 96 segment",
    "marker", fx("canonique $Q$ dans ce module produit du module\n",
                 "canonique $Q$ dans ce module produit du\n  \\oldpage[0\\textsubscript{IV-1}]{97}\n  module\n"),
    "Move, part 1 of 2: insert the marker here; the first p. 97 finding removes the old marker. Apply after every other p. 96 finding (two of them lie after this point). \\oldpage ends with \\ignorespaces, so one space remains between 'du' and 'module'.")

# ---------------- page 97 ----------------
add(97, "old place of the p. 97 marker, before Lemme (19.5.6.5)",
    "Lemme (19.5.6.5) is printed after the three lines that open p. 97",
    "\\oldpage[0\\textsubscript{IV-1}]{97} before \\begin{lemma}[19.5.6.5]",
    "marker", fx("\\oldpage[0\\textsubscript{IV-1}]{97}\n\n\\begin{lemma}[19.5.6.5]", "\\begin{lemma}[19.5.6.5]"),
    "Move, part 2 of 2: remove the old marker; apply with the p. 96 marker finding (insertion first).")
add(97, "Lemme (19.5.6.5): 'de sorte qu'en vertu de (19.5.6.1),'",
    "reference upright in the italic statement", "(19.5.6.1) italic",
    "convention", fx(r"en vertu de (19.5.6.1),", r"en vertu de \textup{(19.5.6.1)},"), conv=6)
add(97, "Lemme (19.5.6.5): 'les conditions de (19.5.6.3) sont satisfaites)'",
    "reference upright", "(19.5.6.3) italic",
    "convention", fx("de\n(19.5.6.3) sont satisfaites", "de\n\\textup{(19.5.6.3)} sont satisfaites"), conv=6)
add(97, "Lemme (19.5.6.5): 'vérifiant les conditions de (19.5.6.3, (i)), il existe'",
    "reference upright", "(19.5.6.3, (i)) italic",
    "convention", fx(r"conditions de (19.5.6.3, (i)), il existe", r"conditions de \textup{(19.5.6.3, (i))}, il existe"), conv=6)
add(97, "Lemme (19.5.6.5): '1° gr⁰(w_{βλ}) : C_λ → C_β et gr¹(w_{βλ}) : ...'",
    "bold upright gr", "\\gr", "font",
    fx("$\\gr^0(w_{\\beta\\lambda}):C_\\lambda\\to C_\\beta$ et\n$\\gr^1(w_{\\beta\\lambda}):",
       "$\\mathbf{gr}^0(w_{\\beta\\lambda}):C_\\lambda\\to C_\\beta$ et\n$\\mathbf{gr}^1(w_{\\beta\\lambda}):"), BOLDGR)
add(97, "proof of (19.5.6.5): 'son noyau N est nilpotent'",
    "Fraktur N", "\\mathfrak R", "symbol",
    fx(r"son noyau $\mathfrak R$ est", r"son noyau $\mathfrak N$ est"), NFRAK)
add(97, "proof of (19.5.6.5): 'le noyau de gr⁰(v_{βδ}) : C_δ → C_β'",
    "bold gr", "\\gr", "font",
    fx(r"$\gr^0(v_{\beta\delta}):C_\delta\to C_\beta$ est aussi", r"$\mathbf{gr}^0(v_{\beta\delta}):C_\delta\to C_\beta$ est aussi"), BOLDGR)
add(97, "proof of (19.5.6.5): 'E_{β,n} s'identifie à F_{δ,n}/N'",
    "Fraktur N", "\\mathfrak R", "symbol",
    fx(r"$F_{\delta,n}/\mathfrak R$.", r"$F_{\delta,n}/\mathfrak N$."), NFRAK)
add(97, "proof of (19.5.6.5): 'donc w se factorise en B → B/b_λ --w_λ--> F_{δ,n}'",
    "arrow label w_λ (no prime; crop)", "\\xrightarrow{w'_\\lambda}",
    "formula", fx(r"$B\to B/\mathfrak b_\lambda\xrightarrow{w'_\lambda}F_{\delta,n}$",
                  r"$B\to B/\mathfrak b_\lambda\xrightarrow{w_\lambda}F_{\delta,n}$"),
    "The print names the factor w_λ and the composite w'_λ; the TeX renames the factor w'_λ and writes the composite as q_{βδ}∘w'_λ throughout the proof (this and the next findings restore the printed text).")
add(97, "proof of (19.5.6.5): 'Considérons l'homomorphisme composé w'_λ : B/b_λ --w_λ--> F_{δ,n} --q_{βδ}--> F_{β,n}'",
    "'w'_λ :' names the composite; first arrow labelled w_λ",
    "no name for the composite; first arrow labelled w'_\\lambda",
    "formula", fx("l'homomorphisme composé\n$B/\\mathfrak b_\\lambda\\xrightarrow{w'_\\lambda}F_{\\delta,n}",
                  "l'homomorphisme composé\n$w'_\\lambda:B/\\mathfrak b_\\lambda\\xrightarrow{w_\\lambda}F_{\\delta,n}"))
add(97, "proof of (19.5.6.5): 'notons que gr⁰(q_{βδ}) = gr⁰(v_{βδ}) : C_δ → C_β'",
    "bold gr", "\\gr", "font",
    fx(r"$\gr^0(q_{\beta\delta})=\gr^0(v_{\beta\delta}):C_\delta\to C_\beta$ est",
       r"$\mathbf{gr}^0(q_{\beta\delta})=\mathbf{gr}^0(v_{\beta\delta}):C_\delta\to C_\beta$ est"), BOLDGR)
add(97, "proof of (19.5.6.5): 'comme le composé v_{βδ}∘w_λ est l'homomorphisme canonique'",
    "v_{βδ}∘w_λ", "v_{\\alpha\\beta}\\circ q_{\\beta\\delta}\\circ w'_\\lambda",
    "formula", fx(r"$v_{\alpha\beta}\circ q_{\beta\delta}\circ w'_\lambda$ est l'homomorphisme",
                  r"$v_{\beta\delta}\circ w_\lambda$ est l'homomorphisme"),
    "The printed statement is correct (v_{βδ}∘w = p_{β,n}); the TeX rewrote it.")
add(97, "proof of (19.5.6.5): 'B/b_λ → B/(b_β + J^{n+1})'",
    "b_β", "\\mathfrak b_\\alpha",
    "formula", fx(r"B/(\mathfrak b_\alpha+\mathfrak J^{n+1})$, cela montre", r"B/(\mathfrak b_\beta+\mathfrak J^{n+1})$, cela montre"),
    "Goes with the previous finding (target E_{β,n} of v_{βδ}).")
add(97, "proof of (19.5.6.5): 'l'image de J_λ = (b_λ+J)/b_λ par w'_λ est contenue'",
    "par w'_λ", "par $q_{\\beta\\delta}\\circ w'_\\lambda$",
    "formula", fx(r"par $q_{\beta\delta}\circ w'_\lambda$ est contenue", r"par $w'_\lambda$ est contenue"))
add(97, "proof of (19.5.6.5): 'contenue dans l'idéal d'augmentation F^+_{δ,n}'",
    "F^+_{δ,n} (crop)", "F_{\\beta,n}^+: silent correction",
    "misprint_in_print", fx(r"$F_{\beta,n}^+$", r"$F_{\delta,n}^+$"),
    "w'_λ = q_{βδ}∘w_λ takes values in F_{β,n}, and its image of J_λ lies in the augmentation ideal of F_{β,n} (gr⁰(q_{βδ}) = gr⁰(v_{βδ})); F^+_{δ,n} is an ideal of F_{δ,n}.",
    corrected=r"$F_{\beta,n}^+$")
add(97, "proof of (19.5.6.5): 'et par suite l'image par w'_λ de J_λ^{n+1}'",
    "'l'image par w'_λ de'", "'l'image de'",
    "missing", fx("et par suite l'image de\n", "et par suite l'image par $w'_\\lambda$ de\n"))
add(97, "proof of (19.5.6.5): 'J_λ^{n+1} = (b_λ+J^{n+1})/b_λ = J^{n+1}/(b_λ ∩ J^{n+1}) est nulle'",
    "second equality '= J^{n+1}/(b_λ ∩ J^{n+1})'", "only '(\\mathfrak b_\\lambda+\\mathfrak J^{n+1})/\\mathfrak b_\\lambda'",
    "missing", fx("^{n+1})/\n\\mathfrak b_\\lambda$",
                  "^{n+1})/\n\\mathfrak b_\\lambda=\\mathfrak J^{n+1}/(\\mathfrak b_\\lambda\\cap\\mathfrak J^{n+1})$"))
add(97, "proof of (19.5.6.5): '... est nulle. Autrement dit'",
    "'nulle' italic", "roman",
    "italics", fx(r"est nulle. Autrement", r"est \emph{nulle}. Autrement"))
add(97, "proof of (19.5.6.5): 'Autrement dit, w'_λ se factorise en'",
    "w'_λ", "$q_{\\beta\\delta}\\circ w'_\\lambda$",
    "formula", fx(r"$q_{\beta\delta}\circ w'_\lambda$ se factorise en", r"$w'_\lambda$ se factorise en"))
add(97, "proof of (19.5.6.5): 'montre aussi que gr⁰(w_{βλ}), qui est le composé'",
    "bold gr", "\\gr", "font",
    fx(r"que $\gr^0(w_{\beta\lambda})$, qui est", r"que $\mathbf{gr}^0(w_{\beta\lambda})$, qui est"), BOLDGR)
add(97, "proof of (19.5.6.5): 'B/(b_λ+J) → gr⁰(F_{δ,n}) --gr⁰(q_{βδ})--> gr⁰(F_{β,n})'",
    "gr⁰(F_{δ,n}) and gr⁰(F_{β,n}) bold; the arrow label gr⁰(q_{βδ}) roman", "\\gr throughout",
    "font", fx("\\to\\gr^0(F_{\\delta,n})\n\\xrightarrow{\\gr^0(q_{\\beta\\delta})}\\gr^0(F_{\\beta,n})$",
               "\\to\\mathbf{gr}^0(F_{\\delta,n})\n\\xrightarrow{\\gr^0(q_{\\beta\\delta})}\\mathbf{gr}^0(F_{\\beta,n})$"), BOLDGR)
add(97, "proof of (19.5.6.5): 'puisque v_{βδ}∘w_λ est l'homomorphisme canonique'",
    "v_{βδ}∘w_λ", "v_{\\beta\\delta}\\circ w",
    "formula", fx(r"$v_{\beta\delta}\circ w$ est", r"$v_{\beta\delta}\circ w_\lambda$ est"))
add(97, "proof of (19.5.6.5): 'on a aussi gr¹(q_{βδ}) = gr¹(v_{βδ}) (19.5.6.3)'",
    "bold gr", "\\gr", "font",
    fx(r"$\gr^1(q_{\beta\delta})=\gr^1(v_{\beta\delta})$ (19.5.6.3)", r"$\mathbf{gr}^1(q_{\beta\delta})=\mathbf{gr}^1(v_{\beta\delta})$ (19.5.6.3)"), BOLDGR)
add(97, "proof of (19.5.6.5), last sentence: 'prouve que gr¹(w_{βδ}) est l'homomorphisme de transition'",
    "bold gr", "\\gr", "font",
    fx(r"prouve que $\gr^1(", r"prouve que $\mathbf{gr}^1("), BOLDGR)
add(97, "proof of (19.5.6.5), last sentence: 'prouve que gr¹(w_{βδ}) est l'homomorphisme de transition'",
    "w_{βδ} (crop)", "w_{\\beta\\lambda}: silent correction",
    "misprint_in_print", fx(r"w_{\beta\lambda})$ est", r"w_{\beta\delta})$ est"),
    "The map of the lemma is w_{βλ}.", corrected=r"w_{\beta\lambda})$ est")
add(97, "(19.5.6.6): 'Les conditions de (19.5.6.5) étant satisfaites'",
    "'conditions de (19.5.6.5)'", "'conditions du lemme (19.5.6.5)'",
    "word", fx(r"conditions du lemme (19.5.6.5)", r"conditions de (19.5.6.5)"))
add(97, "(19.5.6.6), display 'grⁿ(v_{αβ}) : grⁿ(F_{β,n}) → grⁿ(E_{α,n})'",
    "bold gr", "\\gr", "font",
    fx("\\gr^n(v_{\\alpha\\beta}):\\gr^n(F_{\\beta,n})\n  \\longrightarrow\\gr^n(E_{\\alpha,n})",
       "\\mathbf{gr}^n(v_{\\alpha\\beta}):\\mathbf{gr}^n(F_{\\beta,n})\n  \\longrightarrow\\mathbf{gr}^n(E_{\\alpha,n})"), BOLDGR)
add(97, "(19.5.6.6): 'que gr⁰(v_{αβ}) et gr¹(v_{αβ}) coïncident'",
    "bold gr", "\\gr", "font",
    fx("que $\\gr^0(v_{\\alpha\\beta})$ et\n$\\gr^1(v_{\\alpha\\beta})$ coïncident",
       "que $\\mathbf{gr}^0(v_{\\alpha\\beta})$ et\n$\\mathbf{gr}^1(v_{\\alpha\\beta})$ coïncident"), BOLDGR)
add(97, "(19.5.6.6): 'que gr^j(v_{αβ}) et φ_{αβ,j} sont égaux'",
    "bold gr", "\\gr", "font",
    fx(r"que $\gr^j(v_{\alpha\beta})$ et", r"que $\mathbf{gr}^j(v_{\alpha\beta})$ et"), BOLDGR)
add(97, "(19.5.6.6), display 'gr^j(F_{λ,n}) → gr^j(E_{λ,n}) --gr^j(w_{βλ})--> gr^j(F_{β,n})'",
    "the three gr bold; the arrow label gr^j(w_{βλ}) roman (crop)", "\\gr throughout",
    "font", fx("  \\gr^j(F_{\\lambda,n})\\xrightarrow{\\varphi_{\\lambda\\lambda,j}}\n  \\gr^j(E_{\\lambda,n})\\xrightarrow{\\gr^j(w_{\\beta\\lambda})}\n  \\gr^j(F_{\\beta,n})\n",
               "  \\mathbf{gr}^j(F_{\\lambda,n})\\xrightarrow{\\varphi_{\\lambda\\lambda,j}}\n  \\mathbf{gr}^j(E_{\\lambda,n})\\xrightarrow{\\gr^j(w_{\\beta\\lambda})}\n  \\mathbf{gr}^j(F_{\\beta,n})\n"), BOLDGR)
add(97, "(19.5.6.6): 'comme gr•(E_{λ,n}) est engendré par gr¹(E_{λ,n})'",
    "raised bullet; both gr bold", "\\gr^*, \\gr^1",
    "symbol", fx("comme $\\gr^*(E_{\\lambda,n})$ est engendré par\n$\\gr^1(E_{\\lambda,n})$",
                 "comme $\\mathbf{gr}^\\bullet(E_{\\lambda,n})$ est engendré par\n$\\mathbf{gr}^1(E_{\\lambda,n})$"),
    BULLET + " The same edit sets both gr bold (font).")
add(97, "(19.5.6.6): 'transition gr^j(F_{β,n}) → gr^j(F_{α,n})'",
    "bold gr", "\\gr", "font",
    fx(r"$\gr^j(F_{\beta,n})\to\gr^j(F_{\alpha,n})$", r"$\mathbf{gr}^j(F_{\beta,n})\to\mathbf{gr}^j(F_{\alpha,n})$"), BOLDGR)
add(97, "(19.5.6.6): 'l'homomorphisme de transition grⁿ(F_{λ,n}) → grⁿ(F_{α n}) en'",
    "bold gr", "\\gr", "font",
    fx(r"$\gr^n(F_{\lambda,n})\to\gr^n", r"$\mathbf{gr}^n(F_{\lambda,n})\to\mathbf{gr}^n"), BOLDGR)
add(97, "(19.5.6.6): 'grⁿ(F_{λ,n}) → grⁿ(F_{α n}) en'",
    "F_{α n}: no comma between α and n (enlarged crop: a gap, no mark)", "F_{\\alpha,n}: silent correction",
    "misprint_in_print", fx(r"F_{\alpha,n})$ en", r"F_{\alpha\,n})$ en"),
    "Missing comma in the subscript.", conf="medium", corrected=r"F_{\alpha,n})$ en")
add(97, "(19.5.6.6), last display 'grⁿ(F_{λ,n}) --φ_{λλ,n}--> grⁿ(E_{λ,n}) → grⁿ(F_{α,n})'",
    "bold gr", "\\gr", "font",
    fx("  \\gr^n(F_{\\lambda,n})\\xrightarrow{\\varphi_{\\lambda\\lambda,n}}\n  \\gr^n(E_{\\lambda,n})\\longrightarrow\\gr^n(F_{\\alpha,n})",
       "  \\mathbf{gr}^n(F_{\\lambda,n})\\xrightarrow{\\varphi_{\\lambda\\lambda,n}}\n  \\mathbf{gr}^n(E_{\\lambda,n})\\longrightarrow\\mathbf{gr}^n(F_{\\alpha,n})"), BOLDGR)
add(97, "(19.5.6.6), last display",
    "no punctuation after grⁿ(F_{α,n}) (crop)", "trailing comma",
    "punctuation", fx("(F_{\\alpha,n}),\n\\]", "(F_{\\alpha,n})\n\\]"))

# ---------------- page 98 ----------------
add(98, "Lemme (19.5.6.7): 'vérifiant les conditions de (19.5.6.3, (i)), il existe un indice γ≥β'",
    "reference upright in the italic statement", "(19.5.6.3, (i)) italic",
    "convention", fx(r"conditions de (19.5.6.3, (i)), il existe", r"conditions de \textup{(19.5.6.3, (i))}, il existe"), conv=6)
add(98, "proof of (19.5.6.7), display 'w^j_{βγ} : gr^j(E_{γ,n}) → gr^j(F_{β,n})'",
    "bold gr (crop)", "\\gr", "font",
    fx("w_{\\beta\\gamma}^j:\\gr^j(E_{\\gamma,n})\\longrightarrow\n  \\gr^j(F_{\\beta,n})",
       "w_{\\beta\\gamma}^j:\\mathbf{gr}^j(E_{\\gamma,n})\\longrightarrow\n  \\mathbf{gr}^j(F_{\\beta,n})"), BOLDGR)
add(98, "proof of (19.5.6.7), display 'gr^j(F_{γ,n}) → gr^j(E_{γ,n}) → gr^j(F_{β,n})'",
    "bold gr (crop)", "\\gr", "font",
    fx("  \\gr^j(F_{\\gamma,n})\n  \\xrightarrow{\\varphi_{\\gamma\\gamma,j}}\\gr^j(E_{\\gamma,n})\n  \\xrightarrow{w_{\\beta\\gamma}^j}\\gr^j(F_{\\beta,n})",
       "  \\mathbf{gr}^j(F_{\\gamma,n})\n  \\xrightarrow{\\varphi_{\\gamma\\gamma,j}}\\mathbf{gr}^j(E_{\\gamma,n})\n  \\xrightarrow{w_{\\beta\\gamma}^j}\\mathbf{gr}^j(F_{\\beta,n})"), BOLDGR)
add(98, "proof of (19.5.6.7): 'choisir le même indice γ pour tous les γ_j'",
    "γ_j (enlarged crop)", "\\varphi_j: silent correction",
    "misprint_in_print", fx(r"pour tous les $\varphi_j$", r"pour tous les $\gamma_j$"),
    "The index is chosen for each of the φ_j (first line of the proof).", corrected=r"pour tous les $\varphi_j$")
add(98, "proof of (19.5.6.7): 'un homomorphisme de C_γ-algèbres graduées'",
    "'algèbres' italic (crop)", "roman",
    "italics", fx(r"$C_\gamma$-algèbres graduées", r"$C_\gamma$-\emph{algèbres} graduées"))
add(98, "proof of (19.5.6.7): '... graduées gr•(E_{γ,n}) → gr•(F_{β,n}) = F_{β,n}.'",
    "inline, at the end of the running line; raised bullets; bold gr",
    "displayed formula; \\gr^* (roman, asterisk)",
    "other", fx("\\[\n  \\gr^*(E_{\\gamma,n})\\longrightarrow\n  \\gr^*(F_{\\beta,n})=F_{\\beta,n}.\n\\]",
                "$\\mathbf{gr}^\\bullet(E_{\\gamma,n})\\to\\mathbf{gr}^\\bullet(F_{\\beta,n})=F_{\\beta,n}$."),
    "Display where the print sets the formula inline; the same edit writes the raised bullets (GLOBAL_ISSUES item 60) and the bold gr.")
add(98, "proof of (19.5.6.7): 'il en est donc de même de gr⁰(v_{αβ}∘w_{βγ}) et de gr¹(v_{αβ}∘w_{βγ})'",
    "bold gr", "\\gr", "font",
    fx("$\\gr^0(v_{\\alpha\\beta}\\circ w_{\\beta\\gamma})$ et de\n$\\gr^1(v_{\\alpha\\beta}\\circ w_{\\beta\\gamma})$~;",
       "$\\mathbf{gr}^0(v_{\\alpha\\beta}\\circ w_{\\beta\\gamma})$ et de\n$\\mathbf{gr}^1(v_{\\alpha\\beta}\\circ w_{\\beta\\gamma})$~;"), BOLDGR)
add(98, "proof of (19.5.6.7): 'comme gr•(E_{γ,n}) est engendré par gr¹(E_{γ,n})'",
    "raised bullet; both gr bold", "\\gr^*, \\gr^1",
    "symbol", fx(r"$\gr^*(E_{\gamma,n})$ est engendré par $\gr^1(E_{\gamma,n})$",
                 r"$\mathbf{gr}^\bullet(E_{\gamma,n})$ est engendré par $\mathbf{gr}^1(E_{\gamma,n})$"),
    BULLET + " The same edit sets both gr bold (font).")
add(98, "proof of (19.5.6.7): 'on en conclut que gr^j(v_{αβ}∘w_{βγ}) est aussi'",
    "bold gr", "\\gr", "font",
    fx(r"$\gr^j(v_{\alpha\beta}\circ w_{\beta\gamma})$ est aussi", r"$\mathbf{gr}^j(v_{\alpha\beta}\circ w_{\beta\gamma})$ est aussi"), BOLDGR)
add(98, "proof of (19.5.6.7): '... pour 0≤j≤n. | Appliquons maintenant à α, β et γ'",
    "no paragraph break: 'Appliquons' starts flush left (crop of the left margin)",
    "blank line: new paragraph",
    "other", fx("pour $0\\leq j\\leq n$.\n\nAppliquons maintenant", "pour $0\\leq j\\leq n$.\nAppliquons maintenant"))
add(98, "proof of (19.5.6.7), diagram, top left corner 'gr•(E_{γ,n})'",
    "raised bullet; bold gr", "\\gr^*", "symbol",
    fx(r"  \gr^*(E_{\gamma,n})\ar[r]^{w_{\beta\gamma}}", r"  \mathbf{gr}^\bullet(E_{\gamma,n})\ar[r]^{w_{\beta\gamma}}"),
    BULLET + " Same edit: bold gr.")
add(98, "proof of (19.5.6.7), diagram, bottom left corner 'gr•(E_{λ,n})' and the label of its vertical arrow 'gr(p_{γλ})'",
    "corner: raised bullet, bold gr; label: bold gr(p_{γλ}) without any superscript (crop)",
    "\\gr^*(E_{\\lambda,n}) and label \\gr^*(p_{\\gamma\\lambda})",
    "formula", fx(r"  \gr^*(E_{\lambda,n})\ar[u]_{\gr^*(p_{\gamma\lambda})}",
                  r"  \mathbf{gr}^\bullet(E_{\lambda,n})\ar[u]_{\mathbf{gr}(p_{\gamma\lambda})}"),
    "The label has no superscript in the print (the text below writes gr(p_{γλ})). Same edit: bullet and bold gr in the corner.")
add(98, "proof of (19.5.6.7): 'il suffit évidemment de montrer que l'on a Ker(v_{γδ}) ⊂ Ker(q_{βδ}), v_{γδ} et q_{βδ} étant surjectifs'",
    "inline, at the start of the running line", "displayed formula",
    "other", fx("que l'on a\n\\[\n  \\operatorname{Ker}(v_{\\gamma\\delta})\n  \\subset\\operatorname{Ker}(q_{\\beta\\delta}),\n\\]\n$v_{\\gamma\\delta}$",
                "que l'on a\n$\\operatorname{Ker}(v_{\\gamma\\delta})\\subset\\operatorname{Ker}(q_{\\beta\\delta})$,\n$v_{\\gamma\\delta}$"),
    "Display where the print sets the formula inline.")
add(98, "proof of (19.5.6.7): 'équivaut à Ker(v_{γδ}∘w_{δλ}) ⊂ Ker(q_{βδ}∘w_{δλ}) = Ker(w_{βγ}∘(gr(p_{γλ}))).'",
    "inline in the running text; bold gr", "split display; \\gr",
    "other", fx("équivaut à\n\\[\n\\begin{split}\n  \\operatorname{Ker}(v_{\\gamma\\delta}\\circ w_{\\delta\\lambda})\n  &\\subset\\operatorname{Ker}(q_{\\beta\\delta}\\circ w_{\\delta\\lambda})\\\\\n  &=\\operatorname{Ker}\\bigl(w_{\\beta\\gamma}\\circ\n  (\\gr(p_{\\gamma\\lambda}))\\bigr).\n\\end{split}\n\\]",
                "équivaut à\n$\\operatorname{Ker}(v_{\\gamma\\delta}\\circ w_{\\delta\\lambda})\\subset\\operatorname{Ker}(q_{\\beta\\delta}\\circ w_{\\delta\\lambda})=\\operatorname{Ker}(w_{\\beta\\gamma}\\circ(\\mathbf{gr}(p_{\\gamma\\lambda})))$."),
    "Display where the print sets the formula inline; same edit: bold gr.")
add(98, "proof of (19.5.6.7): 'Mais on a vu ci-dessus que gr(p_{γλ}) = gr(v_{γδ}∘w_{δλ})'",
    "bold gr", "\\gr", "font",
    fx(r"$\gr(p_{\gamma\lambda})=\gr(v_{\gamma\delta}\circ w_{\delta\lambda})$",
       r"$\mathbf{gr}(p_{\gamma\lambda})=\mathbf{gr}(v_{\gamma\delta}\circ w_{\delta\lambda})$"), BOLDGR)
add(98, "proof of (19.5.6.7): 'et il est clair que Ker(v_{γδ}∘w_{δλ}) ⊂ Ker(gr(v_{γδ}∘w_{δλ})) = Ker(gr(p_{γλ})) ⊂ Ker(w_{βγ}∘(gr(p_{γλ}))), ce qui achève'",
    "inline in the running text; bold gr", "split display; \\gr",
    "other", fx("est clair que\n\\[\n\\begin{split}\n  \\operatorname{Ker}(v_{\\gamma\\delta}\\circ w_{\\delta\\lambda})\n  &\\subset\\operatorname{Ker}\\bigl(\\gr(v_{\\gamma\\delta}\\circ\n  w_{\\delta\\lambda})\\bigr)\\\\\n  &=\\operatorname{Ker}(\\gr(p_{\\gamma\\lambda}))\n  \\subset\\operatorname{Ker}\\bigl(w_{\\beta\\gamma}\\circ\n  (\\gr(p_{\\gamma\\lambda}))\\bigr),\n\\end{split}\n\\]\nce qui",
                "est clair que\n$\\operatorname{Ker}(v_{\\gamma\\delta}\\circ w_{\\delta\\lambda})\\subset\\operatorname{Ker}(\\mathbf{gr}(v_{\\gamma\\delta}\\circ w_{\\delta\\lambda}))=\\operatorname{Ker}(\\mathbf{gr}(p_{\\gamma\\lambda}))\\subset\\operatorname{Ker}(w_{\\beta\\gamma}\\circ(\\mathbf{gr}(p_{\\gamma\\lambda})))$,\nce qui"),
    "Display where the print sets the formula inline; same edit: bold gr.")
add(98, "proof of (19.5.6.7), end: 'définir u_{βμ} comme le composé E_{μ,n} --p_{γμ}--> E_{γ,n} --u_{βγ}--> F_{β,n}.'",
    "inline, at the end of the running line", "displayed formula",
    "other", fx("comme le composé\n\\[\n  E_{\\mu,n}\\xrightarrow{p_{\\gamma\\mu}}E_{\\gamma,n}\n  \\xrightarrow{u_{\\beta\\gamma}}F_{\\beta,n}.\n\\]",
                "comme le composé\n$E_{\\mu,n}\\xrightarrow{p_{\\gamma\\mu}}E_{\\gamma,n}\\xrightarrow{u_{\\beta\\gamma}}F_{\\beta,n}$."),
    "Display where the print sets the formula inline.")
add(98, "(19.5.6.8): 'N un idéal de carré nul dans G, f : B → G/N ... Comme G/N est discrète'",
    "Fraktur N (three times; crops)", "\\mathfrak R", "symbol",
    fx("$\\mathfrak R$ un idéal de carré nul dans $G$,\n$f:B\\to G/\\mathfrak R$ un $A$-homomorphisme continu d'algèbres. Comme\n$G/\\mathfrak R$ est discrète",
       "$\\mathfrak N$ un idéal de carré nul dans $G$,\n$f:B\\to G/\\mathfrak N$ un $A$-homomorphisme continu d'algèbres. Comme\n$G/\\mathfrak N$ est discrète"),
    NFRAK + " The whole of (19.5.6.8) (pp. 98-99) has N; every \\mathfrak R there is reported.")
add(98, "(19.5.6.8), display 'B --p_α--> E_{α,n} --f_{α,n}--> G/N'",
    "Fraktur N; no punctuation after it (crop)", "G/\\mathfrak R, (trailing comma)",
    "punctuation", fx("\\xrightarrow{f_{\\alpha,n}}G/\\mathfrak R,\n\\]", "\\xrightarrow{f_{\\alpha,n}}G/\\mathfrak N\n\\]"),
    "Same edit: \\mathfrak R -> \\mathfrak N (symbol).")
add(98, "(19.5.6.8), display (19.5.6.9) 'f_{α,n}∘v_{αβ} : F_{β,n} → E_{α,n} → G/N'",
    "Fraktur N; no full stop after it (crop)", "G/\\mathfrak R. (final full stop)",
    "punctuation", fx("\\xrightarrow{f_{\\alpha,n}}G/\\mathfrak R.\n  \\tag{19.5.6.9}", "\\xrightarrow{f_{\\alpha,n}}G/\\mathfrak N\n  \\tag{19.5.6.9}"),
    "Same edit: \\mathfrak R -> \\mathfrak N (symbol).")
add(98, "(19.5.6.8), after (19.5.6.9): 'et comme F_{β,n} est une C_β-algèbre'",
    "'et comme' (lower case: the sentence continues after the display)", "'Comme'",
    "word", fx("\\end{equation}\nComme $F_{\\beta,n}$", "\\end{equation}\net comme $F_{\\beta,n}$"))
add(98, "(19.5.6.8): 'r : C → F_{β,n} → G/N'",
    "Fraktur N", "\\mathfrak R", "symbol",
    fx(r"\to G/\mathfrak R$. Comme d'autre part", r"\to G/\mathfrak N$. Comme d'autre part"), NFRAK)
add(98, "end of p. 98: '... formellement lisse, | cet homomorphisme se factorise' (p. 99)",
    "p. 99 continues the sentence flush left",
    "blank line before \\oldpage{99} (and after it): paragraph break",
    "other", fx("$A$-algèbre formellement lisse,\n\n", "$A$-algèbre formellement lisse,\n"),
    "Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). Apply together with the p. 99 top finding.")

# ---------------- page 99 ----------------
add(99, "top of p. 99: 'cet homomorphisme se factorise en r : C → G → G/N'",
    "continuation of the sentence of p. 98, flush left",
    "blank line after \\oldpage{99}: paragraph break",
    "other", fx("\\oldpage[0\\textsubscript{IV-1}]{99}\n\ncet homomorphisme", "\\oldpage[0\\textsubscript{IV-1}]{99}\ncet homomorphisme"),
    "Apply together with the end-of-p. 98 finding.")
add(99, "(19.5.6.8): 'r : C --r'--> G → G/N où r' est un A-homomorphisme continu'",
    "Fraktur N; no comma before 'où' (crop)", "G/\\mathfrak R$, où",
    "punctuation", fx(r"G\to G/\mathfrak R$, où $r'$", r"G\to G/\mathfrak N$ où $r'$"),
    "Same edit: \\mathfrak R -> \\mathfrak N (symbol).")
add(99, "(19.5.6.8), display 'J/J² → J_β/J_β² → F_{β,n}'",
    "no punctuation (crop)", "trailing comma",
    "punctuation", fx(r"\mathfrak J_\beta/\mathfrak J_\beta^2\longrightarrow F_{\beta,n},", r"\mathfrak J_\beta/\mathfrak J_\beta^2\longrightarrow F_{\beta,n}"))
add(99, "(19.5.6.8): 'un C-homomorphisme continu g : J/J² → G/N'",
    "Fraktur N", "\\mathfrak R", "symbol",
    fx(r"\to G/\mathfrak R$. Comme", r"\to G/\mathfrak N$. Comme"), NFRAK)
add(99, "(19.5.6.8): 'g se factorise en J/J² --h--> G → G/N, où h est un C-homomorphisme continu'",
    "inline in the running line; Fraktur N", "displayed formula; \\mathfrak R",
    "other", fx("factorise en\n\\[\n  \\mathfrak J/\\mathfrak J^2\\xrightarrow{h}G\\longrightarrow G/\\mathfrak R,\n\\]\noù $h$",
                "factorise en\n$\\mathfrak J/\\mathfrak J^2\\xrightarrow{h}G\\to G/\\mathfrak N$, où $h$"),
    "Display where the print sets the formula inline; same edit: \\mathfrak R -> \\mathfrak N.")
add(99, "(19.5.6.8), display 'J/J² → J_γ/J_γ² --h'--> G'",
    "no punctuation (crop)", "trailing comma",
    "punctuation", fx(r"\xrightarrow{h'}G,", r"\xrightarrow{h'}G"))
add(99, "(19.5.6.8), display 'w : S•_{C_γ}(J_γ/J_γ²) → G'",
    "raised bullet", "\\mathbf S_{C_\\gamma}^*", "symbol",
    fx(r"w:\mathbf S_{C_\gamma}^*", r"w:\mathbf S_{C_\gamma}^\bullet"), BULLET)
add(99, "(19.5.6.8): 'un élément de N, ... puisque N² = 0'",
    "Fraktur N (twice; crop)", "\\mathfrak R", "symbol",
    fx("de $\\mathfrak R$, donc tout élément de degré $n=2m$ a une image nulle, puisque\n$\\mathfrak R^2=0$",
       "de $\\mathfrak N$, donc tout élément de degré $n=2m$ a une image nulle, puisque\n$\\mathfrak N^2=0$"), NFRAK)
add(99, "(19.5.6.8), display 'S•_{C_γ}(J_γ/J_γ²) → F_{γ,n} --w'_γ--> G.'",
    "raised bullet", "\\mathbf S_{C_\\gamma}^*", "symbol",
    fx("  \\mathbf S_{C_\\gamma}^*(\\mathfrak J_\\gamma/\\mathfrak J_\\gamma^2)\n  \\longrightarrow F_{\\gamma,n}",
       "  \\mathbf S_{C_\\gamma}^\\bullet(\\mathfrak J_\\gamma/\\mathfrak J_\\gamma^2)\n  \\longrightarrow F_{\\gamma,n}"), BULLET)
add(99, "(19.5.6.8): 'Appliquons maintenant à v_{αγ} : F_{γ,n} --q_{βγ}--> F_{β,n} --v_{αβ}--> E_{α,n} le lemme (19.5.6.7)'",
    "inline in the running line", "displayed formula",
    "other", fx("Appliquons maintenant à\n\\[\n  v_{\\alpha\\gamma}:F_{\\gamma,n}\n  \\xrightarrow{q_{\\beta\\gamma}}F_{\\beta,n}\n  \\xrightarrow{v_{\\alpha\\beta}}E_{\\alpha,n}\n\\]\nle lemme",
                "Appliquons maintenant à\n$v_{\\alpha\\gamma}:F_{\\gamma,n}\\xrightarrow{q_{\\beta\\gamma}}F_{\\beta,n}\\xrightarrow{v_{\\alpha\\beta}}E_{\\alpha,n}$\nle lemme"),
    "Display where the print sets the formula inline.")
add(99, "(19.5.6.8), final diagram, top right 'G/N'",
    "Fraktur N (crop)", "\\mathfrak R", "symbol",
    fx(r"& G/\mathfrak R \\", r"& G/\mathfrak N \\"), NFRAK)
add(99, "(19.5.6.8): 'f se factorise en B --f'--> G → G/N, ce qui prouve'",
    "Fraktur N", "\\mathfrak R", "symbol",
    fx(r"G\to G/\mathfrak R$, ce qui", r"G\to G/\mathfrak N$, ce qui"), NFRAK)
add(99, "Corollaire (19.5.7), condition 1°: '(19.0.2) (cette condition sera remplie en particulier si B est noethérien et sa topologie préadique (0_I, 7.3.2))'",
    "the reference and the whole parenthesis upright, with 'noethérien' and 'préadique' in italic (crop)",
    "all italic, no emphasis",
    "convention", fx("(19.0.2) (cette condition sera remplie en particulier si\n$B$ est noethérien et sa topologie préadique ($\\mathbf 0_{\\mathrm I}$,\n7.3.2))",
                     "\\textup{(19.0.2) (cette condition sera remplie en particulier si\n$B$ est \\emph{noethérien} et sa topologie \\emph{préadique} ($\\mathbf 0_{\\mathrm I}$,\n7.3.2))}"),
    "Roman words inside the italic statement; the two emphasized words become italic inside \\textup.", conv=6)
add(99, "Corollaire (19.5.7)(ii), display (19.5.7.1): 'S•_{C_λ}((J/J²)⊗_C C_λ) → gr•_J(B)⊗_C C_λ'",
    "raised bullets; gr roman here", "\\mathbf S_{C_\\lambda}^*, \\gr_{\\mathfrak J}^*",
    "symbol", fx("\\mathbf S_{C_\\lambda}^*((\\mathfrak J/\\mathfrak J^2)\\otimes_C C_\\lambda)\n    \\longrightarrow\\gr_{\\mathfrak J}^*(B)",
                 "\\mathbf S_{C_\\lambda}^\\bullet((\\mathfrak J/\\mathfrak J^2)\\otimes_C C_\\lambda)\n    \\longrightarrow\\gr_{\\mathfrak J}^\\bullet(B)"), BULLET)

# ---------------- page 100 ----------------
add(100, "Corollaire (19.5.7)(iii): 'et l'homomorphisme (19.5.4.1) soit bijectif'",
    "reference upright in the italic statement", "(19.5.4.1) italic",
    "convention", fx(r"l'homomorphisme (19.5.4.1) soit", r"l'homomorphisme \textup{(19.5.4.1)} soit"), conv=6)
add(100, "Corollaire (19.5.7)(iii): 'et l'homomorphisme (19.5.4.1) soit bijectif'",
    "(19.5.4.1)", "(19.5.4.1): the TeX keeps the printed reading",
    "misprint_in_print", None,
    "(19.5.4.1) is a paragraph of the proof of (19.5.4), not a homomorphism; the homomorphism required bijective 'pour tout λ' is φ_λ of (19.5.7.1).",
    conf="medium", corrected="(19.5.7.1)")
add(100, "Remarque (19.5.8): 'soit un C-module de type fini et que'",
    "'de type fini' italic in the roman remark", "no emphasis",
    "italics", fx("$C$-module de type fini et\n", "$C$-module \\emph{de type fini} et\n"),
    "Judged with the remark body as roman (document-wide remark item).")
add(100, "Remarque (19.5.8): 'C soit un anneau de Zariski;'",
    "'anneau de Zariski' italic", "no emphasis",
    "italics", fx(r"soit un anneau de Zariski~;", r"soit un \emph{anneau de Zariski}~;"),
    "Judged with the remark body as roman.")
add(100, "Remarque (19.5.8)(ii'): 'φ : S•_C(J/J²) → gr•_J(B) est bijectif'",
    "raised bullets", "\\mathbf S_C^*, \\gr_{\\mathfrak J}^*",
    "symbol", fx("$\\varphi:\\mathbf S_C^*(\\mathfrak J/\\mathfrak J^2)\n  \\to\\gr_{\\mathfrak J}^*(B)$",
                 "$\\varphi:\\mathbf S_C^\\bullet(\\mathfrak J/\\mathfrak J^2)\n  \\to\\gr_{\\mathfrak J}^\\bullet(B)$"), BULLET)
add(100, "Remarque (19.5.8): 'En effet, il est clair que (i') entraîne ...'",
    "new indented paragraph after (ii')", "no blank line after \\end{enumerate}: no paragraph indent",
    "other", fx("\\end{enumerate}\nEn effet, il est clair", "\\end{enumerate}\n\nEn effet, il est clair"))
add(100, "heading 19.6: 'Cas des algèbres sur un corps.'",
    "final full stop", "no full stop",
    "punctuation", fx(r"\subsection{Cas des algèbres sur un corps}", r"\subsection{Cas des algèbres sur un corps.}"),
    "GLOBAL_ISSUES items 43/58 (no subsection title in ega0-14 to ega0-23 has the stop).")
add(100, "proof of (19.6.1): 'I. — K est une extension séparable de type fini de k.'",
    "roman, only 'de type fini' italic (crop)", "the whole sentence in \\emph",
    "italics", fx(r"\emph{I. --- $K$ est une extension séparable de type fini de $k$.}",
                  r"I. --- $K$ est une extension séparable \emph{de type fini} de $k$."))
add(100, "proof of (19.6.1): 'Compte tenu de (19.3.5, (ii)), on peut donc se borner'",
    "(19.3.5, (ii)) (crop)", "(19.3.5, (iii))",
    "number", fx(r"Compte tenu de (19.3.5, (iii))", r"Compte tenu de (19.3.5, (ii))"),
    "The print is right: (19.3.5)(ii) is transitivity, which the reduction uses; (iii) is base change.")
add(100, "proof of (19.6.1): 'où S = A—{0}'",
    "long dash for the set difference", "A-\\{0\\}",
    "convention", fx(r"$S=A-\{0\}$", r"$S=A\setmin\{0\}$"), conv=7)
add(100, "proof of (19.6.1): 'les groupes de cohomologie de Hochschild H^i_k(K, L)'",
    "superscript i (crop); the next sentence has H^n_k(K, L)", "\\mathrm H_k^n",
    "formula", fx("Hochschild\n$\\mathrm H_k^n", "Hochschild\n$\\mathrm H_k^i"))
add(100, "proof of (19.6.1): 'H^i_k(K, L) pour un (K, K)-bimodule quelconque L, sont nuls'",
    "no comma after (K, L) (end of the printed line; crop)", "comma",
    "punctuation", fx(r"(K,L)$, pour un", r"(K,L)$ pour un"))
add(100, "proof of (19.6.1): 'sont nuls : en effet'",
    "'nuls' italic", "roman",
    "italics", fx(r"sont nuls~:", r"sont \emph{nuls}~:"))
add(100, "end of p. 100: '... comme (K, K)-bimodule, | donc comme C-module à gauche' (p. 101)",
    "the sentence continues on p. 101",
    "blank line before \\oldpage{101} (and after it): paragraph break",
    "other", fx("$(K,K)$-bimodule,\n\n", "$(K,K)$-bimodule,\n"),
    "Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). The blank line after \\oldpage{101} lies in the p. 101 segment (outside pp. 96-100) and must go too.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(F), "findings written")
