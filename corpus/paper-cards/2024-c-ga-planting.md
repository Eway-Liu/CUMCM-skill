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

- Historical source identity: `2024优秀论文/2024C 基于遗传算法的最优种植策略.pdf` (45 pages; raw PDF removed after distillation).
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

## Structured question records

Problem Type: [inferred] multi-period constrained crop allocation with weather and crop-interaction scenarios.

### Q1

- Goal: [observed] Optimize crop areas for waste and half-price surplus-sales cases.
- Variables: [observed] Area by crop, plot, season, and year plus production, sales, and profit.
- Assumptions: [observed] Land, rotation, legume, concentration, season, and crop-environment constraints hold.
- Data Processing: [unverified] Raw workbook cleaning and imputation were not confirmed.
- Baseline: [inferred] Deterministic feasible allocation under explicit surplus accounting.
- Model: [observed] Constrained multi-period profit maximization for two market cases.
- Algorithm: [observed] Genetic algorithm.
- Validation: [inferred] Replay all land/rotation/legume/season constraints and compare with an exact or relaxed bound where possible.
- Visualization: [observed] Early figures/tables organize the constraints and scenario formulations.
- Main Result: [unverified] Numerical plan and profit values were not independently reproduced. [ev-paper-2024-c-ga-planting, pp. 1-3]

### Q2

- Goal: [observed] Account for market changes and weather-driven yield uncertainty.
- Variables: [observed] Crop areas, demand/price/cost/yield scenarios, profit, and profit volatility.
- Assumptions: [observed] Drought/cold-wave factors modify yields and a volatility indicator represents risk.
- Data Processing: [unverified] Weather-factor calibration and scenario distributions were not confirmed.
- Baseline: [inferred] Q1 nominal plan evaluated under the same weather/market scenarios.
- Model: [observed] Scenario allocation with profit-volatility selection.
- Algorithm: [observed] Genetic-algorithm search under perturbed inputs.
- Validation: [observed] Weather-factor changes and profit volatility are examined; repeatability and exact-gap evidence are unverified.
- Visualization: [inferred] Scenario profit and area-change comparisons are relevant; exact encodings were not confirmed.
- Main Result: [unverified] Risk-adjusted plan and comparative profits were not independently reproduced. [ev-paper-2024-c-ga-planting, pp. 1-3]

### Q3

- Goal: [observed] Include substitute/complement crop relations and coupled market changes.
- Variables: [observed] Relationship parameters, uncertain inputs, crop areas, and profit.
- Assumptions: [observed] Stated substitute/complement relations govern the scenario extension.
- Data Processing: [unverified] Empirical identification or calibration of relationship magnitudes was not confirmed.
- Baseline: [inferred] Q2 model with relationship terms removed.
- Model: [observed] Interaction-aware uncertain planting allocation.
- Algorithm: [observed] Genetic-algorithm search with the expanded assumptions.
- Validation: [inferred] Run a relation-term ablation and perturb assumed relationship strength/sign.
- Visualization: [observed] Early model figures/tables organize the interaction scenario rather than validate causality.
- Main Result: [unverified] Interaction-driven numerical improvement was not independently verified. [ev-paper-2024-c-ga-planting, pp. 1-3]

## Strong Points

- [inferred] The solution extends a feasible allocation in stages from market accounting to weather uncertainty and crop interactions.

## Weak Points

- [unverified] The causal or empirical basis of crop relations, sensitivity grid, GA convergence, and repeated-seed evidence were not confirmed.

## Transferable Patterns

- [expert-rule] Treat uncalibrated relationships as scenarios, not facts, and use a relation-free ablation before attributing gains to the interaction mechanism.

## Problem-Specific Tricks

- [observed] Drought/cold-wave yield factors and the selected substitute/complement crop pairs are case-specific scenario assumptions.
