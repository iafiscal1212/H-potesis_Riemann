"""
Experiment: naive total positivity tests for the Riemann Phi kernel.

This script tests determinants of matrices

    K_ij = Phi(x_i + y_j)

where Phi is the standard kernel appearing in the integral representation
of the Riemann Xi function / de Bruijn-Newman deformation.

Important: numerical tests do not prove or disprove RH. A negative determinant
for the naive kernel only shows that this exact naive total-positivity route
needs modification or a different kernel/variable.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

import mpmath as mp


mp.mp.dps = 80


@dataclass(frozen=True)
class DeterminantResult:
    order: int
    xs: Tuple[mp.mpf, ...]
    ys: Tuple[mp.mpf, ...]
    determinant: mp.mpf


def phi(u: mp.mpf, n_terms: int = 50) -> mp.mpf:
    """Truncated Riemann Phi kernel.

    Phi(u) = sum_{n>=1} (2*pi^2*n^4*e^(9u) - 3*pi*n^2*e^(5u))
             * exp(-pi*n^2*e^(4u)).

    Parameters
    ----------
    u:
        Real argument.
    n_terms:
        Number of terms retained in the rapidly convergent sum.
    """
    u = mp.mpf(u)
    total = mp.mpf("0")
    for n_int in range(1, n_terms + 1):
        n = mp.mpf(n_int)
        term = (
            2 * mp.pi**2 * n**4 * mp.e ** (9 * u)
            - 3 * mp.pi * n**2 * mp.e ** (5 * u)
        ) * mp.e ** (-mp.pi * n**2 * mp.e ** (4 * u))
        total += term
    return total


def kernel_matrix(xs: Sequence[mp.mpf], ys: Sequence[mp.mpf], n_terms: int = 50) -> mp.matrix:
    """Return matrix K_ij = Phi(x_i + y_j)."""
    return mp.matrix([[phi(x + y, n_terms=n_terms) for y in ys] for x in xs])


def determinant(xs: Sequence[mp.mpf], ys: Sequence[mp.mpf], n_terms: int = 50) -> mp.mpf:
    """Compute det[Phi(x_i + y_j)]."""
    return mp.det(kernel_matrix(xs, ys, n_terms=n_terms))


def scan_order_2(grid: Iterable[mp.mpf], n_terms: int = 50) -> List[DeterminantResult]:
    """Scan all 2x2 minors using ordered pairs from a grid."""
    results: List[DeterminantResult] = []
    ordered_pairs = [(a, b) for a, b in itertools.combinations(grid, 2)]
    for xs in ordered_pairs:
        for ys in ordered_pairs:
            det = determinant(xs, ys, n_terms=n_terms)
            results.append(DeterminantResult(order=2, xs=xs, ys=ys, determinant=det))
    return sorted(results, key=lambda r: r.determinant)


def main() -> None:
    grid = [mp.mpf(x) for x in ["0", "0.01", "0.05", "0.1", "0.2", "0.4", "0.6"]]

    print("Phi values:")
    for u in [mp.mpf("0"), mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("1")]:
        print(f"Phi({u}) = {mp.nstr(phi(u), 30)}")

    print("\nSmallest 2x2 determinants for K(x,y)=Phi(x+y):")
    results = scan_order_2(grid, n_terms=50)
    for result in results[:10]:
        print(
            "order=2",
            f"xs={tuple(mp.nstr(x, 8) for x in result.xs)}",
            f"ys={tuple(mp.nstr(y, 8) for y in result.ys)}",
            f"det={mp.nstr(result.determinant, 40)}",
        )


if __name__ == "__main__":
    main()
