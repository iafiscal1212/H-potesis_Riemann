# Results - zeros of Gaussian-quadrature approximants

## Experiment

Script:

```text
experiments/quadrature_zeros_scan.py
```

Approximants:

```math
\Xi_N(z)=\frac12\sum_{j=1}^{N}w_j\cos(zx_j),
```

where `x_j,w_j` are Gaussian quadrature nodes and weights for the even measure

```math
w(x)=\Phi(|x|).
```

## Question

Do the finite approximants `Xi_N` have only real zeros?

If yes, and if `Xi_N -> Xi` locally uniformly, this would support a Laguerre-Polya route.

## Result

The direct approximants fail real-rootedness.

A numerical root scan found non-real zeros for several values of `N`.

Representative roots:

```text
N=4:
  real roots found near:
    20.3087418713
    60.9255167188
  no non-real roots found in the first coarse scan.

N=6:
  real roots near:
    24.5449941897
    73.6950596203
  non-real roots near:
    25.5058113166 +/- 8.5874254871 i
    76.4789193783 +/- 8.6435991461 i

N=8:
  real root near:
    27.3743146930
  non-real root detected near:
    29.9433077039 + 6.2023700350 i

N=10:
  real root near:
    28.2271262920
  non-real roots near:
    34.2366675888 +/- 4.401874865 i
```

## Interpretation

The direct Gaussian-quadrature approximants

```math
\Xi_N(z)=\frac12\sum_j w_j\cos(zx_j)
```

are useful approximants to the cosine transform, but they do not appear to belong to the Laguerre-Polya class.

Therefore the direct claim

```math
\Xi_N \text{ has only real zeros for all } N
```

is false or at least not supported by the numerical scan.

## Consequence

This discards a clean approximation route:

```math
\Phi \to moments \to Gaussian quadrature \to real-rooted \Xi_N \to RH.
```

The obstruction is finite exponential/cosine sums: positive weights and real nodes do not guarantee real zeros.

## Remaining value

The construction remains useful because:

1. it is non-circular;
2. it approximates `Xi` well on real intervals;
3. it produces finite self-adjoint Jacobi matrices from `Phi`;
4. it may be modified by stabilization, heat flow, or de Branges/canonical-system structure.

## Next directions

1. Apply heat-flow deformation to the approximants and test whether zeros become real above a threshold.
2. Search for stable-polynomial modifications of the quadrature approximants.
3. Return to Herglotz/Pick kernel positivity, which remains more promising than direct real-rooted approximants.
4. Investigate one-sided transform / Hermite-Biehler construction instead of symmetric cosine-sum truncation.

## Status

`fallo-detectado` for direct real-rootedness of Gaussian-quadrature approximants.

This is a productive negative result.
