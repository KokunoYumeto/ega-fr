# Build findings_060_064.json for EGA IV-4 pp. 60-64 and check every fix.
import json
import sys
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
OUT = RUN / "findings_060_064.json"

G92 = "Sheaf of differentials: italic Omega (\\varOmega) in the print (GLOBAL_ISSUES 92)."
L88 = "Labels in roman text are italic in the print (GLOBAL_ISSUES 88)."
L16 = "Label printed upright inside the italic statement (GLOBAL_ISSUES 16/88)."
R6 = "'(resp.', 'resp.' and ')' are roman inside the italic statement (GLOBAL_ISSUES 96)."
R78 = ("EGA IV's own reference, printed (1.x.y) with old-style 1 and no comma, misread as a reference to EGA I "
       "(GLOBAL_ISSUES 78).")

F = []


def add(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    e = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        e["corrected"] = corrected
    e["note"] = note
    F.append(e)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- page 60
p = 60
add(p, "proof of (17.2.3) (i): 'Ω^1_f est un O_X-Module de type fini'", "italic Ω (page_060_s1.png)",
    "\\Omega (upright)", "font", fx(r"fini, $\Omega_f^1$ est un", r"fini, $\varOmega_f^1$ est un"), G92)
add(p, "proof of (17.2.3) (i): 'et de (0, 20.4.9 et 0, 19.2.1)'", "both 0 bold (page_060_s1.png)", "plain 0 twice",
    "convention", fx(r"(0, 20.4.9 et 0, 19.2.1)", r"(\textbf{0}, 20.4.9 et \textbf{0}, 19.2.1)"),
    "Two occurrences in one edit.", convention=2)
add(p, "proof of (17.2.3) (ii): 'et de (0, 20.5.7)'", "bold 0", "plain 0", "convention",
    fx(r"(0, 20.5.7)", r"(\textbf{0}, 20.5.7)"), convention=2)
add(p, "Corollaire (17.2.4), display f^*(Ω^1_{Y/Z}) → Ω^1_{X/Z}", "italic Ω twice (page_060_s2.png)",
    "\\Omega (upright) twice", "font",
    fx(r"f^*(\Omega_{Y/Z}^1)\longrightarrow\Omega_{X/Z}^1", r"f^*(\varOmega_{Y/Z}^1)\longrightarrow\varOmega_{X/Z}^1"),
    G92)
add(p, "proof of (17.2.4): 'l'on a alors Ω^1_{X/Y}=0 (17.2.1)'", "italic Ω", "\\Omega (upright)", "font",
    fx(r"alors $\Omega_{X/Y}^1=0$ (17.2.1)", r"alors $\varOmega_{X/Y}^1=0$ (17.2.1)"), G92)
add(p, "Proposition (17.2.5): 'le morphisme composé X' →j X →f Y'",
    "f over the second arrow, as j over the first (crop p60_s2_arrows.png)",
    "X'\\xrightarrow{j}X\\to Y: second arrow without its label", "formula",
    fx(r"X'\xrightarrow{j}X\to Y$", r"X'\xrightarrow{j}X\xrightarrow{f}Y$"),
    "The parentheses of '(où j est l'injection canonique)' are italic in the print (crop p60_s2_paren.png): no change there.")
add(p, "Proposition (17.2.5): 'la suite de O_{X'}-Modules (16.4.21)'", "reference upright (crop p60_s2_prop5.png)",
    "italic (inside the italic statement)", "convention",
    fx(r"Modules (16.4.21)", r"Modules \textup{(16.4.21)}"), convention=6)
add(p, "Proposition (17.2.5), display (17.2.5.1)", "italic Ω twice (crop p60_s2_prop5.png)",
    "\\Omega (upright) twice", "font",
    fx(r"\Omega_{X/Y}^1\otimes_{\sh{O}_X}\sh{O}_{X'}\longrightarrow\Omega_{X'/Y}^1",
       r"\varOmega_{X/Y}^1\otimes_{\sh{O}_X}\sh{O}_{X'}\longrightarrow\varOmega_{X'/Y}^1"), G92)
add(p, "Proposition (17.2.5): 'des homomorphismes de (17.2.5.1) forment'", "reference upright (crop p60_s2_prop5.png)",
    "italic (inside the italic statement)", "convention",
    fx(r"de (17.2.5.1) forment", r"de \textup{(17.2.5.1)} forment"), convention=6)
add(p, "Proposition (17.2.5), end: 'forment une suite exacte et scindée.'",
    "'scindée' roman (emphasized) inside the italic statement (crop p60_s2_prop5.png)",
    "italic like the rest of the statement", "italics",
    fx(r"exacte et scindée.", r"exacte et \emph{scindée}."), "As in (17.2.3) on p. 59.")
add(p, "proof of (17.2.5): 'la conclusion découle de (0, 20.5.14)'", "bold 0 (crop p60_s3_frak.png)", "plain 0",
    "convention", fx(r"(0, 20.5.14)", r"(\textbf{0}, 20.5.14)"), convention=2)
add(p, "Proposition (17.2.6), label a)", "upright 'a)' (crop p60_s3_labels.png)",
    "italic (inside the italic statement)", "convention", fx(r"\item[a)]", r"\item[\textup{a)}]"), L16, convention=6)
add(p, "Proposition (17.2.6), label b)", "upright 'b)' (crop p60_s3_labels.png)",
    "italic (inside the italic statement)", "convention", fx(r"\item[b)]", r"\item[\textup{b)}]"), L16, convention=6)
add(p, "Proposition (17.2.6), label c)", "upright 'c)' (crop p60_s3_labels.png)",
    "italic (inside the italic statement)", "convention", fx(r"\item[c)]", r"\item[\textup{c)}]"), L16, convention=6)
add(p, "Proposition (17.2.6) c): 'est vide ou k(y)-isomorphe'", "bold italic k (crop p60_s3_c.png)", "plain k",
    "convention", fx(r"$k(y)$-isomorphe", r"$\boldsymbol{k}(y)$-isomorphe"), convention=1)
add(p, "Proposition (17.2.6) c): 'à Spec(k(y))'", "bold italic k (crop p60_s3_c.png)", "plain k", "convention",
    fx(r"à $\Spec(k(y))$", r"à $\Spec(\boldsymbol{k}(y))$"), convention=1)
add(p, "Proposition (17.2.6) c): '(autrement dit, est réduite à un seul point z tel que'",
    "the whole parenthesis is roman inside the italic statement, 'isomorphisme' italic (crop p60_s3_c.png)",
    "italic (inside the italic statement)", "convention",
    fx(r"(autrement dit, est réduite à un seul point $z$ tel que",
       r"\textup{(autrement dit, est réduite à un seul point $z$ tel que}"),
    "First half of the roman parenthesis; the formula k(y) → O_z/m_y O_z between the halves is unaffected. "
    "The next-but-one entry closes the parenthesis. Independent of the k(y) entry between them.", convention=6)
add(p, "Proposition (17.2.6) c): 'k(y) → O_z/m_y O_z'", "bold italic k (crop p60_s3_c.png)", "plain k",
    "convention", fx(r"$k(y)\to\sh{O}_z", r"$\boldsymbol{k}(y)\to\sh{O}_z"), convention=1)
add(p, "Proposition (17.2.6) c), end of the parenthesis: 'soit un isomorphisme).'",
    "'soit un' and ')' roman, 'isomorphisme' italic (crop p60_s3_c.png)", "all italic", "convention",
    fx(r"soit un isomorphisme).", r"\textup{soit un \emph{isomorphisme})}."),
    "Second half of the roman parenthesis (see the entry two above); \\emph inside \\textup gives the printed "
    "italic of 'isomorphisme'.", convention=6)
add(p, "proof of (17.2.6): 'Le fait que a) entraîne c) résulte de (8.11.5.1)'",
    "a) and c) italic, parenthesis included (crop p60_s3_proof.png)", "upright", "italics",
    fx(r"Le fait que a) entraîne c) résulte", r"Le fait que \emph{a)} entraîne \emph{c)} résulte"), L88)
add(p, "proof of (17.2.6): 'Il est clair que c) entraîne que f est radiciel'", "c) italic (crop p60_s3_proof.png)",
    "upright", "italics", fx(r"clair que c) entraîne", r"clair que \emph{c)} entraîne"), L88)
add(p, "proof of (17.2.6): 'il résulte aussi de c) que'", "c) italic (crop p60_s3_proof.png)", "upright",
    "italics", fx(r"aussi de c) que", r"aussi de \emph{c)} que"), L88)
add(p, "proof of (17.2.6): 'que Ω^1_{X/Y}=0, ce qui prouvera'", "italic Ω (crop p60_s3_proof.png)",
    "\\Omega (upright)", "font", fx(r"$\Omega_{X/Y}^1=0$, ce qui", r"$\varOmega_{X/Y}^1=0$, ce qui"), G92)
add(p, "proof of (17.2.6): 'ce qui prouvera que c) entraîne b) (17.2.1)'", "c) and b) italic (crop p60_s3_proof.png)",
    "upright", "italics", fx(r"que c) entraîne b)", r"que \emph{c)} entraîne \emph{b)}"), L88)
add(p, "proof of (17.2.6): 'le O_X-Module Ω^1_{X/Y} est quasi-cohérent'", "italic Ω (crop p60_s3_proof.png)",
    "\\Omega (upright)", "font",
    fx(r"-Module $\Omega_{X/Y}^1$ est quasi-cohérent", r"-Module $\varOmega_{X/Y}^1$ est quasi-cohérent"), G92)
add(p, "proof of (17.2.6): 'Il résulte donc de (I, 9.1.13.1)'", "bold I (page_060_s3.png)", "plain I",
    "convention", fx(r"(I, 9.1.13.1)", r"(\textbf{I}, 9.1.13.1)"), convention=2)
add(p, "proof of (17.2.6): 'pour que (Ω^1_{X/Y})_x=0'", "italic Ω", "\\Omega (upright)", "font",
    fx(r"pour que $(\Omega_{X/Y}^1)_x=0$", r"pour que $(\varOmega_{X/Y}^1)_x=0$"), G92)
add(p, "proof of (17.2.6): 'si l'on pose Y_1=Spec(k(y))'", "bold italic k (page_060_s4.png)", "plain k",
    "convention", fx(r"$Y_1=\Spec(k(y))$", r"$Y_1=\Spec(\boldsymbol{k}(y))$"), convention=1)
add(p, "proof of (17.2.6): 'on ait (Ω^1_{X_1/Y_1})_x=0'", "italic Ω (page_060_s4.png)", "\\Omega (upright)", "font",
    fx(r"$(\Omega_{X_1/Y_1}^1)_x=0$", r"$(\varOmega_{X_1/Y_1}^1)_x=0$"), G92)
add(p, "proof of (17.2.6): 'en vertu de l'hypothèse c) (17.1.3)'", "c) italic (crop p60_s4_mid.png)", "upright",
    "italics", fx(r"l'hypothèse c)", r"l'hypothèse \emph{c)}"), L88)
add(p, "proof of (17.2.6): 'Prouvons enfin que b) entraîne a);'", "b) and a) italic (crop p60_s4_mid.png)",
    "upright", "italics", fx(r"enfin que b) entraîne a);", r"enfin que \emph{b)} entraîne \emph{a)};"), L88)
add(p, "proof of (17.2.6): 'puisque f est radiciel, g est surjectif (1.8.7.1)'",
    "'(1.8.7.1)': old-style 1, periods, no comma, no bold (crop p60_s4_ref.png)", "(I, 8.7.1)", "number",
    fx(r"surjectif (I, 8.7.1);", r"surjectif (1.8.7.1);"), R78)
add(p, "proof of (17.2.6): 'd'autre part, Ω^1_{X/Y} est par définition'", "italic Ω (crop p60_s4_mid.png)",
    "\\Omega (upright)", "font",
    fx(r"d'autre part, $\Omega_{X/Y}^1$ est par définition", r"d'autre part, $\varOmega_{X/Y}^1$ est par définition"),
    G92)
add(p, "proof of (17.2.6): 'le faisceau conormal 𝒢r_1(g) de l'immersion g'",
    "script G with italic r (crop p60_s4_mid.png)", "\\mathop{Gr}\\nolimits: roman Gr", "symbol",
    fx(r"$\mathop{Gr}\nolimits_1(g)$ de l'immersion", r"$\mathscr{G}r_1(g)$ de l'immersion"),
    "Written as the edition's other 𝒢r (\\mathscr{G}r, ega4-16).")
add(p, "page break 60/61 inside the sentence 'dire que f est formellement non ramifié signifie donc que | 𝒢r_1(g)=0'",
    "p. 60 ends 'signifie donc que', p. 61 begins '𝒢r_1(g)=0 (17.2.1).' in the same paragraph "
    "(page_060_s4.png, page_061_s1.png)",
    "blank line before \\oldpage[IV-4]{61}: paragraph break the print lacks", "marker",
    fx("signifie donc que\n\n", "signifie donc que\n"),
    "The marker itself is at the right place; only the blank line at the end of page_060.tex goes "
    "(GLOBAL_ISSUES 20).")

# ---------------------------------------------------------------- page 61
p = 61
add(p, "end of the proof of (17.2.6), l. 1: '𝒢r_1(g)=0 (17.2.1)'", "script G with italic r (crop p61_s1_top.png)",
    "\\mathop{Gr}\\nolimits: roman Gr", "symbol",
    fx(r"$\mathop{Gr}\nolimits_1(g)=0$ (17.2.1)", r"$\mathscr{G}r_1(g)=0$ (17.2.1)"),
    "Written as the edition's other 𝒢r (\\mathscr{G}r).")
add(p, "end of the proof of (17.2.6): 'g est localement de présentation finie (1.4.3.1)'",
    "'(1.4.3.1)': old-style 1, periods, no comma, no bold (crop p61_s1_ref1.png)", "(I, 4.3.1)", "number",
    fx(r"finie (I, 4.3.1); donc", r"finie (1.4.3.1); donc"), R78)
add(p, "end of the proof of (17.2.6): 'l'hypothèse 𝒢r_1(g)=0 entraîne'", "script G with italic r (crop p61_s1_top.png)",
    "\\mathop{Gr}\\nolimits: roman Gr", "symbol",
    fx(r"l'hypothèse $\mathop{Gr}\nolimits_1(g)=0$", r"l'hypothèse $\mathscr{G}r_1(g)=0$"))
add(p, "end of the proof of (17.2.6): 'donc f est un monomorphisme (I, 5.3.8)'", "bold I (crop p61_s1_top.png)",
    "plain I", "convention", fx(r"(I, 5.3.8)", r"(\textbf{I}, 5.3.8)"), convention=2)
add(p, "heading 17.3: 'Morphismes lisses, morphismes non ramifiés, morphismes étales.'", "full stop after the title",
    "no full stop", "punctuation",
    fx(r"\subsection{Morphismes lisses, morphismes non ramifiés, morphismes étales}",
       r"\subsection{Morphismes lisses, morphismes non ramifiés, morphismes étales.}"), "GLOBAL_ISSUES 43/58.")
add(p, "Définition (17.3.1): 'est lisse (resp. non ramifié, ou net (1)'",
    "'lisse', 'non ramifié', 'net' italic like the statement; '(resp.' and 'ou' roman (crops p61_s1_def_a.png, "
    "p61_s1_def_b.png)",
    "\\emph{lisse}, \\emph{non ramifié}, \\emph{net} come out upright; '(resp.' and 'ou' italic", "convention",
    fx(r"est \emph{lisse} (resp. \emph{non ramifié}, ou \emph{net}\footnote{",
       r"est lisse \textup{(resp.}\ non ramifié, \textup{ou} net\footnote{"),
    "Unlike (17.1.1), this definition prints the defined words italic and only the connectives roman. "
    "'ou net' and 'ou' look slightly heavier than their neighbours (also in the next paragraph); measured stem widths "
    "are those of the normal founts (inking), so not reported.", convention=6)
add(p, "Définition (17.3.1), footnote (1): 'en conflit avec (0, 19.10).'", "bold 0 (page_061_s4.png)", "plain 0",
    "convention", fx(r"(0, 19.10)", r"(\textbf{0}, 19.10)"), convention=2)
add(p, "Définition (17.3.1): 'net (1) resp. étale)': no comma after the footnote call",
    "'net (¹) resp. étale)' (crop p61_s1_def_b.png)", "'\\footnote{...}, resp.': comma (silent correction)",
    "misprint_in_print", fx(r".},", r".}"),
    "The parallel lists have the comma: '(resp. formellement non ramifié, resp. formellement étale)' in the same "
    "definition and '(resp. non ramifié ou net, resp. étale)' in the next paragraph; the corrected reading keeps the "
    "comma after the footnote call ('.},' at the end of the footnote). The 'old' is the end of the footnote and is "
    "independent of the other edits of this definition. No erratum found in Liste 3.",
    confidence="medium", corrected=r".},")
add(p, "Définition (17.3.1): 'resp. étale) s'il est localement'",
    "'resp.' and ')' roman, 'étale' italic (crop p61_s1_def_b.png)",
    "\\emph{étale} upright, 'resp.' and ')' italic", "convention",
    fx(r"resp. \emph{étale}) s'il", r"\textup{resp.}\ étale\textup{)} s'il"),
    "Second part of the convention-6 edit of the first list of (17.3.1) (the first part ends at '\\footnote{'); "
    "independent of the two footnote-end edits.", convention=6)
add(p, "Définition (17.3.1), end: 'formellement lisse (resp. formellement non ramifié, resp. formellement étale).'",
    "'(resp.', 'resp.' and ')' roman (crop p61_s1_def.png)", "italic", "convention",
    fx(r"formellement lisse (resp. formellement non ramifié, resp. formellement étale).",
       r"formellement lisse \textup{(resp.}\ formellement non ramifié, \textup{resp.}\ formellement étale\textup{)}."),
    R6, convention=6)
add(p, "after (17.3.1): '... resp. étale) sur Y.'", "'sur' italic (crop p61_s1_ondit_z.png)", "'sur' upright",
    "italics", fx(r"\emph{étale}) sur $Y$.", r"\emph{étale}) \emph{sur} $Y$."), "As in the sentence after (17.1.1).")
add(p, "Remarques (17.3.2) (i), display: 'Y' ⇝ Hom_Y(Y', X)'", "wavy arrow (crop p61_s2_leadsto.png)",
    "\\longmapsto", "symbol", fx(r"Y'\longmapsto\Hom_Y(Y',X)", r"Y'\leadsto\Hom_Y(Y',X)"),
    "Wavy arrow in the print (GLOBAL_ISSUES 33), as in (17.1.2, (iii)) on p. 57.")
add(p, "Remarques (17.3.2) (ii): 'une A-algèbre de présentation finie (1.4.6)'",
    "'(1.4.6)': old-style 1, periods, no comma, no bold (crop p61_s3_ref146.png)", "(I, 4.4.6)", "number",
    fx(r"(I, 4.4.6)", r"(1.4.6)"), R78)
add(p, "Remarques (17.3.2) (iii): 'localement de présentation finie (1.4.2)'",
    "'(1.4.2)': old-style 1, periods, no comma, no bold (crop p61_s3_ref142.png)", "(I, 4.4.2)", "number",
    fx(r"(I, 4.4.2)", r"(1.4.2)"), R78)
add(p, "Proposition (17.3.3), label (i)", "upright '(i)' (crop p61_s3_prop3.png)",
    "italic (inside the italic statement)", "convention",
    fx(r"\item[(i)] Une immersion", r"\item[\textup{(i)}] Une immersion"), L16, convention=6)
add(p, "Proposition (17.3.3), label (ii)", "upright '(ii)' (crop p61_s3_prop3.png)",
    "italic (inside the italic statement)", "convention",
    fx(r"\item[(ii)] Le composé", r"\item[\textup{(ii)}] Le composé"), L16, convention=6)
add(p, "Proposition (17.3.3) (ii): 'lisses (resp. non ramifiés, resp. étales) est lisse (resp. non ramifié, resp. étale).'",
    "'(resp.', 'resp.' and ')' roman, twice (crop p61_s3_prop3.png)", "italic", "convention",
    fx(r"lisses (resp. non ramifiés, resp. étales) est lisse (resp. non ramifié, resp. étale).",
       r"lisses \textup{(resp.}\ non ramifiés, \textup{resp.}\ étales\textup{)} est lisse \textup{(resp.}\ non ramifié, "
       r"\textup{resp.}\ étale\textup{)}."), R6, convention=6)
add(p, "Proposition (17.3.3), label (iii)", "upright '(iii)' (page_061_s3.png)", "italic (inside the italic statement)",
    "convention", fx(r"\item[(iii)] Si", r"\item[\textup{(iii)}] Si"), L16, convention=6)
add(p, "Proposition (17.3.3) (iii): 'S-morphisme lisse (resp. non ramifié, resp. étale), il en est'",
    "'(resp.', 'resp.' and ')' roman (crop p61_s3_iii_paren.png)", "italic", "convention",
    fx(r"lisse (resp. non ramifié, resp. étale), il en est de même de $f_{(S')}",
       r"lisse \textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)}, il en est de même de $f_{(S')}"),
    R6, convention=6)
add(p, "Proposition (17.3.3), label (iv)", "upright '(iv)' (crop p61_s4_iv.png)", "italic (inside the italic statement)",
    "convention", fx(r"\item[(iv)]", r"\item[\textup{(iv)}]"), L16, convention=6)
add(p, "Proposition (17.3.3) (iv): 'S-morphismes lisses (resp. non ramifiés, resp. étales), il en est'",
    "'(resp.', 'resp.' and ')' roman (crops p61_s4_iv.png, p61_s4_iv_paren.png)", "italic", "convention",
    fx(r"lisses (resp. non ramifiés, resp. étales), il en est de même de $f\times_S g",
       r"lisses \textup{(resp.}\ non ramifiés, \textup{resp.}\ étales\textup{)}, il en est de même de $f\times_S g"),
    R6, convention=6)

# ---------------------------------------------------------------- page 62
p = 62
add(p, "Proposition (17.3.3), label (v)", "upright '(v)' (page_062_s1.png)", "italic (inside the italic statement)",
    "convention", fx(r"\item[(v)]", r"\item[\textup{(v)}]"), L16, convention=6)
add(p, "proof of (17.3.3): 'Cela résulte aussitôt de (1.4.3) et de (17.1.3).'",
    "'(1.4.3)': old-style 1, periods, no comma, no bold (crop p62_s1_ref143.png)", "(I, 4.3)", "number",
    fx(r"aussitôt de (I, 4.3) et de", r"aussitôt de (1.4.3) et de"), R78)
add(p, "Proposition (17.3.4): 'si g∘f est lisse (resp. non ramifié, resp. étale), il en est de même de f.'",
    "'(resp.', 'resp.' and ')' roman (crop p62_s1_p34.png)", "italic", "convention",
    fx(r"est lisse (resp. non ramifié, resp. étale), il en est de même de $f$.",
       r"est lisse \textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)}, il en est de même de $f$."),
    R6, convention=6)
add(p, "proof of (17.3.4): 'il en est de même de f (1.4.3, (v))'",
    "'(1.4.3, (v))': old-style 1, no bold (crop p62_s1_ref143v.png)", "(I, 4.4.3, (v))", "number",
    fx(r"de $f$ (I, 4.4.3, (v)); la conclusion", r"de $f$ (1.4.3, (v)); la conclusion"), R78)
add(p, "Corollaire (17.3.5): 'pour que f soit lisse (resp. non ramifié, resp. étale), il faut et il suffit'",
    "'(resp.', 'resp.' and ')' roman (crop p62_s1_c35.png)", "italic", "convention",
    fx(r"soit lisse (resp. non ramifié, resp. étale), il faut et il suffit",
       r"soit lisse \textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)}, il faut et il suffit"),
    R6, convention=6)
add(p, "proof of (17.3.5): 'Cela résulte de (17.3.4) et de (17.3.3, (ii)).'", "(ii) (crop p62_s2_ref1733.png)",
    "(17.3.3, (iii))", "number", fx(r"(17.3.3, (iii)).", r"(17.3.3, (ii))."),
    "The print is right: f lisse and g étale give g∘f lisse by the composition statement (17.3.3, (ii)); "
    "(iii) is base change.")
add(p, "Proposition (17.3.6): 'l'homomorphisme canonique (16.4.19)'", "reference upright (page_062_s2.png)",
    "italic (inside the italic statement)", "convention",
    fx(r"canonique (16.4.19)", r"canonique \textup{(16.4.19)}"), convention=6)
add(p, "Proposition (17.3.6), display f^*(Ω^1_{Y/S}) → Ω^1_{X/S}", "italic Ω twice (page_062_s2.png)",
    "\\Omega (upright) twice", "font",
    fx(r"f^*(\Omega_{Y/S}^1)\longrightarrow\Omega_{X/S}^1", r"f^*(\varOmega_{Y/S}^1)\longrightarrow\varOmega_{X/S}^1"),
    G92)
add(p, "proof of (17.3.6): 'localement de présentation finie (1.4.3, (v)), la proposition'",
    "'(1.4.3, (v))': old-style 1, no bold (page_062_s2.png)", "(I, 4.4.3, (v))", "number",
    fx(r"finie (I, 4.4.3, (v)), la proposition", r"finie (1.4.3, (v)), la proposition"), R78)
add(p, "Définition (17.3.7): 'f est lisse (resp. non ramifié, resp. étale) en un point x∈X'",
    "'lisse', 'non ramifié', 'étale', 'en un point' italic like the statement; '(resp.', 'resp.' and ')' roman "
    "(crop p62_s2_def7.png)",
    "\\emph{lisse}, \\emph{non ramifié}, \\emph{étale}, \\emph{en un point} come out upright; '(resp.' etc. italic",
    "convention",
    fx(r"est \emph{lisse} (resp. \emph{non ramifié}, resp. \emph{étale}) \emph{en un point} $x\in X$",
       r"est lisse \textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)} en un point $x\in X$"),
    "As in (17.3.1): the defined words are not set off, the connectives are roman.", convention=6)
add(p, "Définition (17.3.7): 'soit un morphisme lisse (resp. non ramifié, resp. étale) de U dans Y'",
    "'(resp.', 'resp.' and ')' roman (crop p62_s2_def7.png)", "italic", "convention",
    fx(r"soit un morphisme lisse (resp. non ramifié, resp. étale) de $U$",
       r"soit un morphisme lisse \textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)} de $U$"),
    R6, convention=6)
add(p, "after (17.3.7): 'On dit encore alors que X est lisse (resp. non ramifié, resp. étale) sur Y au point x.'",
    "'lisse', 'non ramifié', 'étale', 'sur' and 'au point' italic (crop p62_s2_def7.png)", "all upright", "italics",
    fx(r"$X$ est lisse (resp. non ramifié, resp. étale) sur $Y$ au point $x$.",
       r"$X$ est \emph{lisse} (resp. \emph{non ramifié}, resp. \emph{étale}) \emph{sur} $Y$ \emph{au point} $x$."),
    "Five italic words in one edit.")
add(p, "Proposition (17.3.8): 'le préschéma fibré vectoriel V(ℰ) (II, 1.7.8)'",
    "bold II; parentheses and numbers upright (crop p62_s3_prop8.png)", "plain II, italic reference", "convention",
    fx(r"(II, 1.7.8)", r"\textup{(\textbf{II}, 1.7.8)}"),
    "One edit for convention 2 (bold II) and convention 6 (upright reference inside the italic statement).",
    convention=2)
add(p, "proof of (17.3.8): 'pour les topologies discrètes (0, 19.3.2)'", "bold 0 (page_062_s3.png)", "plain 0",
    "convention", fx(r"(0, 19.3.2)", r"(\textbf{0}, 19.3.2)"), convention=2)
add(p, "Corollaire (17.3.9): 'Sous les hypothèses de (17.3.8), le préschéma'", "reference upright (crop p62_s3_cor9.png)",
    "italic (inside the italic statement)", "convention",
    fx(r"de (17.3.8), le", r"de \textup{(17.3.8)}, le"), convention=6)
add(p, "Corollaire (17.3.9): 'P(ℰ) (II, 4.1.1)'", "bold II; parentheses and numbers upright (crop p62_s3_cor9.png)",
    "plain II, italic reference", "convention", fx(r"(II, 4.1.1)", r"\textup{(\textbf{II}, 4.1.1)}"),
    "One edit for convention 2 (bold II) and convention 6. The P of P(ℰ) and P^r is bold UPRIGHT here "
    "(crops p62_s3_P.png, p62_s3_Pr.png): \\mathbf{P} is right, no convention-10 change.", convention=2)
add(p, "proof of (17.3.9): 'On sait alors (II, 2.3.14)'", "bold II (page_062_s4.png)", "plain II", "convention",
    fx(r"(II, 2.3.14)", r"(\textbf{II}, 2.3.14)"), convention=2)
add(p, "proof of (17.3.9): 'la définition de S_(f) (II, 2.2.1)'", "bold II (page_062_s4.png)", "plain II",
    "convention", fx(r"(II, 2.2.1)", r"(\textbf{II}, 2.2.1)"), convention=2)

# ---------------------------------------------------------------- page 63
p = 63
add(p, "heading 17.4: 'Caractérisations des morphismes non ramifiés.'", "full stop after the title", "no full stop",
    "punctuation",
    fx(r"\subsection{Caractérisations des morphismes non ramifiés}",
       r"\subsection{Caractérisations des morphismes non ramifiés.}"), "GLOBAL_ISSUES 43/58.")
for lab, crop in (("a)", "page_063_s1.png"), ("b)", "page_063_s1.png")):
    add(p, "Théorème (17.4.1), label " + lab, "upright '" + lab + "' (" + crop + ")",
        "italic (inside the italic statement)", "convention",
        fx("\\item[" + lab + "]", "\\item[\\textup{" + lab + "}]"), L16, convention=6)
LP = (" The printed prime is a wedge-shaped prime (crop p63_s1_bprime_z.png): written b$'$ as in the edition's "
      "fixed labels of (17.4.2) and (17.4.4) on p. 65.")
add(p, "Théorème (17.4.1), label b')", "upright \"b')\" (crop p63_s1_bprime_z.png)",
    "\\item[b')]: italic inside the italic statement", "convention",
    fx(r"\item[b')]", r"\item[\textup{b$'$)}]"), L16 + LP, convention=6)
add(p, "Théorème (17.4.1) b'): 'l'homomorphisme θ^♯_x : O_{Z,z} → O_{X,x}'",
    "subscript x under the sharp (crop p63_s1_theta.png)", "\\theta_z^\\#: subscript z", "formula",
    fx(r"$z=\psi(x)$, l'homomorphisme $\theta_z", r"$z=\psi(x)$, l'homomorphisme $\theta_x"),
    "θ^♯_x : O_{Z,ψ(x)} → O_{X,x} is EGA's notation for the stalk map of Δ_f at x; the print is right. Adjacent to, "
    "but independent of, the sharp-sign entry that follows.")
add(p, "Théorème (17.4.1) b'): sharp sign of θ^♯_x", "♯ (crop p63_s1_theta.png)", "^\\# (typesets #)", "convention",
    fx(r"^\#:\sh{O}_{Z,z}\to\sh{O}_{X,x}", r"^\sharp:\sh{O}_{Z,z}\to\sh{O}_{X,x}"), convention=9)
add(p, "Théorème (17.4.1), label b'')", "upright \"b'')\" (page_063_s1.png)", "italic (inside the italic statement)",
    "convention", fx(r"\item[b'')]", r"\item[\textup{b$''$)}]"), L16 + LP, convention=6)
add(p, "Théorème (17.4.1), label c)", "upright 'c)' (crop p63_s2_lbls.png)", "italic (inside the italic statement)",
    "convention", fx(r"\item[c)]", r"\item[\textup{c)}]"), L16, convention=6)
add(p, "Théorème (17.4.1) c): 'On a (Ω^1_{X/Y})_x=0.'", "italic Ω (crop p63_s2_lbls.png)", "\\Omega (upright)",
    "font", fx(r"On a $(\Omega^1_{X/Y})_x=0$", r"On a $(\varOmega^1_{X/Y})_x=0$"), G92)
add(p, "Théorème (17.4.1), label d)", "upright 'd)' (crop p63_s2_lbls.png)", "italic (inside the italic statement)",
    "convention", fx(r"\item[d)]", r"\item[\textup{d)}]"), L16, convention=6)
add(p, "Théorème (17.4.1) d): 'Le k(y)-préschéma f^{-1}(y)'", "bold italic k (crop p63_s2_lbls.png)", "plain k",
    "convention", fx(r"Le $k(y)$-préschéma", r"Le $\boldsymbol{k}(y)$-préschéma"), convention=1)
add(p, "Théorème (17.4.1) d): 'non ramifié sur k(y) au point x'", "bold italic k", "plain k", "convention",
    fx(r"sur $k(y)$ au point", r"sur $\boldsymbol{k}(y)$ au point"), convention=1)
add(p, "Théorème (17.4.1), label d')", "upright \"d')\" (crop p63_s2_lbls.png)", "italic (inside the italic statement)",
    "convention", fx(r"\item[d')]", r"\item[\textup{d$'$)}]"), L16 + LP, convention=6)
add(p, "Théorème (17.4.1) d'): '(autrement dit (Err_III, 20), le morphisme f est quasi-fini au point x)'",
    "'(autrement dit (Err_III, 20), le morphisme f est' and ')' roman, 'Err' bold with a light subscript III, "
    "'quasi-fini au point x' italic (crops p63_s2_dprime.png, p63_s2_err.png, p63_s2_quasifini.png)",
    "all italic (statement environment); plain 'Err'", "convention",
    fx(r"(autrement dit (Err$_{\mathrm{III}}$, 20), le morphisme $f$ est quasi-fini au point $x$)",
       r"\textup{(autrement dit (\textbf{Err}$_{\mathrm{III}}$, 20), le morphisme $f$ est \emph{quasi-fini au point} $x$)}"),
    "One edit for two differences: the roman clause inside the italic statement (convention 6, with \\emph for the "
    "italic 'quasi-fini au point'), and the bold 'Err' (font; the edition writes \\mathbf{Err} / \\textbf{Err} "
    "elsewhere).", convention=6)
add(p, "Théorème (17.4.1) d'): 'extension séparable de k(y)'", "bold italic k (crop p63_s2_dprime.png)", "plain k",
    "convention", fx(r"extension séparable de $k(y)$", r"extension séparable de $\boldsymbol{k}(y)$"), convention=1)
add(p, "Théorème (17.4.1), label d'')", "upright \"d'')\" (crop p63_s2_lbls.png)",
    "italic (inside the italic statement)", "convention", fx(r"\item[d'')]", r"\item[\textup{d$''$)}]"), L16 + LP,
    convention=6)
add(p, "Théorème (17.4.1) d''): 'extension finie séparable de k(y)'", "bold italic k (crop p63_s2_lbls.png)",
    "plain k", "convention", fx(r"finie séparable de $k(y)$", r"finie séparable de $\boldsymbol{k}(y)$"),
    convention=1)
add(p, "Théorème (17.4.1), label e)", "upright 'e)' (crop p63_s2_lbls.png)", "italic (inside the italic statement)",
    "convention", fx(r"\item[e)]", r"\item[\textup{e)}]"), L16, convention=6)
add(p, "proof of (17.4.1): 'le O_X-Module Ω^1_{X/Y} est de type fini (16.3.9)'", "italic Ω (crop p63_s2_proof.png)",
    "\\Omega (upright)", "font",
    fx(r"-Module $\Omega^1_{X/Y}$ est de type fini (16.3.9)", r"-Module $\varOmega^1_{X/Y}$ est de type fini (16.3.9)"),
    G92)
add(p, "proof of (17.4.1): 'dire que (Ω^1_{X/Y})_x=0 ou'", "italic Ω (crop p63_s2_proof.png)", "\\Omega (upright)",
    "font", fx(r"que $(\Omega^1_{X/Y})_x=0$ ou", r"que $(\varOmega^1_{X/Y})_x=0$ ou"), G92)
add(p, "proof of (17.4.1): 'tel que Ω^1_{X/Y}|U=0'", "italic Ω (crop p63_s2_proof.png)", "\\Omega (upright)", "font",
    fx(r"tel que $\Omega^1_{X/Y}|U=0$", r"tel que $\varOmega^1_{X/Y}|U=0$"), G92)
add(p, "proof of (17.4.1): 'cela prouve l'équivalence de a) et c).'", "a) and c) italic (crop p63_s2_proof.png)",
    "upright", "italics", fx(r"l'équivalence de a) et c).", r"l'équivalence de \emph{a)} et \emph{c)}."), L88)
add(p, "proof of (17.4.1): 'on a (Ω^1_{X/Y})_x = Ω^1_{B/A} (16.4.15)'",
    "first Ω italic (sheaf), Ω^1_{B/A} upright (module) (crop p63_s2_proof.png)", "both \\Omega upright", "font",
    fx(r"on a $(\Omega^1_{X/Y})_x=\Omega^1_{B/A}$", r"on a $(\varOmega^1_{X/Y})_x=\Omega^1_{B/A}$"),
    "Only the sheaf changes; the module Ω^1_{B/A} stays upright as printed (GLOBAL_ISSUES 95).")
add(p, "proof of (17.4.1): 'et l'équivalence de c) et e) résulte'", "c) and e) italic (page_063_s3.png)", "upright",
    "italics", fx(r"l'équivalence de c) et e)", r"l'équivalence de \emph{c)} et \emph{e)}"), L88)
add(p, "proof of (17.4.1): 'résulte donc de (0, 20.7.4)'", "bold 0 (page_063_s3.png)", "plain 0", "convention",
    fx(r"(0, 20.7.4)", r"(\textbf{0}, 20.7.4)"), convention=2)
add(p, "proof of (17.4.1): 'Comme d') ne fait intervenir'", "d') italic (crop p63_s3_labels.png)", "upright",
    "italics", fx(r"Comme d') ne fait", r"Comme \emph{d')} ne fait"), L88)
add(p, "proof of (17.4.1): 'du morphisme X_y → Spec(k(y))'", "bold italic k (crop p63_s3_labels.png)", "plain k",
    "convention", fx(r"X_y\to\Spec(k(y))$", r"X_y\to\Spec(\boldsymbol{k}(y))$"), convention=1)
add(p, "proof of (17.4.1): 'l'équivalence de a) et d') entraînera'", "a) and d') italic (crop p63_s3_labels.png)",
    "upright", "italics",
    fx(r"l'équivalence de a) et d') entraînera", r"l'équivalence de \emph{a)} et \emph{d')} entraînera"), L88)
add(p, "proof of (17.4.1): 'celle de d) et d'). D'autre part d') et d'') sont équivalentes'",
    "d), d'), d'), d'') italic (crop p63_s3_labels.png)", "upright", "italics",
    fx(r"celle de d) et d'). D'autre part d') et d'') sont",
       r"celle de \emph{d)} et \emph{d')}. D'autre part \emph{d')} et \emph{d'')} sont"), L88)
add(p, "proof of (17.4.1): 'est une k(y)-algèbre finie'", "bold italic k (crop p63_s3_labels.png)", "plain k",
    "convention", fx(r"une $k(y)$-algèbre", r"une $\boldsymbol{k}(y)$-algèbre"), convention=1)
add(p, "proof of (17.4.1): 'X_y est un k(y)-préschéma localement de type fini'", "bold italic k (crop p63_s3_labels.png)",
    "plain k", "convention", fx(r"un $k(y)$-préschéma", r"un $\boldsymbol{k}(y)$-préschéma"), convention=1)
add(p, "proof of (17.4.1): 'localement de type fini (I, 6.4.4)'", "bold I (crop p63_s3_labels.png)", "plain I",
    "convention", fx(r"(I, 6.4.4)", r"(\textbf{I}, 6.4.4)"), convention=2)
add(p, "proof of (17.4.1): 'Prouvons maintenant l'équivalence de b) et b').'", "b) and b') italic (page_063_s3.png)",
    "upright", "italics", fx(r"l'équivalence de b) et b').", r"l'équivalence de \emph{b)} et \emph{b')}."), L88)
add(p, "proof of (17.4.1): 'le noyau 𝔍 est un idéal de type fini (0, 20.4.4)'", "'de type fini' italic (page_063_s3.png)",
    "upright", "italics", fx(r"idéal de type fini", r"idéal \emph{de type fini}"))
add(p, "proof of (17.4.1): 'un idéal de type fini (0, 20.4.4)'", "bold 0 (page_063_s3.png)", "plain 0", "convention",
    fx(r"(0, 20.4.4)", r"(\textbf{0}, 20.4.4)"), convention=2)
add(p, "proof of (17.4.1): 'l'homomorphisme θ_z : O_{Z,z} → (ψ_*(O_X))_z est bijectif'",
    "θ_z without a sharp sign (crop p63_s3_thetaz.png)", "\\theta_z^\\#", "formula",
    fx(r"$\theta_z^\#: \sh{O}_{Z,z}\to(", r"$\theta_z: \sh{O}_{Z,z}\to("),
    "θ_z is the stalk at z of θ : O_Z → ψ_*(O_X), as in the conclusion 'θ : O_Z → ψ_*(O_X) est lui-même "
    "bijectif'; the print is right.")
add(p, "proof of (17.4.1): 'est lui-même bijectif (0_I, 5.2.7)'", "bold 0 with subscript I (crop p63_s4_0I.png)",
    "plain 0", "convention", fx(r"($0_{\mathrm I}$, 5.2.7)", r"($\mathbf{0}_{\mathrm I}$, 5.2.7)"), convention=2)
add(p, "proof of (17.4.1): 'Cela montre donc que b') entraîne b);'", "b') and b) italic (crop p63_s4_end.png)",
    "upright", "italics", fx(r"que b') entraîne b);", r"que \emph{b')} entraîne \emph{b)};"), L88)
add(p, "proof of (17.4.1): 'l'équivalence de b) et b'') résulte'", "b) and b'') italic (crop p63_s4_end.png)",
    "upright", "italics", fx(r"l'équivalence de b) et b'')", r"l'équivalence de \emph{b)} et \emph{b'')}"), L88)
add(p, "proof of (17.4.1): 'résulte de (I, 5.3.7)'", "bold I (crop p63_s4_end.png)", "plain I", "convention",
    fx(r"(I, 5.3.7)", r"(\textbf{I}, 5.3.7)"), convention=2)
add(p, "page break 63/64 inside the sentence 'équivaut en effet à celle d'un | Y-morphisme h = ...'",
    "p. 63 ends 'celle d'un', p. 64 begins 'Y-morphisme' in the same paragraph (page_063_s4.png, page_064_s1.png)",
    "blank line before \\oldpage[IV-4]{64}: paragraph break the print lacks", "marker",
    fx("celle d'un\n\n", "celle d'un\n"),
    "The marker itself is at the right place; only the blank line at the end of page_063.tex goes "
    "(GLOBAL_ISSUES 20).")

# ---------------------------------------------------------------- page 64
p = 64
add(p, "proof of (17.4.1): 'de sorte que s' = (1_{Y'}, h)_X'", "subscript X after the parenthesis "
    "(crops p64_s1_top.png, p64_s1_sprime_z.png)", "(1_{Y'},h)_X: keeps the printed reading", "misprint_in_print",
    None,
    "s' : Y' → X' = Y'×_Y X has components 1_{Y'} and h; in EGA's notation (u, v)_S the subscript is the base of the "
    "product, here Y. Same slip as the ×_X of the diagram label below. No diplomatic edit; no erratum found in "
    "Liste 3.", confidence="medium", corrected=r"$s'=(1_{Y'},h)_Y$")
add(p, "diagram (17.4.1.1), right vertical arrow: label 'h ×_X 1_X'",
    "the product sign carries a subscript (printed X; crops p64_s1_diag.png, p64_s1_label_z.png)",
    "h\\times 1_X: no subscript on \\times", "formula",
    fx(r"\ar[d]^{h\times 1_X}", r"\ar[d]^{h\times_Y 1_X}"),
    "APPLY BEFORE THE NEXT ENTRY. The TeX drops the subscript; this edit inserts it with the correct letter Y "
    "(for both editions), and the next entry (misprint) restores the printed X in the diplomatic text.")
add(p, "diagram (17.4.1.1), right vertical arrow: 'h ×_X 1_X' for h ×_Y 1_X",
    "×_X (crop p64_s1_label_z.png)", "after the previous entry: h\\times_Y 1_X", "misprint_in_print",
    fx(r"\ar[d]^{h\times_Y 1_X}", r"\ar[d]^{h\times_X 1_X}"),
    "APPLY AFTER THE PREVIOUS ENTRY: 'old' is the text after it (it does not occur in page_064.tex before that edit). "
    "The arrow X' = Y'×_Y X → X×_Y X is the product over Y of h and 1_X. No erratum found in Liste 3.",
    confidence="medium", corrected=r"h\times_Y 1_X")
add(p, "proof of (17.4.1): 'Par suite (I, 4.3.2)'", "bold I (page_064_s2.png)", "plain I", "convention",
    fx(r"(I, 4.3.2)", r"(\textbf{I}, 4.3.2)"), convention=2)
add(p, "proof of (17.4.1): 'ce qui prouve que b) implique b'').'", "b) and b'') italic (crop p64_s2_lbl.png)",
    "upright", "italics", fx(r"que b) implique b'').", r"que \emph{b)} implique \emph{b'')}."), L88)
add(p, "proof of (17.4.1): 'en appliquant b'') au cas où'", "b'') italic (crop p64_s2_lbl.png)", "upright",
    "italics", fx(r"appliquant b'') au cas", r"appliquant \emph{b'')} au cas"), L88)
add(p, "proof of (17.4.1), display 'd'') ⇒ c) ⇒ b) ⇒ d'')'",
    "labels italic with italic parentheses; no full stop after the display (crop p64_s2_impl.png)",
    "math labels with upright parentheses; full stop at the end", "italics",
    fx(r"d'')\Rightarrow c)\Rightarrow b)\Rightarrow d'').",
       r"\textit{d'')}\Rightarrow\textit{c)}\Rightarrow\textit{b)}\Rightarrow\textit{d'')}"),
    "One edit for two differences: the italic labels (written as the edition's other $\\textit{a)}\\Rightarrow"
    "\\textit{b)}$) and the full stop the print lacks (punctuation).")
add(p, "proof of (17.4.1), step heading 'd'') ⇒ c) :'", "labels italic with italic parentheses (crop p64_s2_head.png)",
    "$d'')\\Rightarrow c)$: upright parentheses", "italics",
    fx(r"$d'')\Rightarrow c)$:", r"$\textit{d'')}\Rightarrow\textit{c)}$:"), L88)
add(p, "step d'')⇒c): 'Comme Ω^1_{X/Y} est un O_X-Module de type fini'", "italic Ω (crop p64_s2_head.png)",
    "\\Omega (upright)", "font", fx(r"Comme $\Omega^1_{X/Y}$ est un", r"Comme $\varOmega^1_{X/Y}$ est un"), G92)
add(p, "step d'')⇒c): 'la condition c) équivaut'", "c) italic (crop p64_s2_mid.png)", "upright", "italics",
    fx(r"la condition c) équivaut", r"la condition \emph{c)} équivaut"), L88)
add(p, "step d'')⇒c): '(Ω^1_{X/Y})_x/m_y(Ω^1_{X/Y})_x=0'", "italic Ω twice (crop p64_s2_mid.png)",
    "\\Omega (upright) twice", "font",
    fx(r"$(\Omega^1_{X/Y})_x/\mathfrak{m}_y(\Omega^1_{X/Y})_x=0$",
       r"$(\varOmega^1_{X/Y})_x/\mathfrak{m}_y(\varOmega^1_{X/Y})_x=0$"), G92)
add(p, "step d'')⇒c): '(Ω^1_{X_y/Spec(k(y))})_x=0'", "italic Ω (crop p64_s2_omspec.png)", "\\Omega (upright)",
    "font", fx(r"$(\Omega^1_{X_y/", r"$(\varOmega^1_{X_y/"),
    G92 + " Adjacent to, but independent of, the next entry.")
add(p, "step d'')⇒c): k(y) in the subscript of Ω^1_{X_y/Spec(k(y))}", "bold upright k in the subscript "
    "(crop p64_s2_omspec.png)", "plain k", "convention",
    fx(r"\Spec(k(y))})_x", r"\Spec(\mathbf{k}(y))})_x"), "Subscript: bold upright k (GLOBAL_ISSUES 48).",
    convention=1)
add(p, "step d'')⇒c): 'un corps k', extension finie de k'", "'finie' italic (crop p64_s2_low.png)", "upright",
    "italics", fx(r"extension finie de $k$", r"extension \emph{finie} de $k$"))
add(p, "step d'')⇒c): 'x est fermé dans X (I, 6.4.2)'", "bold I (crop p64_s2_low.png)", "plain I", "convention",
    fx(r"(I, 6.4.2)", r"(\textbf{I}, 6.4.2)"), convention=2)
add(p, "step d'')⇒c): 'donc est un point isolé de X.'", "'isolé' italic (crop p64_s2_low.png)", "upright", "italics",
    fx(r"un point isolé de $X$.", r"un point \emph{isolé} de $X$."))
add(p, "step d'')⇒c): 'entraîne Ω^1_{k'/k}=0 (0, 20.6.20)'", "bold 0 (crop p64_s3_top.png)", "plain 0",
    "convention", fx(r"(0, 20.6.20)", r"(\textbf{0}, 20.6.20)"),
    "The module Ω^1_{k'/k} is upright in the print, as in the TeX.", convention=2)
add(p, "step d'')⇒c), end: 'ce qui prouve c).'", "c) italic (crop p64_s3_top.png)", "upright", "italics",
    fx(r"ce qui prouve c).", r"ce qui prouve \emph{c)}."), L88)
add(p, "step heading 'c) ⇒ b) :'", "labels italic with italic parentheses (crop p64_s3_top.png)",
    "$c)\\Rightarrow b)$: upright parentheses", "italics",
    fx(r"$c)\Rightarrow b)$:", r"$\textit{c)}\Rightarrow\textit{b)}$:"), L88)
add(p, "step c)⇒b): 'l'on a alors Ω^1_{X/Y}|U=0'", "italic Ω (crop p64_s3_top.png)", "\\Omega (upright)", "font",
    fx(r"alors $\Omega^1_{X/Y}|U=0$", r"alors $\varOmega^1_{X/Y}|U=0$"), G92)
add(p, "step c)⇒b): 'l'assertion b) résulte'", "b) italic (crop p64_s3_top.png)", "upright", "italics",
    fx(r"l'assertion b) résulte", r"l'assertion \emph{b)} résulte"), L88)
add(p, "step c)⇒b): 'la définition de Ω^1_{X/Y} (16.3.1)'", "italic Ω (crop p64_s3_top.png)", "\\Omega (upright)",
    "font", fx(r"définition de $\Omega^1_{X/Y}$ (16.3.1)", r"définition de $\varOmega^1_{X/Y}$ (16.3.1)"), G92)
add(p, "step heading 'b) ⇒ d'') :'", "labels italic with italic parentheses (crop p64_s3_top.png)",
    "$b)\\Rightarrow d'')$: upright parentheses", "italics",
    fx(r"$b)\Rightarrow d'')$:", r"$\textit{b)}\Rightarrow\textit{d'')}$:"), L88)
add(p, "step b)⇒d''): 'f_y : X_y → Spec(k(y))'", "bold italic k (page_064_s3.png)", "plain k", "convention",
    fx(r"f_y:X_y\to\Spec(k(y))$", r"f_y:X_y\to\Spec(\boldsymbol{k}(y))$"), convention=1)
add(p, "step b)⇒d''): 'une immersion ouverte (I, 5.3.4)'", "bold I (page_064_s3.png)", "plain I", "convention",
    fx(r"(I, 5.3.4)", r"(\textbf{I}, 5.3.4)"), convention=2)
add(p, "step b)⇒d''): 'la condition d'') ne concerne'", "d'') italic (page_064_s3.png)", "upright", "italics",
    fx(r"la condition d'') ne concerne", r"la condition \emph{d'')} ne concerne"), L88)
add(p, "step b)⇒d''): 'la propriété d'') sera établie'", "d'') italic (page_064_s3.png)", "upright", "italics",
    fx(r"la propriété d'') sera", r"la propriété \emph{d'')} sera"), L88)
add(p, "step b)⇒d''): 'au cas où k est algébriquement clos. Montrons'",
    "'algébriquement clos' italic (crop p64_s3_low.png); the later 'puisque k est algébriquement clos' is roman",
    "upright", "italics",
    fx(r"est algébriquement clos. Montrons", r"est \emph{algébriquement clos}. Montrons"))
add(p, "step b)⇒d''): 'tout point fermé x de X est isolé'", "'isolé' italic (crop p64_s3_low.png)", "upright",
    "italics", fx(r"$X$ est isolé, car alors", r"$X$ est \emph{isolé}, car alors"))
add(p, "step b)⇒d''): 'en vertu de (I, 6.4.4)'", "bold I (page_064_s4.png)", "plain I", "convention",
    fx(r"(I, 6.4.4)", r"(\textbf{I}, 6.4.4)"), convention=2)
add(p, "step b)⇒d''): 'on a alors k(x)=k'", "first k bold italic (residue field), second k light italic "
    "(page_064_s4.png)", "plain k twice", "convention",
    fx(r"$k(x)=k$", r"$\boldsymbol{k}(x)=k$"), convention=1)
add(p, "step b)⇒d''): 'algébriquement clos (I, 6.4.3)'", "bold I (page_064_s4.png)", "plain I", "convention",
    fx(r"(I, 6.4.3)", r"(\textbf{I}, 6.4.3)"), convention=2)
add(p, "step b)⇒d''): 'en vertu de l'hypothèse b).'", "b) italic (page_064_s4.png)", "upright", "italics",
    fx(r"l'hypothèse b).", r"l'hypothèse \emph{b)}."), L88)
add(p, "page break 64/65 inside the sentence 'On a ainsi montré que A est une | k-algèbre finie'",
    "p. 64 ends 'que A est une', p. 65 begins 'k-algèbre finie' in the same paragraph (page_064_s4.png)",
    "blank line before \\oldpage[IV-4]{65}: paragraph break the print lacks", "marker",
    fx("que $A$ est une\n\n", "que $A$ est une\n"),
    "The marker itself is at the right place (page_065.tex begins '$k$-algèbre'); only the blank line at the end of "
    "page_064.tex goes (GLOBAL_ISSUES 20).")


# ---------------------------------------------------------------- checks
def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


problems = []
final = {}
for n in (60, 61, 62, 63, 64):
    orig = page_text(n)
    cur = orig
    for i, e in enumerate(F):
        if e["page"] != n or not e["fix"]:
            continue
        old, new = e["fix"]["old"], e["fix"]["new"]
        c_orig = orig.count(old)
        c_cur = cur.count(old)
        dep = "APPLY AFTER" in e["note"]
        if c_cur != 1:
            problems.append((n, i, "count in current text", c_cur, old))
        if c_orig != 1 and not dep:
            problems.append((n, i, "count in original", c_orig, old))
        if dep and c_orig != 0:
            problems.append((n, i, "dependent old already in original", c_orig, old))
        cur = cur.replace(old, new, 1)
    final[n] = cur

# overlaps between independent fixes on the original text
for n in (60, 61, 62, 63, 64):
    orig = page_text(n)
    spans = []
    for i, e in enumerate(F):
        if e["page"] != n or not e["fix"] or "APPLY AFTER" in e["note"]:
            continue
        k = orig.find(e["fix"]["old"])
        if k >= 0:
            spans.append((k, k + len(e["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            problems.append((n, (a[2], b[2]), "overlap", F[a[2]]["fix"]["old"], F[b[2]]["fix"]["old"]))

for pr in problems:
    print("PROBLEM", pr)

counts = {}
for e in F:
    c = counts.setdefault(e["page"], [0, 0, 0])
    if e["kind"] == "misprint_in_print":
        c[2] += 1
    elif e["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts, "total", len(F))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for n, t in final.items():
    (Path(__file__).resolve().parent / f"fixed_{n:03d}.tex").write_text(t, encoding="utf-8")
print("wrote", OUT)
