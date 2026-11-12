# Builds findings_350_354.json and checks every "old" string.
# Reads the diplomatic source and the page files; writes nothing but the JSON.
# In old/new strings below, the pilcrow stands for a line break (LF).
import json
import sys

RUN = r"user/Documents/ega_scan_check_20261101/run_IVback"
SRC = (r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/"
       r"diplomatic/packages/IV4/native/ega4/ega4-errata-addenda-list3-fr.tex")
OUT = RUN + "/findings_350_354.json"


def L(s):
    return None if s is None else s.replace("\u00b6", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, seg=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": L(old), "new": L(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_seg"] = seg if seg is not None else page
    F.append(d)


SEG349 = ("Text before this page's marker: it lies in the page_349.tex segment (source lines 505-531), "
          "but it is printed on p. 350.")


def heading(page, n, extra=""):
    add(page, "heading (Err_IV, %d)" % n,
        "bold '(Err_IV, %d)' with no full stop; the subscript IV is in light (medium) type, "
        "Err, the number and the parentheses bold" % n,
        "\\paragraph{(Err\\textsubscript{IV}, %d).}: a full stop after the parenthesis, and the bold "
        "heading font sets the subscript IV bold" % n,
        "punctuation", None, "high",
        r"(Err\textsubscript{IV}, %d).}" % n, r"($\mathbf{Err}_{\mathrm{IV}}$, %d)}" % n,
        "One edit for both differences, in the heading form set by the coordinator "
        "(\\paragraph{($\\mathbf{Err}_{\\mathrm{IV}}$, n)}, no final full stop, as in the EGA III errata): "
        "the full stop goes and the subscript IV comes out light. Same pattern in every Err_IV heading "
        "of Liste 3." + extra)


def conv2(page, where, numeral, old, new, extra="", seg=None):
    add(page, where, "bold %s" % numeral, "plain %s" % numeral, "convention", 2, "high",
        old, new, extra, seg=seg)


def conv1(page, where, old, new, extra="", seg=None):
    add(page, where, "bold italic k", "plain $k$", "convention", 1, "high", old, new, extra, seg=seg)


def ital(page, where, words, old, new, extra="", seg=None, conf="high"):
    add(page, where, "'%s' italic" % words, "'%s' roman" % words, "italics", None, conf,
        old, new, extra, seg=seg)


# ---------------------------------------------------------------- page 350 (own segment)
heading(350, 20)
conv2(350, "(Err_IV, 20) 'Après (IV, 4.5.19)'", "IV", r"Après (IV, 4.5.19)", r"Après (\textbf{IV}, 4.5.19)")
conv1(350, "Corollaire (4.5.19.3), 'tels que k(x) soit radiciel'",
      r"tels que $k(x)$ soit radiciel", r"tels que $\boldsymbol{k}(x)$ soit radiciel")
conv1(350, "proof of (4.5.19.3), 'Si x in X est tel que k(x)'",
      r"est tel que $k(x)$¶soit radiciel", r"est tel que $\boldsymbol{k}(x)$¶soit radiciel")
conv2(350, "proof of (4.5.19.3), '(I, 3.4.9)'", "I", r"de $x$ (I, 3.4.9);", r"de $x$ (\textbf{I}, 3.4.9);")
ital(350, "proof of (4.5.19.3), 'nécessairement à deux composantes'", "deux",
     r"nécessairement à deux composantes", r"nécessairement à \emph{deux} composantes")
add(350, "proof of (4.5.19.3), 'l'ensemble Y = p(U_{i<j} X'_{ij}) répond'",
    "set in the line: 'l'ensemble Y=p(U_{i<j}X'_{ij}) répond à la question' (index i<j under the union, "
    "ordinary parentheses)",
    "displayed: \\[ Y=p\\left(\\bigcup_{i<j}X'_{ij}\\right) \\]",
    "formula", None, "high",
    r"l'ensemble¶\[¶ Y=p\left(\bigcup_{i<j}X'_{ij}\right)¶\]¶répond",
    r"l'ensemble $Y=p(\bigcup_{i<j}X'_{ij})$¶répond", "")
ital(350, "proof of (4.5.19.3), last word 'rare'", "rare", r"par suite rare.", r"par suite \emph{rare}.")
heading(350, 21)
conv2(350, "(Err_IV, 21) 'Dans (IV, 5.6.11.1)'", "IV", r"Dans (IV, 5.6.11.1)", r"Dans (\textbf{IV}, 5.6.11.1)")
heading(350, 22)
conv2(350, "(Err_IV, 22) 'Après (IV, 6.2.3)'", "IV", r"Après (IV, 6.2.3)", r"Après (\textbf{IV}, 6.2.3)")
add(350, "Proposition (6.2.4), 'Sous les hypothèses de (6.2.3)'",
    "the reference (6.2.3) upright inside the italic statement",
    "{\\hyperref[...]{(6.2.3)}} inside the italic proposition environment: comes out italic",
    "convention", 6, "high",
    r"hypothèses de {\hyperref[canon-index.ega4.c04.prop.6-2-3]{(6.2.3)}}, soit",
    r"hypothèses de \textup{\hyperref[canon-index.ega4.c04.prop.6-2-3]{(6.2.3)}}, soit",
    "Reference near source line 574 named in the coordinator note.")
add(350, "display '... -> K_i -> K_{i-1} -> ... -> K_0 -> M -> 0'",
    "baseline dots '...' (twice)", "\\cdots (twice)", "symbol", None, "high",
    r" \cdots\longrightarrow K_i\longrightarrow K_{i-1}\longrightarrow¶ \cdots\longrightarrow K_0",
    r" \ldots\longrightarrow K_i\longrightarrow K_{i-1}\longrightarrow¶ \ldots\longrightarrow K_0", "")
add(350, "end of the display '... -> M -> 0'", "no full stop after the 0",
    "'M\\longrightarrow0.'", "punctuation", None, "high",
    r"M\longrightarrow0.¶\]", r"M\longrightarrow0¶\]", "")
add(350, "after the display: 'On a vu que les L_i, N, ...'",
    "'On a vu que' begins a new, indented paragraph",
    "no blank line after \\]: same paragraph, no indent", "other", None, "high",
    r"\]¶On a vu que", r"\]¶¶On a vu que", "Paragraph break after a display (GLOBAL_ISSUES 47 pattern).")
add(350, "page break 350/351: '... B_0(L.) est' | 'plat par (0_I, 6.1.2)'",
    "the sentence runs on from p. 350 to p. 351 (mid-sentence break)",
    "a blank line before \\oldpage[IV]{351}: paragraph break", "marker", None, "high",
    r"dernier cas¶$B_0(L_\bullet)$ est¶¶", r"dernier cas¶$B_0(L_\bullet)$ est¶",
    "The blank line is the end of this page's segment, just before the p. 351 marker; no blank line "
    "follows the marker (\\oldpage ends with \\ignorespaces).")
# ---------------------------------------------------------------- page 351
conv2(351, "first line, '(0_I, 6.1.2)'", "0 with a light subscript I",
      r"plat par ($0_{\mathrm I}$, 6.1.2)", r"plat par ($\mathbf{0}_{\mathrm I}$, 6.1.2)",
      "Bold 0 with a light subscript I (GLOBAL_ISSUES 108 form).")
add(351, "'H_n(K.(x)_AL.) est canoniquement isomorphe à (+)_{p+q=n}(H_p(K.)(x)_AH_q(L.)) (G, I, 5.5)'",
    "in the running text: 'H_n(K.(x)_AL.) est canoniquement isomorphe à (+)_{p+q=n} (H_p(K.)(x)_AH_q(L.)) "
    "(G, I, 5.5), donc'",
    "a display H_n(...)\\simeq\\bigoplus_{p+q=n} H_p(K.)\\otimes_AH_q(L.): the words 'est canoniquement "
    "isomorphe à' replaced by \\simeq, the outer parentheses dropped",
    "missing", None, "high",
    r"dans ces conditions,¶\[¶ H_n(K_\bullet\otimes_AL_\bullet)\simeq¶ \bigoplus_{p+q=n}¶ "
    r"H_p(K_\bullet)\otimes_AH_q(L_\bullet)¶\]¶(G, I, 5.5)",
    r"dans ces conditions,¶$H_n(K_\bullet\otimes_AL_\bullet)$ est canoniquement isomorphe à¶"
    r"$\bigoplus_{p+q=n}(H_p(K_\bullet)\otimes_AH_q(L_\bullet))$ (G, I, 5.5)",
    "Restores the printed words and parentheses and sets the formula in the line.")
ital(351, "'est une résolution de M(x)_AN'", "résolution", r"est une résolution de",
     r"est une \emph{résolution} de")
ital(351, "'par des B-modules libres.'", "libres", r"$B$-modules¶libres. Posons",
     r"$B$-modules¶\emph{libres}. Posons", "Independent of the next finding.")
add(351, "'Posons r = dim.proj_AM, s = dim.proj_B(N) = dim.proj_{B(x)_Ak}(N(x)_Ak) : il y a donc'",
    "in the running text; 'dim.proj_AM' without parentheses; followed by ' : il y a donc' (colon, small "
    "'il')",
    "a display with \\qquad, \\operatorname{dim.proj}_A(M), ending '.', then 'Il y a donc'",
    "formula", None, "high",
    r"Posons¶\[¶ r=\operatorname{dim.proj}_A(M),\qquad¶ s=\operatorname{dim.proj}_B(N)=¶ "
    r"\operatorname{dim.proj}_{B\otimes_Ak}(N\otimes_Ak).¶\]¶Il y a donc",
    r"Posons $r=\operatorname{dim.proj}_AM$,¶"
    r"$s=\operatorname{dim.proj}_B(N)=\operatorname{dim.proj}_{B\otimes_Ak}(N\otimes_Ak)$ :¶il y a donc",
    "Inline formulas, the print's parenthesis-free dim.proj_AM, and its ' : il' for '. Il'.")
conv2(351, "'Il reste à prouver (0, 17.2.6)'", "0", r"($0$, 17.2.6)", r"(\textbf{0}, 17.2.6)",
      "Bare bold 0.")
add(351, "'que l'on a Tor^B_{r+s}(M(x)_AN, k(B)) != 0. Utilisant'",
    "in the running text", "displayed", "formula", None, "high",
    r"que l'on a¶\[¶ \operatorname{Tor}^{B}_{r+s}(M\otimes_AN,k(B))\neq0.¶\]¶Utilisant",
    r"que l'on a $\operatorname{Tor}^{B}_{r+s}(M\otimes_AN,k(B))\neq0$.¶Utilisant",
    "Apply before the next finding (convention 1 inside this formula).")
conv1(351, "'Tor^B_{r+s}(M(x)_AN, k(B)) != 0'", r"AN,k(B))\neq0", r"AN,\boldsymbol{k}(B))\neq0",
      "Apply after the previous finding (inline formula), whose 'old' contains this text.")
conv1(351, "display 'Tor^B_{r+s}(M(x)_AN, k(B)) = H_{r+s}(...)', first k(B)",
      r"AN,k(B))=¶ H_{r+s}", r"AN,\boldsymbol{k}(B))=¶ H_{r+s}")
conv1(351, "display 'Tor ... = H_{r+s}((K.(x)_AL.)(x)_Bk(B))', second k(B)",
      r"L_\bullet)\otimes_Bk(B)).¶\]", r"L_\bullet)\otimes_B\boldsymbol{k}(B)).¶\]")
add(351, "after the display: 'Mais on peut écrire'",
    "'Mais on peut écrire' begins a new, indented paragraph",
    "no blank line after \\]: same paragraph", "other", None, "high",
    r"\]¶Mais on peut écrire", r"\]¶¶Mais on peut écrire", "Independent of the next finding.")
add(351, "'Mais on peut écrire (K.(x)_AL.)(x)_Bk(B) = (K.(x)_Ak)(x)_k(L.(x)_Bk(B)), qui est donc'",
    "in the running text", "displayed", "formula", None, "high",
    r"Mais on peut écrire¶\[¶ (K_\bullet\otimes_AL_\bullet)\otimes_Bk(B)=¶ (K_\bullet\otimes_Ak)\otimes_k¶ "
    r"(L_\bullet\otimes_Bk(B)),¶\]¶qui est donc",
    r"Mais on peut écrire¶$(K_\bullet\otimes_AL_\bullet)\otimes_Bk(B)="
    r"(K_\bullet\otimes_Ak)\otimes_k(L_\bullet\otimes_Bk(B))$,¶qui est donc",
    "Apply before the next two findings (convention 1 inside this formula).")
conv1(351, "'(K.(x)_AL.)(x)_Bk(B) = ...', first k(B)",
      r"L_\bullet)\otimes_Bk(B)=(K", r"L_\bullet)\otimes_B\boldsymbol{k}(B)=(K",
      "Apply after the inline-formula finding before it ('old' taken from the text after it).")
conv1(351, "'... (x)_k(L.(x)_Bk(B)), qui est donc', second k(B)",
      r"(L_\bullet\otimes_Bk(B))$,¶qui", r"(L_\bullet\otimes_B\boldsymbol{k}(B))$,¶qui",
      "Apply after the inline-formula finding ('old' taken from the text after it).")
add(351, "Künneth: 'H_{r+s}((K.(x)_Ak)(x)_k(L.(x)_Bk(B))) = H_r(K.(x)_Ak)(x)_kH_s(L.(x)_Bk(B)),'",
    "in the running text, with an equals sign", "displayed, with \\simeq for the printed '='",
    "formula", None, "high",
    r"Künneth donne¶\[¶ H_{r+s}((K_\bullet\otimes_Ak)\otimes_k¶ (L_\bullet\otimes_Bk(B)))\simeq¶ "
    r"H_r(K_\bullet\otimes_Ak)\otimes_k¶ H_s(L_\bullet\otimes_Bk(B)),¶\]¶l'homologie",
    r"Künneth donne¶$H_{r+s}((K_\bullet\otimes_Ak)\otimes_k(L_\bullet\otimes_Bk(B)))="
    r"H_r(K_\bullet\otimes_Ak)\otimes_kH_s(L_\bullet\otimes_Bk(B))$,¶l'homologie",
    "Inline formula and the printed '=' (the TeX's \\simeq is not printed). Apply before the next two "
    "findings.")
conv1(351, "Künneth formula, first k(B)",
      r"(L_\bullet\otimes_Bk(B)))=H_r", r"(L_\bullet\otimes_B\boldsymbol{k}(B)))=H_r",
      "Apply after the Künneth inline-formula finding ('old' taken from the text after it).")
conv1(351, "Künneth formula, second k(B)",
      r"H_s(L_\bullet\otimes_Bk(B))$", r"H_s(L_\bullet\otimes_B\boldsymbol{k}(B))$",
      "Apply after the Künneth inline-formula finding ('old' taken from the text after it).")
add(351, "'l'homologie du premier (resp. second complexe) étant nulle'",
    "'(resp. second complexe)': the parenthesis closes after 'complexe'",
    "'(resp. second) complexe'", "punctuation", None, "high",
    r"(resp. second) complexe étant", r"(resp. second complexe) étant",
    "The TeX moves the printed parenthesis; the printed wording is grammatical, not a misprint.")
add(351, "'On a donc Tor^B_{r+s}(M(x)_AN, k(B)) = Tor^A_r(M, k)(x)_kTor^B_s(N, k(B)) à isomorphie près'",
    "in the running text", "displayed", "formula", None, "high",
    r"On a donc¶\[¶ \operatorname{Tor}^{B}_{r+s}(M\otimes_AN,k(B))=¶ \operatorname{Tor}^{A}_{r}(M,k)\otimes_k¶ "
    r"\operatorname{Tor}^{B}_{s}(N,k(B))¶\]¶à isomorphie",
    r"On a donc¶$\operatorname{Tor}^{B}_{r+s}(M\otimes_AN,k(B))=\operatorname{Tor}^{A}_{r}(M,k)\otimes_k"
    r"\operatorname{Tor}^{B}_{s}(N,k(B))$¶à isomorphie",
    "Apply before the next two findings.")
conv1(351, "'On a donc Tor^B_{r+s}(M(x)_AN, k(B)) = ...', first k(B)",
      r"AN,k(B))=\operatorname{Tor}^{A}", r"AN,\boldsymbol{k}(B))=\operatorname{Tor}^{A}",
      "Apply after the previous inline-formula finding ('old' taken from the text after it).")
conv1(351, "'... Tor^B_s(N, k(B)) à isomorphie près', second k(B)",
      r"(N,k(B))$¶à", r"(N,\boldsymbol{k}(B))$¶à",
      "Apply after the inline-formula finding ('old' taken from the text after it).")
heading(351, 23)
conv2(351, "(Err_IV, 23) 'Dans (IV, 6.10.1)'", "IV", r"Dans (IV, 6.10.1)", r"Dans (\textbf{IV}, 6.10.1)")
heading(351, 24)
conv2(351, "(Err_IV, 24) 'Dans (IV, 6.14.4)'", "IV", r"{IV, 6.14.4}", r"{\textbf{IV}, 6.14.4}",
      "Link text of the \\hyperref.")
ital(351, "(Err_IV, 24) '(Bourbaki, Alg., chap. V, § 6, exerc. 8 c))'", "c)",
     r"exerc.~8 c))", r"exerc.~8 \emph{c)})", "The label 'c)' is italic, the closing parenthesis of the "
     "citation upright.")
ital(351, "(Err_IV, 24) 'une extension algébrique séparable de A. Soit'", "algébrique",
     r"extension algébrique séparable de $A$.¶", r"extension \emph{algébrique} séparable de $A$.¶",
     "The second 'extension algébrique séparable de A, les' is roman in the print.")
ital(351, "(Err_IV, 24) 'est radicielle sur K''", "radicielle",
     r"est radicielle sur $K'$", r"est \emph{radicielle} sur $K'$")
add(351, "(Err_IV, 24) 'On a x = Sum_lambda e_lambda b_lambda avec b_lambda in B'",
    "no comma after the formula: 'x=Σe_λb_λ avec b_λ∈B'", "'$x=\\sum_\\lambda e_\\lambda b_\\lambda$, avec'",
    "punctuation", None, "high", r"e_\lambda b_\lambda$, avec", r"e_\lambda b_\lambda$ avec", "")
add(351, "(Err_IV, 24) 'tels que l'on ait Sum e^{p^r} b^{p^r} = Sum e^{p^r} a_lambda; mais'",
    "in the running text", "displayed", "formula", None, "high",
    r"tels que l'on ait¶\[¶ \sum_\lambda e_\lambda^{p^r}b_\lambda^{p^r}=¶ \sum_\lambda e_\lambda^{p^r}a_\lambda;¶"
    r"\]¶mais cela",
    r"tels que l'on ait $\sum_\lambda e_\lambda^{p^r}b_\lambda^{p^r}=\sum_\lambda e_\lambda^{p^r}a_\lambda$;¶"
    r"mais cela", "")
heading(351, 25)
conv2(351, "(Err_IV, 25) 'Dans (IV, 7.4.8, B))'", "IV", r"Dans (IV, 7.4.8, B))", r"Dans (\textbf{IV}, 7.4.8, B))")
add(351, "(Err_IV, 25) 'par R. Kiehl'", "KIEHL in capitals and small capitals", "R.~Kiehl (plain)",
    "font", None, "high", r"par R.~Kiehl,", r"par R.~\textsc{Kiehl},", "")
add(351, "(Err_IV, 25) title 'Ausgezeichnete Ringe der nichtarchimedischen analytischen Geometrie'",
    "the title is roman; only 'Inventiones Mathematicae' is italic (crop p351s3_kiehl.png)",
    "\\emph{Ausgezeichnete ... Geometrie}", "italics", None, "high",
    r"\emph{Ausgezeichnete Ringe der nichtarchimedischen¶analytischen Geometrie}",
    r"Ausgezeichnete Ringe der nichtarchimedischen¶analytischen Geometrie", "")
heading(351, 26)
conv2(351, "(Err_IV, 26) 'Dans (IV, 7.8.4), ligne 9'", "IV", r"Dans (IV, 7.8.4), ligne 9",
      r"Dans (\textbf{IV}, 7.8.4), ligne 9")
add(351, "(Err_IV, 26) 'Il a été démontré par R. Kiehl'", "KIEHL in capitals and small capitals",
    "R.~Kiehl (plain)", "font", None, "high",
    r"démontré par R.~Kiehl (dans", r"démontré par R.~\textsc{Kiehl} (dans", "")
add(351, "(Err_IV, 26) '(dans l'article cité en (Err_IV, 25))'",
    "'(Err_IV, 25)' in bold (parentheses, Err, comma, 25) with a light subscript IV; the outer closing "
    "parenthesis roman (crop p351s4_err25_zoom.png)",
    "(Err\\textsubscript{IV}, 25)) all in roman", "font", None, "high",
    r"(Err\textsubscript{IV}, 25)) que", r"\textbf{($\mathbf{Err}_{\mathrm{IV}}$, 25)}) que",
    "Bold reference in the form of the EGA III errata fixes (\\textbf{($\\mathbf{Err}_{\\mathrm{III}}$, 9)}), "
    "matching the coordinator's heading form; the outer closing parenthesis stays roman.")
# ---------------------------------------------------------------- page 352
heading(352, 27)
conv2(352, "(Err_IV, 27) 'Dans (IV, 7.8.4), ajouter'", "IV", r"Dans (IV, 7.8.4), ajouter",
      r"Dans (\textbf{IV}, 7.8.4), ajouter")
ital(352, "(vi), 'noethérien intègre de dimension 1'", "intègre de dimension",
     r"noethérien intègre de dimension¶1;", r"noethérien \emph{intègre de dimension}¶1;",
     "The '1' is roman in the print.")
ital(352, "(vi), 'pour qu'il soit excellent,'", "excellent",
     r"pour qu'il soit excellent,¶il faut", r"pour qu'il soit \emph{excellent},¶il faut")
ital(352, "(vi), 'soient géométriquement réduites'", "géométriquement réduites",
     r"soient géométriquement réduites, ou", r"soient \emph{géométriquement réduites}, ou")
ital(352, "(vi), 'son complété Â soit réduit'", "réduit",
     r"$\widehat A$ soit réduit et", r"$\widehat A$ soit \emph{réduit} et")
ital(352, "(vi), 'des extensions séparables du corps des fractions'", "séparables",
     r"extensions séparables du corps", r"extensions \emph{séparables} du corps")
ital(352, "(vi), 'que A est universellement japonais'", "universellement japonais",
     r"est universellement japonais. Lorsque", r"est \emph{universellement japonais}. Lorsque")
ital(352, "(vi), 'un anneau de valuation discrète'", "anneau de valuation discrète",
     r"un anneau de¶valuation discrète, il", r"un \emph{anneau de¶valuation discrète}, il",
     "Independent of the next finding.")
add(352, "(vi), 'il en est de même de A;'",
    "plain A without the hat ('il en est de même de A;'), while the 'Â' before and after carry it "
    "(crops p352s1_Ahat_b.png, p352s1_Ahat2_b.png)",
    "$\\widehat A$ (silently corrected)", "misprint_in_print", None, "high",
    r"de même de $\widehat A$;", r"de même de $A$;",
    "Misprint: 'if A is a discrete valuation ring, so is Â' needs Â. The TeX silently corrects it; the "
    "diplomatic text restores the printed A.", corrected=r"\widehat A")
ital(352, "(vi), 'dire que A est excellent signifie'", "excellent",
     r"est¶excellent signifie", r"est¶\emph{excellent} signifie")
ital(352, "(vi), 'une extension séparable de K'", "séparable",
     r"extension séparable de $K$, condition", r"extension \emph{séparable} de $K$, condition")
heading(352, 28)
conv2(352, "(Err_IV, 28) 'Après (IV, 8.10.3)'", "IV", r"Après (IV, 8.10.3)", r"Après (\textbf{IV}, 8.10.3)")
conv1(352, "Remarque (8.10.3.1), 'X_alpha = Spec(k(s))'",
      r"\operatorname{Spec}(k(s))$", r"\operatorname{Spec}(\boldsymbol{k}(s))$")
heading(352, 29)
conv2(352, "(Err_IV, 29) 'Dans (IV, 8.12.8)'", "IV", r"Dans (IV, 8.12.8)", r"Dans (\textbf{IV}, 8.12.8)")
ital(352, "(Err_IV, 29) '« tel qu'il existe un O_Y-Module ample »'", "tel qu'il existe un O_Y-Module ample",
     r"« tel qu'il existe un¶$\sh{O}_Y$-Module ample »",
     r"« \emph{tel qu'il existe un¶$\sh{O}_Y$-Module ample} »", "The quoted words of the italic statement.")
ital(352, "(Err_IV, 29) '« et quasi-séparé »'", "et quasi-séparé",
     r"« et quasi-séparé »", r"« \emph{et quasi-séparé} »")
ital(352, "(Err_IV, 29) 'une propriété locale sur Y'", "locale",
     r"propriété locale sur", r"propriété \emph{locale} sur")
ital(352, "(Err_IV, 29) 'supposer Y affine, ce qui »'", "affine",
     r"supposer $Y$ affine, ce qui", r"supposer $Y$ \emph{affine}, ce qui")
heading(352, 30)
conv2(352, "(Err_IV, 30) 'Après (IV, 8.12.11)'", "IV", r"Après (IV, 8.12.11)", r"Après (\textbf{IV}, 8.12.11)")
ital(352, "proof of (8.12.12), 'g(U) est ouvert dans f^{-1}(U)'", "ouvert",
     r"$g(U)$ est ouvert dans¶$f^{-1}(U)$;", r"$g(U)$ est \emph{ouvert} dans¶$f^{-1}(U)$;")
conv2(352, "proof of (8.12.12), '(I, 5.2.1)'", "I", r"de (I, 5.2.1) que", r"de (\textbf{I}, 5.2.1) que")
ital(352, "proof of (8.12.12), 'g est une immersion ouverte'", "immersion ouverte",
     r"une immersion ouverte. D'autre", r"une \emph{immersion ouverte}. D'autre")
ital(352, "proof of (8.12.12), 'g est une immersion fermée'", "immersion fermée",
     r"$g$ est une immersion fermée", r"$g$ est une \emph{immersion fermée}")
conv2(352, "proof of (8.12.12), '(I, 5.4.6)'", "I", r"(I, 5.4.6), donc", r"(\textbf{I}, 5.4.6), donc")
ital(352, "proof of (8.12.12), I), 'Supposons d'abord Y normal'", "normal",
     r"d'abord $Y$ normal, et", r"d'abord $Y$ \emph{normal}, et")
ital(352, "proof of (8.12.12), I), 'c'est un ensemble ouvert dans X'", "ouvert",
     r"un ensemble ouvert¶dans $X$", r"un ensemble \emph{ouvert}¶dans $X$")
add(352, "I), footnote mark after '(13.1.4)'",
    "the footnote mark stands before the full stop: '(13.1.4) (1). Il résulte'",
    "'(13.1.4).\\footnote{...}': the mark after the full stop", "punctuation", None, "high",
    r"{(13.1.4)}}.\footnote{Le", r"{(13.1.4)}}\footnote{Le",
    "Part 1 of 2: removes the full stop before \\footnote; part 2 (next finding) puts it after the "
    "footnote. Apply both. The '(1)' style of the mark is the document-wide footnote item.")
add(352, "I), footnote mark: full stop after the footnote", "(see the previous finding)",
    "no full stop after \\footnote{...}", "punctuation", None, "high",
    r"{(13.1.4)}}.} Il résulte", r"{(13.1.4)}}.}. Il résulte",
    "Part 2 of 2 with the previous finding; apply both.")
add(352, "footnote: 'n'est utilisé dans la preuve de (13.1.4)'", "'utilisé' (masculine)",
    "'utilisée'", "word", None, "high", r"n'est utilisée dans", r"n'est utilisé dans",
    "The TeX changes the printed agreement; 'ni (8.12.12) ni aucune de ses conséquences n'est utilisé' is "
    "the printed wording (not a misprint).")
add(352, "page break 352/353: 'Il résulte alors de (8.12.10)' | 'que la restriction f|V'",
    "the sentence runs on to p. 353 (mid-sentence break)",
    "a blank line before \\oldpage[IV]{353}: paragraph break", "marker", None, "high",
    r"{(8.12.10)}}¶¶", r"{(8.12.10)}}¶",
    "The blank line is the end of this page's segment, just before the p. 353 marker; no blank line "
    "follows the marker.")
# ---------------------------------------------------------------- page 353
add(353, "II), '(par exemple de la forme Y[T_1, ..., T_r])'", "last variable T_r",
    "T_n", "formula", None, "high", r"$Y[T_1,\ldots,T_n]$", r"$Y[T_1,\ldots,T_r]$",
    "Crop p353s1_Tr.png.")
add(353, "II), 'Posons Y' = Spec(O_{Y,y}), X' = X_(Y'), Z' = Z_(Y'), de sorte que'",
    "in the running text", "a display joined by \\qquad", "formula", None, "high",
    r"Posons¶\[¶ Y'=\operatorname{Spec}(\sh{O}_{Y,y}),\qquad¶ X'=X_{(Y')},\qquad Z'=Z_{(Y')},¶\]¶de sorte",
    r"Posons $Y'=\operatorname{Spec}(\sh{O}_{Y,y})$, $X'=X_{(Y')}$, $Z'=Z_{(Y')}$,¶de sorte", "")
conv2(353, "II), '(I, 3.6.5)'", "I", r"(I, 3.6.5)", r"(\textbf{I}, 3.6.5)")
ital(353, "II), 'Puisque Y' est normal'", "normal",
     r"$Y'$ est normal, on peut", r"$Y'$ est \emph{normal}, on peut")
ital(353, "II), 'il existe une Y'-section g' de X''", "section ... de",
     r"$Y'$-section $g'$ de $X'$", r"$Y'$-\emph{section} $g'$ \emph{de} $X'$",
     "The print sets 'section' and 'de' italic here (crops p353s2_sect_zoom.png, p353s2_de_zoom.png).")
ital(353, "II), 'comme une Y'-section de Z''", "de",
     r"$Y'$-section de $Z'$.", r"$Y'$-section \emph{de} $Z'$.", "'section' roman, 'de' italic.")
ital(353, "II), 'suivant la méthode de (8.1.2, a))'", "a)",
     r"la méthode de¶({\hyperref[canon-index.ega4.c04.statement.8-1-2]{8.1.2}}, a))",
     r"la méthode de¶({\hyperref[canon-index.ega4.c04.statement.8-1-2]{8.1.2}}, \emph{a)})",
     "Independent of the next finding.")
add(353, "II), '(8.1.2, a)) d'où l'on conclut'", "no comma before 'd'où'", "', d'où'",
    "punctuation", None, "high", r"), d'où l'on conclut", r") d'où l'on conclut", "")
ital(353, "II), 'd'une U-section g de h^{-1}(U)'", "de",
     r"$U$-section $g$ de $h^{-1}(U)$", r"$U$-section $g$ \emph{de} $h^{-1}(U)$")
ital(353, "II), 'g est une U-section de f^{-1}(U)'", "de",
     r"$U$-section de $f^{-1}(U)$. Mais", r"$U$-section \emph{de} $f^{-1}(U)$. Mais")
conv2(353, "II), 'il suffit pour cela (I, 5.2.2)'", "I", r"pour cela (I, 5.2.2) de voir",
      r"pour cela (\textbf{I}, 5.2.2) de voir")
heading(353, 31)
conv2(353, "(Err_IV, 31) 'Dans (IV, 10.4)'", "IV", r"{IV, 10.4}", r"{\textbf{IV}, 10.4}",
      "Link text of the \\hyperref.")
add(353, "Corollaire (10.4.12) (i), 'bijectif et fini (donc un homéomorphisme universel (2.4.5)).'",
    "'fini (donc un' roman, 'homéomorphisme universel' italic, '(2.4.5))' roman (crop p353s3_i.png)",
    "all italic (corollary environment)", "convention", 6, "high",
    r"bijectif et fini (donc un homéomorphisme¶universel {\hyperref[canon-index.ega4.c04.prop.2-4-5]{(2.4.5)}}).",
    r"bijectif et \textup{fini (donc un \emph{homéomorphisme¶universel} "
    r"{\hyperref[canon-index.ega4.c04.prop.2-4-5]{(2.4.5)}})}.",
    "Covers the reference (2.4.5) near source line 842 named in the coordinator note.")
add(353, "Corollaire (10.4.12) (ii), '(condition automatiquement vérifiée ... corps parfait)'",
    "the parenthesis roman, with 'parfait' italic", "all italic (corollary environment)",
    "convention", 6, "high",
    r"birationnel (condition automatiquement vérifiée si pour tout point¶maximal $x$ de $X$, $k(x)$ est un "
    r"corps parfait). Alors",
    r"birationnel \textup{(condition automatiquement vérifiée si pour tout point¶maximal $x$ de $X$, $k(x)$ "
    r"est un corps \emph{parfait})}. Alors",
    "Apply before the next finding (convention 1 inside this text).")
conv1(353, "Corollaire (10.4.12) (ii), 'k(x) est un corps parfait'",
      r"$X$, $k(x)$ est un corps", r"$X$, $\boldsymbol{k}(x)$ est un corps",
      "Apply after the previous finding, whose 'old' contains this text.")
add(353, "proof (i), 'on ait X = X_0 x_{S_0} S où X_0'", "no comma before 'où'",
    "'$X=X_0\\times_{S_0}S$, où'", "punctuation", None, "high",
    r"$X=X_0\times_{S_0}S$, où", r"$X=X_0\times_{S_0}S$ où", "Crop p353s3_comma.png.")
ital(353, "proof (i), 'des préschémas excellents'", "excellents",
     r"préschémas excellents¶", r"préschémas \emph{excellents}¶")
ital(353, "proof (i), 'un préschéma universellement japonais'", "universellement japonais",
     r"préschéma universellement japonais¶", r"préschéma \emph{universellement japonais}¶")
ital(353, "proof (i), 'supposer X réduit'", "réduit",
     r"supposer $X$ réduit; en effet,", r"supposer $X$ \emph{réduit}; en effet,")
conv2(353, "proof (i), '(I, 5.1.6)'", "I", r"radiciel (I, 5.1.6)", r"radiciel (\textbf{I}, 5.1.6)")
conv2(353, "proof (i), '(II, 5.4.6)'", "II", r"de $f$ (II, 5.4.6)", r"de $f$ (\textbf{II}, 5.4.6)")
conv2(353, "proof (i), '(III, 4.4.2)'", "III", r"fini (III, 4.4.2)", r"fini (\textbf{III}, 4.4.2)")
# ---------------------------------------------------------------- page 354
conv2(354, "'le normalisé de X (II, 6.3.8)'", "II", r"de $X$ (II, 6.3.8)", r"de $X$ (\textbf{II}, 6.3.8)")
ital(354, "'Le morphisme canonique p : X' -> X est fini'", "fini",
     r"$p:X'\to X$ est fini puisque", r"$p:X'\to X$ est \emph{fini} puisque")
conv1(354, "'l'homomorphisme k(x_i) -> k(x'_i)', first k",
      r"l'homomorphisme $k(x_i)\to", r"l'homomorphisme $\boldsymbol{k}(x_i)\to")
conv1(354, "'l'homomorphisme k(x_i) -> k(x'_i)', second k",
      r"\to k(x'_i)$ étant", r"\to\boldsymbol{k}(x'_i)$ étant")
ital(354, "'psi|M est une bijection de M'", "bijection",
     r"est une¶bijection de $M$", r"est une¶\emph{bijection} de $M$")
add(354, "'f|X_i de f se factorise en X_i -f_i-> X_sigma(i) -> X (I, 5.2.2)'",
    "in the running text, at the end of the line", "displayed", "formula", None, "high",
    r"factorise en¶\[¶ X_i\xrightarrow{f_i}X_{\sigma(i)}\longrightarrow X¶\]¶",
    r"factorise en $X_i\xrightarrow{f_i}X_{\sigma(i)}\longrightarrow X$¶", "")
conv2(354, "'(I, 5.2.2), où la seconde flèche'", "I", r"(I, 5.2.2), où la seconde",
      r"(\textbf{I}, 5.2.2), où la seconde")
conv2(354, "'il existe (II, 6.3.9)'", "II", r"il existe (II, 6.3.9)", r"il existe (\textbf{II}, 6.3.9)")
add(354, "diagram after 'rendant commutatif le diagramme': arrow labels",
    "p_i to the LEFT of the left vertical arrow; f_i BELOW the bottom arrow (crop p354s2_diag.png)",
    "'\\downarrow p_i' (label to the right) and \\xrightarrow{f_i} (label above)",
    "other", None, "high",
    r"\downarrow p_i&&\downarrow p_{\sigma(i)}\\¶X_i&\xrightarrow{f_i}&X_{\sigma(i)}",
    r"\llap{$p_i$\,}\downarrow&&\downarrow p_{\sigma(i)}\\¶X_i&\xrightarrow[f_i]{}&X_{\sigma(i)}",
    "Label sides as printed (cf. GLOBAL_ISSUES 30); \\llap keeps the arrow centred in its column.")
add(354, "'et si f' coïncide avec f_i dans chacun des X'_i'",
    "f_i without the prime (crop p354s2_fi_zoom.png)", "$f'_i$ (silently corrected)",
    "misprint_in_print", None, "high",
    r"coïncide avec $f'_i$ dans", r"coïncide avec $f_i$ dans",
    "Misprint: f' coincides with the f'_i of the diagram on the X'_i. The TeX silently corrects it; the "
    "diplomatic text restores the printed f_i.", corrected=r"f'_i")
add(354, "diagram (10.4.12.1): arrow labels",
    "p to the LEFT of the left vertical arrow; f BELOW the bottom arrow (crop p354s3_diag.png)",
    "'\\downarrow p' (label to the right) and \\xrightarrow{f} (label above)",
    "other", None, "high",
    r"\downarrow p&&\downarrow p\\¶X&\xrightarrow{f}&X",
    r"\llap{$p$\,}\downarrow&&\downarrow p\\¶X&\xrightarrow[f]{}&X",
    "Label sides as printed (cf. GLOBAL_ISSUES 30). Independent of the next finding.")
add(354, "diagram (10.4.12.1): end", "no full stop after the last X", "'X.'",
    "punctuation", None, "high", r"X.¶\end{array}¶\tag{10.4.12.1}", r"X¶\end{array}¶\tag{10.4.12.1}", "")
ital(354, "'donc f' est séparé (I, 5.5.1)'", "séparé",
     r"donc $f'$ est séparé", r"donc $f'$ est \emph{séparé}", "The earlier 'comme f est séparé' is roman.")
conv2(354, "'(I, 5.5.1)'", "I", r"(I, 5.5.1)", r"(\textbf{I}, 5.5.1)")
ital(354, "'que f' est quasi-fini'", "quasi-fini",
     r"$f'$ est¶quasi-fini. Puisque", r"$f'$ est¶\emph{quasi-fini}. Puisque")
add(354, "display 'X'_i -f_i-> X''_sigma(i) -u_sigma(i)-> X'_sigma(i)': first arrow label",
    "label f_i with no primes (crop p354s3_label_zoom.png; the f'_i label of the first diagram shows its "
    "prime clearly)", "\\xrightarrow{f''_i} (silently corrected)", "misprint_in_print", None, "high",
    r"X'_i\xrightarrow{f''_i}X''_{\sigma(i)}", r"X'_i\xrightarrow{f_i}X''_{\sigma(i)}",
    "Misprint: the text after the display names this map f''_i ('et f''_i une immersion ouverte'). The TeX "
    "silently corrects it; the diplomatic text restores the printed f_i.", corrected=r"f''_i")
add(354, "display 'X'_i -> X''_sigma(i) -> X'_sigma(i)': end", "no comma after the display",
    "'X'_{\\sigma(i)},'", "punctuation", None, "high",
    r"X'_{\sigma(i)},¶\]", r"X'_{\sigma(i)}¶\]", "")
conv1(354, "'relative à l'extension k(x'_i)'", r"l'extension $k(x'_i)$ de",
      r"l'extension $\boldsymbol{k}(x'_i)$ de")
conv1(354, "'de k(x'_sigma(i)), et f''_i'", r"$k(x'_{\sigma(i)})$, et $f''_i$",
      r"$\boldsymbol{k}(x'_{\sigma(i)})$, et $f''_i$")
conv1(354, "'Mais comme k(x'_i) est une extension radicielle'", r"comme¶$k(x'_i)$ est une",
      r"comme¶$\boldsymbol{k}(x'_i)$ est une")
conv1(354, "'extension radicielle de k(x'_sigma(i))'", r"radicielle de $k(x'_{\sigma(i)})$,",
      r"radicielle de $\boldsymbol{k}(x'_{\sigma(i)})$,")
ital(354, "'u_sigma(i) est un morphisme radiciel'", "radiciel",
     r"morphisme radiciel (Bourbaki,", r"morphisme \emph{radiciel} (Bourbaki,")
ital(354, "'que f' est surjectif'", "surjectif",
     r"$f'$ est¶surjectif;", r"$f'$ est¶\emph{surjectif};")
ital(354, "'que f''_i est bijectif'", "bijectif",
     r"$f''_i$ est bijectif, donc", r"$f''_i$ est \emph{bijectif}, donc")
ital(354, "'le morphisme f' est fini (puisqu'il'", "fini",
     r"le morphisme $f'$ est fini (puisqu'il", r"le morphisme $f'$ est \emph{fini} (puisqu'il")
conv2(354, "'f est propre (II, 5.4.3)'", "II", r"propre (II, 5.4.3)", r"propre (\textbf{II}, 5.4.3)")

# ---------------------------------------------------------------- checks
src = open(SRC, encoding="utf-8", newline="").read()
assert "\r" not in src
pages = {n: open("%s/page_%d.tex" % (RUN, n), encoding="utf-8", newline="").read().replace("\r", "")
         for n in range(349, 355)}
work = src
problems = []
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    old, new = fx["old"], fx["new"]
    c_work = work.count(old)
    c_src = src.count(old)
    c_page = pages[d["_seg"]].count(old)
    tag = "%3d p%d %-12s src=%d page_%d=%d now=%d" % (i, d["page"], d["kind"], c_src, d["_seg"], c_page, c_work)
    if c_work != 1:
        problems.append(tag + "  OLD=" + repr(old[:60]))
    print(tag, repr(old[:50]))
    if c_work == 1:
        work = work.replace(old, new, 1)

print("findings:", len(F))
print("problems:", len(problems))
for p in problems:
    print("  ", p)

# counts per page
from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for pg in range(350, 355):
    print(pg, cnt[(pg, "normal")], cnt[(pg, "convention")], cnt[(pg, "misprint")])

if "--write" in sys.argv and not problems:
    out = []
    for d in F:
        e = dict(d)
        del e["_seg"]
        out.append(e)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
    # keep the simulated result for a compile test (not a release file)
    with open(RUN + "/crops_350_354/simulated_errata_after_fixes.tex", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(work)
