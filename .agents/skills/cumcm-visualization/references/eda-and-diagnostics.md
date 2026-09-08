# EDA and diagnostics

EDA is a question loop:

```text
data concern or modeling hypothesis -> plot -> observation -> decision -> next check
```

Useful mappings:

- Missingness: compact missing-count/rate table; heatmap only when co-occurrence pattern matters.
- Outliers/distribution: histogram or ECDF plus boxplot when comparing groups.
- Suspected nonlinearity: scatter with restrained smoother and observation grain stated.
- Heteroscedasticity: residuals versus fitted and scale-location view.
- Temporal pattern: time plot, seasonal subseries, ACF only when lag structure is the question.
- Class imbalance: counts/rates with the denominator.
- Spatial relation: map only when coordinates and geographic adjacency matter.

Exclude identifiers, constants and free text unless their quality is the question. Do not automatically plot every variable or every pair. Document what each retained EDA figure changed in preprocessing, formulation, feature design or validation.

