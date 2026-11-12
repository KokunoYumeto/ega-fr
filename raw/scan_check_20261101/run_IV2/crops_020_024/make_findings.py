# Build findings_020_024.json for EGA IV-2 pp. 20-24 and check every edit against page_NNN.tex.
# In the strings below the pilcrow stands for a line break (LF), so that raw strings can hold TeX.
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_020_024.json"
NL = "\u00b6"


def nl(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    x = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        x["corrected"] = nl(corrected)
    x["note"] = note
    F.append(x)


def c2(page, where, old, new, note=None, scan=None, tex=None):
    add(page, where, scan or "bold chapter numeral in the reference", tex or "plain numeral", "convention", 2, "high",
        old, new, note)


# ---------------------------------------------------------------- page 20
c2(20, "proof of (2.4.3), (vi): 'D'autre part (I, 5.1.8), pour tout morphisme'",
   r"(I, 5.1.8), pour", r"(\textbf{I}, 5.1.8), pour")
add(20, "proof of (2.4.3), (vi): 'on a (X_red ×_{Y_red} Y_red)_red = (X ×_Y Y')_red, donc la remarque'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶\bigl(X_{\mathrm{red}}\times_{Y_{\mathrm{red}}}Y'_{\mathrm{red}}\bigr)_{\mathrm{red}}¶=(X\times_Y Y')_{\mathrm{red}},¶\]",
    r"$\bigl(X_{\mathrm{red}}\times_{Y_{\mathrm{red}}}Y'_{\mathrm{red}}\bigr)_{\mathrm{red}}¶=(X\times_Y Y')_{\mathrm{red}}$,",
    "Display vs inline; the formula's misprint is the next entry. Apply this edit first (its old string contains the primed Y).")
add(20, "same formula, third factor (line 12 of the page)",
    "(X_red ×_{Y_red} Y_red)_red: third factor Y_red WITHOUT a prime",
    "silently corrected to Y'_{\\mathrm{red}}", "misprint_in_print", None, "high",
    r"Y'_{\mathrm{red}}\bigr)", r"Y_{\mathrm{red}}\bigr)",
    "Authors' errata, EGA IV liste 3, (IV, 2.4.3): 'Ligne 12 de la p. 20, remplacer (X_red×_{Y_red}Y_red)_red par "
    "(X_red×_{Y_red}Y'_red)_red'. The fix restores the printed reading and changes only the prime; its old string is "
    "the same before and after the inline edit above. (The r of 'red' under the × is a wrong-fount bold r, same letter; "
    "not reproduced.)",
    corrected=r"(X_{\mathrm{red}}\times_{Y_{\mathrm{red}}}Y'_{\mathrm{red}})_{\mathrm{red}}")
add(20, "proof of (2.4.3), (vi): '(X_red ×_{Y_red} Y'')_red = (X ×_Y Y'')_red (I, 5.1.8).'",
    "formula and reference set inline in the running text", "displayed with \\[ ... \\quad\\text{(I, 5.1.8).} \\]",
    "other", None, "high",
    r"\[¶\bigl(X_{\mathrm{red}}\times_{Y_{\mathrm{red}}}Y''\bigr)_{\mathrm{red}}¶=(X\times_Y Y'')_{\mathrm{red}}¶\quad\text{(I, 5.1.8).}¶\]",
    r"$\bigl(X_{\mathrm{red}}\times_{Y_{\mathrm{red}}}Y''\bigr)_{\mathrm{red}}¶=(X\times_Y Y'')_{\mathrm{red}}$¶(I, 5.1.8).",
    "Display vs inline. Apply before the convention-2 edit of '(I, 5.1.8).' (next entry). The blank line before 'Enfin' "
    "stays (new paragraph in the print).")
c2(20, "same sentence: '(I, 5.1.8).'", r"(I, 5.1.8).", r"(\textbf{I}, 5.1.8).",
   "Old string matches once before and after the inline edit above.")
add(20, "proof of (2.4.3), (vii), last sentence: 'On peut donc se borner à prouver que f est ouvert'",
    "f (no prime)", "$f'$", "symbol", None, "high",
    r"prouver que $f'$ est", r"prouver que $f$ est",
    "The print reduces to the morphism f itself (f and Y in both places of the sentence).")
add(20, "same sentence: 'resp. un homéomorphisme sur Y), ce qui est immédiat'",
    "Y (no prime)", "$Y'$", "symbol", None, "high",
    r"homéomorphisme sur $Y'$)", r"homéomorphisme sur $Y$)")
add(20, "Proposition (2.4.4): '(donc séparé (1.7.7.1))'",
    "(1.7.7.1): four old-style figures with points (the first 1 has the same x-height glyph as the last; no comma); "
    "set upright inside the italic statement",
    "(I, 7.7.1): the first figure read as the chapter numeral I, comma added", "number", None, "high",
    r"(I, 7.7.1)", r"\textup{(1.7.7.1)}",
    "Restores the printed reference; the \\textup is the convention-6 entry below. The printed reference is itself a "
    "misprint (entry after next).")
add(20, "Proposition (2.4.4): reference '(1.7.7.1)'", "reference upright inside the italic statement",
    "italic (proposition environment)", "convention", 6, "high", None, None,
    "Included in the previous edit (\\textup).")
add(20, "Proposition (2.4.4): '(donc séparé (1.7.7.1))'", "(1.7.7.1)",
    "(I, 7.7.1), a misreading; after the number fix above the TeX keeps the printed reading",
    "misprint_in_print", None, "high", None, None,
    "IV (1.7.7) has no (1.7.7.1) (it concerns (I, 9.4.7)); 'tout morphisme radiciel est séparé' is Lemme (1.8.7.1) "
    "(IV-1, p. 241), and errata liste 3 cites (1.8.7.1) for the same fact.",
    corrected="(1.8.7.1)")
c2(20, "proof of (2.4.4): 'universellement injectif par hypothèse (I, 3.5.11)'",
   r"hypothèse (I, 3.5.11)", r"hypothèse (\textbf{I}, 3.5.11)")
add(20, "Proposition (2.4.5), label (i)", "label (i) upright", "\\item[(i)] inside the italic statement (italic)",
    "convention", 6, "high", r"\item[(i)] Un morphisme", r"\item[\textup{(i)}] Un morphisme",
    "GLOBAL_ISSUES 16.")
add(20, "Proposition (2.4.5), label (ii)", "label (ii) upright", "\\item[(ii)] inside the italic statement (italic)",
    "convention", 6, "high", r"\item[(ii)] Inversement", r"\item[\textup{(ii)}] Inversement",
    "GLOBAL_ISSUES 16.")
c2(20, "proof of (2.4.5) (i): '(I, 3.5.2, I, 3.5.7 et II, 6.1.5)', first I", r"(I, 3.5.2,", r"(\textbf{I}, 3.5.2,")
c2(20, "same reference, second I ('I, 3.5.7')", r" I, 3.5.7 et", r" \textbf{I}, 3.5.7 et")
c2(20, "same reference, 'II, 6.1.5'", r"et II, 6.1.5)", r"et \textbf{II}, 6.1.5)")
c2(20, "proof of (2.4.5) (i): '(II, 6.1.10)'", r"(II, 6.1.10)", r"(\textbf{II}, 6.1.10)")
c2(20, "proof of (2.4.5) (ii): '(II, 5.4.1)'", r"(II, 5.4.1)", r"(\textbf{II}, 5.4.1)")
c2(20, "proof of (2.4.5) (ii): '(III, 4.4.2)'", r"(III, 4.4.2)", r"(\textbf{III}, 4.4.2)")
c2(20, "proof of (2.4.5) (ii): 'universellement injectif (I, 3.5.11)'",
   r"injectif (I, 3.5.11)", r"injectif (\textbf{I}, 3.5.11)")
add(20, "Théorème (2.4.6): 'un morphisme quasi-plat (2.3.3) et localement'", "reference upright inside the italic statement",
    "italic (theorem environment)", "convention", 6, "high",
    r"morphisme quasi-plat (2.3.3)", r"morphisme quasi-plat \textup{(2.3.3)}")

# ---------------------------------------------------------------- page 21
add(21, "l. 1 (end of the proof of (2.4.6)): 'morphisme ouvert. Mais cela résulte'", "'ouvert' italic", "upright",
    "italics", None, "high", r"morphisme ouvert. Mais", r"morphisme \emph{ouvert}. Mais")
add(21, "Corollaire (2.4.7): '(où'", "'(où' upright inside the italic statement", "italic (corollary environment)",
    "convention", 6, "high", r"(où", r"\textup{(où}")
add(21, "Corollaire (2.4.7): 'V^n_Y = Y ⊗_Z Spec(Z[T_1, ..., T_n]), aussi noté'", "formula set inline in the running text",
    "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶\mathbf V_Y^n¶=Y\otimes_{\mathbf Z}\operatorname{Spec}¶  \bigl(\mathbf Z[T_1,\ldots,T_n]\bigr),¶\]",
    r"$\mathbf V_Y^n¶=Y\otimes_{\mathbf Z}\operatorname{Spec}¶  \bigl(\mathbf Z[T_1,\ldots,T_n]\bigr)$,",
    "Display vs inline; the formula itself matches.")
add(21, "Corollaire (2.4.7): 'aussi noté Y[T_1, ..., T_n])'", "'aussi noté' and the closing parenthesis upright",
    "italic (corollary environment)", "convention", 6, "high",
    r"aussi noté $Y[T_1,\ldots,T_n]$)", r"\textup{aussi noté $Y[T_1,\ldots,T_n]$)}")
add(21, "heading of (2.4.8)", "Remarques (2.4.8). — (plural)", "\\begin{remark} prints 'Remarque (2.4.8)'",
    "word", None, "high", r"\begin{remark}[2.4.8]", r"\begin{remarks}[2.4.8]",
    "Apply together with the next edit (\\end). The remarks environment is defined in EGA_IV2_FR.tex (GLOBAL_ISSUES 28).")
add(21, "end of (2.4.8)", "see the previous entry", "\\end{remark}", "word", None, "high",
    r"\end{remark}¶¶\begin{proposition}[2.4.9]", r"\end{remarks}¶¶\begin{proposition}[2.4.9]",
    "Apply together with the previous edit.")
c2(21, "Remarques (2.4.8) (i): 'irréductible (II, 7.4) de point générique'", r"(II, 7.4) de point",
   r"(\textbf{II}, 7.4) de point")
add(21, "Remarques (2.4.8) (i): 'le préschéma somme Y ⨿ Spec(k(y))'", "bold italic k", "plain k", "convention", 1, "high",
    r"\amalg\operatorname{Spec}(k(y))", r"\amalg\operatorname{Spec}(\boldsymbol{k}(y))")
add(21, "Remarques (2.4.8) (i): 'la partie ouverte Spec(k(y)) de X'", "bold italic k", "plain k", "convention", 1, "high",
    r"ouverte $\operatorname{Spec}(k(y))$", r"ouverte $\operatorname{Spec}(\boldsymbol{k}(y))$")
c2(21, "Remarques (2.4.8) (i): 'pas ouvert dans Y (II, 7.4.3)'", r"(II, 7.4.3)", r"(\textbf{II}, 7.4.3)")
add(21, "Remarques (2.4.8) (ii): 'homéomorphisme universel (2.4.4, (vi))'", "(2.4.4, (vi))",
    "keeps the printed reading", "misprint_in_print", None, "high", None, None,
    "(2.4.4) has no part (vi). The statement used (f universally homeomorphic etc. iff f_red is) is (2.4.3, (vi)), proved "
    "on p. 20 and cited as (2.4.3, (vi)) in the proof of (2.4.9) on this page.",
    corrected="(2.4.3, (vi))")
add(21, "Remarques (2.4.8) (ii): 'f n'est plat que si X est réduit'", "'plat' italic", "upright", "italics", None, "high",
    r"n'est plat que", r"n'est \emph{plat} que")
add(21, "Proposition (2.4.9): 'Soit Y un préschéma discret.'", "'discret' upright (emphasis) inside the italic statement",
    "italic", "convention", 6, "high", r"préschéma discret", r"préschéma \emph{discret}",
    "\\emph gives the printed upright face inside the italic statement.")
add(21, "proof of (2.4.9): 'B étant une k-algèbre. Il s'agit'", "'k-algèbre' italic (emphasis)", "'algèbre' upright",
    "italics", None, "high", r"$B$ étant une $k$-algèbre", r"$B$ étant une \emph{$k$-algèbre}")
c2(21, "proof of (2.4.9): 'l'ouvert U_α = D(t_α) (I, 1.2.2.2)'", r"(I, 1.2.2.2)", r"(\textbf{I}, 1.2.2.2)")
add(21, "proof of (2.4.9): 'du préschéma Spec(B'_α ⊗_{A'} k(y')) = Spec(B_α ⊗_k k(y')) et V est son'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶\operatorname{Spec}(B'_\alpha\otimes_{A'}k(y'))¶=\operatorname{Spec}(B_\alpha\otimes_k k(y'))¶\]",
    r"$\operatorname{Spec}(B'_\alpha\otimes_{A'}k(y'))¶=\operatorname{Spec}(B_\alpha\otimes_k k(y'))$",
    "Display vs inline. Apply before the convention-1 edits of its two k (below).")
add(21, "proof of (2.4.9): 'par le morphisme v : Spec(B ⊗_k k(y')) → Spec(B_α ⊗_k k(y')). Comme'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶v:\operatorname{Spec}(B\otimes_k k(y'))¶\longrightarrow\operatorname{Spec}(B_\alpha\otimes_k k(y')).¶\]",
    r"$v:\operatorname{Spec}(B\otimes_k k(y'))¶\longrightarrow\operatorname{Spec}(B_\alpha\otimes_k k(y'))$.",
    "Display vs inline. Apply before the convention-1 edits of its two k (below).")
for where, old, new in [
        ("Spec(B'_α ⊗_{A'} k(y'))", r"\otimes_{A'}k(y')", r"\otimes_{A'}\boldsymbol{k}(y')"),
        ("= Spec(B_α ⊗_k k(y'))", r"=\operatorname{Spec}(B_\alpha\otimes_k k(y'))",
         r"=\operatorname{Spec}(B_\alpha\otimes_k \boldsymbol{k}(y'))"),
        ("v : Spec(B ⊗_k k(y'))", r"v:\operatorname{Spec}(B\otimes_k k(y'))",
         r"v:\operatorname{Spec}(B\otimes_k \boldsymbol{k}(y'))"),
        ("→ Spec(B_α ⊗_k k(y'))", r"\longrightarrow\operatorname{Spec}(B_\alpha\otimes_k k(y'))",
         r"\longrightarrow\operatorname{Spec}(B_\alpha\otimes_k \boldsymbol{k}(y'))"),
        ("last line: 'B_α ⊗_k k(y') → ...', first k(y')", r"$B_\alpha\otimes_k k(y')\to",
         r"$B_\alpha\otimes_k \boldsymbol{k}(y')\to"),
        ("last line: '... → B ⊗_k k(y')', second k(y')", r"\to B\otimes_k k(y')$", r"\to B\otimes_k \boldsymbol{k}(y')$")]:
    add(21, "proof of (2.4.9): " + where, "bold italic k (the subscript k of ⊗_k is plain)", "plain k", "convention", 1,
        "high", old, new, "Old string matches once before and after the inline edits.")

# ---------------------------------------------------------------- page 22
add(22, "l. 1: 'est injectif par platitude'", "'injectif' italic", "upright", "italics", None, "high",
    r"est injectif par platitude", r"est \emph{injectif} par platitude")
c2(22, "l. 1: 'dominant (I, 1.2.7)'", r"(I, 1.2.7)", r"(\textbf{I}, 1.2.7)")
add(22, "Remarque (2.4.11): 'on sait que, pour toute partie E de Y'", "'toute' italic", "upright", "italics", None, "high",
    r"pour toute partie", r"pour \emph{toute} partie")
add(22, "title of 2.5", "'Permanence des propriétés des Modules par descente fidèlement plate.' with a final full stop",
    "no full stop", "punctuation", None, "high",
    r"par descente fidèlement plate}", r"par descente fidèlement plate.}",
    "Same pattern as GLOBAL_ISSUES 43/58: no \\subsection title in ega4-2-fr.tex has the printed full stop.")
add(22, "Proposition (2.5.1): 'soit plat (resp. fidèlement plat) relativement à f, il faut'",
    "'(resp.' upright inside the italic statement", "italic (proposition environment)", "convention", 6, "high",
    r"(resp. fidèlement plat) relativement à $f$,", r"\textup{(resp.} fidèlement plat) relativement à $f$,")
add(22, "Proposition (2.5.1): 'soit plat (resp. fidèlement plat) relativement à f''",
    "'(resp.' upright inside the italic statement", "italic (proposition environment)", "convention", 6, "high",
    r"(resp. fidèlement plat) relativement à¶$f'$", r"\textup{(resp.} fidèlement plat) relativement à¶$f'$")
for lab, rest in [("i", "de type"), ("ii", "de présentation"), ("iii", "localement libre de type"),
                  ("iv", "localement libre de rang")]:
    add(22, f"Proposition (2.5.2), label ({lab})", f"label ({lab}) upright",
        f"\\item[({lab})] inside the italic statement (italic)", "convention", 6, "high",
        "\\item[(" + lab + ")] " + rest, "\\item[\\textup{(" + lab + ")}] " + rest, "GLOBAL_ISSUES 16.")
add(22, "Proposition (2.5.2): 'si P désigne une des propriétés'", "bold italic P", "\\mathbf P (bold upright)",
    "convention", 10, "high", r"si $\mathbf P$ désigne", r"si $\boldsymbol{P}$ désigne")
add(22, "Proposition (2.5.2): 'possède la propriété P, il faut'", "bold italic P", "\\mathbf P (bold upright)",
    "convention", 10, "high", r"propriété $\mathbf P$, il faut", r"propriété $\boldsymbol{P}$, il faut")
add(22, "proof of (2.5.2): '(Bourbaki, Alg. comm., chap. II, § 5, no 2, cor. 2 du th. 1'",
    "chap. II with a BOLD II (wrong fount; other Bourbaki chapter numerals on pp. 20-24 are light)",
    "plain II (silently normalised)", "misprint_in_print", None, "medium",
    r"chap.~II, \S~5", r"chap.~\textbf{II}, \S~5",
    "Wrong-fount numeral (GLOBAL_ISSUES 29: wrong-font letters are reproduced in the diplomatic text).",
    corrected=r"chap.~II, \S~5")
add(22, "proof of (2.5.2): 'car f^*(O^n_Y) = O^n_X, donc si F et F''",
    "f^*(O_Y^n) = O_X^n (subscripts Y and X)", "silently corrected to f^*(\\mathcal O_X^n)=\\mathcal O_{X'}^n",
    "misprint_in_print", None, "high",
    r"f^*(\mathcal O_X^n)=\mathcal O_{X'}^n", r"f^*(\mathcal O_Y^n)=\mathcal O_X^n",
    "In (2.5.2) f : X' -> X, so the printed subscripts are a misprint. The fix restores the printed reading.",
    corrected=r"f^*(\mathcal O_X^n)=\mathcal O_{X'}^n")

# ---------------------------------------------------------------- page 23
add(23, "l. 2: 'un schéma affine X''", "'affine' italic", "upright", "italics", None, "high",
    r"schéma affine $X''$", r"schéma \emph{affine} $X''$")
add(23, "l. 4: 'possède la propriété P, ou que'", "bold italic P", "\\mathbf P (bold upright)", "convention", 10,
    "high", r"$\mathbf P$, ou que", r"$\boldsymbol{P}$, ou que")
c2(23, "l. 5: 'compte tenu de (2.2.3) et (II, 6.1.4.1)'", r"(II, 6.1.4.1)", r"(\textbf{II}, 6.1.4.1)")
add(23, "Lemme (2.5.3): '(resp. de présentation finie)'", "'(resp.' upright inside the italic statement",
    "italic (lemma environment)", "convention", 6, "high",
    r"(resp. de¶présentation", r"\textup{(resp.} de¶présentation")
add(23, "Remarque (2.5.4): 'suppose seulement f quasi-fidèlement plat (2.3.3)'", "'quasi-fidèlement plat' italic",
    "no emphasis", "italics", None, "high",
    r"$f$ quasi-fidèlement plat (2.3.3)", r"$f$ \emph{quasi-fidèlement plat} (2.3.3)")
add(23, "Lemme (2.5.4.1): 'tel que u ⊗ 1 : P ⊗_A A' → Q ⊗_A A' soit surjectif'", "formula set inline in the running text",
    "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶u\otimes 1:P\otimes_A A'\longrightarrow Q\otimes_A A'¶\]",
    r"$u\otimes 1:P\otimes_A A'\longrightarrow Q\otimes_A A'$",
    "Display vs inline; the formula itself matches.")
add(23, "proof of (2.5.4.1): 'l'homomorphisme u ⊗ 1_N' : (P ⊗_A A') ⊗_A' N' → (Q ⊗_A A') ⊗_A' N' est surjectif'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶u\otimes 1_{N'}:(P\otimes_A A')\otimes_{A'}N'¶\longrightarrow(Q\otimes_A A')\otimes_{A'}N'¶\]",
    r"$u\otimes 1_{N'}:(P\otimes_A A')\otimes_{A'}N'¶\longrightarrow(Q\otimes_A A')\otimes_{A'}N'$",
    "Display vs inline; the formula itself matches.")
add(23, "proof of (2.5.4.1): 'il s'écrit u_p ⊗ 1 : P_p ⊗_{A_p} N'_q → Q_p ⊗_{A_p} N'_q (0_I, 1.5.4). Par hypothèse'",
    "formula and reference set inline in the running text", "displayed with \\[ ... \\quad(0_{\\mathrm I},1.5.4). \\]",
    "other", None, "high",
    r"\[¶u_{\mathfrak p}\otimes 1:¶P_{\mathfrak p}\otimes_{A_{\mathfrak p}}N'_{\mathfrak q}¶\longrightarrow¶Q_{\mathfrak p}\otimes_{A_{\mathfrak p}}N'_{\mathfrak q}¶\quad(0_{\mathrm I},1.5.4).¶\]",
    r"$u_{\mathfrak p}\otimes 1:¶P_{\mathfrak p}\otimes_{A_{\mathfrak p}}N'_{\mathfrak q}¶\longrightarrow¶Q_{\mathfrak p}\otimes_{A_{\mathfrak p}}N'_{\mathfrak q}$¶$(0_{\mathrm I},1.5.4)$.",
    "Display vs inline. Apply before the convention-2 edit of (0_I, 1.5.4) (next entry).")
c2(23, "proof of (2.5.4.1): '(0_I, 1.5.4)'", r"(0_{\mathrm I},1.5.4)", r"(\mathbf{0}_{\mathrm I},1.5.4)",
   "Old string matches once before and after the inline edit above.", scan="bold 0", tex="plain 0")
c2(23, "proof of (2.5.4.1): 'A_p-module plat (0_I, 6.3.1)'", r"(0_{\mathrm I},6.3.1)", r"(\mathbf{0}_{\mathrm I},6.3.1)",
   scan="bold 0", tex="plain 0")
c2(23, "proof of (2.5.4.1): 'fidèlement plat (0_I, 6.4.1). Il en résulte'", r"$(0_{\mathrm I},6.4.1)$. Il",
   r"$(\mathbf{0}_{\mathrm I},6.4.1)$. Il", scan="bold 0", tex="plain 0")
c2(23, "proof of (2.5.4.1): 'u_p est surjectif (0_I, 6.4.1), et ceci'", r"$(0_{\mathrm I},6.4.1)$, et",
   r"$(\mathbf{0}_{\mathrm I},6.4.1)$, et", scan="bold 0", tex="plain 0")
add(23, "Proposition (2.5.5): 'on pose F_y = F ⊗_{O_Y} k(y)'", "bold italic k", "plain k", "convention", 1, "high",
    r"\otimes_{\mathcal O_Y}k(y)", r"\otimes_{\mathcal O_Y}\boldsymbol{k}(y)")
add(23, "(2.5.5.1): 'long(E_y) . long((F_y)_x)'", "a point between the two factors: long(E_y) . long((F_y)_x)",
    "thin space \\, (no point)", "symbol", None, "high",
    r"\operatorname{long}(\mathscr E_y)\,", r"\operatorname{long}(\mathscr E_y).")
add(23, "(2.5.5.1), end of the formula", "no full stop after long((F_y)_x)", "full stop after the formula",
    "punctuation", None, "high",
    r"\operatorname{long}\bigl((\mathscr F_y)_x\bigr).", r"\operatorname{long}\bigl((\mathscr F_y)_x\bigr)")
c2(23, "proof of (2.5.5): 'Supp(E ⊗_Y F)) ⊂ Supp(E) (0_I, 5.2.2)'", r"(0_{\mathrm I},5.2.2)",
   r"(\mathbf{0}_{\mathrm I},5.2.2)", scan="bold 0", tex="plain 0")
add(23, "proof of (2.5.5): '(Err_III, 30)'", "bold 'Err' with a light (not bold) subscript III",
    "\\textsubscript{\\textbf{III}} (bold subscript)", "font", None, "high",
    r"\textsubscript{\textbf{III}}", r"\textsubscript{III}")
add(23, "proof of (2.5.5): 'et que l'on a Supp(E ⊗_Y F) = Supp(E ⊗_Y G).' then new paragraph 'Supposons donc'",
    "formula set inline at the end of the paragraph; 'Supposons donc' begins a new indented paragraph",
    "displayed with \\[ ... \\], followed directly by 'Supposons donc' (same paragraph)", "other", None, "high",
    r"\[¶\operatorname{Supp}(\mathscr E\otimes_Y\mathscr F)¶=\operatorname{Supp}(\mathscr E\otimes_Y\mathscr G).¶\]¶Supposons donc",
    r"$\operatorname{Supp}(\mathscr E\otimes_Y\mathscr F)¶=\operatorname{Supp}(\mathscr E\otimes_Y\mathscr G)$.¶¶Supposons donc",
    "Display vs inline, plus the printed paragraph break before 'Supposons donc'.")
add(23, "proof of (2.5.5): 'on a f^{-1}(Z) ⊂ Supp(E ⊗_Y F) (I, 9.1.13), et il résulte'",
    "formula and reference set inline in the running text; bold I", "displayed with \\[ ... \\quad\\text{(I, 9.1.13),} \\]",
    "other", None, "high",
    r"\[¶f^{-1}(Z)\subset\operatorname{Supp}(\mathscr E\otimes_Y\mathscr F)¶\quad\text{(I, 9.1.13),}¶\]",
    r"$f^{-1}(Z)\subset\operatorname{Supp}(\mathscr E\otimes_Y\mathscr F)$¶(\textbf{I}, 9.1.13),",
    "Display vs inline; also sets the bold I of this reference (the convention-2 entry below has no separate edit).")
add(23, "proof of (2.5.5): first '(I, 9.1.13)'", "bold I", "plain I", "convention", 2, "high", None, None,
    "Included in the inline edit above.")
c2(23, "proof of (2.5.5): 'en outre (0_I, 2.1.8)'", r"(0_{\mathrm I},2.1.8)", r"(\mathbf{0}_{\mathrm I},2.1.8)",
   scan="bold 0", tex="plain 0")
c2(23, "proof of (2.5.5): 'Supp(F_y) (I, 9.1.13), et réciproquement'", r"(I, 9.1.13), et¶réciproquement",
   r"(\textbf{I}, 9.1.13), et¶réciproquement")

# ---------------------------------------------------------------- page 24
add(24, "l. 1: 'on a (E ⊗_Y F)_x = E_y ⊗_{O_y} F_x (I, 9.1.12) et'", "formula and reference set inline in the running text",
    "displayed with \\[ ... \\quad\\text{(I, 9.1.12)} \\]", "other", None, "high",
    r"\[¶(\mathscr E\otimes_Y\mathscr F)_x¶=\mathscr E_y\otimes_{\mathcal O_{Y,y}}\mathscr F_x¶\quad\text{(I, 9.1.12)}¶\]",
    r"$(\mathscr E\otimes_Y\mathscr F)_x¶=\mathscr E_y\otimes_{\mathcal O_{Y,y}}\mathscr F_x$¶(I, 9.1.12)",
    "Display vs inline. Apply before the two edits below (subscript O_y and bold I).")
add(24, "l. 1: tensor subscript in 'E_y ⊗_{O_y} F_x'", "⊗ with subscript O_y (script O, subscript y)",
    "\\otimes_{\\mathcal O_{Y,y}}", "formula", None, "high",
    r"\otimes_{\mathcal O_{Y,y}}", r"\otimes_{\mathcal O_y}")
c2(24, "l. 1: '(I, 9.1.12)'", r"(I, 9.1.12)", r"(\textbf{I}, 9.1.12)",
   "Old string matches once before and after the inline edit.")
add(24, "(2.5.5.3): 'long_A(M) . long_B(N/mN)'", "a point between the two factors", "thin space \\, (no point)",
    "symbol", None, "high", r"\operatorname{long}_A(M)\,", r"\operatorname{long}_A(M).")
add(24, "proof of (2.5.5.2): '(m^kM ⊗_A N)/(m^{k+1}M ⊗_A N) étant isomorphe à'",
    "inline, written with a slash and parentheses: (m^kM⊗_A N)/(m^{k+1}M⊗_A N)", "displayed \\frac{...}{...}",
    "formula", None, "high",
    r"\[¶\frac{\mathfrak m^kM\otimes_A N}{\mathfrak m^{k+1}M\otimes_A N}¶\]",
    r"$(\mathfrak m^kM\otimes_A N)/(\mathfrak m^{k+1}M\otimes_A N)$")
add(24, "proof of (2.5.5.2): 'isomorphe à (m^kM/m^{k+1}M) ⊗_A N, donc aussi à'", "formula set inline in the running text",
    "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶(\mathfrak m^kM/\mathfrak m^{k+1}M)\otimes_A N,¶\]",
    r"$(\mathfrak m^kM/\mathfrak m^{k+1}M)\otimes_A N$,",
    "Display vs inline; the formula itself matches.")
add(24, "proof of (2.5.5.2): 'donc aussi à (m^kM/m^{k+1}M) ⊗_{A/m} (N/mN) (0 ≤ k ≤ r—1); la longueur'",
    "formula and range set inline in the running text", "displayed with \\[ ... \\quad(0\\leq k\\leq r-1)~; \\]",
    "other", None, "high",
    r"\[¶(\mathfrak m^kM/\mathfrak m^{k+1}M)¶\otimes_{A/\mathfrak m}(N/\mathfrak mN)¶\quad(0\leq k\leq r-1)~;¶\]",
    r"$(\mathfrak m^kM/\mathfrak m^{k+1}M)¶\otimes_{A/\mathfrak m}(N/\mathfrak mN)$¶$(0\leq k\leq r-1)$~;",
    "Display vs inline. Apply before the convention-7 edit of this r-1 (next entry).")
add(24, "same place: '(0 ≤ k ≤ r—1)'", "long dash for the minus in r—1", "r-1", "convention", 7, "high",
    r"k\leq r-1)", r"k\leq r\setmin 1)",
    "Subtraction (GLOBAL_ISSUES 23). Old string matches once before and after the inline edit. \\setmin is not defined in "
    "EGA_IV2_FR.tex (IV-1 has \\providecommand{\\setmin}{-}).")
add(24, "proof of (2.5.5.2): 'Par addition (pour 0 ≤ k ≤ r—1)'", "long dash for the minus in r—1", "r-1", "convention",
    7, "high", r"r-1$), on en", r"r\setmin 1$), on en", "See the previous entry.")
add(24, "Remarque (2.5.5.4): 'et que N est un A-module plat; en effet'", "'plat' italic", "upright", "italics", None,
    "high", r"$A$-module plat~;", r"$A$-module \emph{plat}~;")
add(24, "proof of (2.5.6): 'l'application v ⇝ u∘v de C dans M'", "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
    r"$v\mapsto u\circ v$", r"$v\leadsto u\circ v$", "GLOBAL_ISSUES 33 (wavy arrows).")
add(24, "Corollaire (2.5.7): 'étant celles de (2.5.6), supposons'", "reference upright inside the italic statement",
    "italic (corollary environment)", "convention", 6, "high", r"celles de (2.5.6)", r"celles de \textup{(2.5.6)}")
add(24, "Corollaire (2.5.7), label (i)", "label (i) upright", "\\item[(i)] inside the italic statement (italic)",
    "convention", 6, "high", r"\item[(i)] $V$ et", r"\item[\textup{(i)}] $V$ et", "GLOBAL_ISSUES 16.")
add(24, "Corollaire (2.5.7), label (ii)", "label (ii) upright", "\\item[(ii)] inside the italic statement (italic)",
    "convention", 6, "high", r"\item[(ii)] $V$ et", r"\item[\textup{(ii)}] $V$ et", "GLOBAL_ISSUES 16.")
add(24, "Corollaire (2.5.7): 'les conditions a) et b) de (2.5.6) sont aussi'", "reference upright inside the italic statement",
    "italic (corollary environment)", "convention", 6, "high", r"de (2.5.6) sont aussi", r"de \textup{(2.5.6)} sont aussi")
add(24, "proof of (2.5.7): 'sur lui-même est bijectif dans les deux cas'", "'bijectif' italic", "upright", "italics",
    None, "high", r"est¶bijectif dans", r"est¶\emph{bijectif} dans")

# ---------------------------------------------------------------- checks
ok = True
pages = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8") for n in range(20, 25)}  # universal newlines: LF
orig = dict(pages)
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    n0 = orig[p].count(fx["old"])
    n1 = pages[p].count(fx["old"])
    if n0 != 1 or n1 != 1:
        ok = False
        print("PROBLEM", p, repr(fx["old"])[:80], "original:", n0, "sequential:", n1)
    if n1 == 1:
        pages[p] = pages[p].replace(fx["old"], fx["new"])
for x in F:
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        ok = False
        print("misprint without corrected", x["where"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    c[1 if x["kind"] == "convention" else 2 if x["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "NOT OK", len(F), "findings", counts)
for n in range(20, 25):
    (HERE / f"after_{n:03d}.tex").write_text(pages[n], encoding="utf-8", newline="\n")
