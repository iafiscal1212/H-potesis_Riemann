# Results - adaptive heat-flow quadrature

## Experiment

Script:

```text
experiments/adaptive_heat_flow_quadrature.py
```

For each deformation parameter `t`, this experiment rebuilds the moments

```math
m_k(t)=\int_{-\infty}^{\infty}x^k e^{t x^2}\Phi(|x|)dx,
```

then constructs a new Jacobi matrix and a new Gaussian quadrature rule.

The approximant is

```math
\Xi_{N,t}^{adaptive}(z)=\frac12\sum_j w_j(t)\cos(zx_j(t)).
```

## Purpose

This corrects the earlier fixed-node deformation, where only the weights were changed.

## Initial scan

A private numerical scan was run for small `N` and moderate `t`.

Representative detected non-real roots:

```text
N=6:
  t=-2 -> z ~= 25.8801 + 8.8704 i
  t=-1 -> z ~= 25.6925 + 8.7300 i
  t= 0 -> z ~= 25.5058 + 8.5874 i
  t= 1 -> z ~= 25.3201 + 8.4427 i
  t= 2 -> z ~= 25.1356 + 8.2959 i
  t= 5 -> z ~= 24.5914 + 7.8424 i

N=8:
  t=-2 -> z ~= 30.8012 + 6.1040 i
  t=-1 -> z ~= 30.7068 + 5.8413 i
  t= 0 -> z ~= 29.9433 + 6.2024 i
  t= 1 -> z ~= 29.7537 + 6.0429 i
  t= 2 -> z ~= 29.5687 + 5.8838 i
  t= 5 -> z ~= 29.0406 + 5.4167 i
```

## Observation

The adaptive deformation is more faithful than fixed-node reweighting, but it still does not produce all-real zeros for the tested finite approximants.

The detected complex zeros move smoothly as `t` varies, but they do not collapse to the real axis in the tested range.

## Interpretation

This suggests that finite Gaussian quadrature approximants are not the right objects for reproducing the de Bruijn-Newman real-zero transition.

The actual de Bruijn-Newman theorem concerns the continuous transform, not arbitrary finite quadrature approximants.

## Consequence

The route

```math
Phi -> adaptive moments -> finite Gaussian quadrature -> real-rooted approximants
```

is not supported by the current experiment.

## Remaining value

The adaptive quadrature remains useful for approximating deformed transforms numerically, but not as a direct Laguerre-Polya proof mechanism.

## Decision

Downgrade the quadrature-real-rootedness route.

Return priority to:

1. Herglotz/Pick positivity of `-Xi'/Xi`;
2. de Branges/Hermite-Biehler construction from a one-sided transform;
3. canonical systems or resolvent models.

## Status

`fallo-detectado` for adaptive finite quadrature as a real-rooted approximant family.
