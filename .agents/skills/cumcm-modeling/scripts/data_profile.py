#!/usr/bin/env python3
"""Produce a compact, read-only profile for a CSV or XLSX table."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import pandas as pd


def profile_frame(frame: pd.DataFrame) -> dict[str, object]:
    """Return deterministic schema and data-quality facts for a DataFrame."""
    numeric = frame.select_dtypes(include="number")
    profile: dict[str, object] = {
        "shape": list(frame.shape),
        "columns": [str(column) for column in frame.columns],
        "dtypes": {str(column): str(dtype) for column, dtype in frame.dtypes.items()},
        "missing": {str(column): int(count) for column, count in frame.isna().sum().items()},
        "duplicate_rows": int(frame.duplicated().sum()),
        "unique_values": {str(column): int(count) for column, count in frame.nunique(dropna=True).items()},
    }
    if not numeric.empty:
        profile["numeric_summary"] = {
            str(column): {
                str(stat): float(value) if math.isfinite(float(value)) else None
                for stat, value in values.items()
            }
            for column, values in numeric.describe().to_dict().items()
        }
        outliers: dict[str, int] = {}
        for column in numeric.columns:
            series = numeric[column].dropna()
            q1, q3 = series.quantile([0.25, 0.75])
            iqr = q3 - q1
            outliers[str(column)] = int(((series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)).sum())
        profile["iqr_outliers"] = outliers
    return profile


def _read_table(path: Path, sheet: str | int = 0) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix == ".tsv":
        return pd.read_csv(path, sep="\t")
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet)
    raise ValueError(f"unsupported table format: {suffix}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--sheet", default=0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = profile_frame(_read_table(args.input, args.sheet))
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
