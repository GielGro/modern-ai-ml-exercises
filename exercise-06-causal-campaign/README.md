# Exercise 06 — Causal Campaign: Did the Email Create Incremental Value?

**Release:** Session 14  
**Due:** One week after Session 14  
**Expected effort:** 5–7 hours  
**Work mode:** Individual

## Your role

The growth team observed that customers receiving a women’s-merchandise email converted at a different rate than customers receiving no email. However, the supplied operational cohort is observational and imbalanced. Decide whether the email caused incremental visits, conversions, and spend—and whether the evidence supports rollout.

## Data

`data/marketing_observational.csv` contains customer history, treatment, and two-week outcomes. `treatment=1` means the women’s email; `0` means no email. The course team retains a randomized benchmark for post-deadline evaluation.

## Required analysis

1. State the estimand, unit, treatment, outcomes, and target population.
2. Draw a DAG before modeling and justify the adjustment set.
3. Report the naive difference in means.
4. Audit overlap and covariate balance using standardized mean differences.
5. Estimate propensity scores without using post-treatment variables.
6. Estimate effects using matching or weighting and one outcome-regression/doubly robust method.
7. Quantify uncertainty with confidence intervals.
8. Conduct at least one refutation, placebo, trimming, or sensitivity analysis.
9. Use SHAP only for an explicitly defined predictive or heterogeneous-effect model; do not present SHAP as proof of causality.
10. Discuss fairness, targeting ethics, and how a future randomized test should be designed.

## Expected outputs

### `effect_estimates.csv`

One final row for each required outcome:

```text
outcome,estimator,ate,ci_low,ci_high
converted,aipw,0.012,0.004,0.020
visited,aipw,0.031,0.020,0.042
spend_usd,aipw,0.85,0.10,1.60
```

Use `sample_effect_estimates.csv` as the schema and replace every placeholder.

Validate with:

```bash
python checks/validate_effects.py effect_estimates.csv
```

### Decision memo

Write two pages for the Chief Growth Officer: recommendation, effect sizes with uncertainty, assumptions, balance/overlap evidence, sensitivity result, responsible-targeting guardrails, and next experiment.

## Evaluation

The hidden randomized benchmark is a diagnostic, not an answer key. Estimates are graded primarily on causal reasoning, diagnostics, uncertainty, and decision quality.

## Source

Kevin Hillstrom’s MineThatData Email Analytics Challenge: https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html
