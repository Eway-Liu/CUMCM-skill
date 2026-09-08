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

- Local source: `2024优秀论文/2024B 基于多阶段模拟仿真的生产决策问题.pdf` (70 pages).
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
