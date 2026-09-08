---
id: 2024-b-aco-ga-monte-carlo
year: 2024
problem: B
title: 基于蚁群算法与遗传算法优化的蒙特卡洛模拟在生产决策优化中的应用研究
source_evidence: [ev-paper-2024-b-aco-ga-monte-carlo]
tags: [quality-control, acceptance-sampling, decision-tree, monte-carlo, ant-colony, genetic-algorithm, robustness]
---

# 2024 B - ACO/GA Monte Carlo production decisions

## Source and evidence quality

- Local source: `2024优秀论文/2024B 基于蚁群算法与遗传算法优化的蒙特卡洛模拟在生产决策优化中的应用研究.pdf` (28 pages).
- Evidence: `ev-paper-2024-b-aco-ga-monte-carlo`.
- [observed] Direct text extraction is readable on the reviewed abstract and model pages; page 1 was rendered for visual confirmation. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-4]

## Subproblem objectives and dependencies

- [observed] Acceptance sampling informs defect-rate treatment; binary inspection/disassembly decisions with return/disassembly feedback then flow through a small decision tree or a larger multistage decision graph. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-3, 7-9]

## Assumptions, data, and preprocessing

- [observed] The paper treats defect uncertainty through sampled scenarios and frames production choices as binary actions with return/disassembly feedback. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-3, 20-22]
- [unverified] not confirmed: a documented raw-data cleaning or missing-value procedure. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 1-4]

## Baseline, model, and algorithm

- [observed] The small-case baseline is a decision tree and expected-profit calculation; Monte Carlo/ant-colony search and genetic algorithm are used as decision-search methods for increasing problem scale. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 1, 3, 7-9]
- [inferred] A stochastic metaheuristic is structurally justified only after the exact decision-state formulation becomes too large for transparent enumeration; the paper's small-case decision tree is the relevant baseline. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 3, 7-9]

## Validation, sensitivity/robustness, and figure purposes

- [observed] A 3-sigma scenario analysis is used to examine decision changes under sampled defect uncertainty. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 20-22]
- [unverified] not confirmed: exact plot encodings, optimization convergence diagnostics, or independent out-of-sample validation. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 20-22]
- [observed] The decision-tree figures organize the small production decision branches; later result figures/tables support scenario comparison. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 3, 20-22]

## Reported results, strengths, limitations, and transferable rules

- [unverified] not confirmed: transferable sample-size thresholds, profit values, and units; the reported outputs were not independently replicated. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 1, 5-7]
- [inferred] Retaining a transparent decision-tree baseline alongside stochastic/metaheuristic search is a useful feature. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 3, 7-9]
- [inferred] Use metaheuristics only after a smaller exact decision-state baseline establishes the accounting and feasibility logic. [ev-paper-2024-b-aco-ga-monte-carlo, pp. 3, 7-9]
