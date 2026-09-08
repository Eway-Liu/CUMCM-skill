# Excellent-paper patterns: evidence-linked decision rules

## Rules from the local 2024 corpus

- [observed] All ten local papers begin by making the problem's state/decision structure explicit: linked geometry in A, process decision nodes in B, and plot-year crop areas in C. [ev-paper-2024-a-geometry-path, pp. 1-4; ev-paper-2024-a-dynamic-search-route, p. 1; ev-paper-2024-a-objective-optimization-form, pp. 1-3; ev-paper-2024-b-multistage-simulation, pp. 1-2; ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-4; ev-paper-2024-b-production-decision-design, pp. 1-2; ev-paper-2024-c-optimization-planting, pp. 1-3; ev-paper-2024-c-differential-ga-planting, pp. 1-2; ev-paper-2024-c-ga-planting, pp. 1-3; ev-paper-2024-c-stochastic-planting, pp. 1-3]
- [expert-rule] Write a simplest feasible baseline before a metaheuristic: recurrence plus full collision test for geometry, enumeration/dynamic programming for a small decision graph, or a transparent constrained program for allocation.
- [observed] The B paper retains a decision-tree/expected-profit representation before applying Monte Carlo/ACO/GA; the C papers retain crop/land constraints when uncertainty is added. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 3, 7-9; ev-paper-2024-c-optimization-planting, pp. 1-3; ev-paper-2024-c-ga-planting, pp. 1-3]
- [expert-rule] Add a search algorithm only when the exact baseline is too large or nonconvex, and state the decision variables, encoding, feasible-repair method, seed/restarts, stopping criterion, and comparison metric.
- [observed] Explicit verification appears as collision/sensitivity checks, defect-rate scenarios, and planting sensitivity/robust selection. [ev-paper-2024-a-objective-optimization-form, pp. 16-17, 28-29; ev-paper-2024-b-aco-ga-monte-carlo, pp. 20-22; ev-paper-2024-c-optimization-planting, pp. 18, 27]
- [expert-rule] Match validation to failure mode: geometry needs boundary/overlap tests; stochastic decisions need scenario or resampling analysis; allocations need constraint violations, out-of-sample scenarios, and objective trade-offs.
- [observed] All four C papers make two surplus-sale assumptions visible and later add uncertainty, risk, or interaction assumptions. [ev-paper-2024-c-optimization-planting, pp. 1-3; ev-paper-2024-c-differential-ga-planting, pp. 1-2, 25-30; ev-paper-2024-c-ga-planting, pp. 1-3; ev-paper-2024-c-stochastic-planting, pp. 1-3]
- [expert-rule] A model extension is credible only when its new assumption is named, parameterized, and assessed against the same baseline; simulated interaction data cannot by itself establish a real market relationship.

## Guardrails

- [observed] One A abstract has an apparent speed-unit inconsistency. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]
- [expert-rule] Treat all source-reported numbers as provisional until units, formula symbols, and result-table headers agree. Do not infer missing equations or tables from visual detail that has not been confirmed.
- [observed] Five PDFs require native PDFKit rather than pypdf for readable Chinese text; their alternate rendered pages lack CJK glyphs, so unreviewed equation/table details remain unverified rather than the papers themselves. [ev-paper-2024-a-dynamic-search-route, p. 1; ev-paper-2024-b-multistage-simulation, p. 1; ev-paper-2024-b-production-decision-design, p. 1; ev-paper-2024-c-differential-ga-planting, p. 1; ev-paper-2024-c-stochastic-planting, p. 1]
