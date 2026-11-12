"""Print repr of the first and last characters of page_NNN.tex files (LF-normalised)."""
import pathlib
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
for p in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    t = (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    print(p, "HEAD", repr(t[:120]))
    print(p, "TAIL", repr(t[-120:]))
    print(p, "Cohen--Macaulay:", t.count("Cohen--Macaulay"), " Cohen-Macaulay:", t.count("Cohen-Macaulay"))
