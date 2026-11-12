"""Build findings_130_134.json for the EGA IV-4 scan check (pages 130-134) and check every fix:
each "old" must occur exactly once in its page_NNN.tex and exactly once in the current source file, and the fixes of a
page must apply in list order."""
import json
import pathlib
import sys

R = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native\ega4\ega4-18-fr.tex")
OUT = R / "findings_130_134.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 130
add(130, "top of p. 130: page break 129/130 inside '... il faut et il suffit que chacune | de ses restrictions'",
    "p. 130 begins mid-sentence with 'de ses restrictions' at the left margin, no indent",
    "blank line after \\oldpage[IV-4]{130}: a paragraph break inside the sentence",
    "marker", None, "high",
    r"\oldpage[IV-4]{130}" + NL + NL + "de ses restrictions",
    r"\oldpage[IV-4]{130}" + NL + "de ses restrictions",
    "BOUNDARY FIX (page break with p. 129). The marker is at the right place. The blank line before it is already "
    "removed in the current source ('il suffit que chacune' + newline + \\oldpage[IV-4]{130}); this removes the one "
    "after it (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")
add(130, "Définition (18.5.8): 'On dit qu'un anneau A est hensélien s'il est semi-local'",
    "'hensélien' italic like the rest of the statement (crop p130_s2_hens1.png)",
    "\\emph{hensélien}: upright inside the italic definition",
    "convention", 6, "high",
    r"est \emph{hensélien} s'il est semi-local", r"est hensélien s'il est semi-local",
    "Printed italic word left upright by \\emph inside the itshape environment.")
add(130, "Définition (18.5.8): 'On appelle schéma local hensélien un schéma isomorphe'",
    "'schéma local hensélien' italic like the rest (crops p130_s2_schema.png, p130_s2_localhens.png)",
    "\\emph{schéma local hensélien}: upright",
    "convention", 6, "high",
    r"On appelle \emph{schéma local hensélien} un schéma", r"On appelle schéma local hensélien un schéma", "")
add(130, "Proposition (18.5.9), label '(i)'", "upright (i) (crop p130_s2_prop1859a.png)",
    "\\item[(i)] (italic in the proposition)", "convention", 6, "high",
    r"\item[(i)] Pour qu'un anneau semi-local", r"\item[\textup{(i)}] Pour qu'un anneau semi-local",
    "GLOBAL_ISSUES 16.")
add(130, "Proposition (18.5.9), label '(ii)'", "upright (ii) (crop p130_s2_prop1859b.png)",
    "\\item[(ii)] (italic)", "convention", 6, "high",
    r"\item[(ii)] Pour qu'un anneau local", r"\item[\textup{(ii)}] Pour qu'un anneau local", "GLOBAL_ISSUES 16.")
add(130, "Proposition (18.5.9) (ii), last word: '... isomorphe à un produit d'anneaux locaux.'",
    "'locaux.' set in roman inside the italic statement (crop p130_s2_prop1859b.png)",
    "italic", "convention", 6, "high",
    "soit isomorphe à un produit d'anneaux locaux.", r"soit isomorphe à un produit d'anneaux \textup{locaux}.",
    "Roman (emphasised) word inside the italic statement; the same phrase in (18.5.11 a)) is all italic.")
add(130, "Proposition (18.5.10): '(donc composé direct d'anneaux locaux henséliens (18.5.9))'",
    "'(donc' and '(18.5.9))' upright, 'composé direct d'anneaux locaux henséliens' italic (crop "
    "p130_s3_prop18510a.png, p130_s3_prop18510b.png)",
    "all italic", "convention", 6, "high",
    "(donc composé direct d'anneaux locaux henséliens (18.5.9))",
    r"\textup{(donc} composé direct d'anneaux locaux henséliens \textup{(18.5.9))}",
    "Roman 'donc', upright parentheses and reference inside the italic statement (GLOBAL_ISSUES 96).")
add(130, "Théorème (18.5.11), label 'a)'", "upright a) (crop p130_s4_thm_a.png)", "\\item[a)] (italic)",
    "convention", 6, "high",
    r"\item[a)] $A$ est hensélien", r"\item[\textup{a)}] $A$ est hensélien", "GLOBAL_ISSUES 16/88.")

# ---------------------------------------------------------------- page 131
add(131, "Théorème (18.5.11), label 'a′)'", "upright a with a prime (crop p131_s1_aprime.png)",
    "\\item[a')] (italic, typographic apostrophe)", "convention", 6, "high",
    r"\item[a')] La condition", r"\item[\textup{a$'$)}] La condition", "GLOBAL_ISSUES 88 (\\item[b$'$)] form).")
add(131, "Théorème (18.5.11) a′): 'La condition a) est satisfaite'", "upright a) inside the italic statement",
    "$a)$ (italic a, upright parenthesis)", "convention", 6, "high",
    "$a)$ est satisfaite pour toutes", r"\textup{a)} est satisfaite pour toutes", "GLOBAL_ISSUES 88.")
add(131, "Théorème (18.5.11), label 'b)'", "upright b)", "\\item[b)] (italic)", "convention", 6, "high",
    r"\item[b)] Soient $S=\Spec(A)$", r"\item[\textup{b)}] Soient $S=\Spec(A)$", "")
add(131, "Théorème (18.5.11) b): 'S_0 = Spec(k)'",
    "bold italic k in Spec(k); the k of S'⊗_A k on the next line is light (crops p131_s1_speck.png, "
    "p131_s1_otk.png)",
    "plain $k$", "convention", 1, "high",
    r"$S_0=\Spec(k)$. Pour tout morphisme étale", r"$S_0=\Spec(\boldsymbol{k})$. Pour tout morphisme étale",
    "Only this k is bold; S'_0=S'⊗_A k keeps the light k.")
add(131, "Théorème (18.5.11), label 'c)'", "upright c)", "\\item[c)] (italic)", "convention", 6, "high",
    r"\item[c)] Pour tout morphisme $f:X\to S$, séparé", r"\item[\textup{c)}] Pour tout morphisme $f:X\to S$, séparé",
    "")
add(131, "Théorème (18.5.11) c): '(Err_III, 20)'",
    "bold upright 'Err', roman subscript III, upright parentheses and 20 (crop p131_s1_err.png)",
    "Err$_{\\mathrm{III}}$ in the italic statement (italic Err, italic parentheses)", "font", None, "high",
    r"quasi-fini au point $x$ (Err$_{\mathrm{III}}$, 20), $X$ est somme",
    r"quasi-fini au point $x$ \textup{(\textbf{Err}$_{\mathrm{III}}$, 20)}, $X$ est somme",
    "Same form as the page fixes on pp. 65, 70-71.")
add(131, "Théorème (18.5.11) c), last word: '... soit un morphisme fini.'",
    "'fini.' set in roman inside the italic statement (crop p131_s1_fini.png)", "italic",
    "convention", 6, "high",
    r"$f|X':X'\to S$ soit un morphisme fini.", r"$f|X':X'\to S$ soit un morphisme \textup{fini}.",
    "Roman (emphasised) word inside the italic statement.")
add(131, "Théorème (18.5.11), label 'c′)'", "upright c with a prime (crop p131_s1_cp.png)",
    "\\item[c')] (italic, apostrophe)", "convention", 6, "high",
    r"\item[c')] Pour tout morphisme localement de type fini",
    r"\item[\textup{c$'$)}] Pour tout morphisme localement de type fini", "")
add(131, "Théorème (18.5.11), label 'c″)'", "upright c with a double prime (crop p131_s1_cp.png)",
    "\\item[c'')] (italic; '' gives a closing quotation mark)", "convention", 6, "high",
    r"\item[c'')] Pour tout morphisme localement de présentation finie",
    r"\item[\textup{c$''$)}] Pour tout morphisme localement de présentation finie", "")
add(131, "first paragraph after (18.5.11): 'Notons d'abord que la condition c′)'",
    "c′) wholly italic, italic parenthesis (crops p131_s2_resp.png, p131_s2_paren1.png)",
    "$c')$ (upright parenthesis)", "italics", None, "high",
    "Notons d'abord que la condition $c')$", r"Notons d'abord que la condition \emph{c$'$)}",
    "Labels in roman text are italic in the print (GLOBAL_ISSUES 88). Adjacent to (not overlapping) the next finding.")
add(131, "same sentence: '(resp. c″)) est équivalente'",
    "two closing parentheses after c″: the label's and the one closing '(resp.'; here both are upright, c″ italic "
    "(crop p131_s2_paren2.png)",
    "(resp. $c'')$ est: one parenthesis only", "punctuation", None, "high",
    "(resp. $c'')$ est équivalente", "(resp. $c'')$) est équivalente",
    "The TeX drops the parenthesis that closes '(resp.'. The label keeps the TeX form $c'')$ because its parenthesis "
    "is upright in the print at this place.")
add(131, "same paragraph: 'De même, la condition b) est équivalente'", "b) italic with italic parenthesis "
    "(crop p131_s2_memeb.png)", "$b)$", "italics", None, "high",
    "De même, la condition $b)$ est", r"De même, la condition \emph{b)} est", "GLOBAL_ISSUES 88.")
add(131, "same paragraph: 'dans b), c′) et c″), les morphismes donnés sont séparés'",
    "all three labels italic with italic parentheses (crop p131_s2_bornons.png)", "$b)$, $c')$, $c'')$",
    "italics", None, "high",
    "dans $b)$, $c')$ et $c'')$, les morphismes",
    r"dans \emph{b)}, \emph{c$'$)} et \emph{c$''$)}, les morphismes", "Three labels, one edit.")
add(131, "'Le fait que a) implique b) et que b) implique a′) est un cas particulier de (18.5.4)'",
    "labels italic with italic parentheses (crop p131_s2_lefait.png)", "$a)$, $b)$, $b)$, $a')$",
    "italics", None, "high",
    "Le fait que $a)$ implique $b)$ et que $b)$ implique $a')$ est",
    r"Le fait que \emph{a)} implique \emph{b)} et que \emph{b)} implique \emph{a$'$)} est", "Four labels, one edit.")
add(131, "'Montrons en outre que a′) implique a).'", "labels italic (crop p131_s2_lefait.png)",
    "$a')$, $a)$", "italics", None, "high",
    "Montrons en outre que $a')$ implique $a)$.", r"Montrons en outre que \emph{a$'$)} implique \emph{a)}.", "")
add(131, "'Or, en vertu de a′), A[T]/F.A[T] est composée directe'", "a′) italic (crop p131_s3_vertu.png)",
    "$a')$", "italics", None, "high",
    "en vertu de $a')$, $A[T]/F.A[T]$", r"en vertu de \emph{a$'$)}, $A[T]/F.A[T]$", "")
add(131, "'Il est immédiat que c) entraîne a), comme on le voit'", "labels italic (crop p131_s3_immediat.png)",
    "$c)$, $a)$", "italics", None, "high",
    "Il est immédiat que $c)$ entraîne $a)$, comme", r"Il est immédiat que \emph{c)} entraîne \emph{a)}, comme", "")
add(131, "'Pour voir que a) implique c), on peut'", "labels italic (crop p131_s3_immediat.png)", "$a)$, $c)$",
    "italics", None, "high",
    "Pour voir que $a)$ implique $c)$, on peut", r"Pour voir que \emph{a)} implique \emph{c)}, on peut", "")
add(131, "'f peut s'écrire comme un morphisme composé X →j Y →g S, où g est un morphisme fini'",
    "the composite is set in the line, followed by ', où g ...' (crop p131_s3_compose.png)",
    "displayed formula \\[ X\\xrightarrow{j}Y\\xrightarrow{g}S, \\]", "formula", None, "high",
    "comme un morphisme composé" + NL + r"\[" + NL + r"  X\xrightarrow{j}Y\xrightarrow{g}S," + NL + r"\]" + NL
    + "où $g$",
    r"comme un morphisme composé $X\xrightarrow{j}Y\xrightarrow{g}S$, où $g$",
    "Formula displayed in the TeX where the print sets it inline.")
add(131, "'il résulte de a) que B est composée directe d'anneaux locaux'", "a) italic (crop p131_s4_aqueB.png)",
    "$a)$", "italics", None, "high",
    "il résulte de $a)$ que $B$ est composée", r"il résulte de \emph{a)} que $B$ est composée", "")
add(131, "'Il est trivial que c) implique c′), en vertu de la remarque du début'",
    "labels italic (crop p131_s4_trivial.png)", "$c)$, $c')$", "italics", None, "high",
    "Il est trivial que $c)$ implique $c')$, en vertu", r"Il est trivial que \emph{c)} implique \emph{c$'$)}, en vertu",
    "")
add(131, "'Prouvons que c′) implique c″). Supposons en effet c′) vérifiée'", "labels italic (crop p131_s4_trivial.png)",
    "$c')$, $c'')$, $c')$", "italics", None, "high",
    "Prouvons que $c')$ implique $c'')$. Supposons en effet $c')$ vérifiée",
    r"Prouvons que \emph{c$'$)} implique \emph{c$''$)}. Supposons en effet \emph{c$'$)} vérifiée", "")
add(131, "end of p. 131: page break 131/132 inside '... prouvons que sous les conditions | de c″), l'ensemble'",
    "p. 132 begins mid-sentence with 'de c″),' at the left margin, no indent",
    "blank lines before and after \\oldpage[IV-4]{132}", "marker", None, "high",
    "prouvons que sous les conditions" + NL + NL, "prouvons que sous les conditions" + NL,
    "The marker is at the right place. Part 1 of 2: the first p. 132 finding removes the blank line after "
    "\\oldpage[IV-4]{132}; apply both.")

# ---------------------------------------------------------------- page 132
add(132, "top of p. 132: page break 131/132", "p. 132 begins mid-sentence ('de c″), l'ensemble ...')",
    "blank line after \\oldpage[IV-4]{132}", "marker", None, "high",
    r"\oldpage[IV-4]{132}" + NL + NL + "de ", r"\oldpage[IV-4]{132}" + NL + "de ",
    "Part 2 of 2 with the last p. 131 finding; both blank lines must go.")
add(132, "first line: 'de c″), l'ensemble Z = Spec(O_X,x)'", "c″) italic with italic parenthesis "
    "(crop p132_s1_l1.png)", "$c'')$", "italics", None, "high",
    "$c'')$, l'ensemble $Z", r"\emph{c$''$)}, l'ensemble $Z", "Does not overlap the marker fix just before.")
add(132, "'ce qui établira c″) (I, 2.4.2)'", "c″) italic (crop p132_s1_l1.png)", "$c'')$", "italics", None, "high",
    "établira $c'')$", r"établira \emph{c$''$)}", "")
add(132, "'ce qui établira c″) (I, 2.4.2). En premier lieu'", "bold I (crop p132_s1_l1.png)", "plain I",
    "convention", 2, "high",
    "(I, 2.4.2). En premier lieu", r"(\textbf{I}, 2.4.2). En premier lieu",
    "Genuine EGA I reference (bold I), not EGA IV's own (1.2.4.2).")
add(132, "'où j est le morphisme canonique (I, 2.4.1)'", "bold I (crop p132_s1_241.png)", "plain I",
    "convention", 2, "high",
    "canonique (I, 2.4.1)", r"canonique (\textbf{I}, 2.4.1)", "Genuine EGA I reference (bold I).")
add(132, "'((II, 6.1.5) et (1.4.3))'", "bold II (crop p132_s1_143.png)", "plain II", "convention", 2, "high",
    "((II, 6.1.5)", r"((\textbf{II}, 6.1.5)", "")
add(132, "same parenthesis: '... et (1.4.3)); j est par suite un morphisme fermé'",
    "(1.4.3): EGA IV's own reference, old-style 1 followed by a full stop, no bold I (crops p132_s1_l2.png, "
    "p132_s1_143.png)",
    "(I, 4.3): misread as an EGA I reference", "number", None, "high",
    "et (I, 4.3));", "et (1.4.3));",
    "The § 18 misreading of (1.x.y) as (I, x.y) (GLOBAL_ISSUES 78).")
add(132, "'j est par suite un morphisme fermé (II, 6.1.10)'", "bold II (crop p132_s1_l2.png)", "plain II",
    "convention", 2, "high", "morphisme fermé (II, 6.1.10), ce qui", r"morphisme fermé (\textbf{II}, 6.1.10), ce qui",
    "")
add(132, "'Il résulte alors de (I, 2.4.2) et (I, 4.2.2)'", "bold I (crop p132_s1_l2.png)", "plain I",
    "convention", 2, "high", "alors de (I, 2.4.2) et", r"alors de (\textbf{I}, 2.4.2) et",
    "Genuine EGA I reference.")
add(132, "same sentence: '(I, 4.2.2) que j est une immersion fermée'", "bold I (crop p132_s1_l3.png)", "plain I",
    "convention", 2, "high", "(I, 4.2.2) que $j$", r"(\textbf{I}, 4.2.2) que $j$", "Genuine EGA I reference.")
add(132, "'((1.4.7) et (0_I, 5.2.2))'", "bold 0 with subscript I (crop p132_s1_l3.png)", "plain 0",
    "convention", 2, "high",
    r"(1.4.7) et ($0_{\mathrm I}$, 5.2.2)", r"(1.4.7) et ($\mathbf{0}_{\mathrm I}$, 5.2.2)", "")
add(132, "'Enfin, c″) implique a′) : en effet'", "labels italic (crop p132_s2_enfin.png)", "$c'')$, $a')$",
    "italics", None, "high",
    "Enfin, $c'')$ implique $a')$", r"Enfin, \emph{c$''$)} implique \emph{a$'$)}", "")
add(132, "Corollaire (18.5.12): 'pour tout morphisme fini f : X → S'", "'fini' roman inside the italic statement "
    "(crop p132_s2_cor.png)", "italic", "convention", 6, "high",
    r"morphisme fini $f:X\to S$ et", r"morphisme \textup{fini} $f:X\to S$ et", "")
add(132, "Corollaire (18.5.12): 'et tout morphisme étale et séparé g : Y → S'",
    "'étale et séparé' roman (crop p132_s2_cor.png)", "italic", "convention", 6, "high",
    r"morphisme étale et séparé $g:Y\to S$", r"morphisme \textup{étale et séparé} $g:Y\to S$",
    "Does not overlap the previous finding.")
add(132, "Corollaire (18.5.12): 'X_0 = X ×_S S_0 et Y_0 = Y ×_S S_0'", "'et' between the formulas roman "
    "(crop p132_s2_cor.png)", "italic", "convention", 6, "high",
    r"$X_0=X\times_S S_0$ et $Y_0=Y\times_S S_0$", r"$X_0=X\times_S S_0$ \textup{et} $Y_0=Y\times_S S_0$", "")
add(132, "proof of (18.5.12): 'de l'équivalence de a) et b) dans (18.5.11)'", "labels italic "
    "(crop p132_s2_suff.png)", "$a)$, $b)$", "italics", None, "high",
    "l'équivalence de $a)$ et $b)$ dans (18.5.11)", r"l'équivalence de \emph{a)} et \emph{b)} dans (18.5.11)", "")
add(132, "proof of (18.5.12): 'de ce que a) implique b) dans (18.5.4)'", "labels italic (crop p132_s3_aimpb.png)",
    "$a)$, $b)$", "italics", None, "high",
    "de ce que $a)$ implique $b)$ dans (18.5.4)", r"de ce que \emph{a)} implique \emph{b)} dans (18.5.4)", "")
add(132, "Remarque (18.5.13): 'Les conditions équivalentes a), a′), b) du théorème'",
    "labels italic in the roman remark (crop p132_s3_rem.png)", "$a)$, $a')$, $b)$", "italics", None, "high",
    "Les conditions équivalentes $a)$, $a')$, $b)$ du théorème",
    r"Les conditions équivalentes \emph{a)}, \emph{a$'$)}, \emph{b)} du théorème",
    "Judged with the remark body as roman (document-wide remark item).")
add(132, "Remarque (18.5.13), condition a″): label and text",
    "label a″) upright; the condition a″) itself is printed italic inside the roman remark (crops p132_s3_app.png)",
    "\\item[a'')] in the italic remark environment ('' gives a closing quotation mark); the condition has no italic "
    "markup of its own", "convention", 6, "high",
    r"\item[a'')] Pour tout polynôme unitaire", r"\item[\textup{a$''$)}] \itshape Pour tout polynôme unitaire",
    "Judged as if the remark body were roman (document-wide remark item): the condition is an italic statement "
    "inside the roman remark; \\itshape lasts to \\end{enumerate} (a″) is the only item). With the current italic "
    "remark the text does not change; the label becomes upright with a double prime.")
add(132, "Remarque (18.5.13) a″): 'produit de deux polynômes unitaires étrangers G_0, H_0'",
    "'étrangers' roman inside the italic condition (crop p132_s3_app.png)", "italic", "convention", 6, "high",
    "unitaires étrangers $G_0$", r"unitaires \textup{étrangers} $G_0$", "")

# ---------------------------------------------------------------- page 133
add(133, "proof of Lemme (18.5.13.1): 'on a nécessairement e″R(t″) = 0 et de même e′S(t′) = 0,'",
    "no comma after the first '= 0' (crop p133_s3_necess_zoom.png)", "$e''R(t'')=0$, et de même",
    "punctuation", None, "high",
    "$e''R(t'')=0$, et de même", "$e''R(t'')=0$ et de même", "")
add(133, "proof of Lemme (18.5.13.1): 'on a aussi G(t) = e′G′(t′) et H(t) = e″H(t″)'",
    "G′(t′): a prime after G (crop p133_s3_Gprime.png)", "$G(t)=e'G(t')$ (silent correction)",
    "misprint_in_print", None, "high",
    "$G(t)=e'G(t')$", "$G(t)=e'G'(t')$",
    "G(t) = e′G(t′)+e″G(t″) = e′G(t′), since e″G(t″) = 0; no G′ is defined. The fix restores the printed G′. No "
    "erratum (Liste 3 covers the earlier parts only).",
    corrected="$G(t)=e'G(t')$")
add(133, "proof of Lemme (18.5.13.1): 'de sorte que, par définition de G et H, R = QH et S = PG'",
    "R = QH et S = PG (crop p133_s3_necess.png)", "same as the print", "misprint_in_print", None, "high",
    None, None,
    "Authors' slip, kept by the TeX. e″R(t″) = 0 means R lies in the kernel G.A[T] of T ↦ t″ (B″ ≅ A[T]/G.A[T], "
    "e″G(t″) = 0), so R is a multiple of G, and S (with e′S(t′) = 0) a multiple of H; G and H are swapped. Check "
    "with F = T(T−1) over a field: e′ = 1−T = −G, e″ = T = H. Correct reading R = PG et S = QH, which keeps the "
    "printed PG+QH = 1+LF that follows (equivalently R = QG, S = PH with QG+PH = 1+LF). No erratum.",
    corrected="$R=PG$ et $S=QH$")
add(133, "'pour voir aussitôt que les conditions a′) et a″) sont équivalentes'",
    "labels italic (crop p133_s3_aprimes.png)", "$a')$, $a'')$", "italics", None, "high",
    "les conditions $a')$ et $a'')$ sont", r"les conditions \emph{a$'$)} et \emph{a$''$)} sont", "")
add(133, "Proposition (18.5.14): '(où r est le radical de A)'",
    "upright parentheses around the italic words (crop p133_s4_ou.png)", "italic parentheses",
    "convention", 6, "high",
    r"(où $\mathfrak r$ est le radical de $A$) est hensélien",
    r"\textup{(}où $\mathfrak r$ est le radical de $A$\textup{)} est hensélien",
    "Parentheses inside italic statements are upright in the print (GLOBAL_ISSUES 96).")
add(133, "proof of (18.5.14): 'Vérifions le critère a′) de (18.5.11)'", "a′) italic (crop p133_s4_crit.png)",
    "$a')$", "italics", None, "high",
    "Vérifions le critère $a')$", r"Vérifions le critère \emph{a$'$)}", "")
add(133, "end of p. 133: page break 133/134 inside '... pour la topologie r-préadique, | qui est aussi'",
    "p. 134 begins mid-sentence with 'qui est aussi' at the left margin, no indent",
    "blank lines before and after \\oldpage[IV-4]{134}", "marker", None, "high",
    r"complet pour la topologie $\mathfrak r$-préadique," + NL + NL,
    r"complet pour la topologie $\mathfrak r$-préadique," + NL,
    "The marker is at the right place. Part 1 of 2: the first p. 134 finding removes the blank line after "
    "\\oldpage[IV-4]{134}; apply both.")

# ---------------------------------------------------------------- page 134
add(134, "top of p. 134: page break 133/134", "p. 134 begins mid-sentence ('qui est aussi la topologie ...')",
    "blank line after \\oldpage[IV-4]{134}", "marker", None, "high",
    r"\oldpage[IV-4]{134}" + NL + NL + "qui est aussi", r"\oldpage[IV-4]{134}" + NL + "qui est aussi",
    "Part 2 of 2 with the last p. 133 finding; both blank lines must go.")
add(134, "Proposition (18.5.15): 'le foncteur B ⇝ B/rB'", "wavy arrow (crop p134_s1_leadsto.png)",
    "\\longmapsto", "symbol", None, "high",
    r"$B\longmapsto B/\mathfrak rB$", r"$B\leadsto B/\mathfrak rB$", "Wavy arrow (\\leadsto), not convention 3.")
add(134, "Remarques (18.5.16) (ii): 'Soient A un anneau noethérien'", "'noethérien' italic "
    "(crop p134_s2_noeth.png)", "upright, no \\emph", "italics", None, "high",
    r"\item[(ii)] Soient $A$ un anneau noethérien", r"\item[(ii)] Soient $A$ un anneau \emph{noethérien}",
    "Judged with the remark body as roman (document-wide remark item).")
add(134, "Remarques (18.5.16) (ii): 'pour la topologie J-préadique (0_I, 7.3.6)'", "bold 0 with subscript I",
    "plain 0", "convention", 2, "high",
    r"préadique ($0_{\mathrm I}$, 7.3.6). Remplaçant", r"préadique ($\mathbf{0}_{\mathrm I}$, 7.3.6). Remplaçant", "")
add(134, "Remarques (18.5.16) (ii): 'que l'on a Idem(A) = lim Idem(A/J^n) pour les applications'",
    "set in the line, and the lim (arrow beneath) has no index (crops p134_s2_lim.png, p134_s2_lim_zoom.png)",
    "displayed, with \\varprojlim_n", "formula", None, "high",
    "que l'on a" + NL + r"  \[" + NL + r"    \operatorname{Idem}(A)=\varprojlim_n\operatorname{Idem}(A/\mathfrak J^n)"
    + NL + r"  \]" + NL + "  pour les applications",
    r"que l'on a $\operatorname{Idem}(A)=\varprojlim\operatorname{Idem}(A/\mathfrak J^n)$ pour les applications",
    "One edit for two differences at the same spot: the formula is inline in the print (GLOBAL_ISSUES 21 pattern), "
    "and its lim carries no index n (GLOBAL_ISSUES 30 pattern; the earlier A = lim (A/J^n) has none either).")
add(134, "Remarques (18.5.16) (ii): 'ψ_nm : Idem(A/J^m) → Idem(A/J^n) restriction des applications canoniques'",
    "'restriction' (singular) (crop p134_s2_lim.png)", "'restrictions' (silent correction)",
    "misprint_in_print", None, "medium",
    "restrictions des applications canoniques", "restriction des applications canoniques",
    "Agreement with 'les applications ψ_nm' calls for the plural (a dropped s); medium: the singular appositive "
    "'restriction de φ' occurs two lines earlier, so it may be the authors' wording. Either way the diplomatic text "
    "takes the printed singular.",
    corrected="restrictions des applications canoniques")
add(134, "Théorème (18.5.17), display: 'Γ(X/S) → Γ(X_s/k(s))'", "bold italic k (crop p134_s3_gamma.png)",
    "plain k", "convention", 1, "high",
    r"\Gamma(X_s/k(s))", r"\Gamma(X_s/\boldsymbol{k}(s))", "")
add(134, "Théorème (18.5.17): '(où X_s = f^{-1}(s)) est surjective'",
    "upright parentheses around 'où X_s = f^{-1}(s)' (crops p134_s3_oparen.png, p134_s3_cparen.png)",
    "italic parentheses", "convention", 6, "high",
    r"(où $X_s=f^{-1}(s)$) est surjective", r"\textup{(}où $X_s=f^{-1}(s)$\textup{)} est surjective",
    "GLOBAL_ISSUES 96.")
add(134, "proof of (18.5.17): 'La donnée d'une k(s)-section de X_s'", "bold italic k (crop p134_s3_ks.png)",
    "plain k", "convention", 1, "high",
    "d'une $k(s)$-section", r"d'une $\boldsymbol{k}(s)$-section", "")
add(134, "proof of (18.5.17): 'au-dessus de s rationnel sur k(s)'", "bold italic k (crop p134_s3_ks.png)",
    "plain k", "convention", 1, "high",
    "rationnel sur $k(s)$", r"rationnel sur $\boldsymbol{k}(s)$", "")
add(134, "proof of (18.5.17): 'on peut supposer que f est étale'", "'étale' italic", "upright",
    "italics", None, "high",
    "que $f$ est étale. Alors", r"que $f$ est \emph{étale}. Alors", "")
add(134, "proof of (18.5.17): 'résulte du critère (18.5.11, b))'",
    "b) italic with italic parenthesis, then the upright closing parenthesis (crop p134_s3_b.png)",
    "$b)$ (upright parenthesis)", "italics", None, "high",
    "du critère (18.5.11, $b)$). (Le lecteur", r"du critère (18.5.11, \emph{b)}). (Le lecteur", "GLOBAL_ISSUES 88.")
add(134, "Remarque (18.5.18), condition d): label and text",
    "label d) upright; the condition d) is printed italic inside the roman remark (crop p134_s4_d.png)",
    "\\item[d)] in the italic remark environment; no italic markup of its own", "convention", 6, "high",
    r"\item[d)] Pour tout morphisme localement de type fini",
    r"\item[\textup{d)}] \itshape Pour tout morphisme localement de type fini",
    "As condition a″) of (18.5.13): judged as if the remark body were roman; \\itshape lasts to \\end{enumerate}. "
    "With the current italic remark only the label changes.")
add(134, "Remarque (18.5.18) d): 'canoniquement isomorphe à k(s) = k'",
    "k(s) bold italic, the k after '=' light (crop p134_s4_kk.png)", "plain $k(s)=k$", "convention", 1, "high",
    "isomorphe à $k(s)=k$", r"isomorphe à $\boldsymbol{k}(s)=k$", "")

# ---------------------------------------------------------------- checks
src = SRC.read_text(encoding="utf-8")
ok = True
work = {}
for d in F:
    fx = d["fix"]
    if not fx:
        continue
    p = d["page"]
    page_text = (R / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    n_page, n_src = page_text.count(fx["old"]), src.count(fx["old"])
    if n_page != 1 or n_src != 1:
        ok = False
        print("NOT UNIQUE", p, n_page, n_src, repr(fx["old"])[:80])
    w = work.setdefault(p, page_text)
    if w.count(fx["old"]) != 1:
        ok = False
        print("ORDER PROBLEM", p, repr(fx["old"])[:80])
    else:
        work[p] = w.replace(fx["old"], fx["new"], 1)
s = src
for d in F:
    fx = d["fix"]
    if fx and s.count(fx["old"]) == 1:
        s = s.replace(fx["old"], fx["new"], 1)
    elif fx:
        ok = False
        print("SOURCE ORDER PROBLEM", d["page"], repr(fx["old"])[:80])
print("blank line already gone before marker 130:", src.count("il suffit que chacune" + NL + r"\oldpage[IV-4]{130}"))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    c[1 if d["kind"] == "convention" else 2 if d["kind"] == "misprint_in_print" else 0] += 1
print("all unique and applicable:" if ok else "PROBLEMS", ok)
print("counts (normal/convention/misprint):", counts, "total", len(F))
(R / "crops_130_134" / "applied_preview.txt").write_text(
    "".join(f"%%%% page {p}\n{w}\n" for p, w in sorted(work.items())), encoding="utf-8")
