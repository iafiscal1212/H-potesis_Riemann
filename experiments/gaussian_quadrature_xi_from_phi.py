"""
Experiment: approximate Xi(z) via Gaussian quadrature from Phi moments.

The cosine transform is

    Xi(z) = int_0^infty Phi(u) cos(z u) du.

The moment/Jacobi construction in the previous experiment used the even measure

    w(x) = Phi(|x|) on R.

For even integrands f(x)=cos(z x),

    int_R Phi(|x|) cos(z x) dx = 2 int_0^infty Phi(u) cos(z u) du = 2 Xi(z).

Thus Gaussian quadrature for the even measure gives approximants to Xi(z):

    Xi_N(z) = 1/2 * sum_j weights_j cos(z nodes_j).

This construction uses Phi moments only, not zeta zeros.
"""

from __future__ import annotations

import math
from typing import List, Tuple

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal


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


def pad_to(poly: np.ndarray, length: int) -> np.ndarray:
    if len(poly) >= length:
        return poly[:length]
    return np.pad(poly, (0, length - len(poly)))


def inner_product(poly_a: np.ndarray, poly_b: np.ndarray, moments: List[float]) -> float:
    length = max(len(poly_a), len(poly_b))
    a = pad_to(poly_a, length)
    b = pad_to(poly_b, length)
    total = 0.0
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            total += ai * bj * moments[i + j]
    return total


def multiply_x(poly: np.ndarray) -> np.ndarray:
    return np.concatenate(([0.0], poly))


def orthonormal_polynomials(n: int, moments: List[float]) -> List[np.ndarray]:
    polys: List[np.ndarray] = []
    for degree in range(n):
        p = np.zeros(degree + 1)
        p[-1] = 1.0
        for q in polys:
            q_padded = pad_to(q, len(p))
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
            J[j, i] = inner_product(x_pi, pj, moments)
    return 0.5 * (J + J.T)


def quadrature_nodes_weights(n: int) -> Tuple[np.ndarray, np.ndarray]:
    J = jacobi_matrix(n)
    vals, vecs = np.linalg.eigh(J)
    m0 = moment(0)
    weights = m0 * (vecs[0, :] ** 2)
    return vals, weights


def xi_quad(z: complex, n: int) -> complex:
    nodes, weights = quadrature_nodes_weights(n)
    return 0.5 * np.sum(weights * np.cos(z * nodes))


def xi_integral(z: complex) -> complex:
    real_part, _ = quad(
        lambda u: phi(u) * np.real(np.cos(z * u)),
        0.0,
        2.5,
        epsabs=1e-13,
        epsrel=1e-13,
        limit=200,
    )
    imag_part, _ = quad(
        lambda u: phi(u) * np.imag(np.cos(z * u)),
        0.0,
        2.5,
        epsabs=1e-13,
        epsrel=1e-13,
        limit=200,
    )
    return real_part + 1j * imag_part


def main() -> None:
    zs = [0, 1, 5, 10, 14.134725, 20]
    ns = [4, 6, 8, 10]

    for z in zs:
        exact = xi_integral(z)
        print("z=", z, "integral=", exact)
        for n in ns:
            approx = xi_quad(z, n)
            print("  n=", n, "quad=", approx, "abs_err=", abs(approx - exact))
        print()


if __name__ == "__main__":
    main()
