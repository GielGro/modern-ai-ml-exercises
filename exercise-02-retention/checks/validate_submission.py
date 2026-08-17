from pathlib import Path
import sys
import numpy as np
import pandas as pd

EXPECTED = ["customer_id", "churn_probability", "contact_customer"]


def validate(path: Path) -> None:
    submission = pd.read_csv(path)
    test = pd.read_csv(Path(__file__).parents[1] / "data" / "test.csv")
    assert submission.columns.tolist() == EXPECTED, f"Expected columns {EXPECTED}"
    assert len(submission) == len(test), "Row count does not match test.csv"
    assert submission.customer_id.is_unique, "customer_id values must be unique"
    assert set(submission.customer_id) == set(test.customer_id), "IDs must exactly match test.csv"
    p = pd.to_numeric(submission.churn_probability, errors="coerce")
    assert np.isfinite(p).all() and p.between(0, 1).all(), "Probabilities must be finite and in [0, 1]"
    assert set(submission.contact_customer.dropna().unique()).issubset({0, 1}), "contact_customer must be 0 or 1"
    print(f"Valid submission: {len(submission):,} decisions; {submission.contact_customer.mean():.1%} contacted")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "submission.csv"))
