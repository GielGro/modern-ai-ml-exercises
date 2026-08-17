from pathlib import Path
import sys
import pandas as pd


def validate(path: Path) -> None:
    submission = pd.read_csv(path)
    customers = pd.read_csv(Path(__file__).parents[1] / "data/customers.csv")
    assert submission.columns.tolist() == ["customer_id", "segment_id"]
    assert submission.customer_id.is_unique
    assert set(submission.customer_id) == set(customers.customer_id)
    segment = pd.to_numeric(submission.segment_id, errors="raise")
    assert (segment == segment.astype(int)).all()
    unique = sorted(segment.astype(int).unique())
    assert 3 <= len(unique) <= 8, "Use 3–8 segments"
    assert unique == list(range(len(unique))), "Segment IDs must be consecutive from 0"
    sizes = segment.value_counts(normalize=True)
    assert sizes.min() >= .01, "Every segment must contain at least 1% of customers"
    print(f"Valid: {len(submission):,} customers across {len(unique)} segments")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "segments.csv"))
