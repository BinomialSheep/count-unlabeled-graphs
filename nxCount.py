import time
from itertools import combinations
import networkx as nx
from networkx.algorithms import isomorphism

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


def is_isomorphic(g1, g2):
    """グラフが同型か判定する"""
    gm = isomorphism.GraphMatcher(g1, g2)
    return gm.is_isomorphic()


def main():
    for N in range(8):
        start = time.perf_counter()

        distinct_graphs = []
        count = 0
        for edges in generate_graphs(N):
            count += 1
            new_graph = nx.Graph()
            new_graph.add_edges_from(edges)

            is_new = True
            for g in distinct_graphs:
                if is_isomorphic(new_graph, g):
                    is_new = False
                    break

            if is_new:
                distinct_graphs.append(new_graph)

        number_of_distinct_graphs = len(distinct_graphs)

        end = time.perf_counter()
        print(
            f"vertices: {N}, number_of_distinct_graphs: {number_of_distinct_graphs}, execution time: {end-start:.3f}"
        )
        assert EXPECTED_VALUE[N] == number_of_distinct_graphs


if __name__ == "__main__":
    main()
