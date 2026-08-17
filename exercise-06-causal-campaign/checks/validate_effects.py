from pathlib import Path
import sys
import numpy as np
import pandas as pd


def validate(path: Path) -> None:
    estimates = pd.read_csv(path)
    expected = ["outcome", "estimator", "ate", "ci_low", "ci_high"]
    assert estimates.columns.tolist() == expected
    assert set(estimates.outcome) == {"converted", "visited", "spend_usd"}
    assert estimates.outcome.is_unique
    for col in ["ate", "ci_low", "ci_high"]:
        assert np.isfinite(pd.to_numeric(estimates[col], errors="coerce")).all()
    assert (estimates.ci_low <= estimates.ate).all()
    assert (estimates.ate <= estimates.ci_high).all()
    assert estimates.estimator.astype(str).str.len().gt(0).all()
    print("Valid: three causal effect estimates with confidence intervals")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "effect_estimates.csv"))
