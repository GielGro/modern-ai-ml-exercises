# Segment Studio data dictionary

Each row is one customer with at least two completed purchase invoices.

| Field | Meaning |
|---|---|
| `customer_id` | Random course identifier |
| `recency_days` | Days from final observation date to most recent purchase |
| `purchase_frequency` | Distinct completed purchase invoices |
| `monetary_value` | Gross completed-purchase value in GBP |
| `product_diversity` | Distinct products purchased |
| `units_purchased` | Units across completed purchases |
| `active_days` | Distinct calendar days with purchases |
| `country` | Modal purchase country |
| `average_basket_value` | Mean completed invoice value in GBP |
| `return_line_rate` | Share of observed transaction lines marked as returns/cancellations |

Extreme values may be valid wholesalers. Investigate before winsorizing or removing them.
