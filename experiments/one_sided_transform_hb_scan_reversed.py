"""
Experiment: reversed one-sided Phi transform Hermite-Biehler scan.

Define

    E_rev(z) = int_0^infty Phi(u) exp(-i z u) du.

Test

    |E_rev(z)| > |E_rev^*(z)|, Im(z)>0.

This is the orientation-reversed version of the previous one-sided transform.
"""

from __future__ import annotations

import math

import numpy as np
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


def E_rev(z: complex, upper: float = 3.0) -> complex:
    real_part, _ = quad(
        lambda u: phi(u) * np.real(np.exp(-1j * z * u)),
        0.0,
        upper,
        epsabs=1e-12,
        epsrel=1e-12,
        limit=300,
    )
    imag_part, _ = quad(
        lambda u: phi(u) * np.imag(np.exp(-1j * z * u)),
        0.0,
        upper,
        epsabs=1e-12,
        epsrel=1e-12,
        limit=300,
    )
    return real_part + 1j * imag_part


def E_rev_star(z: complex) -> complex:
    return np.conj(E_rev(np.conj(z)))


def delta(z: complex) -> float:
    ez = E_rev(z)
    es = E_rev_star(z)
    return abs(ez) ** 2 - abs(es) ** 2


def main() -> None:
    xs = [-20, -10, -2, 0, 2, 10, 20]
    ys = [0.1, 0.5, 1.0, 2.0, 5.0]
    min_delta = float("inf")
    max_delta = -float("inf")
    for x in xs:
        for y in ys:
            z = x + 1j * y
            d = delta(z)
            min_delta = min(min_delta, d)
            max_delta = max(max_delta, d)
            print(f"z={z}, delta={d:.16e}")
    print("min_delta", min_delta)
    print("max_delta", max_delta)


if __name__ == "__main__":
    main()
