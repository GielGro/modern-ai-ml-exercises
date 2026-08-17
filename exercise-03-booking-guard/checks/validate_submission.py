from pathlib import Path
import sys
import numpy as np
import pandas as pd

EXPECTED = ["booking_id", "cancellation_probability", "require_deposit"]


def validate(path: Path) -> None:
    submission = pd.read_csv(path)
    test = pd.read_csv(Path(__file__).parents[1] / "data/test.csv")
    assert submission.columns.tolist() == EXPECTED, f"Expected columns {EXPECTED}"
    assert len(submission) == len(test)
    assert submission.booking_id.is_unique
    assert set(submission.booking_id) == set(test.booking_id)
    probability = pd.to_numeric(submission.cancellation_probability, errors="coerce")
    assert np.isfinite(probability).all() and probability.between(0, 1).all()
    assert set(submission.require_deposit.unique()).issubset({0, 1})
    print(f"Valid: {len(submission):,} bookings; {submission.require_deposit.mean():.1%} deposits")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "submission.csv"))
