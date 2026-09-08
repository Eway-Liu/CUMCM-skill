#!/usr/bin/env python3
"""Small matplotlib style for CUMCM paper figures."""

from __future__ import annotations

import matplotlib as mpl


def paper_style() -> dict[str, object]:
    return {
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "font.family": "sans-serif",
        "font.sans-serif": [
            "Noto Sans CJK SC",
            "Source Han Sans SC",
            "PingFang SC",
            "Microsoft YaHei",
            "SimHei",
            "DejaVu Sans",
        ],
        "mathtext.fontset": "stix",
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "axes.unicode_minus": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "legend.frameon": False,
        "grid.color": "#D9D9D9",
        "grid.linewidth": 0.5,
        "grid.alpha": 0.6,
        "lines.linewidth": 1.4,
        "lines.markersize": 4,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }


def apply_paper_style() -> None:
    mpl.rcParams.update(paper_style())


if __name__ == "__main__":
    apply_paper_style()

