# Via 3-4 - One-sided transform route

## Classification

`candidate-framework` + `de-branges-route`

## Motivation

The derivative candidate

```math
E_a(z)=Xi(z)+i a Xi'(z)
```

shows the correct Hermite-Biehler orientation numerically for sampled points, but it is artificial unless derived from a natural structure.

A more natural source is the one-sided transform of the Riemann kernel.

## Symmetric transform

The Xi function is represented as a cosine transform:

```math
Xi(z)=\int_0^\infty Phi(u)cos(zu)du.
```

Equivalently, using an even extension,

```math
Xi(z)=\frac12\int_{-\infty}^{\infty}Phi(|u|)e^{izu}du.
```

## One-sided transform candidate

Define

```math
E(z)=\int_0^\infty Phi(u)e^{izu}du.
```

Then

```math
E(z)=A(z)+iB(z)
```

where

```math
A(z)=\int_0^\infty Phi(u)cos(zu)du=Xi(z)
```

and

```math
B(z)=\int_0^\infty Phi(u)sin(zu)du.
```

Thus `Xi` is the real component of a natural one-sided transform.

## Hermite-Biehler target

If `E` is Hermite-Biehler, then its real and imaginary parts have real interlacing zeros under standard conditions.

In particular, `A(z)=Xi(z)` would have only real zeros.

Therefore:

```math
E(z)=\int_0^\infty Phi(u)e^{izu}du \text{ Hermite-Biehler}
```

would imply RH.

## Why this is promising

This construction is natural and non-circular:

- it uses `Phi` directly;
- it does not use zeros;
- it resembles Fourier-Laplace transforms of positive kernels;
- it connects de Branges theory with the integral representation of `Xi`.

## Potential obstruction

A one-sided transform of a positive function is not automatically Hermite-Biehler.

The needed inequality is roughly:

```math
|E(z)|>|E^*(z)|,\quad Im(z)>0.
```

Since

```math
E^*(z)=\overline{E(\overline{z})},
```

this inequality compares two Laplace-type transforms with opposite exponential weights.

## First experimental task

Compute numerically

```math
Delta(z)=|E(z)|^2-|E^*(z)|^2
```

for sampled points in the upper half-plane.

If `Delta(z)>0` systematically, the one-sided route becomes high priority.

If it fails, the direct one-sided transform is not the right Hermite-Biehler function.

## Next file

```text
experiments/one_sided_transform_hb_scan.py
```

## Status

Open. This is currently one of the most natural non-circular routes in the project.
