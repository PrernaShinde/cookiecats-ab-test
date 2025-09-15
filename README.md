# 🍪 Cookie Cats A/B Test

A statistical analysis of an A/B test from the Cookie Cats mobile game.  
The experiment tested whether moving the first “gate” from level 30 → 40 improved long-term player retention.

---

## 📊 Project Overview
- **Goal**: Test impact of gate placement on player retention  
- **Groups**:  
  - Group A → Gate at level 30 (Control)  
  - Group B → Gate at level 40 (Treatment)  
- **Primary metric**: Day-7 retention  
- **Guardrail metric**: Day-1 retention  
- **Statistical tests**:  
  - Two-proportion z-test  
  - Wilson confidence intervals  
  - Absolute & relative lift  

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

Place the file in the /data folder:

bash
Copy code
data/
  ├── README.md
  └── cookie_cats.csv   # <- place here
4. Run analysis
Open Jupyter Notebook:

bash
Copy code
jupyter notebook notebooks/analysis.ipynb
📈 Results Summary
Metric	A (Gate 30)	B (Gate 40)	Abs lift (pp)	Rel lift (%)	p-value	Interpretation
Day-1 retention	44.82%	44.23%	–0.59	–1.32%	0.0744	No significant change
Day-7 retention ⭐	19.02%	18.20%	–0.82	–4.31%	0.0016	Significant drop

📌 Decision: ❌ Do not move the gate. Day-7 retention significantly worsens.

📊 Visuals
Day-1 retention


Day-7 retention


🎓 Concepts Demonstrated
Experiment design (primary vs guardrail metrics)

Two-proportion z-test for A/B testing

Wilson confidence intervals

Absolute & relative lift interpretation

Practical decision-making (ship / don’t ship)

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

yaml
Copy code

4. Save the file (**Cmd+S** / **Ctrl+S**).  

---

### 🌀 Push it to GitHub
Back in your terminal (inside the repo folder):

```bash
git add README.md
git commit -m "Improve README structure with overview, results, visuals"
git push origin main