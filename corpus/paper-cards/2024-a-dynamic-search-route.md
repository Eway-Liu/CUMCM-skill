---
id: 2024-a-dynamic-search-route
year: 2024
problem: A
title: 基于动态搜索的“板凳龙”运动状态及路线研究
source_evidence: [ev-paper-2024-a-dynamic-search-route]
tags: [geometry, kinematics, spiral, collision-detection, numerical-search, particle-swarm]
---

# 2024 A - Dynamic-search Bench Dragon route study

## Source and evidence quality

- Local source: `2024优秀论文/2024A 基于动态搜索的“板凳龙”运动状态及路线研究.pdf` (58 pages).
- Evidence: `ev-paper-2024-a-dynamic-search-route`.
- [observed] Native macOS PDFKit page-by-page extraction recovers readable Chinese directly from the PDF text layer. The separate bundled renderer still omits CJK glyphs on p. 1, so equations/tables were not reconstructed from that render. [ev-paper-2024-a-dynamic-search-route, pp. 1, 13, 16-17, 26, 28-29]

## Subproblem objectives and dependencies

- [observed] The paper chains polar-coordinate state propagation, first-collision time, minimum pitch, tangent-arc turnaround, and maximum speed; each optimization uses the preceding kinematic and geometric predicates. [ev-paper-2024-a-dynamic-search-route, pp. 1, 13, 16-17, 26, 28-29]

## Assumptions, data, and preprocessing

- [observed] The setup uses equal-pitch spiral geometry, fixed bench geometry, a 0.15 m half-width collision threshold, and a leader-speed ceiling. [ev-paper-2024-a-dynamic-search-route, p. 1]
- [unverified] not confirmed: an external-data cleaning or missing-value treatment; the reviewed evidence presents a deterministic geometric input rather than a sampled dataset. [ev-paper-2024-a-dynamic-search-route, p. 1]

## Baseline, model, and algorithm

- [observed] The baseline mechanism is polar-coordinate kinematics: calculus/bisection obtains leader angle, cosine-law propagation obtains chain positions, and differentiation obtains speeds. Variable-step bracketing/bisection, particle swarm, and ternary search are layered on the resulting feasibility or extrema calculations. [ev-paper-2024-a-dynamic-search-route, pp. 1, 13, 16-17, 26, 28-29]
- [inferred] The numerical layers fit because the geometry supplies feasibility/collision predicates; they do not replace the governing kinematic relations. [ev-paper-2024-a-dynamic-search-route, pp. 1, 13, 16-17]

## Validation, sensitivity/robustness, and figure purposes

- [observed] The cited validation sections respectively check collision, minimum pitch, turnaround, and maximum-speed outputs. [ev-paper-2024-a-dynamic-search-route, pp. 13, 16-17, 26, 28-29]
- [unverified] not confirmed: a systematic parameter-sensitivity or stochastic robustness analysis. [ev-paper-2024-a-dynamic-search-route, pp. 13, 16-17, 26, 28-29]
- [unverified] not confirmed: individual figure captions/purposes where the alternate renderer does not map the CJK glyphs; the text identifies the validation sections but not every visual encoding. [ev-paper-2024-a-dynamic-search-route, pp. 13, 16-17, 26, 28-29]

## Reported results, strengths, limitations, and transferable rules

- [observed] The abstract reports first collision at 412.473838 s, a minimum pitch of 0.450337 m, and a maximum leader speed of 1.246266 m/s. [ev-paper-2024-a-dynamic-search-route, p. 1]
- [inferred] The explicit numerical validation trail for each geometric decision is a useful modeling feature. [ev-paper-2024-a-dynamic-search-route, pp. 13, 16-17, 26, 28-29]
- [inferred] A transferable rule is to derive an interpretable geometry-based feasibility predicate first, then choose a bracketed or global search appropriate to the remaining scalar or nonconvex decision. [ev-paper-2024-a-dynamic-search-route, pp. 1, 13, 16-17]
