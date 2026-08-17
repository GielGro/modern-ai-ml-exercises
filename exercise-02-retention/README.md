# Exercise 02 — Save or Let Go: Customer Retention Decisions

[![Open starter in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/exercise-02-retention/notebooks/getting_started.ipynb) [![Explore outputs in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/shared/explore_outputs_in_colab.ipynb)

**Release:** End of Session 4  
**Due:** During Session 6 debrief  
**Expected effort:** 5–7 hours  
**Work mode:** Individual

## Your role

You are a data scientist supporting the retention team at Meridian Telecom. The team can contact only a fraction of customers. Every contact costs money, accepted offers reduce margin, and contacting customers who would stay anyway wastes budget.

Build a model that estimates each customer's churn probability, then translate those probabilities into a contact decision. The goal is not merely to identify churners—it is to create a defensible retention policy.

## Business questions

1. Who is most likely to churn?
2. At what probability threshold should the team intervene?
3. What is the estimated financial value of the policy?
4. How sensitive is the decision to uncertain campaign assumptions?

## Data

- `data/train.csv`: customer attributes and observed `churned` outcome.
- `data/test.csv`: customers requiring probabilities and decisions.
- `data/campaign_costs.csv`: supplied decision assumptions.
- `data/data_dictionary.md`: field definitions.
- `sample_submission.csv`: required schema.

The data derive from IBM's fictional telecom sample and have been prepared specifically for the course.

## Required analysis

1. Audit prevalence, missingness, and the unit of analysis.
2. Establish an always-stay baseline.
3. Use stratified cross-validation or justify a stronger alternative.
4. Fit and compare:
   - logistic regression;
   - L1-regularized logistic regression;
   - one decision tree or Random Forest after Session 6.
5. Report ROC-AUC, PR-AUC, log loss, and at least one confusion matrix.
6. Calculate expected campaign value over a range of thresholds using the supplied assumptions.
7. Select one threshold and perform a sensitivity analysis.
8. Generate a probability and contact decision for every test customer.

Do not use boosting, neural networks, external customer data, or reconstructed public labels.

## Expected outputs

### 1. Decision file

`submission.csv` with exactly:

```text
customer_id,churn_probability,contact_customer
CUST-123456,0.73,1
```

`contact_customer` must be `0` or `1`. Validate with:

```bash
python checks/validate_submission.py submission.csv
```

### 2. Executed notebook and experiment summary

Show preprocessing, cross-validation, model comparison, probability evaluation, threshold economics, sensitivity analysis, and final decision generation.

### 3. One-page retention memo

Write for the VP of Customer Retention. Recommend a policy, expected contacts per 10,000 customers, expected value under the supplied assumptions, key churn signals, sensitivity risks, and one fairness or customer-experience concern.

### 4. Three-minute methodology presentation

Explain the validation design, model selection, threshold, and one limitation. Do not narrate notebook cells.

## Leaderboard score

The technical component uses **log loss**, rewarding useful probabilities rather than only rankings. The decision component evaluates realized campaign value using the submitted `contact_customer` policy and hidden outcomes. Public results use 40% of test rows; the remaining 60% determine the final private score.

## Data source

IBM Telco Customer Churn sample: https://github.com/IBM/telco-customer-churn-on-icp4d
