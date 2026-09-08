---
id: 2024-a-objective-optimization-form
year: 2024
problem: A
title: 基于目标优化的板凳龙形态调节
source_evidence: [ev-paper-2024-a-objective-optimization-form]
tags: [geometry, kinematics, spiral, collision-detection, separating-axis-theorem, constrained-optimization]
---

# 2024 A - Objective-optimization Bench Dragon form

## Source and evidence quality

- Local source: `2024优秀论文/2024A 基于目标优化的板凳龙形态调节.pdf` (62 pages).
- Evidence: `ev-paper-2024-a-objective-optimization-form`.
- [observed] Readable text extraction and a rendered page-1 review support the abstract; the paper's later collision verification is located on pp. 28-29. [ev-paper-2024-a-objective-optimization-form, pp. 1, 16-17, 28-29]

## Subproblem objectives and dependencies

- [observed] The paper derives handle positions and speeds from an Archimedean spiral and arc-length relation first, then minimizes pitch under collision constraints and bounds leader speed under a handle-speed constraint. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]

## Assumptions, data, and preprocessing

- [observed] The model input is an Archimedean spiral, linked-bench rectangular geometry, and stated speed/collision constraints. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]
- [unverified] not confirmed: a raw-data cleaning or missing-value procedure; the targeted evidence describes deterministic geometric inputs. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]

## Baseline, model, and algorithm

- [observed] The geometry-derived arc-length recurrence along bench geometry and rectangular separating-axis collision test form the feasibility baseline for the stated constrained objectives. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]
- [inferred] This feasibility baseline is necessary because the stated objective alone does not define physical feasibility. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]

## Validation, sensitivity/robustness, and figure purposes

- [observed] The paper contains sensitivity analysis and a collision-model check. [ev-paper-2024-a-objective-optimization-form, pp. 16-17, 28-29]
- [unverified] not confirmed: individual figure encodings and table values on those pages were not transcribed in this review. [ev-paper-2024-a-objective-optimization-form, pp. 16-17, 28-29]
- [observed] Early figures support the spiral/bench geometry and collision formulation. [ev-paper-2024-a-objective-optimization-form, pp. 2-3]

## Reported results, strengths, limitations, and transferable rules

- [observed] The abstract reports a 412.47 s stopping time and a 45.04 cm minimum pitch. [ev-paper-2024-a-objective-optimization-form, p. 1]
- [unverified] The reported turnaround-length and speed numeric values are not used as cross-paper reference values: a unit inconsistency is visible in the abstract (cm/s versus the problem's m/s convention) and requires author/source reconciliation. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]
- [inferred] The full rectangular separating-axis collision formulation is a useful feature relative to a selected-corner screen, but its numerical outputs still require units auditing. [ev-paper-2024-a-objective-optimization-form, pp. 1, 3]
- [inferred] Relative to the other A cards, this collision strategy is more general geometrically but demands careful numerical/units auditing; do not compare its unverified turnaround-speed number with the other papers' values. [ev-paper-2024-a-objective-optimization-form, pp. 1-3]
