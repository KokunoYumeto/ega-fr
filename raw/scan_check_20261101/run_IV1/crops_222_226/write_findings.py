"""Write findings_222_226.json for run_IV1 and check that every fix's "old" occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV1")
OUT = RUN / "findings_222_226.json"


def F(page, where, scan, tex, kind, old, new, note="", convention=None, confidence="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention, confidence=confidence,
             fix=(dict(old=old, new=new) if old is not None else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def C2(page, where, old, new, scan, tex, note=""):
    return F(page, where, scan, tex, "convention", old, new, note, convention=2)


def C6(page, where, old, new, scan, tex, note=""):
    return F(page, where, scan, tex, "convention", old, new, note, convention=6)


L = []

# ---------------- page 223 ----------------
for n, where in (("1", "item c 1)"), ("2", "item c 2)"), ("3", "item c 3)")):
    L.append(F(223, where + ", label",
               f"label 'c {n})': only the c is italic; the figure {n} and the parenthesis are roman (enlarged crop)",
               f"\\emph{{c {n})}} (figure and parenthesis italic too)", "italics",
               f"\\emph{{c {n})}}", f"\\emph{{c}} {n})",
               "Labels a), b), c) are wholly italic in the print and correctly \\emph{a)} etc. in the TeX."))
    if n == "2":
        L.append(F(223, "item c 2), l. 1-2",
                   "'des techniques noethériennes': 'techniques' roman, only 'noethériennes' italic (enlarged crop)",
                   "\\emph{techniques noethériennes}", "italics",
                   "\\emph{techniques noethériennes}", "techniques \\emph{noethériennes}"))
L.append(F(223, "end of page, 'image réciproque (par un morphisme' | p. 224 'quelconque)'",
           "the sentence runs on over the page break: p. 224 begins 'quelconque) et par image directe' flush left, no new paragraph",
           "blank line before \\oldpage[IV-1]{224} (and after it): paragraph break inside the sentence", "other",
           "(par un morphisme\n\n", "(par un morphisme\n",
           "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 224 "
           "entry that removes the blank line after the marker."))

# ---------------- page 224 ----------------
L.append(F(224, "top of page",
           "page begins mid-sentence: 'quelconque) et par image directe ...' (no indent, same paragraph as p. 223)",
           "\\oldpage[IV-1]{224} followed by a blank line", "other",
           "\\oldpage[IV-1]{224}\n\nquelconque)", "\\oldpage[IV-1]{224}\nquelconque)",
           "Apply together with the p. 223 entry '(par un morphisme' (blank line before the marker)."))
L.append(C2(224, "§ 1, introduction, l. 3", "(I, 6.3 et 6.6)", "(\\textbf{I}, 6.3 et 6.6)",
            "(I, 6.3 et 6.6) with a bold I", "(I, 6.3 et 6.6), plain I",
            "The second '(I, 6.3' of the page is split by a line break and is the next-but-four entry."))
L.append(C2(224, "§ 1, introduction, l. 5", "dans (I, 6.6.1)", "dans (\\textbf{I}, 6.6.1)",
            "(définie dans (I, 6.6.1)), bold I", "plain I"))
L.append(C2(224, "§ 1, introduction, l. 7", "(I, 6.6.2)", "(\\textbf{I}, 6.6.2)",
            "(définie dans (I, 6.6.2)), bold I", "plain I"))
L.append(C2(224, "§ 1, introduction, l. 9", "(I, 6.3.1)", "(\\textbf{I}, 6.3.1)",
            "(définie dans (I, 6.3.1)), bold I", "plain I"))
L.append(C2(224, "§ 1, introduction, l. 11", "(I, 6.3\net 6.6)", "(\\textbf{I}, 6.3\net 6.6)",
            "énoncées dans (I, 6.3 et 6.6), bold I", "plain I"))
L.append(C2(224, "§ 1, second paragraph", "(0\\textsubscript{III}, §~9)", "(\\textbf{0}\\textsubscript{III}, §~9)",
            "(0_III, § 9) with a bold 0", "(0\\textsubscript{III}, §~9), plain 0"))
L.append(F(224, "heading 1.1",
           "'1.1. Morphismes quasi-compacts.' (final full stop)", "\\subsection{Morphismes quasi-compacts} (no full stop)",
           "punctuation", "\\subsection{Morphismes quasi-compacts}", "\\subsection{Morphismes quasi-compacts.}",
           "GLOBAL_ISSUES 43/58: no \\subsection title in ega4-1-fr.tex has the printed full stop either (1.2 on p. 226 too)."))
L.append(C6(224, "Définition (1.1.1), l. 1", "est \\emph{quasi-compact} si", "est quasi-compact si",
            "'est quasi-compact si' all italic, like the rest of the statement (enlarged crop)",
            "\\emph{quasi-compact} inside the italic definition: comes out upright",
            "Printed italic word left upright by \\emph inside the itshape environment."))
L.append(C2(224, "Définition (1.1.1), l. 3", "(0\\textsubscript{III}, 9.1.1)",
            "\\textup{(\\textbf{0}\\textsubscript{III}, 9.1.1)}",
            "(0_III, 9.1.1) upright inside the italic statement, bold 0 (enlarged crop)",
            "(0\\textsubscript{III}, 9.1.1): plain 0, and italic (parentheses, III, numbers) inside the definition",
            "Bold 0 (convention 2) and roman reference inside an italic statement (convention 6), one edit as in the "
            "run_0IV1 findings."))
L.append(C2(224, "Définition (1.1.1), end", "(cf. (I, 6.6.1))", "\\textup{(cf. (\\textbf{I}, 6.6.1))}",
            "(cf. (I, 6.6.1)) upright inside the italic statement ('cf.' roman), bold I (enlarged crop)",
            "(cf. (I, 6.6.1)): plain I, italic inside the definition",
            "Convention 2 with convention 6 (roman reference in an italic statement), one edit."))
L.append(C2(224, "paragraph after (1.1.1), end", "est quasi-compact (I, 6.6.1)", "est quasi-compact (\\textbf{I}, 6.6.1)",
            "quasi-compact (I, 6.6.1), bold I", "plain I"))
L.append(F(224, "end of page, 'alors f est quasi-compact. Par' | p. 225 'suite, si'",
           "the sentence 'Par suite, si ...' runs on over the page break; p. 225 begins 'suite,' flush left",
           "blank line before \\oldpage[IV-1]{225} (and after it): paragraph break inside 'Par suite'", "other",
           "quasi-compact. Par\n\n", "quasi-compact. Par\n",
           "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 225 entry that removes the blank "
           "line after the marker."))

# ---------------- page 225 ----------------
L.append(F(225, "top of page", "page begins mid-sentence 'suite, si f : X -> Y ...' (no indent)",
           "\\oldpage[IV-1]{225} followed by a blank line", "other",
           "\\oldpage[IV-1]{225}\n\nsuite, si", "\\oldpage[IV-1]{225}\nsuite, si",
           "Apply together with the p. 224 entry 'quasi-compact. Par' (blank line before the marker)."))
for lab in ("i", "ii", "iii", "iv", "v", "vi"):
    L.append(C6(225, f"Proposition (1.1.2), label ({lab})", f"\\item[({lab})]", f"\\item[\\textup{{({lab})}}]",
                f"label ({lab}) upright roman", f"\\item[({lab})] comes out italic in the italic proposition",
                "Roman-numeral item labels in italic statements are upright in the print (GLOBAL_ISSUES 16)."))
L.append(C2(225, "after (1.1.2)", "(I, 6.6.4)", "(\\textbf{I}, 6.6.4)",
            "Pour la démonstration, voir (I, 6.6.4): bold I", "plain I"))
L.append(C6(225, "Corollaire (1.1.4), l. 2", "(resp.\nsurjectif)", "\\textup{(resp.}\nsurjectif\\textup{)}",
            "'(resp. surjectif)': '(resp.' and the closing parenthesis roman, 'surjectif' italic (600-dpi crop)",
            "(resp. surjectif) all italic inside the corollary"))
L.append(C6(225, "Corollaire (1.1.4), l. 3", "(resp. dominant), il suffit",
            "\\textup{(resp.} dominant\\textup{)}, il suffit",
            "'(resp. dominant)': '(resp.' and the closing parenthesis roman, 'dominant' italic (enlarged crop)",
            "(resp. dominant) all italic inside the corollary"))
L.append(C2(225, "proof of (1.1.4), l. 1", "(I, 3.5.2)", "(\\textbf{I}, 3.5.2)",
            "morphisme surjectif (I, 3.5.2): bold I", "plain I"))

# ---------------- page 226 (first: text printed on p. 225, before the misplaced p. 226 marker) ----------------
W225 = "printed p. 225 (text that precedes the misplaced p. 226 marker; in page_226.tex)"
for lab in ("a", "b", "c"):
    L.append(C6(226, f"{W225}: Proposition (1.1.5), label {lab})", f"\\item[{lab})]", f"\\item[\\textup{{{lab})}}]",
                f"label {lab}) upright roman, letter and parenthesis (enlarged crop)",
                f"\\item[{lab})] comes out italic in the italic proposition",
                "In the following proof the references a), c), b) are italic and are right as \\emph{..}."))
L.append(F(226, f"{W225}: Proposition (1.1.5) b)",
           "on a f^{-1}(y) ≠ 0 ; the sign after ≠ is the x-height figure 0 (old-style zero, as in '10' of '§§ 8 à 10'), "
           "no slash; the empty set of this fascicle is the full-height slashed Ø (pp. 241, 242: X = Ø, u^{-1}(y) = Ø)",
           "$f^{-1}(y)\\neq\\varnothing$ (silent correction)", "misprint_in_print",
           "\\neq\\varnothing", "\\neq 0",
           "Misprint: a set is meant to be non-empty; the print sets the figure 0 for the empty set. The TeX silently "
           "corrects it; the diplomatic text gets the printed 0 back. Enlarged 600-dpi crop. Apply before the p. 226 "
           "marker move (end of this page's entries).",
           corrected="\\neq\\varnothing"))
L.append(C2(226, f"{W225}: proof of (1.1.5)", "(I, 6.6.5)", "(\\textbf{I}, 6.6.5)",
            "démontrée dans (I, 6.6.5): bold I", "plain I", "Apply before the p. 226 marker move."))
# printed p. 226 proper
L.append(C2(226, "top of p. 226, proof of (1.1.5)", "(0\\textsubscript{I}, 2.1.6)",
            "(\\textbf{0}\\textsubscript{I}, 2.1.6)", "(0_I, 2.1.6), bold 0", "plain 0"))
L.append(C2(226, "proof of (1.1.5), last line", "(0\\textsubscript{I}, 2.1.5)",
            "(\\textbf{0}\\textsubscript{I}, 2.1.5)", "(0_I, 2.1.5), bold 0", "plain 0"))
L.append(F(226, "Proposition (1.1.6), l. 2",
           "X' ⨿ X'': small coproduct sign (x-height, inverted Π) as a binary sign (600-dpi crop)",
           "$X'\\coprod X''$ (large-operator ∐)", "symbol", "$X'\\coprod X''$", "$X'\\amalg X''$",
           "As the run_II pages 11 and 83 (\\amalg for the printed small coproduct sign; GLOBAL_ISSUES 6).",
           confidence="medium"))
L.append(F(226, "heading 1.2",
           "'1.2. Morphismes quasi-séparés.' (final full stop)", "\\subsection{Morphismes quasi-séparés} (no full stop)",
           "punctuation", "\\subsection{Morphismes quasi-séparés}", "\\subsection{Morphismes quasi-séparés.}",
           "As heading 1.1 on p. 224 (GLOBAL_ISSUES 43)."))
L.append(C6(226, "Définition (1.2.1), l. 1-2", "est\n\\emph{quasi-séparé}", "est\nquasi-séparé",
            "'est quasi-séparé' italic like the rest of the statement (enlarged crop)",
            "\\emph{quasi-séparé} inside the italic definition: upright",
            "The next two entries concern the same line: '(ou que' is roman and 'est quasi-séparé sur' italic in the "
            "print, the reverse of the TeX. The three edits do not overlap."))
L.append(C6(226, "Définition (1.2.1), l. 2", "(ou que $X$ est", "\\textup{(ou que} $X$ est",
            "'(ou que' roman, with an upright opening parenthesis (600-dpi crop; the parenthesis of '(en particulier' "
            "in (1.2.2) (i) is slanted for comparison)",
            "(ou que set italic by the environment"))
L.append(C6(226, "Définition (1.2.1), l. 2", "\\emph{quasi-séparé sur} $Y$) si", "quasi-séparé sur $Y$\\textup{)} si",
            "'est quasi-séparé sur Y)': 'quasi-séparé sur' italic, the closing parenthesis upright (600-dpi crop)",
            "\\emph{quasi-séparé sur} upright, closing parenthesis italic"))
L.append(C6(226, "Définition (1.2.1), l. 3", "est \\emph{quasi-séparé} s'il", "est quasi-séparé s'il",
            "'On dit qu'un préschéma X est quasi-séparé s'il est quasi-séparé sur Spec(Z)': all italic",
            "\\emph{quasi-séparé} upright"))
L.append(C2(226, "paragraph after (1.2.1)", "(I, 5.4.1)", "(\\textbf{I}, 5.4.1)",
            "Spec(Z) (I, 5.4.1): bold I", "plain I"))
for lab in ("i", "ii", "iii", "iv", "v", "vi"):
    L.append(C6(226, f"Proposition (1.2.2), label ({lab})", f"\\item[({lab})]", f"\\item[\\textup{{({lab})}}]",
                f"label ({lab}) upright roman", f"\\item[({lab})] comes out italic in the italic proposition"))
L.append(C2(226, "proof of (1.2.2), l. 1", "(I, 5.5.12)", "(\\textbf{I}, 5.5.12)",
            "En vertu de (I, 5.5.12): bold I", "plain I"))
L.append(C2(226, "proof of (1.2.2), l. 2", "(I, 5.5.1)", "(\\textbf{I}, 5.5.1)",
            "séparé (I, 5.5.1): bold I", "plain I"))
L.append(C2(226, "proof of (1.2.2), l. 3", "(I, 3.3.11)", "(\\textbf{I}, 3.3.11)",
            "Y = S (I, 3.3.11): bold I", "plain I"))
L.append(C2(226, "proof of (1.2.2), l. 4", "(I, 5.3.4)", "(\\textbf{I}, 5.3.4)",
            "(Δ_f)_(S') (I, 5.3.4): bold I", "plain I"))
# marker move 225/226 (last entries of the page)
MV = ("Marker move, two edits applied together and AFTER every other page-226 entry above (those in the "
      "printed-p.-225 text are found only while the old marker stands). ")
L.append(F(226, "page break 225/226 (part 1 of 2: new marker)",
           "printed p. 225 ends '... donc est contenu dans la composante irréduc-'; p. 226 begins 'tible Y' = {y}-bar de Y "
           "(0_I, 2.1.6)'. The paragraph 'Pour abréger ...', Proposition (1.1.5) and the start of its proof are on p. 225",
           "\\oldpage[IV-1]{226} stands before 'Pour abréger' (about 18 printed lines too early)", "marker",
           "irréductible\n$Y'=", "irréduc%\n\\oldpage[IV-1]{226}\ntible\n$Y'=",
           MV + "Part 1 inserts the marker at the printed word break, as homo%|morphisme (0_IV-1 p. 138) and "
           "homomor%|phismes (EGA III p. 126)."))
L.append(F(226, "page break 225/226 (part 2 of 2: old marker removed)",
           "see part 1", "\\oldpage[IV-1]{226} between \\end{proof} (of (1.1.4)) and 'Pour abréger'", "marker",
           "\\oldpage[IV-1]{226}\n\nPour abréger", "Pour abréger",
           MV + "Leaves '\\end{proof}' + blank line + 'Pour abréger' (a new paragraph, as printed)."))

# The end of printed p. 226 ('(où π est le morphisme structural) ... Δ_g est quasi-compact,') stood after the
# p. 227 marker in page_227.tex; the marker move and the bold I of (I, 5.3.5) are already applied to the release
# from findings_227_231.json (FIXLOG), and the moved text matches the print, so nothing is repeated here.

json.dump(L, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)

# check: every old occurs exactly once in its page file (LF-normalised)
bad = 0
for x in L:
    if not x["fix"]:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c = t.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], c, repr(x["fix"]["old"]))
from collections import Counter
cnt = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
print("entries", len(L), "bad", bad)
for p in sorted({x["page"] for x in L}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
