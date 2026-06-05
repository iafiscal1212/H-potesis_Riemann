# Via 3-4 - Derivative Hermite-Biehler candidate

## Classification

`candidate-lemma` + `experimental-support`

## Candidate function

Numerical scans suggest the sign-corrected family

```math
E_a(z)=Xi(z)+i a Xi'(z),\quad a>0,
```

has the correct Hermite-Biehler orientation on tested points in the upper half-plane.

## Hermite-Biehler quantity

For real entire `Xi`,

```math
E_a^*(z)=Xi(z)-i a Xi'(z).
```

The desired inequality is

```math
|E_a(z)|>|E_a^*(z)|,\quad Im(z)>0.
```

Expanding:

```math
|Xi+i a Xi'|^2-|Xi-i a Xi'|^2
=4a Im(Xi' \overline{Xi})
```

up to the sign convention determined by the variable `z`.

Thus the Hermite-Biehler inequality is equivalent to a sign condition on the phase derivative of `Xi` in the upper half-plane.

## Relation with logarithmic derivative

Since

```math
M(z)=-Xi'(z)/Xi(z),
```

we have

```math
Xi'(z)\overline{Xi(z)} = (Xi'(z)/Xi(z)) |Xi(z)|^2.
```

Therefore the sign of the Hermite-Biehler delta is controlled by the imaginary part of `Xi'/Xi`, equivalently by the Herglotz orientation of `M`.

This explains why the Hermite-Biehler scan and the Pick/Herglotz scan agree numerically.

## Candidate lemma

If for all `z` with `Im(z)>0`,

```math
Im(-Xi'(z)/Xi(z))>0,
```

then `E_a(z)=Xi(z)+i a Xi'(z)` satisfies the Hermite-Biehler inequality for every `a>0` and `Xi` has only real zeros.

## Obstruction

The condition

```math
Im(-Xi'/Xi)>0
```

is itself essentially equivalent to real-rootedness under standard assumptions.

Therefore the missing step is not algebraic. The missing step is structural:

Find a non-circular source of the Herglotz property.

## Structural sources to investigate

1. One-sided transform of `Phi`.
2. de Branges canonical system.
3. Self-adjoint resolvent representation.
4. Positive Pick kernel from theta identities.
5. Limit of stable polynomials.

## Decision

The project should now focus on producing `M(z)` as a resolvent or as a Herglotz transform of a positive measure, without using the zeros of `Xi`.
