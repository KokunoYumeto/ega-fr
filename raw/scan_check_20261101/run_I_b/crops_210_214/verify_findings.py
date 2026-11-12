"""Read-only check of findings_210_214.json: every fix 'old' occurs exactly once in page_NNN.tex (as stored, CRLF)
and exactly once in the page segment of the r20 diplomatic release file (newlines normalised as apply_fixes.py does).
Also counts findings per page and kind. Writes nothing."""
import collections
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_I_b"
data = json.loads((RUN / "findings_210_214.json").read_text(encoding="utf-8"))
inv = json.loads((E / "page_inventory_r20.json").read_text(encoding="utf-8"))["parts"]["I"]["files"]
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")


def release_segment(page):
    for f in inv:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return f, t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
    return None, None


keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
counts = collections.defaultdict(collections.Counter)
problems = 0
for i, x in enumerate(data):
    missing = keys - set(x)
    if missing:
        print(i, "missing keys", missing); problems += 1
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(i, "misprint without corrected"); problems += 1
    cat = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    counts[x["page"]][cat] += 1
    fix = x.get("fix")
    if not fix:
        continue
    page_tex = (RUN / f"page_{x['page']:03d}.tex").read_bytes().decode("utf-8")
    n_page = page_tex.count(fix["old"])
    f, seg = release_segment(x["page"])
    old_lf = fix["old"].replace("\r\n", "\n")
    n_rel = seg.count(old_lf) if seg is not None else None
    flag = "" if n_page == 1 and n_rel == 1 else "  <-- CHECK"
    if flag:
        problems += 1
    print(f"p{x['page']} #{i}: page={n_page} release={n_rel} ({pathlib.Path(f).name if f else None}){flag}")
for p in sorted(counts):
    print(p, dict(counts[p]))
print("total", len(data), "problems", problems)
