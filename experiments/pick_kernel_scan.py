"""
Experiment: Pick kernel scan for M(z) = -Xi'(z)/Xi(z).

A Herglotz/Pick function M should make the kernel

    P_M(z,w) = (M(z) - conjugate(M(w))) / (z - conjugate(w))

positive semidefinite for points in the upper half-plane.

If this property could be proved for M without assuming RH, it would be a
strong route toward real-rootedness of Xi.

Numerical evidence is not proof.
"""

from __future__ import annotations

import itertools
from typing import Sequence

import mpmath as mp


mp.mp.dps = 60


def xi_completed(s: complex) -> complex:
    s = mp.mpc(s)
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Xi(z: complex) -> complex:
    z = mp.mpc(z)
    return xi_completed(mp.mpf("0.5") + 1j * z)


def Xi_prime(z: complex) -> complex:
    return mp.diff(Xi, z)


def M(z: complex) -> complex:
    return -Xi_prime(z) / Xi(z)


def pick_entry(z: complex, w: complex) -> complex:
    z = mp.mpc(z)
    w = mp.mpc(w)
    return (M(z) - mp.conj(M(w))) / (z - mp.conj(w))


def pick_matrix(points: Sequence[complex]) -> mp.matrix:
    return mp.matrix([[pick_entry(z, w) for w in points] for z in points])


def hermitian_eigenvalues(A: mp.matrix):
    # mp.eigsy expects a Hermitian/symmetric matrix.
    return mp.eigsy(A, eigvals_only=True)


def main() -> None:
    test_sets = [
        [mp.mpc(-2, 0.5), mp.mpc(2, 0.5)],
        [mp.mpc(-10, 0.5), mp.mpc(0.5, 0.75), mp.mpc(10, 0.5)],
        [mp.mpc(-20, 1), mp.mpc(-5, 0.4), mp.mpc(5, 0.4), mp.mpc(20, 1)],
    ]

    for index, points in enumerate(test_sets, start=1):
        print(f"TEST SET {index}")
        print("points:", [mp.nstr(p, 12) for p in points])
        P = pick_matrix(points)
        eigs = hermitian_eigenvalues(P)
        print("eigenvalues:", [mp.nstr(e, 30) for e in eigs])
        print("min eigenvalue:", mp.nstr(min(eigs), 30))
        print()


if __name__ == "__main__":
    main()
