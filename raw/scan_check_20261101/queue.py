"""Queue of EGA scan-check batches (5 printed pages each) for the remaining runs.

python -I queue.py init      build QUEUE.json from the prepared run folders (pages with a page_NNN.tex)
python -I queue.py next N    print the next N pending batches as launch specs and mark them launched
python -I queue.py done RUN FIRST LAST   mark a batch done (its findings file exists)
python -I queue.py status    counts per run
"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
Q = E / "QUEUE.json"
RUNS = [  # run folder, marker part, description for the prompt, apply_fixes PART, release files restriction
    ("run_0I", "0\\textsubscript{I}", "EGA I, chapter 0: markers \\oldpage[0\\textsubscript{I}]{N}"),
    ("run_II", "II", "EGA II: markers \\oldpage[II]{N}"),
    ("run_0III", "0\\textsubscript{III}", "EGA III, part 1, chapter 0: markers \\oldpage[0\\textsubscript{III}]{N}"),
    ("run_III1", "III", "EGA III, part 1 (Publ. IHES 11): markers \\oldpage[III]{N}"),
    ("run_III2", "III", "EGA III, part 2 (Publ. IHES 17): markers \\oldpage[III]{N}; pages 137-167 also exist in part 1, use only this run's page_NNN.tex"),
    ("run_0IV1", "0\\textsubscript{IV-1}", "EGA IV, part 1, chapter 0: markers \\oldpage[0\\textsubscript{IV-1}]{N}"),
    ("run_IV1", "IV-1", "EGA IV, part 1: markers \\oldpage[IV-1]{N}"),
    ("run_IV2", "IV-2", "EGA IV, part 2: markers \\oldpage[IV-2]{N}"),
    ("run_IV3", "IV-3", "EGA IV, part 3: markers \\oldpage[IV-3]{N}"),
    ("run_IV4", "IV-4", "EGA IV, part 4: markers \\oldpage[IV-4]{N}"),
    ("run_IVback", "IV", "EGA IV, part 4, end matter: markers \\oldpage[IV]{N}"),
]


def init():
    batches = []
    for run, part, desc in RUNS:
        pages = sorted(int(m.group(1)) for p in (E / run).glob("page_*.tex")
                       if (m := re.fullmatch(r"page_(\d+)\.tex", p.name)))
        for i in range(0, len(pages), 5):
            chunk = pages[i:i + 5]
            out = E / run / f"findings_{chunk[0]:03d}_{chunk[-1]:03d}.json"
            batches.append(dict(run=run, part=part, desc=desc, pages=chunk, outfile=str(out),
                                state="done" if out.exists() else "pending"))
    old = json.loads(Q.read_text(encoding="utf-8")) if Q.exists() else []
    launched = {(b["run"], b["pages"][0]) for b in old if b["state"] in ("launched", "done", "applied")}
    for b in batches:
        if (b["run"], b["pages"][0]) in launched and b["state"] == "pending":
            b["state"] = "launched"
    Q.write_text(json.dumps(batches, indent=1, ensure_ascii=False), encoding="utf-8")
    status()


def save(batches):
    Q.write_text(json.dumps(batches, indent=1, ensure_ascii=False), encoding="utf-8")


def nxt(n):
    batches = json.loads(Q.read_text(encoding="utf-8"))
    k = 0
    for b in batches:
        if b["state"] == "pending" and k < n:
            b["state"] = "launched"
            k += 1
            pages = ", ".join(map(str, b["pages"]))
            print(f"{b['run']}|{b['pages'][0]:03d}_{b['pages'][-1]:03d}|{pages}|{b['desc']}|{b['outfile']}")
    save(batches)


def mark(run, first, last, state):
    batches = json.loads(Q.read_text(encoding="utf-8"))
    for b in batches:
        if b["run"] == run and b["pages"][0] == first and b["pages"][-1] == last:
            b["state"] = state
    save(batches)


def status():
    batches = json.loads(Q.read_text(encoding="utf-8"))
    by = {}
    for b in batches:
        by.setdefault(b["run"], {}).setdefault(b["state"], 0)
        by[b["run"]][b["state"]] += 1
    for run, c in by.items():
        print(run, c)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "init":
        init()
    elif cmd == "next":
        nxt(int(sys.argv[2]))
    elif cmd in ("done", "launched", "applied", "pending"):
        mark(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), cmd)
    elif cmd == "status":
        status()
