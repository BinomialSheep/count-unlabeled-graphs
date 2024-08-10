"""
https://oeis.org/A000088
stealed by Chai Wah Wu, Jul 02 2024
"""

import time
from itertools import combinations
from math import prod, factorial, gcd
from fractions import Fraction
from sympy.utilities.iterables import partitions

EXPECTED_VALUE = [
    1,
    1,
    2,
    4,
    11,
    34,
    156,
    1044,
    12346,
    274668,
    12005168,
    1018997864,
    165091172592,
    50502031367952,
    29054155657235488,
    31426485969804308768,
    64001015704527557894928,
    245935864153532932683719776,
    1787577725145611700547878190848,
    24637809253125004524383007491432768,
]


def A000088(n):
    return int(
        sum(
            Fraction(
                1
                << sum(p[r] * p[s] * gcd(r, s) for r, s in combinations(p.keys(), 2))
                + sum((q >> 1) * r + (q * r * (r - 1) >> 1) for q, r in p.items()),
                prod(q**r * factorial(r) for q, r in p.items()),
            )
            for p in partitions(n)
        )
    )


def main():
    for N in range(0, 101, 10):
        start = time.perf_counter()
        number_of_distinct_graphs = A000088(N)
        end = time.perf_counter()
        print(
            f"頂点数{N}、ラベルなしグラフの個数：{number_of_distinct_graphs}、実行時間：{end-start:.3f}"
        )
        # assert i >= len(EXPECTED_VALUE) or A000088(i) == EXPECTED_VALUE[i]


if __name__ == "__main__":
    main()
