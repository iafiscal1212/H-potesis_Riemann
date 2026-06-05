"""
Experiment: half-plane sign test for the logarithmic derivative of Xi.

This script evaluates the quotient

    M(z) = -Xi'(z)/Xi(z)

using the integral representation

    Xi(z)  = int_0^infty Phi(u) cos(z u) du
    Xi'(z) = -int_0^infty u Phi(u) sin(z u) du

so

    M(z) = int_0^infty u Phi(u) sin(z u) du / int_0^infty Phi(u) cos(z u) du

The goal is to test whether a half-plane sign property is numerically plausible.

Warning: numerical evidence is not proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

import mpmath as mp


mp.mp.dps = 50


@dataclass(frozen=True)
class SampleResult:
    z: complex
    value: complex
    imaginary_part: mp.mpf


def phi(u: mp.mpf, n_terms: int = 40) -> mp.mpf:
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


def xi_integral(z: complex, n_terms: int = 40) -> complex:
    z = mp.mpc(z)
    f = lambda u: phi(u, n_terms=n_terms) * mp.cos(z * u)
    return mp.quad(f, [0, mp.inf])


def xi_prime_integral(z: complex, n_terms: int = 40) -> complex:
    z = mp.mpc(z)
    f = lambda u: -u * phi(u, n_terms=n_terms) * mp.sin(z * u)
    return mp.quad(f, [0, mp.inf])


def minus_log_derivative(z: complex, n_terms: int = 40) -> complex:
    xi = xi_integral(z, n_terms=n_terms)
    xip = xi_prime_integral(z, n_terms=n_terms)
    return -xip / xi


def sample_grid(xs: Iterable[float], ys: Iterable[float]) -> Tuple[SampleResult, ...]:
    results = []
    for x in xs:
        for y in ys:
            z = mp.mpc(x, y)
            value = minus_log_derivative(z)
            results.append(SampleResult(z=z, value=value, imaginary_part=mp.im(value)))
    return tuple(results)


def main() -> None:
    xs = [-20, -10, -2, 0, 2, 10, 20]
    ys = [0.1, 0.5, 1.0, 2.0]
    results = sample_grid(xs, ys)

    print("z, M(z)=-Xi'(z)/Xi(z), Im(M)")
    for r in results:
        print(
            f"z={mp.nstr(r.z, 12)}",
            f"M={mp.nstr(r.value, 20)}",
            f"Im={mp.nstr(r.imaginary_part, 20)}",
        )

    min_im = min(r.imaginary_part for r in results)
    max_im = max(r.imaginary_part for r in results)
    print("min Im(M) =", mp.nstr(min_im, 30))
    print("max Im(M) =", mp.nstr(max_im, 30))


if __name__ == "__main__":
    main()
