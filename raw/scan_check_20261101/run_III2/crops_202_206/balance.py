import re, os
D = r"user\Documents\ega_scan_check_20261101\run_III2\crops_202_206"

def metrics(s):
    s2 = re.sub(r"\\[{}$]", "", s)          # drop escaped braces/dollars
    s2 = re.sub(r"(?<!\\)%.*", "", s2)      # drop comments
    dollars = s2.count("$")
    braces = s2.count("{") - s2.count("}")
    disp = s2.count("\\[") - s2.count("\\]")
    envs = len(re.findall(r"\\begin\{", s2)) - len(re.findall(r"\\end\{", s2))
    # dollars per paragraph must be even
    odd = [i for i, para in enumerate(re.split(r"\n\s*\n", s2)) if para.count("$") % 2]
    return dollars, braces, disp, envs, odd

for p in range(202, 207):
    o = open(os.path.join(D, f"orig_{p}.tex"), encoding="utf-8").read()
    n = open(os.path.join(D, f"patched_page_{p}.tex"), encoding="utf-8").read()
    print(p, "orig", metrics(o), "patched", metrics(n))
