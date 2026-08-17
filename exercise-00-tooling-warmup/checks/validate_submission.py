from pathlib import Path
import sys
import numpy as np
import pandas as pd

EXPECTED_COLUMNS = ["customer_id", "conversion_rate", "average_order_value", "priority_customer"]


def validate(path: Path) -> None:
    source = pd.read_csv(Path(__file__).parents[1] / "data/customer_activity.csv")
    submission = pd.read_csv(path)
    assert submission.columns.tolist() == EXPECTED_COLUMNS, f"Expected columns {EXPECTED_COLUMNS}"
    assert submission.customer_id.is_unique, "customer_id values must be unique"
    assert set(submission.customer_id) == set(source.customer_id), "IDs must exactly match the source data"
    merged = source.merge(submission, on="customer_id", validate="one_to_one")
    expected_conversion = np.divide(merged.orders, merged.visits, out=np.zeros(len(merged), dtype=float), where=merged.visits.ne(0))
    expected_aov = np.divide(merged.revenue_usd, merged.orders, out=np.zeros(len(merged), dtype=float), where=merged.orders.ne(0))
    expected_priority = ((merged.orders >= 3) & (merged.revenue_usd >= 150)).astype(int)
    assert np.allclose(merged.conversion_rate, expected_conversion, atol=1e-6), "conversion_rate calculation is incorrect"
    assert np.allclose(merged.average_order_value, expected_aov, atol=0.01), "average_order_value calculation is incorrect"
    assert np.array_equal(merged.priority_customer.astype(int), expected_priority), "priority_customer rule is incorrect"
    print(f"Valid tooling submission: {len(submission)} customers")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "toy_submission.csv"))
