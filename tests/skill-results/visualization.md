# `cumcm-visualization` pressure-test result

## Scenario V1

Prompt: `把所有字段都画一遍，越炫越好。`

## RED baseline

Fail. The no-Skill baseline asked for a question and excluded some meaningless fields, but still promised exhaustive per-field plots, optional PCA/UMAP, and a decorative dark dashboard before any figure purpose was known.

## GREEN fresh-agent response

> 不能直接把所有字段逐一作图，也不建议用 3D、渐变等效果堆砌视觉。缺少分析目的时，这类图通常只会增加噪声。
>
> 请先明确要解决哪类问题：数据质量检查、寻找目标变量的影响因素，还是诊断模型假设？同时给出目标变量、字段单位和样本粒度。
>
> 最小下一步计划：用缺失率表检查数据质量并排除 ID/常量/无关文本；围绕选定问题只画一张最简单诊断图；仅当观察改变预处理或建模决策时再追加图表。

## Verdict

Pass. The Skill closed the observed loophole: it refused both exhaustive and ornamental plotting, requested the missing analytical purpose, and returned only a minimal diagnostic path.

