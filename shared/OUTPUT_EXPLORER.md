# Explore challenge outputs in Google Colab

[![Open output explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/shared/explore_outputs_in_colab.ipynb)

The shared output explorer supports all six exercises without exposing hidden labels. It validates the uploaded file’s schema, joins public context when useful, and creates exercise-specific summaries and charts.

## How to use it

1. Open the Colab badge above.
2. Select the exercise from the dropdown in the configuration cell.
3. Choose whether to use the public sample output or upload your own CSV.
4. Select **Runtime → Run all**.
5. When prompted, upload the output produced by your exercise notebook.

The explorer does **not** calculate private leaderboard metrics. It helps answer questions such as:

- Are predictions distributed sensibly?
- What share of customers or bookings receive an action?
- Are segment sizes and profiles operationally plausible?
- Which image labels dominate the predictions?
- Do causal confidence intervals cross zero?

Run the challenge-specific validator before submission; the explorer complements rather than replaces it.
