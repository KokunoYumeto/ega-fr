"""Detect printed-page = pdf-page + k for a Numdam scan by reading the page numbers in the text layer.
usage: python scan_offset.py PDF [PDF ...]"""
import collections
import re
import subprocess
import sys

for pdf in sys.argv[1:]:
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    votes = collections.Counter()
    for p in range(10, pages - 5, max(1, pages // 12)):
        t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-enc", "UTF-8", pdf, "-"], capture_output=True, text=True, encoding="utf-8").stdout
        nums = [int(x) for x in re.findall(r"^\s*(\d{1,3})\s*$", t, re.M)]
        for n in nums:
            if abs(n - p) < 40:
                votes[n - p] += 1
    print(pdf.rsplit("/", 1)[-1], "pages", pages, "offset votes", votes.most_common(3))
