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

- Historical source identity: `2024优秀论文/2024C 基于优化算法的农作物最优种植模型.pdf` (49 pages; raw PDF removed after distillation).
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

## Structured question records

Problem Type: [inferred] deterministic multi-period allocation followed by sensitivity and robust scenario selection.

### Q1

- Goal: [observed] Optimize 2024–2030 crop plans under waste and half-price surplus conventions.
- Variables: [observed] Crop area by plot/year/season and associated production, sales, and profit.
- Assumptions: [observed] Land type, area, non-replanting, three-year legume, dispersion, and minimum-area constraints apply.
- Data Processing: [unverified] Raw attachment cleaning, imputation, and feature engineering were not confirmed.
- Baseline: [observed] Fixed-parameter constrained planting plan.
- Model: [observed] Two deterministic profit-maximization formulations with different surplus accounting.
- Algorithm: [unverified] The reviewed evidence does not establish a portable solver recipe or optimality certificate.
- Validation: [inferred] Replay every operational constraint and reconcile revenue under both surplus conventions.
- Visualization: [observed] Formulation figures/tables organize land and constraint inputs.
- Main Result: [unverified] Seven-year revenue and planting-plan values were not independently reproduced. [ev-paper-2024-c-optimization-planting, pp. 1-3]

### Q2

- Goal: [observed] Evaluate and select plans under uncertain demand, yield, cost, and price.
- Variables: [observed] Uncertain economic/yield factors, crop areas, scenario profit, and robust criterion.
- Assumptions: [observed] Generated uncertainty states represent the stated parameter ranges.
- Data Processing: [unverified] Scenario-generation diagnostics and empirical distribution support were not confirmed.
- Baseline: [inferred] Q1 nominal plan evaluated over the identical scenario set.
- Model: [observed] Scenario evaluation with a worst-case-style robust selection.
- Algorithm: [observed] Generate/evaluate feasible uncertainty states and select by the robust criterion.
- Validation: [observed] Sensitivity analysis and a robust-selection section are reported.
- Visualization: [observed] Later outputs support sensitivity and robust-plan comparison.
- Main Result: [unverified] Robust-plan revenue and dominance claims were not independently reproduced. [ev-paper-2024-c-optimization-planting, pp. 18, 27]

### Q3

- Goal: [observed] Add crop substitution/complementarity and market-variable relationships, then compare with Q2.
- Variables: [observed] Relationship parameters, uncertain inputs, crop areas, and scenario profit.
- Assumptions: [unverified] The reviewed evidence does not confirm empirical calibration of every relationship.
- Data Processing: [unverified] Correlation estimation and relationship-data preparation were not confirmed.
- Baseline: [inferred] Q2 robust model without the relationship layer.
- Model: [inferred] Correlated/interaction-aware scenario allocation built on the Q2 feasibility rules.
- Algorithm: [inferred] Re-evaluate feasible plans under related parameter scenarios.
- Validation: [inferred] Compare against a relation-free ablation and perturb relationship signs/magnitudes.
- Visualization: [inferred] Q2-versus-Q3 plan/profit comparisons are relevant; exact encodings were not confirmed.
- Main Result: [unverified] Relationship-driven strategy changes were not independently verified. [ev-paper-2024-c-optimization-planting, pp. 1-3, 27]

## Strong Points

- [inferred] Surplus-sale conventions are separated before uncertainty and robustness are introduced.

## Weak Points

- [unverified] Solver optimality, scenario calibration, exact sensitivity ranges, and Q3 relationship evidence were not confirmed.

## Transferable Patterns

- [expert-rule] Keep feasibility and accounting identical when comparing nominal, sensitivity, and robust plans so that differences isolate uncertainty treatment.

## Problem-Specific Tricks

- [observed] The exact land-type, rotation, legume-window, dispersion, and minimum-area rules belong to the supplied village data.
