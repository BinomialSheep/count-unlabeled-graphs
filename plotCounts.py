import math
import matplotlib.pyplot as plt

# 20頂点以下のラベルなし単純グラフの個数（https://oeis.org/A000088）
number_of_distinct_graphs = [
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
    645490122795799841856164638490742749440,
]


# 上界：2^(nC2)
def calc_upper_bound(n):
    return 2 ** math.comb(n, 2)


# 下界：2^(nC2)/n!
def calc_lower_bound(n):
    return calc_upper_bound(n) / math.factorial(n)


def main():
    MAX_N = 20
    assert MAX_N < len(number_of_distinct_graphs)
    n = list(range(MAX_N + 1))
    ub_list = [calc_upper_bound(x) for x in n]
    lb_list = [calc_lower_bound(x) for x in n]

    plt.plot(n, ub_list, label="upper bound", color="red", linewidth=1)
    plt.plot(n, lb_list, label="lower bound", color="green", linewidth=1)
    plt.plot(n, number_of_distinct_graphs[: MAX_N + 1], label="ditsinct graphs")

    plt.yscale("log")
    plt.title("Number of Distinct Graphs")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
