# Builds findings_045_049.json for EGA IV-3 pp. 45-49 and checks every fix's old string.
import json
import pathlib
from collections import Counter

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_045_049.json"


def N(s):
    """'¶' stands for a line break in the TeX."""
    return s.replace("¶", "\n")


def fx(old, new):
    return {"old": N(old), "new": N(new)}


def F(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def conv2(page, where, ref, numeral, inside_statement=False, note=""):
    bold = ref.replace("(" + numeral + ",", "(\\textbf{" + numeral + "},", 1)
    if inside_statement:
        bold = "\\textup{" + bold + "}"
        note = (note + " " if note else "") + "The edit also sets the reference upright (next entry)."
    return F(page, where, "bold " + numeral + " in the reference",
             ref + ": plain " + numeral + (", italic inside the statement" if inside_statement else ""),
             "convention", 2, "high", fx(ref, bold), note)


L = []

# ---------------- page 45 ----------------
for lab in ("i", "ii", "iii"):
    L.append(F(45, "Corollaire (8.12.4), item label (" + lab + ")",
               "'(" + lab + ")' upright before the italic statement (enlarged crop)",
               "\\item[(" + lab + ")] inside the italic corollary environment: italic",
               "convention", 6, "high",
               fx("\\item[(" + lab + ")]", "\\item[\\textup{(" + lab + ")}]"),
               "Roman-numeral item labels are upright in the print (GLOBAL_ISSUES 16)."))
L.append(F(45, "proof of (8.12.4) (i): 'une factorisation X -g-> Z -u-> Y où g est une immersion'",
           "no comma after the formula (enlarged crop: the line ends with Y)",
           "'$X\\xrightarrow{g}Z\\xrightarrow{u}Y$, où'",
           "punctuation", None, "high",
           fx("Z\\xrightarrow{u}Y$, où", "Z\\xrightarrow{u}Y$ où"), "Extra comma."))
L.append(conv2(45, "proof of (8.12.4) (i): '(I, 4.3.2)'", "(I, 4.3.2)", "I"))
L.append(conv2(45, "proof of (8.12.4) (i): '(II, 6.1.5)'", "(II, 6.1.5)", "II"))
L.append(F(45, "proof of (8.12.4) (ii): 'est la fermeture intégrale de O_{U_λ} dans B_λ et par suite'",
           "'dans 𝓑_λ' (script B with subscript λ; enlarged crop)",
           "'dans $\\mathcal B|U_\\lambda$'",
           "formula", None, "high",
           fx("dans $\\mathcal B|U_\\lambda$ et", "dans $\\mathcal B_\\lambda$ et"),
           "The print abbreviates 𝓑|U_λ and 𝓒|U_λ (written out earlier in the same sentence) as 𝓑_λ, 𝓒_λ; "
           "the TeX normalized the notation. Authors' shorthand, not a misprint: the fix applies to both editions."))
L.append(F(45, "same sentence: 'Z_λ=Spec(C_λ) s'identifie à h^{-1}(U_λ)'",
           "'Spec(𝒞_λ)' (enlarged crop)",
           "'\\operatorname{Spec}(\\mathcal C|U_\\lambda)'",
           "formula", None, "high",
           fx("\\operatorname{Spec}(\\mathcal C|U_\\lambda)", "\\operatorname{Spec}(\\mathcal C_\\lambda)"),
           "As the previous entry."))
L.append(conv2(45, "proof of (8.12.4) (ii): '(I, 4.2.4)'", "(I, 4.2.4)", "I"))
L.append(conv2(45, "(8.12.5): 'Main theorem » de Zariski (III, 4.4.3)'", "(III, 4.4.3)", "III"))
L.append(F(45, "display (8.12.6.1) X -f'-> Y' -u-> Y",
           "no full stop after the display (enlarged crop); 'où f' est une immersion ouverte' continues the sentence",
           "'Y.' before \\tag{8.12.6.1}",
           "punctuation", None, "high",
           fx("\\xrightarrow{u}Y. \\tag{8.12.6.1}", "\\xrightarrow{u}Y \\tag{8.12.6.1}"),
           "Extra full stop in the display."))

# ---------------- page 46 ----------------
L.append(F(46, "proof of (8.12.6): 'en outre (8.10.5, (v) et (xi)) on peut supposer que f_0 est séparé et quasi-fini'",
           "'(v) et (xi)' (enlarged crop)",
           "'(v) et (xii)'",
           "number", None, "high",
           fx("(8.10.5, (v) et (xii))", "(8.10.5, (v) et (xi))"),
           "Transcription error, not a misprint: in (8.10.5) item (v) is 'séparé', (xi) 'quasi-fini', (xii) 'propre', "
           "so the printed (xi) is right; the fix applies to both editions."))
L.append(conv2(46, "proof of (8.12.6): 'déjà fini (II, 6.2.2)'", "(II, 6.2.2)", "II"))
L.append(F(46, "proof of (8.12.6): 'soit U=Y—{a}'",
           "long dash for set difference",
           "$U=Y-\\{a\\}$",
           "convention", 7, "high",
           fx("$U=Y-\\{a\\}$", "$U=Y\\setmin\\{a\\}$"), "Convention 7 (\\setmin, global pass)."))
L.append(F(46, "proof of (8.12.6): 's'identifie à la A'-algèbre B⊗_A A'. D'autre part, comme A est un anneau local excellent'",
           "'D'autre part' continues the same paragraph (flush left, no indent)",
           "blank line before 'D'autre part' (new paragraph)",
           "other", None, "high",
           fx("$B\\otimes_A A'$.¶¶D'autre part", "$B\\otimes_A A'$.¶D'autre part"),
           "Paragraph break the print does not have."))
L.append(F(46, "proof of (8.12.6): 'U'=Y'—{a'}=u^{-1}(U)'",
           "long dash for set difference",
           "U'=Y'-\\{a'\\}",
           "convention", 7, "high",
           fx("U'=Y'-\\{a'\\}", "U'=Y'\\setmin\\{a'\\}"), "Convention 7 (\\setmin, global pass)."))
L.append(conv2(46, "proof of (8.12.6): 'séparé et quasi-fini (II, 6.2.4)'", "(II, 6.2.4)", "II"))
L.append(conv2(46, "proof of (8.12.6): 'on déduit de (II, 6.2.6)'", "(II, 6.2.6)", "II"))

# ---------------- page 47 ----------------
L.append(F(47, "end of the proof of (8.12.6): 'On conclut bien que g' est une immersion ouverte, C.Q.F.D.'",
           "'immersion ouverte, C.Q.F.D.'",
           "'immersion ouverte.' (no C.Q.F.D.)",
           "missing", None, "high",
           fx("immersion ouverte.¶\\end{proof}", "immersion ouverte, C.Q.F.D.¶\\end{proof}"),
           "The source writes C.Q.F.D. as text elsewhere (e.g. ega4-8-fr.tex line 694)."))
L.append(conv2(47, "Corollaire (8.12.8): 'un O_Y-Module ample (II, 4.5.3)'", "(II, 4.5.3)", "II",
               inside_statement=True))
L.append(F(47, "Corollaire (8.12.8): same reference '(II, 4.5.3)'",
           "the reference is upright inside the italic statement (crop)",
           "(II, 4.5.3) inside the italic corollary environment: italic",
           "convention", 6, "high", None, "Included in the convention-2 edit of the previous entry."))
L.append(conv2(47, "proof of (8.12.8): 'Z=P^r_Y (II, 5.3.3)'", "(II, 5.3.3)", "II",
               note="The bold P of P^r_Y is upright here (crop), as \\mathbf P: no convention 10."))
L.append(conv2(47, "proof of (8.12.8): 'de la définition (II, 4.1.1)'", "(II, 4.1.1)", "II"))
L.append(conv2(47, "proof of (8.12.8): 'de type fini J_λ (I, 9.4.9)'", "(I, 9.4.9)", "I"))
L.append(F(47, "proof of (8.12.8): 'soit un k(y)-préschéma fini'",
           "bold italic k", "plain k",
           "convention", 1, "high",
           fx("$k(y)$-préschéma fini", "$\\boldsymbol{k}(y)$-préschéma fini"), ""))
L.append(F(47, "proof of (8.12.8): 'restriction de g à X_λ, est donc quasi-fini.'",
           "'quasi-fini' italic (enlarged crop)", "upright",
           "italics", None, "high",
           fx("est donc¶quasi-fini.", "est donc¶\\emph{quasi-fini}."), ""))

# ---------------- page 48 ----------------
L.append(F(48, "proof of (8.12.9): 'pour U un voisinage affine de x dans X contenu dans f^{-1}(U)'",
           "f^{-1}(U) (enlarged crop)",
           "f^{-1}(U): the TeX keeps the printed reading",
           "misprint_in_print", None, "high", None,
           "U is to lie in the inverse image of the affine neighbourhood V of y chosen just before; "
           "'contenu dans f^{-1}(U)' is circular. Diplomatic TeX already right; the corrected edition needs f^{-1}(V).",
           corrected="$f^{-1}(V)$"))
L.append(conv2(48, "proof of (8.12.10): 'de la première et de (I, 8.2.8)'", "(I, 8.2.8)", "I"))
L.append(conv2(48, "proof of (8.12.10): 'en vertu de (I, 5.2.3)'", "(I, 5.2.3)", "I"))
L.append(F(48, "proof of (8.12.10.1): 'de sorte que A est une O_Y-Algèbre finie, Y' s'identifiant'",
           "'finie' italic (enlarged crop)", "upright",
           "italics", None, "high",
           fx("-Algèbre finie,", "-Algèbre \\emph{finie},"), ""))
L.append(conv2(48, "proof of (8.12.10.1): 'Spec(A) (II, 1.3.6)'", "(II, 1.3.6)", "II"))
L.append(conv2(48, "Corollaire (8.12.11): 'relativement à L (II, 6.3.4)'", "(II, 6.3.4)", "II",
               inside_statement=True))
L.append(F(48, "Corollaire (8.12.11): same reference '(II, 6.3.4)'",
           "the reference is upright inside the italic statement (crop)",
           "(II, 6.3.4) inside the italic corollary environment: italic",
           "convention", 6, "high", None, "Included in the convention-2 edit of the previous entry."))
L.append(conv2(48, "proof of (8.12.11): 'résultent de (II, 6.3.9)'", "(II, 6.3.9)", "II"))
L.append(F(48, "proof of (8.12.11): 'Il résulte de (II, 6.2.4, (v))'",
           "bold II in the reference", "(II, 6.2.4, (v)): plain II",
           "convention", 2, "high",
           fx("(II, 6.2.4, (v))", "(\\textbf{II}, 6.2.4, (v))"), ""))
L.append(conv2(48, "proof of (8.12.11): 'il résulte de (I, 5.5.1)'", "(I, 5.5.1)", "I"))

# ---------------- page 49 ----------------
L.append(F(49, "heading 8.13",
           "'8.13. Traduction en termes de pro-objets.' (final full stop)",
           "\\subsection{Traduction en termes de pro-objets} (no full stop)",
           "punctuation", None, "high",
           fx("\\subsection{Traduction en termes de pro-objets}", "\\subsection{Traduction en termes de pro-objets.}"),
           "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); same fix as the IV-2 headings."))
L.append(F(49, "Proposition (8.13.1): '(ce qui entraîne (II, 1.6.2) que ...'",
           "bold II; the reference is upright inside the italic statement",
           "(II, 1.6.2): plain II, italic inside the proposition",
           "convention", 2, "high",
           fx("entraîne (II, 1.6.2)", "entraîne \\textup{(\\textbf{II}, 1.6.2)}"),
           "The edit also sets the reference upright (next entry)."))
L.append(F(49, "Proposition (8.13.1): same reference '(II, 1.6.2)'",
           "the reference is upright inside the italic statement (crop)",
           "italic (proposition environment)",
           "convention", 6, "high", None, "Included in the convention-2 edit of the previous entry."))
L.append(F(49, "Proposition (8.13.1): '(ce qui entraîne (II, 1.6.2) que v_λμ est affine pour α⩽λ⩽μ)'",
           "'est affine' (enlarged crop)", "'soit affine'",
           "word", None, "high",
           fx("$v_{\\lambda\\mu}$ soit affine", "$v_{\\lambda\\mu}$ est affine"), ""))
L.append(F(49, "Proposition (8.13.1): 'la limite projective X=lim X_λ existe'",
           "lim with the arrow below and no index (enlarged crop)",
           "\\varprojlim_\\lambda (index λ)",
           "extra", None, "high",
           fx("X=\\varprojlim_\\lambda X_\\lambda", "X=\\varprojlim X_\\lambda"),
           "GLOBAL_ISSUES 30 (lim indices the print lacks)."))
L.append(F(49, "Proposition (8.13.1): 'des S-préschémas (8.2.3). Soit Y'",
           "the reference (8.2.3) is upright inside the italic statement (crop)",
           "(8.2.3) inside the italic proposition environment: italic",
           "convention", 6, "high",
           fx("(8.2.3). Soit $Y$", "\\textup{(8.2.3)}. Soit $Y$"), ""))
L.append(F(49, "Proposition (8.13.1): 'soit e_λ : Hom_S(X_λ, Y) → Hom_S(X, Y) l'application qui'",
           "the formula is in the running text (same line as 'tout λ⩾α, soit' and 'l'application qui')",
           "set as a display \\[ ... \\]",
           "other", None, "high",
           fx("soit¶\\[¶e_\\lambda:\\operatorname{Hom}_S(X_\\lambda,Y)¶\\longrightarrow\\operatorname{Hom}_S(X,Y)¶\\]¶l'application",
              "soit¶$e_\\lambda:\\operatorname{Hom}_S(X_\\lambda,Y)¶\\to\\operatorname{Hom}_S(X,Y)$¶l'application"),
           "Formula displayed where the print has it inline (GLOBAL_ISSUES 21)."))
L.append(F(49, "display (8.13.1.1): 'lim Hom_S(X_λ, Y) → Hom_S(X, Y).'",
           "lim with the arrow below and no index (enlarged crop)",
           "\\varinjlim_\\lambda (index λ)",
           "extra", None, "high",
           fx("\\varinjlim_\\lambda\\operatorname{Hom}_S(X_\\lambda,Y)", "\\varinjlim\\operatorname{Hom}_S(X_\\lambda,Y)"),
           "GLOBAL_ISSUES 30."))
L.append(F(49, "Proposition (8.13.1), after display (8.13.1.1): 'Supposons X_α quasi-compact ...'",
           "new indented paragraph after the display",
           "no blank line after \\end{equation}: the paragraph continues",
           "other", None, "high",
           fx("\\end{equation}¶Supposons", "\\end{equation}¶¶Supposons"),
           "Paragraph break the print has and the TeX lacks (GLOBAL_ISSUES 47 pattern)."))
L.append(F(49, "Proposition (8.13.1): 'Supposons X_α quasi-compact (resp. quasi-compact et quasi-séparé)'",
           "'resp.' upright inside the italic statement (crop)", "(resp. ...): italic",
           "convention", 6, "high",
           fx("quasi-compact (resp. quasi-compact", "quasi-compact (\\textup{resp.} quasi-compact"), ""))
L.append(F(49, "Proposition (8.13.1): 'localement de type fini (resp. localement de présentation finie)'",
           "'resp.' upright inside the italic statement (crop)", "(resp. ...): italic",
           "convention", 6, "high",
           fx("type fini (resp. localement", "type fini (\\textup{resp.} localement"), ""))
L.append(F(49, "Proposition (8.13.1): 'Alors l'application (8.13.1.1) est injective'",
           "the reference (8.13.1.1) is upright inside the italic statement (crop)",
           "(8.13.1.1) inside the italic proposition environment: italic",
           "convention", 6, "high",
           fx("l'application (8.13.1.1) est", "l'application \\textup{(8.13.1.1)} est"), ""))
L.append(F(49, "Proposition (8.13.1): 'est injective (resp. bijective)'",
           "'resp.' upright inside the italic statement (crop)", "(resp. bijective): italic",
           "convention", 6, "high",
           fx("injective (resp.¶bijective)", "injective (\\textup{resp.}¶bijective)"), ""))
L.append(F(49, "proof of (8.13.1): 'si l'on pose aussi w_λμ=1×v_λμ : Z_μ→Z_λ pour α⩽λ⩽μ et w_λ=1×v_λ : Z→Z_λ pour α⩽λ, Z est limite'",
           "both formulas in the running text, joined by 'pour ... et ... pour'",
           "one display with the conditions in parentheses after \\quad and the two formulas joined by \\qquad: "
           "the words 'pour', 'et', 'pour' are missing",
           "missing", None, "high",
           fx("\\[¶w_{\\lambda\\mu}=1\\times v_{\\lambda\\mu}:Z_\\mu\\to Z_\\lambda¶\\quad(\\alpha\\leqslant\\lambda\\leqslant\\mu),¶"
              "\\qquad¶w_\\lambda=1\\times v_\\lambda:Z\\to Z_\\lambda¶\\quad(\\alpha\\leqslant\\lambda),¶\\]¶$Z$ est limite",
              "$w_{\\lambda\\mu}=1\\times v_{\\lambda\\mu}:Z_\\mu\\to Z_\\lambda$¶pour $\\alpha\\leqslant\\lambda\\leqslant\\mu$ et¶"
              "$w_\\lambda=1\\times v_\\lambda:Z\\to Z_\\lambda$ pour $\\alpha\\leqslant\\lambda$,¶$Z$ est limite"),
           "One edit for display to inline and the lost connecting words (GLOBAL_ISSUES 21/51)."))
L.append(conv2(49, "proof of (8.13.1): '(I, 3.3.14). Il suffit maintenant'", "(I, 3.3.14)", "I"))
L.append(F(49, "Corollaire (8.13.2): 'Avec les notations de (8.13.1), on suppose'",
           "the reference (8.13.1) is upright inside the italic statement (crop)",
           "(8.13.1) inside the italic corollary environment: italic",
           "convention", 6, "high",
           fx("notations de (8.13.1), on", "notations de \\textup{(8.13.1)}, on"), ""))
L.append(F(49, "Corollaire (8.13.2): 'on suppose en outre que Y=lim Y_ρ, où (Y_ρ, t_ρσ)'",
           "lim with the arrow below and no index (enlarged crop)",
           "\\varprojlim_\\rho (index ρ)",
           "extra", None, "high",
           fx("Y=\\varprojlim_\\rho Y_\\rho", "Y=\\varprojlim Y_\\rho"),
           "GLOBAL_ISSUES 30. In the display (8.13.2.1) and in the two formulas of the proof the print does have the indices ρ, λ."))
L.append(F(49, "proof of (8.13.2): 'l'application canonique Hom_S(X, Y) → lim_ρ Hom_S(X, Y_ρ) est bijective'",
           "the formula is in the running text (same line as 'l'application canonique' and 'est bijective'; index ρ under the arrow)",
           "set as a display \\[ ... \\]",
           "other", None, "high",
           fx("canonique¶\\[¶\\operatorname{Hom}_S(X,Y)\\longrightarrow¶\\varprojlim_\\rho\\operatorname{Hom}_S(X,Y_\\rho)¶\\]¶est bijective",
              "canonique¶$\\operatorname{Hom}_S(X,Y)\\to¶\\varprojlim_\\rho\\operatorname{Hom}_S(X,Y_\\rho)$¶est bijective"),
           "Formula displayed where the print has it inline (GLOBAL_ISSUES 21)."))
L.append(F(49, "proof of (8.13.2): 'une bijection canonique Hom_S(X, Y_ρ) ⥲ lim_λ Hom_S(S_λ, Y_ρ) en vertu de (8.13.1)'",
           "the formula is in the running text (same line as 'en vertu de (8.13.1); d'où la conclusion.'; index λ under the arrow)",
           "set as a display \\[ ... \\]",
           "other", None, "high",
           fx("\\[¶\\operatorname{Hom}_S(X,Y_\\rho)\\xrightarrow{\\sim}¶\\varinjlim_\\lambda\\operatorname{Hom}_S(S_\\lambda,Y_\\rho)¶\\]¶en vertu",
              "$\\operatorname{Hom}_S(X,Y_\\rho)\\xrightarrow{\\sim}¶\\varinjlim_\\lambda\\operatorname{Hom}_S(S_\\lambda,Y_\\rho)$¶en vertu"),
           "Formula displayed where the print has it inline (GLOBAL_ISSUES 21). Leaves the printed S_λ (misprint, next entry) unchanged; apply this edit before the corrected edition's misprint correction."))
L.append(F(49, "proof of (8.13.2): 'Hom_S(X, Y_ρ) ⥲ lim_λ Hom_S(S_λ, Y_ρ) en vertu de (8.13.1)'",
           "Hom_S(S_λ, Y_ρ) (enlarged crop)",
           "\\operatorname{Hom}_S(S_\\lambda,Y_\\rho): the TeX keeps the printed reading",
           "misprint_in_print", None, "high", None,
           "By (8.13.1) applied to Y_ρ the bijection is with lim_λ Hom_S(X_λ, Y_ρ), as in (8.13.2.1); S_λ is the "
           "notation of (8.8.2) (the proof of (8.13.1) puts X_λ=S_λ). Diplomatic TeX already right; in the corrected "
           "edition replace \\operatorname{Hom}_S(S_\\lambda,Y_\\rho) (once on the page) by the corrected reading.",
           corrected="\\operatorname{Hom}_S(X_\\lambda,Y_\\rho)"))

# ---------------- checks ----------------
pages = {}
for d in L:
    p = d["page"]
    if p not in pages:
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
bad = 0
for d in L:
    if d["fix"] is None:
        continue
    t = pages[d["page"]]
    c = t.count(d["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], c, repr(d["fix"]["old"]))
# apply in order on copies: each old must still occur exactly once at its turn
work = dict(pages)
for d in L:
    if d["fix"] is None:
        continue
    t = work[d["page"]]
    c = t.count(d["fix"]["old"])
    if c != 1:
        bad += 1
        print("SEQUENTIAL FAIL", d["page"], c, repr(d["fix"]["old"]))
        continue
    work[d["page"]] = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")
cnt = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in sorted(pages):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("entries", len(L), "bad", bad)
