# Retention data dictionary

Each row represents one fictional telecom customer observed at a decision point.

| Field | Type | Meaning |
|---|---|---|
| `customer_id` | identifier | Random course identifier; not predictive |
| `gender` | category | Recorded gender in source data |
| `senior_citizen` | binary | Senior-citizen indicator |
| `has_partner` | binary category | Partner indicator |
| `has_dependents` | binary category | Dependents indicator |
| `tenure_months` | integer | Months with the company |
| `phone_service` | binary category | Phone service indicator |
| `multiple_lines` | category | Multiple-line status |
| `internet_service` | category | DSL, fiber optic, or none |
| `online_security` | category | Online-security service status |
| `online_backup` | category | Online-backup service status |
| `device_protection` | category | Device-protection service status |
| `tech_support` | category | Technical-support service status |
| `streaming_tv` | category | Streaming-TV service status |
| `streaming_movies` | category | Streaming-movie service status |
| `contract` | category | Month-to-month, one-year, or two-year contract |
| `paperless_billing` | binary category | Paperless billing indicator |
| `payment_method` | category | Customer payment method |
| `monthly_charges` | numeric USD | Current monthly charges |
| `total_charges` | numeric USD | Cumulative charges; may be missing for new customers |
| `churned` | binary target | `1` if the customer churned, otherwise `0`; training only |

The source represents a fictional company. Demographic fields should be audited for disparate error rates; inclusion in a predictive model is not automatically an ethical or legal justification for use.
