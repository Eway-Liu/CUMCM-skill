---
id: 2024-c-differential-ga-planting
year: 2024
problem: C
title: 基于差分遗传算法的农作物种植策略优化
source_evidence: [ev-paper-2024-c-differential-ga-planting]
tags: [allocation-optimization, crop-planning, genetic-algorithm, differential-evolution, cvar, robust-optimization]
---

# 2024 C - Differential-GA crop planting

## Source and evidence quality

- Historical source identity: `2024优秀论文/2024C 基于差分遗传算法的农作物种植策略优化.pdf` (61 pages; raw PDF removed after distillation).
- Evidence: `ev-paper-2024-c-differential-ga-planting`.
- [observed] Native PDFKit page extraction reads the Chinese text layer; the alternate renderer does not map CJK glyphs. [ev-paper-2024-c-differential-ga-planting, pp. 1-2, 42]

## Subproblem objectives and dependencies

- [observed] The paper solves two surplus-sale allocation scenarios under 12 stated constraint classes, then adds CVaR with total profit for uncertain demand/yield/cost/price and Spearman-based crop/market relationships. [ev-paper-2024-c-differential-ga-planting, pp. 1-2, 25-30]

## Assumptions, data, and preprocessing

- [observed] Its inputs include planting constraints plus uncertain demand, yield, cost, and price factors; the extension uses Spearman correlations. [ev-paper-2024-c-differential-ga-planting, pp. 1-2, 25-30]
- [unverified] not confirmed: raw-data provenance, cleaning, correlation-estimation sample, or missing-data method. [ev-paper-2024-c-differential-ga-planting, pp. 25-30]

## Baseline, model, and algorithm

- [observed] The constrained two-scenario allocation model is optimized with a differential-evolution-enhanced genetic algorithm; CVaR with total profit is the stated risk-aware extension. [ev-paper-2024-c-differential-ga-planting, pp. 1-2, 25-30]
- [inferred] CVaR fits when the decision maker identifies tail-loss tolerance; uncertain parameters alone do not justify its use. [ev-paper-2024-c-differential-ga-planting, pp. 1, 25-30]

## Validation, sensitivity/robustness, and figure purposes

- [observed] The paper reports robust-optimization sensitivity over four uncertainty factors. [ev-paper-2024-c-differential-ga-planting, p. 42]
- [unverified] not confirmed: algorithm convergence diagnostics, correlation estimates, or individual visual encodings. [ev-paper-2024-c-differential-ga-planting, pp. 25-30, 42]
- [observed] The later figures/tables support risk/correlation formulation and four-factor robustness analysis. [ev-paper-2024-c-differential-ga-planting, pp. 25-30, 42]

## Reported results, strengths, limitations, and transferable rules

- [unverified] not confirmed: portable profit, CVaR, correlation, or algorithm-setting values and units. [ev-paper-2024-c-differential-ga-planting, pp. 1, 25-30, 42]
- [inferred] Distinguishing surplus cases before adding tail-risk and correlation structure is a useful feature. [ev-paper-2024-c-differential-ga-planting, pp. 1-2, 25-30]
- [inferred] Add CVaR only when tail loss is decision-relevant and calibrate it from defensible distributions; uncertainty alone does not justify the risk objective. [ev-paper-2024-c-differential-ga-planting, pp. 1, 25-30]

## Structured question records

Problem Type: [inferred] multi-period mixed allocation with operational constraints, uncertainty, and tail-risk optimization.

### Q1

- Goal: [observed] Optimize 2024–2030 crop areas under waste and half-price surplus cases.
- Variables: [observed] Crop area by plot, season, year, and crop plus production/sales/profit quantities.
- Assumptions: [observed] Fixed 2023 economic parameters and 12 stated constraint classes define the deterministic cases.
- Data Processing: [unverified] Raw attachment cleaning and imputation were not confirmed.
- Baseline: [inferred] Deterministic constrained allocation with explicit surplus accounting.
- Model: [observed] Two constrained profit-maximization formulations.
- Algorithm: [observed] Differential-evolution-enhanced genetic algorithm.
- Validation: [inferred] Replay all 12 constraint classes and compare with a deterministic solver or bound on reduced instances.
- Visualization: [inferred] Area plans and scenario-profit comparisons are useful; exact encodings were not confirmed.
- Main Result: [unverified] Profit and planting-plan values were not independently reproduced. [ev-paper-2024-c-differential-ga-planting, pp. 1-2]

### Q2

- Goal: [observed] Select a planting plan under uncertain demand, yield, cost, and price.
- Variables: [observed] Scenario parameters, crop areas, total profit, loss, and CVaR.
- Assumptions: [observed] Tail-risk preference is represented by CVaR with total profit.
- Data Processing: [unverified] Distribution calibration and scenario-generation diagnostics were not confirmed.
- Baseline: [inferred] Q1 nominal feasible plan evaluated over the same scenarios.
- Model: [observed] Risk-aware robust/stochastic allocation objective.
- Algorithm: [observed] Differential-GA search over feasible allocations.
- Validation: [observed] Four-factor uncertainty sensitivity is reported; convergence and exact-gap evidence are unverified.
- Visualization: [observed] Later figures/tables support risk and four-factor robustness comparisons.
- Main Result: [unverified] CVaR/profit values and preferred risk setting were not independently replicated. [ev-paper-2024-c-differential-ga-planting, pp. 25-30, 42]

### Q3

- Goal: [observed] Add substitute/complement and market-variable relationships to the uncertain plan.
- Variables: [observed] Crop/market relationship coefficients, scenarios, areas, profit, and CVaR.
- Assumptions: [observed] Spearman-based relationships represent crop/market dependence.
- Data Processing: [observed] Spearman correlations are introduced; estimation sample and missing-data treatment are unverified.
- Baseline: [inferred] Q2 risk-aware model without relationship terms.
- Model: [observed] Correlated uncertain allocation with tail-risk objective.
- Algorithm: [observed] Differential-GA search under the expanded scenario model.
- Validation: [inferred] Compare with a relation-free ablation and perturb correlation matrices while preserving feasibility.
- Visualization: [observed] Risk/correlation formulation and robustness outputs are displayed in later figures/tables.
- Main Result: [unverified] Correlation and strategy-gain values were not independently reproduced. [ev-paper-2024-c-differential-ga-planting, pp. 25-30, 42]

## Strong Points

- [inferred] The paper separates deterministic surplus accounting, uncertain tail risk, and correlation extensions into identifiable stages.

## Weak Points

- [unverified] Correlation calibration, scenario distributions, stochastic-search repeatability, and exact/bound comparisons were not confirmed.

## Transferable Patterns

- [expert-rule] Add CVaR only for an explicit tail-loss decision, retain a nominal feasible baseline, and test risk/correlation layers by ablation and scenario perturbation.

## Problem-Specific Tricks

- [observed] The twelve crop/land constraints and stated substitute/complement relations are tied to the supplied village planting system.
