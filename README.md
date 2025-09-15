# 🍪 Cookie Cats A/B Test

A statistical analysis of an A/B test from the Cookie Cats mobile game.  
The experiment tested whether moving the first “gate” from level 30 → 40 improved long-term player retention.

---

## 📊 Project Overview

- **Goal:** Evaluate the impact of gate placement on player retention  
- **Groups:**  
  - **Group A (Control):** gate at level 30  
  - **Group B (Treatment):** gate at level 40  
- **Primary metric:** Day-7 retention (long-term engagement)  
- **Guardrail metric:** Day-1 retention (onboarding health)  
- **Statistical methods:**  
  - Two-proportion **z-test** (for differences in proportions)  
  - **Wilson 95% Confidence Intervals** (better than Wald method)  
  - **Absolute & relative lift** (effect sizes)  
  - **MDE / Sample size estimation** (statistical power)  
- **Stack:** Python · pandas · statsmodels · matplotlib  

---

## ✨ Key Learnings

This project demonstrates how to run and interpret an A/B test like a data scientist:  
- Designing experiments with **primary** vs **guardrail** metrics  
- Running a **two-proportion z-test** to compare groups  
- Computing **confidence intervals** for retention rates  
- Interpreting **absolute & relative lift**  
- Using results to make a **ship / don’t ship decision**  

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/PrernaShinde/cookiecats-ab-test.git
cd cookiecats-ab-test
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Data setup
Download dataset from Kaggle:
👉 Cookie Cats Dataset

Place the file into /data:

arduino
Copy code
data/
├── README.md         # explains dataset source
└── cookie_cats.csv   # downloaded from Kaggle
4. Run the analysis
Open Jupyter Notebook:

bash
Copy code
jupyter notebook notebooks/analysis.ipynb
Figures will be saved automatically to results/figures/.

📈 Results
Metric	A (Gate 30)	B (Gate 40)	Abs lift (pp)	Rel lift (%)	p-value	Interpretation
Day-1 retention (guardrail)	44.82%	44.23%	–0.59	–1.32%	0.0744	Not statistically significant
Day-7 retention (primary)	19.02%	18.20%	–0.82	–4.31%	0.0016	Significant drop

Decision: ❌ Do not ship the change. Moving the gate to level 40 harms long-term retention.

🖼️ Visuals
Day-1 Retention (Guardrail)


Day-7 Retention (Primary)


🧠 Concepts Covered
Experiment design: Choosing meaningful metrics

Statistical testing: Two-proportion z-test

Confidence intervals: Wilson method for retention rates

Effect size: Absolute vs relative lift

Business decision-making: Translating results into product strategy

🗂️ Project Structure
bash
Copy code
cookiecats-ab-test/
├── data/
│   └── README.md            # dataset source (Kaggle)
├── notebooks/
│   └── analysis.ipynb       # full analysis notebook
├── results/
│   └── figures/             # generated plots
├── src/
│   ├── metrics.py           # z-test, Wilson CI, MDE helpers
│   └── viz.py               # visualization utilities
├── requirements.txt         # Python dependencies
├── LICENSE
└── README.md
📚 Data & License
Dataset: Cookie Cats A/B Test on Kaggle

Code License: MIT License – see LICENSE

👤 Author
Prerna Shinde
🔗 GitHub: PrernaShinde

