import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 2.4), dpi=150)
for i, fs in enumerate(["stix", "dejavuserif", "cm"]):
    matplotlib.rcParams["mathtext.fontset"] = fs
    fig.text(0.02, 0.75 - 0.33 * i, fs + r": N=$\mathfrak{N}$  R=$\mathfrak{R}$  F/N: $F_{\delta,n}/\mathfrak{N}$  F/R: $F_{\delta,n}/\mathfrak{R}$", fontsize=22)
fig.savefig("frak_NR_ref.png")
