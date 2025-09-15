# 🍪 Cookie Cats A/B Test

A statistical analysis of an A/B test from the Cookie Cats mobile game.  
The experiment tested whether moving the first “gate” from level 30 → 40 improved long-term player retention.

---

## 📊 Project Overview
- **Goal**: Evaluate the impact of gate placement on player retention
- **Groups**:
  - Group A (**Control**): gate at level 30
  - Group B (**Treatment**): gate at level 40
- **Primary metric**: Day-7 retention (long-term engagement)
- **Guardrail metric**: Day-1 retention (onboarding health)
- **Statistical methods**:
  - Two-proportion z-test (for differences in proportions)
  - Wilson 95% Confidence Intervals (better than Wald method)
  - Absolute & relative lift (effect sizes)
  - MDE / sample size estimation (statistical power)
- **Stack**: Python · pandas · statsmodels · matplotlib

---

## ✨ Key Learnings
This project demonstrates how to run and interpret an A/B test like a data scientist:
- Designing experiments with **primary vs guardrail metrics**
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

### 2. Install dependencies
```bash
pip install -r requirements.txt
