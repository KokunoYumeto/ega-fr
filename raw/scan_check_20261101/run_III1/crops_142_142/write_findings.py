"""Write findings_142_142.json for EGA III part 1, p. 142, and check that every fix's "old" occurs exactly once
in page_142.tex (CRLF normalised to LF)."""
import json
import pathlib

run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
P = 142


def F(where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = {"page": P, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    F("proof of (4.6.3): 'le fait que u_x soit injectif résulte de (0, 10.2.4)'",
      "(0, 10.2.4) with a bold 0", "(0, 10.2.4)", "convention", 2, "high",
      {"old": "(0, 10.2.4)", "new": "(\\textbf{0}, 10.2.4)"},
      "Bold chapter numeral in the reference."),
    F("proof of (4.6.3): 'a fortiori l'homomorphisme F_x/m_xF_x → G_x/m_xG_x, qui s'en déduit'",
      "formula inline in the text line", "displayed with \\[ ... \\]", "other", None, "high",
      {"old": "l'homomorphisme\n\\[\n\\mathcal F_x/\\mathfrak m_x\\mathcal F_x\n\\longrightarrow\n"
              "\\mathcal G_x/\\mathfrak m_x\\mathcal G_x,\n\\]\nqui s'en",
       "new": "l'homomorphisme\n$\\mathcal F_x/\\mathfrak m_x\\mathcal F_x\n\\longrightarrow\n"
              "\\mathcal G_x/\\mathfrak m_x\\mathcal G_x$,\nqui s'en"},
      ""),
    F("proof of (4.6.3): '(Bourbaki, Alg., chap. VIII, § 6, n° 3, cor. 4 de la prop. 6)'",
      "n with a raised o (n°)", "no~3 (plain 'no')", "symbol", None, "high",
      {"old": "no~3", "new": "n\\textsuperscript{o}~3"},
      "Enlarged crop. Same form as the page-143 fix of no~8."),
    F("Corollaire (4.6.4): 'X_y = X⊗_Y k(y)'",
      "bold italic k", "k(y)", "convention", 1, "high",
      {"old": "$X_y=X\\otimes_Yk(y)$", "new": "$X_y=X\\otimes_Y\\boldsymbol{k}(y)$"},
      "Enlarged crop: slanted bold k, not in a subscript."),
    F("Corollaire (4.6.4): '(avec les notations de (4.6.2)) soient isomorphes'",
      "(4.6.2) upright: roman old-style figures, upright parentheses",
      "italic (reference inside the corollary environment)", "convention", 6, "high",
      {"old": "(\\hyperref[III.4.6.2-fr]{4.6.2})) soient",
       "new": "\\textup{(\\hyperref[III.4.6.2-fr]{4.6.2})}) soient"},
      "Upright reference in an italic statement; the outer closing parenthesis left as on p. 138."),
    F("Corollaire (4.6.5): 'Sous les hypothèses de (4.6.4) sur f, X, Y'",
      "(4.6.4) upright: roman old-style figures, upright parentheses",
      "italic (reference inside the corollary environment)", "convention", 6, "high",
      {"old": "(\\hyperref[III.4.6.4-fr]{4.6.4}) sur $f$",
       "new": "\\textup{(\\hyperref[III.4.6.4-fr]{4.6.4})} sur $f$"},
      "Upright reference in an italic statement."),
    F("Corollaire (4.6.5): 'supposons que H^1(X_y, O_{X_y}) = 0'",
      "the y of the second-level subscript in O_{X_y} is bold italic (wrong fount); the y of X_y just before it is plain",
      "\\mathcal O_{X_y} with a plain y (silently corrected)", "misprint_in_print", None, "high",
      {"old": "$H^1(X_y,\\mathcal O_{X_y})=0$",
       "new": "$H^1(X_y,\\mathcal O_{X_{\\boldsymbol{y}}})=0$"},
      "Crop measurement: stroke half-width 2.1 px and 171 px of ink, against 1.5 px and 125-133 px for the same "
      "second-level y in O_{X_y} of (4.6.4) and (4.6.4.1); heavy terminal instead of the hairline hook.",
      corrected="$H^1(X_y,\\mathcal O_{X_y})=0$"),
    F("Remarques (4.6.6) (i): 'annoncée dans (II, 4.2.7)'",
      "(II, 4.2.7) with a bold II", "(II, 4.2.7)", "convention", 2, "high",
      {"old": "(II, 4.2.7)", "new": "(\\textbf{II}, 4.2.7)"},
      "Bold chapter numeral (stems 9 px against 6 px for the roman I of 'VIII' on this page)."),
    F("Proposition (4.6.7): 'et soit f_z = f×_Z 1 : X⊗_Z k(z) → Y⊗_Z k(z).'",
      "formula inline at the end of the statement's first paragraph; k bold italic in both k(z)",
      "displayed with \\[ ... \\]; plain k", "other", None, "high",
      {"old": "et soit\n\\[\nf_z=f\\times_Z1:\nX\\otimes_Zk(z)\\longrightarrow Y\\otimes_Zk(z).\n\\]",
       "new": "et soit\n$f_z=f\\times_Z1:\nX\\otimes_Z\\boldsymbol{k}(z)\\longrightarrow Y\\otimes_Z\\boldsymbol{k}(z)$."},
      "One edit for the inline setting and the two convention-1 findings below."),
    F("Proposition (4.6.7), same formula, first k(z)",
      "bold italic k", "k(z)", "convention", 1, "high", None,
      "Covered by the edit of the preceding 'other' finding."),
    F("Proposition (4.6.7), same formula, second k(z)",
      "bold italic k", "k(z)", "convention", 1, "high", None,
      "Covered by the edit of the preceding 'other' finding."),
    F("Proposition (4.6.7): item label (i)",
      "(i) upright", "\\item[(i)] comes out italic in the italic proposition", "convention", 6, "high",
      {"old": "\\item[(i)] Si $f_z$", "new": "\\item[\\textup{(i)}] Si $f_z$"},
      "Item label printed upright (GLOBAL_ISSUES 16)."),
    F("Proposition (4.6.7) (i): 'Si f_z est un morphisme fini (resp. une immersion fermée), il existe'",
      "'(resp.' upright, opening parenthesis included", "italic (statement environment)", "convention", 6, "high",
      {"old": "morphisme fini (resp. une immersion fermée), il",
       "new": "morphisme fini \\textup{(resp.} une immersion fermée), il"},
      "Enlarged crop. Same form as the (4.6.3) fix on p. 141."),
    F("Proposition (4.6.7) (i): 'restriction de f, soit un morphisme fini (resp. une immersion fermée).'",
      "'(resp.' upright, opening parenthesis included", "italic (statement environment)", "convention", 6, "high",
      {"old": "soit un morphisme fini (resp.\nune immersion fermée).",
       "new": "soit un morphisme fini \\textup{(resp.}\nune immersion fermée)."},
      "Enlarged crop."),
    F("Proposition (4.6.7): item label (ii)",
      "(ii) upright", "\\item[(ii)] comes out italic in the italic proposition", "convention", 6, "high",
      {"old": "\\item[(ii)] On suppose", "new": "\\item[\\textup{(ii)}] On suppose"},
      "Item label printed upright (GLOBAL_ISSUES 16)."),
    F("proof of (4.6.7): 'il existe un voisinage V_y de y tel que la restriction'",
      "the subscript y of V_y is bold italic (wrong fount); the y of V_y in f^{-1}(V_y)→V_y on the same line is plain",
      "$V_y$ with a plain y (silently corrected)", "misprint_in_print", None, "high",
      {"old": "voisinage $V_y$ de $y$", "new": "voisinage $V_{\\boldsymbol{y}}$ de $y$"},
      "Crop measurement on the same line: stroke half-width 2.2 px and 163 px of ink, against 1.6-1.7 px and "
      "125-129 px for the two V_y of f^{-1}(V_y)→V_y; heavy terminal instead of the hairline hook.",
      corrected="$V_y$"),
    F("proof of (4.6.7): 'si V est la réunion des V_y, la restriction'",
      "the subscript y of V_y is bold italic (wrong fount)",
      "$V_y$ with a plain y (silently corrected)", "misprint_in_print", None, "medium",
      {"old": "réunion des $V_y$", "new": "réunion des $V_{\\boldsymbol{y}}$"},
      "Crop measurement: stroke half-width 2.2 px against 1.6-1.7 px for the plain subscript y two lines above "
      "(the line's other letters are only about 10% heavier); same heavy terminal as the bold y of 'voisinage V_y'.",
      corrected="$V_y$"),
    F("proof of (4.6.7): '(II, 6.1.1 et I, 4.2.4)', the II",
      "II bold", "(II, 6.1.1", "convention", 2, "high",
      {"old": "(II, 6.1.1", "new": "(\\textbf{II}, 6.1.1"},
      "Bold chapter numeral (stems 9 px)."),
    F("proof of (4.6.7): '(II, 6.1.1 et I, 4.2.4)', the I",
      "light roman I (wrong fount): stem 6.5 px and 260 px of ink, as the roman I of 'VIII' on this page "
      "(6 px, 237-251 px); the bold II before it and in (II, 4.2.7) have 9 px stems and 329-344 px",
      "plain I: keeps the printed reading", "misprint_in_print", None, "high", None,
      "Same wrong-fount I as the page-144 finding (I, 10.9.1 et 10.14.2).",
      corrected="\\textbf{I}, 4.2.4"),
    F("proof of (4.6.7), part (i): '(i) Notons tout d'abord'",
      "(i) upright", "\\textit{(i)}", "italics", None, "high",
      {"old": "\\noindent\\textit{(i)} Notons", "new": "\\noindent (i) Notons"},
      "Enlarged crop. Same as the page-143 fix of \\textit{(ii)}."),
    F("proof of (4.6.7), part (i): 'f est un morphisme propre (II, 5.4.3)'",
      "light roman II (wrong fount): first I stem 6 px and 240 px of ink like the roman I of 'VIII'; the second I "
      "damaged (right serifs missing, prints like '[')",
      "(II, 5.4.3) plain: keeps the printed reading", "misprint_in_print", None, "high", None,
      "Not bold, unlike (II, 6.1.1) two lines above (9 px stems).",
      corrected="(\\textbf{II}, 5.4.3)"),
    F("end of page: 'propre (II, 5.4.3); si on' / top of p. 143 'suppose f_z fini'",
      "printed p. 142 ends with 'si on'; p. 143 begins 'suppose f_z fini, l'existence ... résulte de (4.4.11). "
      "Pour traiter le cas ...' as one running paragraph",
      "\\oldpage[III]{143} stands after 'résulte de (4.4.11).' between two blank lines: this page's segment holds "
      "the first sentence of p. 143 and a paragraph break the print lacks",
      "marker", None, "high",
      {"old": "si on suppose $f_z$ fini", "new": "si on\n\\oldpage[III]{143}\nsuppose $f_z$ fini"},
      "Apply together with the removal of the old marker and its blank lines (page 143's segment): "
      "'résulte de (\\hyperref[III.4.4.11-fr]{4.4.11}).\\n\\n\\oldpage[III]{143}\\n\\nPour traiter' -> "
      "'résulte de (\\hyperref[III.4.4.11-fr]{4.4.11}).\\nPour traiter'. The page-143 checker's 'page start' "
      "finding is the same change as one combined edit: apply that or this pair, not both. The moved sentence "
      "matches the print of p. 143 word for word."),
]

page = (run / f"page_{P:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for x in findings:
    if x["fix"]:
        n = page.count(x["fix"]["old"])
        if n != 1:
            bad += 1
            print("NOT UNIQUE (%d):" % n, repr(x["fix"]["old"]))
olds = [x["fix"]["old"] for x in findings if x["fix"]]
for i, a in enumerate(olds):  # edits must not overlap on the page
    sa = page.find(a)
    for b in olds[i + 1:]:
        sb = page.find(b)
        if sa < sb + len(b) and sb < sa + len(a):
            bad += 1
            print("OVERLAP:", repr(a), repr(b))
out = run / f"findings_{P:03d}_{P:03d}.json"
out.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
kinds = {}
for x in findings:
    k = "convention" if x["kind"] == "convention" else ("misprint" if x["kind"] == "misprint_in_print" else "normal")
    kinds[k] = kinds.get(k, 0) + 1
print("written", out.name, len(findings), "findings", kinds, "problems:", bad)
