import matplotlib.pyplot as plt
import numpy as np
import os

def bar_with_ci(groups, rates, cis, title, ylabel, outpath):
    plt.figure()
    x = np.arange(len(groups))
    y = np.array(rates)
    lo = np.array([r - c[0] for r,c in zip(rates, cis)])
    hi = np.array([c[1] - r for r,c in zip(rates, cis)])
    plt.bar(x, y, yerr=[lo,hi], capsize=6)
    plt.xticks(x, groups)
    plt.title(title)
    plt.ylabel(ylabel)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    plt.savefig(outpath, bbox_inches="tight")
    plt.close()
