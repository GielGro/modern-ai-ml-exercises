# Exercise 04 — Segment Studio: From Transactions to Customer Strategy

[![Open starter in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/exercise-04-segment-studio/notebooks/getting_started.ipynb) [![Explore outputs in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/shared/explore_outputs_in_colab.ipynb)

**Release:** Session 9  
**Due:** Session 10 insight presentations  
**Expected effort:** 5–7 hours  
**Work mode:** Teams of two

## Start and submit

1. Open the starter notebook with the Colab button above and select **File → Save a copy in Drive**. Do not use a GitHub Gist.
2. Complete the analysis, restart the runtime, and run every cell from top to bottom.
3. Validate `segments.csv` and inspect the outputs with the [shared output explorer](../shared/OUTPUT_EXPLORER.md).
4. Download the executed notebook and required outputs to your computer.
5. Assemble the files using the [submission guidelines](../shared/submission_guidelines.md) and submit them through the Exercise 04 assignment in Blackboard. Follow the Blackboard assignment for the designated team submitter and due date.

## Your role

The CMO of a UK online retailer believes its customers need different lifecycle strategies, but does not want arbitrary personas. Create a compact, stable segmentation from behavioral customer profiles and translate it into decisions for marketing, service, and merchandising.

## Data

`data/customers.csv` contains course-prepared customer-level features derived from 541,909 transaction lines. There is no correct label and no conventional leaderboard.

## Required analysis

1. Audit skew, outliers, scale, and the meaning of missingness.
2. Choose transformations and justify them.
3. Compare K-means across a meaningful range of `k` using silhouette, stability, and business usefulness.
4. Compare against hierarchical clustering or DBSCAN on an appropriate sample.
5. Apply PCA and interpret the first two components; use UMAP only as a visual exploration aid.
6. Name each final segment from evidence, not stereotypes.
7. Recommend one differentiated action and one “do not do” warning per segment.
8. Identify unusual customers that should be reviewed separately rather than forced into a persona.

## Expected outputs

### `segments.csv`

```text
customer_id,segment_id
SHOP-123456,2
```

Use integer segment IDs from 0 through `k-1`. Validate with:

```bash
python3 checks/validate_segments.py segments.csv
```

### `segment_profiles.csv`

One row per segment with size, percentage, medians for core behavioral features, proposed name, recommended action, and risk/caveat.
Use `segment_profiles_template.csv` as the schema.

### Segment memo and presentation

Provide a two-page CMO memo and a three-minute presentation. Include the selected `k`, validation evidence, a two-dimensional visualization, profiles, actions, limitations, and reproducibility notes.

## Evaluation

There is no hidden “true cluster.” Grading rewards defensible preparation, stability, distinctiveness, and the quality of business decisions—not maximization of a single internal metric.

## Source

[UCI Online Retail dataset](https://doi.org/10.24432/C5BW33) by Daqing Chen, CC BY 4.0.
