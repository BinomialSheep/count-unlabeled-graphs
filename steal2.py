import time
from itertools import combinations
from math import prod, factorial, gcd, comb
from fractions import Fraction
from sympy.utilities.iterables import partitions


def A000088(n):
    def calculate_numerator(p):
        part1 = sum(p[r] * p[s] * gcd(r, s) for r, s in combinations(p.keys(), 2))
        part2 = sum((q >> 1) * r + (q * r * (r - 1) >> 1) for q, r in p.items())
        return 1 << (part1 + part2)

    def calculate_denominator(p):
        return prod(q**r * factorial(r) for q, r in p.items())

    return int(
        sum(
            Fraction(calculate_numerator(p), calculate_denominator(p))
            for p in partitions(n)
        )
    )


def solve(n):
    def calculate_numerator(p):
        # 個数が異なるサイクル間の組み合わせ
        part1 = 1
        for r, s in combinations(p.keys(), 2):
            part1 *= 2 ** (p[r] * p[s] * gcd(r, s))
        # 個数が同じだけど異なるサイクル間の組み合わせ
        part2 = 1
        for q, r in p.items():
            part2 *= 2 ** (q * comb(r, 2))
        # 同じサイクル内の組み合わせ
        part3 = 1
        for q, r in p.items():
            part3 *= 2 ** (q // 2 * r)
        # それらの総積
        return part1 * part2 * part3

    def calculate_denominator(p):
        return prod(q**r * factorial(r) for q, r in p.items())

    ans = 0
    for p in partitions(n):
        # 分割数ごとに数え上げる
        ans += Fraction(calculate_numerator(p), calculate_denominator(p))
    return ans


def main():
    for i in range(50):
        start = time.perf_counter()
        print(i, solve(i))
        end = time.perf_counter()
        print(f"頂点数{i}の実行時間：{end - start:.3f}")
        assert A000088(i) == solve(i)


if __name__ == "__main__":
    main()
