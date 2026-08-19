# Problem Set 04 - Segmentation, PCA, and Neural-Network Evidence

**Weight:** 3%  
**Work mode:** Individual  
**Suggested time:** 45-60 minutes  
**AI level:** Yellow - assistance permitted with disclosure

## Case

MetroMart is exploring customer segments and an image classifier for product
routing. For segmentation, standardized purchase features produce:

| Clusters (k) | Silhouette score | Minimum cluster size |
|---:|---:|---:|
| 2 | 0.39 | 1,840 |
| 3 | 0.46 | 620 |
| 5 | 0.49 | 42 |
| 8 | 0.41 | 11 |

PCA explains 44%, 23%, 11%, 7%, and 4% of variance in the first five
components. A neural-network experiment reports:

| Model | Training accuracy | Validation accuracy | Validation log loss |
|---|---:|---:|---:|
| Small network | 0.86 | 0.82 | 0.48 |
| Large network | 0.99 | 0.79 | 0.71 |
| Transfer learning | 0.93 | 0.88 | 0.34 |

## Questions

### 1. Select a segmentation candidate - 0.40 points

Choose a value of k for initial business review and justify it using both
silhouette score and cluster size.

### 2. Explain why the maximum is not automatic - 0.35 points

Why should MetroMart not select k=5 solely because it has the highest
silhouette score?

### 3. Test segment usefulness - 0.40 points

Give two checks that would establish whether the segments are stable and
actionable rather than merely mathematically separated.

### 4. Interpret PCA coverage - 0.35 points

How much variance do the first three components explain? What information is
lost if the analysis retains only those components?

### 5. Avoid a PCA interpretation error - 0.30 points

Why is a principal component not automatically a customer persona or causal
business factor?

### 6. Diagnose neural-network fit - 0.40 points

Compare the small and large networks. Which shows stronger evidence of
overfitting, and why?

### 7. Evaluate transfer learning - 0.40 points

Which model has the strongest current validation evidence? Cite at least two
metrics and name one additional check before deployment.

### 8. Recommend next steps - 0.40 points

In 100-150 words, recommend one segmentation follow-up and one image-model
follow-up, each with a success criterion.

## Submission

Enter all eight numbered responses directly in Blackboard and include the
required Yellow-level AI-use disclosure (or the course's no-AI statement).
