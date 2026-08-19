# Problem Set 05 - Causality, Fairness, and Production Monitoring

**Weight:** 3%  
**Work mode:** Individual  
**Suggested time:** 45-60 minutes  
**AI level:** Yellow - assistance permitted with disclosure

## Case

BrightReach evaluates a marketing campaign using observational data. Treated
customers had an average purchase increase of $18; untreated customers had an
increase of $7. After adjustment, the estimated average treatment effect is
$6.20 with a 95% confidence interval of [$1.10, $11.30]. Twenty-two percent of
treated customers have propensity scores above the maximum observed among
untreated customers.

A targeting model has these validation results:

| Group | Selection rate | True-positive rate | False-positive rate |
|---|---:|---:|---:|
| A | 0.31 | 0.76 | 0.18 |
| B | 0.18 | 0.61 | 0.09 |

After launch, overall AUC remains stable, but the positive-class rate rises from
12% to 21%, calibration error doubles, and customer complaints increase.

## Questions

### 1. Separate association from effect - 0.35 points

Why is the unadjusted $11 difference not automatically the campaign's causal
effect?

### 2. Interpret the adjusted estimate - 0.40 points

Give a statistically careful interpretation of the adjusted effect and its
confidence interval.

### 3. Diagnose overlap - 0.40 points

What does the propensity-score fact imply? State one defensible response.

### 4. State an identification assumption - 0.35 points

Name and explain one assumption needed to interpret the adjusted estimate
causally.

### 5. Describe the fairness evidence - 0.40 points

Identify two group differences in the table. Why does the table alone not tell
you which fairness policy is appropriate?

### 6. Propose a fairness response - 0.35 points

Give one diagnostic and one possible mitigation, including a tradeoff that must
be reviewed.

### 7. Diagnose production drift - 0.35 points

Why is stable AUC insufficient reassurance after launch? Cite two other signals
from the case.

### 8. Write an escalation recommendation - 0.40 points

In 100-150 words, recommend whether to continue, restrict, recalibrate, or pause
the system. Include one causal limitation, one fairness concern, and two
monitoring or governance actions.

## Submission

Enter all eight numbered responses directly in Blackboard and include the
required Yellow-level AI-use disclosure (or the course's no-AI statement).
