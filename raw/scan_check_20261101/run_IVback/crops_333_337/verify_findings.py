import json
import sys

base = r"user/Documents/ega_scan_check_20261101/run_IVback/"
src = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/"
srcfile = {333: "ega4-backmatter-bibliography-fr.tex",
           334: "ega4-backmatter-notation-fr.tex",
           335: "ega4-backmatter-notation-fr.tex",
           336: "ega4-backmatter-terminology-fr.tex",
           337: "ega4-backmatter-terminology-fr.tex"}

F = json.load(open(base + "findings_333_337.json", encoding="utf-8"))
pages = {p: open(base + f"page_{p}.tex", encoding="utf-8").read() for p in srcfile}
orig_pages = dict(pages)
sources = {f: open(src + f, encoding="utf-8").read() for f in set(srcfile.values())}
orig_sources = dict(sources)

# the page text (minus the first comment line and the continuation part) must be a substring of the source file
for p, t in orig_pages.items():
    body = t.split("\n", 1)[1]
    body = body.split("% (continued in")[0].rstrip("\n")
    ok = body in orig_sources[srcfile[p]]
    sys.stdout.write(f"page {p}: segment found verbatim in current source: {ok}\n")

bad = 0
for i, x in enumerate(F):
    fx = x["fix"]
    if fx is None:
        continue
    p = x["page"]
    old, new = fx["old"], fx["new"]
    n_page_now = pages[p].count(old)
    n_src_now = sources[srcfile[p]].count(old)
    n_page_orig = orig_pages[p].count(old)
    flag = "" if (n_page_now == 1 and n_src_now == 1) else "   <-- PROBLEM"
    if flag:
        bad += 1
    sys.stdout.write(f"{i:2d} p{p} {x['kind']:18s} page_now={n_page_now} src_now={n_src_now} page_orig={n_page_orig}{flag}\n")
    pages[p] = pages[p].replace(old, new, 1)
    sources[srcfile[p]] = sources[srcfile[p]].replace(old, new, 1)
    # misprint fixes must not carry other changes: report length of change
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        sys.stdout.write("   missing corrected\n")

sys.stdout.write(f"problems: {bad}\n")
# write the fully edited pages for inspection
for p, t in pages.items():
    open(base + f"crops_333_337/after_page_{p}.tex", "w", encoding="utf-8", newline="\n").write(t)
