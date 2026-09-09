# LaTeX 排版规范

- 单个带编号关系式使用 `equation`，多行推导使用 `align`；在有实际意义的等号或不等号处对齐。
- 分段定义使用 `cases`，向量和矩阵使用标准矩阵环境。
- 在正文或紧凑的符号表中定义符号；条件允许时，将单位写在数学符号之外。
- 使用 `\label` 和 `\ref`/`\eqref` 交叉引用，不要硬编码公式、图或表的编号。
- 表格单位写在列标题或表注中，并统一有效数字位数。
- 图注应交代图形含义和情境，不要重复装饰性图标题。
- 对文本特殊字符进行转义，公式中的文字使用 `\mathrm{}` 或 `\text{}`。
- 展示公式必须语法完整且可直接插入 LaTeX 源文件；不要在 LaTeX 源码中混用 Markdown 数学围栏。

示例：

```latex
\begin{equation}
  \min_{x} \; c^{\mathsf T}x
  \quad \text{s.t.} \quad Ax \le b,\; x \in \mathbb{Z}_{+}^{n}.
  \label{eq:allocation}
\end{equation}
```
