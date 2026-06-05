# Via 5-8 - Finite heat-flow approximants

## Classification

`experimental-bridge` + `deformation-route`

## Motivation

The Gaussian-quadrature approximants

```math
Xi_N(z)=\frac12\sum_{j=1}^{N}w_j\cos(zx_j)
```

approximate `Xi(z)` but have non-real zeros for several tested `N`.

This kills the direct Laguerre-Polya approximation route.

However, the de Bruijn-Newman philosophy suggests studying a heat-flow deformation.

## Continuous model

The deformed family has the schematic form

```math
H_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(zu)du.
```

For sufficiently large deformation parameter, zeros become real. The RH question corresponds to the boundary value at the original function.

## Finite model

For quadrature approximants, define

```math
Xi_{N,t}(z)=\frac12\sum_{j=1}^{N}w_j e^{t x_j^2}\cos(zx_j).
```

This is a finite cosine/exponential sum.

## Experimental question

For each `N`, estimate a threshold `t_N` such that:

```math
Xi_{N,t}(z) \text{ has only real zeros for } t >= t_N.
```

and has non-real zeros for `t < t_N`.

## Why this matters

If `t_N` tends toward a limiting value related to the de Bruijn-Newman constant, the finite approximants may provide a non-circular laboratory for studying the transition to real-rootedness.

## Warning

This is not a proof of RH.

Even if `t_N <= 0` for many `N`, this would remain finite numerical evidence.

## First experiment

Create:

```text
experiments/finite_heat_flow_quadrature.py
```

Tasks:

1. construct quadrature nodes and weights;
2. define `Xi_{N,t}`;
3. scan for non-real zeros;
4. estimate a rough threshold for small `N`;
5. compare with direct `t=0` failures.

## Expected difficulty

Finite cosine sums can have complex zero patterns. Root scans may miss zeros. Results must be treated as exploratory.
