"""Write findings_338_343.json (pages 338, 339, 341, 342, 343 of EGA IV-4 end matter) and check every 'old'."""
import json
import pathlib

RUN = pathlib.Path(r"user/Documents/ega_scan_check_20261101/run_IVback")
SRC = pathlib.Path(r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4")
OUT = RUN / "findings_338_343.json"

TERM = "ega4-backmatter-terminology-fr.tex"
CONT = "ega4-backmatter-contents-fr.tex"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None, convention=None):
    x = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        x["corrected"] = corrected
    x["note"] = note
    F.append(x)


# ---------------------------------------------------------------- p. 339 (Index terminologique, end)
add(339, "Index terminologique, entry 'Suite de sections transversalement régulière relativement à S : 19.1.2.'",
    "19.1.2 (enlarged crop crops_338_343/p339_suite.png)",
    "{\\hyperlink{ega4.c04.cor.19-1-2}{19.1.2}} (keeps the printed reading; links to Corollaire (19.1.2))",
    "misprint_in_print", "high",
    None,
    "The notion is defined in Définition (19.2.1) ('une suite (f_i) de sections de F ... transversalement "
    "F-régulière relativement à S'); (19.1.2) is the corollary on a regular local ring A/J (print p. 185, checked "
    "on run_IV4 page_185). Transposed digits; the neighbouring entries 'Idéal transversalement régulier ... : "
    "19.2.1' cite the same definition. The diplomatic link could point to def.19-2-1, as the EGA II index's "
    "transposed 3.8.1 does; left as printed here.",
    corrected="{\\hyperlink{ega4.c04.def.19-2-1}{19.2.1}}")

add(339, "Index terminologique, below the last entry 'n-ème voisinage infinitésimal : 16.1.2.' (end of the index)",
    "a short centred rule under the last entry",
    "nothing between the last \\EGAIVterm and \\endgroup",
    "missing", "high",
    {"old": "{16.1.2}}}\n\n", "new": "{16.1.2}}}\n\n\\begin{center}\\rule{25mm}{0.4pt}\\end{center}\n\n"},
    "GLOBAL_ISSUES item 61 (printed closing rules): apply only if the edition reproduces them; same form as the rules "
    "applied for EGA III p. 223 and IV-2 p. 231 (the IV-3 checker noted the same rule under the IV-3 Index "
    "terminologique, p. 251, without a finding). Independent of the blank-page edit (next finding): this 'old' ends "
    "before \\endgroup.")

add(339, "printed p. 340 (blank, between the Index terminologique and the Table des matières); the edit is at the end "
         "of ega4-backmatter-terminology-fr.tex, in p. 339's segment",
    "p. 340 is blank (scan pdf page 339 of PMIHES_1967__32__5_0.pdf rendered: no ink, no page number)",
    "no \\oldpage[IV]{340}: the terminology file ends with \\endgroup, the contents file begins with \\clearpage and "
    "\\oldpage[IV]{341}",
    "marker", "high",
    {"old": "\\endgroup\n",
     "new": "\\endgroup\n\n\\clearpage\n% La page imprimée 340 est blanche.\n\\oldpage[IV]{340}\n"
            "\\thispagestyle{empty}\n\\null\n"},
    "Markers for every printed page, blank ones included (GLOBAL_ISSUES item 32); same form as the blank p. 252 of "
    "IV-3 (ega4-15-terminal-fr.tex); the \\clearpage at the start of ega4-backmatter-contents-fr.tex ends the blank "
    "page. Filed under p. 339 because apply_fixes.locate(340) finds neither a 340 marker nor a gap around 340 inside "
    "one file (the 339 and 341 markers are in different files). No printed text moves.")

# ---------------------------------------------------------------- p. 341 (Table des matières, 1)
add(341, "Table des matières, top right above the page-number column (before the Chapitre IV line)",
    "column head 'Pages' in small capitals, a short rule under it",
    "absent",
    "missing", "high",
    {"old": "\\endgroup}\n", "new": "\\endgroup}\n\\hfill\\textsc{Pages}\\par\n"},
    "GLOBAL_ISSUES item 45; same form as the IV-2 and IV-3 contents (\\hfill\\textsc{Pages}\\par inside the \\small "
    "group). Inserted right after the \\newcommand of \\EGAIVcontentsline; it does not touch the macro body or the "
    "Chapitre IV line. The rule under it is layout.")

add(341, "\\newcommand{\\EGAIVcontentsline} (the label of every contents line, pp. 341-343)",
    "labels '§ 16.', '16.1.', ..., '21.15.' in roman of normal weight",
    "\\noindent\\textbf{#1}: every label bold",
    "font", "high",
    {"old": "\\noindent\\textbf{#1}", "new": "\\noindent #1"},
    "One edit for all labels of pp. 341-343 (the macro is defined in this page's segment), as for the IV-2 and IV-3 "
    "contents macros. The new string keeps a space after \\noindent. Does not overlap the full-stop edit (next "
    "finding), whose 'old' starts at \\quad.")

add(341, "\\newcommand{\\EGAIVcontentsline}: full stop after each label (pp. 341-343)",
    "every label ends with a full stop: '§ 16.', '16.1.', ..., '§ 20.', '20.0.', ..., '§ 21.', '21.15.' (all 77 "
    "labels of pp. 341-343 checked on the strips)",
    "labels without the stop ('\\S16', link texts '16.1' ...)",
    "punctuation", "high",
    {"old": "\\quad #2\\nobreak",
     "new": "\\if\\relax\\detokenize{#1}\\relax\\else.\\fi\\quad #2\\nobreak"},
    "One edit instead of 77 label edits (the EGA II contents had one finding per label); the stop stands after the "
    "hyperlink, and the lines with an empty label (Bibliographie, Index des notations, Index terminologique, and the "
    "Chapitre IV line after its fix below) get none. A test compile of the macro with both edits gives '§16.', "
    "'16.1.', '21.14.' and no stop on the empty labels. Not recorded: the label of 16.4 prints '16 4.' with the "
    "space of the missing point kept and no trace of ink (crops_338_343/p341_164.png, p341_164_thresh.png), i.e. a "
    "point that did not print (physical defect, not a misprint); the TeX's 16.4 stays.")

add(341, "Table des matières, first line 'Chapitre IV. — Étude locale des schémas et des morphismes de schémas (fin) ... 5'",
    "a contents line with dotted leaders and the page number 5: 'Chapitre' in small capitals, 'IV.' roman of normal "
    "weight, a dash, the title in bold, '(fin)' in light italic",
    "\\begin{center}\\textbf{CHAPITRE IV. --- Étude locale des schémas et des morphismes de schémas (fin)}\\end{center}: "
    "a centred heading in bold capitals with a bold upright '(fin)', no leaders, no page number",
    "missing", "high",
    {"old": "\\begin{center}\\textbf{CHAPITRE IV. --- Étude locale des schémas et des morphismes de schémas (fin)}\\end{center}",
     "new": "\\EGAIVcontentsline{}{\\textsc{Chapitre IV.} --- \\textbf{Étude locale des schémas et des morphismes de "
            "schémas} \\textit{(fin)}}{5}"},
    "One edit for the three differences of this line (the missing page number 5 with its leaders; small capitals and "
    "normal weight for 'Chapitre IV.'; italic '(fin)'). Same form as the IV-1 contents line (ega4-1-fr.tex: empty "
    "label, '\\textsc{Chapitre IV.} --- \\textbf{...}' in the title, \\textit{(suite)}). The empty label gets no stop "
    "from the full-stop edit.")

add(341, "Table des matières, line 17.4 'Caractérisations des morphismes non ramifiés ... 65', page number",
    "65",
    "65 (keeps the printed reading)",
    "misprint_in_print", "high",
    None,
    "Section 17.4 begins at the top of printed p. 63 (run_IV4 page_063_s1: running head with 63, then the heading "
    "'17.4. Caractérisations des morphismes non ramifiés.'), where ega4-17-fr.tex has it after \\oldpage[IV-4]{63}. "
    "All other contents page numbers of pp. 341-343 agree with the page markers of the section headings except "
    "§ 20, 20.0 and 20.1 (p. 342).",
    corrected="63")

# ---------------------------------------------------------------- p. 342 (Table des matières, 2)
add(342, "top right above the page-number column (before the 17.13 line)",
    "column head 'Pages' in small capitals, a short rule under it",
    "absent",
    "missing", "high",
    {"old": "\\EGAIVcontentsline{{\\texorpdfstring{\\protect\\hyperlink{ega4.c04.subsec.17-13}",
     "new": "\\hfill\\textsc{Pages}\n\n\\EGAIVcontentsline{{\\texorpdfstring{\\protect\\hyperlink{ega4.c04.subsec.17-13}"},
    "Repeated on each contents page (GLOBAL_ISSUES item 45); same form as the IV-3 contents, pp. 254-255. The rule "
    "under it is layout.")

add(342, "Table des matières, line '§ 20. Fonctions méromorphes et pseudo-morphismes ... 223', page number",
    "223",
    "223 (keeps the printed reading)",
    "misprint_in_print", "high",
    None,
    "§ 20 and n° 20.0 begin on printed p. 225, below Remarque (19.9.9) (run_IV4 page_225_s3-s4; pp. 223-224 carry "
    "the end of 19.9); \\oldpage[IV-4]{225} is the last marker of ega4-18-fr.tex and ega4-20-fr.tex starts on that "
    "page. The printed numbers of § 20, 20.0 and 20.1 are all 2 too small; 20.2 (231) and the later ones agree.",
    corrected="225")

add(342, "Table des matières, line '20.0. Introduction ... 223', page number",
    "223",
    "223 (keeps the printed reading)",
    "misprint_in_print", "high",
    None,
    "The heading '20.0. Introduction.' is on printed p. 225 (run_IV4 page_225_s3), as for § 20 above.",
    corrected="225")

add(342, "Table des matières, line '20.1. Fonctions méromorphes ... 224', page number",
    "224",
    "224 (keeps the printed reading)",
    "misprint_in_print", "high",
    None,
    "The heading '20.1. Fonctions méromorphes.' is on printed p. 226 (run_IV4 page_226_s3, running head 226), "
    "after \\oldpage[IV-4]{226} in ega4-20-fr.tex.",
    corrected="226")

# ---------------------------------------------------------------- p. 343 (Table des matières, 3)
add(343, "top right above the page-number column (before the 20.3 line)",
    "column head 'Pages' in small capitals, a short rule under it",
    "absent",
    "missing", "high",
    {"old": "\\EGAIVcontentsline{{\\texorpdfstring{\\protect\\hyperlink{ega4.c04.subsec.20-3}",
     "new": "\\hfill\\textsc{Pages}\n\n\\EGAIVcontentsline{{\\texorpdfstring{\\protect\\hyperlink{ega4.c04.subsec.20-3}"},
    "Repeated on each contents page (GLOBAL_ISSUES item 45), as on p. 342.")

add(343, "Table des matières, line 21.14 'Le théorème de Ramanujam-Samuel ... 323'",
    "Ramanujam-Samuel with a hyphen (same length as the hyphens of 'pseudo-morphismes' on this page)",
    "Ramanujam--Samuel (en dash)",
    "punctuation", "high",
    {"old": "Ramanujam--Samuel", "new": "Ramanujam-Samuel"},
    "As for Cohen--Macaulay in IV-2 (GLOBAL_ISSUES item 74). The body (21.14 heading, ega4-21c-fr.tex, and "
    "ega4-20-fr.tex line 17) already has the hyphen.")

add(343, "Table des matières, back-matter line 'Bibliographie ... 333'",
    "'Bibliographie' in small capitals",
    "BIBLIOGRAPHIE (full capitals)",
    "font", "high",
    {"old": "{}{BIBLIOGRAPHIE}", "new": "{}{\\textsc{Bibliographie}}"},
    "As in the EGA II, IV-1, IV-2 and IV-3 contents.")

add(343, "Table des matières, back-matter line 'Index des notations ... 334'",
    "'Index des notations' in small capitals",
    "INDEX DES NOTATIONS (full capitals)",
    "font", "high",
    {"old": "{}{INDEX DES NOTATIONS}", "new": "{}{\\textsc{Index des notations}}"},
    "As in the EGA II, IV-1, IV-2 and IV-3 contents.")

add(343, "Table des matières, back-matter line 'Index terminologique ... 336'",
    "'Index terminologique' in small capitals",
    "INDEX TERMINOLOGIQUE (full capitals)",
    "font", "high",
    {"old": "{}{INDEX TERMINOLOGIQUE}", "new": "{}{\\textsc{Index terminologique}}"},
    "As in the EGA II, IV-1, IV-2 and IV-3 contents. Does not overlap the closing-rule edit (next finding), whose "
    "'old' starts at '{336}'.")

add(343, "Table des matières, below the last line 'Index terminologique ... 336' (end of the contents)",
    "a short centred rule",
    "nothing between the last \\EGAIVcontentsline and \\endgroup",
    "missing", "high",
    {"old": "{336}\n", "new": "{336}\n\n\\begin{center}\\rule{25mm}{0.4pt}\\end{center}\n"},
    "GLOBAL_ISSUES item 61: apply only if the edition reproduces the printed closing rules (as applied for EGA III "
    "p. 223 and IV-2 p. 231). Independent of the blank-page edit (next finding).")

add(343, "printed p. 344 (blank, between the Table des matières and the Errata et addenda, liste 3); the edit is at "
         "the end of ega4-backmatter-contents-fr.tex, in p. 343's segment",
    "p. 344 is blank (scan pdf page 343 of PMIHES_1967__32__5_0.pdf rendered: no ink, no page number)",
    "no \\oldpage[IV]{344}: the contents file ends with \\endgroup, the errata file begins with \\clearpage and "
    "\\oldpage[IV]{345}",
    "marker", "high",
    {"old": "\\endgroup\n",
     "new": "\\endgroup\n\n\\clearpage\n% La page imprimée 344 est blanche.\n\\oldpage[IV]{344}\n"
            "\\thispagestyle{empty}\n\\null\n"},
    "GLOBAL_ISSUES item 32, same form as the p. 340 marker (p. 339 finding); the \\clearpage at the start of "
    "ega4-errata-addenda-list3-fr.tex ends the blank page. Filed under p. 343: locate(344) finds no gap around 344 "
    "inside one file. '\\endgroup\\n' occurs once in the file (the macro's own \\endgroup is followed by '}').")

# ---------------------------------------------------------------- checks
src_text = {339: (SRC / TERM).read_text(encoding="utf-8"), 341: (SRC / CONT).read_text(encoding="utf-8")}
src_text[338] = src_text[339]
src_text[342] = src_text[343] = src_text[341]
ok = True
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    page_t = (RUN / f"page_{x['page']}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n_page = page_t.count(fx["old"])
    n_src = src_text[x["page"]].count(fx["old"])
    flag = "" if (n_page == 1 and n_src == 1) else "   <-- PROBLEM"
    if flag:
        ok = False
    print(x["page"], repr(fx["old"])[:70], "page:", n_page, "source:", n_src, flag)
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", len(F), "findings; all olds unique:", ok)
