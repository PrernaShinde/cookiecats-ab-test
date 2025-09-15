🍪 Cookie Cats A/B Test — Gate Placement Experiment
🌟 Overview

This project analyzes an A/B test from the Cookie Cats mobile game. Developers wanted to test whether moving the first “gate” from level 30 → level 40 improved player engagement.

The analysis covers experiment design, guardrail vs primary metrics, statistical testing (two-proportion z-test, Wilson CIs), absolute/relative lift, and a final ship/no-ship decision.

Built in Python with pandas, statsmodels, and matplotlib, this project demonstrates how to run and interpret an end-to-end A/B test like a real product analyst or data scientist.

✨ Key Features

📊 Experiment Design: Clear primary vs guardrail metrics (Day-7 vs Day-1 retention)
🧮 Statistical Testing: Two-proportion z-test, p-values, Wilson confidence intervals
📈 Effect Size: Absolute lift (pp) and relative lift (%) to quantify impact
🖼️ Visualizations: Retention by group with error bars (CIs)
⚡ Power / MDE Estimation: What effect size can we detect with this sample size?
🛂 Decision Framework: Data → insight → product recommendation

🚀 Quick Start
Prerequisites

Python 3.9+

pip package manager

Installation
# Clone repo
git clone https://github.com/PrernaShinde/cookiecats-ab-test.git
cd cookiecats-ab-test

# Install dependencies
pip install -r requirements.txt

Data Setup

Download the dataset from Kaggle:
👉 Cookie Cats A/B Test Dataset

Place cookie_cats.csv in the /data folder.

data/
├── README.md
└── cookie_cats.csv   # put dataset here

Run the Analysis
jupyter lab
# open notebooks/analysis.ipynb and run all cells


Figures will be saved to results/figures/.

📊 Results Summary
Metric	A (gate 30)	B (gate 40)	Abs lift (pp)	Rel lift (%)	p-value	Interpretation
Day-1 retention (guardrail)	44.82%	44.23%	–0.59	–1.32%	0.0744	No significant change
Day-7 retention (primary)	19.02%	18.20%	–0.82	–4.31%	0.0016	Significant drop
Visuals

Day-1 Retention:


Day-7 Retention:


🧮 Concepts Demonstrated

A/B Testing Framework: Control (A) vs Treatment (B)

Hypothesis Testing: Null (no difference) vs Alternative (difference)

Primary vs Guardrail Metrics: Long-term engagement vs short-term onboarding

Absolute vs Relative Lift: Real impact (pp) and proportional change (%)

Statistical Significance: Two-proportion z-test, p-values, confidence intervals

Decision Making: Translating statistical results into a product recommendation

🛂 Decision & Recommendation

Primary metric worsened (Day-7 retention –0.82 pp, significant).

Guardrail unaffected (Day-1 retention stable).

Decision: ❌ Do not ship gate_40. Keeping the gate at level 30 retains more players long-term.

📂 Project Structure
cookiecats-ab-test/
├── notebooks/
│   └── analysis.ipynb      # Full analysis with explanations
├── src/
│   ├── metrics.py          # Z-test, Wilson CI, MDE functions
│   └── viz.py              # Visualization helpers
├── data/
│   └── README.md           # Instructions to download cookie_cats.csv
├── results/
│   └── figures/            # Saved bar charts
├── requirements.txt        # Dependencies
├── LICENSE
└── README.md

🧪 Testing / Validation

Sanity checks: Confirmed A/B split, schema, mapping.

Statistical robustness: Used Wilson CIs (better than Wald), p-values cross-checked.

Z-score for Day-7 ≈ 3.1 → matches low p-value (0.0016).

📚 Data Source

Dataset: Cookie Cats A/B Test on Kaggle

All rights reserved to original creators.

Used here for educational purposes only.

📄 License

This project’s code is licensed under the MIT License — see LICENSE
.
Dataset remains under the original creators’ terms on Kaggle.