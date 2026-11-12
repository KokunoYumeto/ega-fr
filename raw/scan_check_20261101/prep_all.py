"""Prepare page pairs (TeX + 300-dpi strips) for every remaining EGA volume, using page_inventory.json for the files
of each part and an explicit scan and offset per volume (pdf page = printed page + offset)."""
import json
import pathlib
import subprocess
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
L = pathlib.Path(r"user\Documents\Free or receipted\free\lesson-sources\numdam")
SRC = E / "ega-fr" / "source"
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
R20 = E / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages"
JOBS = [  # (run folder, marker part, scan, offset, first, last, files or None for all files of the part)
    ("run_I_b", "I", L / "PMIHES_1960__4__5_0.pdf", -1, 130, 214, None),
    ("run_I_intro", "I", L / "PMIHES_1960__4__5_0.pdf", -1, 5, 9, None),
    ("run_0I", "0\\textsubscript{I}", L / "PMIHES_1960__4__5_0.pdf", -1, 11, 78, None),
    ("run_II", "II", L / "PMIHES_1961__8__5_0.pdf", -3, 5, 222, None),
    ("run_0III", "0\\textsubscript{III}", L / "PMIHES_1961__11__5_0.pdf", -3, 5, 80, None),
    ("run_III1", "III", L / "PMIHES_1961__11__5_0.pdf", -3, 81, 167, [str(R20 / "BASE/native/ega3/ega3-1-fr.tex")]),
    ("run_III2", "III", L / "PMIHES_1963__17__5_0.pdf", -133, 137, 223, [str(R20 / "BASE/native/ega3/ega3-6-fr.tex"), str(R20 / "BASE/native/ega3/ega3-7-fr.tex")]),
    ("run_0IV1", "0\\textsubscript{IV-1}", L / "PMIHES_1964__20__5_0.pdf", -1, 5, 221, None),
    ("run_IV1", "IV-1", L / "PMIHES_1964__20__5_0.pdf", -1, 222, 259, None),
    ("run_IV2", "IV-2", E / "scans" / "PMIHES_1965__24__5_0.pdf", -3, 5, 231, None),
    ("run_IV3", "IV-3", L / "PMIHES_1966__28__5_0.pdf", -1, 5, 255, None),
    ("run_IV4", "IV-4", L / "PMIHES_1967__32__5_0.pdf", -1, 5, 361, None),
    ("run_IVback", "IV", L / "PMIHES_1967__32__5_0.pdf", -1, 333, 361, None),
]
only = set(sys.argv[1:])
for run, part, scan, off, first, last, files in JOBS:
    if only and run not in only:
        continue
    key = part.replace("\\textsubscript{", "_").replace("}", "")
    if files is None:
        files = inv[key]["files"]
    args = [sys.executable, "-I", str(E / "prep_batch.py"), part, str(scan), str(off), str(first), str(last), str(E / run)] + [str(f) for f in files]
    r = subprocess.run(args, capture_output=True, text=True)
    print(run, (r.stdout or r.stderr).strip()[-300:], flush=True)
