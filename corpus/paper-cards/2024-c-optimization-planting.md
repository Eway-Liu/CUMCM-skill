---
id: 2024-c-optimization-planting
year: 2024
problem: C
title: 基于优化算法的农作物最优种植模型
source_evidence: [ev-paper-2024-c-optimization-planting]
tags: [allocation-optimization, crop-planning, land-use, robust-optimization, scenario-analysis]
---

# 2024 C - Optimization-model crop planting

## Source and evidence quality

- Local source: `2024优秀论文/2024C 基于优化算法的农作物最优种植模型.pdf` (49 pages).
- Evidence: `ev-paper-2024-c-optimization-planting`.
- [observed] Page-aware text extraction is readable on the abstract and problem formulation; rendered page 1 was reviewed. [ev-paper-2024-c-optimization-planting, pp. 1-3]

## Subproblem objectives and dependencies

- [observed] The paper first allocates crop area by year and plot under land type, area, non-replanting, three-year legume, dispersion, and minimum-area constraints for two surplus-sale objectives, then evaluates feasible plans under uncertain demand, yield, cost, and price. [ev-paper-2024-c-optimization-planting, pp. 1-3]

## Assumptions, data, and preprocessing

- [observed] Inputs comprise plot/year crop areas and land-type, area, rotation, legume, dispersion, and minimum-area constraints. [ev-paper-2024-c-optimization-planting, pp. 1-3]
- [unverified] not confirmed: a raw attachment-data cleaning, imputation, or feature-engineering procedure. [ev-paper-2024-c-optimization-planting, pp. 1-3]

## Baseline, model, and algorithm

- [observed] The fixed-parameter constrained planting plan is the baseline; the extension evaluates generated uncertainty states and later selects by a worst-case-style criterion. [ev-paper-2024-c-optimization-planting, pp. 1-3, 27]
- [inferred] Uncertainty handling belongs after feasibility and accounting conventions have been made explicit. [ev-paper-2024-c-optimization-planting, pp. 1-3]

## Validation, sensitivity/robustness, and figure purposes

- [observed] The paper reports sensitivity analysis and a robust-selection section. [ev-paper-2024-c-optimization-planting, pp. 18, 27]
- [unverified] not confirmed: exact sensitivity ranges, visual encodings, scenario-generation diagnostics, or independent outcome validation. [ev-paper-2024-c-optimization-planting, pp. 18, 27]
- [observed] Formulation figures/tables organize land and constraint inputs; later outputs support sensitivity and robust-plan comparison. [ev-paper-2024-c-optimization-planting, pp. 1-3, 18, 27]

## Reported results, strengths, limitations, and transferable rules

- [unverified] not confirmed: seven-year revenue values, currency units, and solver optimality as portable results. [ev-paper-2024-c-optimization-planting, p. 1]
- [inferred] Clearly separating surplus-price assumptions before adding uncertainty and robustness is a useful feature. [ev-paper-2024-c-optimization-planting, pp. 1-3, 27]
- [inferred] For allocation models, establish feasible accounting under each market convention before comparing robust selections. [ev-paper-2024-c-optimization-planting, pp. 1-3]
