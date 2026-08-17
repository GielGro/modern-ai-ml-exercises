# Causal Campaign data dictionary

Each row is one customer in an observational campaign cohort.

| Field | Meaning |
|---|---|
| `customer_id` | Random course identifier |
| `recency` | Months since last purchase |
| `prior_spend_band` | Historical-spend category |
| `prior_spend_usd` | Historical customer spend |
| `mens`, `womens` | Prior category-purchase indicators |
| `geography` | Rural, suburban, or urban grouping |
| `newbie` | New-customer indicator |
| `channel` | Prior purchase channel |
| `treatment` | 1 = women’s email, 0 = no email |
| `visited` | Website visit during outcome window |
| `converted` | Purchase during outcome window |
| `spend_usd` | Spend during outcome window |

`visited`, `converted`, and `spend_usd` are post-treatment outcomes and must never enter a propensity model.
