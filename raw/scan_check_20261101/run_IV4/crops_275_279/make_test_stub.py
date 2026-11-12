"""Write two compile stubs into this folder: the IV-4 preamble plus (a) the replayed ega4-21b with these
findings applied, (b) the current unmodified ega4-21b. Nothing outside this folder is written."""
import pathlib

D = pathlib.Path(__file__).resolve().parent
NAT = (D.parent.parent / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "IV4" / "native")
pre = (NAT / "ega4" / "EGA_IV4_FR.tex").read_text(encoding="utf-8")
pre = pre[:pre.index("\\begin{document}")]
pre = pre.replace("\\input{preamble-base}", "\\input{" + (NAT / "preamble-base").as_posix() + "}")
body = ("\\begin{document}\n\\newcommand{\\shHom}{\\mathcal{H}\\!om}\n\\setcounter{section}{20}\n"
        "\\input{%s}\n\\end{document}\n")
(D / "stub_replay.tex").write_text(pre + body % (D / "replay_ega4-21b.tex").as_posix(), encoding="utf-8")
(D / "stub_orig.tex").write_text(pre + body % (NAT / "ega4" / "ega4-21b-fr.tex").as_posix(), encoding="utf-8")
print("ok")
