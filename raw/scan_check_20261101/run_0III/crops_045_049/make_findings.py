"""Build findings_045_049.json for the EGA 0_III scan check (pp. 45-49)."""
import json
import pathlib

OUT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III\findings_045_049.json")
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


S_NOTE = ("The print names the coefficient system with a script S (𝒮), the letter the TeX's own index of notations uses "
          "(\\mathscr S, 0, 11.8.4-11.8.10); the TeX body of 11.8 writes \\Gamma. The components Γ_{σ,τ}, Γ^k_{σ,τ} are "
          "printed Γ and stay.")
KB = "Bold italic K', K'' (and bold italic category C) in the print; plain $K'$, $K''$ / \\mathcal C in the TeX."
C6 = ("Convention 6: the statement environment is italic, so the \\emph{...} wrapper sets the printed italic text upright; "
      "dropping the wrapper restores the print's italic.")

# ---------------- page 45 ----------------
add(45, "start of p. 45: heading (11.8.6)",
    "p. 45 begins with the heading '(11.8.6) La proposition (11.8.5) ramène ...'",
    "\\begin{env}[11.8.6] and \\label{0.11.8.6-fr} stand at the end of page 44's segment, before \\oldpage[0\\textsubscript{III}]{45}",
    "marker", None, "high",
    r"""\oldpage[0\textsubscript{III}]{45}
La proposition""",
    r"""\oldpage[0\textsubscript{III}]{45}
\begin{env}[11.8.6]
\label{0.11.8.6-fr}
La proposition""",
    "Second half of a move: apply together with deleting the two lines '\\begin{env}[11.8.6]\\n\\label{0.11.8.6-fr}\\n' "
    "at the end of page 44's segment (ega3-1-fr.tex, just before \\oldpage[0\\textsubscript{III}]{45}); otherwise the "
    "environment is opened twice.")
add(45, "(11.8.6), first sentence: 'cohomologie de L·(A, B; 𝒮) à celui de la cohomologie de C·(A, B; 𝒮)'",
    "L·(A, B; 𝒮), C·(A, B; 𝒮) (script S)", "\\mathrm L^\\bullet(A,B;\\Gamma), \\mathrm C^\\bullet(A,B;\\Gamma)",
    "symbol", None, "high",
    r"""$\mathrm L^\bullet(A,B;\Gamma)$ à celui de la cohomologie de
$\mathrm C^\bullet(A,B;\Gamma)$. Rappelons""",
    r"""$\mathrm L^\bullet(A,B;\mathscr S)$ à celui de la cohomologie de
$\mathrm C^\bullet(A,B;\mathscr S)$. Rappelons""",
    S_NOTE)
add(45, "(11.8.6): 'tels que σ et τ aient le même degré;'", "'le même degré' italic", "upright",
    "italics", None, "high", "aient le même degré;", r"aient \emph{le même degré};", "")
add(45, "(11.8.6): 'la différentielle de ce complexe est donnée par d : (σ, τ) ⇝ Σ_{j,k} (—1)^{j+k}(σ_j, τ_k) si'",
    "in the running text: 'd : (σ, τ) ⇝ Σ_{j,k}(—1)^{j+k}(σ_j, τ_k)' (squiggly arrow)",
    "displayed: d(\\sigma,\\tau)=\\sum_{j,k}(-1)^{j+k}(\\sigma_j,\\tau_k)",
    "formula", None, "high",
    r"""est donnée par
\[
d(\sigma,\tau)=\sum_{j,k}(-1)^{j+k}(\sigma_j,\tau_k)
\]
si
""",
    r"""est donnée par
$d:(\sigma,\tau)\leadsto\sum_{j,k}(-1)^{j+k}(\sigma_j,\tau_k)$ si
""",
    "The print writes the differential as a map 'd : (σ, τ) ⇝ ...' (the arrow \\leadsto used elsewhere in ega3-1-fr.tex), "
    "not as an equation 'd(σ, τ) = ...'; the formula is also set inline, not displayed.")
add(45, "(11.8.6): 'si dσ = Σ_j (—1)^j σ_j et dτ = Σ_k (—1)^k τ_k ; on a alors'",
    "inline, the two formulas joined by 'et'", "displayed, joined by ',\\qquad'",
    "missing", None, "high",
    r"""\[
d\sigma=\sum_j(-1)^j\sigma_j,\qquad
d\tau=\sum_k(-1)^k\tau_k;
\]
on a alors""",
    r"""$d\sigma=\sum_j(-1)^j\sigma_j$ et $d\tau=\sum_k(-1)^k\tau_k$;
on a alors""",
    "Missing word 'et'; the print also sets the formulas in the running text.")
add(45, "(11.8.6): 'qu'il y a des homotopies h, h' telles que'", "'homotopies' italic", "upright",
    "italics", None, "high", "qu'il y a des homotopies $h$", r"qu'il y a des \emph{homotopies} $h$", "")
add(45, "(11.8.6), display 'f∘g—1 = d∘h + h∘d   et   g∘f—1 = d∘h' + h'∘d.'",
    "the two equations are joined by 'et'", "joined by ',\\qquad'",
    "missing", None, "high", r"f\circ g-1=d\circ h+h\circ d,\qquad", r"f\circ g-1=d\circ h+h\circ d\qquad\text{et}\qquad",
    "Missing word 'et' between the two displayed equations (no comma in the print).")
add(45, "(11.8.6): 'En outre, on a f(σ, τ)∈C.(|σ|)⊗C.(|τ|) et g(σ, τ)∈P.(|σ|, |τ|) et les homotopies'",
    "inline, the two memberships joined by 'et'", "displayed, joined by ',\\qquad'",
    "missing", None, "high",
    r"""En outre, on a
\[
f(\sigma,\tau)\in\mathrm C_\bullet(|\sigma|)
\otimes\mathrm C_\bullet(|\tau|),\qquad
g(\sigma,\tau)\in\mathrm P_\bullet(|\sigma|,|\tau|)
\]
""",
    r"""En outre, on a
$f(\sigma,\tau)\in\mathrm C_\bullet(|\sigma|)
\otimes\mathrm C_\bullet(|\tau|)$ et
$g(\sigma,\tau)\in\mathrm P_\bullet(|\sigma|,|\tau|)$
""",
    "Missing word 'et'; the print sets both formulas in the running text.")
add(45, "(11.8.6): 'les homotopies h, h' peuvent être prises telles que'", "'peuvent être prises telles que' italic",
    "upright", "italics", None, "high",
    "$h'$ peuvent être prises telles que", r"$h'$ \emph{peuvent être prises telles que}", "")
add(45, "(11.8.6): 'h(σ, τ)∈C.(|σ|)⊗C.(|τ|) et h'(σ, τ)∈P.(|σ|, |τ|). Ce point provient'",
    "inline, joined by an italic 'et'", "displayed, joined by ',\\qquad'",
    "missing", None, "high",
    r"""\[
h(\sigma,\tau)\in\mathrm C_\bullet(|\sigma|)
\otimes\mathrm C_\bullet(|\tau|),\qquad
h'(\sigma,\tau)\in\mathrm P_\bullet(|\sigma|,|\tau|).
\]
""",
    r"""$h(\sigma,\tau)\in\mathrm C_\bullet(|\sigma|)
\otimes\mathrm C_\bullet(|\tau|)$ \emph{et}
$h'(\sigma,\tau)\in\mathrm P_\bullet(|\sigma|,|\tau|)$.
""",
    "Missing italic 'et'; the print sets both formulas in the running text.")
add(45, "(11.8.6): 'peut se faire par récurrence sur la somme'", "'récurrence' italic", "upright",
    "italics", None, "high", "par récurrence sur", r"par \emph{récurrence} sur", "")
add(45, "(11.8.6): 'et de ce que les H^q(C.(|σ|)⊗C.(|τ|)) et H^q(P.(|σ|, |τ|)) sont nuls'",
    "both formulas in the running text", "displayed with \\quad\\text{et}\\quad",
    "other", None, "high",
    r"""et de ce que les
\[
H^q(\mathrm C_\bullet(|\sigma|)\otimes\mathrm C_\bullet(|\tau|))
\quad\text{et}\quad
H^q(\mathrm P_\bullet(|\sigma|,|\tau|))
\]
""",
    r"""et de ce que les
$H^q(\mathrm C_\bullet(|\sigma|)\otimes\mathrm C_\bullet(|\tau|))$ et
$H^q(\mathrm P_\bullet(|\sigma|,|\tau|))$
""",
    "Layout only (display vs inline); the formulas match.")
add(45, "(11.8.6): 'sont nuls pour q>0'", "'nuls' italic", "upright",
    "italics", None, "high", "sont nuls pour $q>0$", r"sont \emph{nuls} pour $q>0$", "")
add(45, "(11.8.6): 'On définit alors P·(A, B; 𝒮)'", "P·(A, B; 𝒮)", "\\mathrm P^\\bullet(A,B;\\Gamma)",
    "symbol", None, "high", r"On définit alors $\mathrm P^\bullet(A,B;\Gamma)$",
    r"On définit alors $\mathrm P^\bullet(A,B;\mathscr S)$", S_NOTE)
add(45, "(11.8.6): 'et comme on a dσ = Σ_j (—1)^j σ_j∈C.(|σ|) et dτ = Σ_k (—1)^k τ_k∈C.(|τ|),'",
    "inline: 'dσ = Σ_j(—1)^jσ_j ∈ C.(|σ|) et dτ = Σ_k(—1)^kτ_k ∈ C.(|τ|),'",
    "displayed 'd\\sigma=\\sum_j(-1)^j\\sigma_j,\\qquad d\\tau=\\sum_k(-1)^k\\tau_k,' without the memberships",
    "missing", None, "high",
    r"""et comme on a
\[
d\sigma=\sum_j(-1)^j\sigma_j,\qquad
d\tau=\sum_k(-1)^k\tau_k,
\]
""",
    r"""et comme on a
$d\sigma=\sum_j(-1)^j\sigma_j\in\mathrm C_\bullet(|\sigma|)$ et
$d\tau=\sum_k(-1)^k\tau_k\in\mathrm C_\bullet(|\tau|)$,
""",
    "The TeX drops '∈C.(|σ|)', '∈C.(|τ|)' and the word 'et'; the print sets the line in the running text.")
add(45, "(11.8.6), display 'dλ(σ, τ) = Σ(—1)^{j+k}λ(σ_j, τ_k)'", "Σ without any index",
    "\\sum_{j,k}", "extra", None, "high",
    r"\sum_{j,k}(-1)^{j+k}\lambda(\sigma_j,\tau_k)", r"\sum(-1)^{j+k}\lambda(\sigma_j,\tau_k)",
    "The print's Σ in this display carries no j, k (not a matter of index position).")
add(45, "(11.8.6): 'la différentielle du complexe P·(A, B; 𝒮). Cela étant'", "P·(A, B; 𝒮)",
    "\\mathrm P^\\bullet(A,B;\\Gamma)", "symbol", None, "high",
    r"""du complexe
$\mathrm P^\bullet(A,B;\Gamma)$. Cela étant""",
    r"""du complexe
$\mathrm P^\bullet(A,B;\mathscr S)$. Cela étant""", S_NOTE)
add(45, "(11.8.6): 'les applications ᵗf : λ→λ∘f, ᵗg : λ→λ∘g, ᵗh : λ→λ∘h et ᵗh' : λ→λ∘h' sont toutes'",
    "transposes with a left superscript t (ᵗf, ᵗg, ᵗh, ᵗh'), plain arrows, 'et' before ᵗh', in the running text",
    "displayed {}'f:\\lambda\\mapsto\\lambda\\circ f,\\quad ... (left prime, \\mapsto, no 'et')",
    "symbol", None, "high",
    r"""\[
{}'f:\lambda\mapsto\lambda\circ f,\quad
{}'g:\lambda\mapsto\lambda\circ g,\quad
{}'h:\lambda\mapsto\lambda\circ h,\quad
{}'h':\lambda\mapsto\lambda\circ h'
\]
""",
    r"""${}^tf:\lambda\to\lambda\circ f$, ${}^tg:\lambda\to\lambda\circ g$,
${}^th:\lambda\to\lambda\circ h$ et ${}^th':\lambda\to\lambda\circ h'$
""",
    "The print's transpose sign is a superscript t before the letter (as ᵗp, ᵗj on p. 44), not a prime. The edit also "
    "adds the missing 'et', replaces the four \\mapsto (convention 3, listed separately) and sets the line inline.")
for x in ("f", "g", "h", "h'"):
    add(45, f"(11.8.6): 'ᵗ{x} : λ→λ∘{x}'", "plain arrow →", "\\mapsto", "convention", 3, "high", None, None,
        "Edit included in the fix of the finding \"(11.8.6): 'les applications ᵗf : λ→λ∘f, ...'\" (same page).")
add(45, "(11.8.6): 'sont toutes définies en vertu des remarques'", "'définies' italic", "upright",
    "italics", None, "high", "sont toutes définies en vertu", r"sont toutes \emph{définies} en vertu", "")
add(45, "(11.8.6): 'ᵗf∘ᵗg et ᵗg∘ᵗf sont donc homotopes'", "ᵗf∘ᵗg, ᵗg∘ᵗf (left superscript t)",
    "\\mathop{}'f\\circ{}'g, \\mathop{}'g\\circ{}'f (left prime)", "symbol", None, "high",
    r"$\mathop{}'f\circ{}'g$ et $\mathop{}'g\circ{}'f$", r"${}^tf\circ{}^tg$ et ${}^tg\circ{}^tf$",
    "Transpose sign: superscript t, not a prime.")
add(45, "(11.8.6), last sentence: 'cohomologie de C·(A, B; 𝒮) et celle de P·(A, B; 𝒮).'", "𝒮 twice", "\\Gamma twice",
    "symbol", None, "high",
    r"""$\mathrm C^\bullet(A,B;\Gamma)$ et celle de
$\mathrm P^\bullet(A,B;\Gamma)$.""",
    r"""$\mathrm C^\bullet(A,B;\mathscr S)$ et celle de
$\mathrm P^\bullet(A,B;\mathscr S)$.""", S_NOTE)
add(45, "Remarque (11.8.7): 'cohomologie de L·(A; 𝒮) sur celle de C·(A; 𝒮)'", "𝒮 twice", "\\Gamma twice",
    "symbol", None, "high",
    r"""$\mathrm L^\bullet(A;\Gamma)$ sur celle de
$\mathrm C^\bullet(A;\Gamma)$""",
    r"""$\mathrm L^\bullet(A;\mathscr S)$ sur celle de
$\mathrm C^\bullet(A;\mathscr S)$""", S_NOTE)
add(45, "(11.8.8): 'considérons un complexe 𝒮· = (𝒮^k) de systèmes de coefficients sur'",
    "'complexe' italic", "upright", "italics", None, "high",
    "considérons un complexe\n", "considérons un \\emph{complexe}\n", "")
add(45, "(11.8.8): '𝒮· = (𝒮^k)'", "𝒮· = (𝒮^k)", "\\Gamma^\\bullet=(\\Gamma^k)", "symbol", None, "high",
    r"$\Gamma^\bullet=(\Gamma^k)$", r"$\mathscr S^\bullet=(\mathscr S^k)$",
    S_NOTE + " The components Γ^k_{σ,τ} on the next line and in the diagram are printed Γ.")
add(45, "(11.8.8): 'de systèmes de coefficients sur Σ(A)×Σ(B)'", "'de systèmes de coefficients' italic", "upright",
    "italics", None, "high", "de systèmes de coefficients sur", r"\emph{de systèmes de coefficients} sur", "")

# ---------------- page 46 ----------------
add(46, "(11.8.8): 'Alors on vérifie aussitôt que C·(A, B; 𝒮·) = (C^h(A, B; 𝒮^k))_{(h,k)∈Z×Z} est un bicomplexe'",
    "𝒮·, 𝒮^k; formula in the running text", "\\Gamma^\\bullet, \\Gamma^k; displayed", "symbol", None, "high",
    r"""aussitôt que
\[
\mathrm C^\bullet(A,B;\Gamma^\bullet)
=\bigl(\mathrm C^h(A,B;\Gamma^k)\bigr)_{(h,k)\in\mathbb Z\times\mathbb Z}
\]
""",
    r"""aussitôt que
$\mathrm C^\bullet(A,B;\mathscr S^\bullet)
=\bigl(\mathrm C^h(A,B;\mathscr S^k)\bigr)_{(h,k)\in\mathbb Z\times\mathbb Z}$
""", S_NOTE + " The edit also sets the formula inline, as printed.")
add(46, "(11.8.8): 'est un bicomplexe de groupes abéliens'", "'bicomplexe' italic", "upright",
    "italics", None, "high", "est un bicomplexe de groupes", r"est un \emph{bicomplexe} de groupes", "")
add(46, "(11.8.8): 'et L·(A, B; 𝒮·) = (L^h(A, B; 𝒮^k)) en est un sous-bicomplexe'",
    "𝒮·, 𝒮^k; formula in the running text", "\\Gamma^\\bullet, \\Gamma^k; displayed", "symbol", None, "high",
    r"""abéliens, et
\[
\mathrm L^\bullet(A,B;\Gamma^\bullet)
=\bigl(\mathrm L^h(A,B;\Gamma^k)\bigr)
\]
""",
    r"""abéliens, et
$\mathrm L^\bullet(A,B;\mathscr S^\bullet)
=\bigl(\mathrm L^h(A,B;\mathscr S^k)\bigr)$
""", S_NOTE + " The edit also sets the formula inline, as printed.")
add(46, "Proposition (11.8.9): 'L'injection canonique L·(A, B; 𝒮·)→C·(A, B; 𝒮·) définit un isomorphisme ...'",
    "𝒮· twice; formula in the running text; whole statement italic",
    "\\Gamma^\\bullet twice; displayed; statement wrapped in \\emph{...} inside the italic environment (upright)",
    "symbol", None, "high",
    r"""\emph{L'injection canonique
\[
\mathrm L^\bullet(A,B;\Gamma^\bullet)\longrightarrow
\mathrm C^\bullet(A,B;\Gamma^\bullet)
\]
définit un isomorphisme pour la cohomologie de ces deux bicomplexes.}""",
    r"""L'injection canonique
$\mathrm L^\bullet(A,B;\mathscr S^\bullet)\to
\mathrm C^\bullet(A,B;\mathscr S^\bullet)$
définit un isomorphisme pour la cohomologie de ces deux bicomplexes.""",
    S_NOTE + " The edit also removes the \\emph wrapper (convention 6, listed separately) and sets the formula inline.")
add(46, "Proposition (11.8.9), whole statement", "italic", "\\emph{...} inside the italic proposition environment: upright",
    "convention", 6, "high", None, None,
    "Edit included in the fix of the finding 'Proposition (11.8.9): L'injection canonique ...' (same page). " + C6)
add(46, "proof of (11.8.9): 'Posons C·· = C·(A, B; 𝒮·) et L·· = L·(A, B; 𝒮·)'", "𝒮· twice", "\\Gamma^\\bullet twice",
    "symbol", None, "high",
    r"""\mathrm C^\bullet(A,B;\Gamma^\bullet)$ et
$\mathrm L^{\bullet\bullet}=
\mathrm L^\bullet(A,B;\Gamma^\bullet)$ pour simplifier""",
    r"""\mathrm C^\bullet(A,B;\mathscr S^\bullet)$ et
$\mathrm L^{\bullet\bullet}=
\mathrm L^\bullet(A,B;\mathscr S^\bullet)$ pour simplifier""", S_NOTE)
add(46, "proof of (11.8.9): 'sont régulières (11.3.3)'", "'régulières' italic", "upright",
    "italics", None, "high", "bicomplexes sont régulières", r"bicomplexes sont \emph{régulières}", "")
add(46, "proof of (11.8.9): 'spectrales ''E(L··)→''E(C··) qui, pour les termes E_2'", "in the running text", "displayed",
    "other", None, "high",
    r"""morphisme de suites spectrales
\[
{}''E(\mathrm L^{\bullet\bullet})\longrightarrow
{}''E(\mathrm C^{\bullet\bullet})
\]
""",
    r"""morphisme de suites spectrales
${}''E(\mathrm L^{\bullet\bullet})\to
{}''E(\mathrm C^{\bullet\bullet})$
""", "Layout only (display vs inline); the formula matches.")
add(46, "proof of (11.8.9): 'est bijectif; la conclusion'", "'bijectif' italic", "upright",
    "italics", None, "high", "est bijectif; la conclusion", r"est \emph{bijectif}; la conclusion", "")
add(46, "(11.8.10): 'homomorphismes canoniques de bicomplexes C·(A, B; 𝒮·)→P·(A, B; 𝒮·) (avec'",
    "𝒮· twice; formula in the running text", "\\Gamma^\\bullet twice; displayed", "symbol", None, "high",
    r"""canoniques de bicomplexes
\[
\mathrm C^\bullet(A,B;\Gamma^\bullet)\longrightarrow
\mathrm P^\bullet(A,B;\Gamma^\bullet)
\]
""",
    r"""canoniques de bicomplexes
$\mathrm C^\bullet(A,B;\mathscr S^\bullet)\to
\mathrm P^\bullet(A,B;\mathscr S^\bullet)$
""", S_NOTE + " The edit also sets the formula inline, as printed.")
add(46, "(11.8.10): 'donne encore un isomorphisme en cohomologie'", "'isomorphisme' italic", "upright",
    "italics", None, "high", "un isomorphisme en cohomologie.", r"un \emph{isomorphisme} en cohomologie.", "")
add(46, "Proposition (11.9.1), first sentence: 'Soient C une catégorie abélienne, K' et K'' des parties ... telles que K''⊂K'",
    "category C and K', K'' bold italic", "\\mathcal C, plain italic K', K''", "font", None, "high",
    r"""Soient $\mathcal C$ une catégorie abélienne, $K'$ et $K''$ des parties de
l'ensemble des objets de $\mathcal C$, telles que $K''\subset K'$, et""",
    r"""Soient $\boldsymbol{C}$ une catégorie abélienne, $\boldsymbol{K}'$ et $\boldsymbol{K}''$ des parties de
l'ensemble des objets de $\boldsymbol{C}$, telles que $\boldsymbol{K}''\subset\boldsymbol{K}'$, et""", KB)
add(46, "Proposition (11.9.1) (i): 'tels que uv soit un épimorphisme'", "uv (juxtaposition)", "u\\circ v",
    "formula", None, "high",
    r"""\item[{\rm(i)}] \emph{Pour tout objet $A'\in K'$ et tout épimorphisme
$u:A\to A'$ dans $\mathcal C$, il existe un objet $B\in K''$ et un morphisme
$v:B\to A$ tels que $u\circ v$ soit un épimorphisme.}""",
    r"""\item[{\rm(i)}] Pour tout objet $A'\in\boldsymbol{K}'$ et tout épimorphisme
$u:A\to A'$ dans $\boldsymbol{C}$, il existe un objet $B\in\boldsymbol{K}''$ et un morphisme
$v:B\to A$ tels que $uv$ soit un épimorphisme.""",
    "The edit also sets bold italic K', K'', C (" + KB + ") and removes the \\emph wrapper (convention 6, listed separately).")
add(46, "Proposition (11.9.1) (i), statement text", "italic", "\\emph{...} inside the italic proposition environment: upright",
    "convention", 6, "high", None, None,
    "Edit included in the fix of the finding 'Proposition (11.9.1) (i): tels que uv soit un épimorphisme' (same page). " + C6)
add(46, "Proposition (11.9.1) (ii): 'A∈K', B∈K' ... Ker(u) appartient à K''", "K' bold italic (3 times)", "plain $K'$",
    "font", None, "high",
    r"""\item[{\rm(ii)}] \emph{Pour tout couple d'objets $A\in K'$, $B\in K'$ et
tout épimorphisme $u:A\to B$, $\operatorname{Ker}(u)$ appartient à $K'$.}""",
    r"""\item[{\rm(ii)}] Pour tout couple d'objets $A\in\boldsymbol{K}'$, $B\in\boldsymbol{K}'$ et
tout épimorphisme $u:A\to B$, $\operatorname{Ker}(u)$ appartient à $\boldsymbol{K}'$.""",
    KB + " The edit also removes the \\emph wrapper (convention 6, listed separately).")
add(46, "Proposition (11.9.1) (ii), statement text", "italic", "\\emph{...} inside the italic proposition environment: upright",
    "convention", 6, "high", None, None,
    "Edit included in the fix of the finding 'Proposition (11.9.1) (ii)' (same page). " + C6)
add(46, "Proposition (11.9.1) (iii): 'Le produit de deux objets de K'' appartient à K''.'", "K'' bold italic (twice)",
    "plain $K''$", "font", None, "high",
    r"""\item[{\rm(iii)}] \emph{Le produit de deux objets de $K''$ appartient à
$K''$.}""",
    r"""\item[{\rm(iii)}] Le produit de deux objets de $\boldsymbol{K}''$ appartient à
$\boldsymbol{K}''$.""",
    KB + " The edit also removes the \\emph wrapper (convention 6, listed separately).")
add(46, "Proposition (11.9.1) (iii), statement text", "italic", "\\emph{...} inside the italic proposition environment: upright",
    "convention", 6, "high", None, None,
    "Edit included in the fix of the finding 'Proposition (11.9.1) (iii)' (same page). " + C6)
add(46, "Proposition (11.9.1), last paragraph: 'un complexe Q. = (Q_i)_{i∈Z} dans C tel que Q_i∈K''",
    "no comma after 'dans C'", "'dans $\\mathcal C$, tel que'", "punctuation", None, "high",
    r"""\emph{Soit $P_\bullet=(P_i)_{i\in\mathbb Z}$ un complexe dans $\mathcal C$,
tel que $H_i(P_\bullet)\in K'$ pour tout $i$, et qu'il existe $d$ tel que
$H_i(P_\bullet)=0$ pour $i<d$. Alors il existe un complexe
$Q_\bullet=(Q_i)_{i\in\mathbb Z}$ dans $\mathcal C$, tel que $Q_i\in K''$
pour tout $i$ et $Q_i=0$ pour $i<d$, et un morphisme
$u:Q_\bullet\to P_\bullet$ de complexes tel que le morphisme correspondant
$H_\bullet(Q_\bullet)\to H_\bullet(P_\bullet)$ soit un isomorphisme.}""",
    r"""Soit $P_\bullet=(P_i)_{i\in\mathbb Z}$ un complexe dans $\boldsymbol{C}$,
tel que $H_i(P_\bullet)\in\boldsymbol{K}'$ pour tout $i$, et qu'il existe $d$ tel que
$H_i(P_\bullet)=0$ pour $i<d$. Alors il existe un complexe
$Q_\bullet=(Q_i)_{i\in\mathbb Z}$ dans $\boldsymbol{C}$ tel que $Q_i\in\boldsymbol{K}''$
pour tout $i$ et $Q_i=0$ pour $i<d$, et un morphisme
$u:Q_\bullet\to P_\bullet$ de complexes tel que le morphisme correspondant
$H_\bullet(Q_\bullet)\to H_\bullet(P_\bullet)$ soit un isomorphisme.""",
    "Extra comma. The edit also sets bold italic C (twice), K', K'' (" + KB + ") and removes the \\emph wrapper "
    "(convention 6, listed separately).")
add(46, "Proposition (11.9.1), paragraph 'Soit P. = (P_i)_{i∈Z} ... soit un isomorphisme.'", "italic",
    "\\emph{...} inside the italic proposition environment: upright", "convention", 6, "high", None, None,
    "Edit included in the fix of the finding 'Proposition (11.9.1), last paragraph' (same page). " + C6)
add(46, "proof of (11.9.1): '(i bis) Soient u : C→B ...'", "'(i' upright, 'bis' italic, ')' upright, then italic text",
    "'(i bis)' all inside \\emph (italic)", "italics", None, "high",
    r"\emph{(i bis) Soient", r"(i \emph{bis}) \emph{Soient",
    "The \\emph group opened here still closes after 'tels que le diagramme}' as before.")
add(46, "proof of (11.9.1), (i bis): 'un épimorphisme dans C, A un objet de K', v : A→B un morphisme dans C; ... D∈K''",
    "bold italic C (twice), K', K''", "\\mathcal C, plain K', K''", "font", None, "high",
    r"""épimorphisme dans $\mathcal C$, $A$ un
objet de $K'$, $v:A\to B$ un morphisme dans $\mathcal C$; il existe alors un
objet $D\in K''$, un épimorphisme""",
    r"""épimorphisme dans $\boldsymbol{C}$, $A$ un
objet de $\boldsymbol{K}'$, $v:A\to B$ un morphisme dans $\boldsymbol{C}$; il existe alors un
objet $D\in\boldsymbol{K}''$, un épimorphisme""", KB)
add(46, "proof of (11.9.1): 'le produit fibré C×_B A dans C et les projections'", "bold italic C", "\\mathcal C",
    "font", None, "high", r"$C\times_B A$ dans $\mathcal C$ et les", r"$C\times_B A$ dans $\boldsymbol{C}$ et les", KB)

# ---------------- page 47 ----------------
add(47, "diagram (11.9.1.2): labels p, v, u", "p, v, u set in bold italic; q in ordinary italic",
    "all four labels ordinary italic", "misprint_in_print", None, "medium",
    r"""C\times_B A\ar[r]^{q}\ar[d]_{p} & A\ar[d]^{v}\\
C\ar[r]_{u} & B""",
    r"""C\times_B A\ar[r]^{q}\ar[d]_{\boldsymbol{p}} & A\ar[d]^{\boldsymbol{v}}\\
C\ar[r]_{\boldsymbol{u}} & B""",
    "Wrong-font letters in the print (checked against the 600-dpi scan: p, v, u much heavier than q here and than the "
    "labels of (11.9.1.1)); the TeX silently uses ordinary italic. Fix reproduces the print.",
    corrected=r"""C\times_B A\ar[r]^{q}\ar[d]_{p} & A\ar[d]^{v}\\
C\ar[r]_{u} & B""")
add(47, "proof of (11.9.1): 'il y a un objet D∈K'' et un morphisme'", "bold italic K''", "plain $K''$",
    "font", None, "high", r"il y a un objet $D\in K''$ et un", r"il y a un objet $D\in\boldsymbol{K}''$ et un", KB)
add(47, "proof of (11.9.1): 'tels que qw soit un épimorphisme; on prendra u' = qw, v' = pw.'", "qw, qw, pw (juxtaposition)",
    "q\\circ w, q\\circ w, p\\circ w", "formula", None, "high",
    r"""tels que $q\circ w$ soit un épimorphisme; on
prendra $u'=q\circ w$, $v'=p\circ w$.""",
    r"""tels que $qw$ soit un épimorphisme; on
prendra $u'=qw$, $v'=pw$.""", "")
add(47, "proof of (11.9.1): 'les morphismes u_j : Q_j→P_j de sorte que'", "no comma after P_j", "comma after $P_j$",
    "punctuation", None, "high",
    r"""$u_j:Q_j\to P_j$, de
sorte que""",
    r"""$u_j:Q_j\to P_j$ de
sorte que""", "")
add(47, "(I_i): 'On a Q_j∈K'' pour j⩽i et B_j(Q.)∈K' pour j<i.'", "bold italic K'', K'", "plain $K''$, $K'$",
    "font", None, "high",
    r"""On a $Q_j\in K''$ pour $j\leq i$ et
$B_j(Q_\bullet)\in K'$ pour $j<i$.""",
    r"""On a $Q_j\in\boldsymbol{K}''$ pour $j\leq i$ et
$B_j(Q_\bullet)\in\boldsymbol{K}'$ pour $j<i$.""", KB)
add(47, "(II_i): 'est un isomorphisme.'", "'isomorphisme' italic", "upright",
    "italics", None, "high",
    r"""$(u_k)_{k\leq i}$
est un isomorphisme.""",
    r"""$(u_k)_{k\leq i}$
est un \emph{isomorphisme}.""", "")
add(47, "(III_i): 'Le morphisme composé v_i : Z_i(Q.)→Z_i(P.)→H_i(P.) (où la flèche'", "in the running text", "displayed",
    "other", None, "high",
    r"""Le morphisme composé
\[
v_i:Z_i(Q_\bullet)\longrightarrow Z_i(P_\bullet)
\longrightarrow H_i(P_\bullet)
\]
""",
    r"""Le morphisme composé
$v_i:Z_i(Q_\bullet)\to Z_i(P_\bullet)
\to H_i(P_\bullet)$
""", "Layout only (display vs inline); the formula matches.")
add(47, "(III_i): 'le morphisme canonique) est un épimorphisme.'", "'épimorphisme' italic", "upright",
    "italics", None, "high", "le morphisme canonique) est un épimorphisme.",
    r"le morphisme canonique) est un \emph{épimorphisme}.", "")
add(47, "proof of (11.9.1): 'appartient à K' en vertu de l'hypothèse (I_i)'", "bold italic K'", "plain $K'$",
    "font", None, "high", r"appartient à $K'$ en vertu de l'hypothèse",
    r"appartient à $\boldsymbol{K}'$ en vertu de l'hypothèse", KB)
add(47, "proof of (11.9.1): 'N_i = Ker (v_i) appartient aussi à K', compte tenu'", "bold italic K'", "plain $K'$",
    "font", None, "high", r"appartient aussi à $K'$, compte tenu", r"appartient aussi à $\boldsymbol{K}'$, compte tenu", KB)
add(47, "proof of (11.9.1): 'En vertu de (i bis), il existe'", "'bis' italic", "upright",
    "italics", None, "high", "En vertu de (i bis), il existe", r"En vertu de (i \emph{bis}), il existe", "")
add(47, "proof of (11.9.1): 'il existe un Q'_{i+1}∈K'', un épimorphisme'", "bold italic K''", "plain $K''$",
    "font", None, "high", r"$Q'_{i+1}\in K''$, un épimorphisme", r"$Q'_{i+1}\in\boldsymbol{K}''$, un épimorphisme", KB)
add(47, "proof of (11.9.1): 'que H_{i+1}(P.)∈K' par hypothèse'", "bold italic K'", "plain $K'$",
    "font", None, "high", r"$H_{i+1}(P_\bullet)\in K'$ par hypothèse", r"$H_{i+1}(P_\bullet)\in\boldsymbol{K}'$ par hypothèse", KB)
add(47, "proof of (11.9.1): 'un objet Q''_{i+1}∈K'' et un morphisme'", "bold italic K''", "plain $K''$",
    "font", None, "high", r"$Q''_{i+1}\in K''$ et un morphisme", r"$Q''_{i+1}\in\boldsymbol{K}''$ et un morphisme", KB)
add(47, "end of p. 47: 'est commutatif, la flèche horizontale inférieure étant 0.'",
    "printed p. 47 ends with diagram (11.9.1.4); the sentence 'est commutatif, ... étant o.' opens p. 48",
    "the sentence is the last line of page_047.tex, before \\oldpage[0\\textsubscript{III}]{48}", "marker", None, "high",
    r"""\]
est commutatif, la flèche horizontale inférieure étant $0$.
""",
    r"""\]
""",
    "First half of a move (both halves in this file): deletes the sentence here; the page-48 marker finding re-inserts "
    "it after \\oldpage[0\\textsubscript{III}]{48}. Apply both or neither; each 'old' lies in its own page segment.")

# ---------------- page 48 ----------------
add(48, "start of p. 48: 'est commutatif, la flèche horizontale inférieure étant 0. Prenons alors'",
    "p. 48 begins with this sentence", "the sentence stands before the marker, at the end of page 47",
    "marker", None, "high",
    r"""\oldpage[0\textsubscript{III}]{48}
""",
    r"""\oldpage[0\textsubscript{III}]{48}
est commutatif, la flèche horizontale inférieure étant $0$. """,
    "Second half of the move begun by the page-47 marker finding. Apply both or neither.")
add(48, "proof of (11.9.1): 'Prenons alors Q_{i+1} = Q'_{i+1}×Q''_{i+1}, qui appartient à K'' en vertu de (iii), et d_{i+1} = ..., u_{i+1} = ....'",
    "inline, with the clause 'qui appartient à K'' en vertu de (iii), et' after the product",
    "displayed Q_{i+1}=...,\\qquad d_{i+1}=...,\\qquad u_{i+1}=...; the clause is missing",
    "missing", None, "high",
    r"""Prenons alors
\[
Q_{i+1}=Q'_{i+1}\times Q''_{i+1},\qquad
d_{i+1}=d'_{i+1}+d''_{i+1},\qquad
u_{i+1}=u'_{i+1}+u''_{i+1}.
\]
""",
    r"""Prenons alors $Q_{i+1}=Q'_{i+1}\times Q''_{i+1}$,
qui appartient à $\boldsymbol{K}''$ en vertu de (iii), et
$d_{i+1}=d'_{i+1}+d''_{i+1}$, $u_{i+1}=u'_{i+1}+u''_{i+1}$.
""",
    "Missing words 'qui appartient à K'' en vertu de (iii), et' (K'' bold italic); the print sets the formulas in "
    "the running text.")
add(48, "proof of (11.9.1): 'Comme d_{i+1}(Q_{i+1}) = d'_{i+1}(Q_{i+1}) = N_i⊂Z_i(Q.)'",
    "d'_{i+1}(Q_{i+1}) (no prime on Q)", "d'_{i+1}(Q'_{i+1})", "formula", None, "high",
    r"=d'_{i+1}(Q'_{i+1})=N_i", r"=d'_{i+1}(Q_{i+1})=N_i",
    "The print applies d'_{i+1} to Q_{i+1}, in the sense of d_{i+1} = d'_{i+1} + d''_{i+1} (d'_{i+1} composed with the "
    "projection); the TeX's Q'_{i+1} is an editorial change. If the corrected edition treats the print as a misprint, "
    "its reading is d'_{i+1}(Q'_{i+1}).")
add(48, "proof of (11.9.1): 'on a d_{i+1}∘d_i = 0 et, avec les notations usuelles'", "d_{i+1}∘d_i = 0",
    "d_i\\circ d_{i+1}=0", "misprint_in_print", None, "high",
    r"$d_i\circ d_{i+1}=0$ et, avec", r"$d_{i+1}\circ d_i=0$ et, avec",
    "Misprint: d_{i+1}∘d_i is not composable (d_i : Q_i→Q_{i-1}, d_{i+1} : Q_{i+1}→Q_i); the hypothesis d_{j-1}∘d_j = 0 "
    "for j = i+1 gives d_i∘d_{i+1} = 0. The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"$d_i\circ d_{i+1}=0$")
add(48, "proof of (11.9.1): 'le morphisme H_i(Q.) = Z_i(Q.)/N_i→H_i(P.) déduit du système'", "in the running text",
    "displayed", "other", None, "high",
    r"""morphisme
\[
H_i(Q_\bullet)=Z_i(Q_\bullet)/N_i\longrightarrow H_i(P_\bullet)
\]
""",
    r"""morphisme
$H_i(Q_\bullet)=Z_i(Q_\bullet)/N_i\to H_i(P_\bullet)$
""", "Layout only (display vs inline); the formula matches.")
add(48, "proof of (11.9.1): 'le morphisme v_{i+1} : Z_{i+1}(Q.)→Z_{i+1}(P.)→H_{i+1}(P.) est un épimorphisme'",
    "in the running text", "displayed", "other", None, "high",
    r"""le morphisme
\[
v_{i+1}:Z_{i+1}(Q_\bullet)\longrightarrow Z_{i+1}(P_\bullet)
\longrightarrow H_{i+1}(P_\bullet)
\]
""",
    r"""le morphisme
$v_{i+1}:Z_{i+1}(Q_\bullet)\to Z_{i+1}(P_\bullet)
\to H_{i+1}(P_\bullet)$
""", "Layout only (display vs inline); the formula matches.")
add(48, "proof of (11.9.2): 'en prenant pour C la catégorie ..., pour K' (resp. K'') l'ensemble'",
    "bold italic C, K', K''", "\\mathcal C, plain K', K''", "font", None, "high",
    r"""pour $\mathcal C$ la
catégorie des $A$-modules à droite, pour $K'$ (resp. $K''$) l'ensemble des""",
    r"""pour $\boldsymbol{C}$ la
catégorie des $A$-modules à droite, pour $\boldsymbol{K}'$ (resp. $\boldsymbol{K}''$) l'ensemble des""", KB)
add(48, "Remarques (11.9.3) (i): 'des A-modules à droite plats'", "'plats' italic", "upright",
    "italics", None, "high", "à droite plats. Alors", r"à droite \emph{plats}. Alors", "")
add(48, "Remarques (11.9.3) (i): 'l'homomorphisme de complexes u⊗1 : Q.⊗_A M→P.⊗_A M définit'", "in the running text",
    "displayed", "other", None, "high",
    r"""l'homomorphisme de complexes
\[
u\otimes 1:Q_\bullet\otimes_A M\longrightarrow P_\bullet\otimes_A M
\]
""",
    r"""l'homomorphisme de complexes
$u\otimes 1:Q_\bullet\otimes_A M\to P_\bullet\otimes_A M$
""", "Layout only (display vs inline); the formula matches.")
add(48, "Remarques (11.9.3) (i): 'définit encore un isomorphisme'", "'isomorphisme' italic", "upright",
    "italics", None, "high", "définit encore un isomorphisme\n", "définit encore un \\emph{isomorphisme}\n", "")
add(48, "Remarques (11.9.3) (i): 'H.(Q.⊗_A M) ⥲ H.(P.⊗_A M)'", "isomorphism arrow (arrow with a tilde above)", "\\simeq",
    "convention", 4, "high", r"(Q_\bullet\otimes_A M)\simeq", r"(Q_\bullet\otimes_A M)\xrightarrow{\sim}", "")
add(48, "Remarques (11.9.3) (ii): 'lorsqu'on ne suppose pas A noethérien;'", "'noethérien' italic", "upright",
    "italics", None, "high", "ne suppose pas $A$ noethérien;", r"ne suppose pas $A$ \emph{noethérien};", "")
add(48, "Remarques (11.9.3) (ii): 'admet une résolution par des modules libres'", "'résolution' italic", "upright",
    "italics", None, "high", "admet une résolution", r"admet une \emph{résolution}", "")
add(48, "(11.10.1): 'un complexe de A-modules à gauche de longueur finie.'",
    "'complexe' and 'longueur finie' italic", "upright", "italics", None, "high",
    "un complexe de $A$-modules à gauche de longueur finie. On appelle",
    r"un \emph{complexe} de $A$-modules à gauche de \emph{longueur finie}. On appelle", "")
add(48, "(11.10.1.1): 'M· : 0→M^0→M^1→...→M^n→0'", "baseline dots (...)", "\\cdots",
    "symbol", None, "high", r"\longrightarrow\cdots\longrightarrow", r"\longrightarrow\ldots\longrightarrow", "")

# ---------------- page 49 ----------------
add(49, "(11.10.1.2): 'χ(M·) = Σ_{i=0}^{n} (—1)^i long M^i.'", "long M^i (no parentheses)", "\\operatorname{long}(M^i)",
    "formula", None, "high", r"(-1)^i\operatorname{long}(M^i).", r"(-1)^i\operatorname{long}M^i.", "")
add(49, "Proposition (11.10.2), whole statement", "italic; 'χ(M·) = χ(H·(M·))' in the running text",
    "\\emph{...} inside the italic proposition environment (upright); the formula displayed",
    "convention", 6, "high",
    r"""\emph{Pour tout complexe fini $M^\bullet$ de $A$-modules à gauche de longueur
finie, on a
\[
\chi(M^\bullet)=\chi(H^\bullet(M^\bullet))
\]
($H^\bullet(M^\bullet)$ étant considéré comme un complexe pour la dérivation
triviale). En particulier, si la suite
(\hyperref[0.11.10.1.1-fr]{11.10.1.1}) est exacte, on a
$\chi(M^\bullet)=0$.}""",
    r"""Pour tout complexe fini $M^\bullet$ de $A$-modules à gauche de longueur
finie, on a $\chi(M^\bullet)=\chi(H^\bullet(M^\bullet))$
($H^\bullet(M^\bullet)$ étant considéré comme un complexe pour la dérivation
triviale). En particulier, si la suite
(\hyperref[0.11.10.1.1-fr]{11.10.1.1}) est exacte, on a
$\chi(M^\bullet)=0$.""",
    C6 + " The edit also sets χ(M·) = χ(H·(M·)) inline, as printed.")
add(49, "proof of (11.10.2): the exact sequences 0→B^i→Z^i→H^i→0 / 0→Z^i→M^i→B^{i+1}→0",
    "two lines, no punctuation", "one display line, a comma and \\qquad between them", "punctuation", None, "high",
    "\\longrightarrow0,\n\\qquad\n0\\longrightarrow Z^i",
    "\\longrightarrow0\n\\]\n\\[\n0\\longrightarrow Z^i",
    "Extra comma; the print stacks the two sequences.")
add(49, "proof of (11.10.2): relations 'long(Z^i) = long(H^i)+long(B^i)' / 'long(M^i) = long(Z^i)+long(B^{i+1})'",
    "two lines, no commas", "one display line, a comma after each relation", "punctuation", None, "high",
    r"""\operatorname{long}(B^i),
\qquad
\operatorname{long}(M^i)=\operatorname{long}(Z^i)+
\operatorname{long}(B^{i+1}),
\]""",
    r"""\operatorname{long}(B^i)
\]
\[
\operatorname{long}(M^i)=\operatorname{long}(Z^i)+
\operatorname{long}(B^{i+1})
\]""",
    "Two extra commas; the print stacks the two relations.")
add(49, "proof of (11.10.2): 'long(M^i)—long(H^i) = long(B^{i+1})+long(B^i)' (after 'd'où')", "no final period",
    "final period", "punctuation", None, "high",
    r"""\operatorname{long}(B^{i+1})+\operatorname{long}(B^i).
\]""",
    r"""\operatorname{long}(B^{i+1})+\operatorname{long}(B^i)
\]""", "")
add(49, "proof of (11.10.2): 'pour 0⩽i⩽n; en notant que B^0 = B^{n+1} = 0'", "semicolon after n", "comma",
    "punctuation", None, "high", r"pour $0\leq i\leq n$, en notant que", r"pour $0\leq i\leq n$; en notant que", "")
add(49, "Corollaire (11.10.3): 'les caractéristiques d'Euler-Poincaré χ(E_r^{(·)}) de tous les complexes E_r^{(·)} = (E_r^{(n)})_{n∈Z}'",
    "superscript (·) with parentheses", "E_r^\\bullet", "formula", None, "high",
    r"""$\chi(E_r^\bullet)$ de tous les complexes
$E_r^\bullet=(E_r^{(n)})_{n\in\mathbb Z}$""",
    r"""$\chi(E_r^{(\bullet)})$ de tous les complexes
$E_r^{(\bullet)}=(E_r^{(n)})_{n\in\mathbb Z}$""",
    "The print writes the complexes E_r^{(·)}, E_2^{(·)}, E_∞^{(·)} with the dot in parentheses (10 times on this page).")
add(49, "Corollaire (11.10.3): 'si on pose E_∞^{(n)} = ⊕_{p+q=n} E_∞^{pq} pour tout n∈Z, on a aussi'",
    "inline, followed by 'pour tout n∈Z,'", "displayed, followed by '\\quad(n\\in\\mathbb Z),'", "word", None, "high",
    r"""et si on pose
\[
E_\infty^{(n)}=\bigoplus_{p+q=n}E_\infty^{pq}\quad(n\in\mathbb Z),
\]
""",
    r"""et si on pose
$E_\infty^{(n)}=\bigoplus_{p+q=n}E_\infty^{pq}$ pour tout $n\in\mathbb Z$,
""",
    "The print has the words 'pour tout n∈Z' where the TeX has '(n∈Z)'; the formula is in the running text.")
add(49, "Corollaire (11.10.3): 'on a aussi χ(E_∞^{(·)}) = χ(E_2^{(·)}), E_∞^{(·)} = (E_∞^{(n)})_{n∈Z}'",
    "superscript (·)", "^\\bullet", "formula", None, "high",
    r"""on a aussi $\chi(E_\infty^\bullet)=\chi(E_2^\bullet)$,
$E_\infty^\bullet=(E_\infty^{(n)})""",
    r"""on a aussi $\chi(E_\infty^{(\bullet)})=\chi(E_2^{(\bullet)})$,
$E_\infty^{(\bullet)}=(E_\infty^{(n)})""", "")
add(49, "proof of (11.10.3): 'on a E_r^{pq} = 0 pour 2⩽r⩽+∞'", "2⩽r⩽+∞", "2\\leq r<+\\infty",
    "symbol", None, "high", r"$2\leq r<+\infty$", r"$2\leq r\leq+\infty$",
    "The print includes r = +∞ (E_∞^{pq} is a subquotient of E_2^{pq}).")
add(49, "proof of (11.10.3): 'donc tous les complexes E_r^{(·)} sont finis'", "E_r^{(·)}", "E_r^\\bullet",
    "formula", None, "high", r"complexes $E_r^\bullet$ sont finis", r"complexes $E_r^{(\bullet)}$ sont finis", "")
add(49, "proof of (11.10.3): 'la relation χ(E_r^{(·)}) = χ(E_{r+1}^{(·)}) pour tout r fini'", "(·) twice", "^\\bullet twice",
    "formula", None, "high", r"$\chi(E_r^\bullet)=\chi(E_{r+1}^\bullet)$ pour tout",
    r"$\chi(E_r^{(\bullet)})=\chi(E_{r+1}^{(\bullet)})$ pour tout", "")
add(49, "proof of (11.10.3): 'l'isomorphie entre H·(E_r^{(·)}) et E_{r+1}^{(·)}'", "(·) twice (H· itself without parentheses)",
    "^\\bullet", "formula", None, "high", r"$H^\bullet(E_r^\bullet)$ et $E_{r+1}^\bullet$",
    r"$H^\bullet(E_r^{(\bullet)})$ et $E_{r+1}^{(\bullet)}$", "")
add(49, "proof of (11.10.3): 'les suites (B_k(E_2^{pq}))_{k⩾2} et (Z_k(E_2^{pq})_{k⩾2} sont stationnaires'",
    "(Z_k(E_2^{pq})_{k⩾2}: one closing parenthesis missing", "(Z_k(E_2^{pq}))_{k\\geq2}", "misprint_in_print", None,
    "high", r"$(Z_k(E_2^{pq}))_{k\geq2}$", r"$(Z_k(E_2^{pq})_{k\geq2}$",
    "Misprint: unbalanced parenthesis (compare (B_k(E_2^{pq}))_{k⩾2} just before). The TeX silently corrects it; the fix "
    "restores the printed reading.", corrected=r"$(Z_k(E_2^{pq}))_{k\geq2}$")
add(49, "proof of (11.10.3): 'd'où l'assertion relative à χ(E_∞^{(·)})'", "E_∞^{(·)}", "E_\\infty^\\bullet",
    "formula", None, "high", r"relative à $\chi(E_\infty^\bullet)$.", r"relative à $\chi(E_\infty^{(\bullet)})$.", "")
add(49, "(12.1.1): 'on définit la cohomologie H·(X, ℱ)'", "'cohomologie' italic", "upright",
    "italics", None, "high", "on définit la cohomologie", r"on définit la \emph{cohomologie}", "")
add(49, "(12.1.1): 'qui est un foncteur cohomologique universel (T, 2.2)'", "'foncteur cohomologique universel' italic",
    "upright", "italics", None, "high", "qui est un foncteur cohomologique universel",
    r"qui est un \emph{foncteur cohomologique universel}", "")
add(49, "(12.1.1): 'de la catégorie C(X) des O_X-Modules'", "bold italic C", "plain $C(X)$",
    "font", None, "high", r"la catégorie $C(X)$ des", r"la catégorie $\boldsymbol{C}(X)$ des",
    "Bold italic category letter C, as in (11.9.1).")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(F), "findings written")
