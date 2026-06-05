# Results - Hermite-Biehler positive-sign candidate

## Experiment

Script:

```text
experiments/hermite_biehler_scan_positive_sign.py
```

Candidate:

```math
E_a^+(z)=Xi(z)+i a Xi'(z)
```

with real positive `a`.

Test quantity:

```math
Delta_a^+(z)=|E_a^+(z)|^2-|((E_a^+)^*)(z)|^2.
```

## Observation

For the same sample grid where the negative-sign candidate failed, the positive-sign candidate gives positive values.

Representative min/max values on the sample grid:

```text
a = 0.01 -> min ~= 3.05824560648e-11, max ~= 0.000195700809258
a = 0.10 -> min ~= 3.05824560648e-10, max ~= 0.00195700809258
a = 1.00 -> min ~= 3.05824560648e-9,  max ~= 0.0195700809258
a = 2.00 -> min ~= 6.11649121297e-9,  max ~= 0.0391401618516
```

## Interpretation

The sign-corrected candidate is compatible with a Hermite-Biehler inequality in the tested region.

This aligns with the earlier observation that

```math
M(z)=-Xi'(z)/Xi(z)
```

appears to have a Herglotz/Pick orientation in the upper half-plane.

## Warning

This is not a proof. The candidate

```math
E_a^+(z)=Xi(z)+i a Xi'(z)
```

is still artificial unless it can be derived from a natural structure.

The next task is to determine whether `E_a^+` can be obtained from:

1. a one-sided transform of the Riemann kernel `Phi`;
2. a de Branges space construction;
3. a self-adjoint operator model;
4. or a canonical system.

## Status

`experiment-numerico` supporting continued de Branges/Hermite-Biehler investigation.
