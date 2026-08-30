# Exercise 00 — First Flight: Week 1 GitHub + Google Colab Lab

[![Open starter notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/exercise-00-tooling-warmup/notebooks/tooling_warmup.ipynb)

**When:** Launched during Week 1; complete before Week 2
**Expected effort:** 25–35 guided minutes in class, plus up to 30 minutes afterward
**Work mode:** Individual, ungraded completion check

## Purpose

This is a guided Week 1 tooling rehearsal, not a machine-learning task. The instructor will introduce the repository and demonstrate the opening steps during class. You will then practice the exact workflow used by later challenges:

1. Fork a GitHub repository.
2. Open and execute a notebook in Google Colab.
3. Load a CSV with pandas.
4. Complete a small calculation and export a submission file.
5. Run an automated validator.
6. Save a working copy in Google Drive, then download the completed notebook and CSV.
7. Upload both files to a branch in your GitHub fork and open a pull request in your fork.

## Toy problem

Northstar Coffee wants a simple weekly customer-priority list. For each customer, calculate:

- `conversion_rate = orders / visits`, using `0` when visits are zero;
- `average_order_value = revenue_usd / orders`, using `0` when orders are zero;
- `priority_customer = 1` when orders are at least 3 **and** revenue is at least $150, otherwise `0`.

No model is needed. The goal is to prove your tools and file workflow work.

## Start during Week 1

1. Follow the instructor's demonstration to sign in to GitHub and open the [course repository](https://github.com/lathrahul/modern-ai-ml-exercises).
2. Select **Fork**, keep the default repository name, and create the fork under your account.
3. Return here and use the Colab badge above.
4. Work with a partner when troubleshooting, but preserve and submit your own notebook, CSV, and pull-request URL.

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

## Preserve and submit your work

Colab may show **Save a copy in Drive** and **Save a copy as a GitHub Gist** without offering a direct repository save. Do **not** use a Gist for this exercise.

1. While working, select **File → Save a copy in Drive** so your notebook is not lost when the temporary runtime ends.
2. After the validator passes, select **File → Download → Download .ipynb**. Rename the file `tooling_warmup.ipynb` if Colab adds `Copy of` to the filename.
3. Run the notebook download cell to download `toy_submission.csv`.
4. In your GitHub fork, create a branch named `tooling-warmup` from `main`.
5. On that branch, upload `tooling_warmup.ipynb` to `exercise-00-tooling-warmup/notebooks/`.
6. Upload `toy_submission.csv` to `exercise-00-tooling-warmup/`.
7. Open a pull request from `tooling-warmup` into the `main` branch of **your own fork**.

Submit the URL of that pull request in Blackboard before Week 2. Do not open a pull request against the instructor’s course repository.

## Completion checklist

- [ ] Notebook runs from top to bottom.
- [ ] Validator prints `Valid tooling submission`.
- [ ] Completed notebook exists at `exercise-00-tooling-warmup/notebooks/tooling_warmup.ipynb` on the `tooling-warmup` branch of your fork.
- [ ] `toy_submission.csv` exists at `exercise-00-tooling-warmup/toy_submission.csv` on the same branch.
- [ ] Pull request targets your own fork’s `main` branch.
- [ ] Pull request description contains one sentence explaining what you learned.
