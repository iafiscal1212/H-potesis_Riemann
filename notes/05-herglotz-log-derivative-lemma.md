# Via 3 - Logarithmic derivative lemma

## Classification

`base-technical` + `conditional-criterion`

## Setup

Let `F` be a real entire function with real zeros only. Assume, for simplicity, that the zeros are simple and denoted by `lambda_n`.

A formal product has the shape

```math
F(z)=C e^{az+b}\prod_n E(z/lambda_n),
```

where `E` is the canonical factor required for convergence.

Its logarithmic derivative has the schematic form

```math
F'(z)/F(z)=a+sum_n corrections(lambda_n,z).
```

In the simplest finite polynomial case,

```math
P(z)=C\prod_{n=1}^{N}(z-lambda_n),
```

we get

```math
P'(z)/P(z)=sum_{n=1}^{N}1/(z-lambda_n).
```

## Half-plane sign property

For `z=x+iy` with `y>0` and real `lambda`,

```math
Im(1/(z-lambda))<0.
```

Therefore

```math
-Im(P'(z)/P(z))>0
```

for finite real-rooted polynomials.

Equivalently, a sign-adjusted logarithmic derivative maps the upper half-plane into itself or its negative, depending on convention.

## Candidate criterion

For `Xi`, a possible target is to prove a half-plane mapping property for a sign-normalized logarithmic derivative.

One possible convention:

```math
G(z)=Xi'(z)/Xi(z)
```

should have negative imaginary part in the upper half-plane if all zeros are real.

Equivalently:

```math
-G(z)
```

should have positive imaginary part in the upper half-plane.

## Why this would imply real zeros

If a meromorphic function has a pole away from the real axis, the local behavior near that pole contradicts the global Herglotz/Pick half-plane sign condition.

Thus, if the logarithmic derivative of `Xi` has the correct Herglotz property and the required growth conditions, the poles of that logarithmic derivative must lie on the real axis.

The poles of `Xi'/Xi` are precisely the zeros of `Xi`, counted with multiplicity.

Therefore, a non-circular proof of the Herglotz property would imply RH.

## Critical obstruction

For `Xi`, proving this mapping property directly is essentially as hard as proving that its zeros are real.

The task is therefore not to assume the property, but to derive it from a positive integral representation or from an operator model.

## Non-circular target

Find a representation of the form

```math
-Xi'(z)/Xi(z)=az+b+int_R ((1/(x-z)) - x/(1+x^2)) dmu(x)
```

with a positive measure `mu`, without using the zeros of `Xi` as input.

If such a representation is derived from the integral kernel, theta structure, or an operator construction, it would be a major route toward RH.

## Next move

Investigate whether the integral representation of `Xi` gives a direct expression for `Xi'/Xi` as a quotient of cosine and sine transforms:

```math
Xi'(z) = -int_0^infty u Phi(u) sin(zu) du.
```

Then

```math
-Xi'(z)/Xi(z)=
(int_0^infty u Phi(u) sin(zu) du) /
(int_0^infty Phi(u) cos(zu) du).
```

The question becomes whether this quotient is a Herglotz function.
