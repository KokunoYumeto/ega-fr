import sys
base = r"user\Documents\ega_scan_check_20261101"
src = base + r"\ega-fr\editions\2026-10-24-r20\%s\packages\IV1\native\ega4\ega0-19-fr.tex"
for ed in ("diplomatic", "current"):
    t = open(src % ed, encoding="utf-8", newline="").read()
    print(ed, "CRLF" if "\r\n" in t else "LF")
    for p in range(86, 91):
        mk = "\\oldpage[0\\textsubscript{IV-1}]{%d}"
        m1 = t.find(mk % p)
        m2 = t.find(mk % (p + 1))
        seg = t[m1:m2]
        pf = open(base + r"\run_0IV1\page_%03d.tex" % p, encoding="utf-8", newline="").read()
        pf = pf.replace("\r\n", "\n").split("\n", 1)[1]
        same = seg == pf
        print(p, m1, m2, "same" if same else "DIFF", len(seg), len(pf))
        if not same:
            # first differing position
            for i, (a, b) in enumerate(zip(seg, pf)):
                if a != b:
                    print("   first diff at", i, repr(seg[max(0, i - 60):i + 60]), "|||", repr(pf[max(0, i - 60):i + 60]))
                    break
