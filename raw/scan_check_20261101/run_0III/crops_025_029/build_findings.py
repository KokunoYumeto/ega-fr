"""Build findings_025_029.json for the EGA 0_III scan check and verify every fix.
The character U+00B6 (pilcrow) stands for a line break in the strings below."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_025_029.json"
NL = "\u00b6"


def nl(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, old, new, conf="high", conv=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


BI = "Category letter printed bold italic in roman text (as $\\boldsymbol{C}$ elsewhere in ega3-1-fr.tex, pp. 10-12)."
BU = "Checked on a crop: inside italic statements the print sets the category letter bold upright (bold italic in roman text)."

# ---------------- page 25 ----------------
add(25, "(11.1.3), 1st sentence: 'est une filtration (décroissante) d'un objet'",
    "'filtration' italic", "est une filtration (décroissante)", "italics",
    r"est une filtration (décroissante)", r"est une \emph{filtration} (décroissante)")
add(25, "(11.1.3), 1st sentence: 'd'un objet X∈C, on dit que'",
    "bold italic C", r"$X\in\mathcal C$", "font",
    r"$X\in\mathcal C$, on dit", r"$X\in\boldsymbol{C}$, on dit", note=BI)
add(25, "(11.1.3), definition of 'faiblement convergente': 'B_∞(E_2^pq)=sup_k(B_k(E_2^pq)), Z_∞(E_2^pq)=inf_k(Z_k(E_2^pq))'",
    "the two equalities are set inline in the running text (k under sup and inf)", "displayed formula", "other",
    r"si l'on a¶\[¶  B_\infty(E_2^{pq})=\sup_k(B_k(E_2^{pq})),\qquad¶  Z_\infty(E_2^{pq})=\inf_k(Z_k(E_2^{pq}))¶\]¶(autrement dit",
    r"si l'on a¶$B_\infty(E_2^{pq})=\sup_k(B_k(E_2^{pq}))$,¶$Z_\infty(E_2^{pq})=\inf_k(Z_k(E_2^{pq}))$¶(autrement dit",
    note="Layout: the print sets this formula inline; the TeX displays it. Index position under sup/inf left as is.")
add(25, "(11.1.3): 'déterminés par les données a) à c) de la suite spectrale E'",
    "a) and c) italic, 'à' roman", "données a) à c) de", "italics",
    r"données a) à c) de", r"données \emph{a)} à \emph{c)} de")
add(25, "(11.1.3), conditions for 'birégulière', label a)",
    "italic label 'a)' without an opening parenthesis", r"\item[(a)]", "punctuation",
    r"\item[(a)]", r"\item[\textit{a)}]", note="Roman paragraph; the print's labels are italic a), b).")
add(25, "(11.1.3), conditions for 'birégulière', label b)",
    "italic label 'b)' without an opening parenthesis", r"\item[(b)]", "punctuation",
    r"\item[(b)]", r"\item[\textit{b)}]", note="As for a).")
add(25, "(11.1.4), 1st line: 'dans la catégorie C, les limites inductives'",
    "bold italic C", r"$\mathcal C$", "font",
    r"catégorie $\mathcal C$, les limites", r"catégorie $\boldsymbol{C}$, les limites", note=BI)
add(25, "(11.1.4): 'd'un objet X∈C est exhaustive'",
    "bold italic C", r"$X\in\mathcal C$", "font",
    r"$X\in\mathcal C$ est", r"$X\in\boldsymbol{C}$ est", note=BI)
add(25, "(11.1.4): 'une suite spectrale E′ de C faiblement convergente'",
    "bold italic C", r"$\mathcal C$", "font",
    r"$\mathcal C$ faiblement convergente", r"$\boldsymbol{C}$ faiblement convergente", note=BI)
add(25, "Proposition (11.1.5): 'Soient C une catégorie abélienne'",
    "bold upright C inside the italic statement", r"$\mathcal C$", "font",
    r"Soient $\mathcal C$ une", r"Soient $\mathbf{C}$ une", note=BU)
add(25, "Proposition (11.1.5): 'E, E′ deux suites spectrales régulières'",
    "E upright inside the italic statement", "plain-text E inside the italic proposition environment (comes out italic)",
    "convention", r"exactes, E, $E'$", r"exactes, \textup{E}, $E'$", conv=6)
add(25, "Proposition (11.1.5): 'régulières de C, u : E→E′ un morphisme'",
    "bold upright C inside the italic statement", r"$\mathcal C$", "font",
    r"de $\mathcal C$, $u", r"de $\mathbf{C}$, $u", note=BU)

# ---------------- page 26 ----------------
add(26, "(11.1.6): 'un entier q(n) tel que E_r^{n−q,q}=0 pour tout q≠q(n)'",
    "'pour tout' italic", "pour tout upright", "italics",
    r"$E_r^{n-q,q}=0$ pour tout", r"$E_r^{n-q,q}=0$ \emph{pour tout}", note="Checked on a crop.")
add(26, "(11.1.6): 'si E est faiblement convergente, on a donc aussi'",
    "'faiblement convergente' italic", "upright", "italics",
    r"si E est faiblement convergente,", r"si E est \emph{faiblement convergente},")
add(26, "(11.1.6): 'pour tout n∈Z, gr_p(E^n)=0 pour p≠q(n) et gr_{q(n)}(E^n)=E_r^{n−q(n),q(n)}'",
    "gr_p(E^n)=0 pour p≠q(n) et gr_{q(n)}(E^n)=E_r^{n−q(n),q(n)}",
    r"$\operatorname{gr}_p(E^n)=0$ pour $p\ne q(n)$ et $\operatorname{gr}_{q(n)}(E^n)=E_r^{n-q(n),q(n)}$ (printed reading kept)",
    "misprint_in_print", None, None, conf="medium",
    corrected=r"$\operatorname{gr}_p(E^n)=0$ pour $p\ne n-q(n)$ et $\operatorname{gr}_{n-q(n)}(E^n)=E_r^{n-q(n),q(n)}$",
    note="The TeX keeps the printed reading. By (11.1.1) f), beta^{pq}: E_inf^{pq} ~ gr_p(E^{p+q}), so gr_p(E^n) ~ E_inf^{p,n-p}, which vanishes unless n-p=q(n); the print uses q(n) (the second index) as the filtration index.")
add(26, "(11.1.6): 'la filtration de E^n est discrète et exhaustive'",
    "'discrète' and 'exhaustive' italic", "upright", "italics",
    r"$E^n$ est discrète et exhaustive,", r"$E^n$ est \emph{discrète} et \emph{exhaustive},")
add(26, "(11.1.6): 'la suite E est régulière et on a'",
    "'régulière' italic", "upright", "italics",
    r"la suite E est régulière et on a", r"la suite E est \emph{régulière} et on a")
add(26, "(11.1.7), 1st line: 'dans la catégorie C les limites inductives'",
    "bold italic C", r"$\mathcal C$", "font",
    r"catégorie $\mathcal C$ les limites", r"catégorie $\boldsymbol{C}$ les limites", note=BI)
add(26, "(11.1.7): 'de suites spectrales de C. Alors la limite inductive'",
    "bold italic C", r"$\mathcal C$", "font",
    r"$\mathcal C$. Alors", r"$\boldsymbol{C}$. Alors", note=BI)
add(26, "(11.1.7): 'des suites spectrales d'objets de C : il suffit'",
    "bold italic C", r"$\mathcal C$", "font",
    r"d'objets de $\mathcal C$~:", r"d'objets de $\boldsymbol{C}$~:", note=BI)
add(26, "(11.1.7), end: 'l'exactitude du foncteur lim dans C.'",
    "bold italic C", r"$\mathcal C$", "font",
    r"$\varinjlim$ dans $\mathcal C$.", r"$\varinjlim$ dans $\boldsymbol{C}$.", note=BI)
add(26, "Remarque (11.1.8): 'Supposons que la catégorie C soit la catégorie des A-modules'",
    "bold italic C (remark printed roman)", r"$\mathcal C$", "font",
    r"catégorie $\mathcal C$ soit", r"catégorie $\boldsymbol{C}$ soit", note="Checked on a crop. " + BI)
add(26, "Remarque (11.1.8): 'l'aboutissement (E^n) est discrète et co-discrète pour tout n'",
    "'discrète' and 'co-discrète' italic", "no \\emph", "italics",
    r"est discrète et co-discrète pour tout", r"est \emph{discrète} et \emph{co-discrète} pour tout",
    note="Judged with the remark body roman (the remark environment is italic in the TeX).")
add(26, "Remarque (11.1.8), last sentence: 'chacun des E_n est aussi un A-module de type fini'",
    "E_n (subscript n)", r"$E^n$ (silently corrected)", "misprint_in_print",
    r"chacun des $E^n$", r"chacun des $E_n$", corrected=r"$E^n$",
    note="Checked on a crop. The aboutissement is (E^n); the TeX silently corrects the print's E_n.")
add(26, "Lemme (11.1.10): 'une famille d'objets de C liés par les données'",
    "bold upright C inside the italic statement", r"$\mathcal C$", "font",
    r"d'objets de $\mathcal C$ liés", r"d'objets de $\mathbf{C}$ liés", note=BU)
add(26, "Lemme (11.1.10): 'liés par les données a), b), c) de (11.1.1)'",
    "a), b), c) upright inside the italic statement", "italic in the lemma environment", "convention",
    r"données¶a), b), c) de", r"données¶\textup{a), b), c)} de", conv=6, note="Checked on a crop.")
add(26, "Lemme (11.1.10): 'de (11.1.1). Pour un entier fixé n'",
    "(11.1.1) upright inside the italic statement", "italic in the lemma environment", "convention",
    r"(\hyperref[0.11.1.1-fr]{11.1.1}). Pour", r"\textup{(\hyperref[0.11.1.1-fr]{11.1.1})}. Pour", conv=6)
for lab in "abcd":
    add(26, f"Lemme (11.1.10), label {lab})",
        f"roman label '{lab})' without an opening parenthesis", f"\\item[({lab})]", "punctuation",
        f"\\item[({lab})]", f"\\item[\\textup{{{lab})}}]",
        note="Inside the italic lemma \\item[(" + lab + ")] prints an italic '(" + lab + ")'; the print has an upright '" + lab + ")'.")

# ---------------- page 27 ----------------
add(27, "proof of (11.1.10), 1st line: 'd'après les conditions a), b), c) de (11.1.1)'",
    "a), b), c) italic", "upright", "italics",
    r"conditions a), b), c) de", r"conditions \emph{a), b), c)} de")
add(27, "(11.2.1), 1st line: 'Étant donnée une catégorie abélienne C, nous conviendrons'",
    "bold italic C", r"$\mathcal C$", "font",
    r"abélienne $\mathcal C$, nous", r"abélienne $\boldsymbol{C}$, nous", note=BI)
add(27, "(11.2.1): 'les complexes (K^i)_{i∈Z} d'objets de C dans lesquels'",
    "bold italic C", r"$\mathcal C$", "font",
    r"$(K^i)_{i\in\mathbb Z}$ d'objets de $\mathcal C$", r"$(K^i)_{i\in\mathbb Z}$ d'objets de $\boldsymbol{C}$", note=BI)
add(27, "(11.2.1): 'les complexes (K_i)_{i∈Z} d'objets de C dans lesquels'",
    "bold italic C", r"$\mathcal C$", "font",
    r"$(K_i)_{i\in\mathbb Z}$ d'objets de $\mathcal C$", r"$(K_i)_{i\in\mathbb Z}$ d'objets de $\boldsymbol{C}$", note=BI)
add(27, "(11.2.1): 'est de degré −1. A tout complexe K^•=(K^i)'",
    "A without accent", "À tout complexe", "word",
    r"À tout complexe", r"A tout complexe", note="Checked on a crop: unaccented capital (as 'A cet' in EGA II, p. 29).")
add(27, "(11.2.1): 'des bicomplexes d'objets de C dans lesquels les deux'",
    "bold italic C", r"$\mathcal C$", "font",
    r"d'objets de¶$\mathcal C$ dans", r"d'objets de¶$\boldsymbol{C}$ dans", note=BI)
add(27, "(11.2.1): 'pour des objets gradués de C, de type Z'",
    "bold italic C", r"$\mathcal C$", "font",
    r"gradués} de $\mathcal C$, de type", r"gradués} de $\boldsymbol{C}$, de type", note=BI)
add(27, "(11.2.1): 'pour des opérateurs de dérivation nuls)'",
    "'nuls' italic", "upright", "italics",
    r"dérivation nuls)", r"dérivation \emph{nuls})")
add(27, "(11.2.1), 2nd paragraph: '(resp. ... et B_i(K_•)=Im(K_{i+1}→K_i)) (« objet des bords »)) de sorte que'",
    "Im(K_{i+1}→K_i)) with two closing parentheses before (« objet des bords »))",
    r"$B_i(K_\bullet)=\operatorname{Im}(K_{i+1}\to K_i)$ (silently corrected)", "misprint_in_print",
    r"\operatorname{Im}(K_{i+1}\to K_i)$", r"\operatorname{Im}(K_{i+1}\to K_i))$",
    corrected=r"$B_i(K_\bullet)=\operatorname{Im}(K_{i+1}\to K_i)$",
    note="Checked on a crop: the print closes one parenthesis more than it opens in the '(resp. ...)' clause; the TeX silently drops it.")
add(27, "(11.2.1), 3rd paragraph: 'est un complexe dans C, et T : C→C′'",
    "bold italic C", r"$\mathcal C$", "font",
    r"complexe dans¶$\mathcal C$, et", r"complexe dans¶$\boldsymbol{C}$, et", note=BI)
add(27, "(11.2.1), 3rd paragraph: 'T : C→C′ un foncteur'",
    "bold italic C and C′", r"$T:\mathcal C\to\mathcal C'$", "font",
    r"$T:\mathcal C\to\mathcal C'$", r"$T:\boldsymbol{C}\to\boldsymbol{C}'$",
    note="Checked on a crop; two letters. " + BI)
add(27, "(11.2.1), 3rd paragraph: 'un foncteur de C dans une catégorie abélienne C′'",
    "bold italic C", r"$\mathcal C$", "font",
    r"foncteur de $\mathcal C$¶dans", r"foncteur de $\boldsymbol{C}$¶dans", note=BI)
add(27, "(11.2.1), 3rd paragraph: 'une catégorie abélienne C′, nous désignerons'",
    "bold italic C′", r"$\mathcal C'$", "font",
    r"abélienne $\mathcal C'$, nous", r"abélienne $\boldsymbol{C}'$, nous", note=BI)
add(27, "(11.2.1), 3rd paragraph: '(resp. (T(K_i))) dans C′.'",
    "bold italic C′", r"$\mathcal C'$", "font",
    r"dans $\mathcal C'$.", r"dans $\boldsymbol{C}'$.", note=BI)
add(27, "(11.2.1), 4th paragraph: 'la définition des ∂-foncteurs (T, 2.1)'",
    "'∂-foncteurs' italic", "upright", "italics",
    r"des $\partial$-foncteurs (T, 2.1)", r"des \emph{$\partial$-foncteurs} (T, 2.1)")
add(27, "(11.2.1), 4th paragraph: 'nous dirons aussi ∂-foncteur au lieu de'",
    "'aussi' italic", "upright", "italics",
    r"dirons aussi $\partial$-foncteur", r"dirons \emph{aussi} $\partial$-foncteur")
add(27, "(11.2.1), last paragraph: 'un objet gradué (A_i)_{i∈Z} de C est limité inférieurement'",
    "bold italic C", r"$\mathcal C$", "font",
    r"$\mathcal C$ est \emph{limité", r"$\boldsymbol{C}$ est \emph{limité", note=BI)
add(27, "(11.2.2), 1st line: 'Soit K^• un complexe de C dont l'opérateur'",
    "bold italic C", r"$\mathcal C$", "font",
    r"complexe de $\mathcal C$ dont", r"complexe de $\boldsymbol{C}$ dont", note=BI)
add(27, "(11.2.2), last line: 'une filtration F(K^•)=(F^p(K^•))_{p∈Z} formé de sous-[objets gradués]'",
    "formé", "formé (printed reading kept)", "misprint_in_print", None, None, conf="low",
    corrected="formée",
    note="The TeX keeps the printed reading. Agreement slip: the participle refers to 'filtration' (feminine). Low: it could be read as agreeing with the symbol F(K^•).")

# ---------------- page 28 ----------------
add(28, "(11.2.2), 1st line: 'formé de sous-objets gradués de K^•'",
    "'gradués' italic", "upright", "italics",
    r"objets gradués de $K^\bullet$", r"objets \emph{gradués} de $K^\bullet$")
add(28, "(11.2.2), 1st display: 'H^{p+q}(F^p(K^•)/F^{p+r}(K^•))→H^{p+q}(F^p(K^•)/F^{p+1}(K^•))'",
    "no final full stop", "display ends with a full stop", "punctuation",
    r"F^{p+1}(K^\bullet)).¶\]", r"F^{p+1}(K^\bullet))¶\]",
    note="Checked on a crop: the print has no full stop after the display.")
add(28, "(11.2.2), 2nd paragraph: 'tous les Z_r^{pq}(K^•) et B_p^{pq}(K^•), pour p, q fixés'",
    "B_p^{pq}(K^•) (subscript p)", r"$B_r^{pq}(K^\bullet)$ (silently corrected)", "misprint_in_print",
    r"$B_r^{pq}(K^\bullet)$, pour $p$", r"$B_p^{pq}(K^\bullet)$, pour $p$",
    corrected=r"$B_r^{pq}(K^\bullet)$",
    note="Checked on a crop: subscript p in the print (Z_r^{pq} just before has r); the TeX silently corrects.")
add(28, "(11.2.3): 'deux complexes filtrés K^•, K′^• de C, et un morphisme'",
    "bold italic C", r"$\mathcal C$", "font",
    r"de $\mathcal C$, et un morphisme", r"de $\boldsymbol{C}$, et un morphisme", note=BI)

# ---------------- page 29 ----------------
add(29, "(11.2.4), 1st line: 'Supposons que dans C les limites inductives'",
    "bold italic C", r"$\mathcal C$", "font",
    r"dans $\mathcal C$ les limites", r"dans $\boldsymbol{C}$ les limites", note=BI)
add(29, "(11.2.4): 'et l'hypothèse sur C entraîne que la cohomologie'",
    "bold italic C", r"$\mathcal C$", "font",
    r"$\mathcal C$ entraîne", r"$\boldsymbol{C}$ entraîne", note=BI)
add(29, "(11.2.4): 'les limites inductives filtrantes dans C sont exactes'",
    "bold italic C", r"$\mathcal C$", "font",
    r"dans $\mathcal C$ sont", r"dans $\boldsymbol{C}$ sont", note=BI)
add(29, "(11.3.1): 'Supposons vérifiées l'une des deux conditions suivantes'",
    "'une' italic", "upright", "italics",
    r"vérifiées l'une des", r"vérifiées l'\emph{une} des")
LAY = "Layout: the print runs 1° and 2° into the paragraph ('suivantes : 1° Les ... dans C ; 2° Pour tout ... K^{pq}≠0. Alors, le bicomplexe ...'); the TeX makes a list. One of three edits that must be applied together (this one, '$.\\n  \\item[$2^\\circ$] Pour', '\\end{enumerate}')."
add(29, "(11.3.1): '1° Les sommes directes infinies existent dans C' (start of the run-in conditions)",
    "1° runs on after 'suivantes :' in the same paragraph", "enumerate list", "other",
    r"\begin{enumerate}¶  \item[$1^\circ$] Les", r"$1^\circ$ Les", conf="medium", note=LAY)
add(29, "(11.3.1): '1° Les sommes directes infinies existent dans C'",
    "'sommes directes infinies' italic", "upright", "italics",
    r"sommes directes infinies", r"\emph{sommes directes infinies}", note="Checked on a crop.")
add(29, "(11.3.1): 'existent dans C ;'",
    "bold italic C", r"$\mathcal C$", "font",
    r"existent dans $\mathcal C", r"existent dans $\boldsymbol{C}",
    note="Checked on a crop. 'old' stops before the closing $ so that it does not overlap the next edit. " + BI)
add(29, "(11.3.1): 'existent dans C ; 2° Pour tout n∈Z'",
    "semicolon after 'dans C', and 2° runs on in the same paragraph", "full stop; \\item[$2^\\circ$]", "punctuation",
    r"$.¶  \item[$2^\circ$] Pour", r"$~;¶$2^\circ$ Pour",
    note="Checked on a crop: semicolon in the print. This edit also runs item 2° into the paragraph (layout, apply with the 1° and \\end{enumerate} edits); without that layout change use new '$~;\\n  \\item[$2^\\circ$] Pour' instead.")
add(29, "(11.3.1): '... et K^{pq}≠0. Alors, le bicomplexe' (end of the run-in conditions)",
    "'Alors' continues the same paragraph", "\\end{enumerate}", "other",
    r"$K^{pq}\ne0$.¶\end{enumerate}¶", r"$K^{pq}\ne0$.¶", conf="medium", note=LAY)
add(29, "(11.3.1): 'le bicomplexe K^{••} définit un complexe (simple)'",
    "'complexe' italic, '(simple)' roman", "upright", "italics",
    r"définit un complexe (simple)", r"définit un \emph{complexe} (simple)")
add(29, "(11.3.1): 'Lorsque nous parlerons par la suite du complexe (simple) défini par un bicomplexe'",
    "'complexe' italic, '(simple)' roman", "complexe upright", "italics",
    r"la suite¶du complexe (simple)", r"la suite¶du \emph{complexe} (simple)")
add(29, "(11.3.1), 2nd paragraph: 'ses p^es objets des cocycles'",
    "p with superscript 'es'", r"$p$-èmes", "word",
    r"ses $p$-èmes objets", r"ses $p$\textsuperscript{es} objets", note="Checked on a crop.")
add(29, "(11.3.1), display, 1st line: 'd′ : Z_II^p(K^{i,•})→Z_II^p(K^{i+1,•})'",
    "no comma at the end of the line", "comma", "punctuation",
    r"Z_{\mathrm{II}}^p(K^{i+1,\bullet}),\\", r"Z_{\mathrm{II}}^p(K^{i+1,\bullet})\\",
    note="Checked on a crop: none of the three lines has a comma.")
add(29, "(11.3.1), display, 2nd line: 'd′ : B_II^p(K^{i,•})→B_II^p(K^{i+1,•})'",
    "no comma at the end of the line", "comma", "punctuation",
    r"B_{\mathrm{II}}^p(K^{i+1,\bullet}),\\", r"B_{\mathrm{II}}^p(K^{i+1,\bullet})\\")
add(29, "(11.3.1), display, 3rd line: 'd′ : H_II^p(K^{i,•})→H_II^p(K^{i+1,•})'",
    "no comma at the end of the display", "comma", "punctuation",
    r"\mathrm H_{\mathrm{II}}^p(K^{i+1,\bullet}),¶\end{aligned}", r"\mathrm H_{\mathrm{II}}^p(K^{i+1,\bullet})¶\end{aligned}")
add(29, "(11.3.1), 2nd paragraph: 'ses q^es objets de cocycles, de cobords'",
    "q with superscript 'es'", r"$q$-èmes", "word",
    r"ses $q$-èmes objets", r"ses $q$\textsuperscript{es} objets")
add(29, "(11.3.1), last sentence: 'désigne le n^e objet de cohomologie'",
    "n with superscript 'e'", r"$n$-ème", "word",
    r"$n$-ème objet", r"$n$\textsuperscript{e} objet", note="Checked on a crop.")
add(29, "(11.3.1), last sentence: 'du complexe (simple) défini par K^{••}'",
    "'(simple)' italic, with italic parentheses", "upright", "italics",
    r"complexe (simple) défini par", r"complexe \emph{(simple)} défini par", note="Checked on a crop.")
add(29, "(11.3.2.1), first sum: 'Σ_{i+j=n, i≥p} K^{ij}'",
    "index on one line: i+j=n, i≥p", r"\sum_{\substack{i+j=n\\i\geq p}} (two stacked lines)", "formula",
    r"\sum_{\substack{i+j=n\\i\geq p}}", r"\sum_{i+j=n,\,i\geq p}")
add(29, "(11.3.2.1), second sum: 'Σ_{i+j=n, j≥p} K^{ij}'",
    "index on one line: i+j=n, j≥p", r"\sum_{\substack{i+j=n\\j\geq p}} (two stacked lines)", "formula",
    r"\sum_{\substack{i+j=n\\j\geq p}}", r"\sum_{i+j=n,\,j\geq p}", note="Checked on a crop.")
add(29, "(11.3.2.1), end of the display",
    "no full stop; the sentence continues on p. 30 ('qui, par définition, sont ...')", "full stop before \\tag", "punctuation",
    r"_{n\in\mathbb Z}.¶  \tag", r"_{n\in\mathbb Z}¶  \tag", note="Checked on a crop.")

# ---------------- write and verify ----------------
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
# the page files were written with CRLF on Windows; the release files use LF, as the fixes do
texts = {n: (RUN / f"page_{n:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n") for n in range(25, 30)}
SRC = RUN.parent / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega3/ega3-1-fr.tex"
src = SRC.read_bytes().decode("utf-8")
assert "\r" not in src
bad = 0
spans = {}
for i, f in enumerate(F):
    t = texts[f["page"]]
    if f["fix"] is not None and f["fix"]["old"] not in src:
        print("NOT IN SOURCE", f["page"], repr(f["fix"]["old"]))
    if f["fix"] is None:
        assert f["kind"] == "misprint_in_print"
        continue
    old = f["fix"]["old"]
    c = t.count(old)
    if c != 1:
        bad += 1
        print("NOT UNIQUE", f["page"], c, repr(old))
    else:
        s = t.index(old)
        spans.setdefault(f["page"], []).append((s, s + len(old), i))
for p, sp in spans.items():
    sp.sort()
    for a, b in zip(sp, sp[1:]):
        if a[1] > b[0]:
            print("OVERLAP p.", p, F[a[2]]["fix"]["old"][:40], "|", F[b[2]]["fix"]["old"][:40])
# every \mathcal C on the pages is covered by a fix
for n, t in texts.items():
    occ = [m.start() for m in re.finditer(r"\\mathcal C(?![A-Za-z])", t)]
    cov = [o for o in occ if any(s <= o < e for s, e, _ in spans.get(n, []))]
    print("page", n, "mathcal C:", len(occ), "covered:", len(cov))
cnt = {}
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("findings", len(F), "not unique", bad)
for p in sorted(cnt):
    print(p, cnt[p])
