# Problem Set 02 - Classification Decisions and Regularization

**Weight:** 3%  
**Work mode:** Individual  
**Suggested time:** 45-60 minutes  
**AI level:** Yellow - assistance permitted with disclosure

## Case

HarborBank uses a classifier to identify customers who may miss their next loan
payment. A flagged customer receives a support call. Each call costs $12. An
unflagged customer who misses a payment creates an estimated $180 loss. The
validation set contains 1,000 customers, including 100 who miss a payment.

| Threshold | Precision | Recall | Flagged customers | Missed positive cases |
|---:|---:|---:|---:|---:|
| 0.30 | 0.32 | 0.88 | 275 | 12 |
| 0.50 | 0.50 | 0.70 | 140 | 30 |
| 0.70 | 0.68 | 0.41 | 60 | 59 |

Two logistic-regression models were fit on the same training data:

| Model | Training AUC | Validation AUC | Number of nonzero coefficients |
|---|---:|---:|---:|
| Weak regularization | 0.91 | 0.74 | 84 |
| Stronger regularization | 0.82 | 0.79 | 26 |

## Questions

### 1. Define the prediction decision - 0.35 points

State the unit of analysis, target, prediction moment, and operational action.

### 2. Compute expected operating cost - 0.55 points

For each threshold, calculate `12 × flagged customers + 180 × missed positive
cases`. Show your work and identify the lowest-cost threshold.

### 3. Explain the threshold tradeoff - 0.35 points

Why does raising the threshold generally increase precision while decreasing
recall? Explain in business terms, not only metric definitions.

### 4. Recommend a threshold - 0.45 points

Recommend a threshold using the calculated cost and one nonfinancial
consideration such as customer experience, staffing capacity, or fairness.

### 5. Diagnose regularization - 0.40 points

Which logistic-regression model currently has stronger generalization evidence?
Use both the AUC values and coefficient counts.

### 6. Evaluate accuracy - 0.25 points

If a model predicts every customer will pay, what is its accuracy? Why is that
number inadequate for this decision?

### 7. Check subgroup performance - 0.30 points

Suppose recall at threshold 0.50 is 0.78 for long-tenure customers and 0.46 for
new customers. Give one diagnostic and one possible operating response.

### 8. Final recommendation - 0.35 points

In 100-150 words, recommend a model-and-threshold policy and describe one
monitoring metric that should be reviewed after launch.

## Submission

Enter all eight numbered responses directly in Blackboard. Include this final
statement:

- If AI was used: name the system, purpose, prompts or prompt log, how output
  was used, and how you verified it.
- If AI was not used: `No generative AI tools were used in preparing this submission.`
