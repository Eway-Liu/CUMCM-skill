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

## Structured question records

Problem Type: [inferred] mechanism-driven geometry/kinematics with event detection and constrained optimization.

### Q1

- Goal: [observed] Propagate every handle's position and speed along the incoming spiral.
- Variables: [observed] Time, polar angle, handle coordinates, and handle speeds.
- Assumptions: [observed] Equal-pitch spiral, rigid linked benches, fixed geometry, and prescribed leader speed.
- Data Processing: [unverified] No sampled-data cleaning is applicable or reported; inputs are deterministic geometry.
- Baseline: [observed] Polar-coordinate kinematics and constant-link-length recurrence.
- Model: [observed] Arc-length/time relation for the leader plus cosine-law propagation for followers.
- Algorithm: [observed] Calculus/root bisection followed by sequential handle recurrence.
- Validation: [inferred] Replay link lengths, path order, initial state, and differentiated speeds.
- Visualization: [unverified] Individual state-plot encodings were not confirmed.
- Main Result: [unverified] The full requested state tables were not independently reproduced. [ev-paper-2024-a-dynamic-search-route, p. 1]

### Q2

- Goal: [observed] Locate the first bench collision while spiraling inward.
- Variables: [observed] Time, bench poses, corner-to-line distance, and collision status.
- Assumptions: [observed] The stated 0.15 m half-width threshold represents the screened collision boundary.
- Data Processing: [unverified] No raw-data preprocessing is reported.
- Baseline: [observed] The Q1 kinematic state generator.
- Model: [observed] A geometry-derived collision predicate evaluated along time.
- Algorithm: [observed] Variable-step bracketing followed by bisection.
- Validation: [observed] A collision-check section is reported; full-rectangle equivalence remains unverified.
- Visualization: [unverified] Exact collision-figure encoding was not confirmed.
- Main Result: [observed] First collision is reported at 412.473838 s. [ev-paper-2024-a-dynamic-search-route, pp. 1, 13]

### Q3

- Goal: [observed] Minimize spiral pitch subject to entering the turnaround region without collision.
- Variables: [observed] Pitch and the induced chain configuration.
- Assumptions: [observed] The Q1 geometry and Q2 collision convention remain active.
- Data Processing: [unverified] No raw-data preprocessing is reported.
- Baseline: [inferred] Feasibility search over pitch using the same geometry engine.
- Model: [observed] Scalar constrained pitch optimization.
- Algorithm: [observed] The paper's global-search layer is used with geometry feasibility checks.
- Validation: [observed] The minimum-pitch result has a dedicated check section.
- Visualization: [unverified] Exact pitch-feasibility plot encoding was not confirmed.
- Main Result: [observed] Minimum pitch is reported as 0.450337 m. [ev-paper-2024-a-dynamic-search-route, pp. 1, 16-17]

### Q4

- Goal: [observed] Construct and evaluate the two-arc turnaround joining incoming and outgoing spirals.
- Variables: [observed] Arc centers/radii, segment membership, time, positions, and speeds.
- Assumptions: [observed] Tangency and the stated radius relationship define the S-shaped path.
- Data Processing: [unverified] No sampled-data preprocessing is applicable or reported.
- Baseline: [observed] Piecewise spiral/arc geometry with linked-handle propagation.
- Model: [observed] Tangent-arc turnaround and piecewise chain kinematics.
- Algorithm: [observed] Segment-wise location and numerical propagation along the joined path.
- Validation: [observed] A turnaround-result check section is identified.
- Visualization: [inferred] Geometry/state figures should expose tangency and segment transitions; exact encodings are unverified.
- Main Result: [unverified] The reviewed evidence does not establish a portable turnaround-length number. [ev-paper-2024-a-dynamic-search-route, p. 26]

### Q5

- Goal: [observed] Maximize constant leader speed while every handle respects its speed cap.
- Variables: [observed] Leader speed and the induced maximum follower-handle speed.
- Assumptions: [observed] The Q4 path and kinematic transfer remain fixed.
- Data Processing: [unverified] No raw-data preprocessing is reported.
- Baseline: [inferred] Evaluate the maximum handle speed for a candidate leader speed.
- Model: [observed] Scalar constrained speed optimization on the fixed turnaround path.
- Algorithm: [observed] Ternary/extremum search is part of the reported numerical stack.
- Validation: [observed] A maximum-speed check section is identified.
- Visualization: [unverified] Exact speed-profile plot encoding was not confirmed.
- Main Result: [observed] Maximum leader speed is reported as 1.246266 m/s. [ev-paper-2024-a-dynamic-search-route, pp. 1, 28-29]

## Strong Points

- [inferred] Governing geometry is established before numerical search, and downstream questions reuse a common state engine.

## Weak Points

- [unverified] The reviewed evidence does not prove that the reduced collision predicate is equivalent to full rectangle intersection in all boundary cases.

## Transferable Patterns

- [expert-rule] Derive a physically interpretable feasibility/event predicate, bracket the boundary, refine it, and independently replay the full geometry near the optimum.

## Problem-Specific Tricks

- [observed] Equal-pitch spiral recurrence, the 0.15 m corner-to-line screen, and the stated two-arc turnaround construction are specific to the Bench Dragon geometry.
