# Submission guidelines

Submit one ZIP named `lastname_exercise##_submission.zip` for individual work or `teamname_exercise##_submission.zip` for team work. Include:

1. A fully executed notebook with visible outputs.
2. Every challenge-specific CSV or model artifact required by the exercise brief.
3. The memo, model card, experiment table, or presentation file required by the exercise brief.
4. The AI-use disclosure in the notebook.

Before submitting, restart the runtime and run all cells. Use relative paths only. Follow the exercise brief for runtime or hardware limits; document any required GPU runtime.

Submissions are rejected automatically when IDs are missing or duplicated, columns do not match the published schema, predictions are missing, or probabilities fall outside `[0, 1]`.

Before submitting, open the [shared Colab output explorer](OUTPUT_EXPLORER.md), upload the primary CSV, and investigate any implausible distribution, action rate, segment size, class count, or confidence interval. The explorer does not reveal instructor-held labels and does not replace the challenge validator.

Blackboard is the source of truth for the submission field, designated team submitter, due date, and any exercise-specific exceptions.
