# Builds findings_145_149.json. Raw strings; "<NL>" stands for a line break in old/new.
import json, sys

OUT = r"user\Documents\ega_scan_check_20261101\run_II\findings_145_149.json"

C2 = "Bold chapter number in the print, plain in the TeX."
C1 = "Bold italic k in the print, plain k in the TeX."

F = []

def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old.replace("<NL>", "\n"),
                                          "new": new.replace("<NL>", "\n")}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 145 ----------------
p = 145
add(p, "Théorème (7.3.8) c): 'où A est un anneau de valuation (resp. un anneau de valuation discrète)'",
    "'(resp.' roman inside the italic statement; 'un anneau de valuation discrète)' italic",
    "(resp. in the italic theorem environment", "convention", 6, "high",
    r"(resp. un anneau", r"\textup{(resp.} un anneau", "Checked on a crop.")
add(p, "Théorème (7.3.8) c): 'l'application canonique (7.3.2.2) relative au Y'-préschéma'",
    "(7.3.2.2) roman inside the italic statement", "italic (theorem environment)", "convention", 6, "high",
    r"(\hyperref[II.7.3.2.2-fr]{7.3.2.2})", r"\textup{(\hyperref[II.7.3.2.2-fr]{7.3.2.2})}", "Checked on a crop.")
add(p, "Théorème (7.3.8) c): 'est surjective (resp. bijective).'",
    "'(resp.' roman inside the italic statement; 'bijective)' italic",
    "(resp. in the italic theorem environment", "convention", 6, "high",
    r"(resp. bijective)", r"\textup{(resp.} bijective)", "Checked on a crop.")
add(p, "after (7.3.8): 'résulte aussitôt de (I, 3.3.14)'", "(𝐈, 3.3.14)", "plain I in the link text",
    "convention", 2, "high", r"{I, 3.3.14}", r"{\textbf{I}, 3.3.14}", C2)
add(p, "after (7.3.8): 'L'équivalence de b) et c) résulte'", "b) and c) italic", "upright b) c)",
    "italics", None, "high", r"L'équivalence de b) et c) résulte",
    r"L'équivalence de \emph{b)} et \emph{c)} résulte", "")
add(p, "after (7.3.8): 'a) implique c), car a) entraîne'", "a), c), a) italic", "upright",
    "italics", None, "high", r"~; a) implique c), car a) entraîne",
    r"~; \emph{a)} implique \emph{c)}, car \emph{a)} entraîne", "")
add(p, "after (7.3.8): 'que f_(Y') est séparé (I, 5.5.1, (iv)) et fermé'", "(𝐈, 5.5.1, (iv))",
    "plain I in the link text", "convention", 2, "high",
    r"{I, 5.5.1, (iv)}) et fermé", r"{\textbf{I}, 5.5.1, (iv)}) et fermé", C2)
add(p, "after (7.3.8): 'Reste à prouver que b) entraîne a).'", "b) and a) italic", "upright",
    "italics", None, "high", r"Reste à prouver que b) entraîne a).",
    r"Reste à prouver que \emph{b)} entraîne \emph{a)}.", "")
add(p, "after (7.3.8): 'Si la condition b) est vérifiée par f'", "b) italic", "upright",
    "italics", None, "high", r"Si la condition b) est vérifiée",
    r"Si la condition \emph{b)} est vérifiée", "")
add(p, "after (7.3.8): 'en vertu de l'équivalence de b) et c), et du fait que'", "b) and c) italic", "upright",
    "italics", None, "high", r"l'équivalence de b) et c), et du fait",
    r"l'équivalence de \emph{b)} et \emph{c)}, et du fait", "")
add(p, "after (7.3.8): 'pour tout morphisme Y'→Y'' (I, 3.3.9.1)'", "(𝐈, 3.3.9.1)", "plain I in the link text",
    "convention", 2, "high", r"{I, 3.3.9.1}", r"{\textbf{I}, 3.3.9.1}", C2)
add(p, "after (7.3.8): 'quand f l'est (I, 5.5.1, (iv) et 6.6.4, (iii))'", "(𝐈, 5.5.1, (iv) et 6.6.4, (iii))",
    "plain I in the link text", "convention", 2, "high",
    r"{I, 5.5.1, (iv)} et", r"{\textbf{I}, 5.5.1, (iv)} et", C2)
add(p, "after (7.3.8): 'on est ramené à prouver que b) entraîne que f est fermé'", "b) italic", "upright",
    "italics", None, "high", r"ramené à prouver que b) entraîne",
    r"ramené à prouver que \emph{b)} entraîne", "")
add(p, "after (7.3.8): 'il suffit de vérifier la condition b) de (7.2.1)'", "b) italic", "upright",
    "italics", None, "high", r"vérifier la condition b) de",
    r"vérifier la condition \emph{b)} de", "")
add(p, "after (7.3.8): 'et qu'il existe un k(y)-homomorphisme'", "bold italic k", "k(y)",
    "convention", 1, "high", r"un $k(y)$", r"un $\boldsymbol{k}(y)$", C1)
add(p, "after (7.3.8): 'k(x)→k(b)', first k", "bold italic k", "k(x)",
    "convention", 1, "high", r"homomorphisme $k(x)", r"homomorphisme $\boldsymbol{k}(x)", C1)
add(p, "after (7.3.8): 'k(x)→k(b)', second k", "bold italic k", "k(b)",
    "convention", 1, "high", r"k(b)$. Ce dernier", r"\boldsymbol{k}(b)$. Ce dernier", C1)
add(p, "after (7.3.8): 'à un Y-morphisme Spec(k(b))→X'", "bold italic k", "k(b)",
    "convention", 1, "high", r"\operatorname{Spec}(k(b))", r"\operatorname{Spec}(\boldsymbol{k}(b))", C1)
add(p, "after (7.3.8): 'Spec(k(b))→X (I, 2.4.6)'", "(𝐈, 2.4.6)", "plain I in the link text",
    "convention", 2, "high", r"{I, 2.4.6}", r"{\textbf{I}, 2.4.6}", C2)
add(p, "after (7.3.8): 'il résulte donc de b) qu'il existe un Y-morphisme'", "b) italic", "upright",
    "italics", None, "high", r"il résulte donc de b) qu'il",
    r"il résulte donc de \emph{b)} qu'il", "")
add(p, "after (7.3.8), second case: 'l'hypothèse b) entraîne d'abord que f est séparé'", "b) italic", "upright",
    "italics", None, "high", r"l'hypothèse<NL>b) entraîne d'abord",
    r"l'hypothèse<NL>\emph{b)} entraîne d'abord", "")
add(p, "Remarques (7.3.9), (i): 'il suffit que la condition b) ou la condition c) soit vérifiée'",
    "b) and c) italic", "upright (judged with the remark body roman)",
    "italics", None, "high", r"condition b) ou la condition c) soit",
    r"condition \emph{b)} ou la condition \emph{c)} soit", "")
add(p, "Remarques (7.3.9), (ii): 'On déduit du critère c) de (7.3.8)'", "c) italic",
    "upright (judged with the remark body roman)", "italics", None, "high",
    r"On déduit du critère c) de", r"On déduit du critère \emph{c)} de", "")
add(p, "Remarques (7.3.9), (ii): 'et le critère c) de (7.3.8), joint à (4.1.3.1)'", "c) italic",
    "upright (judged with the remark body roman)", "italics", None, "high",
    r"et le critère c) de", r"et le critère \emph{c)} de", "")
add(p, "Remarques (7.3.9), (ii): 'tout point de P^n_Y à valeurs dans K provient (par restriction au point générique de Y) d'un point de P^n_Y'",
    "'(par restriction au point générique de Y)' roman between the italic 'provient' and 'd'un point de'",
    "the parenthesis inside \\emph{...} (italic)", "italics", None, "high",
    r"provient (par restriction au point générique de $Y$) d'un point de",
    r"provient} (par restriction au point générique de $Y$) \emph{d'un point de",
    "Checked on a crop. Splits the \\emph; braces stay balanced (the \\emph opened at 'si $Y$' now closes after 'provient', the new one closes at the existing '}' after '$A$').")
add(p, "Remarques (7.3.9), (ii): 'tout O_Y-Module inversible est trivial (I, 2.4.8)'", "(𝐈, 2.4.8)",
    "plain I in the link text", "convention", 2, "high", r"{I, 2.4.8}", r"{\textbf{I}, 2.4.8}", C2)
add(p, "Remarques (7.3.9), (ii), last lines: 'où ζ≠0 et les c sont des éléments non tous nuls de K'",
    "'les c' without subscript (the c ends the line; no i below it)", "les $c_i$",
    "misprint_in_print", None, "high", r"les $c_i$ sont des", r"les $c$ sont des",
    "Checked on a 6x crop: no subscript after the line-final c, while the neighbouring c_0, c_1, c_n show theirs. The TeX silently corrects to c_i; the diplomatic text restores the printed c.",
    corrected=r"les $c_i$ sont des")

# ---------------- page 146 ----------------
p = 146
add(p, "Corollaire (7.3.10): 'Soient Y un schéma intègre (resp. un schéma intègre localement noethérien)'",
    "'(resp.' roman inside the italic statement; the closing parenthesis italic",
    "(resp. in the italic corollary environment", "convention", 6, "high",
    r"(resp. un schéma", r"\textup{(resp.} un schéma", "Checked on a crop.")
add(p, "Corollaire (7.3.10), (ii): 'la propriété énoncée dans (i) soit vérifiée'",
    "(i) roman inside the italic statement", "italic", "convention", 6, "high",
    r"énoncée dans (i) soit", r"énoncée dans \textup{(i)} soit", "Checked on a crop.")
add(p, "Corollaire (7.3.10), (ii): 'tout anneau de valuation (resp. tout anneau de valuation discrète)'",
    "'(resp.' roman inside the italic statement; 'discrète)' italic", "(resp. italic",
    "convention", 6, "high", r"valuation (resp.<NL>tout anneau", r"valuation \textup{(resp.}<NL>tout anneau",
    "Checked on a crop.")
add(p, "proof of (7.3.10): 'que f est séparé (I, 5.5.9)'", "(𝐈, 5.5.9)", "plain I in the link text",
    "convention", 2, "high", r"{I, 5.5.9}", r"{\textbf{I}, 5.5.9}", C2)
add(p, "proof of (7.3.10), (i): 'dans Y (I, 2.4.4) tel que h(a)=y'", "(𝐈, 2.4.4)", "plain I in the link text",
    "convention", 2, "high", r"{I, 2.4.4}", r"{\textbf{I}, 2.4.4}", C2)
add(p, "proof of (7.3.10), (i): 'on a k(ξ)=k(b)=L', first k", "bold italic k", "k(\\xi)",
    "convention", 1, "high", r"$k(\xi)", r"$\boldsymbol{k}(\xi)", C1)
add(p, "proof of (7.3.10), (i): 'on a k(ξ)=k(b)=L', second k", "bold italic k", "k(b)",
    "convention", 1, "high", r"k(b)=L", r"\boldsymbol{k}(b)=L", C1)
add(p, "proof of (7.3.10), (ii): 'comme espace sous-jacent (I, 5.2.1)'", "(𝐈, 5.2.1)", "plain I in the link text",
    "convention", 2, "high", r"{I, 5.2.1}", r"{\textbf{I}, 5.2.1}", C2)
add(p, "proof of (7.3.10), (ii): 'une immersion ouverte dominante (I, 5.2.3)'", "(𝐈, 5.2.3)",
    "plain I in the link text", "convention", 2, "high", r"{I, 5.2.3}", r"{\textbf{I}, 5.2.3}", C2)
add(p, "page break 146/147 (last line of p. 146): 'et Z est intègre; en outre Z est projectif sur Y'",
    "one sentence running over the page break", "blank line before \\oldpage[II]{147} (paragraph break)",
    "other", None, "high", r"et $Z$ est<NL>intègre~;<NL><NL>", r"et $Z$ est<NL>intègre~;<NL>",
    "Spurious paragraph break at the page boundary (GLOBAL_ISSUES item 20). The 'old' is the end of page 146's segment; it occurs once in page_146.tex and once in ega2-1-fr.tex.")

# ---------------- page 147 ----------------
p = 147
add(p, "proof of (7.3.10), (ii): 'et j dominant et birationnel'",
    "'dominant' and 'birationnel' italic, 'et' between them roman", "\\emph{dominant et birationnel} ('et' italic)",
    "italics", None, "high", r"\emph{dominant et birationnel}", r"\emph{dominant} et \emph{birationnel}",
    "Checked on a crop.")
add(p, "proof of (7.3.10), (ii): 'sont apparentés (I, 8.1.4), et comme P est un schéma'",
    "'et comme' (no comma after et)", "'et, comme'", "punctuation", None, "high",
    r"), et, comme $P$", r"), et comme $P$", "Checked on a crop.")
add(p, "proof of (7.3.10), (ii): 'sont apparentés (I, 8.1.4)'", "(𝐈, 8.1.4)", "plain I in the link text",
    "convention", 2, "high", r"{I, 8.1.4}", r"{\textbf{I}, 8.1.4}", C2)
add(p, "proof of (7.3.10), (ii): 'cela entraîne z=j(x') (I, 8.2.2)'", "(𝐈, 8.2.2)", "plain I in the link text",
    "convention", 2, "high", r"{I, 8.2.2}", r"{\textbf{I}, 8.2.2}", C2)
add(p, "proof of (7.3.11): 'En effet (I, 8.2.1.1)'", "(𝐈, 8.2.1.1)", "plain I in the link text",
    "convention", 2, "high", r"{I, 8.2.1.1}", r"{\textbf{I}, 8.2.1.1}", C2)
add(p, "Remarques (7.3.12), first sentence: 'sur l'anneau B=Γ(Y, O_X)'",
    "B=Γ(Y, 𝒪_X) (subscript X)", "B=\\Gamma(Y,\\mathcal{O}_Y)", "misprint_in_print", None, "high",
    r"$B=\Gamma(Y,\mathcal{O}_Y)$", r"$B=\Gamma(Y,\mathcal{O}_X)$",
    "Checked on a 3x crop: the subscript is X. B is the ring of the affine Y, so O_Y is meant; the TeX silently corrects.",
    corrected=r"$B=\Gamma(Y,\mathcal{O}_Y)$")
add(p, "Remarques (7.3.12), second paragraph: 'et (I, 6.4.4, c))'", "(𝐈, 6.4.4, c))", "plain I in the link text",
    "convention", 2, "high", r"{I, 6.4.4", r"{\textbf{I}, 6.4.4",
    C2 + " Independent of the italic-c) finding at the same reference (either order works).")
add(p, "Remarques (7.3.12), second paragraph: '(I, 6.4.4, c))'", "c) italic",
    "upright in the link text (judged with the remark body roman)", "italics", None, "high",
    r"6.4.4, c)}", r"6.4.4, \emph{c)}}", "Independent of the bold-I finding at the same reference (either order works).")
add(p, "Remarques (7.3.12), third paragraph: 'cohérent F (III, 4.4.2)'", "(𝐈𝐈𝐈, 4.4.2)",
    "plain III in the link text", "convention", 2, "high", r"{III, 4.4.2}", r"{\textbf{III}, 4.4.2}", C2)

# ---------------- page 148 ----------------
p = 148
add(p, "Proposition (7.4.1): 'et soit K_i=k(x_i) (1≤i≤n)'", "bold italic k", "k(x_i)",
    "convention", 1, "high", r"$K_i=k(x_i)$", r"$K_i=\boldsymbol{k}(x_i)$", C1)
add(p, "Proposition (7.4.1), b): 'l'anneau local O_x est de dimension 1 (7.1.5)'",
    "(7.1.5) roman inside the italic statement", "italic (proposition environment)", "convention", 6, "high",
    r"(\hyperref[II.7.1.5-fr]{7.1.5})", r"\textup{(\hyperref[II.7.1.5-fr]{7.1.5})}", "Checked on a crop.")
add(p, "proof of (7.4.1): 'contient un point fermé (0, 2.1.3)'", "(𝟎, 2.1.3)", "plain 0 in the link text",
    "convention", 2, "high", r"{0, 2.1.3}", r"{\textbf{0}, 2.1.3}", C2)
add(p, "proof of (7.4.1): 'En vertu de (I, 2.4.2)'", "(𝐈, 2.4.2)", "plain I in the link text",
    "convention", 2, "high", r"{I, 2.4.2}", r"{\textbf{I}, 2.4.2}", C2)
add(p, "proof of (7.4.1): 'contenant x (I, 1.1.14)'", "(𝐈, 1.1.14)", "plain I in the link text",
    "convention", 2, "high", r"{I, 1.1.14}", r"{\textbf{I}, 1.1.14}", C2)
add(p, "proof of (7.4.1): 'l'équivalence de b) et c) en découle aussitôt'", "b) and c) italic", "upright",
    "italics", None, "high", r"l'équivalence de b) et c)", r"l'équivalence de \emph{b)} et \emph{c)}", "")
add(p, "proof of (7.4.1): 'or, la condition a) implique que ces dimensions sont égales à 1, donc a) implique b)'",
    "a), a), b) italic", "upright", "italics", None, "high",
    r"la condition a) implique que ces<NL>dimensions sont égales à 1, donc a) implique b)~;",
    r"la condition \emph{a)} implique que ces<NL>dimensions sont égales à 1, donc \emph{a)} implique \emph{b)}~;", "")
add(p, "proof of (7.4.1): 'ce qui montre que b) entraîne a).'", "b) and a) italic", "upright",
    "italics", None, "high", r"montre que b)<NL>entraîne a).", r"montre que \emph{b)}<NL>entraîne \emph{a)}.", "")
add(p, "after (7.4.1): 'l'ensemble X est vide ou infini'", "'vide' and 'infini' italic, 'ou' roman",
    "\\emph{vide ou infini} ('ou' italic)", "italics", None, "high",
    r"\emph{vide ou infini}", r"\emph{vide} ou \emph{infini}", "Checked on a crop.")
add(p, "after (7.4.1): 'comme il résulte aussitôt de (I, 6.4.4)'", "(𝐈, 6.4.4)", "plain I in the link text",
    "convention", 2, "high", r"{I, 6.4.4}", r"{\textbf{I}, 6.4.4}", C2)
add(p, "Définition (7.4.2): 'On appelle courbe algébrique sur k'",
    "the defined term 'courbe algébrique' roman inside the italic definition", "italic (definition environment)",
    "convention", 6, "high", r"On appelle courbe algébrique sur", r"On appelle \textup{courbe algébrique} sur",
    "Checked on a crop.")
add(p, "Définition (7.4.2): 'un schéma algébrique non vide sur k'",
    "'schéma' roman; 'algébrique non vide' italic", "italic (definition environment)",
    "convention", 6, "high", r"un schéma algébrique non vide sur", r"un \textup{schéma} algébrique non vide sur",
    "Checked on a crop: only 'schéma' is upright.")
add(p, "Définition (7.4.2): 'vérifiant les conditions de (7.4.1)'",
    "(7.4.1) roman inside the italic definition", "italic (definition environment)", "convention", 6, "high",
    r"vérifiant les conditions de (\hyperref[II.7.4.1-fr]{7.4.1})",
    r"vérifiant les conditions de \textup{(\hyperref[II.7.4.1-fr]{7.4.1})}", "Checked on a crop.")
add(p, "page break 148/149 (last line of p. 148): 'ne peut contenir le point générique de X'",
    "one sentence running over the page break", "blank line before \\oldpage[II]{149} (paragraph break)",
    "other", None, "high", r"ne peut contenir<NL><NL>", r"ne peut contenir<NL>",
    "Spurious paragraph break at the page boundary (GLOBAL_ISSUES item 20). The 'old' is the end of page 148's segment; it occurs once in page_148.tex and once in ega2-1-fr.tex.")

# ---------------- page 149 ----------------
p = 149
add(p, "proof of (7.4.3): 'pour espace sous-jacent (I, 5.2.1)'", "(𝐈, 5.2.1)", "plain I in the link text",
    "convention", 2, "high", r"{I, 5.2.1}", r"{\textbf{I}, 5.2.1}", C2)
add(p, "proof of (7.4.3): 'il résulte donc de (I, 6.2.2)'", "(𝐈, 6.2.2)", "plain I in the link text",
    "convention", 2, "high", r"{I, 6.2.2}", r"{\textbf{I}, 6.2.2}", C2)
add(p, "proof of (7.4.4): 'de type fini sur k(η)'", "bold italic k", "k(\\eta)",
    "convention", 1, "high", r"sur $k(\eta)$, et de point", r"sur $\boldsymbol{k}(\eta)$, et de point", C1)
add(p, "proof of (7.4.4): '(I, 6.3.9 et 6.4.11)'", "(𝐈, 6.3.9 et 6.4.11)", "plain I in the link text",
    "convention", 2, "high", r"{I, 6.3.9}", r"{\textbf{I}, 6.3.9}", C2)
add(p, "proof of (7.4.4): 'Comme k(ξ) et k(η)', first k", "bold italic k", "k(\\xi)",
    "convention", 1, "high", r"Comme $k(\xi)$", r"Comme $\boldsymbol{k}(\xi)$", C1)
add(p, "proof of (7.4.4): 'Comme k(ξ) et k(η)', second k", "bold italic k", "k(\\eta)",
    "convention", 1, "high", r"et $k(\eta)$ sont des", r"et $\boldsymbol{k}(\eta)$ sont des", C1)
add(p, "proof of (7.4.4): 'de même degré de transcendance 1, k(ξ) est nécessairement'", "bold italic k", "k(\\xi)",
    "convention", 1, "high", r"1, $k(\xi)$ est", r"1, $\boldsymbol{k}(\xi)$ est", C1)
add(p, "proof of (7.4.4): 'une extension de degré fini de k(η)'", "bold italic k", "k(\\eta)",
    "convention", 1, "high", r"de degré fini de $k(\eta)$", r"de degré fini de $\boldsymbol{k}(\eta)$", C1)
add(p, "proof of (7.4.4): 'ξ est fermé dans f^{-1}(η) (I, 6.4.2)'", "(𝐈, 6.4.2)", "plain I in the link text",
    "convention", 2, "high", r"{I, 6.4.2}", r"{\textbf{I}, 6.4.2}", C2)
add(p, "proof of (7.4.5): 'Cela résulte aussitôt de la condition b) de (7.4.1)'", "b) italic", "upright",
    "italics", None, "high", r"la condition b) de", r"la condition \emph{b)} de", "Checked on a crop.")
add(p, "Corollaire (7.4.6): 'de X relativement à A (6.3.4) est une courbe algébrique normale'",
    "(6.3.4) roman inside the italic statement", "italic (corollary environment)", "convention", 6, "high",
    r"(\hyperref[II.6.3.4-fr]{6.3.4})", r"\textup{(\hyperref[II.6.3.4-fr]{6.3.4})}", "Checked on a crop.")
add(p, "proof of (7.4.6): 'chacun des k(x'_j) est extension algébrique finie'", "bold italic k", "k(x'_j)",
    "convention", 1, "high", r"chacun des $k(x'_j)$", r"chacun des $\boldsymbol{k}(x'_j)$", C1)
add(p, "proof of (7.4.6): 'de l'un des k(x_i) (6.3.6)'", "bold italic k", "k(x_i)",
    "convention", 1, "high", r"l'un des $k(x_i)$", r"l'un des $\boldsymbol{k}(x_i)$", C1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print(len(F), "findings written")
