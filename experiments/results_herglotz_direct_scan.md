# Results - direct Herglotz scan for Xi

## Experiment

Script:

```text
experiments/herglotz_direct_xi_scan.py
```

Object tested:

```math
M(z)=-\Xi'(z)/\Xi(z)
```

where

```math
\Xi(z)=\xi(1/2+iz).
```

## Numerical method

`Xi(z)` was evaluated using the completed zeta expression:

```math
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
```

The derivative was evaluated numerically with `mpmath.diff`.

## Sample grid

```text
x in {-20, -10, -2, 2, 10, 20}
y in {0.1, 0.5, 1.0, 2.0}
z = x + i y
```

The line `x=0` was avoided in this first scan because some sampled values cross special points of the completed expression in the transformed `s` variable and require separate handling.

## Observation

For all sampled points with `Im(z)>0`, the imaginary part of

```math
M(z)=-\Xi'(z)/\Xi(z)
```

was positive.

Representative values:

```text
z = -20 + 0.1i -> Im(M) ~= 0.1067738528690507
z = -10 + 0.1i -> Im(M) ~= 0.0106195505345307
z =  -2 + 0.1i -> Im(M) ~= 0.00471249391588059
z =   2 + 0.1i -> Im(M) ~= 0.00471249391588059
z =  10 + 0.1i -> Im(M) ~= 0.0106195505345307
z =  20 + 0.1i -> Im(M) ~= 0.1067738528690507
```

## Interpretation

This is numerically compatible with a Herglotz/Pick type property for the sign-normalized logarithmic derivative.

If one could prove globally that `M(z)` maps the upper half-plane into the upper half-plane, with the correct analytic conditions, the poles of `M` would be forced to lie on the real axis. Since the poles of `M` are the zeros of `Xi`, this would imply RH.

## Critical warning

This numerical scan is not a proof.

The Herglotz property may fail outside the tested grid, or the numerical derivative may hide difficult behavior near zeros/poles. The main open task is to derive a positive integral representation for `M(z)` without assuming the real-zero property.

## Status

`experiment-numerico` supporting continued investigation of Via 3.
