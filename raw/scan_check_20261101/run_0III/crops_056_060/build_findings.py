import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III")
OUT = RUN / "findings_056_060.json"
NL = "<NL>"


def s(x):
    return None if x is None else x.replace(NL, "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    return d


C2 = "Bold chapter-0 numeral in the reference (enlarged view of the strip)."
BC = "Category letter C printed bold italic (GLOBAL_ISSUES 33); \\boldsymbol{C} as in the earlier page fixes."

L = []

# ---------------- page 56 ----------------
L.append(F(56, "after (12.1.7.2): '(0_I, 3.7.1), et (12.1.7.1) s'obtient'",
           "(0_I, 3.7.1) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 3.7.1}", r"{\textbf{0}\textsubscript{I}, 3.7.1}", C2))
L.append(F(56, "(12.1.7.5), left-hand side",
           "''E_2^{i0}=H^i(H^0_I(Γ(X, 𝓜••))→H^i(Γ(X, 𝓜••)): only two closing parentheses after 𝓜•• on the left side (enlarged crop; (12.1.7.3) has three)",
           "H^i(H_{\\mathrm I}^0(\\Gamma(X,\\mathcal M^{\\bullet\\bullet}))) with three closing parentheses (balanced)",
           "misprint_in_print", None, "high",
           r"''E_2^{i0}=H^i(H_{\mathrm I}^0(\Gamma(X,\mathcal M^{\bullet\bullet})))",
           r"''E_2^{i0}=H^i(H_{\mathrm I}^0(\Gamma(X,\mathcal M^{\bullet\bullet}))",
           "The print drops one closing parenthesis; the TeX silently corrects it. Diplomatic text: the printed, unbalanced reading.",
           corrected=r"''E_2^{i0}=H^i(H_{\mathrm I}^0(\Gamma(X,\mathcal M^{\bullet\bullet})))"))
L.append(F(56, "last line of text: 'deux homomorphismes de complexes de 𝓛• dans 𝓜••'",
           "the second 'de' (before 𝓛•) is printed in bold; the first 'de' and 'dans' are roman (enlarged crop)",
           "roman 'de'", "misprint_in_print", None, "high",
           r"complexes de $\mathcal L^\bullet$ dans", r"complexes \textbf{de} $\mathcal L^\bullet$ dans",
           "Wrong-font (bold) word in the print; the TeX silently corrects it. Reproduced as \\textbf{de}, like the other wrong-font letters kept in the diplomatic text (GLOBAL_ISSUES 29).",
           corrected="de"))

# ---------------- page 57 ----------------
L.append(F(57, "first paragraph: 'il résulte de (M, V, 1.1 a)) que ces deux homomorphismes'",
           "1.1 a)) with the label 'a)' in italics", "1.1a)) upright", "italics", None, "high",
           r"(M, V, 1.1a))", r"(M, V, 1.1 \textit{a)})",
           "Enlarged crop: 'a)' italic, the outer closing parenthesis roman."))
L.append(F(57, "(12.2.1): 'qui définit le foncteur image directe f_*'",
           "image directe in italics", "upright", "italics", None, "high",
           "foncteur<NL>image directe", r"foncteur<NL>\emph{image directe}", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'f_* : C(X)→C(Y), identique d'ailleurs'",
           "formula in the running text, with bold italic C in C(X) and C(Y)",
           "displayed with \\[ ... \\], plain C", "other", None, "high",
           r"\[<NL>f_*:C(X)\longrightarrow C(Y),<NL>\]", r"$f_*:\boldsymbol{C}(X)\longrightarrow\boldsymbol{C}(Y)$,",
           "Two differences in one edit: the print sets the formula inline (cf. GLOBAL_ISSUES 21), and both category letters C are bold italic (GLOBAL_ISSUES 33)."))
L.append(F(57, "(12.2.1): 'à la restriction à C(X) du foncteur ψ_*'",
           "bold italic C", "plain $C$", "font", None, "high",
           r"restriction à $C(X)$", r"restriction à $\boldsymbol{C}(X)$", BC))
L.append(F(57, "(12.2.1): 'un sous-faisceau d'un faisceau injectif de groupes abéliens'",
           "injectif in italics", "upright", "italics", None, "high",
           "faisceau injectif de", r"faisceau \emph{injectif} de", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'on définit les foncteurs dérivés droits'",
           "'foncteurs dérivés' italic, 'droits' roman", "upright", "italics", None, "high",
           "les foncteurs dérivés droits", r"les \emph{foncteurs dérivés} droits", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'les R^pψ_* forment un foncteur cohomologique universel (T, 2.3)'",
           "foncteur cohomologique universel in italics", "upright", "italics", None, "high",
           "un foncteur cohomologique universel (T", r"un \emph{foncteur cohomologique universel} (T",
           "Enlarged crop; the italics run over the line break."))
L.append(F(57, "(12.2.1), second paragraph: 'on suppose que 𝓕 est un 𝒪_X-Module,'",
           "'Module' in italics (𝒪_X-Module)", "upright", "italics", None, "high",
           r"est un $\mathcal O_X$-Module,", r"est un $\mathcal O_X$-\emph{Module},", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'une structure de 𝒪_Y-Module; c'est ce 𝒪_Y-Module'",
           "the first 'Module' (before ';') in italics; the second roman", "upright", "italics", None, "high",
           r"$\mathcal O_Y$-Module;", r"$\mathcal O_Y$-\emph{Module};", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'un foncteur additif de C(X) dans C(Y)'",
           "bold italic C (twice)", "plain $C$", "font", None, "high",
           r"additif de $C(X)$ dans<NL>$C(Y)$", r"additif de $\boldsymbol{C}(X)$ dans<NL>$\boldsymbol{C}(Y)$", BC))
L.append(F(57, "(12.2.1): 'les R^pf_* forment un ∂-foncteur, car si'",
           "∂-foncteur in italics", "upright", "italics", None, "high",
           r"un $\partial$-foncteur, car", r"un \emph{$\partial$-foncteur}, car", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'car si 0→𝓕'→𝓕→𝓕''→0 est une suite exacte'",
           "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           r"\[<NL>0\longrightarrow\mathcal F'\longrightarrow\mathcal F<NL>\longrightarrow\mathcal F''\longrightarrow0<NL>\]",
           r"$0\longrightarrow\mathcal F'\longrightarrow\mathcal F<NL>\longrightarrow\mathcal F''\longrightarrow0$",
           "Inline in the print (cf. GLOBAL_ISSUES 21)."))
L.append(F(57, "(12.2.1): 'l'homomorphisme ∂ : R^pψ_*(𝓕'')→R^{p+1}ψ_*(𝓕') est dans ce cas'",
           "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           r"\[<NL>\partial:R^p\psi_*(\mathcal F'')\longrightarrow<NL>R^{p+1}\psi_*(\mathcal F')<NL>\]",
           r"$\partial:R^p\psi_*(\mathcal F'')\longrightarrow<NL>R^{p+1}\psi_*(\mathcal F')$",
           "Inline in the print (cf. GLOBAL_ISSUES 21)."))
L.append(F(57, "(12.2.1): 'un homomorphisme de 𝒪_Y-Modules. Enfin'",
           "'Modules' in italics", "upright", "italics", None, "high",
           r"de $\mathcal O_Y$-Modules. Enfin", r"de $\mathcal O_Y$-\emph{Modules}. Enfin", "Enlarged crop."))
L.append(F(57, "(12.2.1): 's'identifient aux foncteurs dérivés droits de f_*'",
           "only 'dérivés' in italics", "upright", "italics", None, "high",
           "aux foncteurs dérivés droits", r"aux foncteurs \emph{dérivés} droits", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'admet une résolution injective formée de 𝒪_X-Modules'",
           "injective in italics", "upright", "italics", None, "high",
           "résolution injective formée", r"résolution \emph{injective} formée", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'formée de faisceaux flasques de groupes abéliens (G, II, 7.1)'",
           "flasques in italics", "upright", "italics", None, "high",
           "faisceaux<NL>flasques de groupes", r"faisceaux<NL>\emph{flasques} de groupes", "Enlarged crop."))
L.append(F(57, "(12.2.1): 'pour tout faisceau flasque 𝓖 (T, 2.4.1, Remarque 3'",
           "flasque in italics", "upright", "italics", None, "high",
           r"faisceau flasque $\mathcal G$", r"faisceau \emph{flasque} $\mathcal G$", "Enlarged crop."))
L.append(F(57, "(12.2.1), last sentence: 'forment un foncteur cohomologique universel de C(X) dans C(Y)'",
           "'foncteur cohomologique universel de' in italics; 'dans' roman", "upright", "italics", None, "high",
           "un foncteur<NL>cohomologique universel de", r"un \emph{foncteur<NL>cohomologique universel de}",
           "Enlarged crop: the italic 'de' before C(X) is part of the emphasis."))
L.append(F(57, "(12.2.1), last sentence: 'de C(X) dans C(Y) (T, 2.3)'",
           "bold italic C (twice)", "plain $C$", "font", None, "high",
           r"$C(X)$ dans $C(Y)$ (T", r"$\boldsymbol{C}(X)$ dans $\boldsymbol{C}(Y)$ (T", BC))

# ---------------- page 58 ----------------
L.append(F(58, "after (12.2.2.1): 'se réduit à (0_I, 4.2.2.1)'",
           "(0_I, 4.2.2.1) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 4.2.2.1}", r"{\textbf{0}\textsubscript{I}, 4.2.2.1}", C2))
L.append(F(58, "Proposition (12.2.3), whole statement 'Pour tout 𝒪_X-Module 𝓕 ... isomorphismes canoniques fonctoriels'",
           "statement printed in italics throughout",
           "statement wrapped in \\emph{...} inside the \\itshape proposition environment, so it comes out upright",
           "convention", 6, "high",
           r"\emph{Pour tout $\mathcal O_X$-Module $\mathcal F$ et tout<NL>$\mathcal O_Y$-Module localement libre de rang fini $\mathcal L$, on a des<NL>isomorphismes canoniques fonctoriels<NL>\[<NL>\label{0.12.2.3.1-fr}<NL>\tag{12.2.3.1}<NL>R^p f_*(\mathcal F)\otimes_{\mathcal O_Y}\mathcal L<NL>\xrightarrow{\sim}<NL>R^p f_*(\mathcal F\otimes_{\mathcal O_X}f^*(\mathcal L)).<NL>\]}",
           r"Pour tout $\mathcal O_X$-Module $\mathcal F$ et tout<NL>$\mathcal O_Y$-Module localement libre de rang fini $\mathcal L$, on a des<NL>isomorphismes canoniques fonctoriels<NL>\[<NL>\label{0.12.2.3.1-fr}<NL>\tag{12.2.3.1}<NL>R^p f_*(\mathcal F)\otimes_{\mathcal O_Y}\mathcal L<NL>\xrightarrow{\sim}<NL>R^p f_*(\mathcal F\otimes_{\mathcal O_X}f^*(\mathcal L)).<NL>\]",
           "Drop the \\emph wrapper (opening and closing brace in one edit). Same pattern in 24 statements of ega3-1-fr.tex (document-wide note)."))
L.append(F(58, "proof of (12.2.3): 'provenant de l'homomorphisme canonique (0_I, 4.4.3.2)'",
           "(0_I, 4.4.3.2) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 4.4.3.2}", r"{\textbf{0}\textsubscript{I}, 4.4.3.2}", C2))
L.append(F(58, "(12.2.4): 'que la suite spectrale de Leray des foncteurs composés'",
           "'suite spectrale de Leray' in italics", "upright", "italics", None, "high",
           "la<NL>suite spectrale de Leray", r"la<NL>\emph{suite spectrale de Leray}", "Enlarged view of the strip."))
L.append(F(58, "(12.2.4): 'il y a une suite spectrale birégulière dont l'aboutissement'",
           "birégulière in italics", "upright", "italics", None, "high",
           "spectrale birégulière dont", r"spectrale \emph{birégulière} dont", "Enlarged view of the strip."))

# ---------------- page 59 ----------------
L.append(F(59, "(12.2.5): 'l'homomorphisme canonique (0_I, 4.4.3.3) fournit par fonctorialité'",
           "(0_I, 4.4.3.3) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 4.4.3.3}", r"{\textbf{0}\textsubscript{I}, 4.4.3.3}", C2))
L.append(F(59, "(12.2.5): 'on obtient un homomorphisme de préfaisceaux, qui fournit l'homo-morphisme de faisceaux (12.2.5.1)'",
           "l'homc-|morphisme: the letter before the line-end hyphen is a 'c' (same shape as the other c's on the line; enlarged crop)",
           "l'homomorphisme (silently corrected)", "misprint_in_print", None, "high",
           "fournit l'homomorphisme de faisceaux", "fournit l'homcmorphisme de faisceaux",
           "Wrong sort (c for o) in the print; the TeX silently corrects it. The diplomatic reading joins the hyphenated halves: homcmorphisme.",
           corrected="l'homomorphisme"))
L.append(F(59, "(12.2.5), last sentence: 'et il est immédiat que ces homomorphismes définissent'",
           "'et il' printed in bold; 'est immédiat' roman (enlarged crop)", "roman", "misprint_in_print", None, "high",
           "et il est immédiat que", r"\textbf{et il} est immédiat que",
           "Wrong-font (bold) words in the print; the TeX silently corrects them (GLOBAL_ISSUES 29).",
           corrected="et il"))
L.append(F(59, "(12.2.6): 'et' between the diagrams (12.2.6.1) and (12.2.6.2)",
           "'et' printed in bold (enlarged crop)", "roman 'et'", "misprint_in_print", None, "high",
           r"\]<NL>et<NL>\[", r"\]<NL>\textbf{et}<NL>\[",
           "Wrong-font (bold) word in the print; the TeX silently corrects it (GLOBAL_ISSUES 29).",
           corrected="et"))

# ---------------- page 60 ----------------
L.append(F(60, "end of (12.2.6): '(la dernière combinée avec (0_I, 4.2.2.1))'",
           "(0_I, 4.2.2.1) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 4.2.2.1}", r"{\textbf{0}\textsubscript{I}, 4.2.2.1}", C2))
L.append(F(60, "(12.3.2): 'la notion d'extension d'un 𝒪_X-Module'",
           "extension in italics", "upright", "italics", None, "high",
           "notion d'extension d'un", r"notion d'\emph{extension} d'un", "Enlarged view of the strip."))
L.append(F(60, "(12.3.2), end: 'au groupe abélien des classes d'extensions de 𝓕 par 𝓖.'",
           "'groupe abélien des classes d'extensions de 𝓕 par 𝓖' in italics", "upright", "italics", None, "high",
           r"au groupe abélien des classes d'extensions de<NL>$\mathcal F$ par $\mathcal G$.",
           r"au \emph{groupe abélien des classes d'extensions de<NL>$\mathcal F$ par $\mathcal G$}.",
           "Enlarged view of the strip."))
L.append(F(60, "Proposition (12.3.3), whole statement 'Soit (X, 𝒪_X) un espace annelé ... est un 𝒪_X-Module cohérent.'",
           "statement printed in italics throughout",
           "statement wrapped in \\emph{...} inside the \\itshape proposition environment, so it comes out upright",
           "convention", 6, "high",
           r"\emph{Soit $(X,\mathcal O_X)$ un espace annelé tel que le faisceau d'anneaux<NL>$\mathcal O_X$ soit cohérent. Alors, pour tout couple de<NL>$\mathcal O_X$-Modules cohérents $\mathcal F$, $\mathcal G$ et tout<NL>$p\geq0$, $\mathcal{E}xt_{\mathcal O_X}^p(\mathcal F,\mathcal G)$ est un<NL>$\mathcal O_X$-Module cohérent.}",
           r"Soit $(X,\mathcal O_X)$ un espace annelé tel que le faisceau d'anneaux<NL>$\mathcal O_X$ soit cohérent. Alors, pour tout couple de<NL>$\mathcal O_X$-Modules cohérents $\mathcal F$, $\mathcal G$ et tout<NL>$p\geq0$, $\mathcal{E}xt_{\mathcal O_X}^p(\mathcal F,\mathcal G)$ est un<NL>$\mathcal O_X$-Module cohérent.",
           "Drop the \\emph wrapper (both braces in one edit); as for Proposition (12.2.3) on p. 58."))
L.append(F(60, "proof of (12.3.3): '0→𝓡→𝓛_{p-1}→...→𝓛_0→𝓕|U→0'",
           "low (baseline) dots between the arrows", "\\cdots (centred dots)", "symbol", None, "high",
           r"\longrightarrow\cdots\longrightarrow", r"\longrightarrow\ldots\longrightarrow",
           "Enlarged crop: the dots sit on the baseline, below the arrows (cf. GLOBAL_ISSUES 22 for EGA II)."))
L.append(F(60, "proof of (12.3.3): 'où chacun des 𝓛_i (0⩽i⩽p—1)'",
           "p—1 with the long dash (the subscript p−1 in the displays has a short minus)",
           "p-1 (minus sign)", "convention", 7, "medium",
           r"\leq i\leq p-1$)", r"\leq i\leq p\setmin 1$)",
           "Long dash used for a subtraction (GLOBAL_ISSUES 23). \\setmin proposed so that the dash appears once \\setmin is redefined; leave to the convention-7 decision."))
L.append(F(60, "proof of (12.3.3): 'cela résulte par récurrence sur p de (0_I, 5.3.2)'",
           "(0_I, 5.3.2) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 5.3.2}", r"{\textbf{0}\textsubscript{I}, 5.3.2}", C2))
L.append(F(60, "proof of (12.3.3): 'et (0_I, 5.3.4), vu l'hypothèse que 𝒪_X est cohérent'",
           "(0_I, 5.3.4) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 5.3.4}), vu", r"{\textbf{0}\textsubscript{I}, 5.3.4}), vu", C2))
L.append(F(60, "proof of (12.3.3): 'on a Ext^p_{𝒪_X|U}(𝓛|U, 𝓖|U)=0 pour tout 𝒪_X-Module 𝓛'",
           "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           r"\[<NL>\operatorname{Ext}_{\mathcal O_X|U}^p(\mathcal L|U,\mathcal G|U)=0<NL>\]",
           r"$\operatorname{Ext}_{\mathcal O_X|U}^p(\mathcal L|U,\mathcal G|U)=0$",
           "Inline in the print (cf. GLOBAL_ISSUES 21)."))
L.append(F(60, "proof of (12.3.3): 'au foncteur cohomologique contravariant 𝓕⇝Hom_{𝒪_X|U}(𝓕|U, 𝓖|U), et donne' (opening of the display)",
           "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           r"\[<NL>\mathcal F\leadsto<NL>", r"$\mathcal F\leadsto<NL>",
           "Inline in the print. Opening half of the display-to-inline change; apply together with the next finding (closing half). Kept separate so that the misprint edit for Hom (third finding below) does not overlap."))
L.append(F(60, "proof of (12.3.3): '𝓕⇝Hom_{𝒪_X|U}(𝓕|U, 𝓖|U), et donne une suite exacte' (closing of the display)",
           "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           r"\mathcal G|U),<NL>\]<NL>et donne", r"\mathcal G|U)$,<NL>et donne",
           "Closing half of the display-to-inline change; apply together with the previous finding."))
L.append(F(60, "proof of (12.3.3): '𝓕⇝Hom_{𝒪_X|U}(𝓕|U, 𝓖|U)'",
           "roman 'Hom' (enlarged crop); the next display has script 𝓗om three times",
           "\\mathcal{H}om (silently corrected)", "misprint_in_print", None, "high",
           r"\mathcal{H}om_{\mathcal O_X|U}(\mathcal F|U", r"\mathrm{Hom}_{\mathcal O_X|U}(\mathcal F|U",
           "The functor is the sheaf Hom (its derived functors are the 𝓔xt of the following display), so the roman Hom is a wrong-font misprint; the TeX silently corrects it. Independent of the two display edits (non-overlapping strings).",
           corrected=r"\mathcal{H}om_{\mathcal O_X|U}(\mathcal F|U"))
L.append(F(60, "end of the proof: 'des (𝒪_X|U)-Modules cohérents (0_I, 5.3.5)'",
           "(0_I, 5.3.5) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 5.3.5}", r"{\textbf{0}\textsubscript{I}, 5.3.5}", C2))
L.append(F(60, "end of the proof: 'il en est de même du troisième (0_I, 5.3.4).'",
           "(0_I, 5.3.4) with bold 0", "0\\textsubscript{I}, plain 0", "convention", 2, "high",
           r"{0\textsubscript{I}, 5.3.4}).", r"{\textbf{0}\textsubscript{I}, 5.3.4}).", C2))

# ---------------- checks ----------------
ok = True
pages = {}
for x in L:
    p = x["page"]
    if p not in pages:
        pages[p] = (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    fx = x["fix"]
    if fx is None:
        continue
    n = pages[p].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", p, n, repr(fx["old"][:80]))

# simulate sequential application per page (as apply_fixes.py does)
sim = dict(pages)
for x in L:
    fx = x["fix"]
    if fx is None:
        continue
    t = sim[x["page"]]
    if t.count(fx["old"]) != 1:
        ok = False
        print("SEQUENTIAL FAIL", x["page"], repr(fx["old"][:80]))
        continue
    sim[x["page"]] = t.replace(fx["old"], fx["new"])

json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in sorted(pages):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(L), "ok" if ok else "PROBLEMS")
