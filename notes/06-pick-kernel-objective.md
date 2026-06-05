# Via 3 - Pick kernel objective

## Classification

`conditional-criterion` + `next-objective`

## Object

Let

```math
M(z)=-\Xi'(z)/\Xi(z).
```

The numerical scan suggests that `M` may map the upper half-plane into the upper half-plane.

Such functions are Herglotz/Pick functions.

## Pick kernel

A function `M` mapping the upper half-plane into itself is characterized, under standard analyticity assumptions, by positivity of the Pick kernel

```math
P_M(z,w)=\frac{M(z)-\overline{M(w)}}{z-\overline{w}}.
```

For all finite sets of points `z_1,...,z_n` in the upper half-plane, the matrix

```math
\left[P_M(z_i,z_j)\right]_{i,j=1}^{n}
```

should be positive semidefinite.

## Why this matters

If the Pick kernel positivity can be proved directly from the integral or theta structure of `Xi`, then the poles of `M` must lie on the real axis.

The poles of `M` are zeros of `Xi`.

Therefore, a non-circular proof of Pick positivity for `M` would imply RH.

## New target

Prove or disprove:

```math
P_M(z,w) \succeq 0
```

for `Im(z)>0`, `Im(w)>0`, without assuming RH.

## Experimental route

Build a numerical script that:

1. samples points in the upper half-plane;
2. computes `M(z)` using completed zeta;
3. forms the Pick matrix;
4. checks eigenvalues.

## Mathematical route

Try to express

```math
P_M(z,w)
```

in terms of `Xi`, `Xi'`, and eventually the integral kernel `Phi`.

Since

```math
M(z)=-\frac{\Xi'(z)}{\Xi(z)},
```

we get

```math
P_M(z,w)=
\frac{-\Xi'(z)/\Xi(z)+\overline{\Xi'(w)/\Xi(w)}}{z-\overline{w}}.
```

If this can be rewritten as a squared norm or positive integral, the route becomes serious.

## Critical obstruction

For a general entire function, Pick positivity of the logarithmic derivative is essentially equivalent to real-rootedness.

Thus the only useful proof must derive positivity from additional structure of `Xi`, not from a hidden assumption about its zeros.

## Next experiment

Create:

```text
experiments/pick_kernel_scan.py
```

and record results in:

```text
experiments/results_pick_kernel_scan.md
```
