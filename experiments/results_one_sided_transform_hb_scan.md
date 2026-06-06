# Results - one-sided Phi transform Hermite-Biehler scan

## Experiment

Script:

```text
experiments/one_sided_transform_hb_scan.py
```

Candidate:

```math
E(z)=\int_0^\infty \Phi(u)e^{izu}du.
```

Hermite-Biehler test quantity:

```math
\Delta(z)=|E(z)|^2-|E^*(z)|^2.
```

## Observation

In the sampled upper half-plane, `Delta(z)` is negative with the convention above.

This means the direct orientation

```math
|E(z)|>|E^*(z)|
```

fails.

## Interpretation

This does not discard the one-sided transform route.

It indicates that the Hermite-Biehler orientation is reversed. The candidate may need to be replaced by `E^*`, or equivalently by

```math
\widetilde E(z)=\int_0^\infty \Phi(u)e^{-izu}du.
```

For `Im(z)>0`, the exponential factor `e^{-izu}` has growth rather than damping, but the superexponential decay of `Phi` may still make the transform entire.

## Consequence

The one-sided transform remains natural, but the correct Hermite-Biehler function is likely orientation-dependent.

## Next step

Test

```math
\widetilde E(z)=\int_0^\infty \Phi(u)e^{-izu}du.
```

and record whether

```math
|\widetilde E(z)|>|\widetilde E^*(z)|
```

holds in the upper half-plane.

## Status

`orientation-failure` for the first one-sided convention.
