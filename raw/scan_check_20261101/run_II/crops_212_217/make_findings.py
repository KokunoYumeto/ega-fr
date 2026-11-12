"""Build findings_212_217.json for EGA II pp. 212-217 and check every fix's "old" occurs exactly once both in
page_NNN.tex (CRLF normalised) and in the release file's page segment (as apply_fixes.py locates it)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_212_217.json"
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["II"]["files"]
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")

F = []


def add(page, where, scan, tex, kind, old, new, note="", conv=None, conf="high"):
    F.append(dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
                  fix=dict(old=old, new=new), note=note))


# ---------------------------------------------------------------- p. 213 (contents, first page)
add(213, "contents table, header row",
    "only the column head 'Pages' (small capitals, a short rule under it) above the page numbers; no other heads",
    r"\textbf{Unité} & \textbf{Titre} & \textbf{Page originale}\\",
    "word",
    r"\textbf{Unité} & \textbf{Titre} & \textbf{Page originale}\\",
    r" & & \textsc{Pages}\\",
    "The words 'Unité', 'Titre' and 'Page originale' are not printed. The \\hline under the row is layout (the print "
    "has only a short rule under 'Pages'). The print repeats 'Pages' at the top of pp. 214 and 215 (separate findings).")
add(213, "contents, first entry (the chapter)",
    "Chapitre (small capitals) II. — Étude globale élémentaire de quelques classes de morphismes (title bold) ...... 5; "
    "'II.' and the page number 5 are roman, not bold",
    r"\textbf{II} & \textbf{Étude globale élémentaire de quelques classes de morphismes} & \textbf{5}\\",
    "missing",
    r"\textbf{II} & \textbf{Étude globale élémentaire de quelques classes de morphismes} & \textbf{5}\\",
    r"\multicolumn{2}{@{}p{0.78\textwidth}}{\textsc{Chapitre} II. --- \textbf{Étude globale élémentaire de quelques "
    r"classes de morphismes}} & 5\\",
    "The TeX drops 'Chapitre', the full stop after II and the dash, and sets II and the page number bold. The "
    "multicolumn cell keeps 'Chapitre II. — <title>' in one entry as printed (the title wraps under itself).")

LABEL_NOTE = ("Contents labels end with a full stop in the print (every label on pp. 213-215: '§ 1.', '1.1.', ...); "
              "the TeX has none. Checked on the strips.")
labels = {
    213: ["§1", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7",
          "§2", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
          "§3", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8"],
    214: ["§4", "4.1", "4.2", "4.3", "4.4", "4.5", "4.6",
          "§5", "5.1", "5.2", "5.3", "5.4", "5.5", "5.6",
          "§6", "6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7",
          "§7", "7.1", "7.2", "7.3", "7.4",
          "§8", "8.1", "8.2", "8.3", "8.4", "8.5", "8.6"],
    215: ["8.7", "8.8", "8.9", "8.10", "8.11", "8.12", "8.13", "8.14"],
}


def label_findings(page):
    for lab in labels[page]:
        if lab.startswith("§"):
            n = lab[1:]
            add(page, f"contents, label '§ {n}.'", f"§ {n}.", "\\textsection" + n, "punctuation",
                "]{\\textsection" + n + "}", "]{\\textsection" + n + ".}", LABEL_NOTE)
        else:
            add(page, f"contents, label '{lab}.'", f"{lab}.", lab, "punctuation",
                "]{" + lab + "}", "]{" + lab + ".}", LABEL_NOTE)


label_findings(213)

# ---------------------------------------------------------------- p. 214
add(214, "top of the contents table (repeated column head)",
    "'Pages' (small capitals, short rule under it) at the top right, above the page numbers, as on p. 213",
    "the page's longtable starts directly with the § 4 entry",
    "missing",
    "r@{}}\n\\hyperref[section:II.4-fr]",
    "r@{}}\n & & \\textsc{Pages}\\\\\n\\hyperref[section:II.4-fr]",
    "Repeated column head of the contents table (the TeX starts a new longtable on each page). Independent of the "
    "label fix for '§ 4.'.")
label_findings(214)

# ---------------------------------------------------------------- p. 215
add(215, "top of the contents table (repeated column head)",
    "'Pages' (small capitals, short rule under it) above the page numbers, as on pp. 213-214",
    "the page's longtable starts directly with the 8.7 entry",
    "missing",
    "r@{}}\n\\hyperref[subsection:II.8.7-fr]",
    "r@{}}\n & & \\textsc{Pages}\\\\\n\\hyperref[subsection:II.8.7-fr]",
    "Repeated column head of the contents table. Independent of the label fix for '8.7.'.")
label_findings(215)
add(215, "contents entry 'Bibliographie (suite) ... 205'",
    "Bibliographie in small capitals, '(suite)' in italic (italic parentheses)",
    "Bibliographie (suite) (roman)",
    "italics",
    "{Bibliographie (suite)}",
    "{\\textsc{Bibliographie} \\textit{(suite)}}",
    "Checked on a crop. The four back-matter entries are set in small capitals (separate findings).")
add(215, "contents entry 'Index des notations ... 207'",
    "Index des notations in small capitals", "Index des notations (roman)", "font",
    "{Index des notations}", "{\\textsc{Index des notations}}", "Checked on a crop.")
add(215, "contents entry 'Index terminologique ... 209'",
    "Index terminologique in small capitals", "Index terminologique (roman)", "font",
    "{Index terminologique}", "{\\textsc{Index terminologique}}", "Checked on a crop.")
add(215, "contents entry 'Errata et addenda (Liste 1) ... 217'",
    "'Errata et addenda' in small capitals with a lower-case a in 'addenda' (only the E is a full capital); "
    "'(Liste 1)' roman",
    "Errata et Addenda (Liste 1) (roman, capital A)",
    "word",
    "{Errata et Addenda (Liste 1)}",
    "{\\textsc{Errata et addenda} (Liste 1)}",
    "Checked on a 2x crop: the A of 'addenda' has small-capital height, like the following letters.")
add(215, "end of ega2-indexes-and-contents-fr.tex, after the contents (printed p. 216)",
    "printed p. 216 is blank (PDF page 213 of PMIHES_1961__8__5_0.pdf rendered: no ink); p. 215 ends with "
    "'Reçu le 22 juillet 1960.' and a short rule, p. 217 begins with the errata heading",
    "no \\oldpage[II]{216}; page_215.tex and page_217.tex contain no p. 216 text",
    "marker",
    "\\end{flushright}\n\\endgroup",
    "\\end{flushright}\n\\endgroup\n\n\\clearpage\n\\oldpage[II]{216}\n\\thispagestyle{empty}\n\\mbox{}",
    "No printed p. 216 text is misplaced. This edit only adds a blank-page marker in the same form as the blank "
    "p. 212 (\\clearpage, \\oldpage[II]{212}, \\thispagestyle{empty}, \\mbox{}); the \\clearpage at the start of "
    "ega2-errata-addenda-fr.tex ends the blank page. Printed pp. 204 and 206 are blank too and also have no marker: "
    "decide blank-page markers once for the edition.",
    conf="medium")

# ---------------------------------------------------------------- p. 217 (errata, list 1)
HEAD_NOTE = ("The print sets the bold reference and continues the line with no full stop after it; the TeX adds a "
             "full stop inside \\paragraph{...}. Checked on crops; same for every errata heading on this page.")
for ref in ["(0, 2.1.3)", "(0, 2.1.6)", "(0, 3.1.6)", "(0, 4.1.1)", "(0, 4.2.1)", "(0, 5.1.2)", "(0, 5.2.4)",
            "(0, 5.3.4)", "(0, 5.4.1)", "(0, 6.6.2)", "(0, 6.7.1)", "(0, 7.2.9)", "(I, 1.2.1)", "(I, 1.2.7)"]:
    add(217, f"errata heading {ref}", f"{ref} (no full stop)", f"\\paragraph{{{ref}.}}", "punctuation",
        f"\\paragraph{{{ref}.}}", f"\\paragraph{{{ref}}}", HEAD_NOTE)
add(217, "errata heading (I, 1.7.3) et (I, 2.2.4)", "(I, 2.2.4) Les énoncés (no full stop)",
    "\\paragraph{(I, 1.7.3) et (I, 2.2.4).}", "punctuation",
    "(I, 2.2.4).}", "(I, 2.2.4)}", HEAD_NOTE + " Independent of the 'et' finding (non-overlapping).")
add(217, "errata heading (I, 1.7.3) et (I, 2.2.4)",
    "'et' between the two bold references is roman (medium weight)",
    "'et' bold (inside \\paragraph)", "font",
    "(I, 1.7.3) et (I", "(I, 1.7.3) \\textmd{et} (I",
    "Checked on a 1.6x crop.")
add(217, "(0, 2.1.3)", "remplacer inter-section par intersection. (no quotation marks, roman)",
    "remplacer «~inter-section~» par «~intersection~».", "extra",
    "«~inter-section~» par\n«~intersection~»", "inter-section par\nintersection",
    "The TeX adds guillemets; the print has none. Checked on a crop.")
add(217, "(0, 2.1.6)",
    "remplacer Z_i∩∁(⋃_{j≠i} Z_j) par ⋃_{j≠i} Z_j. — set in the text line (limits j≠i under the unions), "
    "with the complement sign ∁",
    "display \\[ Z_i\\cap C\\left(\\bigcup_{j\\ne i}Z_j\\right) \\quad\\hbox{par}\\quad \\bigcup_{j\\ne i}Z_j. \\] "
    "with a letter C",
    "symbol",
    "remplacer\n\\[\n  Z_i\\cap C\\left(\\bigcup_{j\\ne i}Z_j\\right)\n  \\quad\\hbox{par}\\quad\n"
    "  \\bigcup_{j\\ne i}Z_j.\n\\]",
    "remplacer $Z_i\\cap\\complement(\\bigcup\\limits_{j\\ne i}Z_j)$ par\n$\\bigcup\\limits_{j\\ne i}Z_j$.",
    "Checked on a 2x crop: the sign after ∩ is the complement sign (the edition writes \\complement, e.g. "
    "ega0-1-fr.tex at (0, 2.1.6) itself: Z_i\\cap\\complement\\Bigl(...\\Bigr)), not a letter C. The same edit sets "
    "the formula inline as printed (display vs inline is layout only).")
add(217, "(0, 4.2.1)", "remplacer faisceaux par faisceau. (no quotation marks)",
    "remplacer «~faisceaux~» par «~faisceau~».", "extra",
    "«~faisceaux~» par «~faisceau~»", "faisceaux par faisceau",
    "The TeX adds guillemets; the print has none. Checked on a crop.")
add(217, "(0, 5.3.4), added text",
    "Si 𝒜→ℬ→𝒞→𝒟→ℰ est une suite exacte ... (the sequence is in the text line)",
    "the sequence is displayed with \\[ ... \\]", "other",
    "Si\n\\[\n  \\sh{A}\\to\\sh{B}\\to\\sh{C}\\to\\sh{D}\\to\\sh{E}\n\\]\nest une suite exacte",
    "Si $\\sh{A}\\to\\sh{B}\\to\\sh{C}\\to\\sh{D}\\to\\sh{E}$\nest une suite exacte",
    "Layout only (display vs inline); the formula itself matches.")
for old, new, w in [
    ("Supposons $\\sh{O}_X$ cohérent,", "Supposons $\\sh{O}_X$ \\emph{cohérent},", "'Supposons 𝒪_X cohérent'"),
    ("-Module\ncohérent. Alors", "-Module\n\\emph{cohérent}. Alors", "'un 𝒪_X-Module cohérent.'"),
    ("-module libre de rang $n$,", "-module \\emph{libre de rang $n$},", "'𝒪_x-module libre de rang n'"),
    ("soit localement libre de rang $n$;", "soit \\emph{localement libre de rang $n$};",
     "'soit localement libre de rang n'"),
]:
    add(217, f"(0, 5.4.1), added text: {w}", "italic in the print", "roman", "italics", old, new,
        "Checked on the strip: 'cohérent' (twice), 'libre de rang n' and 'localement libre de rang n' are italic.")
add(217, "(0, 5.4.1), added text, last line", "et la proposition résulte de (5.2.7).",
    "de (0, 5.2.7).", "extra", "de (0, 5.2.7).", "de (5.2.7).",
    "The print has no '0,' in this reference. Checked on a 1.5x crop.")
add(217, "(0, 6.6.2), replacement text", "En effet, cela résulte de (6.4.1, d)).",
    "de (0, 6.4.1, d)).", "extra", "de (0, 6.4.1", "de (6.4.1",
    "The print has no '0,' in this reference. Independent of the italic-d) finding (non-overlapping).")
add(217, "(0, 6.6.2), replacement text", "'d)' italic: (6.4.1, d))",
    "d) roman", "italics", ", d)).", ", \\emph{d)}).",
    "Lettered reference italic in the print (edition form \\emph{b)} as in ega2-1-fr.tex). Checked on a 1.6x crop.")
add(217, "(I, 1.2.1)", "remplacer (deux fois) K par k. — K bold italic",
    "$K$ (plain italic)", "font", "(deux fois) $K$", "(deux fois) $\\boldsymbol{K}$",
    "Checked on a 2x crop: the K is bold italic like the k after it (the residue-field typeface).")
add(217, "(I, 1.2.1)", "... K par k. — k bold italic",
    "$k$ (plain italic)", "convention", "par $k$.", "par $\\boldsymbol{k}$.",
    "Bold italic k of the residue field (convention 1); checked on a 2x crop.", conv=1)
add(217, "heading 1.8", "1.8. Morphismes d'espaces annelés en anneaux locaux dans les schémas affines.",
    "no final full stop", "punctuation",
    "dans les schémas affines}", "dans les schémas affines.}",
    "Checked on a crop; same kind of fix as the headings 4.4 (p. 78) and 8.2 (p. 157).")

# ---------------------------------------------------------------- checks
def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


def release_segment(n):
    for f in inv:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (p, s) in enumerate(cuts):
            if p == n:
                return t[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(t))]
    return None


bad = 0
for x in F:
    o = x["fix"]["old"]
    c1 = page_text(x["page"]).count(o)
    seg = release_segment(x["page"])
    c2 = seg.count(o) if seg is not None else -1
    if c1 != 1 or c2 != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], repr(o), c1, c2)
# overlapping olds on the same page (one edit destroying another's old)
for p in sorted({x["page"] for x in F}):
    t = release_segment(p)
    xs = [x for x in F if x["page"] == p]
    for a in xs:
        t2 = t.replace(a["fix"]["old"], a["fix"]["new"])
        for b in xs:
            if b is not a and t2.count(b["fix"]["old"]) != 1:
                bad += 1
                print("CONFLICT", p, repr(a["fix"]["old"]), "breaks", repr(b["fix"]["old"]))
# all fixes of a page applied in order must leave a single \oldpage marker for that page and apply cleanly
for p in sorted({x["page"] for x in F}):
    t = release_segment(p)
    for x in [x for x in F if x["page"] == p]:
        assert t.count(x["fix"]["old"]) == 1, (p, x["fix"]["old"])
        t = t.replace(x["fix"]["old"], x["fix"]["new"])
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter((x["page"], "misprint" if x["kind"] == "misprint_in_print" else
               ("convention" if x["kind"] == "convention" else "normal")) for x in F)
print("written", OUT, len(F), "findings; problems:", bad)
for p in [212, 213, 214, 215, 217]:
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
