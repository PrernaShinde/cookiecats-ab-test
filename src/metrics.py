import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

def sanity_checks(df: pd.DataFrame):
    cols = {"userid","version","sum_gamerounds","retention_1","retention_7"}
    assert cols.issubset(df.columns), f"Missing columns. Need: {cols}"
    out = df.copy()
    out.columns = [c.lower() for c in out.columns]
    out["group"] = out["version"].map({"gate_30":"A","gate_40":"B"})
    assert out["group"].isin(["A","B"]).all(), "Unexpected values in version/group"
    split = out["group"].value_counts(normalize=True)
    return out, split

def rate_ci(success, total, alpha=0.05, method="wilson"):
    rate = success / total
    lo, hi = proportion_confint(success, total, alpha=alpha, method=method)
    return rate, lo, hi

def ab_summary(df: pd.DataFrame, flag: str):
    g = df.groupby("group")[flag].agg(["sum","count"])
    a_s, a_n = int(g.loc["A","sum"]), int(g.loc["A","count"])
    b_s, b_n = int(g.loc["B","sum"]), int(g.loc["B","count"])

    a_rate, a_lo, a_hi = rate_ci(a_s, a_n)
    b_rate, b_lo, b_hi = rate_ci(b_s, b_n)

    z, p = proportions_ztest([b_s, a_s], [b_n, a_n], alternative="two-sided")
    abs_lift = b_rate - a_rate
    rel_lift = abs_lift / a_rate if a_rate>0 else np.nan

    return {
        "A_success": a_s, "A_total": a_n, "A_rate": a_rate, "A_CI": (a_lo,a_hi),
        "B_success": b_s, "B_total": b_n, "B_rate": b_rate, "B_CI": (b_lo,b_hi),
        "abs_lift_pp": 100*abs_lift,
        "rel_lift_%": 100*rel_lift,
        "z": float(z), "p": float(p)
    }

def mde_or_sample(power=0.8, alpha=0.05, p_baseline=0.25, n=None, mde=None):
    from statistics import NormalDist
    z_alpha = NormalDist().inv_cdf(1 - alpha/2)
    z_beta  = NormalDist().inv_cdf(power)

    if n is not None:
        p1 = p_baseline
        return {"n_per_group": n,
                "mde_abs": float((z_alpha + z_beta)*np.sqrt(2*p1*(1-p1)/n))}
    if mde is not None:
        p1 = p_baseline; p2 = p1 + mde
        pbar = (p1+p2)/2; qbar = 1-pbar
        num = (z_alpha*np.sqrt(2*pbar*qbar) + z_beta*np.sqrt(p1*(1-p1)+p2*(1-p2)))**2
        n_req = np.ceil(2 * num / (p2-p1)**2)
        return {"mde_abs": mde, "n_per_group": int(n_req)}
    raise ValueError("Provide either n or mde.")
