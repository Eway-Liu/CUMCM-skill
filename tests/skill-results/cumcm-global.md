# `cumcm-global` pressure-test result

## Scenario O1

Same prompt as `tests/pressure-scenarios/scenarios.md`: given a four-question CUMCM problem and Excel attachments, state the first-round output and the gates for code, figures, and thesis finalization.

## RED baseline

The no-Skill baseline passed. It proposed problem/data/dependency/model-route outputs and distinct gates. There was no observed orchestrator failure to invent or encode.

## GREEN fresh-agent observation

The evaluator loaded `cumcm-global` in a fresh context and produced:

- a source inventory with unresolved gaps;
- one `PROBLEM BRIEF` per question;
- a `QUESTION GRAPH` with hard/soft/independent dependencies and named transferred artifacts;
- structure-based classification and specialist routing;
- a code gate requiring mathematical formalization and baseline reasoning;
- a figure gate requiring a question, verified artifact, message, variables, units and format;
- a thesis gate requiring validated, traceable model/result/figure evidence;
- a `FINAL CONSISTENCY REVIEW` covering model, code, result, figure, text, units, symbols, parameters and conclusion evidence.

## Verdict

Pass. The Skill preserved the already-good baseline behavior, made the contracts observable, and did not jump to code or prescribe a historical model. No new rationalization was observed, so no extra prohibition was added.

