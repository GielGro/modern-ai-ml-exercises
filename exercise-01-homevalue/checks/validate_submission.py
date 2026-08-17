from pathlib import Path
import sys
import numpy as np
import pandas as pd

EXPECTED = ["property_id", "predicted_sale_price"]


def validate(path: Path) -> None:
    submission = pd.read_csv(path)
    test = pd.read_csv(Path(__file__).parents[1] / "data" / "test.csv")
    assert submission.columns.tolist() == EXPECTED, f"Expected columns {EXPECTED}"
    assert len(submission) == len(test), "Row count does not match test.csv"
    assert submission.property_id.is_unique, "property_id values must be unique"
    assert set(submission.property_id) == set(test.property_id), "IDs must exactly match test.csv"
    values = pd.to_numeric(submission.predicted_sale_price, errors="coerce")
    assert np.isfinite(values).all(), "Predictions must be numeric and finite"
    assert (values > 0).all(), "Predictions must be positive"
    print(f"Valid submission: {len(submission):,} predictions")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "submission.csv"))
