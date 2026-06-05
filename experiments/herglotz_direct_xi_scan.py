"""
Experiment: direct Xi logarithmic derivative scan.

This script evaluates

    M(z) = -Xi'(z) / Xi(z)

using the completed zeta expression rather than the integral representation.

Xi(z) = xi(1/2 + i z)
xi(s) = 1/2 s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)

For a real-entire function with only real zeros, the sign-normalized logarithmic
 derivative should satisfy a half-plane sign property. This experiment checks
 whether Im(M(z)) is positive for sample points with Im(z)>0.

Numerical evidence is not proof.
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


def M(z: complex) -> complex:
    return -Xi_prime(z) / Xi(z)


def main() -> None:
    xs = [-20, -10, -2, 2, 10, 20]
    ys = [0.1, 0.5, 1.0, 2.0]

    print("z, Im(M(z)), M(z)")
    min_im = mp.inf
    max_im = -mp.inf

    for x in xs:
        for y in ys:
            z = mp.mpc(x, y)
            value = M(z)
            im_value = mp.im(value)
            min_im = min(min_im, im_value)
            max_im = max(max_im, im_value)
            print(
                f"z={mp.nstr(z, 12)}",
                f"Im(M)={mp.nstr(im_value, 20)}",
                f"M={mp.nstr(value, 25)}",
            )

    print("min Im(M) =", mp.nstr(min_im, 30))
    print("max Im(M) =", mp.nstr(max_im, 30))


if __name__ == "__main__":
    main()
