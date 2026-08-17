from pathlib import Path
import sys
import numpy as np
import pandas as pd


def validate(path: Path) -> None:
    base = Path(__file__).parents[1]
    submission = pd.read_csv(path)
    test = np.load(base / "data/test_images.npz")
    allowed = set(pd.read_csv(base / "data/label_map.csv").label)
    assert submission.columns.tolist() == ["image_id", "predicted_label"]
    assert submission.image_id.is_unique
    assert set(submission.image_id) == set(test["image_id"])
    assert set(submission.predicted_label).issubset(allowed)
    print(f"Valid: {len(submission):,} image predictions")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "submission.csv"))
