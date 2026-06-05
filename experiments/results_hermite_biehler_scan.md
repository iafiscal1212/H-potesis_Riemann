# Results - Hermite-Biehler candidate scan

## Experiment

Script:

```text
experiments/hermite_biehler_scan.py
```

Candidate:

```math
E_a(z)=Xi(z)-i a Xi'(z)
```

with real positive `a`.

Hermite-Biehler test quantity:

```math
Delta_a(z)=|E_a(z)|^2-|E_a^*(z)|^2.
```

For this convention, a positive value in the upper half-plane would support the Hermite-Biehler inequality.

## Sample result

For sample points in the upper half-plane and

```text
a in {0.01, 0.05, 0.1, 0.5, 1, 2}
```

the values of `Delta_a(z)` were negative in the tested grid.

Representative values:

```text
a = 0.1, z =  2 + 0.5i  -> Delta ~= -0.0019570081
a = 1.0, z =  2 + 0.5i  -> Delta ~= -0.0195700809
a = 2.0, z =  2 + 0.5i  -> Delta ~= -0.0391401619
```

## Interpretation

The direct candidate

```math
E_a(z)=Xi(z)-i a Xi'(z)
```

with this sign convention does not satisfy the desired Hermite-Biehler inequality in the tested region.

This does not eliminate the de Branges route. It only discards or modifies this naive candidate.

## Immediate correction

Test the opposite sign:

```math
E_a^+(z)=Xi(z)+i a Xi'(z).
```

Because the previous delta was consistently negative, the opposite sign is expected to reverse the inequality in the same sample region.

## Status

`fallo-detectado` for one sign of the naive derivative candidate.

Next step: test the opposite sign and then seek a non-arbitrary construction from the unilateral transform of `Phi`.
