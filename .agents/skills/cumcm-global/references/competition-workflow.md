# Competition workflow

Use the shortest path that satisfies the user's requested stage. For an end-to-end task, preserve this dependency order:

| Stage | Required output | Exit evidence |
|---|---|---|
| 0. Read materials | Source inventory and gaps | All supplied statements and attachment instructions inspected |
| 1. Structure problem | `PROBLEM BRIEF` | Inputs, outputs, variables, objectives, constraints, units |
| 2. Link questions | `QUESTION GRAPH` | Shared data, parameters, code and result dependencies |
| 3. Audit data | Data profile and EDA questions | Schema, quality, sampling and leakage risks |
| 4. Formalize | Equations and feasible set | Every symbol and modeling assumption defined |
| 5–7. Compare models | Candidates, baseline, main model | Choice tied to structure, data and validation |
| 8–10. Solve and test | Saved results and checks | Feasibility, error, sensitivity and robustness evidence |
| 11. Visualize | Figure manifest | Each figure answers a named question |
| 12. Write | Traceable manuscript | Claims and numbers point to verified artifacts |
| 13. Review | `FINAL CONSISTENCY REVIEW` | Cross-artifact checks completed |

If the user asks only for plotting, writing, or review, begin there after checking that its input contract is present. Missing upstream evidence is a limitation to surface, not a reason to fabricate it.

