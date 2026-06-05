"""
Experiment: Hermite-Biehler scan for candidates E_a(z)=Xi(z)-i*a*Xi'(z).

For a real entire function Xi, define

    E_a(z) = Xi(z) - i a Xi'(z)

and test the Hermite-Biehler inequality

    |E_a(z)| > |E_a^*(z)|, Im(z)>0

where E_a^*(z)=conj(E_a(conj(z))).

For real entire Xi and real a, E_a^*(z)=Xi(z)+i*a*Xi'(z).

This is only an experimental candidate. Failure does not affect RH.
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


def E(z: complex, a: float) -> complex:
    z = mp.mpc(z)
    return Xi(z) - 1j * mp.mpf(a) * Xi_prime(z)


def E_star(z: complex, a: float) -> complex:
    # For real entire Xi and real a.
    z = mp.mpc(z)
    return Xi(z) + 1j * mp.mpf(a) * Xi_prime(z)


def hb_delta(z: complex, a: float) -> mp.mpf:
    ez = E(z, a)
    es = E_star(z, a)
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
            d = hb_delta(z, a)
            deltas.append(d)
            print(" ", mp.nstr(z, 12), mp.nstr(d, 30))
        print(" min delta", mp.nstr(min(deltas), 30))
        print()


if __name__ == "__main__":
    main()
