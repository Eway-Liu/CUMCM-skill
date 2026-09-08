# Final checklist

Use evidence states `pass`, `fail`, `not applicable`, or `not verified`; never turn an unchecked item into a pass.

## Problem and model

- Every subquestion has an identifiable answer.
- Variables, assumptions, equations, constraints and units agree across sections.
- The physical event and its Boolean predicate agree in prose, equations and code.
- Multi-actor objectives handle overlap as intended, and indexed resource limits mean what the text says when expanded on a small case.
- Baseline, model choice, validation, sensitivity and limitations are explicit.

## Data and computation

- Missing values, duplicates, outliers, sampling unit and leakage risk were checked.
- Paths, random seeds, parameters and environments needed to rerun are recorded.
- Key manuscript numbers resolve to saved CSV/JSON/table output, not manual transcription.
- Ratios, percentage changes and before/after labels recompute from those saved values and agree across prose, tables and figures.
- Optimization results satisfy constraints; stochastic algorithms report repeated-run stability.

## Figures and paper

- Every figure has a purpose, source artifact, axes, units, legend and readable export.
- Captions and text interpret the current figure rather than an earlier run.
- Symbols, equation references, figure/table numbering and bibliography are consistent.
- Abstract includes methods, key results and defensible conclusions without invented values.

## Final verdict

List failed and unverified items first. A polished manuscript cannot compensate for an unverified model, stale result or missing constraint.
