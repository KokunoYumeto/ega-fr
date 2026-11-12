import json

base = r"user\Documents\ega_scan_check_20261101"
src_dir = base + r"\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4"
run = base + r"\run_IV4"
OUT = run + r"\findings_255_259.json"

NL = "\n"
BEFORE21 = ("Lies before the first page marker of ega4-21a-fr.tex (the § 21 opening printed on p. 255; "
            "page_255.tex carries it after '% (continued in ...)').")

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, src="ega4-21a-fr.tex"):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    d["_src"] = src
    F.append(d)


# ---------------- page 255 ----------------
add(255, "(20.6.9), l. 4: 'X'_{s'} = X_s ⊗_{k(s)} k(s')' (subscript of the tensor sign)",
    "subscript k(s) printed in bold upright type (crop p255_k.png)",
    r"\otimes_{k(s)} with a plain k",
    "convention", 1, "high",
    r"X_s\otimes_{k(s)}", r"X_s\otimes_{\mathbf{k}(s)}",
    "Bold upright in subscripts (GLOBAL_ISSUES 48). Adjacent to the next fix; the two 'old' strings do not overlap.",
    src="ega4-20-fr.tex")
add(255, "(20.6.9), l. 4: '... ⊗_{k(s)} k(s'), donc le morphisme'",
    "k(s') in bold italic (crop p255_k.png)",
    r"k(s') plain",
    "convention", 1, "high",
    r"k(s')$, donc le morphisme", r"\boldsymbol{k}(s')$, donc le morphisme",
    "Residue field on the line: bold italic.",
    src="ega4-20-fr.tex")
add(255, "heading of 21.1: '21.1. Diviseurs sur un espace annelé.'",
    "the title ends with a full stop",
    "no full stop in the \\subsection title",
    "punctuation", None, "high",
    r"\subsection{Diviseurs sur un espace annelé}", r"\subsection{Diviseurs sur un espace annelé.}",
    BEFORE21 + " Same form as the 20.3 title on p. 237 (GLOBAL_ISSUES 43/58).")
add(255, "(21.1.1), l. 4: 'des germes de sections inversibles de O_X'",
    "'inversibles' italic",
    "'inversibles' upright",
    "italics", None, "high",
    r"des germes de sections inversibles de", r"des germes de sections \emph{inversibles} de",
    BEFORE21)
add(255, "Définition (21.1.2), l. 1: 'On appelle faisceau des diviseurs sur X et on note'",
    "'faisceau des diviseurs' upright, 'sur' italic like the rest of the statement (crop p255_def_b.png)",
    r"\emph{faisceau des diviseurs sur $X$} sets 'sur' upright too",
    "italics", None, "high",
    r"On appelle \emph{faisceau des diviseurs sur $X$} et on note",
    r"On appelle \emph{faisceau des diviseurs} sur $X$ et on note",
    BEFORE21)
add(255, "Définition (21.1.2), l. 3: 'se nomment les diviseurs sur X; ils forment'",
    "'les diviseurs sur X' italic, no change of face (crop p255_def_c.png)",
    r"\emph{diviseurs sur $X$} prints upright inside the italic definition",
    "italics", None, "high",
    r"se nomment les \emph{diviseurs sur $X$};", r"se nomment les diviseurs sur $X$;",
    BEFORE21)
add(255, "Définition (21.1.2), l. 4: '(autrement dit, toute fonction méromorphe régulière sur X (20.1.8))'",
    "the parenthesis is roman: '(autrement dit, toute' and 'sur X (20.1.8))' upright with upright parentheses, "
    "only 'fonction méromorphe régulière' italic (crops p255_def_c.png, p255_def_d.png)",
    "all italic (inside the italic definition environment)",
    "convention", 6, "high",
    r"(autrement dit, toute fonction méromorphe régulière sur $X$ \sref{IV.20.1.8})",
    r"\textup{(autrement dit, toute \emph{fonction méromorphe régulière} sur $X$ \sref{IV.20.1.8})}",
    BEFORE21 + " Inside \\textup, \\emph sets the three italic words italic.")
add(255, "Définition (21.1.2), l. 5: 'on appelle diviseur de f et on note'",
    "'diviseur de f' italic, no change of face (crop p255_def_e.png)",
    r"\emph{diviseur de $f$} prints upright inside the italic definition",
    "italics", None, "high",
    r"on appelle \emph{diviseur de $f$} et on note", r"on appelle diviseur de $f$ et on note",
    BEFORE21)
add(255, "Définition (21.1.2), l. 5: 'div(f) (ou div_X(f))'",
    "'(ou' upright, upright parentheses (crop p255_def_e.png)",
    "'ou' and the parentheses italic (inside the italic definition)",
    "convention", 6, "high",
    r"(ou $\operatorname{div}_X(f)$)", r"\textup{(ou $\operatorname{div}_X(f)$)}",
    BEFORE21)
add(255, "Définition (21.1.2), last line: 'canonique Γ(X, M*_X) → Γ(X, Div_X).'",
    "the formula stands in the line after 'canonique' (crop p255_def_e.png)",
    "set as a display",
    "formula", None, "high",
    r"par l'homomorphisme canonique" + NL + r"\[" + NL + r"  \Gamma(X,\sh{M}_X^*)\longrightarrow\Gamma(X,\sh{D}iv_X)." + NL + r"\]",
    r"par l'homomorphisme canonique $\Gamma(X,\sh{M}_X^*)\to\Gamma(X,\sh{D}iv_X)$.",
    BEFORE21)

# ---------------- page 256 ----------------
add(256, "l. 4: 'est égal au préfaisceau U ⇝ Div(U)'",
    "wavy arrow (crop p256_leads.png)",
    r"\mapsto",
    "symbol", None, "high",
    r"$U\mapsto\operatorname{Div}(U)$", r"$U\leadsto\operatorname{Div}(U)$",
    "GLOBAL_ISSUES 33/107 (wavy arrows).")
add(256, "(21.1.3), after (21.1.3.2): 'Par définition, pour toute fonction méromorphe régulière f sur X'",
    "new indented paragraph after the display (crop p256_pardef.png)",
    "no blank line after the display: the line continues the paragraph without an indent",
    "other", None, "high",
    r"\tag{21.1.3.2}" + NL + r"\]" + NL + r"Par définition",
    r"\tag{21.1.3.2}" + NL + r"\]" + NL + NL + r"Par définition",
    "Paragraph break after a display (GLOBAL_ISSUES 47 pattern).")
add(256, "(21.1.4), l. 1: 'un O_X-Module inversible, et soit s'",
    "'inversible' italic (crop p256_inv.png)",
    "'inversible' upright",
    "italics", None, "high",
    r"$\sh{O}_X$-Module inversible, et soit $s$", r"$\sh{O}_X$-Module \emph{inversible}, et soit $s$",
    "")

# ---------------- page 257 ----------------
add(257, "l. 2: 'sont les inverses dans Γ(U, M*_X)'",
    "'inverses' italic (crop p257_inv.png)",
    "'inverses' upright",
    "italics", None, "high",
    r"sont les inverses dans", r"sont les \emph{inverses} dans",
    "")
add(257, "Définition (21.1.6), l. 2-3: 'sont appelées diviseurs positifs sur X'",
    "'diviseurs positifs sur X' italic, no change of face (crop p257_def_b.png)",
    r"\emph{diviseurs positifs sur $X$} prints upright inside the italic definition",
    "italics", None, "high",
    r"sont appelées \emph{diviseurs positifs sur $X$}, et leur", r"sont appelées diviseurs positifs sur $X$, et leur",
    "")
add(257, "after (21.1.6.2): 'pour une structure d'ordre sur le groupe Div(X)'",
    "only \"d'ordre\" italic, 'structure' roman (crop p257_ordre.png)",
    r"\emph{structure d'ordre}",
    "italics", None, "high",
    r"pour une \emph{structure d'ordre} sur le groupe", r"pour une structure \emph{d'ordre} sur le groupe",
    "")
add(257, "after (21.1.6.3): 'une structure de faisceau de groupes ordonnés.'",
    "'faisceau de groupes ordonnés' italic (crop p257_fgo_b.png)",
    "upright",
    "italics", None, "high",
    r"une structure de faisceau de groupes ordonnés.", r"une structure de \emph{faisceau de groupes ordonnés}.",
    "")
add(257, "after (21.1.6.4): 'f est une section régulière de O_X'",
    "'section régulière de' italic, including 'de' (crop p257_secreg.png)",
    r"\emph{section régulière} de",
    "italics", None, "high",
    r"est une \emph{section régulière} de $\sh{O}_X$", r"est une \emph{section régulière de} $\sh{O}_X$",
    "")
add(257, "paragraph 'Plus généralement': 'il existe un élément régulier t de Γ(U, O_X)'",
    "'régulier' italic (crop p257_regulier.png)",
    "'régulier' upright",
    "italics", None, "high",
    r"un élément régulier $t$ de", r"un élément \emph{régulier} $t$ de",
    "")
add(257, "Proposition (21.1.8), l. 2: 'on ait D_x ⩾ 0 (resp. D_x = 0).'",
    "'(resp.' roman, upright parentheses (crop p257_resp1.png)",
    "'resp.' and the parentheses italic (inside the italic proposition)",
    "convention", 6, "high",
    r"on ait $D_x\geq0$ (resp. $D_x=0$).", r"on ait $D_x\geq0$ \textup{(resp. $D_x=0$)}.",
    "")
add(257, "Proposition (21.1.8), l. 3: 'Alors on a D ⩾ 0 (resp. D = 0).'",
    "'(resp.' roman, upright parentheses (crop p257_resp2.png)",
    "'resp.' and the parentheses italic",
    "convention", 6, "high",
    r"Alors on a $D\geq0$ (resp. $D=0$).", r"Alors on a $D\geq0$ \textup{(resp. $D=0$)}.",
    "")

# ---------------- page 258 ----------------
add(258, "proof of (21.1.8), l. 1: 'équivaut à x∈dom(f) donc l'hypothèse'",
    "no comma after dom(f) (crop p258_dom.png)",
    "comma after dom(f)",
    "punctuation", None, "high",
    r"$x\in\operatorname{dom}(f)$, donc l'hypothèse", r"$x\in\operatorname{dom}(f)$ donc l'hypothèse",
    "")
add(258, "proof of (21.1.8), l. 2: 'si T = X—dom(f)'",
    "long dash for set difference (crop p258_Tdash.png)",
    "minus sign",
    "convention", 7, "high",
    r"$T=X-\operatorname{dom}(f)$", r"$T=X\setmin\operatorname{dom}(f)$",
    "")
add(258, "proof of (21.1.8), l. 4: 'Γ(X, O_X) → Γ(X—T, O_X)'",
    "long dash for set difference",
    "minus sign",
    "convention", 7, "high",
    r"\Gamma(X-T,\sh{O}_X)$", r"\Gamma(X\setmin T,\sh{O}_X)$",
    "Independent of the next fix on the same line (no overlap).")
add(258, "proof of (21.1.8), l. 4: 'est bijectif, ce qui montre'",
    "'bijectif' italic",
    "'bijectif' upright",
    "italics", None, "high",
    r"est bijectif, ce qui montre", r"est \emph{bijectif}, ce qui montre",
    "")
add(258, "proof of (21.1.8), l. 5: 'telle que f = s|(X—T)'",
    "long dash for set difference",
    "minus sign",
    "convention", 7, "high",
    r"$f=s|(X-T)$", r"$f=s|(X\setmin T)$",
    "")
add(258, "Proposition (21.1.10), end: '... soit associé à A (0, 16.4.6)).'",
    "the reference is roman: upright parentheses, upright 16.4.6, and the closing parenthesis of the "
    "italic parenthetical is upright too; the parenthetical's opening '(' before 'autrement' is italic "
    "(crops p258_ref.png, p258_paren.png)",
    "the reference text and both closing parentheses italic (inside the italic proposition)",
    "convention", 6, "high",
    r"(\hyperref[0.16.4.6]{$\mathbf{0}$, 16.4.6})).", r"\textup{(\hyperref[0.16.4.6]{$\mathbf{0}$, 16.4.6}))}.",
    "The bold 0 without subscript matches the print. The '(' before 'autrement dit' stays italic.")
add(258, "heading of 21.2: '21.2. Diviseurs et Idéaux fractionnaires inversibles.'",
    "the title ends with a full stop",
    "no full stop in the \\subsection title",
    "punctuation", None, "high",
    r"\subsection{Diviseurs et Idéaux fractionnaires inversibles}",
    r"\subsection{Diviseurs et Idéaux fractionnaires inversibles.}",
    "Same form as the 20.3 title on p. 237 (GLOBAL_ISSUES 43/58).")
add(258, "(21.2.1), l. 1: 'On appelle Idéal fractionnaire sur X un'",
    "'Idéal fractionnaire' italic, 'sur' roman (crop p258_211_b.png)",
    r"\emph{Idéal fractionnaire sur $X$} sets 'sur' italic too",
    "italics", None, "high",
    r"\emph{Idéal fractionnaire sur $X$}", r"\emph{Idéal fractionnaire} sur $X$",
    "Independent of the next fix (no overlap).")
add(258, "(21.2.1), l. 2: 'un sous-O_X-Module du O_X-Module M_X'",
    "'sous-O_X-Module' italic (crop p258_211_a.png)",
    "upright",
    "italics", None, "high",
    r"sous-$\sh{O}_X$-Module du", r"\emph{sous-$\sh{O}_X$-Module} du",
    "")
add(258, "(21.2.1), l. 3: 'qui est un O_X-Module inversible est appelé'",
    "'O_X-Module inversible' italic (crop p258_211_b.png)",
    "upright",
    "italics", None, "high",
    r"qui est un $\sh{O}_X$-Module inversible est appelé", r"qui est un \emph{$\sh{O}_X$-Module inversible} est appelé",
    "")
add(258, "proof of (21.2.2), l. 1: \"l'application s ⇝ s(f|V)\"",
    "wavy arrow (crop p258_wavy.png)",
    r"\mapsto",
    "symbol", None, "high",
    r"$s\mapsto s(f|V)$", r"$s\leadsto s(f|V)$",
    "GLOBAL_ISSUES 33/107 (wavy arrows).")
add(258, "proof of (21.2.2): '(où V est un ouvert contenu dans U) la section v(u|V)/(s|V)'",
    "no comma after the closing parenthesis (crop p258_ou_b.png)",
    "comma after the parenthesis",
    "punctuation", None, "high",
    r"contenu dans $U$), la section", r"contenu dans $U$) la section",
    "")
add(258, "last paragraph: 'déterminée à la multiplication près par un élément de Γ(U, O*_X)'",
    "'à la multiplication près par un élément de' italic (crop p258_mult.png)",
    r"only '\emph{à la multiplication près}' italic",
    "italics", None, "high",
    r"\emph{à la multiplication près} par un élément de", r"\emph{à la multiplication près par un élément de}",
    "")

# ---------------- page 259 ----------------
add(259, "Corollaire (21.2.3): item labels (i), (ii)",
    "labels upright (crops p259_i.png, p259_ii.png)",
    "enumerate labels italic inside the italic corollary",
    "convention", 6, "high",
    r"\label{IV.21.2.3}" + NL + r"\begin{enumerate}[label=(\roman*)]",
    r"\label{IV.21.2.3}" + NL + r"\begin{enumerate}[label=\textup{(\roman*)}]",
    "GLOBAL_ISSUES 16; one edit covers both labels.")
add(259, "Corollaire (21.2.3) (i), l. 2: \"l'Idéal fractionnaire J' (transporteur de J dans O_X)\"",
    "'transporteur' italic like the rest of the statement, italic parentheses (crop p259_transp.png)",
    r"\emph{transporteur} prints upright inside the italic corollary",
    "italics", None, "high",
    r"(\emph{transporteur} de $\sh{J}$ dans $\sh{O}_X$)", r"(transporteur de $\sh{J}$ dans $\sh{O}_X$)",
    "")
add(259, "proof of (21.2.3): \"l'homomorphisme t(f|V) ⇝ st\"",
    "wavy arrow",
    r"\mapsto",
    "symbol", None, "high",
    r"$t(f|V)\mapsto st$", r"$t(f|V)\leadsto st$",
    "")
add(259, "after the proof: 'En vertu de (21.2.3, (i)), on identifiera'",
    "'(21.2.3, (i))', the label inside the reference's parentheses (crop p259_ref.png)",
    r"\sref{IV.21.2.3},~(i) prints '(21.2.3), (i)'",
    "punctuation", None, "high",
    r"En vertu de \sref{IV.21.2.3},~(i), on identifiera", r"En vertu de \sref{IV.21.2.3}[(i)], on identifiera",
    "\\sref's third argument prints '(21.2.3, (i))' (GLOBAL_ISSUES 68).")
add(259, "after the proof: 'comme un sous-O_X-Module de M*_X.'",
    "'sous-O_X-Module' italic (crop p259_Mstar.png)",
    "upright",
    "italics", None, "high",
    r"comme un sous-$\sh{O}_X$-Module", r"comme un \emph{sous-$\sh{O}_X$-Module}",
    "Apply before the misprint fix that follows (same sentence; the two 'old' strings do not overlap).")
add(259, "after the proof: 'sous-O_X-Module de M*_X.'",
    "the print has M*_X (with the asterisk) (crop p259_Mstar.png)",
    r"\sh{M}_X without the asterisk: silent correction",
    "misprint_in_print", None, "high",
    r"de $\sh{M}_X$." + NL + NL + r"\begin{env}[21.2.4]", r"de $\sh{M}_X^*$." + NL + NL + r"\begin{env}[21.2.4]",
    "Misprint: a fractional Ideal is a sub-O_X-Module of M_X (21.2.1); M*_X is a sheaf of multiplicative groups. "
    "The TeX silently corrects it; restore the printed reading. The corrected edition already has \\sh{M}_X. "
    "Apply after the italics fix above.",
    corrected=r"\sh{M}_X")
add(259, "(21.2.4), l. 3: 'pour la loi de composition (J_1, J_2) ⇝ J_1 J_2'",
    "wavy arrow (crop p259_J12.png)",
    r"\mapsto",
    "symbol", None, "high",
    r"(\sh{J}_1,\sh{J}_2)\mapsto\sh{J}_1\sh{J}_2", r"(\sh{J}_1,\sh{J}_2)\leadsto\sh{J}_1\sh{J}_2",
    "")
add(259, "(21.2.4): \"l'application de restriction J ⇝ J|U\"",
    "wavy arrow (crop p259_JJU.png)",
    r"\mapsto",
    "symbol", None, "high",
    r"$\sh{J}\mapsto\sh{J}|U$", r"$\sh{J}\leadsto\sh{J}|U$",
    "")
add(259, "(21.2.4): 'un préfaisceau de groupes commutatifs U ⇝ Id.inv(U)'",
    "wavy arrow",
    r"\mapsto",
    "symbol", None, "high",
    r"$U\mapsto\operatorname{Id.inv}(U)$", r"$U\leadsto\operatorname{Id.inv}(U)$",
    "")
add(259, "(21.2.4), end: \"que l'on note Id.inv_X\" (script letter)",
    "script I: the letter sits on the base line without the descender of the script J used for the Ideals "
    "J, J', J_1 on these pages (crops p259_Idinv1.png against p259_JJU.png, p259_Jf.png)",
    r"\sh{J}d.inv_X",
    "symbol", None, "high",
    r"que l'on note $\sh{J}d.inv_X$.", r"que l'on note $\sh{I}d.inv_X$.",
    "Wrong letter (script I and J fixed by the print; no blanket change). The J of J(f), J', J_1, J|U is a "
    "script J in the print and stays.")
add(259, "(21.2.5), l. 3: \"l'application f ⇝ J(f)\"",
    "wavy arrow (crop p259_fJf.png)",
    r"\mapsto",
    "symbol", None, "high",
    r"$f\mapsto\sh{J}(f)$", r"$f\leadsto\sh{J}(f)$",
    "")
add(259, "(21.2.5.1): 'I_0 : M*_X → Id.inv_X.'",
    "script I (crop p259_Idinv2.png)",
    r"\sh{J}d.inv_X",
    "symbol", None, "high",
    r"I_0:\sh{M}_X^*\to\sh{J}d.inv_X.", r"I_0:\sh{M}_X^*\to\sh{I}d.inv_X.",
    "Wrong letter, as at the end of (21.2.4).")
add(259, "after (21.2.5.1): 'Notons que si f∈Γ(X, O*_X), on a J(f) = O_X'",
    "new indented paragraph after the display (crop p259_notons.png)",
    "no blank line after the display: the line continues the paragraph without an indent",
    "other", None, "high",
    r"\tag{21.2.5.1}" + NL + r"\]" + NL + r"Notons que si",
    r"\tag{21.2.5.1}" + NL + r"\]" + NL + NL + r"Notons que si",
    "Paragraph break after a display (GLOBAL_ISSUES 47 pattern). Independent of the (21.2.5.1) letter fix (no overlap).")
add(259, "(21.2.5.2): 'M*_X → M*_X/O*_X = Div_X →(I) Id.inv_X'",
    "script I (crop p259_Idinv3.png)",
    r"\sh{J}d.inv_X",
    "symbol", None, "high",
    r"\xrightarrow{I}\sh{J}d.inv_X", r"\xrightarrow{I}\sh{I}d.inv_X",
    "Wrong letter, as at the end of (21.2.4).")
add(259, "after (21.2.5.2): 'le faisceau de groupes multiplicatifs Id.inv_X'",
    "script I (crop p259_IU.png)",
    r"\sh{J}d.inv_X",
    "symbol", None, "high",
    r"groupes multiplicatifs $\sh{J}d.inv_X$", r"groupes multiplicatifs $\sh{I}d.inv_X$",
    "Wrong letter, as at the end of (21.2.4).")
add(259, "after (21.2.5.2): 'un homomorphisme I_U : Div(U) → Id.inv(U)' (script I_U)",
    "script I with subscript U (crop p259_IU.png)",
    r"\sh{J}_U",
    "symbol", None, "high",
    r"$\sh{J}_U:\operatorname{Div}(U)", r"$\sh{I}_U:\operatorname{Div}(U)",
    "Wrong letter (no descender in the print). The script J_X(D) at the top of p. 260 (TeX \\sh{J}_X) is for "
    "the p. 260 check.")
add(259, "(21.2.5.3): 'I_U(div_U(f)) = O_U.f.'",
    "script I (crop p259_IU2.png)",
    r"\sh{J}_U",
    "symbol", None, "high",
    r"\sh{J}_U(\operatorname{div}_U(f))", r"\sh{I}_U(\operatorname{div}_U(f))",
    "Wrong letter, as in the line above.")


# ---------------- verification ----------------
def read(p):
    with open(p, encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')


pages = {n: read(run + rf"\page_{n}.tex") for n in range(255, 260)}
srcs = {name: read(src_dir + "\\" + name) for name in ("ega4-20-fr.tex", "ega4-21a-fr.tex")}

ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    cp = pages[d["page"]].count(fx["old"])
    cs = srcs[d["_src"]].count(fx["old"])
    flag = "" if (cp == 1 and cs == 1) else "  <-- CHECK"
    if cp != 1:
        ok = False
    print(d["page"], d["kind"], "page:", cp, "src:", cs, flag, "|", fx["old"][:60].replace("\n", "\\n"))

# overlaps within a page
for n in range(255, 260):
    txt = pages[n]
    spans = []
    for d in F:
        if d["page"] == n and d["fix"]:
            i = txt.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP on", n, a, b)

for d in F:
    del d["_src"]
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", len(F), "all page-unique:", ok)
from collections import Counter
c = Counter((d["page"], "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")) for d in F)
for n in range(255, 260):
    print(n, c[(n, "normal")], c[(n, "convention")], c[(n, "misprint")])
