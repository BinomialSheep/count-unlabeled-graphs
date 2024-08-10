import time
from itertools import combinations, permutations
from typing import Set, Tuple


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


def generate_graphs(n):
    """n頂点グラフの辺集合を返すジェネレータ関数
    単純無効グラフの個数分生成される（2^(nC2)通り）
    """
    possible_edges = list(combinations(range(n), 2))
    for i in range(2 ** len(possible_edges)):
        # iの2進数表現で1が立っている辺からなるグラフ
        edges = set()
        for j, edge in enumerate(possible_edges):
            # j桁目が立っていたらj番目の辺を追加
            if i & (1 << j):
                edges.add(edge)
        yield edges


def is_isomorphic(
    edges1: Set[Tuple[int, int]], edges2: Set[Tuple[int, int]], n: int
) -> bool:
    """グラフが同型か判定する"""
    # 辺の本数が異なるグラフは明らかに同型でない
    if len(edges1) != len(edges2):
        return False

    # 同型の定義を満たす1対1写像があるか全探索する
    permutations_list = permutations([x for x in range(n)])
    for f in permutations_list:
        is_currently_isomorphic = True
        # 「頂点j, iを結ぶ辺の有無」と「頂点f(j), f(i)を結ぶ辺の有無」が常に一致していればTrue
        for i in range(n):
            if not is_currently_isomorphic:
                break
            for j in range(i):
                # 実装上j<iなので右辺ではmin,maxを取ればよい
                if ((j, i) in edges1) != ((min(f[j], f[i]), max(f[j], f[i])) in edges2):
                    is_currently_isomorphic = False
                    break
        if is_currently_isomorphic:
            return True
    return False


def main():
    for N in range(8):
        start = time.perf_counter()

        distinct_graphs = []
        for edges1 in generate_graphs(N):
            # これまで発見したいずれかのグラフと同型な場合は不採用
            is_new = True
            for edges2 in distinct_graphs:
                if is_isomorphic(edges1, edges2, N):
                    is_new = False
                    break
            if is_new:
                distinct_graphs.append(edges1)

        number_of_distinct_graphs = len(distinct_graphs)

        end = time.perf_counter()
        print(
            f"vertices: {N}, number_of_distinct_graphs: {number_of_distinct_graphs}, execution time: {end-start:.3f}"
        )

        assert EXPECTED_VALUE[N] == number_of_distinct_graphs


if __name__ == "__main__":
    main()
