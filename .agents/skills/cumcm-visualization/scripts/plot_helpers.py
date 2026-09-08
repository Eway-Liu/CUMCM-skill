#!/usr/bin/env python3
"""Minimal reusable plots for verified CUMCM results."""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from pathlib import Path

import matplotlib.pyplot as plt


def _axis_label(prefix: str, variable: str, unit: str | None) -> str:
    suffix = f" ({unit})" if unit else ""
    return f"{prefix} {variable}{suffix}"


def actual_vs_predicted(
    actual: Iterable[float],
    predicted: Iterable[float],
    *,
    variable: str,
    unit: str | None = None,
):
    actual_values = [float(value) for value in actual]
    predicted_values = [float(value) for value in predicted]
    if len(actual_values) != len(predicted_values):
        raise ValueError("actual and predicted must have the same length")
    if not actual_values:
        raise ValueError("actual and predicted must not be empty")

    low = min(actual_values + predicted_values)
    high = max(actual_values + predicted_values)
    padding = (high - low) * 0.04 or 0.04
    fig, ax = plt.subplots(figsize=(3.4, 3.2), constrained_layout=True)
    ax.scatter(
        actual_values,
        predicted_values,
        s=24,
        facecolors="white",
        edgecolors="#2F5D8A",
        linewidths=1.0,
        label="Observations",
    )
    ax.plot(
        [low - padding, high + padding],
        [low - padding, high + padding],
        color="#333333",
        linestyle="--",
        linewidth=1.0,
        label="Ideal",
    )
    ax.set_xlim(low - padding, high + padding)
    ax.set_ylim(low - padding, high + padding)
    ax.set_xlabel(_axis_label("Actual", variable, unit))
    ax.set_ylabel(_axis_label("Predicted", variable, unit))
    ax.grid(True)
    ax.legend(loc="best")
    return fig, ax


def save_figure(
    figure,
    stem: Path,
    *,
    formats: Sequence[str] = ("png", "pdf", "svg"),
) -> list[Path]:
    stem = Path(stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for format_name in formats:
        normalized = format_name.lower().lstrip(".")
        if normalized not in {"png", "pdf", "svg"}:
            raise ValueError(f"unsupported figure format: {format_name}")
        output = stem.with_suffix(f".{normalized}")
        figure.savefig(output, format=normalized, bbox_inches="tight")
        outputs.append(output)
    return outputs

