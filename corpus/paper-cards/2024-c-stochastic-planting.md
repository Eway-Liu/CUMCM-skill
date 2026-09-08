---
id: 2024-c-stochastic-planting
year: 2024
problem: C
title: 基于随机优化的农作物种植策略模型
source_evidence: [ev-paper-2024-c-stochastic-planting]
tags: [allocation-optimization, crop-planning, linear-programming, greedy-baseline, stochastic-programming, monte-carlo]
---

# 2024 C - Stochastic-optimization crop planting

## Source and evidence quality

- Historical source identity: `2024优秀论文/2024C 基于随机优化的农作物种植策略模型.pdf` (58 pages; raw PDF removed after distillation).
- Evidence: `ev-paper-2024-c-stochastic-planting`.
- [observed] Native PDFKit page extraction reads the Chinese text layer directly; the bundled renderer still lacks CJK glyph output. [ev-paper-2024-c-stochastic-planting, pp. 1-3, 15-22]

## Subproblem objectives and dependencies

- [observed] The first constrained planting linear program with management-concentration parameters establishes a feasible allocation for two surplus-sale cases; the stochastic scenario/perturbation and crop-interaction extensions use that accounting framework. [ev-paper-2024-c-stochastic-planting, pp. 1-3, 15-22]

## Assumptions, data, and preprocessing

- [observed] The paper uses management-concentration parameters, normal random parameter sequences, and stated substitution/complement and sales-price-cost relations. [ev-paper-2024-c-stochastic-planting, pp. 1-3]
- [unverified] not confirmed: raw-data cleaning, normality diagnostics, probability discretization, or correlation estimation. [ev-paper-2024-c-stochastic-planting, pp. 1, 15-22]

## Baseline, model, and algorithm

- [observed] A constrained linear-program solver is compared with a greedy strategy under identical stated surplus assumptions; scenario generation and perturbation/evaluation extend the allocation model. [ev-paper-2024-c-stochastic-planting, pp. 1-3]
- [inferred] The greedy solution is a computational baseline for the same constraints, and a solver comparison is meaningful only when revenue, feasibility, and surplus treatment are identical. [ev-paper-2024-c-stochastic-planting, pp. 1-3]

## Validation, sensitivity/robustness, and figure purposes

- [observed] Separate result-analysis sections examine scenario-plan and interaction extensions. [ev-paper-2024-c-stochastic-planting, pp. 15-22]
- [unverified] not confirmed: a systematic sensitivity grid, convergence diagnostics, individual visual encodings, or independent outcome validation. [ev-paper-2024-c-stochastic-planting, pp. 15-22]
- [observed] The solver-versus-greedy comparison provides a computational baseline figure/table purpose; later outputs support scenario-result analysis. [ev-paper-2024-c-stochastic-planting, pp. 1-3, 15-22]

## Reported results, strengths, limitations, and transferable rules

- [unverified] not confirmed: portable expected-benefit values, scenario count, and units. [ev-paper-2024-c-stochastic-planting, pp. 1, 15-22]
- [inferred] An explicit greedy comparator for the same constrained allocation problem is a useful feature. [ev-paper-2024-c-stochastic-planting, pp. 1-3]
- [inferred] Compare stochastic optimization to a baseline only under identical feasibility and surplus accounting; otherwise performance differences confound model structure with conventions. [ev-paper-2024-c-stochastic-planting, pp. 1-3]

## Structured question records

Problem Type: [inferred] constrained linear allocation with stochastic scenarios and crop/market interaction extensions.

### Q1

- Goal: [observed] Produce feasible planting plans for waste and half-price surplus cases.
- Variables: [observed] Crop area by plot, season, and year plus production, sales, and profit.
- Assumptions: [observed] Land/rotation/legume rules and management-concentration parameters define feasibility.
- Data Processing: [unverified] Raw workbook cleaning and imputation were not confirmed.
- Baseline: [observed] Greedy strategy under the same stated surplus and feasibility rules.
- Model: [observed] Constrained linear-program allocation.
- Algorithm: [observed] Linear-program solver compared with greedy construction.
- Validation: [inferred] Replay all constraints and compare LP/greedy revenue under identical accounting.
- Visualization: [observed] Solver-versus-greedy figures/tables provide a computational comparison.
- Main Result: [unverified] Expected-benefit values and full plans were not independently reproduced. [ev-paper-2024-c-stochastic-planting, pp. 1-3]

### Q2

- Goal: [observed] Optimize/evaluate planting plans under uncertain demand, yield, cost, and price.
- Variables: [observed] Random parameter sequences, crop areas, scenario outcomes, and expected benefit.
- Assumptions: [observed] Normal random sequences represent the paper's uncertain parameters.
- Data Processing: [unverified] Normality diagnostics, scenario count, and probability discretization were not confirmed.
- Baseline: [inferred] Q1 nominal feasible plan evaluated on the same scenarios.
- Model: [observed] Stochastic scenario allocation and perturbation/evaluation.
- Algorithm: [observed] Scenario generation followed by constrained solution/evaluation.
- Validation: [observed] A separate scenario-result analysis exists; systematic sensitivity and out-of-sample checks are unverified.
- Visualization: [observed] Later outputs support scenario-plan analysis.
- Main Result: [unverified] Expected benefits and preferred stochastic plan were not independently reproduced. [ev-paper-2024-c-stochastic-planting, pp. 15-22]

### Q3

- Goal: [observed] Include crop substitution/complementarity and sales-price-cost relationships.
- Variables: [observed] Relationship parameters, random inputs, crop areas, and scenario outcomes.
- Assumptions: [observed] Stated substitution/complement and market relations govern the extension.
- Data Processing: [unverified] Correlation estimation and empirical calibration were not confirmed.
- Baseline: [inferred] Q2 stochastic model with relationship terms removed.
- Model: [observed] Interaction-aware stochastic allocation.
- Algorithm: [observed] Perturbation and evaluation of feasible plans under the expanded relations.
- Validation: [inferred] Use a relation-free ablation and vary relationship strengths/distributions.
- Visualization: [observed] Later outputs support interaction-scenario result analysis.
- Main Result: [unverified] Interaction-driven benefit changes were not independently reproduced. [ev-paper-2024-c-stochastic-planting, pp. 15-22]

## Strong Points

- [inferred] An explicit greedy comparator provides a simple same-problem baseline for the constrained solver.

## Weak Points

- [unverified] Distribution diagnostics, scenario count, correlation calibration, and independent outcome validation were not confirmed.

## Transferable Patterns

- [expert-rule] Compare stochastic and deterministic methods only under identical constraints and accounting, then isolate scenario and relation layers with ablations.

## Problem-Specific Tricks

- [observed] Management-concentration parameters and the supplied crop substitution/complement assumptions belong to the 2024 C case.
