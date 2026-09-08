# Abstract and problem analysis

## Abstract

Use a cohesive evidence chain:

```text
overall real problem and objective
-> shared mathematical structure or dependency
-> method choices tied to that structure
-> targeted extension tied to a baseline defect
-> verified key results with units
-> validation and practical conclusion
```

Adapt the number and order of sentences to the actual question graph. Avoid mechanical repetition of “针对问题一/二/三/四”. Do not list interchangeable model families or assume every four-question problem follows data cleaning -> prediction -> optimization -> robustness.

If verified results are absent, write a blueprint that names the missing artifact rather than claiming “提升/降低/更优”. Example placeholder: `[由 outputs/metrics.json 的 test_rmse 写入，单位：mm]`.

## Problem restatement and analysis

Restatement translates reality into mathematical objects, inputs, outputs and constraints; it does not copy the prompt.

Analysis answers “why this formulation and route?” Use visible evidence: data pattern, physical relation, decision structure, constraint type, uncertainty or question dependency. Each paragraph should connect a problem feature to a modeling consequence. “根据题意建立模型” contains no analysis.

