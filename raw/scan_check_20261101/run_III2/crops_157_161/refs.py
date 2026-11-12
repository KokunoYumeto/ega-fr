import re, pathlib, collections
p = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native")
t6 = (p / "ega3" / "ega3-6-fr.tex").read_text(encoding="utf-8")
t7 = (p / "ega3" / "ega3-7-fr.tex").read_text(encoding="utf-8")
pat = re.compile(r"\(\$0_\{\\mathrm \{?I\}?\}\$, [0-9.]+\)")
for name, t in (("ega3-6", t6), ("ega3-7", t7)):
    c = collections.Counter(pat.findall(t))
    print(name, "0_I refs:", sum(c.values()))
    print("  ", sorted(c.items()))
    print("   0_III forms:", len(re.findall(r"0_\{\\mathrm\{?III", t)), " textbf{0}:", t.count("\\textbf{0}"))
    print("   mathfrak{Tor}:", t.count("\\mathfrak{Tor}"), " mathscr{T}\\!or:", t.count("\\mathscr{T}\\!or"),
          " ^{\\sim} after paren:", len(re.findall(r"\)(\\bigr\)|\\Bigr\)|\))?\^\{?\\sim", t)))
for f in ["ega1/ega1-1-fr.tex", "ega1/ega0-1-fr.tex", "ega1/ega1-2-fr.tex"]:
    t = (p / f).read_text(encoding="utf-8")
    for lab in ["[1.4.15]", "{1.4.15.1}", "[4.15", "[6.7.1]", "[6.2.1]"]:
        i = t.find(lab)
        if i >= 0:
            print(f, lab, repr(t[i:i + 200]))
