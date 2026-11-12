import json
import pathlib

D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
t = (D / "crops_090_094" / "simulated_ega4-9.tex").read_text(encoding="utf-8")
out = []
for key in ["il résulte de (6.2.1) que l'on", "pour tout $x'\\in V$, on ait", "Spec}(\\boldsymbol", "on en conclut que l'on a",
            "(resp.\n$x_0\\in X_0$) tels que", "\\label{IV.9.9.4-fr}", "(i.e.", "\\item[\\textup{(ix)}]",
            "relatives à", "posons $F="]:
    i = t.find(key)
    out.append(f"==== {key!r} at {i}\n" + t[i - 20:i + 420] + "\n")
d = json.load(open(D / "findings_090_094.json", encoding="utf-8"))
out.append(f"findings: {len(d)}; first where: {d[0]['where']}\n")
(D / "crops_090_094" / "excerpts.txt").write_text("".join(out), encoding="utf-8")
