#!/usr/bin/env python3
"""Small deterministic helpers for common CUMCM validation checks."""

from __future__ import annotations

import math
from collections.abc import Iterable


def time_split(
    n: int, train_fraction: float, validation_fraction: float
) -> tuple[list[int], list[int], list[int]]:
    if n < 3:
        raise ValueError("n must allow nonempty train, validation, and test sets")
    if train_fraction <= 0 or validation_fraction <= 0 or train_fraction + validation_fraction >= 1:
        raise ValueError("fractions must be positive and sum to less than 1")
    train_end = int(n * train_fraction)
    validation_end = train_end + int(n * validation_fraction)
    if train_end == 0 or validation_end == train_end or validation_end >= n:
        raise ValueError("fractions must produce nonempty train, validation, and test sets")
    return (
        list(range(train_end)),
        list(range(train_end, validation_end)),
        list(range(validation_end, n)),
    )


def regression_metrics(y_true: Iterable[float], y_pred: Iterable[float]) -> dict[str, float]:
    actual = [float(value) for value in y_true]
    predicted = [float(value) for value in y_pred]
    if len(actual) != len(predicted):
        raise ValueError("y_true and y_pred must have the same length")
    if not actual:
        raise ValueError("y_true and y_pred must not be empty")
    errors = [estimate - truth for truth, estimate in zip(actual, predicted)]
    return {
        "mae": sum(abs(error) for error in errors) / len(errors),
        "mse": sum(error * error for error in errors) / len(errors),
        "rmse": math.sqrt(sum(error * error for error in errors) / len(errors)),
    }


def constraint_violations(
    values: Iterable[float], lower: float | None = None, upper: float | None = None
) -> dict[str, int | float]:
    if lower is not None and upper is not None and lower > upper:
        raise ValueError("lower must not exceed upper")
    materialized = [float(value) for value in values]
    lower_amounts = [max(0.0, float(lower) - value) if lower is not None else 0.0 for value in materialized]
    upper_amounts = [max(0.0, value - float(upper)) if upper is not None else 0.0 for value in materialized]
    return {
        "lower_count": sum(amount > 0 for amount in lower_amounts),
        "upper_count": sum(amount > 0 for amount in upper_amounts),
        "max_violation": max(lower_amounts + upper_amounts, default=0.0),
    }


def perturbation_grid(value: float, fractions: Iterable[float]) -> list[float]:
    return [float(value) + float(value) * float(fraction) for fraction in fractions]
