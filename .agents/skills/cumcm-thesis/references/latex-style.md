# LaTeX style

- Use `equation` for one numbered relation and `align` for multi-line derivations; align meaningful equality/inequality signs.
- Use `cases` for piecewise definitions and standard matrix environments for vectors/matrices.
- Define symbols in prose or a compact notation table; include units outside math symbols where practical.
- Use `\label` and `\ref`/`\eqref`; do not hardcode equation, figure or table numbers.
- Put table units in column headers and captions; use consistent significant digits.
- Put figure meaning and context in the caption rather than repeating a decorative chart title.
- Escape text characters and use `\mathrm{}`/`\text{}` for words inside equations.
- Keep displayed equations syntactically complete and directly insertable; do not mix Markdown math fences into LaTeX source.

Example:

```latex
\begin{equation}
  \min_{x} \; c^{\mathsf T}x
  \quad \text{s.t.} \quad Ax \le b,\; x \in \mathbb{Z}_{+}^{n}.
  \label{eq:allocation}
\end{equation}
```

