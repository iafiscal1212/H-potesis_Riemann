# Results - finite heat-flow quadrature approximants

## Experiment

Script:

```text
experiments/finite_heat_flow_quadrature.py
```

Finite deformation:

```math
\Xi_{N,t}(z)=\frac12\sum_{j=1}^{N} w_j e^{t x_j^2}\cos(zx_j),
```

where `x_j,w_j` are Gaussian quadrature nodes and weights for the even measure `Phi(|x|)`.

## Motivation

This was designed as a finite analogue of the de Bruijn-Newman deformation:

```math
H_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(zu)du.
```

## Initial scan

Tested:

```text
N in {6,8,10}
t in {-20,-10,-5,-2,-1,0,1,2,5,10,20}
```

The scan counted non-real roots found by a coarse root search in a finite box.

## Observation

The finite deformation does not show a clean transition to all-real zeros in this naive implementation.

Non-real zeros persist for several positive values of `t` in the finite approximants.

## Interpretation

The direct deformation

```math
w_j -> w_j e^{t x_j^2}
```

inside a fixed quadrature rule is probably not the correct finite analogue of the de Bruijn-Newman flow.

Reason: the true deformation changes the continuous weight before quadrature. A fixed quadrature rule for `Phi` is not necessarily a good quadrature rule for `e^{t u^2}Phi(u)`.

## Consequence

Do not infer anything about the actual de Bruijn-Newman constant from this finite fixed-node experiment.

## Better next experiment

For each `t`, construct a new moment sequence

```math
m_k(t)=\int_{-\infty}^{\infty}x^k e^{t x^2}\Phi(|x|)dx
```

then build a new Jacobi matrix and new Gaussian quadrature rule for the deformed measure.

This gives:

```math
\Xi_{N,t}^{adaptive}(z)=\frac12\sum_j w_j(t)\cos(zx_j(t)).
```

This is a more faithful finite analogue.

## Status

`fallo-detectado` for fixed-node finite heat deformation.

The deformation route remains open with adaptive moments.
