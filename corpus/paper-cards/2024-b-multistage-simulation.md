---
id: 2024-b-multistage-simulation
year: 2024
problem: B
title: 基于多阶段模拟仿真的生产决策问题
source_evidence: [ev-paper-2024-b-multistage-simulation]
tags: [quality-control, acceptance-sampling, multistage-decision, expected-profit, simulated-annealing, bayesian-updating]
---

# 2024 B - Multistage simulation production decision

## Source and evidence quality

- Historical source identity: `2024优秀论文/2024B 基于多阶段模拟仿真的生产决策问题.pdf` (70 pages; raw PDF removed after distillation).
- Evidence: `ev-paper-2024-b-multistage-simulation`.
- [observed] Native PDFKit page extraction reads the Chinese text layer directly; the bundled renderer's missing CJK mapping remains a visual-verification limitation. [ev-paper-2024-b-multistage-simulation, pp. 1, 15, 21]

## Subproblem objectives and dependencies

- [observed] The `(n,c)` sampling plan addresses acceptance first; multistage inspection/disassembly binary decisions use the resulting defect-rate treatment and are compared by expected net profit. [ev-paper-2024-b-multistage-simulation, pp. 1-2]

## Assumptions, data, and preprocessing

- [observed] The paper simulates production inputs with a normal distribution and uses `(n,c)` sampling and binary stage decisions. [ev-paper-2024-b-multistage-simulation, pp. 1-2]
- [unverified] not confirmed: empirical-data provenance, cleaning, or missing-value treatment. [ev-paper-2024-b-multistage-simulation, pp. 1-2]

## Baseline, model, and algorithm

- [observed] Expected net profit and the multistage binary-decision representation are the baseline model; simulation, linear simulated annealing, and Bayesian updating extend the calculation. [ev-paper-2024-b-multistage-simulation, pp. 1-2]
- [inferred] A multistage formulation fits when disassembly returns components to earlier stages, but a state-transition/expected-profit baseline should remain auditable before annealing is trusted. [ev-paper-2024-b-multistage-simulation, pp. 1-2]

## Validation, sensitivity/robustness, and figure purposes

- [observed] The paper provides simulation-results and model-evaluation sections. [ev-paper-2024-b-multistage-simulation, pp. 15, 21]
- [unverified] not confirmed: a targeted parameter-sensitivity design, convergence trace, or independent holdout validation. [ev-paper-2024-b-multistage-simulation, pp. 15, 21]
- [unverified] not confirmed: specific figure/table encodings, because the alternate renderer does not map CJK glyphs and detailed visual review was not used to reconstruct them. [ev-paper-2024-b-multistage-simulation, pp. 15, 21]

## Reported results, strengths, limitations, and transferable rules

- [unverified] not confirmed: sampling pairs, profit matrices, annealing parameters, and simulation replication design as generally valid outputs. [ev-paper-2024-b-multistage-simulation, pp. 1, 15, 21]
- [inferred] The explicit staging of sampling, production decisions, and Bayesian defect-rate updating is a useful feature. [ev-paper-2024-b-multistage-simulation, pp. 1-2]
- [inferred] For looped production systems, establish the state transition and expected-profit accounting before adopting an annealing search. [ev-paper-2024-b-multistage-simulation, pp. 1-2]

## Structured question records

Problem Type: [inferred] acceptance sampling, multistage expected-profit simulation, and uncertainty-aware discrete optimization.

### Q1

- Goal: [observed] Obtain an `(n,c)` acceptance plan satisfying the stated confidence requirements.
- Variables: [observed] Sample size, allowed defect count, observed defects, and lot decision.
- Assumptions: [observed] Production inputs are simulated with a normal-distribution treatment in the paper's framework.
- Data Processing: [unverified] Empirical provenance, cleaning, and distribution diagnostics were not confirmed.
- Baseline: [inferred] Exact acceptance probability under the stated defect model.
- Model: [observed] `(n,c)` sampling plan.
- Algorithm: [inferred] Search candidate `(n,c)` pairs against acceptance/rejection constraints.
- Validation: [inferred] Check both confidence constraints and compare simulation against exact probabilities.
- Visualization: [unverified] Exact sampling-plan visual encoding was not confirmed.
- Main Result: [unverified] Reported sampling pairs were not independently replicated. [ev-paper-2024-b-multistage-simulation, pp. 1-2]

### Q2

- Goal: [observed] Select inspections and disassembly for the two-component production cases.
- Variables: [observed] Binary stage actions and expected revenues/costs.
- Assumptions: [observed] Disassembly/return behavior follows the modeled feedback process.
- Data Processing: [unverified] No empirical missing-value or cleaning procedure is reported.
- Baseline: [observed] Expected net profit over binary decision states.
- Model: [observed] Multistage inspection/disassembly decision representation.
- Algorithm: [observed] Simulation and linear simulated annealing extend the expected-profit calculation.
- Validation: [observed] A simulation-results section exists; exhaustive small-case comparison is unverified.
- Visualization: [unverified] Specific result-table and plot encodings were not visually confirmed.
- Main Result: [unverified] Case policies and profit values were not independently reproduced. [ev-paper-2024-b-multistage-simulation, pp. 1-2, 15]

### Q3

- Goal: [observed] Extend the decision model to the two-process, eight-component system.
- Variables: [observed] Component/intermediate/final inspection and disassembly actions plus process state and net profit.
- Assumptions: [inferred] The chosen state contains enough feedback information to evaluate future cost and yield.
- Data Processing: [unverified] No raw-data preprocessing is reported.
- Baseline: [observed] Auditable state-transition and expected-profit accounting.
- Model: [observed] Multistage binary decision system.
- Algorithm: [observed] Simulation with simulated-annealing search.
- Validation: [unverified] Small-instance enumeration, multiple seeds, feasibility rate, and bound/gap evidence were not confirmed.
- Visualization: [unverified] Process/result figure encodings were not confirmed.
- Main Result: [unverified] The large-system policy and profit matrix were not independently reproduced. [ev-paper-2024-b-multistage-simulation, pp. 1-2, 15]

### Q4

- Goal: [observed] Update defect-rate beliefs from samples and reassess Q2/Q3 decisions.
- Variables: [observed] Prior/posterior defect parameters, policy actions, and expected net profit.
- Assumptions: [observed] Bayesian updating is used for defect-rate uncertainty.
- Data Processing: [inferred] Sampling information is converted to posterior parameters; calibration details are unverified.
- Baseline: [inferred] Nominal-rate policy without posterior updating.
- Model: [observed] Bayesian defect-rate update coupled to multistage decisions.
- Algorithm: [observed] Posterior updating followed by repeated simulation/search.
- Validation: [observed] A model-evaluation section exists; posterior predictive checks are unverified.
- Visualization: [unverified] Specific uncertainty/result graphics were not confirmed.
- Main Result: [unverified] Posterior-sensitive policies and numerical gains were not independently replicated. [ev-paper-2024-b-multistage-simulation, pp. 1-2, 21]

## Strong Points

- [inferred] Sampling, production-state accounting, search, and uncertainty updating are staged rather than collapsed into one opaque objective.

## Weak Points

- [unverified] Distribution diagnostics, annealing repeatability, exact small-case checks, and posterior predictive validation were not confirmed.

## Transferable Patterns

- [expert-rule] Build and verify the state transition and expected-profit ledger before adding simulation, annealing, or Bayesian uncertainty layers.

## Problem-Specific Tricks

- [observed] The `(n,c)` plan, inspect/disassemble actions, and return-to-earlier-stage loop reflect the 2024 B manufacturing graph.
