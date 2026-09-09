---
name: cumcm-visualization
description: Use when a mathematical modeling competition task needs exploratory data visualization, scientific plotting, result presentation, flowcharts, tables, maps, sensitivity plots, or publication-ready figures.
---

# CUMCM Visualization

Every figure must answer a question. Visual polish cannot rescue an undefined message, unverified data, or misleading scale.

## Figure gate

Require a `FIGURE REQUEST` containing: purpose/question, verified data or a schema-valid `RESULT_MANIFEST`, one-sentence main message, variables, units, output surface and format. If purpose or message is missing, return the smallest diagnostic plan needed to discover it; do not promise all-field plotting, ornamental dashboards, PCA/UMAP, 3D effects, gradients, or exhaustive chart suites.

This Skill does not choose the underlying model. Ask `cumcm-modeling` for verified results or diagnostics when they are absent.

## Workflow

1. Check data grain, denominator, sample size, uncertainty, missing values and whether the claimed comparison is supported.
2. Select the simplest chart by analytical relationship using [chart selection](references/chart-selection.md). Use tables when exact lookup matters more than shape.
3. For EDA, begin with a hypothesis or data-quality question; read [EDA and diagnostics](references/eda-and-diagnostics.md). Stop when the observation has changed or supported a modeling decision.
4. Write a compact figure plan from [template](templates/figure-plan.md) before plotting.
5. Apply [scientific style](references/scientific-style.md). Use explicit units, restrained accessible colors, non-color distinctions, readable Chinese/English text, and vector output where possible.
6. Export in the actual deliverable context, inspect it visually, and revise clipping, scale, legend, density, grayscale and caption problems.

Use [result plots](references/result-plots.md) for prediction, optimization, evaluation, clustering, sensitivity or uncertainty outputs. Use [flowcharts and tables](references/flowcharts-and-tables.md) only when relationships or exact values justify them. Check [common errors](references/common-errors.md) before delivery.

## Python helpers

- `scripts/plot_style.py`: shared matplotlib paper defaults with CJK fallbacks and vector-friendly fonts.
- `scripts/plot_helpers.py`: verified actual-vs-predicted plot and PNG/PDF/SVG export.

Extend helpers only for repeated, stable needs; one-off plots belong with the analysis code.

## Output contract

Return the figure plan and a `FIGURE_MANIFEST` conforming to the [JSON Schema](../../cumcm-shared/schemas/figure-manifest.schema.json). The manifest must bind each output hash to source result artifact IDs, encodings/units, caption/main message, and an audit covering scale, labels, uncertainty, accessibility, export quality, and text consistency. Report failed or unverified items explicitly.

