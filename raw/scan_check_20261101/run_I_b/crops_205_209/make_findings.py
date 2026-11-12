"""Write findings_205_209.json for the EGA I pp. 205-209 scan check (helper; reads no .tex, writes only the JSON)."""
import json
from pathlib import Path

OUT = Path(r"user\Documents\ega_scan_check_20261101\run_I_b\findings_205_209.json")
NL = "\n"
F = []


def add(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def bold0(page, where, ref, old=None, note="Chapter numeral 0 printed bold."):
    o = old if old else "{0, " + ref + "}"
    add(page, where, "bold 0", "(\\hyperref[0." + ref + "-fr]{0, " + ref + "})", "convention", 2, "high",
        {"old": o, "new": o.replace("{0, ", "{\\textbf{0}, ", 1)}, note)


UPREF = "Reference printed upright inside the italic statement; italic in the TeX environment (checked on a crop)."
LABEL_IT = ("Labels a), b), c) are italic in the roman proof text of the print (checked on a crop); "
            "the TeX sets them roman.")
THREE_755 = "Chapter numeral 0 printed bold. {0, 7.5.5} occurs three times on the page."

# ---------------- page 205 ----------------
bold0(205, "first line: '(0, 3.8.2). En outre, si ℋ est un sous-𝒪_𝔛-Module cohérent'", "3.8.2")
bold0(205, "end of (10.11.6): 'puisque ℱ/ℋ est cohérent (0, 5.3.4)'", "5.3.4")
add(205, "Proposition (10.11.7): 'On peut définir (avec les notations de (10.11.3)) des isomorphismes'",
    "'(avec les notations de (10.11.3))' roman inside the italic statement",
    r"(avec les notations de (\hyperref[I.10.11.3-fr]{10.11.3}))", "convention", 6, "high",
    {"old": r"(avec les" + NL + r"notations de (\hyperref[I.10.11.3-fr]{10.11.3}))",
     "new": r"\textup{(avec les" + NL + r"notations de (\hyperref[I.10.11.3-fr]{10.11.3}))}"},
    "Checked on a crop: '(avec' upright right after italic 'définir'; italic resumes at 'des isomorphismes'. "
    "The 'old' spans the line break after 'les'.")
add(205, "Proposition (10.11.7): 'de 𝒪_𝔛-Modules topologiques (10.11.6)'",
    "(10.11.6) upright inside the italic statement", r"(\hyperref[I.10.11.6-fr]{10.11.6})", "convention", 6, "high",
    {"old": r"(\hyperref[I.10.11.6-fr]{10.11.6})", "new": r"\textup{(\hyperref[I.10.11.6-fr]{10.11.6})}"}, UPREF)
bold0(205, "proof of (10.11.7): 'ce qui a été prouvé dans (0, 7.8.2)'", "7.8.2")
add(205, "Proposition (10.11.9): 'les homomorphismes surjectifs (resp. injectifs, bijectifs)'",
    "'(resp.' roman inside the italic statement; 'injectifs, bijectifs)' italic, closing parenthesis italic",
    "surjectifs (resp. injectifs, bijectifs)", "convention", 6, "high",
    {"old": "surjectifs (resp.", "new": r"surjectifs \textup{(resp.}"},
    "Checked on a crop; the closing parenthesis after 'bijectifs' is italic in the print, as in the TeX.")
bold0(205, "proof of (10.11.9): 'cela a déjà été prouvé dans (0, 7.8.3)'", "7.8.3")

# ---------------- page 206 ----------------
bold0(206, "(10.12.1): '𝒥^n⊂𝒥_1 et 𝒥_1^n⊂𝒥 (10.3.6 et 0, 7.1.4)'", "7.1.4",
      old="et" + NL + r"\hyperref[0.7.1.4-fr]{0, 7.1.4}",
      note="Chapter numeral 0 printed bold. {0, 7.1.4} occurs twice on the page; this 'old' spans the line break "
           "after 'et'.")
F[-1]["tex"] = r"(\hyperref[I.10.3.6-fr]{10.3.6} et \hyperref[0.7.1.4-fr]{0, 7.1.4})"
bold0(206, "(10.12.1): 'est un idéal de définition de A (0, 7.1.4), d'où notre assertion'", "7.1.4",
      old="{0, 7.1.4}), d'où notre")
add(206, "(10.12.2): 'identifient X_m au produit X_n×_{S_n}S_m=(X_n)_{(S_n)}'",
    "(X_n)_{(S_n)}: the index of the inner S is n",
    r"$X_n\times_{S_n}S_m=(X_n)_{(S_m)}$", "misprint_in_print", None, "high",
    {"old": "S_m=(X_n)_{(S_m)}", "new": "S_m=(X_n)_{(S_n)}"},
    "The TeX silently corrects the print. Checked on a 3x crop: the index is n (two arches, like the n of ×_{S_n} "
    "in the same formula), not m. (X_n)_{(S_n)} would be X_n itself; the base change of X_n to S_m is (X_n)_{(S_m)}, "
    "as in '(u_n)_{(S_m)}' three lines below and at the top of p. 207.",
    corrected=r"X_n\times_{S_n}S_m=(X_n)_{(S_m)}")

# ---------------- page 207 ----------------
add(207, "Proposition (10.12.3.1): 'tels que les diagrammes (10.12.2.1) soient commutatifs'",
    "(10.12.2.1) upright inside the italic statement", r"(\hyperref[I.10.12.2.1-fr]{10.12.2.1})", "convention", 6,
    "high", {"old": r"(\hyperref[I.10.12.2.1-fr]{10.12.2.1})",
             "new": r"\textup{(\hyperref[I.10.12.2.1-fr]{10.12.2.1})}"}, UPREF)
add(207, "Proposition (10.12.3.1): 'vérifie les conditions b) et c) de (10.6.3)'",
    "'b)' roman inside the italic statement ('et' italic)", "les conditions b) et c) de", "convention", 6, "high",
    {"old": "conditions b) et", "new": r"conditions \textup{b)} et"}, "Checked on a crop.")
add(207, "Proposition (10.12.3.1): 'vérifie les conditions b) et c) de (10.6.3)'",
    "'c)' roman inside the italic statement ('de' italic)", "les conditions b) et c) de", "convention", 6, "high",
    {"old": "et c) de", "new": r"et \textup{c)} de"}, "Checked on a crop.")
add(207, "Proposition (10.12.3.1): 'b) et c) de (10.6.3) ; soient 𝔛 sa limite inductive'",
    "(10.6.3) upright inside the italic statement", r"(\hyperref[I.10.6.3-fr]{10.6.3})~; soient", "convention", 6,
    "high", {"old": r"(\hyperref[I.10.6.3-fr]{10.6.3})~; soient",
             "new": r"\textup{(\hyperref[I.10.6.3-fr]{10.6.3})}~; soient"},
    UPREF + " (10.6.3) occurs twice on the page; the 'old' includes '~; soient'.")
add(207, "proof of (10.12.3.1): 'donc 𝔎_1=𝔎_1/𝔎_1^2 est de type fini sur B_1'",
    "𝔎_1=𝔎_1/𝔎_1^2: no bar over the first 𝔎_1",
    r"$\overline{\mathfrak{K}}_1=\mathfrak{K}_1/\mathfrak{K}_1^2$", "symbol", None, "high",
    {"old": r"$\overline{\mathfrak{K}}_1=\mathfrak{K}_1/\mathfrak{K}_1^2$",
     "new": r"$\mathfrak{K}_1=\mathfrak{K}_1/\mathfrak{K}_1^2$"},
    "Checked on a 4x crop and a pixel-row profile: nothing above the first 𝔎_1 (the only ink there is the subscript n "
    "of the line above). The printed equality is correct as it stands, so this is not a misprint: by the preceding "
    "sentence the kernel of B_1→B_1 is 𝔎_1^2, so 𝔎_1^2=0 and 𝔎_1/𝔎_1^2=𝔎_1. The overline is an addition of the TeX.")
bold0(207, "proof of (10.12.3.1): 'comme tout idéal de B est fermé (0, 7.3.5)'", "7.3.5")
add(207, "Proposition (10.13.1), label a)", "label 'a)' roman inside the italic statement", r"\item[a)]",
    "convention", 6, "high", {"old": r"\item[a)]", "new": r"\item[\textup{a)}]"},
    "Checked on a crop; \\item[a)] takes the italic of the proposition environment.")
add(207, "Proposition (10.13.1) a): 'f est un morphisme adique (10.12.1) et si l'on pose'",
    "(10.12.1) upright inside the italic statement", r"(\hyperref[I.10.12.1-fr]{10.12.1})", "convention", 6, "high",
    {"old": r"(\hyperref[I.10.12.1-fr]{10.12.1})", "new": r"\textup{(\hyperref[I.10.12.1-fr]{10.12.1})}"}, UPREF)
add(207, "Proposition (10.13.1), label b)", "label 'b)' roman inside the italic statement", r"\item[b)]",
    "convention", 6, "high", {"old": r"\item[b)]", "new": r"\item[\textup{b)}]"}, "Checked on a crop.")

# ---------------- page 208 ----------------
add(208, "Proposition (10.13.1), label c)", "label 'c)' roman inside the italic statement", r"\item[c)]",
    "convention", 6, "high", {"old": r"\item[c)]", "new": r"\item[\textup{c)}]"}, "Checked on a crop.")
add(208, "Proposition (10.13.1) c), label of the property (Q)",
    "'(Q)' in roman: upright, regular weight (not bold), upright parentheses", r"\item[(\textbf{Q})]", "font", None,
    "high", {"old": r"\item[(\textbf{Q})]", "new": r"\item[\textup{(Q)}]"},
    "Checked on a 2x crop: the Q has the stroke weight of the roman V in 'f^{-1}(V)' beside it, while the bold 0 of "
    "(0, 7.5.1) two lines below is clearly heavier. \\textbf{Q} inside the italic statement gives a bold italic Q in "
    "italic parentheses. The fix also sets the label upright (convention 6); no separate convention-6 entry is listed "
    "for this label.")
add(208, "Proposition (10.13.1) (Q): 'séries formelles restreintes (0, 7.5.1) sur Γ(V, 𝒪_𝔜)'",
    "(0, 7.5.1) upright inside the italic statement", r"(\hyperref[0.7.5.1-fr]{0, 7.5.1})", "convention", 6, "high",
    {"old": r"(\hyperref[0.7.5.1-fr]{0, 7.5.1})", "new": r"\textup{(\hyperref[0.7.5.1-fr]{0, 7.5.1})}"},
    UPREF + " Listed before the bold-0 fix of the same reference: in this order both edits apply "
    "('{0, 7.5.1}' survives inside \\textup).")
bold0(208, "Proposition (10.13.1) (Q): 'restreintes (0, 7.5.1)'", "7.5.1",
      note="Chapter numeral 0 printed bold. Apply after the convention-6 fix of the same reference (listed just before).")
add(208, "proof of (10.13.1): 'Il est immédiat que a) entraîne b) en vertu de (10.12.3)'", "a) and b) in italics",
    "que a) entraîne b) en vertu", "italics", None, "high",
    {"old": "que a) entraîne b) en vertu", "new": r"que \emph{a)} entraîne \emph{b)} en vertu"}, LABEL_IT)
add(208, "proof of (10.13.1): 'Pour montrer que b) entraîne c), on peut'", "b) and c) in italics",
    "que b) entraîne c), on", "italics", None, "high",
    {"old": "que b) entraîne c), on", "new": r"que \emph{b)} entraîne \emph{c)}, on"}, LABEL_IT)
add(208, "proof of (10.13.1): 'l'hypothèse b) entraîne que pour m⩽n'", "b) in italics", "l'hypothèse b) entraîne",
    "italics", None, "high", {"old": "l'hypothèse b) entraîne", "new": r"l'hypothèse \emph{b)} entraîne"}, LABEL_IT)
bold0(208, "proof of (10.13.1): 'On en conclut (0, 7.5.5) que A_i est topologiquement isomorphe'", "7.5.5",
      old="{0, 7.5.5}) que", note=THREE_755)
bold0(208, "proof of (10.13.1): 'puisqu'une telle algèbre est noethérienne (0, 7.5.4)'", "7.5.4")
add(208, "proof of (10.13.1): 'Pour démontrer que c) entraîne a), on peut'", "c) and a) in italics",
    "que c) entraîne a)", "italics", None, "high",
    {"old": "que c) entraîne a)", "new": r"que \emph{c)} entraîne \emph{a)}"}, LABEL_IT)
bold0(208, "proof of (10.13.1): 'Alors (0, 7.5.5), A/𝔎A est une algèbre de type fini'", "7.5.5",
      old="{0, 7.5.5}), $A/", note=THREE_755)
add(208, "proof of (10.13.1): 'les conditions de a) sont satisfaites'", "a) in italics", "conditions de a) sont",
    "italics", None, "high", {"old": "conditions de a) sont", "new": r"conditions de \emph{a)} sont"}, LABEL_IT)
add(208, "'On notera que ... la propriété a) est valable'", "a) in italics", "la propriété a) est", "italics", None,
    "high", {"old": "la propriété a) est", "new": r"la propriété \emph{a)} est"}, LABEL_IT)
add(208, "'la propriété a) est valable pour tout Idéal de définition 𝒦 de 𝔜'",
    "only 'tout' in italics; 'Idéal de définition' roman",
    r"\emph{tout Idéal de définition $\mathscr{K}$}", "italics", None, "high",
    {"old": r"\emph{tout Idéal de définition $\mathscr{K}$}", "new": r"\emph{tout} Idéal de définition $\mathscr{K}$"},
    "Checked on a 2x crop: 'Idéal de définition' upright (slightly over-inked, same roman letter shapes).")
add(208, "'(en vertu de c))'", "c) in italics, outer closing parenthesis roman", "(en vertu de c))", "italics", None,
    "high", {"old": "(en vertu de c))", "new": r"(en vertu de \emph{c)})"}, LABEL_IT)
add(208, "'et par suite, dans la propriété b), tous les f_n'", "b) in italics", "propriété b),", "italics", None,
    "high", {"old": "propriété b),", "new": r"propriété \emph{b)},"}, LABEL_IT)
add(208, "'tous les f_n sont des morphismes de type fini.'",
    "only 'tous' in italics; 'les f_n sont des morphismes de type fini' roman",
    r"\emph{tous les $f_n$ sont des morphismes de type fini}", "italics", None, "high",
    {"old": r"\emph{tous les $f_n$ sont des morphismes de type fini}",
     "new": r"\emph{tous} les $f_n$ sont des morphismes de type fini"}, "Checked on a crop.")
add(208, "Corollaire (10.13.2): 'Si les conditions de (10.13.1) sont vérifiées'",
    "(10.13.1) upright inside the italic statement", r"(\hyperref[I.10.13.1-fr]{10.13.1})", "convention", 6, "high",
    {"old": r"Si les conditions de (\hyperref[I.10.13.1-fr]{10.13.1})",
     "new": r"Si les conditions de \textup{(\hyperref[I.10.13.1-fr]{10.13.1})}"},
    UPREF + " (10.13.1) occurs five times on the page; the 'old' includes 'Si les conditions de'.")
add(208, "Corollaire (10.13.2): 'possède la propriété (Q) et si 𝔜 est noethérien'",
    "'(Q)' in roman: upright, regular weight (not bold), upright parentheses", r"(\textbf{Q})", "font", None, "high",
    {"old": r"(\textbf{Q}) et si", "new": r"\textup{(Q)} et si"},
    "Checked on a 3x crop: same regular upright Q as the label (Q) of (10.13.1). The fix also sets it upright "
    "(convention 6); no separate convention-6 entry is listed for it.")
add(208, "Définition (10.13.3): 'Lorsque les propriétés équivalentes a), b), c) de (10.13.1)'",
    "'a), b), c)' roman inside the italic statement ('de' italic)", "équivalentes a), b), c) de", "convention", 6,
    "high", {"old": "équivalentes a), b), c) de", "new": r"équivalentes \textup{a), b), c)} de"}, "Checked on a crop.")
add(208, "Définition (10.13.3): 'a), b), c) de (10.13.1) sont vérifiées'",
    "(10.13.1) upright inside the italic statement", r"(\hyperref[I.10.13.1-fr]{10.13.1})", "convention", 6, "high",
    {"old": r"(\hyperref[I.10.13.1-fr]{10.13.1}) sont vérifiées, on dit",
     "new": r"\textup{(\hyperref[I.10.13.1-fr]{10.13.1})} sont vérifiées, on dit"}, UPREF)
NOFACE = ("Checked on a crop: the defined terms are italic like the rest of the definition (no change of face); "
          "\\emph inside the italic definition environment sets them upright. Drop the \\emph.")
add(208, "Définition (10.13.3): 'on dit que le morphisme f est de type fini'",
    "'de type fini' italic like the rest of the definition (no change of face)", r"\emph{de type fini}",
    "convention", 6, "high", {"old": r"\emph{de type fini}, ou que", "new": r"de type fini, ou que"}, NOFACE)
add(208, "Définition (10.13.3): 'ou que 𝔛 est un 𝔜-préschéma formel de type fini'",
    "'𝔜-préschéma formel de type fini' italic like the rest of the definition (no change of face)",
    r"\emph{$\mathfrak{Y}$-préschéma formel de type fini}", "convention", 6, "high",
    {"old": r"\emph{$\mathfrak{Y}$-préschéma formel de type fini}",
     "new": r"$\mathfrak{Y}$-préschéma formel de type fini"}, NOFACE)
add(208, "Définition (10.13.3): 'ou un préschéma formel de type fini au-dessus de 𝔜'",
    "'préschéma formel de type fini au-dessus de 𝔜' italic like the rest of the definition (no change of face)",
    r"\emph{préschéma formel de type fini au-dessus de $\mathfrak{Y}$}", "convention", 6, "high",
    {"old": r"\emph{préschéma formel de type fini au-dessus de $\mathfrak{Y}$}",
     "new": r"préschéma formel de type fini au-dessus de $\mathfrak{Y}$"}, NOFACE)
bold0(208, "proof of (10.13.4): 'On conclut donc par (0, 7.5.5).'", "7.5.5", old="{0, 7.5.5}).", note=THREE_755)

# ---------------- page 209 ----------------
add(209, "Proposition (10.13.5)(ii): 'trois préschémas formels localement noethériens (resp. noethériens),'",
    "'(resp.' and the closing parenthesis roman inside the italic statement; 'noethériens' italic",
    "localement noethériens (resp. noethériens),", "convention", 6, "high",
    {"old": "noethériens (resp." + NL + "    noethériens),",
     "new": r"noethériens \textup{(resp.}" + NL + r"    noethériens\textup{)},"},
    "Checked on a crop: upright 'resp.' and upright closing parenthesis. The 'old' spans the line break after 'resp.'.")
add(209, "Proposition (10.13.5)(ii): 'est localement noethérien (resp. noethérien) et est de type fini'",
    "'(resp.' and the closing parenthesis roman inside the italic statement; 'noethérien' italic",
    "noethérien (resp. noethérien) et", "convention", 6, "high",
    {"old": "noethérien (resp. noethérien) et", "new": r"noethérien \textup{(resp.} noethérien\textup{)} et"},
    "Checked on a crop: upright 'resp.' and upright closing parenthesis.")
add(209, "Corollaire (10.13.6): 'Sous les hypothèses de (10.9.9), si f est un morphisme de type fini'",
    "(10.9.9) upright inside the italic statement", r"(\hyperref[I.10.9.9-fr]{10.9.9})", "convention", 6, "high",
    {"old": r"(\hyperref[I.10.9.9-fr]{10.9.9})", "new": r"\textup{(\hyperref[I.10.9.9-fr]{10.9.9})}"}, UPREF)
bold0(209, "proof of (10.14.1): '𝒪_𝔛/𝒜 est cohérent en vertu de (10.10.3) et (0, 5.3.4)'", "5.3.4")
bold0(209, "proof of (10.14.1): 'donc son support 𝔜 est fermé (0, 5.2.2)'", "5.2.2")
bold0(209, "proof of (10.14.1): 'est aussi un (𝒪_𝔛/𝒥^{n+1})-Module cohérent (0, 5.3.10)'", "5.3.10")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "findings written to", OUT)
