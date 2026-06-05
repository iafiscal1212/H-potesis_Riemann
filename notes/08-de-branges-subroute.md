# Via 3-4 - de Branges / Hermite-Biehler subroute

## Classification

`strategic-subroute` + `candidate-framework`

## Why this route

The current strongest direction is the Herglotz/Pick behavior of

```math
M(z)=-Xi'(z)/Xi(z).
```

Positive Pick kernels, Herglotz functions, self-adjoint operators, and real zeros of entire functions are naturally connected by de Branges theory.

This makes de Branges spaces a plausible framework for unifying:

1. real-rootedness of `Xi`;
2. Hilbert-space kernels;
3. spectral interpretation;
4. Herglotz logarithmic derivatives.

## Hermite-Biehler functions

A function `E` is in the Hermite-Biehler class if it is entire and satisfies a strict half-plane inequality, typically

```math
|E(z)|>|E^*(z)|
```

for `Im(z)>0`, where

```math
E^*(z)=\overline{E(\overline{z})}.
```

Writing

```math
E(z)=A(z)-iB(z)
```

with real entire `A` and `B`, de Branges theory gives strong real-zero and interlacing properties for `A` and `B`.

## Desired connection to Xi

Find `E` such that either

```math
A(z)=Xi(z)
```

or

```math
B(z)=Xi(z)
```

or `Xi` is a canonical component of `E`.

If `E` is Hermite-Biehler by a non-circular argument, then real-zero properties for `Xi` may follow.

## Why this is difficult

Constructing such an `E` may be equivalent to RH.

The task is not simply to define

```math
E(z)=Xi(z)-i Xi'(z)
```

and assume it is Hermite-Biehler. The Hermite-Biehler inequality must be proved from theta, Phi, primes, or operator structure.

## Candidate construction A

Try

```math
E_a(z)=Xi(z)-i a Xi'(z)
```

for a positive parameter `a`.

Question:

```math
|E_a(z)|>|E_a^*(z)| \quad Im(z)>0?
```

This inequality may be testable numerically.

If it holds for some natural `a`, it would imply constraints on zeros of `Xi`.

## Candidate construction B

Use shifted functions:

```math
E_h(z)=Xi(z-ih)
```

or combinations

```math
E_h(z)=Xi(z-ih)+c Xi(z+ih).
```

Shifts into the half-plane may create Hermite-Biehler functions if zeros lie in the expected region. But this risks circularity.

## Candidate construction C

Build `E` directly from the integral kernel:

```math
E(z)=\int_0^\infty Phi(u)e^{izu}du
```

so that

```math
Xi(z)=Re(E(z))
```

or a symmetrized component.

Then the Hermite-Biehler inequality would become a statement about one-sided Fourier/Laplace transforms of `Phi`.

This is attractive because it uses `Phi` directly, not the zeros.

## First numerical experiment

For candidate A, compute

```math
D_a(z)=|E_a(z)|^2-|E_a^*(z)|^2
```

for sample points in the upper half-plane.

If `D_a(z)>0` systematically for some `a`, investigate.

If it fails, discard candidate A.

## Next files

Create:

```text
experiments/hermite_biehler_scan.py
experiments/results_hermite_biehler_scan.md
```

## Current status

This is not a proof. It is a structured route to search for a non-circular positivity mechanism.
