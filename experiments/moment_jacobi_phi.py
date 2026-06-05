"""
Experiment: moment/Jacobi matrices from the Riemann Phi kernel.

Goal:
    Build finite Jacobi matrices from moments of a positive weight derived from Phi,
    then inspect whether their spectra resemble structural approximants.

This is exploratory. It does not prove RH.

Possible idea:
    Positive measures -> orthogonal polynomials -> Jacobi matrices -> real spectra.

If a natural measure derived from Phi generated characteristic polynomials converging
 to Xi, it would provide a Hilbert-Polya-like route. This experiment only starts
 probing that possibility.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 80


def phi(u: mp.mpf, n_terms: int = 50) -> mp.mpf:
    u = mp.mpf(u)
    total = mp.mpf("0")
    eu4 = mp.e ** (4 * u)
    eu5 = mp.e ** (5 * u)
    eu9 = mp.e ** (9 * u)
    for n_int in range(1, n_terms + 1):
        n = mp.mpf(n_int)
        n2 = n * n
        total += (
            2 * mp.pi**2 * n2 * n2 * eu9 - 3 * mp.pi * n2 * eu5
        ) * mp.e ** (-mp.pi * n2 * eu4)
    return total


def even_weight(x: mp.mpf) -> mp.mpf:
    """Symmetric positive candidate weight w(x)=Phi(abs(x))."""
    return phi(abs(x))


def moment(k: int) -> mp.mpf:
    """Compute m_k=int_R x^k w(x) dx for the even weight."""
    if k % 2 == 1:
        return mp.mpf("0")
    f = lambda x: (x ** k) * phi(x)
    return 2 * mp.quad(f, [0, mp.inf])


def hankel_moment_matrix(n: int) -> mp.matrix:
    """Return H_ij = m_{i+j}, i,j=0..n-1."""
    moments = [moment(k) for k in range(2 * n - 1)]
    return mp.matrix([[moments[i + j] for j in range(n)] for i in range(n)])


def main() -> None:
    for n in [2, 3, 4, 5]:
        H = hankel_moment_matrix(n)
        eigs = mp.eigsy(H, eigvals_only=True)
        print(f"n={n}")
        print("moments/eigenvalues of Hankel matrix:")
        print([mp.nstr(e, 30) for e in eigs])
        print("min eigenvalue:", mp.nstr(min(eigs), 30))
        print()


if __name__ == "__main__":
    main()
