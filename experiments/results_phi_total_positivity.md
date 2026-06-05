# Results - Phi total positivity, first scan

## Experiment

Script:

```text
experiments/phi_total_positivity.py
```

Kernel tested:

```math
K(x,y)=\Phi(x+y)
```

with

```math
\Phi(u)=\sum_{n=1}^{\infty}
\left(2\pi^2 n^4 e^{9u}-3\pi n^2 e^{5u}\right)
\exp\left(-\pi n^2 e^{4u}\right).
```

## Numerical precision

Initial private scan used high precision arithmetic via `mpmath`, with `mp.mp.dps` between 50 and 80.

## Initial values

Approximate values:

```text
Phi(0)   = 0.4466969004671234440869846670547
Phi(0.1) = 0.3042748526669574957029064524149
Phi(0.5) = 1.3778139406356337655e-7
Phi(1.0) = 5.1020013390244491264e-70
```

## First determinant scan

For the naive kernel `K(x,y)=Phi(x+y)`, the `2x2` determinant

```math
\det
\begin{pmatrix}
\Phi(x_1+y_1) & \Phi(x_1+y_2) \\
\Phi(x_2+y_1) & \Phi(x_2+y_2)
\end{pmatrix}
```

was negative for simple ordered points.

Example:

```text
x1 = 0
x2 = 0.1
y1 = 0
y2 = 0.1

det ~= -0.05406000986043653553444468620273
```

## Interpretation

This is an important negative result for the naive version of Via 2.

It suggests:

```math
K(x,y)=\Phi(x+y)
```

is not totally positive in the direct sense tested.

This does not refute RH and does not eliminate all positivity-based routes. It only shows that the most naive total-positivity formulation is probably not the correct one.

## Consequences

The Via 2 program must be refined. Possible modifications:

1. Change variable, e.g. use `r=e^{4u}` or another theta-natural coordinate.
2. Test `Phi(x-y)` or related convolution kernels instead of `Phi(x+y)`.
3. Test signed total positivity or eventual total positivity.
4. Apply a normalizing factor before testing minors.
5. Study whether derivatives of `Phi`, rather than `Phi` itself, satisfy a Pólya frequency condition.
6. Move toward Herglotz or Laguerre-Polya criteria instead of direct total positivity.

## Status

`fallo-detectado` for naive total positivity of `Phi(x+y)`.

This is useful: it prevents wasting time on a false direct lemma.
