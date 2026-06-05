"""
Experiment: finite heat-flow deformation of Gaussian-quadrature approximants.

Approximants:

    Xi_{N,t}(z) = 1/2 * sum_j w_j exp(t*x_j^2) cos(z*x_j)

where nodes x_j and weights w_j come from Gaussian quadrature for
w(x)=Phi(|x|).

Goal:
    Explore whether increasing t makes zeros more real, in the spirit of
    de Bruijn-Newman deformation.

This is exploratory and not a proof.
"""

from __future__ import annotations

import math
from typing import List, Tuple

import numpy as np
from scipy.integrate import quad
from scipy.optimize import root


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
        epsabs=1e-12,
        epsrel=1e-12,
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


def xi_nt(z: complex, nodes: np.ndarray, weights: np.ndarray, t: float) -> complex:
    heat_weights = weights * np.exp(t * nodes * nodes)
    return 0.5 * np.sum(heat_weights * np.cos(z * nodes))


def root_equations(v: np.ndarray, nodes: np.ndarray, weights: np.ndarray, t: float) -> np.ndarray:
    z = v[0] + 1j * v[1]
    value = xi_nt(z, nodes, weights, t)
    return np.array([value.real, value.imag])


def count_nonreal_roots(n: int, t: float, x_max=90.0, y_max=12.0, nx=13, ny=7) -> int:
    nodes, weights = quadrature_nodes_weights(n)
    roots = []
    for x0 in np.linspace(0.0, x_max, nx):
        for y0 in np.linspace(0.1, y_max, ny):
            sol = root(lambda v: root_equations(v, nodes, weights, t), np.array([x0, y0]), method="hybr")
            if sol.success:
                x, y = sol.x
                if -1 <= x <= x_max + 1 and abs(y) <= y_max + 2:
                    z = x + 1j * y
                    val = xi_nt(z, nodes, weights, t)
                    if abs(val) < 1e-8 and abs(y) > 1e-6:
                        if all(abs(z - existing) > 1e-5 for existing in roots):
                            roots.append(z)
    return len(roots)


def main() -> None:
    ns = [6, 8, 10]
    ts = [-20, -10, -5, -2, -1, 0, 1, 2, 5, 10, 20]
    for n in ns:
        print("N=", n)
        for t in ts:
            count = count_nonreal_roots(n, float(t))
            print(f"  t={t:>5}: nonreal_roots_found={count}")
        print()


if __name__ == "__main__":
    main()
