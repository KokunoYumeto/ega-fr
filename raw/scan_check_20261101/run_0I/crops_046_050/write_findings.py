import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_0I"
OUT = os.path.join(RUN, "findings_046_050.json")

F = []

def add(**kw):
    kw.setdefault("convention", None)
    F.append(kw)

# ---------------- page 46 ----------------
add(page=46,
    where="(5.2.3), first sentence: 'tels que G soit de type fini'",
    scan="soit de *type fini*, (\"de\" upright; only \"type fini\" italic)",
    tex="soit \\emph{de type fini},",
    kind="italics", confidence="high",
    fix={"old": "soit \\emph{de type fini}", "new": "soit de \\emph{type fini}"},
    note="Checked on an enlarged crop: 'de' is roman.")

add(page=46,
    where="(5.2.4), 'comme f_U est exact a droite (4.3.1) et commute aux sommes directes (4.3.2)'",
    scan="comme f_U est exact \u00e0 droite (f_U without asterisk)",
    tex="comme $f_U$ est exact \u00e0 droite",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="comme $f_U^*$ est exact \u00e0 droite",
    note="TeX keeps the printed reading. Right exactness and commuting with direct sums are properties of the functor f_U^*; "
         "the same argument in (5.3.11), p. 48, prints 'comme f_U^* est exact \u00e0 droite'.")

# ---------------- page 48 ----------------
add(page=48,
    where="(5.3.9), statement: 'alors il existe un voisinage ouvert U de X'",
    scan="un voisinage ouvert U de X (capital X)",
    tex="voisinage ouvert $U$ de $X$",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="voisinage ouvert $U$ de $x$",
    note="TeX keeps the printed reading. The neighbourhood is of the point x (M is an O_x-module and F_x is to be isomorphic to M).")

add(page=48,
    where="(5.3.9), proof: 'il existe une section u de Hom(O_X^p, O_X^q) telle que u_x = phi'",
    scan="il existe une section u de \U0001D4D7om_{\U0001D4AA_X}(\U0001D4AA_X^p, \U0001D4AA_X^q) telle que u_x=\u03c6 ;",
    tex="$\\mathcal{H}\\!om_{\\mathcal{O}_X}(\\mathcal{O}_X^p,\\mathcal{O}_X^q)$ au-dessus d'un voisinage ouvert $U$ de $x$ telle que $u_x=\\varphi$",
    kind="extra", confidence="high",
    fix={"old": "au-dessus\nd'un voisinage ouvert $U$ de $x$ telle que", "new": "telle que"},
    note="'au-dessus d'un voisinage ouvert U de x' is not in the print; it is an editorial completion "
         "(the print uses U in the following clause without introducing it in the proof).")

# ---------------- page 49 ----------------
add(page=49,
    where="(5.4.3), 'Or, pour tout O_X-Module F, on a un homomorphisme canonique O_X -> Hom(F,F) (5.3.7)'",
    scan="homomorphisme canonique \U0001D4AA_X \u2972 \U0001D4D7om_{\U0001D4AA_X}(\U0001D4D5, \U0001D4D5) (arrow with tilde above)",
    tex="$\\mathcal{O}_X\\xrightarrow{\\sim}\n\\mathcal{H}\\!om_{\\mathcal{O}_X}(\\mathcal{F},\\mathcal{F})$",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="$\\mathcal{O}_X\\to\\mathcal{H}\\!om_{\\mathcal{O}_X}(\\mathcal{F},\\mathcal{F})$",
    note="TeX keeps the printed isomorphism arrow. For an arbitrary F this map is only a homomorphism; "
         "the next sentence proves bijectivity only when F = L is invertible.")

# ---------------- page 50 ----------------
add(page=50,
    where="(5.4.5), 'et lorsque L est localement libre, cet homomorphisme est bijectif'",
    scan="lorsque L est localement libre (roman capital L, not script)",
    tex="lorsque $L$ est localement libre",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="lorsque $\\mathcal{L}$ est localement libre",
    note="TeX keeps the printed reading.")

add(page=50,
    where="(5.4.5), 'homomorphisme canonique fonctoriel f^*(L-check) -> (f^*(L))-check (4.4.6)'",
    scan="(f^*(\U0001D4DB))\u02c7 : the check accent is set after the closing parenthesis, like an exponent",
    tex="\\check{\\bigl(f^*(\\mathcal{L})\\bigr)}",
    kind="symbol", confidence="medium",
    fix={"old": "\\check{\\bigl(f^*(\\mathcal{L})\\bigr)}", "new": "\\bigl(f^*(\\mathcal{L})\\bigr)\\check{}"},
    note="Same pattern as convention 5, but with a check instead of a tilde; the coordinator may prefer one document-wide rendering. "
         "(The print has this formula in-line rather than displayed; layout only.)")

add(page=50,
    where="(5.4.6), first paragraph: 'ou s_n in Gamma(X, L^{(x)n}), s_m in Gamma(X, L^{(x)n})'",
    scan="s_m\u2208\u0393(X, \U0001D4DB^{\u2297n})",
    tex="$s_m\\in\\Gamma(X,\\mathcal{L}^{\\otimes m})$",
    kind="misprint_in_print", confidence="high",
    fix={"old": "$s_m\\in\\Gamma(X,\\mathcal{L}^{\\otimes m})$", "new": "$s_m\\in\\Gamma(X,\\mathcal{L}^{\\otimes n})$"},
    corrected="$s_m\\in\\Gamma(X,\\mathcal{L}^{\\otimes m})$",
    note="TeX silently corrects the print's exponent (x)n to (x)m; the fix restores the printed reading.")

add(page=50,
    where="(5.4.6), second paragraph: 'et u_m in Gamma(X, F (x) L^{(x)m})'",
    scan="u_m\u2208\u0393(X, \U0001D4D5\u2297\U0001D4DB^{\u2297m}) : tensor sign without subscript",
    tex="$u_m\\in\\Gamma(X,\n\\mathcal{F}\\otimes_{\\mathcal{O}_X}\\mathcal{L}^{\\otimes m})$",
    kind="formula", confidence="high",
    fix={"old": "\\mathcal{F}\\otimes_{\\mathcal{O}_X}\\mathcal{L}^{\\otimes m})$, on fait",
         "new": "\\mathcal{F}\\otimes\\mathcal{L}^{\\otimes m})$, on fait"},
    note="The print omits the subscript O_X here (it is printed in the definition of Gamma_*(L,F) just above).")

add(page=50,
    where="(5.4.6), second paragraph: 'la section de F (x) L^{(x)(m+n)}'",
    scan="\U0001D4D5\u2297\U0001D4DB^{\u2297(m+n)} : tensor sign without subscript",
    tex="$\\mathcal{F}\\otimes_{\\mathcal{O}_X}\\mathcal{L}^{\\otimes(m+n)}$",
    kind="formula", confidence="high",
    fix={"old": "\\mathcal{F}\\otimes_{\\mathcal{O}_X}\\mathcal{L}^{\\otimes(m+n)}",
         "new": "\\mathcal{F}\\otimes\\mathcal{L}^{\\otimes(m+n)}"},
    note="")

add(page=50,
    where="(5.4.6), last paragraph: 'Gamma(X, F (x) L^{(x)n}) -> Gamma(Y, f^*(F (x) L^{(x)n}))'",
    scan="\u0393(X, \U0001D4D5\u2297\U0001D4DB^{\u2297n}) \u2192 \u0393(Y, f*(\U0001D4D5\u2297\U0001D4DB^{\u2297n})) : both tensor signs without subscript",
    tex="\\otimes_{\\mathcal{O}_X} in both Gamma factors",
    kind="formula", confidence="high",
    fix={"old": "\\mathcal{F}\\otimes_{\\mathcal{O}_X}\\mathcal{L}^{\\otimes n}\\bigr)\n  \\longrightarrow\n  \\Gamma\\bigl(Y,\n    f^*(\\mathcal{F}\\otimes_{\\mathcal{O}_X}\\mathcal{L}^{\\otimes n})\\bigr),",
         "new": "\\mathcal{F}\\otimes\\mathcal{L}^{\\otimes n}\\bigr)\n  \\longrightarrow\n  \\Gamma\\bigl(Y,\n    f^*(\\mathcal{F}\\otimes\\mathcal{L}^{\\otimes n})\\bigr),"},
    note="(The print has this map in-line rather than displayed; layout only.)")

add(page=50,
    where="(5.4.6), last display: 'f^*(F (x) L^{(x)n}) = f^*(F) (x) (f^*(L))^{(x)n}'",
    scan="f*(\U0001D4D5\u2297\U0001D4DB^{\u2297n})=f*(\U0001D4D5)\u2297(f*(\U0001D4DB))^{\u2297n} : no subscripts on either tensor sign",
    tex="f^*(\\mathcal{F}\\otimes_{\\mathcal{O}_X}\\mathcal{L}^{\\otimes n}) =f^*(\\mathcal{F})\\otimes_{\\mathcal{O}_Y} (f^*(\\mathcal{L}))^{\\otimes n}",
    kind="formula", confidence="high",
    fix={"old": "f^*(\\mathcal{F}\\otimes_{\\mathcal{O}_X}\\mathcal{L}^{\\otimes n})\n  =f^*(\\mathcal{F})\\otimes_{\\mathcal{O}_Y}",
         "new": "f^*(\\mathcal{F}\\otimes\\mathcal{L}^{\\otimes n})\n  =f^*(\\mathcal{F})\\otimes"},
    note="")

add(page=50,
    where="(5.4.6), last display: reference '(4.3.3.1),'",
    scan="... (f*(\U0001D4DB))^{\u2297n}  (4.3.3.1),  : a citation set right after the formula, followed by a comma",
    tex="\\tag{4.3.3.1}",
    kind="other", confidence="high",
    fix={"old": "\\tag{4.3.3.1}", "new": "\\quad\\text{(4.3.3.1),}"},
    note="\\tag turns the reference into an equation number of this formula (it cites (4.3.3.1) of section 4) and drops the printed comma; "
         "the sentence continues on p. 51.")

# ---------------- checks ----------------
ok = True
tex_cache = {}
for i, f in enumerate(F):
    p = f["page"]
    if p not in tex_cache:
        with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
            # page files here are CRLF; the release files use LF, so compare on LF text
            tex_cache[p] = fh.read().replace("\r\n", "\n")
    t = tex_cache[p]
    if "\r" in t:
        print("WARNING: stray CR in page", p)
    if f.get("fix"):
        n = t.count(f["fix"]["old"])
        if n != 1:
            ok = False
        print("p%d #%d kind=%s old-count=%d" % (p, i, f["kind"], n))
    else:
        print("p%d #%d kind=%s fix=null" % (p, i, f["kind"]))
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False
        print("  missing corrected")

# fixes on the same page must not overlap
for p, t in tex_cache.items():
    spans = []
    for f in F:
        if f["page"] == p and f.get("fix"):
            s = t.find(f["fix"]["old"])
            spans.append((s, s + len(f["fix"]["old"])))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP on page", p, a, b)

if not ok:
    print("CHECK FAILED; not writing")
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("wrote", OUT, len(F), "findings")
