# Exercise 03 — BookingGuard: Protecting Hotel Revenue

**Release:** Session 7  
**Due:** Before Session 8 debrief  
**Expected effort:** 5–7 hours  
**Work mode:** Individual

## Your role

You support revenue management for a hotel group. Late cancellations leave rooms empty, but requiring a deposit from every guest creates friction and reduces bookings. At a fixed decision point before arrival, predict cancellation risk and recommend which bookings should require a deposit.

## Business questions

1. Which bookings are most likely to cancel?
2. Does gradient boosting materially improve on logistic regression and Random Forest?
3. Which probability threshold produces the strongest expected policy value?
4. Where does the policy fail across hotel, market, and customer groups?

## Data

- `data/train.csv`: arrivals before July 2017, including `canceled`.
- `data/test.csv`: July–August 2017 arrivals without labels.
- `data/policy_costs.csv`: published decision assumptions.
- `data/data_dictionary.md`: prediction-time field definitions.
- `sample_submission.csv`: required schema.

The holdout is later in time. Random cross-validation alone may overstate performance when demand patterns shift.

## Required analysis

1. Define the prediction moment and audit leakage.
2. Establish prevalence and logistic-regression baselines.
3. Use a time-aware validation design.
4. Compare logistic regression, Random Forest, and one gradient-boosting implementation.
5. Track at least five deliberate experiments, including parameters, validation period, runtime, and metrics. W&B is recommended; a documented experiment table is acceptable.
6. Evaluate log loss, PR-AUC, ROC-AUC, calibration, and policy value.
7. Select a deposit threshold and test its sensitivity to all supplied cost assumptions.
8. Analyze error or policy rates across at least three operational groups.

Do not use reservation status, post-arrival information, external labels, or reconstructed source outcomes.

## Expected outputs

### Prediction and policy file

```text
booking_id,cancellation_probability,require_deposit
BOOK-123456,0.71,1
```

Validate it with:

```bash
python checks/validate_submission.py submission.csv
```

### Notebook and experiment report

Provide an executed, reproducible notebook plus a W&B report link or equivalent experiment table.

### Revenue-management memo

In one page, recommend a threshold, expected deposits per 1,000 bookings, expected value, evidence of temporal generalization, important drivers, and two guest-experience guardrails.

## Leaderboard

The predictive component uses log loss. The policy component applies the published economics to hidden outcomes. Public scoring uses 40% of holdout bookings; 60% remain private until the deadline.

## Source

Hotel Booking Demand datasets by António, de Almeida, and Nunes, CC BY 4.0: https://doi.org/10.1016/j.dib.2018.11.126
