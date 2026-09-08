---
id: 2024-c-ga-planting
year: 2024
problem: C
title: 基于遗传算法的最优种植策略
source_evidence: [ev-paper-2024-c-ga-planting]
tags: [allocation-optimization, crop-planning, genetic-algorithm, uncertainty, crop-interactions]
---

# 2024 C - Genetic-algorithm crop planting

## Source and evidence quality

- Local source: `2024优秀论文/2024C 基于遗传算法的最优种植策略.pdf` (45 pages).
- Evidence: `ev-paper-2024-c-ga-planting`.
- [observed] Readable page-aware extraction and a rendered page-1 review support the abstract. [ev-paper-2024-c-ga-planting, pp. 1-3]

## Subproblem objectives and dependencies

- [observed] The paper allocates crop areas by year/plot under land, rotation, legume, concentration, season, and crop-environment constraints for two surplus-sale scenarios, then changes yields under drought/cold-wave factors and finally introduces substitute/complement crop relationships. [ev-paper-2024-c-ga-planting, pp. 1-3]

## Assumptions, data, and preprocessing

- [observed] Inputs include crop area by year/plot and land, rotation, legume, concentration, season, crop-environment, demand-price-cost, and crop-relation assumptions. [ev-paper-2024-c-ga-planting, pp. 1-3]
- [unverified] not confirmed: raw-data cleaning, imputation, or empirical calibration of the stated crop relationships. [ev-paper-2024-c-ga-planting, pp. 1-3]

## Baseline, model, and algorithm

- [observed] The constrained two-scenario planting formulation is optimized by a genetic algorithm, with profit-volatility selection used in the uncertainty extension. [ev-paper-2024-c-ga-planting, pp. 1-3]
- [inferred] The crop-interaction extension requires externally defensible relation parameters; simulated input cannot itself validate a real price-elasticity claim. [ev-paper-2024-c-ga-planting, pp. 1-3]

## Validation, sensitivity/robustness, and figure purposes

- [observed] Weather-factor changes and a profit-volatility indicator provide the paper's stated uncertainty/robustness extension. [ev-paper-2024-c-ga-planting, pp. 1-3]
- [unverified] not confirmed: a formal sensitivity grid, convergence evidence, figure/table encodings, or out-of-sample validation. [ev-paper-2024-c-ga-planting, pp. 1-3]
- [observed] The early model figures/tables organize constraints and scenario formulations rather than independently validating causal crop relations. [ev-paper-2024-c-ga-planting, pp. 1-3]

## Reported results, strengths, limitations, and transferable rules

- [unverified] not confirmed: numerical profits, comparative superiority, and units as transferable results. [ev-paper-2024-c-ga-planting, p. 1]
- [inferred] The staged extension from feasible allocation to weather uncertainty and crop interactions is a useful feature. [ev-paper-2024-c-ga-planting, pp. 1-3]
- [inferred] Treat assumed substitute/complement relations as scenario inputs unless external data identifies and validates their magnitude. [ev-paper-2024-c-ga-planting, pp. 1-3]
