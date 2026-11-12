"""Write findings_257_259.json and check every fix. Usage: write_findings.py RUN_DIR"""
import itertools
import json
import sys

run = sys.argv[1]
OUT = f"{run}/findings_257_259.json"


def F(page, where, scan, tex, kind, fix, note, confidence="high", convention=None):
    return {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
            "confidence": confidence, "fix": fix, "note": note}


PAGES_NOTE = ("Contents column head, added the same way as in the EGA II and EGA III part 1 contents "
              "(GLOBAL_ISSUES item 45). The short rule under it is layout.")

findings = [
    # ---------------- p. 257 ----------------
    F(257, "top right, above the page-number column (before the Chapitre 0 line)",
      "column head 'Pages' (small capitals, a short rule under it) above the page numbers",
      r"(nothing): the entries follow \section*{TABLE DES MATIÈRES} directly",
      "missing",
      {"old": "\\section*{TABLE DES MATIÈRES}\n",
       "new": "\\section*{TABLE DES MATIÈRES}\n\n\\hfill\\textsc{Pages}\n"},
      PAGES_NOTE + r" Anchored on the \section* line so that it does not touch the Chapitre 0 line; it lands"
      r" before the \newcommand line, which typesets nothing."),
    F(257, "Chapitre 0 line",
      "CHAPITRE o. — Préliminaires (suite): 'Chapitre' in small capitals with a full capital C "
      "(enlarged crop), set like 'CHAPITRE IV.' on p. 259",
      r"\ivonecontentsline{Chapitre 0.}{...}: 'Chapitre 0.' roman, in the label box",
      "font",
      {"old": "\\ivonecontentsline{Chapitre 0.}{",
       "new": "\\ivonecontentsline{}{\\textsc{Chapitre 0.} "},
      r"Same form as the TeX's own Chapitre IV line on p. 259 (empty label box; '\textsc{Chapitre IV.} ---"
      r" \textbf{...}' in the title box). The new string ends with a space. Does not overlap the dash fix"
      r" (next finding); in either order the two give '\ivonecontentsline{}{\textsc{Chapitre 0.} ---"
      r" \textbf{Préliminaires} ...'."),
    F(257, "Chapitre 0 line",
      "CHAPITRE o. — Préliminaires: a long dash between 'o.' and 'Préliminaires' (enlarged crop)",
      r"no dash: 'Chapitre 0.' in the label box, then \textbf{Préliminaires}",
      "punctuation",
      {"old": "\\textbf{Préliminaires}",
       "new": "--- \\textbf{Préliminaires}"},
      "The TeX's Chapitre IV line (p. 259) has the dash."),
    F(257, "Chapitre 0 line, '(suite)'",
      "'(suite)' italic, its parentheses italic too (slanted; enlarged crop)",
      r"(\emph{suite}): upright parentheses",
      "italics",
      {"old": "(\\emph{suite})}{5}",
       "new": "\\textit{(suite)}}{5}"},
      r"As fixed in the EGA III part 1 contents and in the chapter heading on p. 5 (\textit{(suite)})."),
    # ---------------- p. 258 ----------------
    F(258, "top right, above the page-number column (before 19.3.)",
      "column head 'Pages' (small capitals, short rule under it), as on p. 257",
      "(nothing): the page starts with the 19.3 entry",
      "missing",
      {"old": "\\ivonecontentsline{19.3.}",
       "new": "\\hfill\\textsc{Pages}\n\n\\ivonecontentsline{19.3.}"},
      PAGES_NOTE + " Repeated on each contents page."),
    # ---------------- p. 259 ----------------
    F(259, "top right, above the page-number column (before 22.5.)",
      "column head 'Pages' (small capitals, short rule under it), as on pp. 257-258",
      "(nothing): the page starts with the 22.5 entry",
      "missing",
      {"old": "\\ivonecontentsline{22.5.}",
       "new": "\\hfill\\textsc{Pages}\n\n\\ivonecontentsline{22.5.}"},
      PAGES_NOTE + " Repeated on each contents page."),
    F(259, "back-matter entry 'Bibliographie (suite)'",
      "BIBLIOGRAPHIE in small capitals with a full capital B (enlarged crop)",
      "Bibliographie, roman",
      "font",
      {"old": "{}{Bibliographie",
       "new": "{}{\\textsc{Bibliographie}"},
      "As in the EGA II and EGA III contents. Does not overlap the '(suite)' fix (next finding)."),
    F(259, "back-matter entry 'Bibliographie (suite)', '(suite)'",
      "'(suite)' italic, its parentheses italic too (slanted; enlarged crop)",
      r"(\emph{suite}): upright parentheses",
      "italics",
      {"old": "(\\emph{suite})}{251}",
       "new": "\\textit{(suite)}}{251}"},
      r"Same as the EGA II and EGA III contents entry (\textsc{Bibliographie} \textit{(suite)})."),
    F(259, "back-matter entry 'Index des notations'",
      "INDEX DES NOTATIONS in small capitals with a full capital I (enlarged crop)",
      "Index des notations, roman",
      "font",
      {"old": "{}{Index des notations}",
       "new": "{}{\\textsc{Index des notations}}"},
      "As in the EGA II contents."),
    F(259, "back-matter entry 'Index terminologique'",
      "INDEX TERMINOLOGIQUE in small capitals with a full capital I (enlarged crop)",
      "Index terminologique, roman",
      "font",
      {"old": "{}{Index terminologique}",
       "new": "{}{\\textsc{Index terminologique}}"},
      "As in the EGA II contents."),
]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# ---- checks ----
data = json.load(open(OUT, encoding="utf-8"))
raw = {p: open(f"{run}/page_{p:03d}.tex", encoding="utf-8", newline="").read() for p in (257, 258, 259)}
ok = True
for p, t in raw.items():
    print(f"page {p}: CRLF={t.count(chr(13) + chr(10))}, bare CR={t.count(chr(13)) - t.count(chr(13) + chr(10))}")
texts = {p: t.replace("\r\n", "\n") for p, t in raw.items()}

# the release source (LF): segment of each page between its marker and the next one
src = open(sys.argv[2], encoding="utf-8", newline="").read()
print("source CR count:", src.count("\r"))
starts = {p: src.index("\\oldpage[IV-1]{%d}" % p) for p in (257, 258, 259)}
segs = {257: src[starts[257]:starts[258]], 258: src[starts[258]:starts[259]], 259: src[starts[259]:]}
for p in (257, 258, 259):
    page_body = texts[p].split("\n", 1)[1]  # drop the '% from ...' line
    print(f"page {p}: page file equals source segment: {page_body.strip() == segs[p].strip()}")
for i, x in enumerate(data):
    n_seg = segs[x["page"]].count(x["fix"]["old"])
    n_all = src.count(x["fix"]["old"])
    if n_seg != 1:
        ok = False
    print(f"#{i} p{x['page']} in source segment: {n_seg}, in whole ega4-1-fr.tex: {n_all}")
for i, x in enumerate(data):
    fx = x["fix"]
    n = texts[x["page"]].count(fx["old"])
    if n != 1:
        ok = False
    print(f"#{i} p{x['page']} {x['kind']:<11} count={n} old={fx['old']!r}")

# simulate all fixes of a page, in every order, and require one identical result
for p, t in texts.items():
    fixes = [x["fix"] for x in data if x["page"] == p]
    results = set()
    for perm in itertools.permutations(fixes):
        s = t
        for fx in perm:
            if s.count(fx["old"]) != 1:
                results.add("FAIL " + fx["old"])
                break
            s = s.replace(fx["old"], fx["new"])
        else:
            results.add(s)
    if len(results) != 1 or any(r.startswith("FAIL") for r in results):
        ok = False
        print("ORDER PROBLEM on page", p, [r[:60] for r in results])
    else:
        print(f"--- page {p}: all {len(fixes)} fixes apply in every order; result:")
        print(results.pop())
print("ALL OK" if ok else "PROBLEMS")
