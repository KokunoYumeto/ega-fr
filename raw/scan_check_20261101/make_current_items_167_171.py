"""Corrected-edition counterparts of two combined misprint+layout fixes of run_III2/findings_167_171.json (entries 13 and
46): the layout part applies to the corrected edition, the misprint part does not (it keeps the correct reading)."""
import json
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
d = json.loads((E / "run_III2" / "findings_167_171.json").read_text(encoding="utf-8"))
f13, f46 = d[13], d[46]
assert f13["kind"] == f46["kind"] == "misprint_in_print"
n13 = f13["fix"]["new"].replace("q_1+\\ldots q_m", "q_1+\\ldots+q_m")
assert n13 != f13["fix"]["new"]
n46 = f46["fix"]["new"]
assert n46.count("f_m:\n") == 1
n46 = n46.replace("f_m:\n", "f_m;\n")
items = [
    dict(file="ega3-6-fr.tex", part="III", page=167, region="page", kind="symbol", old=f13["fix"]["old"], new=n13,
         why="baseline dots of the print (findings_167_171 #13 without its misprint part: the corrected edition keeps '+')"),
    dict(file="ega3-6-fr.tex", part="III", page=168, region="page", kind="formula", old=f46["fix"]["old"], new=n46,
         why="formula set inline as in the print (findings_167_171 #46 with ';', the correct reading, for the printed ':')"),
]
out = E / "CURRENT_ITEMS_III2_167_171.json"
out.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", out)
