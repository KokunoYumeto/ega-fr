import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_100_104.json"


def F(page, where, scan, tex, kind, convention, confidence, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


K1 = ("Residue-field k printed bold italic (convention 1).")
findings = [
    # ---------------- page 100 ----------------
    F(100, "top of the page: 'appli-|cations, où l'on remplace Y par f(X)'",
      "Printed p. 100 begins with 'cations, où l'on remplace Y par f(X), sont bijectives.'; p. 99 ends with "
      "'Pour les deux premières, ... de celle de f(X) les cinq dernières appli-' (page_099_s4.png)",
      "\\oldpage[IV-3]{100} stands two lines early, before 'Pour les deux premières'",
      "marker", None, "high", None, None,
      "Same move as the page-100 entry of findings_095_099.json (marker into appli-|cations), already applied "
      "(FIXLOG.jsonl): no second edit here. The two lines it hands to p. 99 agree with the p. 99 scan word "
      "for word."),
    F(100, "Remarques (10.2.8) (ii): 'on a f*(F ⊗_{Z_Y} G) = f*(F) ⊗_{Z_X} f*(G) à un isomorphisme canonique près'",
      "formula in the running text: 'abéliens sur Y, on a f*(F⊗_{Z_Y}G)=f*(F)⊗_{Z_X}f*(G) à un isomorphisme "
      "canonique près'",
      "displayed with \\[ ... \\]",
      "other", None, "high",
      "on a\n\\[\nf^*(\\mathcal F\\otimes_{\\mathbf Z_Y}\\mathcal G)\n"
      "=f^*(\\mathcal F)\\otimes_{\\mathbf Z_X}f^*(\\mathcal G)\n\\]\nà un",
      "on a\n$f^*(\\mathcal F\\otimes_{\\mathbf Z_Y}\\mathcal G)=f^*(\\mathcal F)\\otimes_{\\mathbf Z_X}"
      "f^*(\\mathcal G)$\nà un",
      "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); the connecting words 'on a' and "
      "'à un isomorphisme canonique près' are kept."),
    F(100, "Remarques (10.2.8): 'le foncteur F ⇝ f*(F)' (display)",
      "wavy arrow ⇝", "\\mapsto",
      "symbol", None, "high",
      "\\mathcal F\\mapsto f^*(\\mathcal F)",
      "\\mathcal F\\leadsto f^*(\\mathcal F)",
      "Wavy maps-to arrow (GLOBAL_ISSUES 33), \\leadsto as in the earlier IV-3 page fixes."),
    # ---------------- page 101 ----------------
    F(101, "title of 10.3", "'10.3. Espaces de Jacobson.' with a full stop", "no full stop",
      "punctuation", None, "high",
      "\\subsection{Espaces de Jacobson}", "\\subsection{Espaces de Jacobson.}",
      "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."),
    F(101, "Définition (10.3.1): 'est un espace de Jacobson si'",
      "'espace de Jacobson' italic like the rest of the definition (no change of face)",
      "\\emph{espace de Jacobson} inside the italic definition environment: upright",
      "convention", 6, "high",
      "un \\emph{espace de Jacobson} si", "un espace de Jacobson si",
      "Drop \\emph inside the italic environment."),
    F(101, "Définition (10.3.1): '(autrement dit, si l'injection canonique X_0→X est un quasi-homéomorphisme).'",
      "'(autrement dit, si l'injection canonique', 'est un' and the closing parenthesis roman; only "
      "'quasi-homéomorphisme' italic (enlarged crop)",
      "the whole parenthesis italic (inside the definition environment)",
      "convention", 6, "high",
      "(autrement\ndit, si l'injection canonique $X_0\\to X$ est un\nquasi-homéomorphisme).",
      "\\textup{(autrement\ndit, si l'injection canonique $X_0\\to X$ est un}\nquasi-homéomorphisme\\textup{)}.",
      "Roman words inside an italic statement; 'quasi-homéomorphisme' stays italic as printed."),
    F(101, "title of 10.4", "'10.4. Préschémas de Jacobson et anneaux de Jacobson.' with a full stop",
      "no full stop",
      "punctuation", None, "high",
      "\\subsection{Préschémas de Jacobson et anneaux de Jacobson}",
      "\\subsection{Préschémas de Jacobson et anneaux de Jacobson.}",
      "GLOBAL_ISSUES 43/58."),
    F(101, "Définition (10.4.1): 'est un préschéma de Jacobson si'",
      "'préschéma de Jacobson' italic like the rest of the definition",
      "\\emph{préschéma de Jacobson} inside the italic definition environment: upright",
      "convention", 6, "high",
      "\\emph{préschéma de Jacobson} si", "préschéma de Jacobson si",
      "Drop \\emph inside the italic environment."),
    F(101, "Définition (10.4.1): 'est un anneau de Jacobson si Spec(A)'",
      "'anneau de Jacobson' italic like the rest of the definition",
      "\\emph{anneau de Jacobson} inside the italic definition environment: upright",
      "convention", 6, "high",
      "\\emph{anneau de Jacobson} si", "anneau de Jacobson si",
      "Drop \\emph inside the italic environment."),
    # ---------------- page 102 ----------------
    F(102, "Lemme (10.4.5.1): 'et un point x∈Z', fermé dans Z'.'",
      "'dans' printed in roman inside the italic statement (wrong fount; enlarged crop: the 'dans' of "
      "'(ou dans Z' on the same line is italic)",
      "italic 'dans' (the TeX silently corrects)",
      "misprint_in_print", None, "high",
      "fermé dans $Z'$", "fermé \\textup{dans} $Z'$",
      "Wrong-fount word in the print (cf. GLOBAL_ISSUES 29): reproduce it in the diplomatic text.",
      corrected="fermé dans $Z'$"),
    F(102, "page end: '... mais il résulte de (5.1.10.1) que | cet ensemble est très dense ...'",
      "mid-sentence page break; p. 103 continues the sentence without a new paragraph",
      "blank line before \\oldpage[IV-3]{103}: paragraph break the print does not have",
      "marker", None, "high",
      "(5.1.10.1) que\n\n", "(5.1.10.1) que\n",
      "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 103 marker itself is in the right place. The edit ends "
      "the p. 102 segment, just before \\oldpage[IV-3]{103}."),
    # ---------------- page 103 ----------------
    F(103, "heading of (10.4.10)",
      "'Applications (10.4.10) : I : Démonstration de (6.15.9). — Soient': 'Applications' and 'Démonstration de' "
      "italic, only the number bold, 'I' and '(6.15.9)' roman; no number before 'Applications' (enlarged crop)",
      "\\begin{env}[10.4.10] prints a bold '(10.4.10)' first, then the hand-made heading all in bold: "
      "'(10.4.10) Applications (10.4.10) : I : Démonstration de (6.15.9). —'",
      "font", None, "high",
      "\\begin{env}[10.4.10]\n\\label{IV.10.4.10-fr}\n"
      "\\textbf{Applications (10.4.10)~: I~: Démonstration de (6.15.9).} --- Soient",
      "\\par\\medskip\\noindent\\label{IV.10.4.10-fr}%\n"
      "\\emph{Applications} \\textbf{(10.4.10)}~: I~: \\emph{Démonstration de} (6.15.9). --- Soient",
      "APPLY TOGETHER with the next finding (it replaces the matching \\end{env}); either alone breaks "
      "compilation. No IV-3 environment prints this heading, so env becomes a plain paragraph with the env's "
      "spacing; the label is kept. Hand-made headings: GLOBAL_ISSUES 40/61."),
    F(103, "end of (10.4.10): '... (où X_0 est l'ensemble des points fermés de X) (10.2.7).'",
      "(companion edit)", "\\end{env} closing the env opened at (10.4.10)",
      "other", None, "high",
      "fermés de $X$) (10.2.7).\n\\end{env}", "fermés de $X$) (10.2.7).\n\\par",
      "APPLY TOGETHER with the previous finding (env opening of (10.4.10) replaced by a plain paragraph)."),
    F(103, "Applications : II : Proposition (10.4.11) (heading and statement)",
      "'Applications : II : Proposition (10.4.11). — Soient S un préschéma, X un S-préschéma de type fini. Tout "
      "S-endomorphisme de X qui est radiciel est surjectif (donc bijectif).': 'Applications' and 'Proposition' "
      "italic, number bold, 'II' roman; the statement italic except '(donc' and the closing parenthesis "
      "(enlarged crop)",
      "\\begin{env}[10.4.11] prints a bold '(10.4.11)' first, then an all-bold hand-made heading; the "
      "statement is upright",
      "font", None, "high",
      "\\begin{env}[10.4.11]\n\\EGAReaderTarget{ega4.c04.statement.10-4-11}{IV.10.4.11-fr}\n"
      "\\textbf{Applications~: II~: Proposition (10.4.11).} --- Soient $S$ un\n"
      "préschéma, $X$ un $S$-préschéma de type fini. Tout $S$-endomorphisme de $X$\n"
      "qui est radiciel est surjectif (donc bijectif).\n\\end{env}",
      "\\par\\medskip\\noindent\\EGAReaderTarget{ega4.c04.statement.10-4-11}{IV.10.4.11-fr}%\n"
      "\\emph{Applications}~: II~: \\emph{Proposition} \\textbf{(10.4.11)}. --- \\emph{Soient $S$ un\n"
      "préschéma, $X$ un $S$-préschéma de type fini. Tout $S$-endomorphisme de $X$\n"
      "qui est radiciel est surjectif} (donc \\emph{bijectif}).\n\\par",
      "One self-contained edit (env opening, heading, italic statement, env closing); the reader target is kept. "
      "Hand-made headings: GLOBAL_ISSUES 40/61."),
    # ---------------- page 104 ----------------
    F(104, "proof of (10.4.11): 'changement de base Spec(k(s))→S'", "bold italic k(s)", "plain k(s)",
      "convention", 1, "high",
      "\\operatorname{Spec}(k(s))\\to S", "\\operatorname{Spec}(\\boldsymbol{k}(s))\\to S", K1),
    F(104, "proof of (10.4.11): 'qui est un k(s)-endomorphisme'", "bold italic k(s)", "plain k(s)",
      "convention", 1, "high",
      "$k(s)$-endomorphisme", "$\\boldsymbol{k}(s)$-endomorphisme", K1),
    F(104, "proof of (10.4.11): 'f^{-1}(s)=X×_S Spec(k(s))'", "bold italic k(s)", "plain k(s)",
      "convention", 1, "high",
      "\\operatorname{Spec}(k(s))$.", "\\operatorname{Spec}(\\boldsymbol{k}(s))$.", K1),
    F(104, "proof of (10.4.11): 'et g(X) est constructible dans X (1.8.5)'",
      "'(1.8.5)' (a reference to EGA IV itself; enlarged crop)", "'(\\textbf{I}, 1.8.5)'",
      "extra", None, "high",
      "dans $X$ (\\textbf{I}, 1.8.5)", "dans $X$ (1.8.5)",
      "GLOBAL_ISSUES 78 (EGA IV's own references written (I, 1.x.y)). '(I, 3.5.7)' and '(I, 6.4.2)' on this page "
      "are printed with I and are right."),
    F(104, "Lemme (10.4.11.1): item labels (i), (ii)",
      "'(i)', '(ii)' upright before the italic items",
      "label=(\\roman*) inside the italic lemma environment: italic",
      "convention", 6, "high",
      "\\begin{enumerate}[label=(\\roman*)]", "\\begin{enumerate}[label=\\textup{(\\roman*)}]",
      "Roman-numeral labels upright in the print (GLOBAL_ISSUES 16); one edit covers both labels."),
    F(104, "Lemme (10.4.11.1) (i): 'il faut et il suffit que k(y) soit un corps fini'", "bold italic k(y)",
      "plain k(y)", "convention", 1, "high",
      "que $k(y)$ soit un corps fini", "que $\\boldsymbol{k}(y)$ soit un corps fini", K1),
    F(104, "Lemme (10.4.11.1) (ii): 'tels que k(y) soit une extension de F_p'", "bold italic k(y)", "plain k(y)",
      "convention", 1, "high",
      "tels que $k(y)$ soit une extension", "tels que $\\boldsymbol{k}(y)$ soit une extension", K1),
    F(104, "proof of (10.4.11.1): 'le degré de k(y) sur F_p divise d'", "bold italic k(y)", "plain k(y)",
      "convention", 1, "high",
      "$k(y)$ sur", "$\\boldsymbol{k}(y)$ sur", K1),
    F(104, "'tels que k(z) soit une extension de F_p de degré divisant d'", "bold italic k(z)", "plain k(z)",
      "convention", 1, "high",
      "tels que $k(z)$ soit", "tels que $\\boldsymbol{k}(z)$ soit", K1),
    F(104, "'k(h(z)) est isomorphe à un sous-corps de k(z)' (first k)", "bold italic k(h(z))", "plain k(h(z))",
      "convention", 1, "high",
      "$k(h(z))$ est isomorphe", "$\\boldsymbol{k}(h(z))$ est isomorphe", K1),
    F(104, "'k(h(z)) est isomorphe à un sous-corps de k(z)' (second k)", "bold italic k(z)", "plain k(z)",
      "convention", 1, "high",
      "sous-corps de $k(z)$", "sous-corps de $\\boldsymbol{k}(z)$", K1),
    F(104, "title of 10.5", "'10.5. Préschémas de Jacobson noethériens.' with a full stop", "no full stop",
      "punctuation", None, "high",
      "\\subsection{Préschémas de Jacobson noethériens}", "\\subsection{Préschémas de Jacobson noethériens.}",
      "GLOBAL_ISSUES 43/58."),
    F(104, "Proposition (10.5.1): 'Les conditions équivalentes a) à d) de (10.4.4) sont alors'",
      "'(10.4.4)' upright (as 'a)' and 'd)'; enlarged crop)",
      "(10.4.4) italic inside the italic proposition environment",
      "convention", 6, "high",
      "de (10.4.4) sont", "de \\textup{(10.4.4)} sont",
      "Roman reference inside an italic statement; \\emph{a)}, \\emph{d)} already come out upright as printed."),
    F(104, "Proposition (10.5.1): item labels e), f)",
      "'e)' and 'f)' italic, like the statement (enlarged crop)",
      "label=\\emph{\\alph*)} inside the italic proposition: upright",
      "convention", 6, "high",
      "\\begin{enumerate}[label=\\emph{\\alph*)}]", "\\begin{enumerate}[label=\\alph*)]",
      "Printed italic labels left upright by \\emph in the italic environment (in (10.4.4) and (10.4.5), p. 102, "
      "the labels are upright as the TeX gives them)."),
    F(104, "proof of (10.5.1): 'du théorème d'Artin-Tate (0, 16.3.3)'", "hyphen 'Artin-Tate'",
      "en dash 'Artin--Tate'",
      "punctuation", None, "high",
      "d'Artin--Tate", "d'Artin-Tate",
      "Same as the Cohen--Macaulay fixes (GLOBAL_ISSUES 74)."),
]

# verify: every old occurs exactly once in its LF-normalised page file; no CR in strings
ok = True
for x in findings:
    fx = x["fix"]
    if fx is None:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c = t.count(fx["old"])
    if c != 1 or "\r" in fx["old"] or "\r" in fx["new"] or fx["old"] == fx["new"]:
        ok = False
        print("PROBLEM", x["page"], c, repr(fx["old"][:80]))
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
counts = {}
for x in findings:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("all old unique:", ok, "| findings:", len(findings))
print(counts)
