"""
Experiment: Hermite-Biehler scan for E_a^+(z)=Xi(z)+i*a*Xi'(z).

This is the sign-reversed version of the previous candidate.

For a real entire Xi and real a:

    E_a^+(z)      = Xi(z) + i a Xi'(z)
    (E_a^+)^*(z) = Xi(z) - i a Xi'(z)

We test

    Delta_a^+(z)=|E_a^+(z)|^2-|((E_a^+)^*)(z)|^2

in the upper half-plane.

Numerical evidence is not proof. A useful result requires a non-arbitrary
construction of E, preferably from a one-sided transform, operator model, or
de Branges structure.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 50


def xi_completed(s: complex) -> complex:
    s = mp.mpc(s)
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Xi(z: complex) -> complex:
    z = mp.mpc(z)
    return xi_completed(mp.mpf("0.5") + 1j * z)


def Xi_prime(z: complex) -> complex:
    return mp.diff(Xi, z)


def E_plus(z: complex, a: float) -> complex:
    z = mp.mpc(z)
    return Xi(z) + 1j * mp.mpf(a) * Xi_prime(z)


def E_plus_star(z: complex, a: float) -> complex:
    z = mp.mpc(z)
    return Xi(z) - 1j * mp.mpf(a) * Xi_prime(z)


def hb_delta_plus(z: complex, a: float) -> mp.mpf:
    ez = E_plus(z, a)
    es = E_plus_star(z, a)
    return abs(ez) ** 2 - abs(es) ** 2


def main() -> None:
    alphas = [0.01, 0.05, 0.1, 0.5, 1.0, 2.0]
    points = [
        mp.mpc(-20, 0.5),
        mp.mpc(-10, 0.5),
        mp.mpc(-2, 0.5),
        mp.mpc(2, 0.5),
        mp.mpc(10, 0.5),
        mp.mpc(20, 0.5),
        mp.mpc(-5, 1.0),
        mp.mpc(5, 1.0),
    ]

    for a in alphas:
        print("alpha", a)
        deltas = []
        for z in points:
            d = hb_delta_plus(z, a)
            deltas.append(d)
            print(" ", mp.nstr(z, 12), mp.nstr(d, 30))
        print(" min delta", mp.nstr(min(deltas), 30))
        print()


if __name__ == "__main__":
    main()
