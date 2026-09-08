# 2024 local excellent-paper corpus analysis

## Scope and access

This analysis uses only the ten replacement local PDFs in `2024优秀论文`: 3 A, 3 B, and 4 C papers (513 pages total). It uses direct page-aware extraction through macOS PDFKit, with targeted alternate-render review where available; no OCR, other-year excellent papers, or reference-repository case material supplied evidence.

| Problem | Cards | Direct text readable | Alternate-render page-1 CJK legible |
| --- | ---: | ---: | ---: |
| A | 3 | 3 | 2 |
| B | 3 | 3 | 1 |
| C | 4 | 4 | 2 |
| Total | 10 | 10 | 5 |

- [observed] All ten evidence records are local-PDF records with page locators and SHA-256 values; PDFKit extracted readable text on every page of every selected source. [ev-paper-2024-a-geometry-path, pp. 1-45; ev-paper-2024-a-dynamic-search-route, pp. 1-58; ev-paper-2024-a-objective-optimization-form, pp. 1-62; ev-paper-2024-b-multistage-simulation, pp. 1-70; ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-28; ev-paper-2024-b-production-decision-design, pp. 1-37; ev-paper-2024-c-optimization-planting, pp. 1-49; ev-paper-2024-c-differential-ga-planting, pp. 1-61; ev-paper-2024-c-ga-planting, pp. 1-45; ev-paper-2024-c-stochastic-planting, pp. 1-58]
- [observed] Targeted source pages include A collision/sensitivity checks, B result/evaluation or robustness, and C sensitivity/robust selection; the alternate renderer lacks CJK glyph support for five PDFs, so unreviewed figure/table details remain unverified. [ev-paper-2024-a-dynamic-search-route, pp. 13, 16-17, 26, 28-29; ev-paper-2024-a-objective-optimization-form, pp. 16-17, 28-29; ev-paper-2024-b-aco-ga-monte-carlo, pp. 20-22; ev-paper-2024-b-multistage-simulation, pp. 15, 21; ev-paper-2024-b-production-decision-design, pp. 21-23; ev-paper-2024-c-optimization-planting, pp. 18, 27; ev-paper-2024-c-differential-ga-planting, p. 42]

## Required-dimension summary

| Required analysis dimension | Corpus result | Evidence boundary |
| --- | --- | --- |
| Paper count | [observed] 10 local papers, totaling 513 pages. | Complete for the user-selected 2024 PDFs, not the wider CUMCM literature. |
| Year and problem | [observed] 2024 A: 3; 2024 B: 3; 2024 C: 4. | No reusable 2025 solution paper is mixed into this corpus. |
| Problem types | [inferred] A: geometry/kinematics/event constraints; B: sampling and multistage quality decisions; C: multi-period constrained allocation. | Types summarize mathematical structure, not contest-letter stereotypes. |
| Model types | [observed] Geometry/recurrence/collision, sampling/expected-profit/state decisions, LP/constrained allocation, scenario/risk models, and numerical or metaheuristic search. | Presence is not evidence that a family is valid for a future task. |
| Model combinations | [inferred] Mechanism + boundary/global search; sampling + decision graph + uncertainty update; deterministic allocation + scenario/robust/risk extension. | A combination is transferable only when each added layer fixes a named limitation. |
| Data processing | [observed] A mainly uses deterministic geometry; B uses sampling or generated defect scenarios; C maps workbook economic/land inputs into allocation parameters. [unverified] Detailed raw-data cleaning was not confirmed in most reviewed pages. | Do not infer imputation, outlier treatment, distribution fit, or correlation quality when absent. |
| Validation methods | [observed] Explicit validation/sensitivity/evaluation sections were located in 7 of 10 cards, including collision/model checks, defect scenarios, and planting sensitivity/robust selection. | Section presence does not prove independent replication or adequate controls. |
| Sensitivity/robustness | [observed] Parameter sensitivity, 3-sigma defect scenarios, Bayesian updates, uncertain crop inputs, CVaR, and robust selection appear in B/C/A subsets. | Distribution choice, risk level, and perturbation range require task-specific justification. |
| Figure types/purposes | [observed] Identifiable purposes in 6 cards cover geometry/state explanation, decision flow, solver comparison, and plan/risk comparison; 4 cards remain figure-level `unverified`. | No palette or chart style is copied mechanically. |
| Abstract pattern | [observed] All 10 abstracts progress from problem to method to solution/reportable output, with differing numerical detail. | This is a reasoning shape, not a sentence template or fixed Q1/Q2 repetition. |
| Common paper structure | [inferred] Formalize objects/constraints -> establish a mechanism or accounting baseline -> apply a solution layer -> report outputs -> evaluate or discuss limits. | Chronological work logs and unexplained formula stacks are not promoted as patterns. |
| Model-improvement pattern | [inferred] More complete collision checks, scale-up search, parameter uncertainty, tail risk, or interaction assumptions are added after a base model. | An addition counts as improvement only after baseline-defect naming, controlled comparison, and failure-mode validation. |

The ten paper cards now contain **39 explicit question records**: 15 across the three five-question A papers, 12 across the three four-question B papers, and 12 across the four three-question C papers. Every record exposes Goal, Variables, Assumptions, Data Processing, Baseline, Model, Algorithm, Validation, Visualization, and Main Result; each card separately records Strong Points, Weak Points, Transferable Patterns, and Problem-Specific Tricks.

## Observed structures and reported practices

| Structure | Count in selected cards | Observed support | Validity boundary |
| --- | ---: | --- | --- |
| Geometry/kinematics with collision constraints | 3 A | Spiral, linked-handle recurrences, tangent turnaround, collision screening. [observed] [ev-paper-2024-a-geometry-path, pp. 1-4; ev-paper-2024-a-dynamic-search-route, pp. 1, 13; ev-paper-2024-a-objective-optimization-form, pp. 1-3] | No paper establishes that its screening reduction is universally complete. |
| Constrained pitch/speed optimization | 3 A | Pitch and speed objectives are coupled to geometry constraints. [observed] [ev-paper-2024-a-geometry-path, pp. 1-4; ev-paper-2024-a-dynamic-search-route, pp. 1, 16-17, 28-29; ev-paper-2024-a-objective-optimization-form, pp. 1-3] | One abstract displays inconsistent speed units, so numeric comparison is unsafe. |
| Quality-control decision graph | 3 B | Sampling, inspect/disassemble decisions, feedback loops, expected-profit comparison. [observed] [ev-paper-2024-b-multistage-simulation, pp. 1-2; ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-4, 7-9; ev-paper-2024-b-production-decision-design, pp. 1-2] | The reported distributional approximations and thresholds are not independently validated. |
| Planting allocation under operational constraints | 4 C | Area variables, land/rotation/legume/season and surplus-sale constraints. [observed] [ev-paper-2024-c-optimization-planting, pp. 1-3; ev-paper-2024-c-differential-ga-planting, pp. 1-2; ev-paper-2024-c-ga-planting, pp. 1-3; ev-paper-2024-c-stochastic-planting, pp. 1-3] | Solver output is not a proof of optimality without formulation and reproducibility checks. |
| Uncertainty / robustness extension | 7 B/C cards | Defect scenarios; Bayesian updates; demand/yield/cost/price variation; CVaR, hazard factors, or robust selection. [observed] [ev-paper-2024-b-multistage-simulation, p. 1; ev-paper-2024-b-aco-ga-monte-carlo, pp. 20-22; ev-paper-2024-b-production-decision-design, p. 1; ev-paper-2024-c-optimization-planting, pp. 1, 18, 27; ev-paper-2024-c-differential-ga-planting, pp. 1, 25-30, 42; ev-paper-2024-c-ga-planting, pp. 1-3; ev-paper-2024-c-stochastic-planting, pp. 1-3] | Frequency does not prove a particular scenario distribution, penalty, or algorithm is valid. |

## Frequency is not validity

- [observed] Search/heuristic methods appear across all ten selected cards: recurrence/search in A, simulation/annealing/ACO/GA/DP in B, and solver/GA/CVaR/stochastic planning in C. [ev-paper-2024-a-geometry-path, p. 1; ev-paper-2024-a-dynamic-search-route, pp. 1, 16-17, 28-29; ev-paper-2024-a-objective-optimization-form, pp. 1-3; ev-paper-2024-b-multistage-simulation, p. 1; ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-4; ev-paper-2024-b-production-decision-design, p. 1; ev-paper-2024-c-optimization-planting, p. 1; ev-paper-2024-c-differential-ga-planting, p. 1; ev-paper-2024-c-ga-planting, pp. 1-3; ev-paper-2024-c-stochastic-planting, pp. 1-3]
- [inferred] This is still a small selected corpus, so recurrence of a method is a coverage observation, not a recommendation to default to GA, ACO, or simulation. [ev-paper-2024-a-geometry-path, p. 1; ev-paper-2024-a-dynamic-search-route, p. 1; ev-paper-2024-a-objective-optimization-form, p. 1; ev-paper-2024-b-multistage-simulation, p. 1; ev-paper-2024-b-aco-ga-monte-carlo, p. 1; ev-paper-2024-b-production-decision-design, p. 1; ev-paper-2024-c-optimization-planting, p. 1; ev-paper-2024-c-differential-ga-planting, p. 1; ev-paper-2024-c-ga-planting, p. 1; ev-paper-2024-c-stochastic-planting, p. 1]
- [expert-rule] Select a method after writing the state/decision variables, governing relation, constraints, objective, and a simpler feasible baseline; then demonstrate why the extra search or stochastic layer changes a decision-relevant outcome.

## Abstract, figures, and improvement patterns

- [observed] All ten abstracts use a problem-to-model-to-solution-to-reported-output progression, although the degree of numerical detail differs. [ev-paper-2024-a-geometry-path, p. 1; ev-paper-2024-a-dynamic-search-route, p. 1; ev-paper-2024-a-objective-optimization-form, p. 1; ev-paper-2024-b-multistage-simulation, p. 1; ev-paper-2024-b-aco-ga-monte-carlo, p. 1; ev-paper-2024-b-production-decision-design, p. 1; ev-paper-2024-c-optimization-planting, p. 1; ev-paper-2024-c-differential-ga-planting, p. 1; ev-paper-2024-c-ga-planting, p. 1; ev-paper-2024-c-stochastic-planting, p. 1]
- [observed] Explicit validation/sensitivity or evaluation sections were located in seven cards: two A, three B, and two C. [ev-paper-2024-a-dynamic-search-route, pp. 13, 16-17, 26, 28-29; ev-paper-2024-a-objective-optimization-form, pp. 16-17, 28-29; ev-paper-2024-b-multistage-simulation, pp. 15, 21; ev-paper-2024-b-aco-ga-monte-carlo, pp. 20-22; ev-paper-2024-b-production-decision-design, pp. 21-23; ev-paper-2024-c-optimization-planting, pp. 18, 27; ev-paper-2024-c-differential-ga-planting, p. 42]
- [observed] Figure purposes were identified in six cards: geometry/state explanation in A, decision-flow explanation in B, and constraint/plan/scenario comparison in C; figure-level purposes in the remaining four cards were left unverified rather than inferred. [ev-paper-2024-a-geometry-path, pp. 2-4; ev-paper-2024-a-objective-optimization-form, pp. 2-3; ev-paper-2024-b-aco-ga-monte-carlo, pp. 3, 20-22; ev-paper-2024-c-optimization-planting, pp. 1-3, 18, 27; ev-paper-2024-c-ga-planting, pp. 1-3; ev-paper-2024-c-stochastic-planting, pp. 1-3, 15-22]
- [expert-rule] A figure is useful when it resolves a geometry/state, decision-flow, or plan/risk question, not merely because a paper has many figures.
- [expert-rule] Treat an “improvement” as a testable change to an identified limitation (for example, a missing constraint, uncertainty source, or numerical check), with a fixed baseline and the same unit conventions.

## A-problem focus: mechanism and disagreement

- [observed] All three A papers start with equal-pitch spiral geometry, linked-rigid-bench relations, collision constraints, tangent-turnaround geometry, and a speed cap. [ev-paper-2024-a-geometry-path, pp. 1-4; ev-paper-2024-a-dynamic-search-route, p. 1; ev-paper-2024-a-objective-optimization-form, pp. 1-3]
- [observed] Their collision/numerical strategies differ: geometry-path reduces the check to selected corners and handle lines, dynamic-search brackets/bisects a corner-to-line collision predicate and uses particle swarm/ternary search, while objective-optimization uses rectangular separating-axis tests and reports sensitivity/model checks. [ev-paper-2024-a-geometry-path, pp. 1, 4; ev-paper-2024-a-dynamic-search-route, pp. 1, 13, 16-17, 26, 28-29; ev-paper-2024-a-objective-optimization-form, pp. 1-3, 16-17, 28-29]
- [observed] The objective-optimization abstract reports a maximum speed in `cm/s`, while its stated problem convention lists leader speed in `m/s`; this is recorded as a source inconsistency, not normalized by this corpus. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]
- [observed] The dynamic-search A paper independently reports the same 0.450337 m pitch scale and a 1.246266 m/s speed result after its own collision/search construction. [ev-paper-2024-a-dynamic-search-route, pp. 1, 16-17, 28-29]
- [expert-rule] For geometry mechanisms, verify dimensions/units at input, governing equations, stopping condition, and reported output; test limiting configurations and run an independent full-geometry collision check near the claimed optimum.

## Saturation and limitations

- [observed] This is complete coverage of the ten user-selected local PDFs, not saturation over the larger CUMCM literature. [ev-paper-2024-a-geometry-path, pp. 1-45; ev-paper-2024-a-dynamic-search-route, pp. 1-58; ev-paper-2024-a-objective-optimization-form, pp. 1-62; ev-paper-2024-b-multistage-simulation, pp. 1-70; ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-28; ev-paper-2024-b-production-decision-design, pp. 1-37; ev-paper-2024-c-optimization-planting, pp. 1-49; ev-paper-2024-c-differential-ga-planting, pp. 1-61; ev-paper-2024-c-ga-planting, pp. 1-45; ev-paper-2024-c-stochastic-planting, pp. 1-58]
- [observed] The alternate renderer's missing CJK glyphs limits visual equation/table inspection for five papers, but PDFKit direct extraction is readable and their method claims are included. [ev-paper-2024-a-dynamic-search-route, p. 1; ev-paper-2024-b-multistage-simulation, p. 1; ev-paper-2024-b-production-decision-design, p. 1; ev-paper-2024-c-differential-ga-planting, p. 1; ev-paper-2024-c-stochastic-planting, p. 1]
- [expert-rule] Do not turn unverified formula/table visual detail into a mandatory method rule; obtain a clean visual confirmation before expanding evidence beyond clearly extracted prose.
