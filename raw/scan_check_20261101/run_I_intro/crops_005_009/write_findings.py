"""Write findings_005_009.json for EGA I, Introduction, pp. 5-9, and check every fix string.

Each "old" must occur exactly once in page_NNN.tex; the one marker move spans the page boundary and is checked
against intro-fr.tex of the r20 release instead."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_intro")
INTRO = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                     r"\diplomatic\packages\BASE\native\ega1\intro-fr.tex")
OUT = RUN / "findings_005_009.json"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, convention=None):
    F.append(dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
                  confidence=conf, fix=fix, note=note))


# ---- page 5 -------------------------------------------------------------------------------------------------
add(5, "top of the page: heading and dedication",
    "printed p. 5 begins with the heading 'INTRODUCTION' and the italic dedication "
    "'A Oscar Zariski et André Weil.', then 'Ce mémoire, et les nombreux autres ...'",
    "\\section*{Introduction} and the dedication stand before \\oldpage[I]{5} (intro-fr.tex ll. 1-7), "
    "so both fall outside page 5",
    "marker", "high",
    {"old": "\\section*{Introduction}\n\n\\begin{center}\n\\emph{A Oscar Zariski et André Weil.}\n"
            "\\end{center}\n\n\\oldpage[I]{5}",
     "new": "\\oldpage[I]{5}\n\\section*{Introduction}\n\n\\begin{center}\n"
            "\\emph{A Oscar Zariski et André Weil.}\n\\end{center}"},
    "The marker belongs before \\section*{Introduction}, as at pp. 101 and 130. The 'old' string spans the page "
    "boundary: it is an exact, unique substring of intro-fr.tex ll. 1-7 (LF line endings; identical in "
    "source/ega1 and the r20 release), not of page_005.tex, which starts at the marker. Apply it as a file-level "
    "edit (apply_manual.py, region 'file'). \\oldpage is a \\marginpar, which is allowed in vertical mode "
    "before \\section*.")

for lab, what in [("a", "a) L'Algèbre commutative"), ("b", "b) L'Algèbre homologique"),
                  ("c", "c) La Théorie des faisceaux"), ("d", "d) Enfin, il sera utile")]:
    add(5, f"list of prerequisites, label of item {lab})",
        f"'{lab})' set in italic, letter and parenthesis ({what} ...)",
        f"\\item[{lab})]: upright label",
        "italics", "high",
        {"old": f"\\item[{lab})]", "new": f"\\item[\\textit{{{lab})}}]"},
        "The four labels a) to d) are italic in the print (the parenthesis is slanted too). Labels set upright "
        "were corrected the same way on pp. 84 and 122." if lab == "a" else "As for a).")

# ---- page 6 -------------------------------------------------------------------------------------------------
plan = [("II", "Étude globale élémentaire de quelques classes de morphismes."),
        ("III", "Cohomologie des faisceaux algébriques cohérents. Applications."),
        ("IV", "Étude locale des morphismes."),
        ("V", "Procédés élémentaires de construction de schémas."),
        ("VI", "Technique de descente. Méthode générale de construction des schémas."),
        ("VII", "Schémas de groupes, espaces fibrés principaux."),
        ("VIII", "Étude différentielle des espaces fibrés."),
        ("IX", "Le groupe fondamental."),
        ("X", "Résidus et dualité."),
        ("XI", "Théories d'intersection, classes de Chern, théorème de Riemann-Roch."),
        ("XII", "Schémas abéliens et schémas de Picard."),
        ("XIII", "Cohomologie de Weil.")]
for i, (num, title) in enumerate(plan):
    add(6, f"plan of the treatise, chapter {num}",
        f"'— {num}. — {title}' with the numeral {num} in regular roman (not bold)",
        f"--- \\textbf{{{num}}}. & --- {title}",
        "font", "high",
        {"old": f"\\textbf{{{num}}}.", "new": f"{num}."},
        ("The chapter numerals of the plan are printed in the text weight. Measured at 300 dpi, each capital I in "
         "them has a 6 px stem and about 240 dark pixels, the same as the sentence-initial 'Il' on pp. 7 and 9; "
         "the bold reference numeral of (II, 2.4.3) on p. 101 measures 8-9 px stems, and its two I's merge "
         "into one blob. The chapter numerals in the running text of pp. 7-9 (chap. II, III, IV, V, VI, IX; "
         "'III, 4.9.3') measure the same regular weight, and the TeX sets those plain.") if i == 0
        else "As for II.")

# ---- page 8 -------------------------------------------------------------------------------------------------
for n in "1234":
    add(8, f"label {n}° of the four steps",
        f"'{n}' followed by a superior letter o (oval, with thick and thin strokes): the ordinal {n}º",
        f"\\item[${n}^\\circ$]: math ring (degree-like circle)",
        "symbol", "medium",
        {"old": f"${n}^\\circ$", "new": f"{n}\\textsuperscript{{o}}"},
        ("The print has the French ordinal with a superior letter o, not a degree ring (a 5x crop of 1º shows an "
         "upright oval with stroke contrast). ega1-7-fr.tex l. 443 and ega1-9-fr.tex l. 659 already write "
         "\\item[1\\textsuperscript{o}]; ega1-4-fr.tex l. 55 has $1^\\circ$ like this page. The old-style figure "
         "of the print is ignored.") if n == "1" else "As for 1°.")

# ---- page 9 -------------------------------------------------------------------------------------------------
add(9, "last paragraph, last sentence",
    "A l'intérieur du même chapitre, on supprimera la mention du chapitre. ('du même chapitre' italic)",
    "A l'intérieur du même chapitre, on supprimera la mention du chapitre. (all roman)",
    "italics", "high",
    {"old": "du même chapitre, on", "new": "\\emph{du même chapitre}, on"},
    "Only 'du même chapitre' is italic; 'A l'intérieur' and the rest of the sentence are roman.")

# ---- checks -------------------------------------------------------------------------------------------------
pages = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8") for n in range(5, 10)}
intro = INTRO.read_text(encoding="utf-8")
ok = True
for x in F:
    old = x["fix"]["old"]
    if x["kind"] == "marker":
        c_page, c_file = pages[x["page"]].count(old), intro.count(old)
        good = c_file == 1
        print(f"p.{x['page']} marker: in page {c_page}, in intro-fr.tex {c_file}", "OK" if good else "BAD")
    else:
        c = pages[x["page"]].count(old)
        good = c == 1
        if not good:
            print(f"p.{x['page']} {x['kind']}: {old!r} occurs {c} times  BAD")
    ok &= good
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT, "findings:", len(F), "| all fix strings checked:", ok)
by = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    by.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
for n in range(5, 10):
    print(n, by.get(n, {"normal": 0, "convention": 0, "misprint": 0}))
