# Results - Jacobi matrices from Phi moments

## Experiment

Script:

```text
experiments/jacobi_from_phi_moments.py
```

This constructs finite Jacobi matrices from the moment sequence

```math
m_k=\int_{-\infty}^{\infty}x^k\Phi(|x|)\,dx.
```

The construction uses Gram-Schmidt on monomials with respect to the moment inner product and represents multiplication by `x` in the resulting orthonormal polynomial basis.

## Correction

The first version of the script had a padding error when multiplying a polynomial by `x`. This was corrected in commit updating `experiments/jacobi_from_phi_moments.py`.

## Numerical structure

Because the measure is even, the Jacobi diagonal coefficients are approximately zero.

The resulting finite Jacobi matrices are symmetric tridiagonal up to numerical noise.

## Sample matrices and spectra

For `n=3`:

```text
J ~= [[0, 0.10748254, 0],
      [0.10748254, 0, 0.14384613],
      [0, 0.14384613, 0]]

eigenvalues ~= [-0.179566717855, 0, 0.179566717855]
```

For `n=4`:

```text
eigenvalues ~= [-0.234041975269, -0.077602228548,
                 0.077602228548,  0.234041975269]
```

For `n=6`:

```text
eigenvalues ~= [-0.314584574416, -0.187748153017, -0.062902918243,
                 0.062902918243,  0.187748153017,  0.314584574416]
```

For `n=8`:

```text
eigenvalues ~= [-0.373869931787, -0.265452907574, -0.160305260508,
                -0.053771488995,  0.053771488995,  0.160305260508,
                 0.265452907574,  0.373869931787]
```

## Interpretation

This produces a natural self-adjoint finite matrix from the Phi kernel without using zeta zeros.

However, its eigenvalues are small and symmetric around zero because they are quadrature nodes for the moment measure, not approximations to the ordinates of zeta zeros.

Thus this Jacobi matrix is non-circular and structurally clean, but it is not yet a Hilbert-Polya operator.

## Key obstruction

We still need a functional relation between this moment/Jacobi construction and either:

```math
\Xi(z)
```

or

```math
-\Xi'(z)/\Xi(z).
```

Without such a relation, the matrix is only an auxiliary operator attached to `Phi`.

## Status

`experiment-numerico` + `operator-prototype`.

## Next step

Investigate whether Gaussian quadrature from this Jacobi matrix approximates the cosine transform defining `Xi`:

```math
\Xi(z)=\int_0^\infty \Phi(u)\cos(zu)du.
```

If quadrature approximants have real-zero properties, this may connect the moment operator to the Xi function.
