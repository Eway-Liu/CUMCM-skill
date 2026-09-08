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

- Local source: `2024优秀论文/2024C 基于差分遗传算法的农作物种植策略优化.pdf` (61 pages).
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
