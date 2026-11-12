"""Read-only check of findings_205_209.json: every fix 'old' must occur exactly once in the original page_NNN.tex,
and the fixes must apply in the listed order (simulated in memory) both on page_NNN.tex and on the release page
segment that apply_fixes.py would edit. Writes nothing."""
import json
import pathlib
import re
from collections import Counter

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_I_b"
findings = json.load(open(RUN / "findings_205_209.json", encoding="utf-8"))
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")


def release_segment(page):
    for f in inv["I"]["files"]:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return pathlib.Path(f).name, t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
    return None, None


ok = True
by_page = {}
for x in findings:
    by_page.setdefault(x["page"], []).append(x)
for page, xs in sorted(by_page.items()):
    orig = (RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    fname, seg = release_segment(page)
    cur_p, cur_r = orig, seg
    for x in xs:
        fx = x.get("fix")
        if not fx:
            continue
        old, new = fx["old"], fx["new"]
        c0 = orig.count(old)
        cp, cr = cur_p.count(old), cur_r.count(old)
        flag = "OK " if (c0 == 1 and cp == 1 and cr == 1) else "BAD"
        if flag == "BAD":
            ok = False
        print(f"{flag} p{page} orig={c0} seq_page={cp} seq_release={cr} | {old[:60]!r}")
        if cp == 1:
            cur_p = cur_p.replace(old, new)
        if cr == 1:
            cur_r = cur_r.replace(old, new)
    # brace balance of each 'new' vs 'old'
    for x in xs:
        fx = x.get("fix")
        if fx:
            d = (fx["new"].count("{") - fx["new"].count("}")) - (fx["old"].count("{") - fx["old"].count("}"))
            if d:
                ok = False
                print("BRACE", page, fx)
    print(f"  page {page}: release file {fname}; release segment == page copy body: "
          f"{seg.strip() == orig.split(chr(10), 1)[1].strip()}")
cnt = Counter((x["page"], "misprint" if x["kind"] == "misprint_in_print" else
               ("convention" if x["kind"] == "convention" else "normal")) for x in findings)
for p in sorted(by_page):
    print(p, {k: cnt[(p, k)] for k in ("normal", "convention", "misprint")})
print("conventions:", Counter(x["convention"] for x in findings if x["kind"] == "convention"))
print("ALL OK" if ok else "PROBLEMS")
