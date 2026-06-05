# Results - Pick kernel scan

## Experiment

Script:

```text
experiments/pick_kernel_scan.py
```

Object:

```math
M(z)=-\Xi'(z)/\Xi(z)
```

Pick kernel:

```math
P_M(z,w)=\frac{M(z)-\overline{M(w)}}{z-\overline{w}}.
```

For a Herglotz/Pick function, finite matrices

```math
[P_M(z_i,z_j)]
```

should be positive semidefinite for points in the upper half-plane.

## Initial numerical scan

Tested point sets:

```text
1. {-2+0.5i, 2+0.5i}
2. {-10+0.5i, 0.5+0.75i, 10+0.5i}
3. {-20+1i, -5+0.4i, 5+0.4i, 20+1i}
```

The Hermitian eigenvalues were approximately:

```text
set 1: [0.00061222, 0.09359611]
set 2: [0.00306304, 0.04646313, 0.20741832]
set 3: [0.00412251, 0.07196820, 0.54433354, 0.69746064]
```

All sampled Pick matrices were positive definite.

## Interpretation

This is numerically compatible with the hypothesis that

```math
M(z)=-\Xi'(z)/\Xi(z)
```

is a Herglotz/Pick function in the upper half-plane.

If this property can be proved without assuming RH, then the zeros of `Xi` would be forced onto the real axis, implying RH.

## Warning

This is not a proof.

The positive matrices only test finitely many points. A global proof would require either:

1. an analytic positive-kernel representation;
2. a Herglotz integral representation;
3. an operator model producing this kernel as a Gram matrix;
4. or an equivalent non-circular positivity theorem.

## Status

`experiment-numerico` supporting Via 3.

## Next step

Try to express the Pick kernel as a Gram-type object from the integral representation of `Xi`.
