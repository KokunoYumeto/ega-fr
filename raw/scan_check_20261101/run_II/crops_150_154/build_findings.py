"""Build findings_150_154.json and check that every fix 'old' occurs exactly once.

<NL> in old/new strings stands for a line break (LF).
"""
import json

BASE = r"user\Documents\ega_scan_check_20261101\run_II"
OUT = BASE + r"\findings_150_154.json"


def conv2(page, where, ref, old=None, new=None):
    old = old if old is not None else "{" + ref + "}"
    if new is None:
        chap, rest = ref.split(",", 1)
        new = old.replace("{" + chap + ",", "{\\textbf{" + chap + "},", 1)
    return {
        "page": page, "where": where,
        "scan": "(" + ref + ") with bold " + ref.split(",")[0],
        "tex": "(" + ref + ") with plain " + ref.split(",")[0] + " in the link text",
        "kind": "convention", "convention": 2, "confidence": "high",
        "fix": {"old": old, "new": new}, "note": "",
    }


def conv1(page, where, old, new, scan="bold italic k", tex="plain k"):
    return {
        "page": page, "where": where, "scan": scan, "tex": tex,
        "kind": "convention", "convention": 1, "confidence": "high",
        "fix": {"old": old, "new": new}, "note": "",
    }


F = []

# ---------------- page 150 ----------------
F.append({
    "page": 150,
    "where": "proof of Corollaire (7.4.8), first paragraph: 'comme il résulte de (5.4.2, (ii)) et (5.4.3, (ii))'",
    "scan": "(5.4.2, (ii))",
    "tex": r"(\hyperref[II.5.4.2-fr]{5.4.2, (iii)})",
    "kind": "number", "convention": None, "confidence": "high",
    "fix": {"old": r"{5.4.2, (iii)}", "new": r"{5.4.2, (ii)}"},
    "note": "Enlarged crop: '(ii)' in both references. (5.4.2, (ii)) is the clause on composites of proper morphisms that the argument uses (g proper implies g∘f proper); base change (5.4.2, (iii)) is cited, correctly, on p. 152.",
})
F.append({
    "page": 150,
    "where": "Proposition (7.4.9): 'Soient X une courbe algébrique normale sur k'",
    "scan": "normale upright inside the italic statement",
    "tex": "normale in the italic proposition environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"algébrique normale sur $k$, $Y$", "new": r"algébrique \textup{normale} sur $k$, $Y$"},
    "note": "Enlarged crop.",
})
F.append({
    "page": 150,
    "where": "Proposition (7.4.9): 'Y un k-schéma algébrique propre sur k'",
    "scan": "propre upright inside the italic statement",
    "tex": "propre in the italic proposition environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"propre sur $k$. Toute", "new": r"\textup{propre} sur $k$. Toute"},
    "note": "",
})
F.append(conv2(150, "proof of (7.4.9): 'la dernière assertion provient de (I, 7.2.3)'", "I, 7.2.3"))
F.append(conv2(150, "proof of (7.4.10): 'il en est de même de la restriction de g à U_i (I, 5.3.14)'", "I, 5.3.14"))
F.append(conv2(150, "proof of (7.4.10): 'que g est séparé (I, 5.5.1, (v))'", "I, 5.5.1, (v)"))
F.append(conv2(150, "proof of (7.4.10): 'g est une immersion de X dans P (I, 8.2.8)'", "I, 8.2.8"))
F.append(conv2(150, "proof of (7.4.11): 'Soit X̄ l'adhérence de X dans P_k^n (I, 9.5.11)'", "I, 9.5.11"))
F.append(conv2(150, "proof of (7.4.11): 'sur un ouvert dense dans X̄ (I, 9.5.10)'", "I, 9.5.10"))
F.append(conv1(150, "proof of (7.4.11): 'et les k(x_i) sont les mêmes pour ces deux schémas'",
               r"les $k(x_i)$ sont", r"les $\boldsymbol{k}(x_i)$ sont",
               scan="k(x_i) with bold italic k", tex="$k(x_i)$ with plain k"))
F.append(conv2(150, "proof of (7.4.11): 'qui est réduite (I, 9.5.9)'", "I, 9.5.9"))

# ---------------- page 151 ----------------
F.append({
    "page": 151,
    "where": "Remarque (7.4.12), line 1: 'Nous montrerons au chapitre V que la conclusion de (7.4.10)'",
    "scan": "chapitre V",
    "tex": "chapitre V (keeps the print)",
    "kind": "misprint_in_print", "convention": None, "confidence": "high",
    "fix": None,
    "corrected": "chapitre III",
    "note": "Authors' errata in EGA III (ega3-7-fr.tex, Errata et Addenda): '(II, 7.4.12) Ligne 1 de la p. 151, remplacer chap. V par chap. III.' The TeX keeps the printed reading.",
})
F.append({
    "page": 151,
    "where": "Corollaire (7.4.13): 'Soient X une courbe normale irréductible de corps R(X)=K'",
    "scan": "normale upright inside the italic statement",
    "tex": "normale in the italic corollary environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"normale irréductible de corps $R(X)=K$, $Y$", "new": r"\textup{normale} irréductible de corps $R(X)=K$, $Y$"},
    "note": "Enlarged crop: 'normale', 'complète' and 'dominants' are roman in this statement, everything else italic.",
})
F.append({
    "page": 151,
    "where": "Corollaire (7.4.13): 'Y une courbe intègre complète de corps L=R(Y)'",
    "scan": "complète upright inside the italic statement",
    "tex": "complète in the italic corollary environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"intègre complète de corps", "new": r"intègre \textup{complète} de corps"},
    "note": "",
})
F.append({
    "page": 151,
    "where": "Corollaire (7.4.13): 'entre les k-morphismes dominants X→Y'",
    "scan": "dominants upright inside the italic statement",
    "tex": "dominants in the italic corollary environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"morphismes dominants $X\to Y$", "new": r"morphismes \textup{dominants} $X\to Y$"},
    "note": "",
})
F.append(conv2(151, "proof of (7.4.13): 'le corollaire résulte de ces remarques et de (I, 7.1.13)'", "I, 7.1.13"))
F.append({
    "page": 151,
    "where": "Corollaire (7.4.15): 'Soit X une courbe normale irréductible de corps R(X)=K'",
    "scan": "normale upright inside the italic statement",
    "tex": "normale in the italic corollary environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"courbe normale irréductible de corps $R(X)=K$. Il", "new": r"courbe \textup{normale} irréductible de corps $R(X)=K$. Il"},
    "note": "",
})
F.append(conv2(151, "proof of (7.4.15.1): 'à valeurs dans l'extension K de k (I, 7.1.12)'", "I, 7.1.12"))
F.append(conv2(151, "proof of (7.4.15.1): 'Si un tel point est localisé (I, 3.4.5) au point générique'", "I, 3.4.5",
               old=r"{I, 3.4.5}) au point", new=r"{\textbf{I}, 3.4.5}) au point"))
F.append({
    "page": 151,
    "where": "proof of (7.4.15.1): 'comme tout point de P_k^1 distinct du point générique est fermé'",
    "scan": "P_k^1 with a bold italic k as subscript (the residue-field letter of k(x), in subscript size)",
    "tex": r"\mathbf{P}_k^1 with plain k",
    "kind": "misprint_in_print", "convention": None, "confidence": "high",
    "fix": {"old": r"$\mathbf{P}_k^1$<NL>distinct du", "new": r"$\mathbf{P}_{\boldsymbol{k}}^1$<NL>distinct du"},
    "corrected": r"\mathbf{P}_k^1",
    "note": "Wrong font in the print: the base field k is plain italic in every other P_k^1 of the page (e.g. three lines above). Enlarged crops compared with the bold k of k(x) on p. 154 and a plain subscript k. The TeX silently corrects; the fix restores the printed reading.",
})
F.append(conv2(151, "proof of (7.4.15.1): 'l'unique morphisme U→P_k^1 de la classe u (I, 7.2.2)'", "I, 7.2.2"))
F.append({
    "page": 151,
    "where": "proof of (7.4.15.1): 'Il reste à mettre en correspondance biunivoque les points de P_k^1 à valeurs dans K'",
    "scan": "P_k^1 with a bold italic k as subscript",
    "tex": r"\mathbf{P}_k^1 with plain k",
    "kind": "misprint_in_print", "convention": None, "confidence": "high",
    "fix": {"old": r"$\mathbf{P}_k^1$ à valeurs dans $K$", "new": r"$\mathbf{P}_{\boldsymbol{k}}^1$ à valeurs dans $K$"},
    "corrected": r"\mathbf{P}_k^1",
    "note": "Same wrong-font k as in 'comme tout point de P_k^1 distinct du' (enlarged crop); the other P_k^1 on the page have a plain k. The TeX silently corrects; the fix restores the printed reading.",
})
F.append(conv2(151, "proof of (7.4.15.1): 'de localité (I, 3.4.5) distincte de ∞'", "I, 3.4.5",
               old=r"{I, 3.4.5}) distincte", new=r"{\textbf{I}, 3.4.5}) distincte"))
F.append({
    "page": 151,
    "where": "last line of p. 151: 's'il correspond à un' continues on p. 152 with 'élément transcendant sur k'",
    "scan": "one sentence across the page break; p. 152 begins flush left",
    "tex": r"blank line before \oldpage[II]{152} (paragraph break)",
    "kind": "other", "convention": None, "confidence": "high",
    "fix": {"old": "s'il correspond à un<NL><NL>", "new": "s'il correspond à un<NL>"},
    "note": "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line is the last line of this page's segment; nothing follows the p. 152 marker that needs changing.",
})

# ---------------- page 152 ----------------
F.append({
    "page": 152,
    "where": "Corollaire (7.4.16): 'deux courbes algébriques sur k, normales, complètes et irréductibles'",
    "scan": "'normales, complètes' upright inside the italic statement ('et irréductibles' italic)",
    "tex": "set in the italic corollary environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"normales, complètes et", "new": r"\textup{normales, complètes} et"},
    "note": "Enlarged crop.",
})
F.append({
    "page": 152,
    "where": "Proposition (7.4.18): 'L'ensemble des anneaux locaux de X s'identifie (I, 8.2.1)'",
    "scan": "the reference (I, 8.2.1) upright inside the italic statement",
    "tex": "reference inside the italic proposition environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"(\hyperref[I.8.2.1-fr]{I, 8.2.1})", "new": r"\textup{(\hyperref[I.8.2.1-fr]{I, 8.2.1})}"},
    "note": "Enlarged crop. Apply before the next item (bold I of the same reference): its 'old' survives this edit, but this 'old' does not survive that one.",
})
F.append(conv2(152, "Proposition (7.4.18): reference (I, 8.2.1)", "I, 8.2.1"))
F.append({
    "page": 152,
    "where": "heading of § 8: 'SCHÉMAS ÉCLATÉS; CONES PROJETANTS / FERMETURE PROJECTIVE'",
    "scan": "two centred lines; no semicolon after PROJETANTS at the line break (the semicolon after ÉCLATÉS is printed)",
    "tex": r"\section{Schémas éclatés~; cônes projetants~; fermeture projective}",
    "kind": "misprint_in_print", "convention": None, "confidence": "medium",
    "fix": {"old": r"cônes projetants~; fermeture projective", "new": r"cônes projetants fermeture projective"},
    "corrected": r"cônes projetants~; fermeture projective",
    "note": "Enlarged crop: the semicolon is absent. Both tables of contents (front-fr.tex and ega2-indexes-and-contents-fr.tex) read 'cônes projetants; fermeture projective'. The omission at the line break may be a display-heading habit rather than an error; classed as a misprint so that the corrected edition keeps the semicolon. The heading also prints CONES without the circumflex (capitals); not reported separately.",
})
F.append({
    "page": 152,
    "where": "display (8.1.1.2): equation number",
    "scan": "'8.1.1.2)' without the opening parenthesis",
    "tex": r"\tag{8.1.1.2} (typesets '(8.1.1.2)')",
    "kind": "misprint_in_print", "convention": None, "confidence": "high",
    "fix": {"old": r"\tag{8.1.1.2}", "new": r"\tag*{8.1.1.2)}"},
    "corrected": r"\tag{8.1.1.2}",
    "note": "Enlarged crop: the '(' of (8.1.1.1) one line above is printed, that of (8.1.1.2) is missing. The TeX silently corrects; \\tag* restores the printed form (the bold tag font is the document-wide heading-number item).",
})

# ---------------- page 153 ----------------
F.append({
    "page": 153,
    "where": "(8.1.2): 'est un Idéal fractionnaire de R(Y) s'il est de type fini (0, 5.2.1)'",
    "scan": "'de type fini' all italic",
    "tex": r"de \emph{type fini} ('de' upright)",
    "kind": "italics", "convention": None, "confidence": "high",
    "fix": {"old": r"s'il est de \emph{type fini}", "new": r"s'il est \emph{de type fini}"},
    "note": "Enlarged crop.",
})
F.append(conv2(153, "(8.1.2): 'une O_Y-Algèbre quasi-cohérente (I, 7.3.7)'", "I, 7.3.7"))
F.append(conv2(153, "(8.1.2): 's'il est de type fini (0, 5.2.1)'", "0, 5.2.1"))
F.append({
    "page": 153,
    "where": "(8.1.2), last line: 'pour tout Idéal fractionnaire inversible J de R(Y)'",
    "scan": "inversible in italics",
    "tex": "inversible upright",
    "kind": "italics", "convention": None, "confidence": "high",
    "fix": {"old": r"inversible $\mathcal{J}$ de $\mathcal{R}(Y)$.", "new": r"\emph{inversible} $\mathcal{J}$ de $\mathcal{R}(Y)$."},
    "note": "Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "Définition (8.1.3): 'Soit Y un préschéma (resp. un préschéma localement intègre)'",
    "scan": "'(resp.' roman inside the italic statement",
    "tex": "(resp. in the italic definition environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"un préschéma (resp. un préschéma", "new": r"un préschéma \textup{(resp.} un préschéma"},
    "note": "Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "Définition (8.1.3): 'un Idéal quasi-cohérent de O_Y (resp. un Idéal fractionnaire quasi-cohérent de R(Y))'",
    "scan": "'(resp.' roman inside the italic statement",
    "tex": "(resp. in the italic definition environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"de $\mathcal{O}_Y$ (resp. un Idéal", "new": r"de $\mathcal{O}_Y$ \textup{(resp.} un Idéal"},
    "note": "",
})
F.append({
    "page": 153,
    "where": "Définition (8.1.3): 'est obtenu en faisant éclater l'Idéal I'",
    "scan": "italic like the rest of the statement (no change of face)",
    "tex": r"\emph{...} inside the italic definition environment (comes out upright)",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"\emph{faisant éclater l'Idéal $\mathcal{I}$}", "new": r"faisant éclater l'Idéal $\mathcal{I}$"},
    "note": "Printed italic words left upright (drop \\emph inside the italic environment). Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "Définition (8.1.3): 'ou est le préschéma éclaté de Y relativement à I'",
    "scan": "italic like the rest of the statement (no change of face)",
    "tex": r"\emph{...} inside the italic definition environment (comes out upright)",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"\emph{préschéma éclaté<NL>de $Y$ relativement à $\mathcal{I}$}", "new": r"préschéma éclaté<NL>de $Y$ relativement à $\mathcal{I}$"},
    "note": "Printed italic words left upright (drop \\emph inside the italic environment). Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "after (8.1.3): 'si I est un O_Y-Module de type fini, X est donc projectif sur Y'",
    "scan": "'de type fini' all italic",
    "tex": r"de \emph{type fini} ('de' upright)",
    "kind": "italics", "convention": None, "confidence": "high",
    "fix": {"old": r"Module de \emph{type fini}", "new": r"Module \emph{de type fini}"},
    "note": "Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "after (8.1.3): 'la restriction de f à f^{-1}(Y—Y')'",
    "scan": "Y—Y' (long dash, set difference)",
    "tex": r"$f^{-1}(Y-Y')$",
    "kind": "convention", "convention": 7, "confidence": "high",
    "fix": {"old": r"$f^{-1}(Y-Y')$", "new": r"$f^{-1}(Y\setmin Y')$"},
    "note": "",
})
F.append({
    "page": 153,
    "where": "after (8.1.3): 'est un isomorphisme sur Y—Y''",
    "scan": "Y—Y' (long dash, set difference)",
    "tex": r"$Y-Y'$",
    "kind": "convention", "convention": 7, "confidence": "high",
    "fix": {"old": r"sur $Y-Y'$", "new": r"sur $Y\setmin Y'$"},
    "note": "",
})
F.append({
    "page": 153,
    "where": "after (8.1.3): 'lorsque I est un Idéal de O_Y et Y' le sous-préschéma fermé qu'il définit'",
    "scan": "'Idéal de' in italics",
    "tex": "upright",
    "kind": "italics", "convention": None, "confidence": "high",
    "fix": {"old": r"est un Idéal de $\mathcal{O}_Y$", "new": r"est un \emph{Idéal de} $\mathcal{O}_Y$"},
    "note": "Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "after (8.1.3): 'est remplacé par un Y-schéma canoniquement isomorphe X' (8.1.1)'",
    "scan": "isomorphe in italics",
    "tex": "upright",
    "kind": "italics", "convention": None, "confidence": "high",
    "fix": {"old": r"canoniquement isomorphe $X'$", "new": r"canoniquement \emph{isomorphe} $X'$"},
    "note": "Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "after (8.1.3): 'pour tout Idéal (resp. Idéal fractionnaire) inversible J, le préschéma éclaté'",
    "scan": "inversible in italics",
    "tex": "upright",
    "kind": "italics", "convention": None, "confidence": "high",
    "fix": {"old": r"fractionnaire) inversible $\mathcal{J}$", "new": r"fractionnaire) \emph{inversible} $\mathcal{J}$"},
    "note": "Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "after (8.1.3): 'le Y-schéma obtenu en faisant éclater I est isomorphe à Y (3.1.7)'",
    "scan": "'isomorphe à' in italics (italic à)",
    "tex": r"\emph{isomorphe} à (à upright)",
    "kind": "italics", "convention": None, "confidence": "high",
    "fix": {"old": r"\emph{isomorphe} à $Y$", "new": r"\emph{isomorphe à} $Y$"},
    "note": "Enlarged crop.",
})
F.append({
    "page": 153,
    "where": "last line of p. 153: Proposition (8.1.4) (i) '... vérifiant (8.1.1.2)' continues on p. 154 with 'et tels que I_0=O_Y'",
    "scan": "one sentence across the page break; p. 154 begins flush left",
    "tex": r"blank line before \oldpage[II]{154} (paragraph break inside the item)",
    "kind": "other", "convention": None, "confidence": "high",
    "fix": {"old": r"{8.1.1.2})<NL><NL>", "new": r"{8.1.1.2})<NL>"},
    "note": "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). Apply before the next item: this 'old' does not survive that edit, but its 'old' survives this one.",
})
F.append({
    "page": 153,
    "where": "Proposition (8.1.4) (i): 'vérifiant (8.1.1.2)'",
    "scan": "the reference (8.1.1.2) upright inside the italic statement",
    "tex": "reference inside the italic proposition environment",
    "kind": "convention", "convention": 6, "confidence": "high",
    "fix": {"old": r"vérifiant<NL>(\hyperref[II.8.1.1.2-fr]{8.1.1.2})", "new": r"vérifiant<NL>\textup{(\hyperref[II.8.1.1.2-fr]{8.1.1.2})}"},
    "note": "Enlarged crop. Apply after the previous item (page-break blank line).",
})

# ---------------- page 154 ----------------
F.append(conv2(154, "proof of (8.1.4) (i): 'O_y est un anneau intègre (I, 5.1.4)'", "I, 5.1.4"))
F.append(conv1(154, "proof of (8.1.4) (ii): 'il faut prouver que k(x) est de rang 1 sur k(y)', k(x)",
               r"$k(x)$", r"$\boldsymbol{k}(x)$", scan="k(x) with bold italic k", tex="$k(x)$ with plain k"))
F.append(conv1(154, "proof of (8.1.4) (ii): 'est de rang 1 sur k(y)'",
               r"sur $k(y)$", r"sur $\boldsymbol{k}(y)$", scan="k(y) with bold italic k", tex="$k(y)$ with plain k"))
F.append(conv1(154, "proof of (8.1.4) (ii): 'où Z=Spec(k(y))'",
               r"$Z=\operatorname{Spec}(k(y))$", r"$Z=\operatorname{Spec}(\boldsymbol{k}(y))$",
               scan="Spec(k(y)) with bold italic k", tex="plain k"))
F.append(conv2(154, "proof of (8.1.4) (ii): 'I_y≠0 (I, 7.3.6)'", "I, 7.3.6"))
F.append(conv1(154, "proof of (8.1.4) (ii): 'd'où I_y=k(y)'",
               r"$\mathcal{I}_y=k(y)$", r"$\mathcal{I}_y=\boldsymbol{k}(y)$",
               scan="k(y) with bold italic k", tex="plain k"))
F.append(conv1(154, "proof of (8.1.4) (ii): 'Proj(S') s'identifie donc à Spec(k(y)) (3.1.7)'",
               r"$\operatorname{Spec}(k(y))$ (", r"$\operatorname{Spec}(\boldsymbol{k}(y))$ (",
               scan="Spec(k(y)) with bold italic k", tex="plain k"))
F.append(conv2(154, "'Nous démontrerons une réciproque de (8.1.4) dans (III, 2.3.8)'", "III, 2.3.8"))
F.append({
    "page": 154,
    "where": "'Nous démontrerons une réciproque de (8.1.4) dans (III, 2.3.8)' (line 15 of the page)",
    "scan": "(III, 2.3.8)",
    "tex": "(III, 2.3.8) (keeps the print)",
    "kind": "misprint_in_print", "convention": None, "confidence": "high",
    "fix": None,
    "corrected": r"(\hyperref[III.2.3.7-fr]{III, 2.3.7})",
    "note": "Authors' errata in EGA III (ega3-7-fr.tex, Errata et Addenda): '(II, 8.1.4) Ligne 15 de la p. 154, remplacer (III, 2.3.8) par (III, 2.3.7).' The TeX keeps the printed reading (link target III.2.3.8-fr).",
})
F.append({
    "page": 154,
    "where": "(8.1.5): 'comme S_+(k+1) et S(k+1) sont canoniquement (TN)-isomorphes'",
    "scan": "(TN) in bold, parentheses included",
    "tex": "(TN) plain",
    "kind": "font", "convention": None, "confidence": "high",
    "fix": {"old": r"(TN)-isomorphes", "new": r"\textbf{(TN)}-isomorphes"},
    "note": "Enlarged crop. Cf. GLOBAL_ISSUES item 24 ((TN) printed bold in section 3.6).",
})
F.append({
    "page": 154,
    "where": "end of p. 154: display (8.1.5.4) 'S_X=⊕_{n∈Z} O_X(n)'; the sentence continues on p. 155 with 'une structure de O_X-Algèbre graduée quasi-cohérente'",
    "scan": "p. 155 begins flush left, continuing the sentence (checked on the p. 155 scan)",
    "tex": r"blank line after \end{equation}, before \oldpage[II]{155} (paragraph break)",
    "kind": "other", "convention": None, "confidence": "high",
    "fix": {"old": r"\tag{8.1.5.4}<NL>\end{equation}<NL><NL>", "new": r"\tag{8.1.5.4}<NL>\end{equation}<NL>"},
    "note": "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line is the last line of this page's segment, so the p. 155 checker cannot see it.",
})

# ---------------- finalize and check ----------------
for f in F:
    fx = f.get("fix")
    if fx:
        fx["old"] = fx["old"].replace("<NL>", "\n")
        fx["new"] = fx["new"].replace("<NL>", "\n")
    if f["kind"] != "misprint_in_print":
        f.pop("corrected", None)

pages = {}
for n in range(150, 155):
    with open(rf"{BASE}\page_{n}.tex", encoding="utf-8", newline="") as fh:
        pages[n] = fh.read().replace("\r\n", "\n")

bad = 0
for i, f in enumerate(F):
    fx = f.get("fix")
    if not fx:
        continue
    c = pages[f["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", i, f["page"], c, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        print("NO-OP", i)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)

from collections import Counter
cnt = Counter()
for f in F:
    k = "convention" if f["kind"] == "convention" else ("misprint" if f["kind"] == "misprint_in_print" else "normal")
    cnt[(f["page"], k)] += 1
for n in range(150, 155):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("total", len(F), "bad", bad)
