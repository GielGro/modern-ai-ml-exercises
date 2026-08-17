# Exercise 04 — Segment Studio: From Transactions to Customer Strategy

**Release:** Session 9  
**Due:** Session 10 insight presentations  
**Expected effort:** 5–7 hours  
**Work mode:** Teams of two

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
python checks/validate_segments.py segments.csv
```

### `segment_profiles.csv`

One row per segment with size, percentage, medians for core behavioral features, proposed name, recommended action, and risk/caveat.

### Segment memo and presentation

Provide a two-page CMO memo and a three-minute presentation. Include the selected `k`, validation evidence, a two-dimensional visualization, profiles, actions, limitations, and reproducibility notes.

## Evaluation

There is no hidden “true cluster.” Grading rewards defensible preparation, stability, distinctiveness, and the quality of business decisions—not maximization of a single internal metric.

## Source

UCI Online Retail dataset by Daqing Chen, CC BY 4.0: https://doi.org/10.24432/C5BW33
