# Results - Moment/Hankel scan from Phi

## Experiment

Script base:

```text
experiments/moment_jacobi_phi.py
```

Object:

```math
m_k=\int_{-\infty}^{\infty}x^k\Phi(|x|)\,dx.
```

Since the weight is even, odd moments vanish:

```math
m_{2j+1}=0.
```

The Hankel matrix is

```math
H_n=(m_{i+j})_{0\le i,j<n}.
```

## Numerical method

A fast local scan used double precision quadrature on `[0,2.5]`, enough for a first test because `Phi(u)` decays superexponentially. This is not a rigorous interval computation.

## Initial moments

Approximate moments:

```text
m0  = 1.24280194547078546e-01
m1  = 0
m2  = 1.43574651969659013e-03
m3  = 0
m4  = 4.62945067763692627e-05
m5  = 0
m6  = 2.34099979139679544e-06
m7  = 0
m8  = 1.57193920459175421e-07
m9  = 0
m10 = 1.29488853218483088e-08
```

## Hankel eigenvalues

Minimum eigenvalues for small Hankel matrices:

```text
n=2 -> min eigenvalue ~= 1.4357465196965901e-03
n=3 -> min eigenvalue ~= 2.9704084789692942e-05
n=4 -> min eigenvalue ~= 8.4738862998073150e-07
n=5 -> min eigenvalue ~= 3.0026217556334670e-08
n=6 -> min eigenvalue ~= 1.2494492274610673e-09
```

All tested Hankel matrices were positive definite.

## Interpretation

This supports that the even weight

```math
w(x)=\Phi(|x|)
```

acts like a positive moment measure in the tested range.

That is expected if `Phi` is positive, but still useful because it allows construction of orthogonal polynomials and finite Jacobi matrices without using zeta zeros as input.

## Important limitation

This does not connect the resulting Jacobi matrices to `Xi` yet.

A positive moment measure gives a self-adjoint multiplication/Jacobi operator, but the decisive missing step is to show that its spectral transform or characteristic approximants converge to `Xi` or to the Herglotz function

```math
-\Xi'/\Xi.
```

## Status

`experiment-numerico` supporting construction of a non-circular operator prototype.

## Next step

Create a constructor for Jacobi matrices from the moment sequence and compare their finite spectral data with candidate approximants derived from `Xi`.
