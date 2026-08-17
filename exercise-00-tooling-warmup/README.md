# Exercise 00 — First Flight: GitHub + Google Colab

[![Open starter notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/exercise-00-tooling-warmup/notebooks/tooling_warmup.ipynb)

**When:** Before Session 1  
**Expected effort:** 45–60 minutes  
**Work mode:** Individual, ungraded completion check

## Purpose

This is a tooling rehearsal, not a machine-learning task. You will practice the exact workflow used by later challenges:

1. Fork a GitHub repository.
2. Open and execute a notebook in Google Colab.
3. Load a CSV with pandas.
4. Complete a small calculation and export a submission file.
5. Run an automated validator.
6. Save the notebook to your GitHub fork.
7. Commit your output on a branch and open a pull request in your fork.

## Toy problem

Northstar Coffee wants a simple weekly customer-priority list. For each customer, calculate:

- `conversion_rate = orders / visits`, using `0` when visits are zero;
- `average_order_value = revenue_usd / orders`, using `0` when orders are zero;
- `priority_customer = 1` when orders are at least 3 **and** revenue is at least $150, otherwise `0`.

No model is needed. The goal is to prove your tools and file workflow work.

## Before opening Colab

1. Sign in to GitHub.
2. Open the [course repository](https://github.com/lathrahul/modern-ai-ml-exercises).
3. Select **Fork**, keep the default repository name, and create the fork under your account.
4. Return here and use the Colab badge above.

## Required output

Create `toy_submission.csv` with exactly:

```text
customer_id,conversion_rate,average_order_value,priority_customer
TOY-001,0.25,40.00,0
```

Run the validator in Colab or locally:

```bash
python checks/validate_submission.py toy_submission.csv
```

## GitHub completion evidence

In Colab, use **File → Save a copy in GitHub** and select your fork. Save the notebook to a branch named `tooling-warmup`. Upload `toy_submission.csv` to the same branch through GitHub, then open a pull request from `tooling-warmup` into your fork’s `main` branch.

Submit the URL of that pull request. Do not open a pull request against the instructor’s course repository.

## Completion checklist

- [ ] Notebook runs from top to bottom.
- [ ] Validator prints `Valid tooling submission`.
- [ ] Notebook and CSV exist on the `tooling-warmup` branch of your fork.
- [ ] Pull request targets your own fork’s `main` branch.
- [ ] Pull request description contains one sentence explaining what you learned.
