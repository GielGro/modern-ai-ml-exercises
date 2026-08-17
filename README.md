# Modern AI & Machine Learning — Applied Challenges

Two individual, business-facing machine-learning exercises for the opening six sessions of the course. Each challenge is designed for 5–7 hours of student work over a 7–10 day window.

| Exercise | Course sessions | Core question | Primary method |
|---|---:|---|---|
| [HomeValue](exercise-01-homevalue/) | 1–3 | What is a defensible screening value for a home? | Linear regression |
| [Save or Let Go](exercise-02-retention/) | 4–6 | Which customers should receive a retention offer? | Classification and thresholding |

## Submission principles

- Start with a simple baseline and improve it deliberately.
- Use a pipeline so preprocessing learned from training data is not leaked into validation.
- Evaluate the model in technical and business terms.
- Submit reproducible work: Restart the runtime and run all cells before submission.
- Disclose use of generative AI using [the course template](shared/ai_use_disclosure.md).

The test labels and instructor solutions are intentionally absent from this repository.

## Environment

Google Colab is recommended. For local use, install the packages in `requirements.txt` with Python 3.10 or later.

## Data provenance

- Exercise 1 derives from the Ames Housing data made available by Dean De Cock and the Ames City Assessor's Office: https://cmustatistics.github.io/data-repository/money/ames-housing.html
- Exercise 2 derives from IBM's fictional Telco Customer Churn sample: https://github.com/IBM/telco-customer-churn-on-icp4d

Both exercise datasets use randomized identifiers and course-specific preparation. Do not attempt to reconstruct labels from online copies.
