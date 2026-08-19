# Problem Set 03 - Trees, Ensembles, and Honest Model Selection

**Weight:** 3%  
**Work mode:** Individual  
**Suggested time:** 45-60 minutes  
**AI level:** Yellow - assistance permitted with disclosure

## Case

StayWell predicts hotel-booking cancellations. An analyst compares four models.
The final test set must be used once, after model selection.

| Model | Cross-validation AUC (mean ± SD) | Test AUC | Inference time per 1,000 cases |
|---|---:|---:|---:|
| Logistic regression | 0.781 ± 0.012 | 0.779 | 8 ms |
| Decision tree | 0.744 ± 0.041 | 0.731 | 5 ms |
| Random forest | 0.824 ± 0.010 | 0.819 | 62 ms |
| Gradient boosting | 0.832 ± 0.009 | 0.826 | 21 ms |

The analyst tuned 60 configurations, repeatedly checked test AUC, selected the
largest test value, and reported it as an unbiased estimate. The strongest
boosting model also uses `days_before_cancellation`, a field populated only
after a cancellation occurs.

## Questions

### 1. Identify leakage - 0.40 points

Explain why `days_before_cancellation` cannot be used and connect the problem to
the prediction moment.

### 2. Diagnose test-set misuse - 0.40 points

Why is repeatedly checking the test set during tuning a methodological error?

### 3. Propose an honest workflow - 0.45 points

Describe a valid train/validation/test or nested-cross-validation workflow for
selecting and estimating the performance of these models.

### 4. Compare tree stability - 0.35 points

What does the decision tree's cross-validation standard deviation suggest when
compared with the ensemble models?

### 5. Select a deployment candidate - 0.45 points

Assuming leakage is removed and performance remains similar, choose a model and
justify it using predictive quality, variability, and inference time.

### 6. Explain ensemble improvement - 0.30 points

Briefly explain how random forests or gradient boosting can improve on a single
decision tree.

### 7. Design an ablation - 0.30 points

Describe one comparison that would reveal whether the model benefits from a
feature family rather than from leakage or chance.

### 8. Communicate uncertainty - 0.35 points

In 100-150 words, explain to an operations manager what can and cannot be
concluded from the table before deployment.

## Submission

Enter all eight numbered responses directly in Blackboard and include the
required Yellow-level AI-use disclosure (or the course's no-AI statement).
