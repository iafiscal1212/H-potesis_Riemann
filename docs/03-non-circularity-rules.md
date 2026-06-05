# Non-circularity rules

## Purpose

This file defines rules to avoid circular reasoning in the RH research archive.

## Rule 1 - No zero-input constructions

Do not construct an operator, matrix, measure, approximant, or kernel using the nontrivial zeros of zeta as input if the goal is to prove their location.

Allowed:

- theta function;
- Phi kernel;
- zeta functional equation;
- Euler product in its valid domain;
- von Mangoldt function;
- primes and prime powers;
- explicit formula when used with clear logical dependencies;
- known unconditional zero-free regions;
- verified numerical zeros only for calibration, not proof.

Not allowed as proof input:

- diagonal matrices with entries equal to known zero ordinates;
- products over zeros assuming real ordinates;
- positivity criteria whose proof already assumes RH;
- truncations selected by matching zeros.

## Rule 2 - Experiments are not proofs

Numerical experiments may generate hypotheses, detect failures, or prioritize routes.

They cannot close RH.

Every experiment must state:

- precision;
- formulas used;
- parameters;
- whether zeros were used as input;
- what would be needed for a proof.

## Rule 3 - Functional equation is not enough

The symmetry

```math
xi(s)=xi(1-s)
```

explains why the critical line is natural.

It does not force all zeros to lie on that line.

Any argument from symmetry must include an additional positivity, spectral, or extremal mechanism.

## Rule 4 - Herglotz route discipline

If trying to prove that

```math
M(z)=-Xi'(z)/Xi(z)
```

is Herglotz/Pick, the proof must derive this from structure, not from the product over real zeros.

Acceptable sources:

- positive integral representation;
- self-adjoint resolvent;
- canonical system with positive Hamiltonian;
- stable-polynomial limit independent of zeros.

## Rule 5 - Approximation route discipline

For approximants `F_N -> Xi`, record:

1. definition of `F_N`;
2. proof or numerical evidence of real-rootedness;
3. convergence type;
4. whether construction is independent of zeros;
5. known failure modes.
