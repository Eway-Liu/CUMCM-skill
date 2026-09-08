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

- Local source: `2024优秀论文/2024C 基于随机优化的农作物种植策略模型.pdf` (58 pages).
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
