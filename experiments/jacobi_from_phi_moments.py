"""
Experiment: construct finite Jacobi matrices from moments of w(x)=Phi(|x|).

This builds a non-circular self-adjoint finite matrix from the Phi kernel.
It does not yet prove a relation to Xi.

Method:
    Use moments m_k = int x^k w(x) dx.
    Use Stieltjes procedure via multiplication-by-x in an orthonormal polynomial basis.

For an even measure, diagonal Jacobi coefficients alpha_n should be close to 0.
"""

from __future__ import annotations

import math
from typing import List

import numpy as np
from numpy.linalg import eigvalsh
from scipy.integrate import quad


def phi(u: float, n_terms: int = 30) -> float:
    eu4 = math.exp(4 * u)
    eu5 = math.exp(5 * u)
    eu9 = math.exp(9 * u)
    total = 0.0
    for n in range(1, n_terms + 1):
        n2 = n * n
        total += (2 * math.pi**2 * n2 * n2 * eu9 - 3 * math.pi * n2 * eu5) * math.exp(
            -math.pi * n2 * eu4
        )
    return total


def moment(k: int, upper: float = 2.5) -> float:
    if k % 2 == 1:
        return 0.0
    value, _ = quad(
        lambda x: (x**k) * phi(x),
        0.0,
        upper,
        epsabs=1e-13,
        epsrel=1e-13,
        limit=200,
    )
    return 2.0 * value


def inner_product(poly_a: np.ndarray, poly_b: np.ndarray, moments: List[float]) -> float:
    """Inner product of polynomials with coefficients in ascending order."""
    total = 0.0
    for i, ai in enumerate(poly_a):
        for j, bj in enumerate(poly_b):
            total += ai * bj * moments[i + j]
    return total


def multiply_x(poly: np.ndarray) -> np.ndarray:
    return np.concatenate(([0.0], poly))


def orthonormal_polynomials(n: int, moments: List[float]) -> List[np.ndarray]:
    """Modified Gram-Schmidt for 1, x, x^2, ... with moment inner product."""
    polys: List[np.ndarray] = []
    for degree in range(n):
        p = np.zeros(degree + 1)
        p[-1] = 1.0
        for q in polys:
            q_padded = np.pad(q, (0, len(p) - len(q)))
            coeff = inner_product(p, q_padded, moments)
            p = p - coeff * q_padded
        norm_sq = inner_product(p, p, moments)
        if norm_sq <= 0:
            raise ValueError(f"non-positive norm at degree {degree}: {norm_sq}")
        p = p / math.sqrt(norm_sq)
        polys.append(p)
    return polys


def jacobi_matrix(n: int) -> np.ndarray:
    moments = [moment(k) for k in range(2 * n + 2)]
    polys = orthonormal_polynomials(n, moments)
    J = np.zeros((n, n))
    for i, pi in enumerate(polys):
        x_pi = multiply_x(pi)
        for j, pj in enumerate(polys):
            pj_padded = np.pad(pj, (0, len(x_pi) - len(pj)))
            J[j, i] = inner_product(x_pi, pj_padded, moments)
    return 0.5 * (J + J.T)


def main() -> None:
    for n in [3, 4, 5, 6, 8]:
        J = jacobi_matrix(n)
        print("n=", n)
        print("Jacobi matrix:")
        print(np.array2string(J, precision=8, suppress_small=True))
        print("eigenvalues:", np.array2string(eigvalsh(J), precision=12))
        print()


if __name__ == "__main__":
    main()
