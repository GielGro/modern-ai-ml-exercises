# Week 1 Micro-Lab — Familiar Customers vs New Customers

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/shared/notebooks/customer_split_micro_lab.ipynb)

This 8–10 minute activity asks students to choose the validation test that matches a retailer’s real decision: estimating next-month spending for newly acquired customers.

Students should:

1. Notice that the data contains repeated visits for the same customer.
2. Predict the difference between a “familiar customer” test and a “new customer” test.
3. Run one collapsed comparison cell and interpret a simple results table and chart.
4. Preserve one sentence explaining which test supports the business claim.

The activity deliberately distinguishes two ideas:

- **Validation-design mismatch:** training and validation contain the same customer identities even though deployment concerns new customers.
- **Future-information leakage:** a feature contains information unavailable at the prediction moment.

No file submission is required. The notebook supports the Week 1 discussion of generalization and credible evaluation.
