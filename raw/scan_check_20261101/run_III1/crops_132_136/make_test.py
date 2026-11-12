"""Assemble a compile test of the patched pages 131 (from Remarque (4.3.4)) to 136 with the stub preamble."""
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
NAT = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native"
C = E / "run_III1/crops_132_136"
stub = (NAT / "stub_ega1-2-fr.tex").read_text(encoding="utf-8")
pre = stub[: stub.index("\\begin{document}")]
pre = pre.replace("\\input{preamble-base.tex}", "\\input{" + (NAT / "preamble-base.tex").as_posix() + "}")
body = []
for p in range(131, 137):
    t = (C / f"patched_{p}.tex").read_text(encoding="utf-8").split("\n", 1)[1]
    if p == 131:
        t = t[t.index("\\begin{remark}[4.3.4]"):]
    body.append(t)
(C / "test_132_136.tex").write_text(pre + "\\begin{document}\n" + "".join(body) + "\n\\end{document}\n", encoding="utf-8")
print("ok")
