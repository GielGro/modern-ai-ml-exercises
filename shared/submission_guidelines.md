# Submission guidelines

Submit one ZIP named `lastname_exercise##_submission.zip` containing:

1. A fully executed notebook with visible outputs.
2. The challenge-specific `submission.csv`.
3. A one-page PDF business memo.
4. The AI-use disclosure in the notebook.

Before submitting, restart the runtime and run all cells. Use relative paths only. The notebook must complete in under 10 minutes on a standard Google Colab CPU runtime.

Submissions are rejected automatically when IDs are missing or duplicated, columns do not match the published schema, predictions are missing, or probabilities fall outside `[0, 1]`.

Before submitting, open the [shared Colab output explorer](OUTPUT_EXPLORER.md), upload the primary CSV, and investigate any implausible distribution, action rate, segment size, class count, or confidence interval. The explorer does not reveal hidden labels and does not replace the challenge validator.
